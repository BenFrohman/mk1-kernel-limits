# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Benjamin Stanley Frohman
"""Gram matrix of 4 points by compute-uncompute: exact, Aer shot simulator, and (optionally) IBM hardware.

One job of 6 circuits x 8192 shots; estimates for N = 256..8192 use the first N shots.
Usage: python hardware/run.py [--ibm]   (IBM needs IBM_QUANTUM_TOKEN)
"""
from __future__ import annotations

import datetime as dt
import json
import os
import sys
from pathlib import Path

import numpy as np
from qiskit import transpile
from qiskit.quantum_info import Statevector

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from mk1.circuits import kernel_circuit, pairs, points  # noqa: E402
from mk1.kernel import gram, kernel  # noqa: E402
from mk1.shots import SHOTS, estimates_from_bits, fit_loglog  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "results"
NMAX = max(SHOTS)


def zero_hits_from_bitstrings(bits):
    return np.array([b == "00" for b in bits])


def summarize(label, hits_by_pair, pts, meta):
    k = gram(pts)
    prs = pairs(len(pts))
    est = {n: [estimates_from_bits(hits_by_pair[q])[n] for q in range(len(prs))] for n in SHOTS}
    exact = [k[i, j] for i, j in prs]
    rms = [float(np.sqrt(np.mean((np.array(est[n]) - exact) ** 2))) for n in SHOTS]
    slope, _ = fit_loglog(SHOTS, rms)
    res = dict(label=label, meta=meta, pairs=prs, exact=exact,
               estimates={str(n): est[n] for n in SHOTS}, rms=rms, loglog_slope=slope)
    OUT.mkdir(exist_ok=True)
    (OUT / f"{label}.json").write_text(json.dumps(res, indent=1))
    print(label, "rms", [f"{r:.4f}" for r in rms], "slope", f"{slope:.3f}")
    return res


def main():
    pts = points()
    circs = [kernel_circuit(pts[i], pts[j]) for i, j in pairs(len(pts))]
    # exact check: P(00) of Qiskit circuit == numpy statevector kernel
    for (i, j), c in zip(pairs(len(pts)), circs):
        p00 = abs(Statevector(c.remove_final_measurements(inplace=False)).data[0]) ** 2
        assert abs(p00 - kernel(pts[i], pts[j])) < 1e-12, (i, j)
    print("qiskit statevector agrees with numpy kernel to 1e-12")

    from qiskit_aer import AerSimulator
    from qiskit_ibm_runtime import SamplerV2
    sim = AerSimulator(seed_simulator=11)
    r = SamplerV2(mode=sim).run(transpile(circs, sim), shots=NMAX).result()
    hits = [zero_hits_from_bitstrings(r[q].data.meas.get_bitstrings()) for q in range(len(circs))]
    summarize("aer_simulator", hits, pts, dict(backend="AerSimulator (seed 11)",
              date=dt.datetime.now(dt.timezone.utc).isoformat()))

    if "--ibm" in sys.argv:
        from qiskit_ibm_runtime import QiskitRuntimeService
        svc = QiskitRuntimeService(channel="ibm_quantum_platform",
                                   token=os.environ["IBM_QUANTUM_TOKEN"], instance="open-instance")
        be = svc.least_busy(operational=True, simulator=False)
        tc = transpile(circs, be, optimization_level=1, seed_transpiler=3)
        job = SamplerV2(mode=be).run(tc, shots=NMAX)
        print("submitted", be.name, job.job_id(), flush=True)
        res = job.result()
        hits = [zero_hits_from_bitstrings(res[q].data.meas.get_bitstrings()) for q in range(len(circs))]
        summarize("ibm_hardware", hits, pts, dict(backend=be.name, job_ids=[job.job_id()],
                  date=dt.datetime.now(dt.timezone.utc).isoformat(), shots=NMAX,
                  depth=[c.depth() for c in tc]))


if __name__ == "__main__":
    main()

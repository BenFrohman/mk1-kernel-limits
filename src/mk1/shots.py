# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Benjamin Stanley Frohman
"""Finite-shot estimation of K and the measured N^(-1/2) error scaling."""
from __future__ import annotations

import numpy as np

from .kernel import gram

SHOTS = (256, 512, 1024, 2048, 4096, 8192)


def estimates_from_bits(zero_hits: np.ndarray, shots=SHOTS) -> dict[int, float]:
    """zero_hits: boolean array of per-shot 'outcome == 00'; estimate from first N shots."""
    return {n: float(np.mean(zero_hits[:n])) for n in shots}


def fit_loglog(ns, errs) -> tuple[float, float]:
    """Least-squares slope and intercept of log(err) vs log(N)."""
    slope, icpt = np.polyfit(np.log(ns), np.log(errs), 1)
    return float(slope), float(icpt)


def binomial_study(points, reps: int = 400, seed: int = 1, shots=SHOTS):
    """RMS error of the off-diagonal Gram estimate vs N under exact binomial shot noise."""
    k = gram(points)
    iu = np.triu_indices(len(points), 1)
    p = k[iu]
    rng = np.random.default_rng(seed)
    rms = []
    for n in shots:
        est = rng.binomial(n, p, size=(reps, p.size)) / n
        rms.append(float(np.sqrt(np.mean((est - p) ** 2))))
    return list(shots), rms

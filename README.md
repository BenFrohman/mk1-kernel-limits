# mk1-kernel-limits

A two-qubit ZZ fidelity kernel, studied for what it is: a classically computable teaching artefact.

- `src/mk1/`: feature map (`zz` corrected, `legacy` defective), closed-form classical kernel, Qiskit circuits, shot-noise tools.
- `lean/`: Lean 4 / Mathlib proofs: fidelity-kernel symmetry, unit diagonal, bounds, Gram PSD; CNOT identities; the legacy map gives a product state and a product kernel (explicit 4x4 complex matrices). Standard axioms only (`lean/AxiomAudit.lean`).
- `hardware/run.py`: 4-point Gram matrix, 6 compute-uncompute circuits; Aer baseline and (with `--ibm`) one IBM Runtime job. Results in `results/`.
- `paper/mk1.tex`, `paper/mk1.pdf`: the note.

Scope: no SVM or kernel ridge model is trained, there is no quantum-advantage claim, and the general concentration and dequantisation results are cited, not proved.
Hardware: ibm_kingston, 2026-11-04, job dblpgrd8ft8s738ths20, no mitigation.

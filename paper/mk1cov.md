# PipelineHalt full-coverage audit — /tmp/mk1_audit.tex

Title: MK-1: an exactly simulated two-qubit ZZ-feature-map fidelity kernel,\\ with machine-checked kernel properties\\ and a finite-shot hardware check

Verdict: **HALT** · units 51 · classified 51/51 (100.0%)

Real build: 27 theorems across 2 modules, 8267 lake jobs

| status | count |
|---|---|
| verified | 5 |
| verified-audit | 0 |
| build-ok | 0 |
| build-mismatch | 0 |
| broken | 0 |
| open | 0 |
| silent | 19 |
| non-claim | 27 |

VERIFIED means every Lean reference resolves and depends only on propext / Classical.choice / Quot.sound. It does not mean the Lean statement says the same thing as the prose; OPEN and SILENT units are flags that need a human answer.

| id | line | kind | status | refs | notes | text |
|---|---|---|---|---|---|---|
| 5655280fcc | 4 | title | non-claim |  |  | MK-1: an exactly simulated two-qubit ZZ-feature-map fidelity kernel,\\ with machine-checked kernel properties\\ and a finite-shot hardware check |
| 8cd62e0437 | 11 | sentence | silent |  | mathematical content with no Lean mapping | MK-1 is a small, self-contained implementation of a quantum fidelity kernel on two qubits: a ZZ-type feature map $U(x)$, the compute--uncompute estimator $K(... |
| 81b008cf25 | 13 | sentence | non-claim |  |  | The construction is not new; it follows Havl\'{\i}\v{c}ek et al.~\cite{havlicek} and Schuld--Killoran~\cite{schuld}. |
| 0eeacdbff4 | 14 | sentence | silent |  | mathematical content with no Lean mapping | This note records exactly what the code computes, documents a defect in the original script (its ``entangling'' gate was a no-op, so the state is a product s... |
| 9e3c5ebb46 | 17 | sentence | silent |  | mathematical content with no Lean mapping | A small finite-shot study (6 circuits, $N=256$--$8192$) on a simulator and on one IBM device is reported. |
| 7d72350c4c | 18 | sentence | non-claim |  |  | No quantum advantage or new learning-theoretic claim is made, and no SVM is trained. |
| 0bfda8ecac | 21 | heading | non-claim |  |  | The construction |
| ac8a1af275 | 22 | sentence | non-claim |  |  | Qubit 0 is the first tensor factor and the CNOT control. |
| c4f4ad88f5 | 22 | sentence | silent |  | mathematical content with no Lean mapping | For $x=(x_0,x_1)\in\mathbb{R}^2$, \[ U(x)=\mathrm{CNOT}\,(I\otimes R_Z(2x_0x_1))\,\mathrm{CNOT}\,(R_Z(2x_0)\otimes R_Z(2x_1))\,(H\otimes H), \qquad R_Z(\thet... |
| 44394777ce | 26 | sentence | silent |  | mathematical content with no Lean mapping | \] Since $\mathrm{CNOT}(I\otimes R_Z(\theta))\mathrm{CNOT}=e^{-i\theta Z\otimes Z/2}$, writing basis states by signs $s\in\{\pm1\}^2$, \[ U(x)\|00\rangle=\tfr... |
| 0f3c1292a3 | 26 | display | silent |  | mathematical content with no Lean mapping | \[ U(x)\|00\rangle=\tfrac12\sum_{s} e^{-i\varphi(s,x)}\|s\rangle,\qquad \varphi(s,x)=x_0s_0+x_1s_1+x_0x_1s_0s_1, \] |
| 6056e12c38 | 34 | sentence | silent |  | mathematical content with no Lean mapping | \] This is one layer of the ZZ feature map of~\cite{havlicek} with the simplified pair coefficient $x_0x_1$ (their map uses $(\pi-x_0)(\pi-x_1)$ and two laye... |
| a8c28c5ca9 | 36 | sentence | non-claim |  |  | With one layer, and on two qubits, the kernel has the closed form above and is trivially classically computable; MK-1 is a teaching and testing artefact. |
| ee5000fe50 | 38 | sentence | silent |  | mathematical content with no Lean mapping | The closed form (\texttt{kernel\_closed\_form}) agrees with the statevector kernel to $10^{-12}$ in the tests ($1.3\times10^{-15}$ on the 16 pairs of Section... |
| 83d217f0f1 | 39 | sentence | non-claim |  |  | General results on when quantum kernels concentrate or can be dequantised~\cite{kubler,thanasilp,huang} are cited, not proved or formalised here. |
| b8dc4a4245 | 41 | heading | non-claim |  |  | A defect in the original script |
| d9f471c34e | 42 | sentence | silent |  | mathematical content with no Lean mapping | The original \texttt{mk1\_moving\_tower.py} (kept in \texttt{original/}) applied the middle $R_Z(2x_0x_1)$ to the \emph{control} qubit. |
| bf68f4a6f0 | 43 | sentence | silent |  | mathematical content with no Lean mapping | A diagonal gate on the control commutes with CNOT, so the two CNOTs cancel and no $Z\otimes Z$ phase is produced; the kernel becomes the product $\cos^2(\Del... |
| 84680c7192 | 44 | sentence | non-claim |  |  | The package keeps this as \texttt{variant="legacy"} for reproducibility and uses the corrected map by default. |
| 0384c5460d | 45 | sentence | verified | MK1.cnot_onControl_cnot, MK1.phantom_entangler, MK1.cnot_onTarget_cnot | MK1.cnot_onControl_cnot [theorem] axioms: propext, Classical.choice, Quot.sound; MK1.phantom_entangler [theorem] axioms: propext, Classical.choice, Quot.sound; MK1.cnot_onTarget_cnot [theorem] axioms: propext, Classical.choice, Quot.sound | Both facts ($\mathrm{CNOT}(D\otimes I)\mathrm{CNOT}=D\otimes I$ and the $Z\otimes Z$ phase for a target gate) are proved in Lean (\texttt{cnot\_onControl\_cn... |
| e7744424c8 | 46 | sentence | verified | MK1.legacyState_eq_prod, MK1.inner_prod2, MK1.kernel4_prod2, MK1.legacy_kernel_factors, MK1.kernel4_symm, MK1.kernel4_self | MK1.legacyState_eq_prod [theorem] axioms: propext, Classical.choice, Quot.sound; MK1.inner_prod2 [theorem] axioms: propext, Classical.choice, Quot.sound; MK1.kernel4_prod2 [theorem] axioms: propext, Classical.choice, Quot.sound; MK1.legacy_kernel_factors [theorem] axioms: propext, Classical.choice, Quot.sound; MK1.kernel4_symm [theorem] axioms: propext, Classical.choice, Quot.sound; MK1.kernel4_self [theorem] axioms: propext, Classical.choice, Quot.sound | \texttt{lean/MK1/Factorization.lean} proves on explicit $4\times4$ complex matrices that the legacy state is a product state (\texttt{legacyState\_eq\_prod}\... |
| fda27372ce | 51 | heading | non-claim |  |  | What is machine-checked |
| 9283185bd1 | 52 | sentence | silent |  | mathematical content with no Lean mapping | \texttt{lean/MK1/FidelityKernel.lean} defines $K_\psi(x,y)=\|\langle\psi(y),\psi(x)\rangle\|^2$ for any family $\psi$ in a complex inner product space and proves: |
| 4764939d8a | 54 | sentence | verified | MK1.fidelity_self, MK1.fidelity_symm, MK1.fidelity_nonneg, MK1.fidelity_le_one | MK1.fidelity_self [theorem] axioms: propext, Classical.choice, Quot.sound; MK1.fidelity_symm [theorem] axioms: propext, Classical.choice, Quot.sound; MK1.fidelity_nonneg [theorem] axioms: propext, Classical.choice, Quot.sound; MK1.fidelity_le_one [theorem] axioms: propext, Classical.choice, Quot.sound | \texttt{fidelity\_self}\lean{MK1.fidelity_self}, \texttt{fidelity\_symm}\lean{MK1.fidelity_symm}, \texttt{fidelity\_nonneg}\lean{MK1.fidelity_nonneg}, \textt... |
| c645cfe6ca | 55 | sentence | verified | MK1.norm_featureState, MK1.computeUncompute_eq_fidelity | MK1.norm_featureState [theorem] axioms: propext, Classical.choice, Quot.sound; MK1.computeUncompute_eq_fidelity [theorem] axioms: propext, Classical.choice, Quot.sound | \texttt{norm\_featureState}\lean{MK1.norm_featureState}, \texttt{computeUncompute\_eq\_fidelity}\lean{MK1.computeUncompute_eq_fidelity}: states $U(x)v$ from ... |
| 73feb234fb | 56 | sentence | verified | MK1.fidelity_gram_posSemidef | MK1.fidelity_gram_posSemidef [theorem] axioms: propext, Classical.choice, Quot.sound | \texttt{fidelity\_gram\_posSemidef}\lean{MK1.fidelity_gram_posSemidef}: for states in $\mathbb{C}^n$ and finitely many points, the matrix $[K(x_j,x_i)]$ is p... |
| 934398bf3e | 59 | sentence | non-claim |  |  | All are \texttt{sorry}-free; \texttt{AxiomAudit.lean} shows only \texttt{propext}, \texttt{Classical.choice}, \texttt{Quot.sound}; CI rebuilds and audits on ... |
| eb3e9e8c3b | 60 | sentence | non-claim |  |  | These are standard facts; the Lean development checks them, it does not establish anything new. |
| 4a7c80fc2e | 61 | sentence | non-claim |  |  | The Lean code does not model the specific gate angles beyond the CNOT identities and the legacy factorisation; the agreement of the numerical circuit with th... |
| 3a574f49c5 | 63 | heading | non-claim |  |  | What is tested numerically |
| 2c2b2416f5 | 64 | sentence | silent |  | mathematical content with no Lean mapping | The Python tests (CI, every push) check for both variants: unitarity of $U(x)$; $K(x,x)=1$; symmetry; $0\le K\le1$; compute--uncompute equals $\|\langle\psi(x... |
| aa4300c1e1 | 68 | heading | non-claim |  |  | Finite-shot estimation |
| a2f7b44292 | 68 | sentence | silent |  | mathematical content with no Lean mapping | \label{sec:shots} For four points (seed 7) the exact Gram matrix has off-diagonal entries $0.1246, 0.0840, 0.2525, 0.9176, 0.3283, 0.3298$ (minimum eigenvalu... |
| dc2a132cba | 70 | sentence | silent |  | mathematical content with no Lean mapping | Each is estimated as the frequency of $00$ in a compute--uncompute circuit, using the first $N$ of 8192 shots. |
| 0d59512ab4 | 70 | sentence | non-claim |  |  | RMS error over the six entries: |
| 13e440aeb4 | 71 | table-row | silent |  | mathematical content with no Lean mapping | $N$ & 256 & 512 & 1024 & 2048 & 4096 & 8192 & log--log slope |
| c04bc1319c | 72 | table-row | silent |  | mathematical content with no Lean mapping | Aer simulator (seed 11) & .0234 & .0105 & .0084 & .0102 & .0045 & .0044 & $-0.44$ |
| 6215fc5c1e | 73 | table-row | silent |  | mathematical content with no Lean mapping | IBM \texttt{ibm\_kingston} & .0373 & .0330 & .0299 & .0218 & .0213 & .0194 & $-0.20$ |
| 3b3c3c8865 | 76 | sentence | silent |  | mathematical content with no Lean mapping | A 400-repetition binomial study gives slope $-0.506$, consistent with $N^{-1/2}$. |
| 71c30bb6db | 76 | sentence | silent |  | mathematical content with no Lean mapping | On hardware the error levels off near $0.02$: device noise adds a bias that more shots do not remove. |
| c03dd8f97d | 77 | sentence | non-claim |  |  | Run: \texttt{ibm\_kingston}, 2026-11-04 20:42 UTC, one SamplerV2 job \texttt{dblpgrd8ft8s738ths20}, 6 circuits, 8192 shots, transpiled depth 18, no error mit... |
| e1e5d4c699 | 80 | heading | non-claim |  |  | Limitations |
| 0d0b71b04e | 81 | sentence | non-claim |  |  | Two qubits; one hardware job without mitigation; no SVM is trained in the package (the DUAL/DECIDE stages are illustrative); no claim of quantum advantage. |
| 924ad4821b | 82 | sentence | non-claim |  |  | For the limits of such kernels see~\cite{kubler}. |
| 2e778488e7 | 84 | sentence | non-claim |  |  | \begin{thebibliography}{9} \bibitem{havlicek} V.~Havl\'{\i}\v{c}ek, A.~D.~C\'orcoles, K.~Temme, A.~W.~Harrow, A.~Kandala, J.~M.~Chow, J.~M.~Gambetta, Supervi... |
| ea40cf4b16 | 87 | sentence | non-claim |  |  | \bibitem{schuld} M.~Schuld, N.~Killoran, Quantum machine learning in feature Hilbert spaces, \emph{Phys.\ Rev.\ Lett.} 122 (2019) 040504. |
| 1dd90f2748 | 88 | sentence | non-claim |  |  | \bibitem{kubler} J.~M.~K\"ubler, S.~Buchholz, B.~Sch\"olkopf, The inductive bias of quantum kernels, \emph{NeurIPS} 34 (2021). |
| a6b7f9bfdd | 89 | sentence | non-claim |  |  | \bibitem{thanasilp} S.~Thanasilp, S.~Wang, M.~Cerezo, Z.~Holmes, Exponential concentration in quantum kernel methods, \emph{Nat.\ Commun.} 15 (2024) 5200. |
| 93321a65ce | 90 | sentence | non-claim |  |  | \bibitem{huang} H.-Y.~Huang et al., Power of data in quantum machine learning, \emph{Nat.\ Commun.} 12 (2021) 2631. |
| 76dca4bfc6 | 91 | sentence | non-claim |  |  | \end{thebibliography} Code: \url{https://github.com/BenFrohman/mk1-kernel-limits}. |
| aa8a1aa244 | 92 | sentence | non-claim |  |  | License: Apache-2.0 (code), CC BY 4.0 (this note). |

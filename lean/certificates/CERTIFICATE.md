# Kernel certificate: mk1-kernel-limits

This file records a reproducible machine check of the Lean 4 development in this repository. Lean does not issue a signed "official" certificate. What is recorded here is the exact commit and toolchain, the complete `lake build` log, a scan for `sorry`/`admit`/`native_decide`/`axiom`, the `#print axioms` result for every theorem the build produces, and a replay of every module through Lean's kernel with the toolchain's `leanchecker`. Each check can be rerun with the command at the end.

| Item | Value |
|---|---|
| Repository | https://github.com/BenFrohman/mk1-kernel-limits |
| Certified commit | `67c0a94f3d16dce08f75cd7251ef3ed4c0e86c27` (branch `certs/kernel-certificate-787ef4d`) |
| Lean sources | identical to `main` at `787ef4dcf1bbd6f125856c0797f91d34a7fe1261`: no `.lean`, lakefile, manifest or toolchain file differs; the certified commit only adds CI and the scripts in `lean/certificates/tools/` |
| lean-toolchain | `leanprover/lean4:v4.30.0-rc1` |
| Lean | Lean (version 4.30.0-rc1, x86_64-unknown-linux-gnu, commit 714601baf118066cbf3f282361339c6d06665b2a, Release) |
| Mathlib | `0c154d67103f74be3a0f2c509f72ccbf5be9f2a7` (lake-manifest.json; inputRev `v4.30.0-rc1`) |
| Date (UTC) | 2026-11-17T02:14:34Z |
| CI run | https://github.com/BenFrohman/mk1-kernel-limits/actions/runs/44001447715 |
| `lake build` | `Build completed successfully (8267 jobs).` ([build.log](build.log)) |
| sorry / admit / native_decide / axiom scan | `RESULT: 0 hits` ([sorry-scan.txt](sorry-scan.txt)) |
| `#print axioms` | `AUDIT PASS: 27 theorems in 2 modules depend only on propext, Classical.choice, Quot.sound (or on no axioms)` ([axioms.txt](axioms.txt)) |
| Kernel replay (leanchecker) | `RESULT: 3 of 3 modules replayed through the kernel, 0 failures` ([leanchecker.txt](leanchecker.txt)) |

## What each check means

- **Build.** `lake build` of the default targets with the pinned toolchain. Mathlib comes from `lake exe cache get` (it is never rebuilt from source). The build elaborates every proof and sends each declaration to Lean's kernel.
- **Scan.** `certificates/tools/sorry_scan.py` strips comments and strings from every tracked `.lean` file and reports any `sorry`, `admit`, `native_decide` or `axiom` declaration. Result: RESULT: 0 hits.
- **Axioms.** `certificates/tools/gen_audit.py` imports all 3 built modules ([modules.txt](modules.txt)) and calls `Lean.collectAxioms`, the function behind `#print axioms`, on every theorem declared in them (27 theorems, auto-generated internal names excluded). `check_audit.py` fails unless each depends only on `propext`, `Classical.choice` and `Quot.sound`, or on no axioms. Raw output: [axioms.raw.txt](axioms.raw.txt); generated Lean file: [KernelCertificateAudit.lean.txt](KernelCertificateAudit.lean.txt).
- **Kernel replay.** checker: leanchecker source shipped with v4.30.0-rc1 (src/lean/LeanChecker.lean), prefix match -> exact match, run with lean --run. For each module, the checker loads the module's imports from their `.olean` files and replays every declaration of that module through the kernel. The stock checker treats its argument as a module-name prefix and replays all matching modules in parallel, which runs out of memory on a root module, so it is run once per module with exact matching (the one-line patch is printed in [leanchecker.txt](leanchecker.txt)). The checker's own documentation describes it as a tool to detect environment hacking, not an independent external verifier; imported Mathlib and core declarations are trusted from their `.olean` files.

## Scope

The axiom result says the listed theorems are proved from Lean's standard axioms. It does not by itself say what the theorems mean; read the statements in the sources. Conditional theorems remain conditional on their hypotheses.

Full `#print axioms` output (verbatim from `axioms.txt`):

```
'MK1.diagKron.eq_1' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.hh.eq_1' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.inner_prod2' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.kernel4_prod2' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.kernel4_self' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.kernel4_symm' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.ket00.eq_1' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.legacyState_eq_prod' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.legacy_kernel_factors' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.phantom_entangler' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.prod2.eq_1' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.cnot.eq_1' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.cnot_onControl_cnot' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.cnot_onTarget_cnot' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.computeUncompute_eq_fidelity' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.featureState.eq_1' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.fidelity.eq_1' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.fidelity_gram_posSemidef' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.fidelity_le_one' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.fidelity_nonneg' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.fidelity_self' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.fidelity_symm' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.inner_lift' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.lift.eq_1' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.norm_featureState' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.onControl.eq_1' depends on axioms: [propext, Classical.choice, Quot.sound]
'MK1.onTarget.eq_1' depends on axioms: [propext, Classical.choice, Quot.sound]
```

## Rebuild

```
git clone https://github.com/BenFrohman/mk1-kernel-limits.git && cd mk1-kernel-limits && git checkout 67c0a94f3d16dce08f75cd7251ef3ed4c0e86c27 && cd lean && lake exe cache get && lake build && python3 certificates/tools/sorry_scan.py && python3 certificates/tools/gen_audit.py /tmp/KernelCertificateAudit.lean /tmp/modules.txt && lake env lean /tmp/KernelCertificateAudit.lean > /tmp/axioms.raw.txt && python3 certificates/tools/check_audit.py /tmp/axioms.raw.txt | tail -n 1
```

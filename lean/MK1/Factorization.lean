/-
Copyright (c) 2026 Benjamin Stanley Frohman. Released under Apache 2.0.
Concrete 4×4 factorization theorem for the MK-1 legacy circuit.
-/
import Mathlib
import MK1.FidelityKernel

/-!
# Factorization of the legacy MK-1 map

Basis order `|00⟩,|01⟩,|10⟩,|11⟩`, qubit 0 = first factor = CNOT control. If the middle
phase sits on the control (`onControl`), then for *arbitrary* complex diagonal entries the
circuit `CNOT · (C ⊗ I) · CNOT · (A ⊗ B) · (H ⊗ H)` maps `|00⟩` to a product state, and the
compute–uncompute kernel is the product of two single-qubit kernels.
-/

noncomputable section
namespace MK1

open Matrix

/-- Product state `a ⊗ b` in `ℂ⁴`. -/
def prod2 (a b : Fin 2 → ℂ) : Fin 4 → ℂ := ![a 0 * b 0, a 0 * b 1, a 1 * b 0, a 1 * b 1]

/-- `diag(a0,a1) ⊗ diag(b0,b1)`. -/
def diagKron (a0 a1 b0 b1 : ℂ) : Matrix (Fin 4) (Fin 4) ℂ :=
  !![a0 * b0, 0, 0, 0; 0, a0 * b1, 0, 0; 0, 0, a1 * b0, 0; 0, 0, 0, a1 * b1]

/-- `H ⊗ H` with `h = 1/√2` left symbolic. -/
def hh (h : ℂ) : Matrix (Fin 4) (Fin 4) ℂ :=
  !![h*h, h*h, h*h, h*h; h*h, -(h*h), h*h, -(h*h); h*h, h*h, -(h*h), -(h*h); h*h, -(h*h), -(h*h), h*h]

/-- `|00⟩`. -/
def ket00 : Fin 4 → ℂ := ![1, 0, 0, 0]

/-- Legacy circuit applied to `|00⟩`, with control phase `diag(c0,c1)`. -/
def legacyState (h a0 a1 b0 b1 c0 c1 : ℂ) : Fin 4 → ℂ :=
  (cnot * onControl c0 c1 * cnot * diagKron a0 a1 b0 b1 * hh h) *ᵥ ket00

/-- Two-qubit fidelity kernel on concrete vectors: `|⟨ψ y, ψ x⟩|²`. -/
noncomputable def kernel4 (u v : Fin 4 → ℂ) : ℝ := ‖star v ⬝ᵥ u‖ ^ 2

/-- One-qubit fidelity kernel. -/
noncomputable def kernel2 (u v : Fin 2 → ℂ) : ℝ := ‖star v ⬝ᵥ u‖ ^ 2

/-- **Legacy state is a product state** (for any diagonal phases). -/
theorem legacyState_eq_prod (h a0 a1 b0 b1 c0 c1 : ℂ) :
    legacyState h a0 a1 b0 b1 c0 c1 = prod2 ![h * (c0 * a0), h * (c1 * a1)] ![h * b0, h * b1] := by
  unfold legacyState
  rw [cnot_onControl_cnot]
  ext i
  fin_cases i <;>
    simp [prod2, onControl, diagKron, hh, ket00, Matrix.mulVec, dotProduct, Matrix.mul_apply,
      Fin.sum_univ_four] <;> ring

/-- Inner products of product states factor. -/
theorem inner_prod2 (a b c d : Fin 2 → ℂ) :
    star (prod2 c d) ⬝ᵥ prod2 a b = (star c ⬝ᵥ a) * (star d ⬝ᵥ b) := by
  simp [prod2, dotProduct, Fin.sum_univ_four, Fin.sum_univ_two]; ring

/-- The fidelity kernel of product states is the product of single-qubit kernels. -/
theorem kernel4_prod2 (a b c d : Fin 2 → ℂ) :
    kernel4 (prod2 a b) (prod2 c d) = kernel2 a c * kernel2 b d := by
  unfold kernel4 kernel2; rw [inner_prod2, norm_mul, mul_pow]

/-- **Factorization theorem.** With the phase on the CNOT control, the MK-1 compute–uncompute
kernel between inputs with phases `(a,b,c)` and `(a',b',c')` is a product of one-qubit kernels. -/
theorem legacy_kernel_factors (h a0 a1 b0 b1 c0 c1 a0' a1' b0' b1' c0' c1' : ℂ) :
    kernel4 (legacyState h a0 a1 b0 b1 c0 c1) (legacyState h a0' a1' b0' b1' c0' c1') =
      kernel2 ![h * (c0 * a0), h * (c1 * a1)] ![h * (c0' * a0'), h * (c1' * a1')] *
      kernel2 ![h * b0, h * b1] ![h * b0', h * b1'] := by
  rw [legacyState_eq_prod, legacyState_eq_prod, kernel4_prod2]

/-- Symmetry of the concrete kernel. -/
theorem kernel4_symm (u v : Fin 4 → ℂ) : kernel4 u v = kernel4 v u := by
  unfold kernel4
  have : star u ⬝ᵥ v = star (star v ⬝ᵥ u) := by
    simp [dotProduct, star_sum, mul_comm]
  rw [this, norm_star]

/-- Unit diagonal of the concrete kernel for unit vectors. -/
theorem kernel4_self (u : Fin 4 → ℂ) (hu : star u ⬝ᵥ u = 1) : kernel4 u u = 1 := by
  unfold kernel4; rw [hu]; simp

/-- **Phantom entangler**: `CNOT · (Rz ⊗ I) · CNOT = Rz ⊗ I` for any diagonal gate on the control. -/
theorem phantom_entangler (a b : ℂ) : cnot * onControl a b * cnot = onControl a b :=
  cnot_onControl_cnot a b

end MK1
end

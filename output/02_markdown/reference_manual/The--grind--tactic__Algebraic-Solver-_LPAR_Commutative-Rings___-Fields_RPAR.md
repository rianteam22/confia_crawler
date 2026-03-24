[←16.7. Linear Integer Arithmetic](The--grind--tactic/Linear-Integer-Arithmetic/#cutsat "16.7. Linear Integer Arithmetic")[16.9. Linear Arithmetic Solver→](The--grind--tactic/Linear-Arithmetic-Solver/#grind-linarith "16.9. Linear Arithmetic Solver")
#  16.8. Algebraic Solver (Commutative Rings, Fields)[🔗](find/?domain=Verso.Genre.Manual.section&name=grind-ring "Permalink")
The `ring` solver in `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` is inspired by Gröbner basis computation procedures and term rewriting completion. It views multivariate polynomials as rewriting rules. For example, the polynomial equality `x * y + x - 2 = 0` is treated as a rewriting rule `x * y ↦ -x + 2`. It uses superposition to ensure the rewriting system is confluent.
The following examples demonstrate goals that can be decided by the `ring` solver. In these examples, the `Lean` and `Lean.Grind` namespaces are open:
`[open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Lean Grind `Commutative Rings
`example [[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α] (x : α) : (x + 1) * (x - 1) = x ^ 2 - 1 := byα:Type u_1inst✝:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") αx:α⊢ [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 1[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 1   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("PYBwpgdgBAMmCGEB0BxATgSwgEwFC7AA94BbEAGzCgG0BhYEkgJSwHMpBG4AF0oAKQqAC5OASiF8BAaigBGMQCoJUALSyxAXigCAelABMK2UM0AjAJ64oUVphxA"\))
Ring Characteristics
The solver “knows” that `16*16 = 0` because the [ring characteristic](https://en.wikipedia.org/wiki/Characteristic_%28algebra%29) (that is, the minimum number of copies of the multiplicative identity that sum to the additive identity) is `256`, which is provided by the `[IsCharP](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___IsCharP___mk "Documentation for Lean.Grind.IsCharP")` instance.
`example [[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α] [[IsCharP](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___IsCharP___mk "Documentation for Lean.Grind.IsCharP") α 256] (x : α) :     (x + 16)*(x - 16) = x^2 := byα:Type u_1inst✝¹:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") αinst✝:[IsCharP](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___IsCharP___mk "Documentation for Lean.Grind.IsCharP") α 256x:α⊢ [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 16[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 16[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("PYBwpgdgBAMmCGEB0BxATgSwgEwFC7AA94BbEAGzCgG0BhYEkgJSwHMpBG4AF0aBJAZ1oALeGgAKnKACYArADYeACkJQAXJwCUa3FF1RlUANRQAjHI0AqAwFpT5qAF4ohAHpS1TgEYBPHVFaYOEA"\))
Standard Library Types
Types in the standard library are supported by the solver out of the box. `UInt8` is a commutative ring with characteristic `256`, and thus has instances of `[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")` and `[IsCharP](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___IsCharP___mk "Documentation for Lean.Grind.IsCharP") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") 256`.
`example (x : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : (x + 16) * (x - 16) = x ^ 2 := byx:[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")⊢ [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 16[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 16[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("PYBwpgdgBAMmCGEB0BxATgSwgEwFC7AA94BbEAGzCgApCoAuKAVQEkIAXADgEoGa6A1FACMANl4AqflAC0I8VAC8UOgD0oAJgbKARgE9cUKAHNMOIA"\))
More Commutative Ring Proofs
The axioms of a commutative ring are sufficient to prove these statements.
`example [[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α] (a b c : α) :     a + b + c = 3 →     a ^ 2 + b ^ 2 + c ^ 2 = 5 →     a ^ 3 + b ^ 3 + c ^ 3 = 7 →     a ^ 4 + b ^ 4 = 9 - c ^ 4 := byα:Type u_1inst✝:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") αa:αb:αc:α⊢ a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 3 → a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 5 → a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 3 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 3 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 3 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 7 → a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 9 [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") c [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 ``example [[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α] (x y : α) :     x ^ 2 * y = 1 →     x * y ^ 2 = y →     y * x = 1 := byα:Type u_1inst✝:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") αx:αy:α⊢ x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1 → x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y → y [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("PYBwpgdgBAMmCGEB0BxATgSwgEwFC7AA94BbEAGzCgG0BhYEkgJSwHMpBG4AF0oAKeKACMoAYygAuTgEoJuKPKgCA1EKgqxAXigBmKICTCOQoEA9KACY1q0xfVRrULQFZ9h+SZ2Xhp3be8OoAOwuCop2UAAsnmGRWgCcUAC0otESWoIAnoasmDj4RKQUVHQMzGycPLyEUOkS0rIhVfYAVNX+AIzBClUtNfZaNQYhNS1VWh3iaZny2VjYQA"\))
Characteristic Zero
`ring` proves that `a + 1 = 2 + a` is unsatisfiable because the characteristic is known to be 0.
`example [[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α] [[IsCharP](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___IsCharP___mk "Documentation for Lean.Grind.IsCharP") α 0] (a : α) :     a + 1 = 2 + a → [False](Basic-Propositions/Truth/#False "Documentation for False") := byα:Type u_1inst✝¹:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") αinst✝:[IsCharP](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___IsCharP___mk "Documentation for Lean.Grind.IsCharP") α 0a:α⊢ a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a → [False](Basic-Propositions/Truth/#False "Documentation for False")   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("PYBwpgdgBAMmCGEB0BxATgSwgEwFC7AA94BbEAGzCgG0BhYEkgJSwHMpBG4AF0aBJAZ1oALeGgAKnKAAYeACnhQAXJwCUS3FE1QFAaigBGKAF4oAJih6FgJMIoAMXjl+VRSYBGATw1RWmHEA"\))
Inferred Characteristic
Even when the characteristic is not initially known, when `grind` discovers that `n = 0` for some numeral `n`, it makes inferences about the characteristic:
`example [[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α] (a b c : α)     (h₁ : a + 6 = a) (h₂ : c = c + 9) (h : b + 3*c = 0) :     27*a + b = 0 := byα:Type u_1inst✝:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") αa:αb:αc:αh₁:a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 6 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ah₂:c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") c [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 9h:b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 3 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ 27 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("PYBwpgdgBAMmCGEB0BxATgSwgEwFC7AA94BbEAGzCgG0BhYEkgJSwHMpBG4AF0oAKeKACMoAYygAuTgEpcUOXwAWgQIIJUAQGooANigBeNVMWAgglVj9YzQE5DvBauGaAzACozUAAyHxs+QCYA7M4aQnoeEvqCAJ4+rJg4QA"\))
##  16.8.1. Solver Type Classes[🔗](find/?domain=Verso.Genre.Manual.section&name=grind-ring-classes "Permalink")
Users can enable the `ring` solver for their own types by providing instances of the following [type classes](Type-Classes/#--tech-term-type-class), all in the `Lean.Grind` namespace:
  * `[Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring")`
  * `[Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring")`
  * `[CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring")`
  * `[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing")`
  * `[IsCharP](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___IsCharP___mk "Documentation for Lean.Grind.IsCharP")`
  * `[AddRightCancel](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___AddRightCancel___mk "Documentation for Lean.Grind.AddRightCancel")`
  * `[NoNatZeroDivisors](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___NoNatZeroDivisors___mk "Documentation for Lean.Grind.NoNatZeroDivisors")`
  * `[Field](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Field___mk "Documentation for Lean.Grind.Field")`


The algebraic solvers will self-configure depending on the availability of these instances, so not all need to be provided. The capabilities of the algebraic solvers will, of course, degrade when some are not available.
The Lean standard library contains the applicable instances for the types defined in the standard library. By providing these instances, other libraries can also enable `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")`'s `ring` solver. For example, the Mathlib `CommRing` type class implements `Lean.Grind.CommRing` to ensure the `ring` solver works out-of-the-box.
###  16.8.1.1. Algebraic Structures[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--grind--tactic--Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_--Solver-Type-Classes--Algebraic-Structures "Permalink")
To enable the algebraic solver, a type should have an instance of the most specific possible algebraic structure that the solver supports. In order of increasing specificity, that is `[Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring")`, `[Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring")`, `[CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring")`, `[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing")`, and `[Field](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Field___mk "Documentation for Lean.Grind.Field")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Grind.Semiring.pow_zero "Permalink")type class
```


Lean.Grind.Semiring.{u} (α : Type u) : Type u


Lean.Grind.Semiring.{u} (α : Type u) :
  Type u


```

A semiring, i.e. a type equipped with addition, multiplication, and a map from the natural numbers, satisfying appropriate compatibilities.
Use `Ring` instead if the type also has negation, `CommSemiring` if the multiplication is commutative, or `CommRing` if the type has negation and multiplication is commutative.
#  Instance Constructor

```
[Lean.Grind.Semiring.mk](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring.mk").{u}
```

#  Extends
  * `[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") α`
  * `[Mul](Type-Classes/Basic-Classes/#Mul___mk "Documentation for Mul") α`


#  Methods

```
add : α → α → α
```

Inherited from 
  1. `[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") α`
  2. `[Mul](Type-Classes/Basic-Classes/#Mul___mk "Documentation for Mul") α`



```
mul : α → α → α
```

Inherited from 
  1. `[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") α`
  2. `[Mul](Type-Classes/Basic-Classes/#Mul___mk "Documentation for Mul") α`



```
natCast : [NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast") α
```

In every semiring there is a canonical map from the natural numbers to the semiring, providing the values of `0` and `1`. Note that this function need not be injective.

```
ofNat : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") α n
```

Natural number numerals in the semiring. The field `ofNat_eq_natCast` ensures that these are (propositionally) equal to the values of `natCast`.

```
nsmul : [SMul](Type-Classes/Basic-Classes/#SMul___mk "Documentation for SMul") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") α
```

Scalar multiplication by natural numbers.

```
npow : [HPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow") α [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") α
```

Exponentiation by a natural number.

```
add_zero : ∀ (a : α), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
```

Zero is the right identity for addition.

```
add_comm : ∀ (a b : α), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a
```

Addition is commutative.

```
add_assoc : ∀ (a b c : α), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")
```

Addition is associative.

```
mul_assoc : ∀ (a b c : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")
```

Multiplication is associative.

```
mul_one : ∀ (a : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") 1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
```

One is the right identity for multiplication.

```
one_mul : ∀ (a : α), 1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
```

One is the left identity for multiplication.

```
left_distrib : ∀ (a b c : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c
```

Left distributivity of multiplication over addition.

```
right_distrib : ∀ (a b c : α), [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c
```

Right distributivity of multiplication over addition.

```
zero_mul : ∀ (a : α), 0 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
```

Zero is right absorbing for multiplication.

```
mul_zero : ∀ (a : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
```

Zero is left absorbing for multiplication.

```
pow_zero : ∀ (a : α), a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1
```

The zeroth power of any element is one.

```
pow_succ : ∀ (a : α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") n [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a
```

The successor power law for exponentiation.

```
ofNat_succ : ∀ (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1
```

Numerals are consistently defined with respect to addition.

```
ofNat_eq_natCast : ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ↑n
```

Numerals are consistently defined with respect to the canonical map from natural numbers.

```
nsmul_eq_natCast_mul : ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α), n • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ↑n [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a
```

Multiplying by a numeral is consistently defined with respect to the canonical map from natural numbers.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Grind.CommSemiring.mk "Permalink")type class
```


Lean.Grind.CommSemiring.{u} (α : Type u) : Type u


Lean.Grind.CommSemiring.{u} (α : Type u) :
  Type u


```

A commutative semiring, i.e. a semiring with commutative multiplication.
Use `CommRing` if the type has negation.
#  Instance Constructor

```
[Lean.Grind.CommSemiring.mk](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring.mk").{u}
```

#  Extends
  * `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`


#  Methods

```
add : α → α → α
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
mul : α → α → α
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
natCast : [NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast") α
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
ofNat : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") α n
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
nsmul : [SMul](Type-Classes/Basic-Classes/#SMul___mk "Documentation for SMul") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") α
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
npow : [HPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow") α [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") α
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
add_zero : ∀ (a : α), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
add_comm : ∀ (a b : α), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
add_assoc : ∀ (a b c : α), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
mul_assoc : ∀ (a b c : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
mul_one : ∀ (a : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") 1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
one_mul : ∀ (a : α), 1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
left_distrib : ∀ (a b c : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
right_distrib : ∀ (a b c : α), [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
zero_mul : ∀ (a : α), 0 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
mul_zero : ∀ (a : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
pow_zero : ∀ (a : α), a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
pow_succ : ∀ (a : α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") n [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
ofNat_succ : ∀ (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
ofNat_eq_natCast : ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ↑n
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
nsmul_eq_natCast_mul : ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α), n • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ↑n [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`



```
mul_comm : ∀ (a b : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a
```

Multiplication is commutative.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Grind.Ring.mk "Permalink")type class
```


Lean.Grind.Ring.{u} (α : Type u) : Type u


Lean.Grind.Ring.{u} (α : Type u) : Type u


```

A ring, i.e. a type equipped with addition, negation, multiplication, and a map from the integers, satisfying appropriate compatibilities.
Use `CommRing` if the multiplication is commutative.
#  Instance Constructor

```
[Lean.Grind.Ring.mk](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring.mk").{u}
```

#  Extends
  * `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  * `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  * `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`


#  Methods

```
add : α → α → α
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
mul : α → α → α
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
natCast : [NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast") α
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
ofNat : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") α n
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
nsmul : [SMul](Type-Classes/Basic-Classes/#SMul___mk "Documentation for SMul") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") α
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
npow : [HPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow") α [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") α
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
add_zero : ∀ (a : α), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
add_comm : ∀ (a b : α), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
add_assoc : ∀ (a b c : α), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
mul_assoc : ∀ (a b c : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
mul_one : ∀ (a : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") 1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
one_mul : ∀ (a : α), 1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
left_distrib : ∀ (a b c : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
right_distrib : ∀ (a b c : α), [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
zero_mul : ∀ (a : α), 0 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
mul_zero : ∀ (a : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
pow_zero : ∀ (a : α), a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
pow_succ : ∀ (a : α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") n [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
ofNat_succ : ∀ (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
ofNat_eq_natCast : ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ↑n
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
nsmul_eq_natCast_mul : ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α), n • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ↑n [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
neg : α → α
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
sub : α → α → α
```

Inherited from 
  1. `[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α`
  2. `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") α`
  3. `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") α`



```
intCast : [IntCast](Coercions/Coercing-Between-Types/#IntCast___mk "Documentation for IntCast") α
```

In every ring there is a canonical map from the integers to the ring.

```
zsmul : [SMul](Type-Classes/Basic-Classes/#SMul___mk "Documentation for SMul") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") α
```

Scalar multiplication by integers.

```
neg_add_cancel : ∀ (a : α), [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
```

Negation is the left inverse of addition.

```
sub_eq_add_neg : ∀ (a b : α), a [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")b
```

Subtraction is addition of the negative.

```
neg_zsmul : ∀ (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) (a : α), [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")i • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")(i • a)
```

Scalar multiplication by the negation of an integer is the negation of scalar multiplication by that integer.

```
zsmul_natCast_eq_nsmul : ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α), ↑n • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n • a
```

Scalar multiplication by natural numbers is consistent with scalar multiplication by integers.

```
intCast_ofNat : ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), ↑([OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") n) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") n
```

The canonical map from the integers is consistent with the canonical map from the natural numbers.

```
intCast_neg : ∀ (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")), ↑[(](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")[-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")i[)](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")↑i
```

The canonical map from the integers is consistent with negation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Grind.CommRing.mk "Permalink")type class
```


Lean.Grind.CommRing.{u} (α : Type u) : Type u


Lean.Grind.CommRing.{u} (α : Type u) :
  Type u


```

A commutative ring, i.e. a ring with commutative multiplication.
#  Instance Constructor

```
[Lean.Grind.CommRing.mk](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing.mk").{u}
```

#  Extends
  * `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  * `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`


#  Methods

```
add : α → α → α
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
mul : α → α → α
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
natCast : [NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast") α
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
ofNat : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") α n
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
nsmul : [SMul](Type-Classes/Basic-Classes/#SMul___mk "Documentation for SMul") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") α
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
npow : [HPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow") α [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") α
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
add_zero : ∀ (a : α), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
add_comm : ∀ (a b : α), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
add_assoc : ∀ (a b c : α), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
mul_assoc : ∀ (a b c : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
mul_one : ∀ (a : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") 1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
one_mul : ∀ (a : α), 1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
left_distrib : ∀ (a b c : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
right_distrib : ∀ (a b c : α), [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
zero_mul : ∀ (a : α), 0 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
mul_zero : ∀ (a : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
pow_zero : ∀ (a : α), a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
pow_succ : ∀ (a : α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") n [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
ofNat_succ : ∀ (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
ofNat_eq_natCast : ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ↑n
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
nsmul_eq_natCast_mul : ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α), n • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ↑n [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
neg : α → α
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
sub : α → α → α
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
intCast : [IntCast](Coercions/Coercing-Between-Types/#IntCast___mk "Documentation for IntCast") α
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
zsmul : [SMul](Type-Classes/Basic-Classes/#SMul___mk "Documentation for SMul") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") α
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
neg_add_cancel : ∀ (a : α), [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
sub_eq_add_neg : ∀ (a b : α), a [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")b
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
neg_zsmul : ∀ (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) (a : α), [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")i • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")(i • a)
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
zsmul_natCast_eq_nsmul : ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α), ↑n • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n • a
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
intCast_ofNat : ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), ↑([OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") n) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") n
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
intCast_neg : ∀ (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")), ↑[(](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")[-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")i[)](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")↑i
```

Inherited from 
  1. `[Lean.Grind.Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring") α`
  2. `[Lean.Grind.CommSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring") α`



```
mul_comm : ∀ (a b : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a
```

Multiplication is commutative.
####  16.8.1.1.1. Fields[🔗](find/?domain=Verso.Genre.Manual.section&name=grind-ring-field "Permalink")
The `ring` solver also has support for `[Field](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Field___mk "Documentation for Lean.Grind.Field")`s. If a `[Field](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Field___mk "Documentation for Lean.Grind.Field")` instance is available, the solver preprocesses the term `a / b` into `a * b⁻¹`. It also rewrites every disequality `p ≠ 0` as the equality `p * p⁻¹ = 1`.
Fields and `grind`
This example requires its `[Field](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Field___mk "Documentation for Lean.Grind.Field")` instance:
`example [[Field](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Field___mk "Documentation for Lean.Grind.Field") α] (a : α) :     a ^ 2 = 0 →     a = 0 := byα:Type u_1inst✝:[Field](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Field___mk "Documentation for Lean.Grind.Field") αa:α⊢ a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("PYBwpgdgBAMmCGEB0BxATgSwgEwFC7AA94BbEAGzCgG0AxDMc7KQRuABdKACnigC5WAlH1xRRUHgD0oAJigBeKAAYogJMIRYnguW8FAIwCe6gOaYcQA"\))
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Grind.Field.toCommRing "Permalink")type class
```


Lean.Grind.Field.{u} (α : Type u) : Type u


Lean.Grind.Field.{u} (α : Type u) : Type u


```

A field is a commutative ring with inverses for all non-zero elements.
#  Instance Constructor

```
[Lean.Grind.Field.mk](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Field___mk "Documentation for Lean.Grind.Field.mk").{u}
```

#  Extends
  * `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  * `Inv α`
  * `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`


#  Methods

```
add : α → α → α
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
mul : α → α → α
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
natCast : [NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast") α
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
ofNat : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") α n
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
nsmul : [SMul](Type-Classes/Basic-Classes/#SMul___mk "Documentation for SMul") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") α
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
npow : [HPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow") α [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") α
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
add_zero : ∀ (a : α), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
add_comm : ∀ (a b : α), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
add_assoc : ∀ (a b c : α), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
mul_assoc : ∀ (a b c : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
mul_one : ∀ (a : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") 1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
one_mul : ∀ (a : α), 1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
left_distrib : ∀ (a b c : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
right_distrib : ∀ (a b c : α), [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
zero_mul : ∀ (a : α), 0 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
mul_zero : ∀ (a : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
pow_zero : ∀ (a : α), a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
pow_succ : ∀ (a : α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") n [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
ofNat_succ : ∀ (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
ofNat_eq_natCast : ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ↑n
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
nsmul_eq_natCast_mul : ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α), n • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ↑n [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
neg : α → α
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
sub : α → α → α
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
intCast : [IntCast](Coercions/Coercing-Between-Types/#IntCast___mk "Documentation for IntCast") α
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
zsmul : [SMul](Type-Classes/Basic-Classes/#SMul___mk "Documentation for SMul") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") α
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
neg_add_cancel : ∀ (a : α), [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
sub_eq_add_neg : ∀ (a b : α), a [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")b
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
neg_zsmul : ∀ (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) (a : α), [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")i • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")(i • a)
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
zsmul_natCast_eq_nsmul : ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α), ↑n • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n • a
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
intCast_ofNat : ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), ↑([OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") n) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") n
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
intCast_neg : ∀ (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")), ↑[(](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")[-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")i[)](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")↑i
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
mul_comm : ∀ (a b : α), a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
inv : α → α
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
div : α → α → α
```

Inherited from 
  1. `[Lean.Grind.CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α`
  2. `Inv α`
  3. `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") α`



```
zpow : [HPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow") α [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") α
```

An exponentiation operator.

```
div_eq_mul_inv : ∀ (a b : α), a [/](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv.hDiv") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b⁻¹
```

Division is multiplication by the inverse.

```
zero_ne_one : 0 ≠ 1
```

Zero is not equal to one: fields are non trivial.

```
inv_zero : 0⁻¹ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
```

The inverse of zero is zero. This is a "junk value" convention.

```
mul_inv_cancel : ∀ {a : α}, a ≠ 0 → a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a⁻¹ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1
```

The inverse of a non-zero element is a right inverse.

```
zpow_zero : ∀ (a : α), a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1
```

The zeroth power of any element is one.

```
zpow_succ : ∀ (a : α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")↑n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") ↑n [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a
```

The (n+1)-st power of any element is the element multiplied by the n-th power.

```
zpow_neg : ∀ (a : α) (n : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")), a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") [(](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")[-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")n[)](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [(](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") n[)](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")⁻¹
```

Raising to a negative power is the inverse of raising to the positive power.
###  16.8.1.2. Ring Characteristics[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--grind--tactic--Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_--Solver-Type-Classes--Ring-Characteristics "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Grind.IsCharP.mk "Permalink")type class
```


Lean.Grind.IsCharP.{u} (α : Type u) [[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α]
  (p : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : Prop


Lean.Grind.IsCharP.{u} (α : Type u)
  [[Lean.Grind.Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") α]
  (p : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : Prop


```

A ring `α` has characteristic `p` if `[OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") x = 0` iff `x % p = 0`.
Note that for `p = 0`, we have `x % p = x`, so this says that `[OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat")` is injective from `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` to `α`.
In the case of a semiring, we take the stronger condition that `[OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") x = [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") y` iff `x % p = y % p`.
#  Instance Constructor

```
[Lean.Grind.IsCharP.mk](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___IsCharP___mk "Documentation for Lean.Grind.IsCharP.mk").{u}
```

#  Methods

```
ofNat_ext_iff : ∀ {x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}, [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") y [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") x [%](Type-Classes/Basic-Classes/#HMod___mk "Documentation for HMod.hMod") p [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y [%](Type-Classes/Basic-Classes/#HMod___mk "Documentation for HMod.hMod") p
```

Two numerals in a semiring are equal iff they are congruent module `p` in the natural numbers.
###  16.8.1.3. Natural Number Zero Divisors[🔗](find/?domain=Verso.Genre.Manual.section&name=NoNatZeroDivisors "Permalink")
The class `NoNatZeroDivisors` is used to control coefficient growth. For example, the polynomial `2 * x * y + 4 * z = 0` is simplified to `x * y + 2 * z = 0`. It also used when processing disequalities.
Using `NoNatZeroDivisors`
In this example, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` relies on the `[NoNatZeroDivisors](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___NoNatZeroDivisors___mk "Documentation for Lean.Grind.NoNatZeroDivisors")` instance to simplify the goal:
`example [[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α] [[NoNatZeroDivisors](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___NoNatZeroDivisors___mk "Documentation for Lean.Grind.NoNatZeroDivisors") α] (a b : α) :     2 * a + 2 * b = 0 →     b ≠ -a → [False](Basic-Propositions/Truth/#False "Documentation for False") := byα:Type u_1inst✝¹:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") αinst✝:[NoNatZeroDivisors](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___NoNatZeroDivisors___mk "Documentation for Lean.Grind.NoNatZeroDivisors") αa:αb:α⊢ 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → b ≠ [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")a → [False](Basic-Propositions/Truth/#False "Documentation for False")   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
Without it, the proof fails:
`example [[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α] (a b : α) :     2 * a + 2 * b = 0 →     b ≠ -a → [False](Basic-Propositions/Truth/#False "Documentation for False") := byα:Type u_1inst✝:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") αa:αb:α⊢ 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → b ≠ [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")a → [False](Basic-Propositions/Truth/#False "Documentation for False")   ``grind` failed grindα:Type u_1inst:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") αa b:αh:2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0h_1:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")a⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")a
 
 
  * [eqc] False propositions
    * [prop] b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")a
 
  * [eqc] Equivalence classes
    * [eqc] {0, 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b}
 
  * [ring] Ring `α` 
    * [basis] Basis
      * [_] 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
    * [diseqs] Disequalities
      * [_] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
```
`grind` failed
grindα:Type u_1inst:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") αa b:αh:2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0h_1:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")a⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts

    * [prop] 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")a




  * [eqc] False propositions
    * [prop] b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")a


  * [eqc] Equivalence classes
    * [eqc] {0, 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b}


  * [ring] Ring `α`

    * [basis] Basis
      * [_] 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


    * [diseqs] Disequalities
      * [_] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0





```

[Live ↪](javascript:openLiveLink\("PYBwpgdgBAMmCGEB0BxATgSwgEwFC7AA94BbEAGzCgG0BhYEkgJSwHMpBG4AF0aA5YXvAAuALTBpgAEQwA3DAGdgaeZx4AKeFABGUAFycAlHtxRTUAExQAVFE0BqC9e1QAvFAAMUQEmEJszsAGRFAAtJpeUABi8OTyVLpuWgCevqyYOEA"\))
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Grind.NoNatZeroDivisors.mk "Permalink")type class
```


Lean.Grind.NoNatZeroDivisors.{u} (α : Type u) [[Lean.Grind.NatModule](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___NatModule___mk "Documentation for Lean.Grind.NatModule") α] :
  Prop


Lean.Grind.NoNatZeroDivisors.{u}
  (α : Type u) [[Lean.Grind.NatModule](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___NatModule___mk "Documentation for Lean.Grind.NatModule") α] :
  Prop


```

We say a module has no natural number zero divisors if `k ≠ 0` and `k * a = k * b` implies `a = b` (here `k` is a natural number and `a` and `b` are element of the module).
For a module over the integers this is equivalent to `k ≠ 0` and `k * a = 0` implies `a = 0`. (See the alternative constructor `NoNatZeroDivisors.mk'`, and the theorem `eq_zero_of_mul_eq_zero`.)
#  Instance Constructor

```
[Lean.Grind.NoNatZeroDivisors.mk](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___NoNatZeroDivisors___mk "Documentation for Lean.Grind.NoNatZeroDivisors.mk").{u}
```

#  Methods

```
no_nat_zero_divisors : ∀ (k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a b : α), k ≠ 0 → k • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k • b → a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b
```

If `k * a ≠ k * b` then `k ≠ 0` or `a ≠ b`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Grind.NoNatZeroDivisors.mk' "Permalink")def
```


Lean.Grind.NoNatZeroDivisors.mk'.{u_1} {α : Type u_1}
  [[Lean.Grind.IntModule](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___IntModule___mk "Documentation for Lean.Grind.IntModule") α]
  (eq_zero_of_mul_eq_zero :
    ∀ (k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α), k ≠ 0 → k • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0) :
  [Lean.Grind.NoNatZeroDivisors](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___NoNatZeroDivisors___mk "Documentation for Lean.Grind.NoNatZeroDivisors") α


Lean.Grind.NoNatZeroDivisors.mk'.{u_1}
  {α : Type u_1} [[Lean.Grind.IntModule](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___IntModule___mk "Documentation for Lean.Grind.IntModule") α]
  (eq_zero_of_mul_eq_zero :
    ∀ (k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α),
      k ≠ 0 → k • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0) :
  [Lean.Grind.NoNatZeroDivisors](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___NoNatZeroDivisors___mk "Documentation for Lean.Grind.NoNatZeroDivisors") α


```

Alternative constructor for `NoNatZeroDivisors` when we have an `IntModule`.
The `ring` module also performs case-analysis for terms `a⁻¹` on whether `a` is zero or not. In the following example, if `2*a` is zero, then `a` is also zero since we have `NoNatZeroDivisors α`, and all terms are zero and the equality hold. Otherwise, `ring` adds the equalities `a*a⁻¹ = 1` and `2*a*(2*a)⁻¹ = 1`, and closes the goal.
`example [[Field](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Field___mk "Documentation for Lean.Grind.Field") α] [[NoNatZeroDivisors](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___NoNatZeroDivisors___mk "Documentation for Lean.Grind.NoNatZeroDivisors") α] (a : α) :     1 / a + 1 / (2 * a) = 3 / (2 * a) := byα:Type u_1inst✝¹:[Field](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Field___mk "Documentation for Lean.Grind.Field") αinst✝:[NoNatZeroDivisors](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___NoNatZeroDivisors___mk "Documentation for Lean.Grind.NoNatZeroDivisors") αa:α⊢ 1 [/](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv.hDiv") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [/](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv.hDiv") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 3 [/](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv.hDiv") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
Without `NoNatZeroDivisors`, `grind` will perform case splits on numerals being zero as needed:
`example [[Field](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Field___mk "Documentation for Lean.Grind.Field") α] (a : α) : (2 * a)⁻¹ = a⁻¹ / 2 := byα:Type u_1inst✝:[Field](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Field___mk "Documentation for Lean.Grind.Field") αa:α⊢ [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")⁻¹ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a⁻¹ [/](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv.hDiv") 2 [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
In the following example, `ring` does not need to perform any case split because the goal contains the disequalities `y ≠ 0` and `w ≠ 0`.
`example [[Field](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Field___mk "Documentation for Lean.Grind.Field") α] {x y z w : α} :     x / y = z / w →     y ≠ 0 → w ≠ 0 →     x * w = z * y := byα:Type u_1inst✝:[Field](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Field___mk "Documentation for Lean.Grind.Field") αx:αy:αz:αw:α⊢ x [/](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv.hDiv") y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") z [/](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv.hDiv") w → y ≠ 0 → w ≠ 0 → x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") z [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") (splits := 0)All goals completed! 🐙 `
You can disable the `ring` solver using the option `grind -ring`.
`example [[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α] (x y : α) :     x ^ 2 * y = 1 →     x * y ^ 2 = y →     y * x = 1 := byα:Type u_1inst✝:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") αx:αy:α⊢ x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1 → x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y → y [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1   ``grind` failed grindα:Type u_1inst:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") αx y:αh:x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1h_1:x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") yh_2:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")y [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1
 
    * [prop] x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y
 
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")y [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1
 
 
  * [eqc] False propositions
    * [prop] y [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1
 
  * [eqc] Equivalence classes 
    * [eqc] {y, x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2}
 
    * [eqc] {1, x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y}
 
 
  * [ematch] E-matching patterns 
    * [thm] Nat.pow_pos: [[@](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")[HPow.hPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHPow] #2 #1]
 
    * [thm] Nat.div_pow_of_pos: [[@](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")[HPow.hPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHPow] #2 #1]
 
 
  * [linarith] Linarith assignment for `α` 
    * [assign] x := 2
 
    * [assign] y := 3
 
    * [assign] 「x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2」 := 4
 
    * [assign] 「y [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2」 := 6
 
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") -ringAll goals completed! 🐙 `
```
`grind` failed
grindα:Type u_1inst:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") αx y:αh:x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1h_1:x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") yh_2:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")y [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts

    * [prop] x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1


    * [prop] x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y


    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")y [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1




  * [eqc] False propositions
    * [prop] y [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1


  * [eqc] Equivalence classes

    * [eqc] {y, x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2}


    * [eqc] {1, x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y}




  * [ematch] E-matching patterns

    * [thm] Nat.pow_pos: [[@](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")[HPow.hPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHPow] #2 #1]


    * [thm] Nat.div_pow_of_pos: [[@](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")[HPow.hPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHPow] #2 #1]




  * [linarith] Linarith assignment for `α`

    * [assign] x := 2


    * [assign] y := 3


    * [assign] 「x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2」 := 4


    * [assign] 「y [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2」 := 6





```

####  16.8.1.3.1. Right-Cancellative Addition[🔗](find/?domain=Verso.Genre.Manual.section&name=AddRightCancel "Permalink")
The `ring` solver automatically embeds `CommSemiring`s into a `CommRing` envelope (using the construction `Lean.Grind.Ring.OfSemiring.Q`). However, the embedding is injective only when the `CommSemiring` implements the type class `AddRightCancel`. `Nat` is an example of a commutative semiring that implements `AddRightCancel`.
`example (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :     x ^ 2 * y = 1 →     x * y ^ 2 = y →     y * x = 1 := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1 → x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y → y [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Grind.AddRightCancel.mk "Permalink")type class
```


Lean.Grind.AddRightCancel.{u} (M : Type u) [[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") M] : Prop


Lean.Grind.AddRightCancel.{u} (M : Type u)
  [[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") M] : Prop


```

A type where addition is right-cancellative, i.e. `a + c = b + c` implies `a = b`.
#  Instance Constructor

```
[Lean.Grind.AddRightCancel.mk](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___AddRightCancel___mk "Documentation for Lean.Grind.AddRightCancel.mk").{u}
```

#  Methods

```
add_right_cancel : ∀ (a b c : M), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c → a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b
```

Addition is right-cancellative.
##  16.8.2. Resource Limits[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--grind--tactic--Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_--Resource-Limits "Permalink")
Gröbner basis computation can be very expensive. You can limit the number of steps performed by the `ring` solver using the option `grind (ringSteps := <num>)`
Limiting `ring` Steps
This example cannot be solved by performing at most 100 steps:
`example [[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α] [[IsCharP](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___IsCharP___mk "Documentation for Lean.Grind.IsCharP") α 0] (d t c : α) (d_inv PSO3_inv : α) :     d ^ 2 * (d + t - d * t - 2) * (d + t + d * t) = 0 →     -d ^ 4 * (d + t - d * t - 2) *       (2 * d + 2 * d * t - 4 * d * t ^ 2 + 2 * d * t^4 +       2 * d^2 * t^4 - c * (d + t + d * t)) = 0 →     d * d_inv = 1 →     (d + t - d * t - 2) * PSO3_inv = 1 →     t^2 = t + 1 := byα:Type u_1inst✝¹:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") αinst✝:[IsCharP](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___IsCharP___mk "Documentation for Lean.Grind.IsCharP") α 0d:αt:αc:αd_inv:αPSO3_inv:α⊢ d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 →   [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")         [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 4 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") c [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")       0 →     d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1 → [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1 → t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1   ``grind` failed grindα:Type u_1inst:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") αinst_1:[IsCharP](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___IsCharP___mk "Documentation for Lean.Grind.IsCharP") α 0d t c d_inv PSO3_inv:αh:d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0h_1:[-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")     [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 4 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") c [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")   0h_2:d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1h_3:[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1h_4:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] [IsCharP](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___IsCharP___mk "Documentation for Lean.Grind.IsCharP") α 0
 
    * [prop] d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
    * [prop] [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")         [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 4 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") c [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")       0
 
    * [prop] d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1
 
    * [prop] [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1
 
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1
 
 
  * [eqc] True propositions
    * [prop] [IsCharP](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___IsCharP___mk "Documentation for Lean.Grind.IsCharP") α 0
 
  * [eqc] False propositions
    * [prop] t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1
 
  * [eqc] Equivalence classes 
    * [eqc] {0,     [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")       [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 4 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") c [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub"),     d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")}
 
    * [eqc] {1, d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv, [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv}
 
 
  * [ematch] E-matching patterns 
    * [thm] Nat.pow_pos: [[@](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")[HPow.hPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHPow] #2 #1]
 
    * [thm] Nat.div_pow_of_pos: [[@](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")[HPow.hPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHPow] #2 #1]
 
 
  * [ring] Ring `α` 
    * [basis] Basis 
      * [_] t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")t [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
      * [_] 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")d_inv [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d_inv [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")d_inv [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d_inv [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
      * [_] d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")t [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
      * [_] d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
      * [_] t [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
      * [_] 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")d_inv [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
      * [_] 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")t [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")d_inv [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d_inv [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
 
    * [diseqs] Disequalities
      * [_] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
 
  * [limits] Thresholds reached
    * [limit] maximum number of ring steps has been reached, threshold: `(ringSteps := 100)`
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") (ringSteps := 100)All goals completed! 🐙 `
```
`grind` failed
grindα:Type u_1inst:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") αinst_1:[IsCharP](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___IsCharP___mk "Documentation for Lean.Grind.IsCharP") α 0d t c d_inv PSO3_inv:αh:d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0h_1:[-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")
    [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 4 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") c [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
  0h_2:d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1h_3:[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1h_4:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts

    * [prop] [IsCharP](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___IsCharP___mk "Documentation for Lean.Grind.IsCharP") α 0


    * [prop] d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


    * [prop] [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")
        [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 4 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") c [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
      0


    * [prop] d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1


    * [prop] [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1


    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1




  * [eqc] True propositions
    * [prop] [IsCharP](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___IsCharP___mk "Documentation for Lean.Grind.IsCharP") α 0


  * [eqc] False propositions
    * [prop] t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1


  * [eqc] Equivalence classes

    * [eqc] {0,
    [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")
      [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 4 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") c [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub"),
    d [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")}


    * [eqc] {1, d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv, [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv}




  * [ematch] E-matching patterns

    * [thm] Nat.pow_pos: [[@](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")[HPow.hPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHPow] #2 #1]


    * [thm] Nat.div_pow_of_pos: [[@](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")[HPow.hPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHPow] #2 #1]




  * [ring] Ring `α`

    * [basis] Basis

      * [_] t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")t [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


      * [_] 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")d_inv [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d_inv [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")d_inv [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d_inv [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


      * [_] d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")t [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


      * [_] d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


      * [_] t [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


      * [_] 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")d [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")d_inv [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d_inv [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


      * [_] 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")t [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")d_inv [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") PSO3_inv[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d_inv [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0




    * [diseqs] Disequalities
      * [_] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")t [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") t [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0




  * [limits] Thresholds reached
    * [limit] maximum number of ring steps has been reached, threshold: `(ringSteps := 100)`



```

[Live ↪](javascript:openLiveLink\("PYBwpgdgBAMmCGEB0BxATgSwgEyA"\))
The `ring` solver propagates equalities back to the `grind` core by normalizing terms using the computed Gröbner basis. In the following example, the equations `x ^ 2 * y = 1` and `x * y ^ 2 = y` imply the equalities `x = 1` and `y = 1`. Thus, the terms `x * y` and `1` are equal, and consequently `some (x * y) = some 1` by congruence.
`example (x y : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) :     x ^ 2 * y = 1 →     x * y ^ 2 = y →     [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (y * x) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 1 := byx:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")y:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1 → x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y → [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")y [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 1   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 ` [←16.7. Linear Integer Arithmetic](The--grind--tactic/Linear-Integer-Arithmetic/#cutsat "16.7. Linear Integer Arithmetic")[16.9. Linear Arithmetic Solver→](The--grind--tactic/Linear-Arithmetic-Solver/#grind-linarith "16.9. Linear Arithmetic Solver")

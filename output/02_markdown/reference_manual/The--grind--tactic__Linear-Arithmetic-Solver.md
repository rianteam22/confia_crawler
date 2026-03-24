[←16.8. Algebraic Solver (Commutative Rings, Fields)](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#grind-ring "16.8. Algebraic Solver \(Commutative Rings, Fields\)")[16.10. Annotating Libraries for grind→](The--grind--tactic/Annotating-Libraries-for--grind/#grind-annotation "16.10. Annotating Libraries for grind")
#  16.9. Linear Arithmetic Solver[🔗](find/?domain=Verso.Genre.Manual.section&name=grind-linarith "Permalink")
The `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` tactic includes a linear arithmetic solver for arbitrary types, called `linarith`, that is used for types not supported by [`cutsat`](The--grind--tactic/Linear-Integer-Arithmetic/#cutsat). Like the [`ring`](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#grind-ring) solver, it can be used with any type that has instances of certain type classes. It self-configures depending on the availability of these type classes, so it is not necessary to provide all of them to use the solver; however, its capabilities are increased by the availability of more instances. This solver is useful for reasoning about the real numbers, ordered vector spaces, and other types that can't be embedded into `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`.
The core functionality of `linarith` is a model-based solver for linear inequalities with integer coefficients. It can be disabled using the option `grind -linarith`.
Goals Decided by `linarith`
All of these examples rely on instances of the following ordering notation and `linarith` classes:
`[variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax") [[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") α] [[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") α] [Std.LawfulOrderLT α]  [Std.IsLinearOrder α] [variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax") [[IntModule](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___IntModule___mk "Documentation for Lean.Grind.IntModule") α] [[OrderedAdd](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___OrderedAdd___mk "Documentation for Lean.Grind.OrderedAdd") α] `
Integer modules (`[IntModule](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___IntModule___mk "Documentation for Lean.Grind.IntModule")`) are types with zero, addition, negation, subtraction, and scalar multiplication by integers that satisfy the expected properties of these operations. Linear orders (`Std.IsLinearOrder`) are orders in which any pair of elements is ordered, and `[OrderedAdd](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___OrderedAdd___mk "Documentation for Lean.Grind.OrderedAdd")` states that adding a constant to both sides preserves orderings.
`example {a b : α} : 2 • a + b ≥ b + a + a := byα:Type u_1inst✝⁵:[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") αinst✝⁴:[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") αinst✝³:Std.LawfulOrderLT αinst✝²:Std.IsLinearOrder αinst✝¹:[IntModule](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___IntModule___mk "Documentation for Lean.Grind.IntModule") αinst✝:[OrderedAdd](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___OrderedAdd___mk "Documentation for Lean.Grind.OrderedAdd") αa:αb:α⊢ 2 • a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b ≥ b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  example {a b : α} (h : a ≤ b) : 3 • a + b ≤ 4 • b := byα:Type u_1inst✝⁵:[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") αinst✝⁴:[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") αinst✝³:Std.LawfulOrderLT αinst✝²:Std.IsLinearOrder αinst✝¹:[IntModule](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___IntModule___mk "Documentation for Lean.Grind.IntModule") αinst✝:[OrderedAdd](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___OrderedAdd___mk "Documentation for Lean.Grind.OrderedAdd") αa:αb:αh:a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b⊢ 3 • a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 4 • b [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  example {a b c : α} :     a = b + c →     2 • b ≤ c →     2 • a ≤ 3 • c := byα:Type u_1inst✝⁵:[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") αinst✝⁴:[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") αinst✝³:Std.LawfulOrderLT αinst✝²:Std.IsLinearOrder αinst✝¹:[IntModule](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___IntModule___mk "Documentation for Lean.Grind.IntModule") αinst✝:[OrderedAdd](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___OrderedAdd___mk "Documentation for Lean.Grind.OrderedAdd") αa:αb:αc:α⊢ a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c → 2 • b [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") c → 2 • a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 3 • c   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  example {a b c d e : α} :     2 • a + b ≥ 0 →     b ≥ 0 → c ≥ 0 → d ≥ 0 → e ≥ 0 →     a ≥ 3 • c → c ≥ 6 • e → d - 5 • e ≥ 0 →     a + b + 3 • c + d + 2 • e < 0 →     [False](Basic-Propositions/Truth/#False "Documentation for False") := byα:Type u_1inst✝⁵:[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") αinst✝⁴:[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") αinst✝³:Std.LawfulOrderLT αinst✝²:Std.IsLinearOrder αinst✝¹:[IntModule](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___IntModule___mk "Documentation for Lean.Grind.IntModule") αinst✝:[OrderedAdd](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___OrderedAdd___mk "Documentation for Lean.Grind.OrderedAdd") αa:αb:αc:αd:αe:α⊢ 2 • a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b ≥ 0 →   b ≥ 0 → c ≥ 0 → d ≥ 0 → e ≥ 0 → a ≥ 3 • c → c ≥ 6 • e → d [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 5 • e ≥ 0 → a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 3 • c [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 • e [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 0 → [False](Basic-Propositions/Truth/#False "Documentation for False")   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAZRgEwFComApgOzgGSwEMcA6AcSmBzVQDciqiAjAGyzgG18BROQRuAAul3wAVAcM5JkpfEQDuAMwCurAPJRkWKGIlwu00gEkAzvmrEoGrVAn1GwFuy5GcMALIRkqjkK7XtLGQAQWRkO1QsAA8icGcAbyI4ZjgALgEAXzS4ACY4QCICOCSAamS4QFMiMtKSorSAXmSATzgAcyoadGjYsASklPT+LIAKAAtspMATImSASmyAZgLa0pSpgBZF/obmZrbqWi64jkSygGNswbTUfX0krbhSs8AkwivrvMKVuCeX/TfaqYXCmdUltGi9dh1IjFDnBjikzuEOAMsqlvrlFjUUpUAAxwZ7XMrY3GfCpwHGPODhQnkjhU1FJSoA4nks6VABsiw45PCAFo4ABWDkksl0+5VOCMs6lcKlX4cAA8pNxqIAYkRWCZESCwe1kEA"\))
Commutative Ring Goals Decided by `linarith`
For types that are commmutative rings (that is, types in which the multiplication operator is commutative) with `[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing")` instances, `linarith` has more capabilities.
`[variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax") [[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") R] [[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") R] [Std.IsLinearOrder R] [Std.LawfulOrderLT R] [variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax") [[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") R] [[OrderedRing](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___OrderedRing___mk "Documentation for Lean.Grind.OrderedRing") R] `
The `[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") R` instance allows `linarith` to perform basic normalization, such as identifying linear atoms `a * b` and `b * a`, and to account for scalar multiplication on both sides. The `[OrderedRing](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___OrderedRing___mk "Documentation for Lean.Grind.OrderedRing") R` instance allows the solver to support constants, because it has access to the fact that `(0 : R) < 1`.
`example (a b : R) (h : a * b ≤ 1) : b * 3 • a + 1 ≤ 4 := byR:Type u_1inst✝⁵:[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") Rinst✝⁴:[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") Rinst✝³:Std.IsLinearOrder Rinst✝²:Std.LawfulOrderLT Rinst✝¹:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") Rinst✝:[OrderedRing](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___OrderedRing___mk "Documentation for Lean.Grind.OrderedRing") Ra:Rb:Rh:a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 1⊢ b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") 3 • a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 4 [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  example (a b c d e f : R) :     2 • a + b ≥ 1 →     b ≥ 0 → c ≥ 0 → d ≥ 0 → e • f ≥ 0 →     a ≥ 3 • c →     c ≥ 6 • e • f → d - f * e * 5 ≥ 0 →     a + b + 3 • c + d + 2 • e • f < 0 →     [False](Basic-Propositions/Truth/#False "Documentation for False") := byR:Type u_1inst✝⁵:[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") Rinst✝⁴:[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") Rinst✝³:Std.IsLinearOrder Rinst✝²:Std.LawfulOrderLT Rinst✝¹:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") Rinst✝:[OrderedRing](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___OrderedRing___mk "Documentation for Lean.Grind.OrderedRing") Ra:Rb:Rc:Rd:Re:Rf:R⊢ 2 • a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b ≥ 1 →   b ≥ 0 →     c ≥ 0 →       d ≥ 0 → e • f ≥ 0 → a ≥ 3 • c → c ≥ 6 • e • f → d [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") f [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") e [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") 5 ≥ 0 → a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 3 • c [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 • e • f [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 0 → [False](Basic-Propositions/Truth/#False "Documentation for False")   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAZRgEwFComApgOzgGSwEMcA6AcSmBzVQDciqiAjAGyzgG18BROAJQC6XfABUBwzkmSkAkgGd81YlADyUZFigSu00viIB3AGYBXVus1QxE+o2At2XAMIQQIftQDmOzpa1YyJ44PkLoWAAeROBOABREcMxwAFwCAJRwsQAWKXAJAFSJcIAmRHAAjBmpSYUAzHCARAR5cADU5SVwACwpALyJAJ5wXlQ04VExHPFFAMZwyHAcxrn8lahwa3AATA1NrUmApkRtgEmEq+v7cAAMcIdwMweX13N3V/Pbi0/H600HdY0zH+u3OAANm2HEaiwecAAtHBFoUOIUAKxwd4nNYJXYtOA/G5YuatLaNMGwuAAHguVzRcAAYkRWPIOMlesw+ichtRkEA"\))
##  16.9.1. Supporting `linarith`[🔗](find/?domain=Verso.Genre.Manual.section&name=grind-linarith-classes "Permalink")
To add support for a new type to `linarith`, the first step is to implement `[IntModule](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___IntModule___mk "Documentation for Lean.Grind.IntModule")` if possible, or `[NatModule](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___NatModule___mk "Documentation for Lean.Grind.NatModule")` otherwise. Every `[Ring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Ring___mk "Documentation for Lean.Grind.Ring")` is already an `[IntModule](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___IntModule___mk "Documentation for Lean.Grind.IntModule")`, and every `[Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring")` is already a `[NatModule](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___NatModule___mk "Documentation for Lean.Grind.NatModule")`, so implementing one of those instances is also sufficient. Next, one of the order classes (`Std.IsPreorder`, `Std.IsPartialOrder`, or `Std.IsLinearOrder`) should be implemented. Typically an `IsPreorder` instance is enough when the context already includes a contradiction, but an `IsLinearOrder` instance is required in order to prove linear inequality goals. Additional features are enabled by implementing `[OrderedAdd](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___OrderedAdd___mk "Documentation for Lean.Grind.OrderedAdd")`, which expresses that the additive structure in a module is compatible with the order, and `[OrderedRing](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___OrderedRing___mk "Documentation for Lean.Grind.OrderedRing")`, which improves support for constants.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Grind.NatModule.mk "Permalink")type class
```


Lean.Grind.NatModule.{u} (M : Type u) : Type u


Lean.Grind.NatModule.{u} (M : Type u) :
  Type u


```

A module over the natural numbers, i.e. a type with zero, addition, and scalar multiplication by natural numbers, satisfying appropriate compatibilities.
Equivalently, an additive commutative monoid.
Use `[IntModule](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___IntModule___mk "Documentation for Lean.Grind.IntModule")` if the type has negation.
#  Instance Constructor

```
[Lean.Grind.NatModule.mk](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___NatModule___mk "Documentation for Lean.Grind.NatModule.mk").{u}
```

#  Extends
  * `AddCommMonoid M`


#  Methods

```
zero : M
```

Inherited from 
  1. `AddCommMonoid M`



```
add : M → M → M
```

Inherited from 
  1. `AddCommMonoid M`



```
add_zero : ∀ (a : M), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
```

Inherited from 
  1. `AddCommMonoid M`



```
add_comm : ∀ (a b : M), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a
```

Inherited from 
  1. `AddCommMonoid M`



```
add_assoc : ∀ (a b c : M), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")
```

Inherited from 
  1. `AddCommMonoid M`



```
nsmul : [SMul](Type-Classes/Basic-Classes/#SMul___mk "Documentation for SMul") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") M
```

Scalar multiplication by natural numbers.

```
zero_nsmul : ∀ (a : M), 0 • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
```

Scalar multiplication by zero is zero.

```
add_one_nsmul : ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : M), [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n • a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a
```

Scalar multiplication by a successor.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Grind.IntModule "Permalink")type class
```


Lean.Grind.IntModule.{u} (M : Type u) : Type u


Lean.Grind.IntModule.{u} (M : Type u) :
  Type u


```

A module over the integers, i.e. a type with zero, addition, negation, subtraction, and scalar multiplication by integers, satisfying appropriate compatibilities.
Equivalently, an additive commutative group.
#  Instance Constructor

```
[Lean.Grind.IntModule.mk](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___IntModule___mk "Documentation for Lean.Grind.IntModule.mk").{u}
```

#  Extends
  * `AddCommGroup M`


#  Methods

```
zero : M
```

Inherited from 
  1. `AddCommGroup M`



```
add : M → M → M
```

Inherited from 
  1. `AddCommGroup M`



```
add_zero : ∀ (a : M), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
```

Inherited from 
  1. `AddCommGroup M`



```
add_comm : ∀ (a b : M), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a
```

Inherited from 
  1. `AddCommGroup M`



```
add_assoc : ∀ (a b c : M), a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")
```

Inherited from 
  1. `AddCommGroup M`



```
neg : M → M
```

Inherited from 
  1. `AddCommGroup M`



```
sub : M → M → M
```

Inherited from 
  1. `AddCommGroup M`



```
neg_add_cancel : ∀ (a : M), [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
```

Inherited from 
  1. `AddCommGroup M`



```
sub_eq_add_neg : ∀ (a b : M), a [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")b
```

Inherited from 
  1. `AddCommGroup M`



```
nsmul : [SMul](Type-Classes/Basic-Classes/#SMul___mk "Documentation for SMul") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") M
```

Scalar multiplication by natural numbers.

```
zsmul : [SMul](Type-Classes/Basic-Classes/#SMul___mk "Documentation for SMul") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") M
```

Scalar multiplication by integers.

```
zero_zsmul : ∀ (a : M), 0 • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
```

Scalar multiplication by zero is zero.

```
one_zsmul : ∀ (a : M), 1 • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
```

Scalar multiplication by one is the identity.

```
add_zsmul : ∀ (n m : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) (a : M), [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") m[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n • a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") m • a
```

Scalar multiplication is distributive over addition in the integers.

```
zsmul_natCast_eq_nsmul : ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : M), ↑n • a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n • a
```

Scalar multiplication by natural numbers is consistent with scalar multiplication by integers.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Grind.OrderedAdd.mk "Permalink")type class
```


Lean.Grind.OrderedAdd.{u} (M : Type u) [[HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd") M M M] [[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") M]
  [Std.IsPreorder M] : Prop


Lean.Grind.OrderedAdd.{u} (M : Type u)
  [[HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd") M M M] [[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") M] [Std.IsPreorder M] :
  Prop


```

Addition is compatible with a preorder if `a ≤ b ↔ a + c ≤ b + c`.
#  Instance Constructor

```
[Lean.Grind.OrderedAdd.mk](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___OrderedAdd___mk "Documentation for Lean.Grind.OrderedAdd.mk").{u}
```

#  Methods

```
add_le_left_iff : ∀ {a b : M} (c : M), a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c
```

`a + c ≤ b + c` iff `a ≤ b`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Grind.OrderedRing.mul_lt_mul_of_pos_left "Permalink")type class
```


Lean.Grind.OrderedRing.{u} (R : Type u) [[Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") R] [[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") R] [[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") R]
  [Std.IsPreorder R] : Prop


Lean.Grind.OrderedRing.{u} (R : Type u)
  [[Semiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Semiring___mk "Documentation for Lean.Grind.Semiring") R] [[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") R] [[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") R]
  [Std.IsPreorder R] : Prop


```

A ring which is also equipped with a preorder is considered a strict ordered ring if addition, negation, and multiplication are compatible with the preorder, and `0 < 1`.
#  Instance Constructor

```
[Lean.Grind.OrderedRing.mk](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___OrderedRing___mk "Documentation for Lean.Grind.OrderedRing.mk").{u}
```

#  Extends
  * `[OrderedAdd](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___OrderedAdd___mk "Documentation for Lean.Grind.OrderedAdd") R`


#  Methods

```
add_le_left_iff : ∀ {a b : R} (c : R), a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c
```

Inherited from 
  1. `[OrderedAdd](The--grind--tactic/Linear-Arithmetic-Solver/#Lean___Grind___OrderedAdd___mk "Documentation for Lean.Grind.OrderedAdd") R`



```
zero_lt_one : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 1
```

In a strict ordered semiring, we have `0 < 1`.

```
mul_lt_mul_of_pos_left : ∀ {a b c : R}, a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b → 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") c → c [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") c [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b
```

In a strict ordered semiring, we can multiply an inequality `a < b` on the left by a positive element `0 < c` to obtain `c * a < c * b`.

```
mul_lt_mul_of_pos_right : ∀ {a b c : R}, a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b → 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") c → a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") c
```

In a strict ordered semiring, we can multiply an inequality `a < b` on the right by a positive element `0 < c` to obtain `a * c < b * c`.
[←16.8. Algebraic Solver (Commutative Rings, Fields)](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#grind-ring "16.8. Algebraic Solver \(Commutative Rings, Fields\)")[16.10. Annotating Libraries for grind→](The--grind--tactic/Annotating-Libraries-for--grind/#grind-annotation "16.10. Annotating Libraries for grind")

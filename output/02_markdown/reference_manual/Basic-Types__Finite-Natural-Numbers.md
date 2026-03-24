[←20.2. Integers](Basic-Types/Integers/#Int "20.2. Integers")[20.4. Fixed-Precision Integers→](Basic-Types/Fixed-Precision-Integers/#fixed-ints "20.4. Fixed-Precision Integers")
#  20.3. Finite Natural Numbers[🔗](find/?domain=Verso.Genre.Manual.section&name=Fin "Permalink")
For any [natural number](Basic-Types/Natural-Numbers/#--tech-term-natural-numbers) `n`, the `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` is a type that contains all the natural numbers that are strictly less than `n`. In other words, `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` has exactly `n` elements. It can be used to represent the valid indices into a list or array, or it can serve as a canonical `n`-element type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin "Permalink")structure
```


Fin (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : Type


Fin (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : Type


```

Natural numbers less than some upper bound.
In particular, a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` is a natural number `i` with the constraint that `i < n`. It is the canonical type with `n` elements.
#  Constructor

```
[Fin.mk](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.mk")
```

Creates a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` from `i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` and a proof that `i < n`.
#  Fields

```
val : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

The number that is strictly less than `n`.
`[Fin.val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val")` is a coercion, so any `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` can be used in a position where a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` is expected.

```
isLt : ↑self [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n
```

The number `val` is strictly less than the bound `n`.
`[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` is closely related to `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")`, `[UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")`, `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")`, `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`, and `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")`, which also represent finite non-negative integral types. However, these types are backed by bitvectors rather than by natural numbers, and they have fixed bounds. `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` is comparatively more flexible, but also less convenient for low-level reasoning. In particular, using bitvectors rather than proofs that a number is less than some power of two avoids needing to take care to avoid evaluating the concrete bound.
##  20.3.1. Run-Time Characteristics[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Finite-Natural-Numbers--Run-Time-Characteristics "Permalink")
Because `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` is a structure in which only a single field is not a proof, it is a [trivial wrapper](The-Type-System/Inductive-Types/#inductive-types-trivial-wrappers). This means that it is represented identically to the underlying natural number in compiled code.
##  20.3.2. Coercions and Literals[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Finite-Natural-Numbers--Coercions-and-Literals "Permalink")
There is a [coercion](Coercions/#--tech-term-coercion) from `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` to `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` that discards the proof that the number is less than the bound. In particular, this coercion is precisely the projection `[Fin.val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val")`. One consequence of this is that uses of `[Fin.val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val")` are displayed as coercions rather than explicit projections in proof states.
Coercing from `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` to `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`
A `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` can be used where a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` is expected:
``1`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") let one : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 3 := ⟨1, by⊢ 1 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3 [omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic")All goals completed! 🐙⟩; (one : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) `
```
1
```

Uses of `[Fin.val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val")` show up as coercions in proof states:
n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")i:[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n⊢ ↑i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n
[Live ↪](javascript:openLiveLink\("MQUwbghgNgBFIBcYHsB2IYC4YDECWqMAzFgLwyAX5AIwA0MARgJ4oC2IA5hIJfkA3DABRoM2AHIQEASiA"\))
Natural number literals may be used for `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` types, implemented as usual via an `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat")` instance. The `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat")` instance for `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` requires that the upper bound `n` is not zero, but does not check that the literal is less than `n`. If the literal is larger than the type can represent, the remainder when dividing it by `n` is used.
Numeric Literals for `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")`
If `n > 0`, then natural number literals can be used for `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n`:
`example : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 5 := 3 example : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 20 := 19 `
When the literal is greater than or equal to `n`, the remainder when dividing by `n` is used:
``2`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (5 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 3) `
```
2
```
``[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 0[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ([0, 1, 2, 3, 4, 5, 6] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 3)) `
```
[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 0[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

If Lean can't synthesize an instance of `[NeZero](Type-Classes/Basic-Classes/#NeZero___mk "Documentation for NeZero") n`, then there is no `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n)` instance:
`example : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 0 := `failed to synthesize instance of type class   [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 0) 0 numerals are polymorphic in Lean, but the numeral `0` cannot be used in a context where the expected type is   [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 0 due to the absence of the instance above  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`0 `
```
failed to synthesize instance of type class
  [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 0) 0
numerals are polymorphic in Lean, but the numeral `0` cannot be used in a context where the expected type is
  [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 0
due to the absence of the instance above

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```
`example (k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") k := `failed to synthesize instance of type class   [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") k) 0 numerals are polymorphic in Lean, but the numeral `0` cannot be used in a context where the expected type is   [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") k due to the absence of the instance above  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`0 `
```
failed to synthesize instance of type class
  [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") k) 0
numerals are polymorphic in Lean, but the numeral `0` cannot be used in a context where the expected type is
  [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") k
due to the absence of the instance above

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```

[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAueAxAlgO3gViQXngGYAoUSWBZdLAJgAZ94BGATmOIGJgA3MGeABS4qmIgEp2XXvwEBtOgBpmSmksJKALEuxKAbAF0k8ADJoAzgBdB1cWKA"\))
##  20.3.3. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Finite-Natural-Numbers--API-Reference "Permalink")
###  20.3.3.1. Construction[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Finite-Natural-Numbers--API-Reference--Construction "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.last "Permalink")def
```


Fin.last (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


Fin.last (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


```

The greatest value of `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n+1)`, namely `n`.
Examples:
  * `[Fin.last](Basic-Types/Finite-Natural-Numbers/#Fin___last "Documentation for Fin.last") 4 = (4 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 5)`
  * `([Fin.last](Basic-Types/Finite-Natural-Numbers/#Fin___last "Documentation for Fin.last") 0).[val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val") = (0 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.succ "Permalink")def
```


Fin.succ {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


Fin.succ {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


```

The successor, with an increased bound.
This differs from adding `1`, which instead wraps around.
Examples:
  * `(2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 3).[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ") = (3 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 4)`
  * `(2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 3) + 1 = (0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 3)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.pred "Permalink")def
```


Fin.pred {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) (h : i ≠ 0) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


Fin.pred {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd"))
  (h : i ≠ 0) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


```

The predecessor of a non-zero element of `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n+1)`, with the bound decreased.
Examples:
  * `(4 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 8).[pred](Basic-Types/Finite-Natural-Numbers/#Fin___pred "Documentation for Fin.pred") (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")) = (3 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 7)`
  * `(1 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 2).[pred](Basic-Types/Finite-Natural-Numbers/#Fin___pred "Documentation for Fin.pred") (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")) = (0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 1)`


###  20.3.3.2. Arithmetic[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Finite-Natural-Numbers--API-Reference--Arithmetic "Permalink")
Typically, arithmetic operations on `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` should be accessed using Lean's overloaded arithmetic notation, particularly via the instances `[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n)`, `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n)`, `[Mul](Type-Classes/Basic-Classes/#Mul___mk "Documentation for Mul") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n)`, `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n)`, and `[Mod](Type-Classes/Basic-Classes/#Mod___mk "Documentation for Mod") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n)`. Heterogeneous operators such as `[Fin.natAdd](Basic-Types/Finite-Natural-Numbers/#Fin___natAdd "Documentation for Fin.natAdd")` do not have corresponding heterogeneous instances (e.g. `[HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd")`) to avoid confusing type inference behavior.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.add "Permalink")def
```


Fin.add {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


Fin.add {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


```

Addition modulo `n`, usually invoked via the `+` operator.
Examples:
  * `(2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 8) + (2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 8) = (4 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 8)`
  * `(2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 3) + (2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 3) = (1 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 3)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.natAdd "Permalink")def
```


Fin.natAdd {m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") m) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") m[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


Fin.natAdd {m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") m) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") m[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


```

Adds a natural number to a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")`, increasing the bound.
This is a generalization of `[Fin.succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ")`.
`[Fin.addNat](Basic-Types/Finite-Natural-Numbers/#Fin___addNat "Documentation for Fin.addNat")` is a version of this function that takes its `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` parameter second.
Examples:
  * `[Fin.natAdd](Basic-Types/Finite-Natural-Numbers/#Fin___natAdd "Documentation for Fin.natAdd") 3 (5 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 8) = (8 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 11)`
  * `[Fin.natAdd](Basic-Types/Finite-Natural-Numbers/#Fin___natAdd "Documentation for Fin.natAdd") 1 (0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 8) = (1 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 9)`
  * `[Fin.natAdd](Basic-Types/Finite-Natural-Numbers/#Fin___natAdd "Documentation for Fin.natAdd") 1 (2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 8) = (3 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 9)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.addNat "Permalink")def
```


Fin.addNat {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") m[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


Fin.addNat {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n)
  (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") m[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


```

Adds a natural number to a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")`, increasing the bound.
This is a generalization of `[Fin.succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ")`.
`[Fin.natAdd](Basic-Types/Finite-Natural-Numbers/#Fin___natAdd "Documentation for Fin.natAdd")` is a version of this function that takes its `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` parameter first.
Examples:
  * `[Fin.addNat](Basic-Types/Finite-Natural-Numbers/#Fin___addNat "Documentation for Fin.addNat") (5 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 8) 3 = (8 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 11)`
  * `[Fin.addNat](Basic-Types/Finite-Natural-Numbers/#Fin___addNat "Documentation for Fin.addNat") (0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 8) 1 = (1 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 9)`
  * `[Fin.addNat](Basic-Types/Finite-Natural-Numbers/#Fin___addNat "Documentation for Fin.addNat") (1 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 8) 2 = (3 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.mul "Permalink")def
```


Fin.mul {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


Fin.mul {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


```

Multiplication modulo `n`, usually invoked via the `*` operator.
Examples:
  * `(2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) * (2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) = (4 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10)`
  * `(2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) * (7 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) = (4 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10)`
  * `(3 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) * (7 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) = (1 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.sub "Permalink")def
```


Fin.sub {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


Fin.sub {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


```

Subtraction modulo `n`, usually invoked via the `-` operator.
Examples:
  * `(5 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 11) - (3 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 11) = (2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 11)`
  * `(3 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 11) - (5 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 11) = (9 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 11)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.subNat "Permalink")def
```


Fin.subNat {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") m[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) (h : m [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") ↑i) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


Fin.subNat {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") m[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) (h : m [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") ↑i) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


```

Subtraction of a natural number from a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")`, with the bound narrowed.
This is a generalization of `[Fin.pred](Basic-Types/Finite-Natural-Numbers/#Fin___pred "Documentation for Fin.pred")`. It is guaranteed to not underflow or wrap around.
Examples:
  * `(5 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 9).[subNat](Basic-Types/Finite-Natural-Numbers/#Fin___subNat "Documentation for Fin.subNat") 2 (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")) = (3 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 7)`
  * `(5 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 9).[subNat](Basic-Types/Finite-Natural-Numbers/#Fin___subNat "Documentation for Fin.subNat") 0 (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")) = (5 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 9)`
  * `(3 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 9).[subNat](Basic-Types/Finite-Natural-Numbers/#Fin___subNat "Documentation for Fin.subNat") 3 (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")) = (0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 6)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.div "Permalink")def
```


Fin.div {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


Fin.div {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


```

Division of bounded numbers, usually invoked via the `/` operator.
The resulting value is that computed by the `/` operator on `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`. In particular, the result of division by `0` is `0`.
Examples:
  * `(5 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) / (2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) = (2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10)`
  * `(5 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) / (0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) = (0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10)`
  * `(5 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) / (7 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) = (0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.mod "Permalink")def
```


Fin.mod {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


Fin.mod {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


```

Modulus of bounded numbers, usually invoked via the `%` operator.
The resulting value is that computed by the `%` operator on `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.modn "Permalink")def
```


Fin.modn {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


Fin.modn {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


```

Modulus of bounded numbers with respect to a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`.
The resulting value is that computed by the `%` operator on `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.log2 "Permalink")def
```


Fin.log2 {m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (n : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") m) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") m


Fin.log2 {m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (n : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") m) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") m


```

Logarithm base 2 for bounded numbers.
The resulting value is the same as that computed by `[Nat.log2](Basic-Types/Natural-Numbers/#Nat___log2 "Documentation for Nat.log2")`. In particular, the result for `0` is `0`.
Examples:
  * `(8 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10).[log2](Basic-Types/Finite-Natural-Numbers/#Fin___log2 "Documentation for Fin.log2") = (3 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10)`
  * `(7 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10).[log2](Basic-Types/Finite-Natural-Numbers/#Fin___log2 "Documentation for Fin.log2") = (2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10)`
  * `(4 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10).[log2](Basic-Types/Finite-Natural-Numbers/#Fin___log2 "Documentation for Fin.log2") = (2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10)`
  * `(3 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10).[log2](Basic-Types/Finite-Natural-Numbers/#Fin___log2 "Documentation for Fin.log2") = (1 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10)`
  * `(1 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10).[log2](Basic-Types/Finite-Natural-Numbers/#Fin___log2 "Documentation for Fin.log2") = (0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10)`
  * `(0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10).[log2](Basic-Types/Finite-Natural-Numbers/#Fin___log2 "Documentation for Fin.log2") = (0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10)`


###  20.3.3.3. Bitwise Operations[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Finite-Natural-Numbers--API-Reference--Bitwise-Operations "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.shiftLeft "Permalink")def
```


Fin.shiftLeft {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


Fin.shiftLeft {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} :
  [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


```

Bitwise left shift of bounded numbers, with wraparound on overflow.
Examples:
  * `(1 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) <<< (1 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) = (2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10)`
  * `(1 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) <<< (3 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) = (8 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10)`
  * `(1 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) <<< (4 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) = (6 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.shiftRight "Permalink")def
```


Fin.shiftRight {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


Fin.shiftRight {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} :
  [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


```

Bitwise right shift of bounded numbers.
This operator corresponds to logical rather than arithmetic bit shifting. The new bits are always `0`.
Examples:
  * `(15 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 16) >>> (1 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 16) = (7 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 16)`
  * `(15 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 16) >>> (2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 16) = (3 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 16)`
  * `(15 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 17) >>> (2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 17) = (3 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 17)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.land "Permalink")def
```


Fin.land {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


Fin.land {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


```

Bitwise and.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.lor "Permalink")def
```


Fin.lor {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


Fin.lor {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


```

Bitwise or.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.xor "Permalink")def
```


Fin.xor {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


Fin.xor {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


```

Bitwise xor (“exclusive or”).
###  20.3.3.4. Conversions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Finite-Natural-Numbers--API-Reference--Conversions "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.toNat "Permalink")def
```


Fin.toNat {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Fin.toNat {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Extracts the underlying `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` value.
This function is a synonym for `[Fin.val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val")`, which is the simp normal form. `[Fin.val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val")` is also a coercion, so values of type `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` are automatically converted to `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`s as needed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.ofNat "Permalink")def
```


Fin.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) [[NeZero](Type-Classes/Basic-Classes/#NeZero___mk "Documentation for NeZero") n] (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


Fin.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) [[NeZero](Type-Classes/Basic-Classes/#NeZero___mk "Documentation for NeZero") n] (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


```

Returns `a` modulo `n` as a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n`.
The assumption `[NeZero](Type-Classes/Basic-Classes/#NeZero___mk "Documentation for NeZero") n` ensures that `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` is nonempty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.cast "Permalink")def
```


Fin.cast {n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (eq : n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") m) (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") m


Fin.cast {n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (eq : n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") m)
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") m


```

Uses a proof that two bounds are equal to allow a value bounded by one to be used with the other.
In other words, when `eq : n = m`, `[Fin.cast](Basic-Types/Finite-Natural-Numbers/#Fin___cast "Documentation for Fin.cast") eq i` converts `i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` into a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") m`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.castLT "Permalink")def
```


Fin.castLT {n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") m) (h : ↑i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


Fin.castLT {n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") m)
  (h : ↑i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


```

Replaces the bound with another that is suitable for the value.
The proof embedded in `i` can be used to cast to a larger bound even if the concrete value is not known.
Examples:
`example : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 12 := (7 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10).[castLT](Basic-Types/Finite-Natural-Numbers/#Fin___castLT "Documentation for Fin.castLT") (by⊢ 7 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 12 [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")All goals completed! 🐙 : 7 < 12) ``example (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 12 :=   i.[castLT](Basic-Types/Finite-Natural-Numbers/#Fin___castLT "Documentation for Fin.castLT") <| byi:[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10⊢ ↑i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 12     [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") imkval✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")isLt✝:val✝ [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 10⊢ ↑[⟨](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.mk")val✝[,](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.mk") isLt✝[⟩](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.mk") [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 12; [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")mkval✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")isLt✝:val✝ [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 10⊢ val✝ [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 12; [omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic")All goals completed! 🐙 `
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.castLE "Permalink")def
```


Fin.castLE {n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (h : n [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") m) (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") m


Fin.castLE {n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (h : n [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") m)
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") m


```

Coarsens a bound to one at least as large.
See also `[Fin.castAdd](Basic-Types/Finite-Natural-Numbers/#Fin___castAdd "Documentation for Fin.castAdd")` for a version that represents the larger bound with addition rather than an explicit inequality proof.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.castAdd "Permalink")def
```


Fin.castAdd {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") m[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


Fin.castAdd {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") m[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


```

Coarsens a bound to one at least as large.
See also `[Fin.natAdd](Basic-Types/Finite-Natural-Numbers/#Fin___natAdd "Documentation for Fin.natAdd")` and `[Fin.addNat](Basic-Types/Finite-Natural-Numbers/#Fin___addNat "Documentation for Fin.addNat")` for addition functions that increase the bound, and `[Fin.castLE](Basic-Types/Finite-Natural-Numbers/#Fin___castLE "Documentation for Fin.castLE")` for a version that uses an explicit inequality proof.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.castSucc "Permalink")def
```


Fin.castSucc {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


Fin.castSucc {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} :
  [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


```

Coarsens a bound by one.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.rev "Permalink")def
```


Fin.rev {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


Fin.rev {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n


```

Replaces a value with its difference from the largest value in the type.
Considering the values of `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` as a sequence `0`, `1`, …, `n-2`, `n-1`, `[Fin.rev](Basic-Types/Finite-Natural-Numbers/#Fin___rev "Documentation for Fin.rev")` finds the corresponding element of the reversed sequence. In other words, it maps `0` to `n-1`, `1` to `n-2`, ..., and `n-1` to `0`.
Examples:
  * `(5 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 6).[rev](Basic-Types/Finite-Natural-Numbers/#Fin___rev "Documentation for Fin.rev") = (0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 6)`
  * `(0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 6).[rev](Basic-Types/Finite-Natural-Numbers/#Fin___rev "Documentation for Fin.rev") = (5 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 6)`
  * `(2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 5).[rev](Basic-Types/Finite-Natural-Numbers/#Fin___rev "Documentation for Fin.rev") = (2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 5)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.elim0 "Permalink")def
```


Fin.elim0.{u} {α : Sort u} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 0 → α


Fin.elim0.{u} {α : Sort u} : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 0 → α


```

The type `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 0` is uninhabited, so it can be used to derive any result whatsoever.
This is similar to `[Empty.elim](Basic-Types/The-Empty-Type/#Empty___elim "Documentation for Empty.elim")`. It can be thought of as a compiler-checked assertion that a code path is unreachable, or a logical contradiction from which `[False](Basic-Propositions/Truth/#False "Documentation for False")` and thus anything else could be derived.
###  20.3.3.5. Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Finite-Natural-Numbers--API-Reference--Iteration "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.foldr "Permalink")def
```


Fin.foldr.{u_1} {α : Sort u_1} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → α → α)
  (init : α) : α


Fin.foldr.{u_1} {α : Sort u_1} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → α → α) (init : α) : α


```

Combine all the values that can be represented by `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` with an initial value, starting at `n - 1` and nesting to the right.
Example:
  * `[Fin.foldr](Basic-Types/Finite-Natural-Numbers/#Fin___foldr "Documentation for Fin.foldr") 3 (·.[val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val") + ·) (0 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) = (0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 3).[val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val") + ((1 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 3).[val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val") + ((2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 3).[val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val") + 0))`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.foldrM "Permalink")def
```


Fin.foldrM.{u_1, u_2} {m : Type u_1 → Type u_2} {α : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → α → m α) (init : α) : m α


Fin.foldrM.{u_1, u_2}
  {m : Type u_1 → Type u_2} {α : Type u_1}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → α → m α) (init : α) : m α


```

Folds a monadic function over `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` from right to left, starting with `n-1`.
It is the sequence of steps:

```
Fin.foldrM n f xₙ = do
  let xₙ₋₁ ← f (n-1) xₙ
  let xₙ₋₂ ← f (n-2) xₙ₋₁
  ...
  let x₀ ← f 0 x₁
  pure x₀

```

[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.foldl "Permalink")def
```


Fin.foldl.{u_1} {α : Sort u_1} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : α → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → α)
  (init : α) : α


Fin.foldl.{u_1} {α : Sort u_1} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : α → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → α) (init : α) : α


```

Combine all the values that can be represented by `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` with an initial value, starting at `0` and nesting to the left.
Example:
  * `[Fin.foldl](Basic-Types/Finite-Natural-Numbers/#Fin___foldl "Documentation for Fin.foldl") 3 (· + ·.[val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val")) (0 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) = ((0 + (0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 3).[val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val")) + (1 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 3).[val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val")) + (2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 3).[val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.foldlM "Permalink")def
```


Fin.foldlM.{u_1, u_2} {m : Type u_1 → Type u_2} {α : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : α → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → m α) (init : α) : m α


Fin.foldlM.{u_1, u_2}
  {m : Type u_1 → Type u_2} {α : Type u_1}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : α → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → m α) (init : α) : m α


```

Folds a monadic function over all the values in `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` from left to right, starting with `0`.
It is the sequence of steps:

```
Fin.foldlM n f x₀ = do
  let x₁ ← f x₀ 0
  let x₂ ← f x₁ 1
  ...
  let xₙ ← f xₙ₋₁ (n-1)
  pure xₙ

```

[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.hIterate "Permalink")def
```


Fin.hIterate.{u_1} (P : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u_1) {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (init : P 0)
  (f : (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) → P ↑i → P [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")↑i [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) : P n


Fin.hIterate.{u_1} (P : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u_1)
  {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (init : P 0)
  (f : (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) → P ↑i → P [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")↑i [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) :
  P n


```

Applies an index-dependent function to all the values less than the given bound `n`, starting at `0` with an accumulator.
Concretely, `[Fin.hIterate](Basic-Types/Finite-Natural-Numbers/#Fin___hIterate "Documentation for Fin.hIterate") P init f` is equal to

```
  init |> f 0 |> f 1 |> ... |> f (n-1)

```

Theorems about `[Fin.hIterate](Basic-Types/Finite-Natural-Numbers/#Fin___hIterate "Documentation for Fin.hIterate")` can be proven using the general theorem `Fin.hIterate_elim` or other more specialized theorems.
`[Fin.hIterateFrom](Basic-Types/Finite-Natural-Numbers/#Fin___hIterateFrom "Documentation for Fin.hIterateFrom")` is a variant that takes a custom starting value instead of `0`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.hIterateFrom "Permalink")def
```


Fin.hIterateFrom.{u_1} (P : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u_1) {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (f : (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) → P ↑i → P [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")↑i [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (ubnd : i [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") n)
  (a : P i) : P n


Fin.hIterateFrom.{u_1}
  (P : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u_1) {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (f : (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) → P ↑i → P [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")↑i [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd"))
  (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (ubnd : i [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") n) (a : P i) : P n


```

Applies an index-dependent function `f` to all of the values in `[i:n]`, starting at `i` with an initial accumulator `a`.
Concretely, `[Fin.hIterateFrom](Basic-Types/Finite-Natural-Numbers/#Fin___hIterateFrom "Documentation for Fin.hIterateFrom") P f i a` is equal to

```
  a |> f i |> f (i + 1) |> ... |> f (n - 1)

```

Theorems about `[Fin.hIterateFrom](Basic-Types/Finite-Natural-Numbers/#Fin___hIterateFrom "Documentation for Fin.hIterateFrom")` can be proven using the general theorem `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin").hIterateFrom_elim` or other more specialized theorems.
`[Fin.hIterate](Basic-Types/Finite-Natural-Numbers/#Fin___hIterate "Documentation for Fin.hIterate")` is a variant that always starts at `0`.
###  20.3.3.6. Reasoning[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Finite-Natural-Numbers--API-Reference--Reasoning "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.induction "Permalink")def
```


Fin.induction.{u_1} {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} {motive : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") → Sort u_1}
  (zero : motive 0)
  (succ : (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) → motive i.[castSucc](Basic-Types/Finite-Natural-Numbers/#Fin___castSucc "Documentation for Fin.castSucc") → motive i.[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ"))
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) : motive i


Fin.induction.{u_1} {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  {motive : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") → Sort u_1}
  (zero : motive 0)
  (succ :
    (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) →
      motive i.[castSucc](Basic-Types/Finite-Natural-Numbers/#Fin___castSucc "Documentation for Fin.castSucc") → motive i.[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ"))
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) : motive i


```

Proves a statement by induction on the underlying `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` value in a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n + 1)`.
For the induction:
  * `zero` is the base case, demonstrating `motive 0`.
  * `succ` is the inductive step, assuming the motive for `i : Fin n` (lifted to `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n + 1)` with `[Fin.castSucc](Basic-Types/Finite-Natural-Numbers/#Fin___castSucc "Documentation for Fin.castSucc")`) and demonstrating it for `i.[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ")`.


`[Fin.inductionOn](Basic-Types/Finite-Natural-Numbers/#Fin___inductionOn "Documentation for Fin.inductionOn")` is a version of this induction principle that takes the `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` as its first parameter, `[Fin.cases](Basic-Types/Finite-Natural-Numbers/#Fin___cases "Documentation for Fin.cases")` is the corresponding case analysis operator, and `[Fin.reverseInduction](Basic-Types/Finite-Natural-Numbers/#Fin___reverseInduction "Documentation for Fin.reverseInduction")` is a version that starts at the greatest value instead of `0`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.inductionOn "Permalink")def
```


Fin.inductionOn.{u_1} {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd"))
  {motive : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") → Sort u_1} (zero : motive 0)
  (succ : (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) → motive i.[castSucc](Basic-Types/Finite-Natural-Numbers/#Fin___castSucc "Documentation for Fin.castSucc") → motive i.[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ")) : motive i


Fin.inductionOn.{u_1} {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd"))
  {motive : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") → Sort u_1}
  (zero : motive 0)
  (succ :
    (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) →
      motive i.[castSucc](Basic-Types/Finite-Natural-Numbers/#Fin___castSucc "Documentation for Fin.castSucc") → motive i.[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ")) :
  motive i


```

Proves a statement by induction on the underlying `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` value in a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n + 1)`.
For the induction:
  * `zero` is the base case, demonstrating `motive 0`.
  * `succ` is the inductive step, assuming the motive for `i : Fin n` (lifted to `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n + 1)` with `[Fin.castSucc](Basic-Types/Finite-Natural-Numbers/#Fin___castSucc "Documentation for Fin.castSucc")`) and demonstrating it for `i.[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ")`.


`[Fin.induction](Basic-Types/Finite-Natural-Numbers/#Fin___induction "Documentation for Fin.induction")` is a version of this induction principle that takes the `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` as its last parameter.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.reverseInduction "Permalink")def
```


Fin.reverseInduction.{u_1} {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} {motive : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") → Sort u_1}
  (last : motive ([Fin.last](Basic-Types/Finite-Natural-Numbers/#Fin___last "Documentation for Fin.last") n))
  (cast : (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) → motive i.[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ") → motive i.[castSucc](Basic-Types/Finite-Natural-Numbers/#Fin___castSucc "Documentation for Fin.castSucc"))
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) : motive i


Fin.reverseInduction.{u_1} {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  {motive : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") → Sort u_1}
  (last : motive ([Fin.last](Basic-Types/Finite-Natural-Numbers/#Fin___last "Documentation for Fin.last") n))
  (cast :
    (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) →
      motive i.[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ") → motive i.[castSucc](Basic-Types/Finite-Natural-Numbers/#Fin___castSucc "Documentation for Fin.castSucc"))
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) : motive i


```

Proves a statement by reverse induction on the underlying `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` value in a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n + 1)`.
For the induction:
  * `last` is the base case, demonstrating `motive ([Fin.last](Basic-Types/Finite-Natural-Numbers/#Fin___last "Documentation for Fin.last") n)`.
  * `[cast](Basic-Propositions/Propositional-Equality/#cast "Documentation for cast")` is the inductive step, assuming the motive for `(j : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n).[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ")` and demonstrating it for the predecessor `j.[castSucc](Basic-Types/Finite-Natural-Numbers/#Fin___castSucc "Documentation for Fin.castSucc")`.


`[Fin.induction](Basic-Types/Finite-Natural-Numbers/#Fin___induction "Documentation for Fin.induction")` is the non-reverse induction principle.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.cases "Permalink")def
```


Fin.cases.{u_1} {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} {motive : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") → Sort u_1}
  (zero : motive 0) (succ : (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) → motive i.[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ"))
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) : motive i


Fin.cases.{u_1} {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  {motive : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") → Sort u_1}
  (zero : motive 0)
  (succ : (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) → motive i.[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ"))
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) : motive i


```

Proves a statement by cases on the underlying `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` value in a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n + 1)`.
The two cases are:
  * `zero`, used when the value is of the form `(0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n + 1))`
  * `succ`, used when the value is of the form `(j : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n).[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ")`


The corresponding induction principle is `[Fin.induction](Basic-Types/Finite-Natural-Numbers/#Fin___induction "Documentation for Fin.induction")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.lastCases "Permalink")def
```


Fin.lastCases.{u_1} {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} {motive : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") → Sort u_1}
  (last : motive ([Fin.last](Basic-Types/Finite-Natural-Numbers/#Fin___last "Documentation for Fin.last") n)) (cast : (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) → motive i.[castSucc](Basic-Types/Finite-Natural-Numbers/#Fin___castSucc "Documentation for Fin.castSucc"))
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) : motive i


Fin.lastCases.{u_1} {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  {motive : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") → Sort u_1}
  (last : motive ([Fin.last](Basic-Types/Finite-Natural-Numbers/#Fin___last "Documentation for Fin.last") n))
  (cast : (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) → motive i.[castSucc](Basic-Types/Finite-Natural-Numbers/#Fin___castSucc "Documentation for Fin.castSucc"))
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) : motive i


```

Proves a statement by cases on the underlying `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` value in a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n + 1)`, checking whether the value is the greatest representable or a predecessor of some other.
The two cases are:
  * `last`, used when the value is `[Fin.last](Basic-Types/Finite-Natural-Numbers/#Fin___last "Documentation for Fin.last") n`
  * `[cast](Basic-Propositions/Propositional-Equality/#cast "Documentation for cast")`, used when the value is of the form `(j : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n).[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ")`


The corresponding induction principle is `[Fin.reverseInduction](Basic-Types/Finite-Natural-Numbers/#Fin___reverseInduction "Documentation for Fin.reverseInduction")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.addCases "Permalink")def
```


Fin.addCases.{u} {m n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} {motive : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")m [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") → Sort u}
  (left : (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") m) → motive ([Fin.castAdd](Basic-Types/Finite-Natural-Numbers/#Fin___castAdd "Documentation for Fin.castAdd") n i))
  (right : (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) → motive ([Fin.natAdd](Basic-Types/Finite-Natural-Numbers/#Fin___natAdd "Documentation for Fin.natAdd") m i)) (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")m [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) :
  motive i


Fin.addCases.{u} {m n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  {motive : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")m [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") → Sort u}
  (left :
    (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") m) →
      motive ([Fin.castAdd](Basic-Types/Finite-Natural-Numbers/#Fin___castAdd "Documentation for Fin.castAdd") n i))
  (right :
    (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) → motive ([Fin.natAdd](Basic-Types/Finite-Natural-Numbers/#Fin___natAdd "Documentation for Fin.natAdd") m i))
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")m [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) : motive i


```

A case analysis operator for `i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (m + n)` that separately handles the cases where `i < m` and where `m ≤ i < m + n`.
The first case, where `i < m`, is handled by `left`. In this case, `i` can be represented as `[Fin.castAdd](Basic-Types/Finite-Natural-Numbers/#Fin___castAdd "Documentation for Fin.castAdd") n (j : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") m)`.
The second case, where `m ≤ i < m + n`, is handled by `right`. In this case, `i` can be represented as `[Fin.natAdd](Basic-Types/Finite-Natural-Numbers/#Fin___natAdd "Documentation for Fin.natAdd") m (j : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n)`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.succRec "Permalink")def
```


Fin.succRec.{u_1} {motive : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → Sort u_1}
  (zero : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → motive n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") 0)
  (succ : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) → motive n i → motive n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") i.[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ"))
  {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) : motive n i


Fin.succRec.{u_1}
  {motive : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → Sort u_1}
  (zero : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → motive n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") 0)
  (succ :
    (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) →
      (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) →
        motive n i → motive n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") i.[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ"))
  {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) : motive n i


```

An induction principle for `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` that considers a given `i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` as given by a sequence of `i` applications of `[Fin.succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ")`.
The cases in the induction are:
  * `zero` demonstrates the motive for `(0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n + 1))` for all bounds `n`
  * `succ` demonstrates the motive for `[Fin.succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ")` applied to an arbitrary `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` for an arbitrary bound `n`


Unlike `[Fin.induction](Basic-Types/Finite-Natural-Numbers/#Fin___induction "Documentation for Fin.induction")`, the motive quantifies over the bound, and the bound varies at each inductive step. `[Fin.succRecOn](Basic-Types/Finite-Natural-Numbers/#Fin___succRecOn "Documentation for Fin.succRecOn")` is a version of this induction principle that takes the `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` argument first.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Fin.succRecOn "Permalink")def
```


Fin.succRecOn.{u_1} {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n)
  {motive : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → Sort u_1}
  (zero : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → motive [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0)
  (succ : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) → motive n i → motive n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") i.[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ")) :
  motive n i


Fin.succRecOn.{u_1} {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n)
  {motive : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → Sort u_1}
  (zero : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → motive [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0)
  (succ :
    (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) →
      (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) →
        motive n i →
          motive n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") i.[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ")) :
  motive n i


```

An induction principle for `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` that considers a given `i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` as given by a sequence of `i` applications of `[Fin.succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ")`.
The cases in the induction are:
  * `zero` demonstrates the motive for `(0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n + 1))` for all bounds `n`
  * `succ` demonstrates the motive for `[Fin.succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ")` applied to an arbitrary `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` for an arbitrary bound `n`


Unlike `[Fin.induction](Basic-Types/Finite-Natural-Numbers/#Fin___induction "Documentation for Fin.induction")`, the motive quantifies over the bound, and the bound varies at each inductive step. `[Fin.succRec](Basic-Types/Finite-Natural-Numbers/#Fin___succRec "Documentation for Fin.succRec")` is a version of this induction principle that takes the `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` argument last.
[←20.2. Integers](Basic-Types/Integers/#Int "20.2. Integers")[20.4. Fixed-Precision Integers→](Basic-Types/Fixed-Precision-Integers/#fixed-ints "20.4. Fixed-Precision Integers")

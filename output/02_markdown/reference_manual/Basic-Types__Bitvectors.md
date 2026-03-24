[←20.4. Fixed-Precision Integers](Basic-Types/Fixed-Precision-Integers/#fixed-ints "20.4. Fixed-Precision Integers")[20.6. Floating-Point Numbers→](Basic-Types/Floating-Point-Numbers/#Float "20.6. Floating-Point Numbers")
#  20.5. Bitvectors[🔗](find/?domain=Verso.Genre.Manual.section&name=BitVec "Permalink")
Bitvectors are fixed-width sequences of binary digits. They are frequently used in software verification, because they closely model efficient data structures and operations that are similar to hardware. A bitvector can be understood from two perspectives: as a sequence of bits, or as a number encoded by a sequence of bits. When a bitvector represents a number, it can do so as either a signed or an unsigned number. Signed numbers are represented in two's complement form.
##  20.5.1. Logical Model[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Bitvectors--Logical-Model "Permalink")
Bitvectors are represented as a wrapper around a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` with a suitable bound. Because `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` itself is a wrapper around a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, bitvectors are able to use the kernel's special support for efficient computation with natural numbers.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.ofFin "Permalink")structure
```


BitVec (w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : Type


BitVec (w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : Type


```

A bitvector of the specified width.
This is represented as the underlying `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` number in both the runtime and the kernel, inheriting all the special support for `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`.
#  Constructor

```
[BitVec.ofFin](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec.ofFin")
```

Construct a `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w` from a number less than `2^w`. O(1), because we use `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` as the internal representation of a bitvector.
#  Fields

```
toFin : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [(](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")2 [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") w[)](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")
```

Interpret a bitvector as a number less than `2^w`. O(1), because we use `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` as the internal representation of a bitvector.
##  20.5.2. Runtime Representation[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Bitvectors--Runtime-Representation "Permalink")
Bitvectors are represented as a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` with the corresponding range. Because `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec")` is a [trivial wrapper](The-Type-System/Inductive-Types/#inductive-types-trivial-wrappers) around `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` and `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` is a trivial wrapper around `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, bitvectors use the same runtime representation as `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` in compiled code.
##  20.5.3. Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Bitvectors--Syntax "Permalink")
There is an `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") ([BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) n` instance for all widths `w` and natural numbers `n`. Natural number literals, including those that use hexadecimal or binary notation, may be used to represent bitvectors in contexts where the expected type is known. When the expected type is not known, a dedicated syntax allows the width of the bitvector to be specified along with its value.
Numeric Literals for Bitvectors
The following literals are all equivalent:
`example : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 8 := 0xff example : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 8 := 255 example : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 8 := 0b1111_1111 `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAueAhAlgFwGrAMbwA4kBeeABhADNKAoUSWBZdbPQk+AJgFZu7xocJKkw58RRKTIAjAIzzZAfQWyaNALTr4ASQB2MNLoQZgAZwz8GQ5AAoK1YSzGEAlPFI9uHaQE94AJ0oYS0EmeDs5BWUFR1E2AjcPXm8/QJggA"\))
syntaxFixed-Width Bitvector Literals

```
term ::= ...
    | 


Notation for bitvector literals. i#n is a shorthand for BitVec.ofNat n i. 


Conventions for notations in identifiers:




  * 

The recommended spelling of 0#n in identifiers is zero (not ofNat_zero).




  * 

The recommended spelling of 1#n in identifiers is one (not ofNat_one).






num#term
```

This notation pairs a numeric literal with a term that denotes its width. Spaces are forbidden around the `#`. Literals that overflow the width of the bitvector are truncated.
Fixed-Width Bitvector Literals
Bitvectors may be represented by natural number literals, so `(5 : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 8)` is a valid bitvector. Additionally, a width may be specified directly in the literal:
`5#8`
Spaces are not allowed on either side of the `#`:

```
5 expected end of input#8
```

```
<example>:1:2-1:3: expected end of input
```

```
5# expected no space before8
```

```
<example>:1:3-1:4: expected no space before
```

A numeric literal is required to the left of the `#`:

```
(3 + 2)expected end of input#8
```

```
<example>:1:7-1:8: expected end of input
```

However, a term is allowed to the right of the `#`:
`5#(4 + 4)`
If the literal is too large to fit in the specified number of bits, then it is truncated:
``[3](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")2`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") 7#2 `
```
[3](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")2
```

[Live ↪](javascript:openLiveLink\("MQUwbghgNgBA7MATEA"\))
syntaxBounded Bitvector Literals

```
term ::= ...
    | 


Notation for bitvector literals without truncation. i#'lt is a shorthand for BitVec.ofNatLT i lt. 


num#'term
```

This notation is available only when the `BitVec` namespace has been opened. Rather than an explicit width, it expects a proof that the literal value is representable by a bitvector of the corresponding width.
Bounded Bitvector Literals
The bounded bitvector literal notation ensures that literals do not overflow the specified number of bits. The notation is only available when the `BitVec` namespace has been opened.
`[open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") BitVec `
Literals that are in bounds require a proof to that effect:
`example : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 8 := 1#'(by⊢ 1 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 2 [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 8 [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")All goals completed! 🐙) `
Literals that are not in bounds are not allowed:
`example : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 8 := 256#'(by⊢ 256 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 2 [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 8 `Tactic `decide` proved that the proposition   256 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 2 [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 8 is false`[decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")⊢ 256 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 2 [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 8) `
```
Tactic `decide` proved that the proposition
  256 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 2 [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 8
is false
```

[Live ↪](javascript:openLiveLink\("PYBwpgdgBAQglgFwGpgMYCh1gB4EMC2IANmFAFyyIqpQAc5AvFAIwDEA5ABQBGAnlABM0cIQEogA"\))
##  20.5.4. Automation[🔗](find/?domain=Verso.Genre.Manual.section&name=BitVec-automation "Permalink")
In addition to the full suite of automation and tools provided by Lean for every type, the `[bv_decide](Tactic-Proofs/Tactic-Reference/#bv_decide "Documentation for tactic")` tactic can solve many bitvector-related problems. This tactic invokes an external automated theorem prover (`cadical`) and reconstructs the proof that it provides in Lean's own logic. The resulting proofs rely only on the axiom `Lean.ofReduceBool`; the external prover is not part of the trusted code base.
Popcount
The function `[popcount](Basic-Types/Bitvectors/#popcount-_LPAR_in-Popcount_RPAR_ "Definition of example")` returns the number of set bits in a bitvector. It can be implemented as a 32-iteration loop that tests each bit, incrementing a counter if the bit is set:
`def popcount_spec (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32 :=   (32 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")).[fold](Basic-Types/Natural-Numbers/#Nat___fold "Documentation for Nat.fold") (init := 0) fun i _ pop =>     pop + ((x >>> i) &&& 1) `
An alternative implementation of `[popcount](Basic-Types/Bitvectors/#popcount-_LPAR_in-Popcount_RPAR_ "Definition of example")` is described in _Hacker's Delight, Second Edition_ , by Henry S. Warren, Jr. in Figure 5-2 on p. 82. It uses low-level bitwise operations to compute the same value with far fewer operations:
`def popcount (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32 :=   let x := x - ((x >>> 1) &&& 0x55555555)   let x := (x &&& 0x33333333) + ((x >>> 2) &&& 0x33333333)   let x := (x + (x >>> 4)) &&& 0x0F0F0F0F   let x := x + (x >>> 8)   let x := x + (x >>> 16)   let x := x &&& 0x0000003F   x `
These two implementations can be proven equivalent using `[bv_decide](Tactic-Proofs/Tactic-Reference/#bv_decide "Documentation for tactic")`:
`theorem popcount_correct : [popcount](Basic-Types/Bitvectors/#popcount-_LPAR_in-Popcount_RPAR_ "Definition of example") = [popcount_spec](Basic-Types/Bitvectors/#popcount_spec-_LPAR_in-Popcount_RPAR_ "Definition of example") := by⊢ [popcount](Basic-Types/Bitvectors/#popcount-_LPAR_in-Popcount_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [popcount_spec](Basic-Types/Bitvectors/#popcount_spec-_LPAR_in-Popcount_RPAR_ "Definition of example")   [funext](Tactic-Proofs/Tactic-Reference/#funext-next "Documentation for tactic") xhx:[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32⊢ [popcount](Basic-Types/Bitvectors/#popcount-_LPAR_in-Popcount_RPAR_ "Definition of example") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [popcount_spec](Basic-Types/Bitvectors/#popcount_spec-_LPAR_in-Popcount_RPAR_ "Definition of example") x   [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [[popcount](Basic-Types/Bitvectors/#popcount-_LPAR_in-Popcount_RPAR_ "Definition of example"), [popcount_spec](Basic-Types/Bitvectors/#popcount_spec-_LPAR_in-Popcount_RPAR_ "Definition of example")]hx:[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32⊢ [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 1 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1431655765](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [858993459](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 1 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1431655765](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 2 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [858993459](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")             [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")[(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 1 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1431655765](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [858993459](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                 [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 1 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1431655765](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 2 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [858993459](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight")               4 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")           [252645135](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")         [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 1 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1431655765](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [858993459](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                 [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 1 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1431655765](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 2 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [858993459](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")               [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")[(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 1 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1431655765](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [858993459](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                   [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 1 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1431655765](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 2 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [858993459](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight")                 4 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")             [252645135](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight")           8 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")       [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")[(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 1 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1431655765](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [858993459](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                 [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 1 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1431655765](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 2 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [858993459](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")               [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")[(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 1 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1431655765](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [858993459](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                   [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 1 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1431655765](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 2 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [858993459](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight")                 4 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")             [252645135](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")           [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 1 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1431655765](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [858993459](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                   [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 1 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1431655765](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 2 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [858993459](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                 [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")[(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 1 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1431655765](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [858993459](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                     [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 1 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1431655765](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 2 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [858993459](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight")                   4 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")               [252645135](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight")             8[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight")         16 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")     [63](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")   [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 1 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 2 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 3 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 4 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                                                         [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 5 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                                                       [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 6 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                                                     [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 7 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                                                   [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 8 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                                                 [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 9 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                                               [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 10 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                                             [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 11 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                                           [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 12 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                                         [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 13 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                                       [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 14 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                                     [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 15 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                                   [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 16 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                                 [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 17 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                               [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 18 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                             [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 19 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                           [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 20 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                         [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 21 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                       [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 22 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                     [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 23 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                   [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 24 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")                 [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 25 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")               [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 26 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")             [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 27 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")           [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 28 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")         [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 29 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")       [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 30 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")     [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")x [>>>](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.hShiftRight") 31 [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [1](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")[#](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")32[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")   bv_decideAll goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAZRgEwHQBUCGBjGxuoBCAagCICm2wy5AULTQGZyRjYQCuAdjAPoDOYSnAAUADzgAuOIWAxiwgMwAmAJRSZchdjgqpAXlpxRe6QDlMMVakYQANslHAucg3AAM6xtzjA4vFggwOH0APiNjQOCAalFxOFDE33UAMjS4AEZVeiYo9m54eOlZeSU1DRLtXWUDCLtyeAlJfTgJAFo4iUTQzNT09zEAVmGR4ezjesa3eLSUjzFFRaXF9ViReO64ctn55eXxuEnW6Yk1rqSAFlU+uYH3ADEHp/u6huPm47OEpIAOA6Omi1TqJzj0MgA2f5vQHHHZ3dwIhGKF7GMT0GAAC3I0HIIDynB4vHYUCglHg0lY+R4IXxBQEQh0HwARgBPCLeLjkMSNCL8UDBADalIJMAANLTCYJKABdCJMgBuvBoVBoQA"\))
##  20.5.5. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=BitVec-api "Permalink")
###  20.5.5.1. Bounds[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Bitvectors--API-Reference--Bounds "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.intMax "Permalink")def
```


BitVec.intMax (w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


BitVec.intMax (w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


```

The bitvector of width `w` that has the largest value when interpreted as an integer.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.intMin "Permalink")def
```


BitVec.intMin (w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


BitVec.intMin (w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


```

The bitvector of width `w` that has the smallest value when interpreted as an integer.
###  20.5.5.2. Construction[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Bitvectors--API-Reference--Construction "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.fill "Permalink")def
```


BitVec.fill (w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


BitVec.fill (w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


```

Fills a bitvector with `w` copies of the bit `b`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.zero "Permalink")def
```


BitVec.zero (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.zero (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Returns a bitvector of size `n` where all bits are `0`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.allOnes "Permalink")def
```


BitVec.allOnes (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.allOnes (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Returns a bitvector of size `n` where all bits are `1`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.twoPow "Permalink")def
```


BitVec.twoPow (w i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


BitVec.twoPow (w i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


```

`twoPow w i` is the bitvector `2^i` if `i < w`, and `0` otherwise. In other words, it is 2 to the power `i`.
From the bitwise point of view, it has the `i`th bit as `1` and all other bits as `0`.
###  20.5.5.3. Conversion[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Bitvectors--API-Reference--Conversion "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.toHex "Permalink")def
```


BitVec.toHex {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


BitVec.toHex {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Converts a bitvector into a fixed-width hexadecimal number with enough digits to represent it.
If `n` is `0`, then one digit is returned. Otherwise, `⌊(n + 3) / 4⌋` digits are returned.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.toInt "Permalink")def
```


BitVec.toInt {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


BitVec.toInt {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Interprets the bitvector as an integer stored in two's complement form.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.toNat "Permalink")def
```


BitVec.toNat {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


BitVec.toNat {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) :
  [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Return the underlying `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` that represents a bitvector.
This is O(1) because `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec")` is a (zero-cost) wrapper around a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.ofBool "Permalink")def
```


BitVec.ofBool (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 1


BitVec.ofBool (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 1


```

Turns a `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` into a bitvector of length `1`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.ofBoolListBE "Permalink")def
```


BitVec.ofBoolListBE (bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") bs.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")


BitVec.ofBoolListBE (bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") bs.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")


```

Converts a list of `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`s into a big-endian `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.ofBoolListLE "Permalink")def
```


BitVec.ofBoolListLE (bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") bs.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")


BitVec.ofBoolListLE (bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") bs.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")


```

Converts a list of `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`s into a little-endian `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.ofInt "Permalink")def
```


BitVec.ofInt (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.ofInt (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Converts an integer to its two's complement representation as a bitvector of the given width `n`, over- and underflowing as needed.
The underlying `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` is `(2^n + (i mod 2^n)) mod 2^n`. Converting the bitvector back to an `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` with `[BitVec.toInt](Basic-Types/Bitvectors/#BitVec___toInt "Documentation for BitVec.toInt")` results in the value `i.[bmod](Basic-Types/Integers/#Int___bmod "Documentation for Int.bmod") (2^n)`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.ofNat "Permalink")def
```


BitVec.ofNat (n i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.ofNat (n i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

The bitvector with value `i mod 2^n`.
Conventions for notations in identifiers:
  * The recommended spelling of `0#n` in identifiers is `zero` (not `ofNat_zero`).
  * The recommended spelling of `1#n` in identifiers is `one` (not `ofNat_one`).


[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.ofNatLT "Permalink")def
```


BitVec.ofNatLT {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (p : i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 2 [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") w) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


BitVec.ofNatLT {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (p : i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 2 [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") w) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


```

The `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec")` with value `i`, given a proof that `i < 2^w`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.cast "Permalink")def
```


BitVec.cast {n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (eq : n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") m) (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") m


BitVec.cast {n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (eq : n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") m)
  (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") m


```

If two natural numbers `n` and `m` are equal, then a bitvector of width `n` is also a bitvector of width `m`.
Using `x.[cast](Basic-Types/Bitvectors/#BitVec___cast "Documentation for BitVec.cast") eq` should be preferred over `eq ▸ x` because there are special-purpose `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` lemmas that can more consistently simplify `[BitVec.cast](Basic-Types/Bitvectors/#BitVec___cast "Documentation for BitVec.cast")` away.
###  20.5.5.4. Comparisons[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Bitvectors--API-Reference--Comparisons "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.ule "Permalink")def
```


BitVec.ule {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


BitVec.ule {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Unsigned less-than-or-equal-to for bitvectors.
SMT-LIB name: `bvule`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.sle "Permalink")def
```


BitVec.sle {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


BitVec.sle {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Signed less-than-or-equal-to for bitvectors.
SMT-LIB name: `bvsle`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.ult "Permalink")def
```


BitVec.ult {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


BitVec.ult {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Unsigned less-than for bitvectors.
SMT-LIB name: `bvult`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.slt "Permalink")def
```


BitVec.slt {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


BitVec.slt {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Signed less-than for bitvectors.
SMT-LIB name: `bvslt`.
Examples:
  * `[BitVec.slt](Basic-Types/Bitvectors/#BitVec___slt "Documentation for BitVec.slt") 6#4 7 = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[BitVec.slt](Basic-Types/Bitvectors/#BitVec___slt "Documentation for BitVec.slt") 7#4 8 = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.decEq "Permalink")def
```


BitVec.decEq {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


BitVec.decEq {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


```

Bitvectors have decidable equality.
This should be used via the instance `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") ([BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w)`.
###  20.5.5.5. Hashing[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Bitvectors--API-Reference--Hashing "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.hash "Permalink")def
```


BitVec.hash {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (bv : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


BitVec.hash {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (bv : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Computes a hash of a bitvector, combining 64-bit words using `[mixHash](Type-Classes/Basic-Classes/#mixHash "Documentation for mixHash")`.
###  20.5.5.6. Sequence Operations[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Bitvectors--API-Reference--Sequence-Operations "Permalink")
These operations treat bitvectors as sequences of bits, rather than as encodings of numbers.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.nil "Permalink")def
```


BitVec.nil : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 0


BitVec.nil : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 0


```

The empty bitvector.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.cons "Permalink")def
```


BitVec.cons {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (msb : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (lsbs : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


BitVec.cons {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (msb : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (lsbs : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


```

Prepends a single bit to the front of a bitvector, using big-endian order (see `append`).
The new bit is the most significant bit.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.concat "Permalink")def
```


BitVec.concat {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (msbs : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) (lsb : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


BitVec.concat {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (msbs : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n)
  (lsb : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


```

Append a single bit to the end of a bitvector, using big endian order (see `append`). That is, the new bit is the least significant bit.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.shiftConcat "Permalink")def
```


BitVec.shiftConcat {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.shiftConcat {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Shifts all bits of `x` to the left by `1` and sets the least significant bit to `b`.
This is a non-dependent version of `[BitVec.concat](Basic-Types/Bitvectors/#BitVec___concat "Documentation for BitVec.concat")` that does not change the total bitwidth.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.truncate "Permalink")def
```


BitVec.truncate {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (v : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") v


BitVec.truncate {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (v : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") v


```

Transforms a bitvector of length `w` into a bitvector of length `v`, padding with `0` as needed.
The specific behavior depends on the relationship between the starting width `w` and the final width `v`:
  * If `v > w`, it is zero-extended; the high bits are padded with zeroes until the bitvector has `v` bits.
  * If `v = w`, the bitvector is returned unchanged.
  * If `v < w`, the high bits are truncated.


`[BitVec.setWidth](Basic-Types/Bitvectors/#BitVec___setWidth "Documentation for BitVec.setWidth")`, `[BitVec.zeroExtend](Basic-Types/Bitvectors/#BitVec___zeroExtend "Documentation for BitVec.zeroExtend")`, and `[BitVec.truncate](Basic-Types/Bitvectors/#BitVec___truncate "Documentation for BitVec.truncate")` are aliases for this operation.
SMT-LIB name: `zero_extend`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.setWidth "Permalink")def
```


BitVec.setWidth {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (v : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") v


BitVec.setWidth {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (v : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") v


```

Transforms a bitvector of length `w` into a bitvector of length `v`, padding with `0` as needed.
The specific behavior depends on the relationship between the starting width `w` and the final width `v`:
  * If `v > w`, it is zero-extended; the high bits are padded with zeroes until the bitvector has `v` bits.
  * If `v = w`, the bitvector is returned unchanged.
  * If `v < w`, the high bits are truncated.


`[BitVec.setWidth](Basic-Types/Bitvectors/#BitVec___setWidth "Documentation for BitVec.setWidth")`, `[BitVec.zeroExtend](Basic-Types/Bitvectors/#BitVec___zeroExtend "Documentation for BitVec.zeroExtend")`, and `[BitVec.truncate](Basic-Types/Bitvectors/#BitVec___truncate "Documentation for BitVec.truncate")` are aliases for this operation.
SMT-LIB name: `zero_extend`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.setWidth' "Permalink")def
```


BitVec.setWidth' {n w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (le : n [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") w) (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


BitVec.setWidth' {n w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (le : n [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") w)
  (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


```

Increases the width of a bitvector to one that is at least as large by zero-extending it.
This is a constant-time operation because the underlying `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` is unmodified; because the new width is at least as large as the old one, no overflow is possible.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.append "Permalink")def
```


BitVec.append {n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (msbs : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) (lsbs : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") m) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") m[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


BitVec.append {n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (msbs : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) (lsbs : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") m) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") m[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


```

Concatenates two bitvectors using the “big-endian” convention that the more significant input is on the left. Usually accessed via the `++` operator.
SMT-LIB name: `concat`.
Example:
  * `0xAB#8 ++ 0xCD#8 = 0xABCD#16`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.replicate "Permalink")def
```


BitVec.replicate {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w → [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")w [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") i[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")


BitVec.replicate {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w → [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")w [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") i[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")


```

Concatenates `i` copies of `x` into a new vector of length `w * i`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.reverse "Permalink")def
```


BitVec.reverse {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w → [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


BitVec.reverse {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w → [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


```

Reverses the bits in a bitvector.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.rotateLeft "Permalink")def
```


BitVec.rotateLeft {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


BitVec.rotateLeft {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w)
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


```

Rotates the bits in a bitvector to the left.
All the bits of `x` are shifted to higher positions, with the top `n` bits wrapping around to fill the vacated low bits.
SMT-LIB name: `[rotate_left](Tactic-Proofs/The-Tactic-Language/#rotate_left "Documentation for tactic")`, except this operator uses a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` shift amount.
Example:
  * `(0b0011#4).[rotateLeft](Basic-Types/Bitvectors/#BitVec___rotateLeft "Documentation for BitVec.rotateLeft") 3 = 0b1001`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.rotateRight "Permalink")def
```


BitVec.rotateRight {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


BitVec.rotateRight {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


```

Rotates the bits in a bitvector to the right.
All the bits of `x` are shifted to lower positions, with the bottom `n` bits wrapping around to fill the vacated high bits.
SMT-LIB name: `[rotate_right](Tactic-Proofs/The-Tactic-Language/#rotate_right "Documentation for tactic")`, except this operator uses a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` shift amount.
Example:
  * `rotateRight 0b01001#5 1 = 0b10100`


####  20.5.5.6.1. Bit Extraction[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Bitvectors--API-Reference--Sequence-Operations--Bit-Extraction "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.msb "Permalink")def
```


BitVec.msb {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


BitVec.msb {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns the most significant bit in a bitvector.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.getMsbD "Permalink")def
```


BitVec.getMsbD {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


BitVec.getMsbD {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w)
  (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns the `i`th most significant bit, or `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` if `i ≥ w`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.getMsb "Permalink")def
```


BitVec.getMsb {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") w) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


BitVec.getMsb {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w)
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") w) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns the `i`th most significant bit.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.getMsb? "Permalink")def
```


BitVec.getMsb? {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


BitVec.getMsb? {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w)
  (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns the `i`th most significant bit or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if `i ≥ w`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.getLsbD "Permalink")def
```


BitVec.getLsbD {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


BitVec.getLsbD {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w)
  (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns the `i`th least significant bit or `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` if `i ≥ w`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.getLsb "Permalink")def
```


BitVec.getLsb {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") w) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


BitVec.getLsb {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w)
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") w) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns the `i`th least significant bit.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.getLsb? "Permalink")def
```


BitVec.getLsb? {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


BitVec.getLsb? {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w)
  (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns the `i`th least significant bit, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if `i ≥ w`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.extractLsb "Permalink")def
```


BitVec.extractLsb {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (hi lo : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")hi [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") lo [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


BitVec.extractLsb {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (hi lo : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")hi [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") lo [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


```

Extracts the bits from `hi` down to `lo` (both inclusive) from a bitvector, which is implicitly zero-extended if necessary.
The resulting bitvector has size `hi - lo + 1`.
SMT-LIB name: `extract`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.extractLsb' "Permalink")def
```


BitVec.extractLsb' {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (start len : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") len


BitVec.extractLsb' {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (start len : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") len


```

Extracts the bits `start` to `start + len - 1` from a bitvector of size `n` to yield a new bitvector of size `len`. If `start + len > n`, then the bitvector is zero-extended.
###  20.5.5.7. Bitwise Operators[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Bitvectors--API-Reference--Bitwise-Operators "Permalink")
These operators modify the individual bits of one or more bitvectors.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.and "Permalink")def
```


BitVec.and {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.and {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Bitwise and for bitvectors. Usually accessed via the `&&&` operator.
SMT-LIB name: `bvand`.
Example:
  * `0b1010#4 &&& 0b0110#4 = 0b0010#4`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.or "Permalink")def
```


BitVec.or {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.or {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Bitwise or for bitvectors. Usually accessed via the `|||` operator.
SMT-LIB name: `bvor`.
Example:
  * `0b1010#4 ||| 0b0110#4 = 0b1110#4`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.not "Permalink")def
```


BitVec.not {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.not {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Bitwise complement for bitvectors. Usually accessed via the `~~~` prefix operator.
SMT-LIB name: `bvnot`.
Example:
  * `~~~(0b0101#4) == 0b1010`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.xor "Permalink")def
```


BitVec.xor {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.xor {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Bitwise xor for bitvectors. Usually accessed via the `^^^` operator.
SMT-LIB name: `bvxor`.
Example:
  * `0b1010#4 ^^^ 0b0110#4 = 0b1100#4`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.zeroExtend "Permalink")def
```


BitVec.zeroExtend {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (v : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") v


BitVec.zeroExtend {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (v : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") v


```

Transforms a bitvector of length `w` into a bitvector of length `v`, padding with `0` as needed.
The specific behavior depends on the relationship between the starting width `w` and the final width `v`:
  * If `v > w`, it is zero-extended; the high bits are padded with zeroes until the bitvector has `v` bits.
  * If `v = w`, the bitvector is returned unchanged.
  * If `v < w`, the high bits are truncated.


`[BitVec.setWidth](Basic-Types/Bitvectors/#BitVec___setWidth "Documentation for BitVec.setWidth")`, `[BitVec.zeroExtend](Basic-Types/Bitvectors/#BitVec___zeroExtend "Documentation for BitVec.zeroExtend")`, and `[BitVec.truncate](Basic-Types/Bitvectors/#BitVec___truncate "Documentation for BitVec.truncate")` are aliases for this operation.
SMT-LIB name: `zero_extend`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.signExtend "Permalink")def
```


BitVec.signExtend {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (v : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") v


BitVec.signExtend {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (v : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") v


```

Transforms a bitvector of length `w` into a bitvector of length `v`, padding as needed with the most significant bit's value.
If `x` is an empty bitvector, then the sign is treated as zero.
SMT-LIB name: `sign_extend`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.ushiftRight "Permalink")def
```


BitVec.ushiftRight {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) (s : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.ushiftRight {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) (s : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Shifts a bitvector to the right. This is a logical right shift - the high bits are filled with zeros.
As a numeric operation, this is equivalent to `x / 2^s`, rounding down.
SMT-LIB name: `bvlshr` except this operator uses a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` shift value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.sshiftRight "Permalink")def
```


BitVec.sshiftRight {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) (s : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.sshiftRight {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) (s : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Shifts a bitvector to the right. This is an arithmetic right shift - the high bits are filled with most significant bit's value.
As a numeric operation, this is equivalent to `x.[toInt](Basic-Types/Bitvectors/#BitVec___toInt "Documentation for BitVec.toInt") >>> s`.
SMT-LIB name: `bvashr` except this operator uses a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` shift value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.sshiftRight' "Permalink")def
```


BitVec.sshiftRight' {n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (a : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) (s : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") m) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.sshiftRight' {n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (a : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) (s : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") m) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Shifts a bitvector to the right. This is an arithmetic right shift - the high bits are filled with most significant bit's value.
As a numeric operation, this is equivalent to `a.[toInt](Basic-Types/Bitvectors/#BitVec___toInt "Documentation for BitVec.toInt") >>> s.[toNat](Basic-Types/Bitvectors/#BitVec___toNat "Documentation for BitVec.toNat")`.
SMT-LIB name: `bvashr`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.shiftLeft "Permalink")def
```


BitVec.shiftLeft {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) (s : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.shiftLeft {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n)
  (s : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Shifts a bitvector to the left. The low bits are filled with zeros. As a numeric operation, this is equivalent to `x * 2^s`, modulo `2^n`.
SMT-LIB name: `bvshl` except this operator uses a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` shift value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.shiftLeftZeroExtend "Permalink")def
```


BitVec.shiftLeftZeroExtend {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (msbs : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")w [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") m[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


BitVec.shiftLeftZeroExtend {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (msbs : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")w [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") m[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")


```

Returns `zeroExtend (w+n) x <<< n` without needing to compute `x % 2^(2+n)`.
###  20.5.5.8. Arithmetic[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Bitvectors--API-Reference--Arithmetic "Permalink")
These operators treat bitvectors as numbers. Some operations are signed, while others are unsigned. Because bitvectors are understood as two's complement numbers, addition, subtraction and multiplication coincide for the signed and unsigned interpretations.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.add "Permalink")def
```


BitVec.add {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.add {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Adds two bitvectors. This can be interpreted as either signed or unsigned addition modulo `2^n`. Usually accessed via the `+` operator.
SMT-LIB name: `bvadd`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.sub "Permalink")def
```


BitVec.sub {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.sub {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Subtracts one bitvector from another. This can be interpreted as either signed or unsigned subtraction modulo `2^n`. Usually accessed via the `-` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.mul "Permalink")def
```


BitVec.mul {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.mul {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Multiplies two bitvectors. This can be interpreted as either signed or unsigned multiplication modulo `2^n`. Usually accessed via the `*` operator.
SMT-LIB name: `bvmul`.
####  20.5.5.8.1. Unsigned Operations[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Bitvectors--API-Reference--Arithmetic--Unsigned-Operations "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.udiv "Permalink")def
```


BitVec.udiv {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.udiv {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Unsigned division of bitvectors using the Lean convention where division by zero returns zero. Usually accessed via the `/` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.smtUDiv "Permalink")def
```


BitVec.smtUDiv {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.smtUDiv {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Unsigned division of bitvectors using the [SMT-LIB convention](http://smtlib.cs.uiowa.edu/theories-FixedSizeBitVectors.shtml), where division by zero returns `BitVector.allOnes n`.
SMT-LIB name: `bvudiv`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.umod "Permalink")def
```


BitVec.umod {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.umod {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Unsigned modulo for bitvectors. Usually accessed via the `%` operator.
SMT-LIB name: `bvurem`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.uaddOverflow "Permalink")def
```


BitVec.uaddOverflow {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


BitVec.uaddOverflow {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether addition of `x` and `y` results in _unsigned_ overflow.
SMT-LIB name: `bvuaddo`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.usubOverflow "Permalink")def
```


BitVec.usubOverflow {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


BitVec.usubOverflow {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether subtraction of `x` and `y` results in _unsigned_ overflow.
SMT-Lib name: `bvusubo`.
####  20.5.5.8.2. Signed Operations[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Bitvectors--API-Reference--Arithmetic--Signed-Operations "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.abs "Permalink")def
```


BitVec.abs {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.abs {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Returns the absolute value of a signed bitvector.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.neg "Permalink")def
```


BitVec.neg {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.neg {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Negation of bitvectors. This can be interpreted as either signed or unsigned negation modulo `2^n`. Usually accessed via the `-` prefix operator.
SMT-LIB name: `bvneg`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.sdiv "Permalink")def
```


BitVec.sdiv {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.sdiv {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Signed T-division (using the truncating rounding convention) for bitvectors. This function obeys the Lean convention that division by zero returns zero.
Examples:
  * `(7#4).[sdiv](Basic-Types/Bitvectors/#BitVec___sdiv "Documentation for BitVec.sdiv") 2 = 3#4`
  * `(-8#4).[sdiv](Basic-Types/Bitvectors/#BitVec___sdiv "Documentation for BitVec.sdiv") 2 = -4#4`
  * `(5#4).[sdiv](Basic-Types/Bitvectors/#BitVec___sdiv "Documentation for BitVec.sdiv") -2 = -2#4`
  * `(-7#4).[sdiv](Basic-Types/Bitvectors/#BitVec___sdiv "Documentation for BitVec.sdiv") (-2) = 3#4`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.smtSDiv "Permalink")def
```


BitVec.smtSDiv {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.smtSDiv {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Signed division for bitvectors using the SMT-LIB using the [SMT-LIB convention](http://smtlib.cs.uiowa.edu/theories-FixedSizeBitVectors.shtml), where division by zero returns `BitVector.allOnes n`.
Specifically, `x.[smtSDiv](Basic-Types/Bitvectors/#BitVec___smtSDiv "Documentation for BitVec.smtSDiv") 0 = [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x >= 0 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") -1 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 1`
SMT-LIB name: `bvsdiv`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.smod "Permalink")def
```


BitVec.smod {m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") m) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") m


BitVec.smod {m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") m) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") m


```

Remainder for signed division rounded to negative infinity.
SMT-LIB name: `bvsmod`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.srem "Permalink")def
```


BitVec.srem {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


BitVec.srem {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") n


```

Remainder for signed division rounding to zero.
SMT-LIB name: `bvsrem`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.saddOverflow "Permalink")def
```


BitVec.saddOverflow {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


BitVec.saddOverflow {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether addition of `x` and `y` results in _signed_ overflow, treating `x` and `y` as 2's complement signed bitvectors.
SMT-LIB name: `bvsaddo`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.ssubOverflow "Permalink")def
```


BitVec.ssubOverflow {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


BitVec.ssubOverflow {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the subtraction of `x` and `y` results in _signed_ overflow, treating `x` and `y` as 2's complement signed bitvectors.
SMT-Lib name: `bvssubo`.
###  20.5.5.9. Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Bitvectors--API-Reference--Iteration "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.iunfoldr "Permalink")def
```


BitVec.iunfoldr.{u_1} {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} {α : Type u_1}
  (f : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") w → α → α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (s : α) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


BitVec.iunfoldr.{u_1} {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  {α : Type u_1}
  (f : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") w → α → α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (s : α) :
  α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


```

Constructs a bitvector by iteratively computing a state for each bit using the function `f`, starting with the initial state `s`. At each step, the prior state and the current bit index are passed to `f`, and it produces a bit along with the next state value. These bits are assembled into the final bitvector.
It produces a sequence of state values `[s_0, s_1 .. s_w]` and a bitvector `v` where `f i s_i = (s_{i+1}, b_i)` and `b_i` is bit `i`th least-significant bit in `v` (e.g., `getLsb v i = b_i`).
The theorem `iunfoldr_replace` allows uses of `[BitVec.iunfoldr](Basic-Types/Bitvectors/#BitVec___iunfoldr "Documentation for BitVec.iunfoldr")` to be replaced with declarative specifications that are easier to reason about.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.iunfoldr_replace "Permalink")theorem
```


BitVec.iunfoldr_replace.{u_1} {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} {α : Type u_1}
  {f : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") w → α → α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")} (state : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → α) (value : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w)
  (a : α) (init : state 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a)
  (step : ∀ (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") w), f i (state ↑i) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")state [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")↑i [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") value[[](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem.getElem")↑i[]](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem.getElem")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")) :
  [BitVec.iunfoldr](Basic-Types/Bitvectors/#BitVec___iunfoldr "Documentation for BitVec.iunfoldr") f a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")state w[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") value[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")


BitVec.iunfoldr_replace.{u_1} {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  {α : Type u_1}
  {f : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") w → α → α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")}
  (state : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → α) (value : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w)
  (a : α) (init : state 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a)
  (step :
    ∀ (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") w),
      f i (state ↑i) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
        [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")state [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")↑i [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") value[[](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem.getElem")↑i[]](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem.getElem")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")) :
  [BitVec.iunfoldr](Basic-Types/Bitvectors/#BitVec___iunfoldr "Documentation for BitVec.iunfoldr") f a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")state w[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") value[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")


```

Given a function `state` that provides the correct state for every potential iteration count and a function that computes these states from the correct initial state, the result of applying `[BitVec.iunfoldr](Basic-Types/Bitvectors/#BitVec___iunfoldr "Documentation for BitVec.iunfoldr") f` to the initial state is the state corresponding to the bitvector's width paired with the bitvector that consists of each computed bit.
This theorem can be used to prove properties of functions that are defined using `[BitVec.iunfoldr](Basic-Types/Bitvectors/#BitVec___iunfoldr "Documentation for BitVec.iunfoldr")`.
###  20.5.5.10. Proof Automation[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Bitvectors--API-Reference--Proof-Automation "Permalink")
####  20.5.5.10.1. Bit Blasting[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Bitvectors--API-Reference--Proof-Automation--Bit-Blasting "Permalink")
The standard library contains a number of helper implementations that are useful to implement bit blasting, which is the technique used by `[bv_decide](Tactic-Proofs/Tactic-Reference/#bv_decide "Documentation for tactic")` to encode propositions as Boolean satisfiability problems for external solvers.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.adc "Permalink")def
```


BitVec.adc {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


BitVec.adc {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


```

Bitwise addition implemented via a ripple carry adder.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.adcb "Permalink")def
```


BitVec.adcb (x y c : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


BitVec.adcb (x y c : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Carry function for bitwise addition.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.carry "Permalink")def
```


BitVec.carry {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) (c : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


BitVec.carry {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) (c : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

carry i x y c returns true if the `i` carry bit is true when computing `x + y + c`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.mulRec "Permalink")def
```


BitVec.mulRec {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w) (s : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


BitVec.mulRec {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w)
  (s : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w


```

A recurrence that describes multiplication as repeated addition.
This function is useful for bit blasting multiplication.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.divRec "Permalink")def
```


BitVec.divRec {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (args : BitVec.DivModArgs w)
  (qr : BitVec.DivModState w) : BitVec.DivModState w


BitVec.divRec {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (args : BitVec.DivModArgs w)
  (qr : BitVec.DivModState w) :
  BitVec.DivModState w


```

A recursive definition of division for bit blasting, in terms of a shift-subtraction circuit.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.divSubtractShift "Permalink")def
```


BitVec.divSubtractShift {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (args : BitVec.DivModArgs w)
  (qr : BitVec.DivModState w) : BitVec.DivModState w


BitVec.divSubtractShift {w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (args : BitVec.DivModArgs w)
  (qr : BitVec.DivModState w) :
  BitVec.DivModState w


```

One round of the division algorithm. It tries to perform a subtract shift.
This should only be called when `r.msb = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, so it will not overflow.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.shiftLeftRec "Permalink")def
```


BitVec.shiftLeftRec {w₁ w₂ : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w₁) (y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w₂)
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w₁


BitVec.shiftLeftRec {w₁ w₂ : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w₁) (y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w₂)
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w₁


```

Shifts `x` to the left by the first `n` bits of `y`.
The theorem `BitVec.shiftLeft_eq_shiftLeftRec` proves the equivalence of `(x <<< y)` and `[BitVec.shiftLeftRec](Basic-Types/Bitvectors/#BitVec___shiftLeftRec "Documentation for BitVec.shiftLeftRec") x y`.
Together with equations `BitVec.shiftLeftRec_zero` and `BitVec.shiftLeftRec_succ`, this allows `[BitVec.shiftLeft](Basic-Types/Bitvectors/#BitVec___shiftLeft "Documentation for BitVec.shiftLeft")` to be unfolded into a circuit for bit blasting.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.sshiftRightRec "Permalink")def
```


BitVec.sshiftRightRec {w₁ w₂ : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w₁) (y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w₂)
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w₁


BitVec.sshiftRightRec {w₁ w₂ : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w₁) (y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w₂)
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w₁


```

Shifts `x` arithmetically (signed) to the right by the first `n` bits of `y`.
The theorem `BitVec.sshiftRight_eq_sshiftRightRec` proves the equivalence of `(x.[sshiftRight](Basic-Types/Bitvectors/#BitVec___sshiftRight "Documentation for BitVec.sshiftRight") y)` and `[BitVec.sshiftRightRec](Basic-Types/Bitvectors/#BitVec___sshiftRightRec "Documentation for BitVec.sshiftRightRec") x y`. Together with equations `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec").sshiftRightRec_zero`, and `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec").sshiftRightRec_succ`, this allows `[BitVec.sshiftRight](Basic-Types/Bitvectors/#BitVec___sshiftRight "Documentation for BitVec.sshiftRight")` to be unfolded into a circuit for bit blasting.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BitVec.ushiftRightRec "Permalink")def
```


BitVec.ushiftRightRec {w₁ w₂ : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w₁) (y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w₂)
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w₁


BitVec.ushiftRightRec {w₁ w₂ : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w₁) (y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w₂)
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") w₁


```

Shifts `x` logically to the right by the first `n` bits of `y`.
The theorem `BitVec.shiftRight_eq_ushiftRightRec` proves the equivalence of `(x >>> y)` and `[BitVec.ushiftRightRec](Basic-Types/Bitvectors/#BitVec___ushiftRightRec "Documentation for BitVec.ushiftRightRec")`.
Together with equations `BitVec.ushiftRightRec_zero` and `BitVec.ushiftRightRec_succ`, this allows `[BitVec.ushiftRight](Basic-Types/Bitvectors/#BitVec___ushiftRight "Documentation for BitVec.ushiftRight")` to be unfolded into a circuit for bit blasting.
[←20.4. Fixed-Precision Integers](Basic-Types/Fixed-Precision-Integers/#fixed-ints "20.4. Fixed-Precision Integers")[20.6. Floating-Point Numbers→](Basic-Types/Floating-Point-Numbers/#Float "20.6. Floating-Point Numbers")

[←20.5. Bitvectors](Basic-Types/Bitvectors/#BitVec "20.5. Bitvectors")[20.7. Characters→](Basic-Types/Characters/#Char "20.7. Characters")
#  20.6. Floating-Point Numbers[🔗](find/?domain=Verso.Genre.Manual.section&name=Float "Permalink")
Floating-point numbers are a an approximation of the real numbers that are efficiently implemented in computer hardware. Computations that use floating-point numbers are very efficient; however, the nature of the way that they approximate the real numbers is complex, with many corner cases. The IEEE 754 standard, which defines the floating-point format that is used on modern computers, allows hardware designers to make certain choices, and real systems differ in these small details. For example, there are many distinct bit representations of `NaN`, the indicator that a result is undefined, and some platforms differ with respect to _which_ `NaN` is returned from adding two `NaN`s.
Lean exposes the underlying platform's floating-point values for use in programming, but they are not encoded in Lean's logic. They are represented by an opaque type. This means that the [kernel](Elaboration-and-Compilation/#--tech-term-kernel) is not capable of computing with or reasoning about floating-point values without additional [axioms](Axioms/#axioms). A consequence of this is that equality of floating-point numbers is not decidable. Furthermore, comparisons between floating-point values are decidable, but the code that does so is opaque; in practice, the decision procedure can only be used in compiled code.
Lean provides two floating-point types: `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` represents 64-bit floating point values, while `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` represents 32-bit floating point values. The precision of `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` does not vary based on the platform that Lean is running on.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float "Permalink")type
```


Float : Type


Float : Type


```

64-bit floating-point numbers.
`[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` corresponds to the IEEE 754 _binary64_ format (`double` in C or `f64` in Rust). Floating-point numbers are a finite representation of a subset of the real numbers, extended with extra “sentinel” values that represent undefined and infinite results as well as separate positive and negative zeroes. Arithmetic on floating-point numbers approximates the corresponding operations on the real numbers by rounding the results to numbers that are representable, propagating error and infinite values.
Floating-point numbers include [subnormal numbers](https://en.wikipedia.org/wiki/Subnormal_number). Their special values are:
  * `NaN`, which denotes a class of “not a number” values that result from operations such as dividing zero by zero, and
  * `Inf` and `-Inf`, which represent positive and infinities that result from dividing non-zero values by zero.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32 "Permalink")type
```


Float32 : Type


Float32 : Type


```

32-bit floating-point numbers.
`[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` corresponds to the IEEE 754 _binary32_ format (`float` in C or `f32` in Rust). Floating-point numbers are a finite representation of a subset of the real numbers, extended with extra “sentinel” values that represent undefined and infinite results as well as separate positive and negative zeroes. Arithmetic on floating-point numbers approximates the corresponding operations on the real numbers by rounding the results to numbers that are representable, propagating error and infinite values.
Floating-point numbers include [subnormal numbers](https://en.wikipedia.org/wiki/Subnormal_number). Their special values are:
  * `NaN`, which denotes a class of “not a number” values that result from operations such as dividing zero by zero, and
  * `Inf` and `-Inf`, which represent positive and infinities that result from dividing non-zero values by zero.


No Kernel Reasoning About Floating-Point Numbers
The Lean kernel can compare expressions of type `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` for syntactic equality, so `0.0` is definitionally equal to itself.
`example : (0.0 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) = (0.0 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) := by⊢ 0.0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0.0 [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 `
Terms that require reduction to become syntactically equal cannot be checked by the kernel:
`example : (0.0 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) = (0.0 + 0.0 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) := by⊢ 0.0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0.0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0.0 `Tactic `rfl` failed: The left-hand side   0.0 is not definitionally equal to the right-hand side   0.0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0.0  ⊢ 0.0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0.0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0.0`[rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")⊢ 0.0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0.0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0.0 `
```
Tactic `rfl` failed: The left-hand side
  0.0
is not definitionally equal to the right-hand side
  0.0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0.0

⊢ 0.0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0.0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0.0
```

Similarly, the kernel cannot evaluate `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`-valued comparisons of floating-point numbers while checking definitional equality:
`theorem Float.zero_eq_zero_plus_zero :     ((0.0 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) == (0.0 + 0.0 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float"))) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") :=   by⊢ [(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")0.0 [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") 0.0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0.0[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") `Tactic `rfl` failed: The left-hand side   0.0 [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") 0.0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0.0 is not definitionally equal to the right-hand side   [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")  ⊢ [(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")0.0 [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") 0.0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0.0[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`[rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")⊢ [(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")0.0 [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") 0.0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0.0[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") `
```
Tactic `rfl` failed: The left-hand side
  0.0 [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") 0.0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0.0
is not definitionally equal to the right-hand side
  [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")

⊢ [(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")0.0 [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") 0.0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0.0[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")
```

However, the `[native_decide](Tactic-Proofs/Tactic-Reference/#native_decide "Documentation for tactic")` tactic can invoke the underlying platform's floating-point primitives that are used by Lean for run-time programs:
`theorem Float.zero_eq_zero_plus_zero :     ((0.0 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) == (0.0 + 0.0 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float"))) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") := by⊢ [(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")0.0 [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") 0.0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0.0[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")   [native_decide](Tactic-Proofs/Tactic-Reference/#native_decide "Documentation for tactic")All goals completed! 🐙 `
This tactic executes a decision procedure as compiled native code. This requires trusting the Lean compiler, interpreter and the low-level implementations of built-in operators in addition to the kernel. To make this dependency precisely clear, the tactic creates the axiom `Float.zero_eq_zero_plus_zero._native.native_decide.ax_1`:
``'Float.zero_eq_zero_plus_zero' depends on axioms: [Classical.choice,  Float.zero_eq_zero_plus_zero._native.native_decide.ax_1]`[#print](Interacting-with-Lean/#Lean___Parser___Command___printAxioms "Documentation for syntax") [axioms](Interacting-with-Lean/#Lean___Parser___Command___printAxioms "Documentation for syntax") Float.zero_eq_zero_plus_zero `
```
'Float.zero_eq_zero_plus_zero' depends on axioms: [Classical.choice,
 Float.zero_eq_zero_plus_zero._native.native_decide.ax_1]
```

[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAueAKADAOjU+AxGA9mAC4CU8AvKptsvkWUlQEYCe8ATgGYwBQvxABbACHYBDyESGAF7AOBAPrAAjorkLFsAK4BndfIJJe8U6nRYc9EuQpUL2ANTwaVqWVvxiHbQkQtWE3gAOxIASwA3YEUAE2AAYzC4/gBiKA4w4OJ4MBAwgghdSQZZQ2U1DSUdfUqgA"\))
Floating-Point Equality Is Not Reflexive
Floating-point operations may produce `NaN` values that indicate an undefined result. These values are not comparable with each other; in particular, all comparisons involving `NaN` will return `false`, including equality.
``[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ((0.0 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) / 0.0) == ((0.0 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) / 0.0) `
[Live ↪](javascript:openLiveLink\("MQUwbghgNgBAFHADAOkTAXDAYlA9hAFwEoYB6GFREgXmviVQ2z0JPMqKA"\))
Floating-Point Equality Is Not a Congruence
Applying a function to two equal floating-point numbers may not result in equal numbers. In particular, positive and negative zero are distinct values that are equated by floating-point equality, but division by positive or negative zero yields positive or negative infinite values.
`def neg0 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") := -0.0  def pos0 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") := 0.0  `[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ([neg0](Basic-Types/Floating-Point-Numbers/#neg0-_LPAR_in-Floating-Point-Equality-Is-Not-a-Congruence_RPAR_ "Definition of example") == [pos0](Basic-Types/Floating-Point-Numbers/#pos0-_LPAR_in-Floating-Point-Equality-Is-Not-a-Congruence_RPAR_ "Definition of example"), 1.0 / [neg0](Basic-Types/Floating-Point-Numbers/#neg0-_LPAR_in-Floating-Point-Equality-Is-Not-a-Congruence_RPAR_ "Definition of example") == 1.0 / [pos0](Basic-Types/Floating-Point-Numbers/#pos0-_LPAR_in-Floating-Point-Equality-Is-Not-a-Congruence_RPAR_ "Definition of example")) `
```
[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")
```

[Live ↪](javascript:openLiveLink\("CYUwZgBAdiDmAMEBcEBiAbA9gQwC7IF4IBaeAOngChLRIAHTAZ0RQx3ySPKsoGIQAbtnQQAFDAQQCRBswA0EAIwUIAemhxE0pSvWz4ASiA"\))
##  20.6.1. Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Floating-Point-Numbers--Syntax "Permalink")
Lean does not have dedicated floating-point literals. Instead, floating-point literals are resolved via the appropriate instances of the `[OfScientific](Terms/Numeric-Literals/#OfScientific___mk "Documentation for OfScientific")` and `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg")` type classes.
Floating-Point Literals
The term
`(-2.523 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float"))`
is syntactic sugar for
`([Neg.neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg") ([OfScientific.ofScientific](Terms/Numeric-Literals/#OfScientific___mk "Documentation for OfScientific.ofScientific") 22523 [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") 4) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float"))`
and the term
`(413.52 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32"))`
is syntactic sugar for
`([OfScientific.ofScientific](Terms/Numeric-Literals/#OfScientific___mk "Documentation for OfScientific.ofScientific") 41352 [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") 2 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32"))`
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAueAKAtAJgHQYKwYGYl4AxGAezABcBKeAXlQDlgBzLAOzdQHkAzAMoBjAJbAOVEXxFCs5QaPGTpQ+BjyF4VAE4BXBABY6yMpVpJGAIwCe8AM4jo8ANr9hYiVJlyFH5TIBdAChQSFgEZBQDAEYCLHxiU2oCDDpGFDdFTxUfdyUvVRiCBJ19NUSKZNSLeBt7RygXTL8C3Kz/IQCgA"\))
##  20.6.2. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=Float-api "Permalink")
###  20.6.2.1. Properties[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Floating-Point-Numbers--API-Reference--Properties "Permalink")
Floating-point numbers fall into one of three categories:
  * Finite numbers are ordinary floating-point values.
  * Infinities, which may be positive or negative, result from division by zero.
  * `NaN`s, which are not numbers, result from other undefined operations, such as the square root of a negative number.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.isInf "Permalink")opaque
```


Float.isInf : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Float.isInf : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a floating-point number is a positive or negative infinite number, but not a finite number or `NaN`.
This function does not reduce in the kernel. It is compiled to the C operator `isinf`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.isInf "Permalink")opaque
```


Float32.isInf : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Float32.isInf : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a floating-point number is a positive or negative infinite number, but not a finite number or `NaN`.
This function does not reduce in the kernel. It is compiled to the C operator `isinf`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.isNaN "Permalink")opaque
```


Float.isNaN : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Float.isNaN : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a floating point number is `NaN` (“not a number”) value.
`NaN` values result from operations that might otherwise be errors, such as dividing zero by zero.
This function does not reduce in the kernel. It is compiled to the C operator `isnan`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.isNaN "Permalink")opaque
```


Float32.isNaN : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Float32.isNaN : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a floating point number is `NaN` ("not a number") value.
`NaN` values result from operations that might otherwise be errors, such as dividing zero by zero.
This function does not reduce in the kernel. It is compiled to the C operator `isnan`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.isFinite "Permalink")opaque
```


Float.isFinite : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Float.isFinite : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a floating-point number is finite, that is, whether it is normal, subnormal, or zero, but not infinite or `NaN`.
This function does not reduce in the kernel. It is compiled to the C operator `isfinite`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.isFinite "Permalink")opaque
```


Float32.isFinite : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Float32.isFinite : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a floating-point number is finite, that is, whether it is normal, subnormal, or zero, but not infinite or `NaN`.
This function does not reduce in the kernel. It is compiled to the C operator `isfinite`.
###  20.6.2.2. Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Floating-Point-Numbers--API-Reference--Syntax "Permalink")
These operations exist to support the `[OfScientific](Terms/Numeric-Literals/#OfScientific___mk "Documentation for OfScientific") [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` and `[OfScientific](Terms/Numeric-Literals/#OfScientific___mk "Documentation for OfScientific") [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` instances and are normally invoked indirectly as a result of a literal value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.ofScientific "Permalink")opaque
```


Float.ofScientific (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (s : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (e : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.ofScientific (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (s : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (e : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Constructs a `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` from the given mantissa, sign, and exponent values.
This function is part of the implementation of the `[OfScientific](Terms/Numeric-Literals/#OfScientific___mk "Documentation for OfScientific") [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` instance that is used to interpret floating-point literals.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.ofScientific "Permalink")opaque
```


Float32.ofScientific (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (s : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (e : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.ofScientific (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (s : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (e : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Constructs a `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` from the given mantissa, sign, and exponent values.
This function is part of the implementation of the `[OfScientific](Terms/Numeric-Literals/#OfScientific___mk "Documentation for OfScientific") [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` instance that is used to interpret floating-point literals.
###  20.6.2.3. Conversions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Floating-Point-Numbers--API-Reference--Conversions "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.toBits "Permalink")opaque
```


Float.toBits : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


Float.toBits : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Bit-for-bit conversion to `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`. Interprets a `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` as a `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`, ignoring the numeric value and treating the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")`'s bit pattern as a `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`.
`[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")`s and `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`s have the same endianness on all supported platforms. IEEE 754 very precisely specifies the bit layout of floats.
This function is distinct from `[Float.toUInt64](Basic-Types/Floating-Point-Numbers/#Float___toUInt64 "Documentation for Float.toUInt64")`, which attempts to preserve the numeric value rather than reinterpreting the bit pattern.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.toBits "Permalink")opaque
```


Float32.toBits : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


Float32.toBits : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Bit-for-bit conversion to `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")`. Interprets a `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` as a `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")`, ignoring the numeric value and treating the `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")`'s bit pattern as a `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")`.
`[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")`s and `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")`s have the same endianness on all supported platforms. IEEE 754 very precisely specifies the bit layout of floats.
This function is distinct from `[Float.toUInt32](Basic-Types/Floating-Point-Numbers/#Float___toUInt32 "Documentation for Float.toUInt32")`, which attempts to preserve the numeric value rather than reinterpreting the bit pattern.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.ofBits "Permalink")opaque
```


Float.ofBits : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.ofBits : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Bit-for-bit conversion from `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`. Interprets a `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")` as a `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")`, ignoring the numeric value and treating the `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`'s bit pattern as a `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")`.
`[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")`s and `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`s have the same endianness on all supported platforms. IEEE 754 very precisely specifies the bit layout of floats.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.ofBits "Permalink")opaque
```


Float32.ofBits : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.ofBits : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Bit-for-bit conversion from `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")`. Interprets a `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")` as a `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")`, ignoring the numeric value and treating the `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")`'s bit pattern as a `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")`.
`[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")`s and `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")`s have the same endianness on all supported platforms. IEEE 754 very precisely specifies the bit layout of floats.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.toFloat32 "Permalink")opaque
```


Float.toFloat32 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float.toFloat32 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Converts a 64-bit floating-point number to a 32-bit floating-point number. This may lose precision.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.toFloat "Permalink")opaque
```


Float32.toFloat : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float32.toFloat : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Converts a 32-bit floating-point number to a 64-bit floating-point number.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.toString "Permalink")opaque
```


Float.toString : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


Float.toString : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Converts a floating-point number to a string.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.toString "Permalink")opaque
```


Float32.toString : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


Float32.toString : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Converts a floating-point number to a string.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.toUInt8 "Permalink")opaque
```


Float.toUInt8 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


Float.toUInt8 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Converts a floating-point number to an 8-bit unsigned integer.
If the given `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is non-negative, truncates the value to a positive integer, rounding down and clamping to the range of `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")`. Returns `0` if the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is negative or `NaN`, and returns the largest `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")` value (i.e. `[UInt8.size](Basic-Types/Fixed-Precision-Integers/#UInt8___size "Documentation for UInt8.size") - 1`) if the float is larger than it.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.toInt8 "Permalink")opaque
```


Float.toInt8 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Float.toInt8 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Truncates a floating-point number to the nearest 8-bit signed integer, rounding towards zero.
If the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is larger than the maximum value for `[Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")` (including `Inf`), returns the maximum value of `[Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")` (i.e. `[Int8.maxValue](Basic-Types/Fixed-Precision-Integers/#Int8___maxValue "Documentation for Int8.maxValue")`). If it is smaller than the minimum value for `[Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")` (including `-Inf`), returns the minimum value of `[Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")` (i.e. `[Int8.minValue](Basic-Types/Fixed-Precision-Integers/#Int8___minValue "Documentation for Int8.minValue")`). If it is `NaN`, returns `0`.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.toUInt8 "Permalink")opaque
```


Float32.toUInt8 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


Float32.toUInt8 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Converts a floating-point number to an 8-bit unsigned integer.
If the given `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` is non-negative, truncates the value to a positive integer, rounding down and clamping to the range of `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")`. Returns `0` if the `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` is negative or `NaN`, and returns the largest `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")` value (i.e. `[UInt8.size](Basic-Types/Fixed-Precision-Integers/#UInt8___size "Documentation for UInt8.size") - 1`) if the float is larger than it.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.toInt8 "Permalink")opaque
```


Float32.toInt8 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Float32.toInt8 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Truncates a floating-point number to the nearest 8-bit signed integer, rounding towards zero.
If the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is larger than the maximum value for `[Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")` (including `Inf`), returns the maximum value of `[Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")` (i.e. `[Int8.maxValue](Basic-Types/Fixed-Precision-Integers/#Int8___maxValue "Documentation for Int8.maxValue")`). If it is smaller than the minimum value for `[Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")` (including `-Inf`), returns the minimum value of `[Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")` (i.e. `[Int8.minValue](Basic-Types/Fixed-Precision-Integers/#Int8___minValue "Documentation for Int8.minValue")`). If it is `NaN`, returns `0`.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.toUInt16 "Permalink")opaque
```


Float.toUInt16 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


Float.toUInt16 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Converts a floating-point number to a 16-bit unsigned integer.
If the given `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is non-negative, truncates the value to a positive integer, rounding down and clamping to the range of `[UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")`. Returns `0` if the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is negative or `NaN`, and returns the largest `[UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")` value (i.e. `[UInt16.size](Basic-Types/Fixed-Precision-Integers/#UInt16___size "Documentation for UInt16.size") - 1`) if the float is larger than it.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.toInt16 "Permalink")opaque
```


Float.toInt16 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Float.toInt16 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Truncates a floating-point number to the nearest 16-bit signed integer, rounding towards zero.
If the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is larger than the maximum value for `[Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")` (including `Inf`), returns the maximum value of `[Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")` (i.e. `[Int16.maxValue](Basic-Types/Fixed-Precision-Integers/#Int16___maxValue "Documentation for Int16.maxValue")`). If it is smaller than the minimum value for `[Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")` (including `-Inf`), returns the minimum value of `[Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")` (i.e. `[Int16.minValue](Basic-Types/Fixed-Precision-Integers/#Int16___minValue "Documentation for Int16.minValue")`). If it is `NaN`, returns `0`.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.toUInt16 "Permalink")opaque
```


Float32.toUInt16 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


Float32.toUInt16 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Converts a floating-point number to a 16-bit unsigned integer.
If the given `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` is non-negative, truncates the value to a positive integer, rounding down and clamping to the range of `[UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")`. Returns `0` if the `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` is negative or `NaN`, and returns the largest `[UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")` value (i.e. `[UInt16.size](Basic-Types/Fixed-Precision-Integers/#UInt16___size "Documentation for UInt16.size") - 1`) if the float is larger than it.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.toInt16 "Permalink")opaque
```


Float32.toInt16 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Float32.toInt16 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Truncates a floating-point number to the nearest 16-bit signed integer, rounding towards zero.
If the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is larger than the maximum value for `[Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")` (including `Inf`), returns the maximum value of `[Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")` (i.e. `[Int16.maxValue](Basic-Types/Fixed-Precision-Integers/#Int16___maxValue "Documentation for Int16.maxValue")`). If it is smaller than the minimum value for `[Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")` (including `-Inf`), returns the minimum value of `[Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")` (i.e. `[Int16.minValue](Basic-Types/Fixed-Precision-Integers/#Int16___minValue "Documentation for Int16.minValue")`). If it is `NaN`, returns `0`.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.toUInt32 "Permalink")opaque
```


Float.toUInt32 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


Float.toUInt32 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Converts a floating-point number to a 32-bit unsigned integer.
If the given `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is non-negative, truncates the value to a positive integer, rounding down and clamping to the range of `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")`. Returns `0` if the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is negative or `NaN`, and returns the largest `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")` value (i.e. `[UInt32.size](Basic-Types/Fixed-Precision-Integers/#UInt32___size "Documentation for UInt32.size") - 1`) if the float is larger than it.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.toUInt32 "Permalink")opaque
```


Float32.toUInt32 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


Float32.toUInt32 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Converts a floating-point number to a 32-bit unsigned integer.
If the given `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` is non-negative, truncates the value to a positive integer, rounding down and clamping to the range of `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")`. Returns `0` if the `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` is negative or `NaN`, and returns the largest `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")` value (i.e. `[UInt32.size](Basic-Types/Fixed-Precision-Integers/#UInt32___size "Documentation for UInt32.size") - 1`) if the float is larger than it.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.toInt32 "Permalink")opaque
```


Float.toInt32 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Float.toInt32 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Truncates a floating-point number to the nearest 32-bit signed integer, rounding towards zero.
If the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is larger than the maximum value for `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` (including `Inf`), returns the maximum value of `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` (i.e. `[Int32.maxValue](Basic-Types/Fixed-Precision-Integers/#Int32___maxValue "Documentation for Int32.maxValue")`). If it is smaller than the minimum value for `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` (including `-Inf`), returns the minimum value of `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` (i.e. `[Int32.minValue](Basic-Types/Fixed-Precision-Integers/#Int32___minValue "Documentation for Int32.minValue")`). If it is `NaN`, returns `0`.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.toInt32 "Permalink")opaque
```


Float32.toInt32 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Float32.toInt32 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Truncates a floating-point number to the nearest 32-bit signed integer, rounding towards zero.
If the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is larger than the maximum value for `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` (including `Inf`), returns the maximum value of `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` (i.e. `[Int32.maxValue](Basic-Types/Fixed-Precision-Integers/#Int32___maxValue "Documentation for Int32.maxValue")`). If it is smaller than the minimum value for `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` (including `-Inf`), returns the minimum value of `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` (i.e. `[Int32.minValue](Basic-Types/Fixed-Precision-Integers/#Int32___minValue "Documentation for Int32.minValue")`). If it is `NaN`, returns `0`.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.toUInt64 "Permalink")opaque
```


Float.toUInt64 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


Float.toUInt64 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Converts a floating-point number to a 64-bit unsigned integer.
If the given `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is non-negative, truncates the value to a positive integer, rounding down and clamping to the range of `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`. Returns `0` if the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is negative or `NaN`, and returns the largest `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")` value (i.e. `[UInt64.size](Basic-Types/Fixed-Precision-Integers/#UInt64___size "Documentation for UInt64.size") - 1`) if the float is larger than it.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.toInt64 "Permalink")opaque
```


Float.toInt64 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Float.toInt64 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Truncates a floating-point number to the nearest 64-bit signed integer, rounding towards zero.
If the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is larger than the maximum value for `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` (including `Inf`), returns the maximum value of `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` (i.e. `[Int64.maxValue](Basic-Types/Fixed-Precision-Integers/#Int64___maxValue "Documentation for Int64.maxValue")`). If it is smaller than the minimum value for `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` (including `-Inf`), returns the minimum value of `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` (i.e. `[Int64.minValue](Basic-Types/Fixed-Precision-Integers/#Int64___minValue "Documentation for Int64.minValue")`). If it is `NaN`, returns `0`.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.toUInt64 "Permalink")opaque
```


Float32.toUInt64 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


Float32.toUInt64 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Converts a floating-point number to a 64-bit unsigned integer.
If the given `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` is non-negative, truncates the value to a positive integer, rounding down and clamping to the range of `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`. Returns `0` if the `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` is negative or `NaN`, and returns the largest `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")` value (i.e. `[UInt64.size](Basic-Types/Fixed-Precision-Integers/#UInt64___size "Documentation for UInt64.size") - 1`) if the float is larger than it.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.toInt64 "Permalink")opaque
```


Float32.toInt64 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Float32.toInt64 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Truncates a floating-point number to the nearest 64-bit signed integer, rounding towards zero.
If the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is larger than the maximum value for `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` (including `Inf`), returns the maximum value of `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` (i.e. `[Int64.maxValue](Basic-Types/Fixed-Precision-Integers/#Int64___maxValue "Documentation for Int64.maxValue")`). If it is smaller than the minimum value for `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` (including `-Inf`), returns the minimum value of `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` (i.e. `[Int64.minValue](Basic-Types/Fixed-Precision-Integers/#Int64___minValue "Documentation for Int64.minValue")`). If it is `NaN`, returns `0`.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.toUSize "Permalink")opaque
```


Float.toUSize : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


Float.toUSize : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Converts a floating-point number to a word-sized unsigned integer.
If the given `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is non-negative, truncates the value to a positive integer, rounding down and clamping to the range of `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")`. Returns `0` if the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is negative or `NaN`, and returns the largest `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")` value (i.e. `[USize.size](Basic-Types/Fixed-Precision-Integers/#USize___size "Documentation for USize.size") - 1`) if the float is larger than it.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.toUSize "Permalink")opaque
```


Float32.toUSize : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


Float32.toUSize : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Converts a floating-point number to a word-sized unsigned integer.
If the given `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` is non-negative, truncates the value to a positive integer, rounding down and clamping to the range of `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")`. Returns `0` if the `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` is negative or `NaN`, and returns the largest `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")` value (i.e. `[USize.size](Basic-Types/Fixed-Precision-Integers/#USize___size "Documentation for USize.size") - 1`) if the float is larger than it.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.toISize "Permalink")opaque
```


Float.toISize : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


Float.toISize : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Truncates a floating-point number to the nearest word-sized signed integer, rounding towards zero.
If the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is larger than the maximum value for `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` (including `Inf`), returns the maximum value of `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` (i.e. `[ISize.maxValue](Basic-Types/Fixed-Precision-Integers/#ISize___maxValue "Documentation for ISize.maxValue")`). If it is smaller than the minimum value for `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` (including `-Inf`), returns the minimum value of `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` (i.e. `[ISize.minValue](Basic-Types/Fixed-Precision-Integers/#ISize___minValue "Documentation for ISize.minValue")`). If it is `NaN`, returns `0`.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.toISize "Permalink")opaque
```


Float32.toISize : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


Float32.toISize : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Truncates a floating-point number to the nearest word-sized signed integer, rounding towards zero.
If the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is larger than the maximum value for `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` (including `Inf`), returns the maximum value of `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` (i.e. `[ISize.maxValue](Basic-Types/Fixed-Precision-Integers/#ISize___maxValue "Documentation for ISize.maxValue")`). If it is smaller than the minimum value for `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` (including `-Inf`), returns the minimum value of `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` (i.e. `[ISize.minValue](Basic-Types/Fixed-Precision-Integers/#ISize___minValue "Documentation for ISize.minValue")`). If it is `NaN`, returns `0`.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.ofInt "Permalink")def
```


Float.ofInt : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.ofInt : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Converts an integer into the closest-possible 64-bit floating-point number, or positive or negative infinite floating-point value if the range of `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is exceeded.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.ofInt "Permalink")def
```


Float32.ofInt : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.ofInt : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Converts an integer into the closest-possible 32-bit floating-point number, or positive or negative infinite floating-point value if the range of `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` is exceeded.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.ofNat "Permalink")def
```


Float.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Converts a natural number into the closest-possible 64-bit floating-point number, or an infinite floating-point value if the range of `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is exceeded.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.ofNat "Permalink")def
```


Float32.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Converts a natural number into the closest-possible 32-bit floating-point number, or an infinite floating-point value if the range of `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` is exceeded.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.ofBinaryScientific "Permalink")def
```


Float.ofBinaryScientific (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (e : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.ofBinaryScientific (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (e : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes `m * 2^e`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.ofBinaryScientific "Permalink")def
```


Float32.ofBinaryScientific (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (e : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.ofBinaryScientific (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (e : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes `m * 2^e`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.frExp "Permalink")opaque
```


Float.frExp : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Float.frExp : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Splits the given float `x` into a significand/exponent pair `(s, i)` such that `x = s * 2^i` where `s ∈ (-1;-0.5] ∪ [0.5; 1)`. Returns an undefined value if `x` is not finite.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `frexp`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.frExp "Permalink")opaque
```


Float32.frExp : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Float32.frExp : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Splits the given float `x` into a significand/exponent pair `(s, i)` such that `x = s * 2^i` where `s ∈ (-1;-0.5] ∪ [0.5; 1)`. Returns an undefined value if `x` is not finite.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `frexp`.
###  20.6.2.4. Comparisons[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Floating-Point-Numbers--API-Reference--Comparisons "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.beq "Permalink")opaque
```


Float.beq (a b : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Float.beq (a b : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether two floating-point numbers are equal according to IEEE 754.
Floating-point equality does not correspond with propositional equality. In particular, it is not reflexive since `NaN != NaN`, and it is not a congruence because `0.0 == -0.0`, but `1.0 / 0.0 != 1.0 / -0.0`.
This function does not reduce in the kernel. It is compiled to the C equality operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.beq "Permalink")opaque
```


Float32.beq (a b : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Float32.beq (a b : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether two floating-point numbers are equal according to IEEE 754.
Floating-point equality does not correspond with propositional equality. In particular, it is not reflexive since `NaN != NaN`, and it is not a congruence because `0.0 == -0.0`, but `1.0 / 0.0 != 1.0 / -0.0`.
This function does not reduce in the kernel. It is compiled to the C equality operator.
####  20.6.2.4.1. Inequalities[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Floating-Point-Numbers--API-Reference--Comparisons--Inequalities "Permalink")
The decision procedures for inequalities are opaque constants in the logic. They can only be used via the `Lean.ofReduceBool` axiom, e.g. via the `[native_decide](Tactic-Proofs/Tactic-Reference/#native_decide "Documentation for tactic")` tactic.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.le "Permalink")def
```


Float.le : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → Prop


Float.le : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → Prop


```

Non-strict inequality of floating-point numbers. Typically used via the `≤` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.le "Permalink")def
```


Float32.le : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → Prop


Float32.le : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → Prop


```

Non-strict inequality of floating-point numbers. Typically used via the `≤` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.lt "Permalink")def
```


Float.lt : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → Prop


Float.lt : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → Prop


```

Strict inequality of floating-point numbers. Typically used via the `<` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.lt "Permalink")def
```


Float32.lt : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → Prop


Float32.lt : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → Prop


```

Strict inequality of floating-point numbers. Typically used via the `<` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.decLe "Permalink")opaque
```


Float.decLe (a b : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


Float.decLe (a b : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


```

Compares two floating point numbers for non-strict inequality.
This function does not reduce in the kernel. It is compiled to the C inequality operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.decLe "Permalink")opaque
```


Float32.decLe (a b : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


Float32.decLe (a b : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


```

Compares two floating point numbers for non-strict inequality.
This function does not reduce in the kernel. It is compiled to the C inequality operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.decLt "Permalink")opaque
```


Float.decLt (a b : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


Float.decLt (a b : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


```

Compares two floating point numbers for strict inequality.
This function does not reduce in the kernel. It is compiled to the C inequality operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.decLt "Permalink")opaque
```


Float32.decLt (a b : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


Float32.decLt (a b : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


```

Compares two floating point numbers for strict inequality.
This function does not reduce in the kernel. It is compiled to the C inequality operator.
###  20.6.2.5. Arithmetic[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Floating-Point-Numbers--API-Reference--Arithmetic "Permalink")
Arithmetic operations on floating-point values are typically invoked via the `[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")`, `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")`, `[Mul](Type-Classes/Basic-Classes/#Mul___mk "Documentation for Mul") [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")`, `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")`, and `[HomogeneousPow](Type-Classes/Basic-Classes/#HomogeneousPow___mk "Documentation for HomogeneousPow") [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` instances, along with the corresponding `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` instances.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.add "Permalink")opaque
```


Float.add : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.add : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Adds two 64-bit floating-point numbers according to IEEE 754. Typically used via the `+` operator.
This function does not reduce in the kernel. It is compiled to the C addition operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.add "Permalink")opaque
```


Float32.add : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.add : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Adds two 32-bit floating-point numbers according to IEEE 754. Typically used via the `+` operator.
This function does not reduce in the kernel. It is compiled to the C addition operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.sub "Permalink")opaque
```


Float.sub : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.sub : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Subtracts 64-bit floating-point numbers according to IEEE 754. Typically used via the `-` operator.
This function does not reduce in the kernel. It is compiled to the C subtraction operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.sub "Permalink")opaque
```


Float32.sub : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.sub : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Subtracts 32-bit floating-point numbers according to IEEE 754. Typically used via the `-` operator.
This function does not reduce in the kernel. It is compiled to the C subtraction operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.mul "Permalink")opaque
```


Float.mul : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.mul : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Multiplies 64-bit floating-point numbers according to IEEE 754. Typically used via the `*` operator.
This function does not reduce in the kernel. It is compiled to the C multiplication operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.mul "Permalink")opaque
```


Float32.mul : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.mul : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Multiplies 32-bit floating-point numbers according to IEEE 754. Typically used via the `*` operator.
This function does not reduce in the kernel. It is compiled to the C multiplication operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.div "Permalink")opaque
```


Float.div : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.div : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Divides 64-bit floating-point numbers according to IEEE 754. Typically used via the `/` operator.
In Lean, division by zero typically yields zero. For `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")`, it instead yields either `Inf`, `-Inf`, or `NaN`.
This function does not reduce in the kernel. It is compiled to the C division operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.div "Permalink")opaque
```


Float32.div : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.div : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Divides 32-bit floating-point numbers according to IEEE 754. Typically used via the `/` operator.
In Lean, division by zero typically yields zero. For `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")`, it instead yields either `Inf`, `-Inf`, or `NaN`.
This function does not reduce in the kernel. It is compiled to the C division operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.pow "Permalink")opaque
```


Float.pow : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.pow : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Raises one floating-point number to the power of another. Typically used via the `^` operator.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `pow`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.pow "Permalink")opaque
```


Float32.pow : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.pow : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Raises one floating-point number to the power of another. Typically used via the `^` operator.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `powf`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.exp "Permalink")opaque
```


Float.exp (x : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.exp (x : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the exponential `e^x` of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `exp`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.exp "Permalink")opaque
```


Float32.exp : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.exp : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the exponential `e^x` of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `expf`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.exp2 "Permalink")opaque
```


Float.exp2 (x : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.exp2 (x : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the base-2 exponential `2^x` of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `exp2`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.exp2 "Permalink")opaque
```


Float32.exp2 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.exp2 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the base-2 exponential `2^x` of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `exp2f`.
####  20.6.2.5.1. Roots[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Floating-Point-Numbers--API-Reference--Arithmetic--Roots "Permalink")
Computing the square root of a negative number yields `NaN`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.sqrt "Permalink")opaque
```


Float.sqrt : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.sqrt : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the square root of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `sqrt`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.sqrt "Permalink")opaque
```


Float32.sqrt : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.sqrt : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the square root of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `sqrtf`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.cbrt "Permalink")opaque
```


Float.cbrt : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.cbrt : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the cube root of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `cbrt`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.cbrt "Permalink")opaque
```


Float32.cbrt : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.cbrt : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the cube root of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `cbrtf`.
###  20.6.2.6. Logarithms[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Floating-Point-Numbers--API-Reference--Logarithms "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.log "Permalink")opaque
```


Float.log (x : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.log (x : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the natural logarithm `ln x` of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `log`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.log "Permalink")opaque
```


Float32.log : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.log : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the natural logarithm `ln x` of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `logf`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.log10 "Permalink")opaque
```


Float.log10 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.log10 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the base-10 logarithm of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `log10`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.log10 "Permalink")opaque
```


Float32.log10 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.log10 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the base-10 logarithm of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `log10f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.log2 "Permalink")opaque
```


Float.log2 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.log2 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the base-2 logarithm of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `log2`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.log2 "Permalink")opaque
```


Float32.log2 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.log2 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the base-2 logarithm of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `log2f`.
###  20.6.2.7. Scaling[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Floating-Point-Numbers--API-Reference--Scaling "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.scaleB "Permalink")opaque
```


Float.scaleB (x : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.scaleB (x : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Efficiently computes `x * 2^i`.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.scaleB "Permalink")opaque
```


Float32.scaleB (x : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")) (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.scaleB (x : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")) (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) :
  [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Efficiently computes `x * 2^i`.
This function does not reduce in the kernel.
###  20.6.2.8. Rounding[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Floating-Point-Numbers--API-Reference--Rounding "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.round "Permalink")opaque
```


Float.round : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.round : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Rounds to the nearest integer, rounding away from zero at half-way points.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `round`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.round "Permalink")opaque
```


Float32.round : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.round : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Rounds to the nearest integer, rounding away from zero at half-way points.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `roundf`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.floor "Permalink")opaque
```


Float.floor : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.floor : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the floor of a floating-point number, which is the largest integer that's no larger than the given number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `floor`.
Examples:
  * `[Float.floor](Basic-Types/Floating-Point-Numbers/#Float___floor "Documentation for Float.floor") 1.5 = 1`
  * `[Float.floor](Basic-Types/Floating-Point-Numbers/#Float___floor "Documentation for Float.floor") (-1.5) = (-2)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.floor "Permalink")opaque
```


Float32.floor : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.floor : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the floor of a floating-point number, which is the largest integer that's no larger than the given number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `floorf`.
Examples:
  * `[Float32.floor](Basic-Types/Floating-Point-Numbers/#Float32___floor "Documentation for Float32.floor") 1.5 = 1`
  * `[Float32.floor](Basic-Types/Floating-Point-Numbers/#Float32___floor "Documentation for Float32.floor") (-1.5) = (-2)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.ceil "Permalink")opaque
```


Float.ceil : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.ceil : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the ceiling of a floating-point number, which is the smallest integer that's no smaller than the given number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `ceil`.
Examples:
  * `[Float.ceil](Basic-Types/Floating-Point-Numbers/#Float___ceil "Documentation for Float.ceil") 1.5 = 2`
  * `[Float.ceil](Basic-Types/Floating-Point-Numbers/#Float___ceil "Documentation for Float.ceil") (-1.5) = (-1)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.ceil "Permalink")opaque
```


Float32.ceil : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.ceil : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the ceiling of a floating-point number, which is the smallest integer that's no smaller than the given number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `ceilf`.
Examples:
  * `[Float32.ceil](Basic-Types/Floating-Point-Numbers/#Float32___ceil "Documentation for Float32.ceil") 1.5 = 2`
  * `[Float32.ceil](Basic-Types/Floating-Point-Numbers/#Float32___ceil "Documentation for Float32.ceil") (-1.5) = (-1)`


###  20.6.2.9. Trigonometry[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Floating-Point-Numbers--API-Reference--Trigonometry "Permalink")
####  20.6.2.9.1. Sine[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Floating-Point-Numbers--API-Reference--Trigonometry--Sine "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.sin "Permalink")opaque
```


Float.sin : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.sin : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the sine of a floating-point number in radians.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `sin`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.sin "Permalink")opaque
```


Float32.sin : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.sin : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the sine of a floating-point number in radians.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `sinf`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.sinh "Permalink")opaque
```


Float.sinh : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.sinh : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the hyperbolic sine of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `sinh`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.sinh "Permalink")opaque
```


Float32.sinh : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.sinh : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the hyperbolic sine of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `sinhf`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.asin "Permalink")opaque
```


Float.asin : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.asin : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the arc sine (inverse sine) of a floating-point number in radians.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `asin`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.asin "Permalink")opaque
```


Float32.asin : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.asin : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the arc sine (inverse sine) of a floating-point number in radians.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `asinf`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.asinh "Permalink")opaque
```


Float.asinh : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.asinh : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the hyperbolic arc sine (inverse sine) of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `asinh`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.asinh "Permalink")opaque
```


Float32.asinh : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.asinh : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the hyperbolic arc sine (inverse sine) of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `asinhf`.
####  20.6.2.9.2. Cosine[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Floating-Point-Numbers--API-Reference--Trigonometry--Cosine "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.cos "Permalink")opaque
```


Float.cos : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.cos : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the cosine of a floating-point number in radians.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `cos`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.cos "Permalink")opaque
```


Float32.cos : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.cos : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the cosine of a floating-point number in radians.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `cosf`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.cosh "Permalink")opaque
```


Float.cosh : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.cosh : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the hyperbolic cosine of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `cosh`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.cosh "Permalink")opaque
```


Float32.cosh : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.cosh : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the hyperbolic cosine of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `coshf`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.acos "Permalink")opaque
```


Float.acos : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.acos : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the arc cosine (inverse cosine) of a floating-point number in radians.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `acos`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.acos "Permalink")opaque
```


Float32.acos : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.acos : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the arc cosine (inverse cosine) of a floating-point number in radians.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `acosf`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.acosh "Permalink")opaque
```


Float.acosh : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.acosh : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the hyperbolic arc cosine (inverse cosine) of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `acosh`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.acosh "Permalink")opaque
```


Float32.acosh : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.acosh : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the hyperbolic arc cosine (inverse cosine) of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `acoshf`.
####  20.6.2.9.3. Tangent[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Floating-Point-Numbers--API-Reference--Trigonometry--Tangent "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.tan "Permalink")opaque
```


Float.tan : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.tan : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the tangent of a floating-point number in radians.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `tan`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.tan "Permalink")opaque
```


Float32.tan : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.tan : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the tangent of a floating-point number in radians.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `tanf`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.tanh "Permalink")opaque
```


Float.tanh : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.tanh : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the hyperbolic tangent of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `tanh`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.tanh "Permalink")opaque
```


Float32.tanh : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.tanh : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the hyperbolic tangent of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `tanhf`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.atan "Permalink")opaque
```


Float.atan : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.atan : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the arc tangent (inverse tangent) of a floating-point number in radians.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `atan`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.atan "Permalink")opaque
```


Float32.atan : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.atan : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the arc tangent (inverse tangent) of a floating-point number in radians.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `atanf`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.atanh "Permalink")opaque
```


Float.atanh : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.atanh : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the hyperbolic arc tangent (inverse tangent) of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `atanh`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.atanh "Permalink")opaque
```


Float32.atanh : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.atanh : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the hyperbolic arc tangent (inverse tangent) of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `atanhf`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.atan2 "Permalink")opaque
```


Float.atan2 (y x : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.atan2 (y x : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the arc tangent (inverse tangent) of `y / x` in radians, in the range `-π`–`π`. The signs of the arguments determine the quadrant of the result.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `atan2`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.atan2 "Permalink")opaque
```


Float32.atan2 : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.atan2 :
  [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the arc tangent (inverse tangent) of `y / x` in radians, in the range `-π`–`π`. The signs of the arguments determine the quadrant of the result.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `atan2f`.
###  20.6.2.10. Negation and Absolute Value[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Floating-Point-Numbers--API-Reference--Negation-and-Absolute-Value "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.abs "Permalink")opaque
```


Float.abs : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.abs : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Computes the absolute value of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `fabs`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.abs "Permalink")opaque
```


Float32.abs : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.abs : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Computes the absolute value of a floating-point number.
This function does not reduce in the kernel. It is implemented in compiled code by the C function `fabsf`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float.neg "Permalink")opaque
```


Float.neg : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Float.neg : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float") → [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Negates 64-bit floating-point numbers according to IEEE 754. Typically used via the `-` prefix operator.
This function does not reduce in the kernel. It is compiled to the C negation operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Float32.neg "Permalink")opaque
```


Float32.neg : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Float32.neg : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32") → [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Negates 32-bit floating-point numbers according to IEEE 754. Typically used via the `-` prefix operator.
This function does not reduce in the kernel. It is compiled to the C negation operator.
[←20.5. Bitvectors](Basic-Types/Bitvectors/#BitVec "20.5. Bitvectors")[20.7. Characters→](Basic-Types/Characters/#Char "20.7. Characters")

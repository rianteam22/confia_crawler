[←20.3. Finite Natural Numbers](Basic-Types/Finite-Natural-Numbers/#Fin "20.3. Finite Natural Numbers")[20.5. Bitvectors→](Basic-Types/Bitvectors/#BitVec "20.5. Bitvectors")
#  20.4. Fixed-Precision Integers[🔗](find/?domain=Verso.Genre.Manual.section&name=fixed-ints "Permalink")
Lean's standard library includes the usual assortment of fixed-width integer types. From the perspective of formalization and proofs, these types are wrappers around bitvectors of the appropriate size; the wrappers ensure that the correct implementations of e.g. arithmetic operations are applied. In compiled code, they are represented efficiently: the compiler has special support for them, as it does for other fundamental types.
##  20.4.1. Logical Model[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Fixed-Precision-Integers--Logical-Model "Permalink")
Fixed-width integers may be unsigned or signed. Furthermore, they are available in five sizes: 8, 16, 32, and 64 bits, along with the current architecture's word size. In their logical models, the unsigned integers are structures that wrap a `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec")` of the appropriate width. Signed integers wrap the corresponding unsigned integers, and use a twos-complement representation.
###  20.4.1.1. Unsigned[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Fixed-Precision-Integers--Logical-Model--Unsigned "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize "Permalink")structure
```


USize : Type


USize : Type


```

Unsigned integers that are the size of a word on the platform's architecture.
On a 32-bit architecture, `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")` is equivalent to `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")`. On a 64-bit machine, it is equivalent to `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`.
#  Constructor

```
[USize.ofBitVec](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize.ofBitVec")
```

Creates a `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")` from a `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [System.Platform.numBits](IO/System-and-Platform-Information/#System___Platform___numBits "Documentation for System.Platform.numBits")`. This function is overridden with a native implementation.
#  Fields

```
toBitVec : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [System.Platform.numBits](IO/System-and-Platform-Information/#System___Platform___numBits "Documentation for System.Platform.numBits")
```

Unpacks a `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")` into a `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [System.Platform.numBits](IO/System-and-Platform-Information/#System___Platform___numBits "Documentation for System.Platform.numBits")`. This function is overridden with a native implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.toBitVec "Permalink")structure
```


UInt8 : Type


UInt8 : Type


```

Unsigned 8-bit integers.
This type has special support in the compiler so it can be represented by an unboxed 8-bit value rather than wrapping a `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 8`.
#  Constructor

```
[UInt8.ofBitVec](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8.ofBitVec")
```

Creates a `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")` from a `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 8`. This function is overridden with a native implementation.
#  Fields

```
toBitVec : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 8
```

Unpacks a `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")` into a `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 8`. This function is overridden with a native implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.toBitVec "Permalink")structure
```


UInt16 : Type


UInt16 : Type


```

Unsigned 16-bit integers.
This type has special support in the compiler so it can be represented by an unboxed 16-bit value rather than wrapping a `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 16`.
#  Constructor

```
[UInt16.ofBitVec](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16.ofBitVec")
```

Creates a `[UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")` from a `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 16`. This function is overridden with a native implementation.
#  Fields

```
toBitVec : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 16
```

Unpacks a `[UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")` into a `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 16`. This function is overridden with a native implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.ofBitVec "Permalink")structure
```


UInt32 : Type


UInt32 : Type


```

Unsigned 32-bit integers.
This type has special support in the compiler so it can be represented by an unboxed 32-bit value rather than wrapping a `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32`.
#  Constructor

```
[UInt32.ofBitVec](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32.ofBitVec")
```

Creates a `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")` from a `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32`. This function is overridden with a native implementation.
#  Fields

```
toBitVec : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32
```

Unpacks a `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")` into a `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32`. This function is overridden with a native implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.ofBitVec "Permalink")structure
```


UInt64 : Type


UInt64 : Type


```

Unsigned 64-bit integers.
This type has special support in the compiler so it can be represented by an unboxed 64-bit value rather than wrapping a `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 64`.
#  Constructor

```
[UInt64.ofBitVec](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64.ofBitVec")
```

Creates a `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")` from a `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 64`. This function is overridden with a native implementation.
#  Fields

```
toBitVec : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 64
```

Unpacks a `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")` into a `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 64`. This function is overridden with a native implementation.
###  20.4.1.2. Signed[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Fixed-Precision-Integers--Logical-Model--Signed "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize "Permalink")structure
```


ISize : Type


ISize : Type


```

Signed integers that are the size of a word on the platform's architecture.
On a 32-bit architecture, `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` is equivalent to `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")`. On a 64-bit machine, it is equivalent to `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")`. This type has special support in the compiler so it can be represented by an unboxed value.
#  Constructor

```
[ISize.ofUSize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize.ofUSize")
```

#  Fields

```
toUSize : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")
```

Converts a word-sized signed integer into the word-sized unsigned integer that is its two's complement encoding.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.toUInt8 "Permalink")structure
```


Int8 : Type


Int8 : Type


```

Signed 8-bit integers.
This type has special support in the compiler so it can be represented by an unboxed 8-bit value.
#  Constructor

```
[Int8.ofUInt8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8.ofUInt8")
```

#  Fields

```
toUInt8 : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")
```

Converts an 8-bit signed integer into the 8-bit unsigned integer that is its two's complement encoding.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16 "Permalink")structure
```


Int16 : Type


Int16 : Type


```

Signed 16-bit integers.
This type has special support in the compiler so it can be represented by an unboxed 16-bit value.
#  Constructor

```
[Int16.ofUInt16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16.ofUInt16")
```

#  Fields

```
toUInt16 : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")
```

Converts an 16-bit signed integer into the 16-bit unsigned integer that is its two's complement encoding.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.ofUInt32 "Permalink")structure
```


Int32 : Type


Int32 : Type


```

Signed 32-bit integers.
This type has special support in the compiler so it can be represented by an unboxed 32-bit value.
#  Constructor

```
[Int32.ofUInt32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32.ofUInt32")
```

#  Fields

```
toUInt32 : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")
```

Converts an 32-bit signed integer into the 32-bit unsigned integer that is its two's complement encoding.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.ofUInt64 "Permalink")structure
```


Int64 : Type


Int64 : Type


```

Signed 64-bit integers.
This type has special support in the compiler so it can be represented by an unboxed 64-bit value.
#  Constructor

```
[Int64.ofUInt64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64.ofUInt64")
```

#  Fields

```
toUInt64 : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")
```

Converts an 64-bit signed integer into the 64-bit unsigned integer that is its two's complement encoding.
##  20.4.2. Run-Time Representation[🔗](find/?domain=Verso.Genre.Manual.section&name=fixed-int-runtime "Permalink")
In compiled code in contexts that require [boxed](Run-Time-Code/Boxing/#--tech-term-Boxed) representations, fixed-width integer types that fit in one less bit than the platform's pointer size are always represented without additional allocations or indirections. This always includes `[Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")`, `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")`, `[Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")`, and `[UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")`. On 64-bit architectures, `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` and `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")` are also represented without pointers. On 32-bit architectures, `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` and `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")` require a pointer to an object on the heap. `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")`, `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")`, `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` and `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")` may require pointers on all architectures.
Even though some fixed-with integer types require boxing in general, the compiler is able to represent them without boxing or pointer indirections in code paths that use only a specific fixed-width type rather than being polymorphic, potentially after a specialization pass. This applies in most practical situations where these types are used: their values are represented using the corresponding unsigned fixed-width C type when a constructor parameter, function parameter, function return value, or intermediate result is known to be a fixed-width integer type. The Lean run-time system includes primitives for storing fixed-width integers in constructors of [inductive types](The-Type-System/Inductive-Types/#--tech-term-Inductive-types), and the primitive operations are defined on the corresponding C types, so boxing tends to happen at the “edges” of integer calculations rather than for each intermediate result. In contexts where other types might occur, such as the contents of polymorphic containers like `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")`, these types are boxed, even if an array is statically known to contain only a single fixed-width integer type.The monomorphic array type `[ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")` avoids boxing for arrays of `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")`. Lean does not specialize the representation of inductive types or arrays. Inspecting a function's type in Lean is not sufficient to determine how fixed-width integer values will be represented, because boxed values are not eagerly unboxed—a function that projects an `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` from an array returns a boxed integer value.
##  20.4.3. Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Fixed-Precision-Integers--Syntax "Permalink")
All the fixed-width integer types have `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat")` instances, which allow numerals to be used as literals, both in expression and in pattern contexts. The signed types additionally have `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg")` instances, allowing negation to be applied.
Fixed-Width Literals
Lean allows both decimal and hexadecimal literals to be used for types with `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat")` instances. In this example, literal notation is used to define masks.
`structure Permissions where   readable : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")   writable : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")   executable : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")  def Permissions.encode (p : [Permissions](Basic-Types/Fixed-Precision-Integers/#Permissions-_LPAR_in-Fixed-Width-Literals_RPAR_ "Definition of example")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") :=   let r := [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") p.[readable](Basic-Types/Fixed-Precision-Integers/#Permissions___readable-_LPAR_in-Fixed-Width-Literals_RPAR_ "Definition of example") [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 0x01 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 0   let w := [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") p.[writable](Basic-Types/Fixed-Precision-Integers/#Permissions___writable-_LPAR_in-Fixed-Width-Literals_RPAR_ "Definition of example") [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 0x02 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 0   let x := [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") p.[executable](Basic-Types/Fixed-Precision-Integers/#Permissions___executable-_LPAR_in-Fixed-Width-Literals_RPAR_ "Definition of example") [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 0x04 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 0   r ||| w ||| x  def Permissions.decode (i : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [Permissions](Basic-Types/Fixed-Precision-Integers/#Permissions-_LPAR_in-Fixed-Width-Literals_RPAR_ "Definition of example") :=   ⟨i &&& 0x01 ≠ 0, i &&& 0x02 ≠ 0, i &&& 0x04 ≠ 0⟩ `
[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgArzAWwJbGJg9gHbCIDuAFmvAFCKIICGAJvQEYA2SAXIgEJ55sapMJhCsOibnwFD4AD3hQIY9l179BVRvABmKNFhz4iAOngEoebYgAUAB0n6M2XIWABKRwFUAkgRAAHJIAvEIcIHQhiJh6diYMzKqIIBQEiAAMcukAjIjwbMBI6WHwESRRMYhxJCIqEinmGVkATHkFRSURchWxZgpKdUgNaZnpACxthRlCYIgAPguk84tyVFq6ToauptqW1jaY3n6BntyozkZuIUKAF+SHAGSPTTmIgAZEGQA00YiP98+t73SXweT1GE0BgEvyNYAWmhiAAwhQoABrZIURCsPAAN2oDTwCHQmxcxmAJl2VngAH1zHskPZHOctiTTlVEMFEGTFBTbHEaRTTuyWABPTqIG5gL4kL5yCFROxCKD0QrEWYAHgA3AA+RCK5VLDXa3XwYjdA1CXDoBwAal2mGsAG1ydoALpAA"\))
Literals that overflow their types' precision are interpreted modulus the precision. Signed types, are interpreted according to the underlying twos-complement representation.
Overflowing Fixed-Width Literals
The following statements are all true:
`example : (255 : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) = 255 := by⊢ 255 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 255 [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 example : (256 : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) = 0   := by⊢ 256 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 example : (257 : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) = 1   := by⊢ 257 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1 [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙  example : (0x7f : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) = 127  := by⊢ 127 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 127 [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 example : (0x8f : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) = -113 := by⊢ 143 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") -113 [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 example : (0xff : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) = -1   := by⊢ 255 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") -1 [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAueAKATAVg0+BVAkgHYAuAHAJTwC88m2iNARgJ7wBOAZjAFCiSwJk6DADYcBEhWrwADPHkN4Ldl17hocHMIDs4omUo0AjPKRNWnHmv6ahMkNo459U42l1mlF1Xw2DU9qROyC6G8AC0RkYAzJ7KltZ+WvYcwfCh0pGmivFcQA"\))
##  20.4.4. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Fixed-Precision-Integers--API-Reference "Permalink")
###  20.4.4.1. Sizes[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Fixed-Precision-Integers--API-Reference--Sizes "Permalink")
Each fixed-width integer has a _size_ , which is the number of distinct values that can be represented by the type. This is not equivalent to C's `sizeof` operator, which instead determines how many bytes the type occupies.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.size "Permalink")def
```


USize.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


USize.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of distinct values representable by `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")`, that is, `2^[System.Platform.numBits](IO/System-and-Platform-Information/#System___Platform___numBits "Documentation for System.Platform.numBits")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.size "Permalink")def
```


ISize.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


ISize.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of distinct values representable by `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")`, that is, `2^[System.Platform.numBits](IO/System-and-Platform-Information/#System___Platform___numBits "Documentation for System.Platform.numBits")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.size "Permalink")def
```


UInt8.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


UInt8.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of distinct values representable by `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")`, that is, `2^8 = 256`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.size "Permalink")def
```


Int8.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Int8.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of distinct values representable by `[Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")`, that is, `2^8 = 256`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.size "Permalink")def
```


UInt16.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


UInt16.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of distinct values representable by `[UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")`, that is, `2^16 = 65536`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.size "Permalink")def
```


Int16.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Int16.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of distinct values representable by `[Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")`, that is, `2^16 = 65536`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.size "Permalink")def
```


UInt32.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


UInt32.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of distinct values representable by `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")`, that is, `2^32 = 4294967296`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.size "Permalink")def
```


Int32.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Int32.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of distinct values representable by `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")`, that is, `2^32 = 4294967296`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.size "Permalink")def
```


UInt64.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


UInt64.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of distinct values representable by `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`, that is, `2^64 = 18446744073709551616`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.size "Permalink")def
```


Int64.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Int64.size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of distinct values representable by `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")`, that is, `2^64 = 18446744073709551616`.
###  20.4.4.2. Ranges[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Fixed-Precision-Integers--API-Reference--Ranges "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.minValue "Permalink")def
```


ISize.minValue : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.minValue : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

The smallest number that `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` can represent: `-2^([System.Platform.numBits](IO/System-and-Platform-Information/#System___Platform___numBits "Documentation for System.Platform.numBits") - 1)`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.maxValue "Permalink")def
```


ISize.maxValue : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.maxValue : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

The largest number that `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` can represent: `2^([System.Platform.numBits](IO/System-and-Platform-Information/#System___Platform___numBits "Documentation for System.Platform.numBits") - 1) - 1`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.minValue "Permalink")def
```


Int8.minValue : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.minValue : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

The smallest number that `[Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")` can represent: `-2^7 = -128`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.maxValue "Permalink")def
```


Int8.maxValue : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.maxValue : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

The largest number that `[Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")` can represent: `2^7 - 1 = 127`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.minValue "Permalink")def
```


Int16.minValue : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.minValue : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

The smallest number that `[Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")` can represent: `-2^15 = -32768`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.maxValue "Permalink")def
```


Int16.maxValue : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.maxValue : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

The largest number that `[Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")` can represent: `2^15 - 1 = 32767`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.minValue "Permalink")def
```


Int32.minValue : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.minValue : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

The smallest number that `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` can represent: `-2^31 = -2147483648`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.maxValue "Permalink")def
```


Int32.maxValue : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.maxValue : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

The largest number that `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` can represent: `2^31 - 1 = 2147483647`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.minValue "Permalink")def
```


Int64.minValue : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.minValue : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

The smallest number that `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` can represent: `-2^63 = -9223372036854775808`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.maxValue "Permalink")def
```


Int64.maxValue : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.maxValue : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

The largest number that `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` can represent: `2^63 - 1 = 9223372036854775807`.
###  20.4.4.3. Conversions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Fixed-Precision-Integers--API-Reference--Conversions "Permalink")
####  20.4.4.3.1. To and From `Int`[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Fixed-Precision-Integers--API-Reference--Conversions--To-and-From--Int "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.toInt "Permalink")def
```


ISize.toInt (i : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


ISize.toInt (i : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Converts a word-sized signed integer to an arbitrary-precision integer that denotes the same number.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.toInt "Permalink")def
```


Int8.toInt (i : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int8.toInt (i : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Converts an 8-bit signed integer to an arbitrary-precision integer that denotes the same number.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.toInt "Permalink")def
```


Int16.toInt (i : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int16.toInt (i : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Converts a 16-bit signed integer to an arbitrary-precision integer that denotes the same number.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.toInt "Permalink")def
```


Int32.toInt (i : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int32.toInt (i : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Converts a 32-bit signed integer to an arbitrary-precision integer that denotes the same number.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.toInt "Permalink")def
```


Int64.toInt (i : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int64.toInt (i : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Converts a 64-bit signed integer to an arbitrary-precision integer that denotes the same number.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.ofInt "Permalink")def
```


ISize.ofInt (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.ofInt (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Converts an arbitrary-precision integer to a word-sized signed integer, wrapping around on over- or underflow.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.ofInt "Permalink")def
```


Int8.ofInt (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.ofInt (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Converts an arbitrary-precision integer to an 8-bit integer, wrapping on overflow or underflow.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int8.ofInt](Basic-Types/Fixed-Precision-Integers/#Int8___ofInt "Documentation for Int8.ofInt") 48 = 48`
  * `[Int8.ofInt](Basic-Types/Fixed-Precision-Integers/#Int8___ofInt "Documentation for Int8.ofInt") (-115) = -115`
  * `[Int8.ofInt](Basic-Types/Fixed-Precision-Integers/#Int8___ofInt "Documentation for Int8.ofInt") (-129) = 127`
  * `[Int8.ofInt](Basic-Types/Fixed-Precision-Integers/#Int8___ofInt "Documentation for Int8.ofInt") (128) = -128`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.ofInt "Permalink")def
```


Int16.ofInt (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.ofInt (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Converts an arbitrary-precision integer to a 16-bit signed integer, wrapping on overflow or underflow.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int16.ofInt](Basic-Types/Fixed-Precision-Integers/#Int16___ofInt "Documentation for Int16.ofInt") 48 = 48`
  * `[Int16.ofInt](Basic-Types/Fixed-Precision-Integers/#Int16___ofInt "Documentation for Int16.ofInt") (-129) = -129`
  * `[Int16.ofInt](Basic-Types/Fixed-Precision-Integers/#Int16___ofInt "Documentation for Int16.ofInt") (128) = 128`
  * `[Int16.ofInt](Basic-Types/Fixed-Precision-Integers/#Int16___ofInt "Documentation for Int16.ofInt") 70000 = 4464`
  * `[Int16.ofInt](Basic-Types/Fixed-Precision-Integers/#Int16___ofInt "Documentation for Int16.ofInt") (-40000) = 25536`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.ofInt "Permalink")def
```


Int32.ofInt (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.ofInt (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Converts an arbitrary-precision integer to a 32-bit integer, wrapping on overflow or underflow.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int32.ofInt](Basic-Types/Fixed-Precision-Integers/#Int32___ofInt "Documentation for Int32.ofInt") 48 = 48`
  * `[Int32.ofInt](Basic-Types/Fixed-Precision-Integers/#Int32___ofInt "Documentation for Int32.ofInt") (-129) = -129`
  * `[Int32.ofInt](Basic-Types/Fixed-Precision-Integers/#Int32___ofInt "Documentation for Int32.ofInt") 70000 = 70000`
  * `[Int32.ofInt](Basic-Types/Fixed-Precision-Integers/#Int32___ofInt "Documentation for Int32.ofInt") (-40000) = -40000`
  * `[Int32.ofInt](Basic-Types/Fixed-Precision-Integers/#Int32___ofInt "Documentation for Int32.ofInt") 2147483648 = -2147483648`
  * `[Int32.ofInt](Basic-Types/Fixed-Precision-Integers/#Int32___ofInt "Documentation for Int32.ofInt") (-2147483649) = 2147483647`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.ofInt "Permalink")def
```


Int64.ofInt (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.ofInt (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Converts an arbitrary-precision integer to a 64-bit integer, wrapping on overflow or underflow.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int64.ofInt](Basic-Types/Fixed-Precision-Integers/#Int64___ofInt "Documentation for Int64.ofInt") 48 = 48`
  * `[Int64.ofInt](Basic-Types/Fixed-Precision-Integers/#Int64___ofInt "Documentation for Int64.ofInt") (-40_000) = -40_000`
  * `[Int64.ofInt](Basic-Types/Fixed-Precision-Integers/#Int64___ofInt "Documentation for Int64.ofInt") 2_147_483_648 = 2_147_483_648`
  * `[Int64.ofInt](Basic-Types/Fixed-Precision-Integers/#Int64___ofInt "Documentation for Int64.ofInt") (-2_147_483_649) = -2_147_483_649`
  * `[Int64.ofInt](Basic-Types/Fixed-Precision-Integers/#Int64___ofInt "Documentation for Int64.ofInt") 9_223_372_036_854_775_808 = -9_223_372_036_854_775_808`
  * `[Int64.ofInt](Basic-Types/Fixed-Precision-Integers/#Int64___ofInt "Documentation for Int64.ofInt") (-9_223_372_036_854_775_809) = 9_223_372_036_854_775_807`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.ofIntTruncate "Permalink")def
```


ISize.ofIntTruncate (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.ofIntTruncate (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Constructs an `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` from an `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`, clamping if the value is too small or too large.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.ofIntTruncate "Permalink")def
```


Int8.ofIntTruncate (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.ofIntTruncate (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Constructs an `[Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")` from an `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`, clamping if the value is too small or too large.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.ofIntTruncate "Permalink")def
```


Int16.ofIntTruncate (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.ofIntTruncate (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Constructs an `[Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")` from an `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`, clamping if the value is too small or too large.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.ofIntTruncate "Permalink")def
```


Int32.ofIntTruncate (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.ofIntTruncate (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Constructs an `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` from an `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`, clamping if the value is too small or too large.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.ofIntTruncate "Permalink")def
```


Int64.ofIntTruncate (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.ofIntTruncate (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Constructs an `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` from an `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`, clamping if the value is too small or too large.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.ofIntLE "Permalink")def
```


ISize.ofIntLE (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) (_hl : [ISize.minValue](Basic-Types/Fixed-Precision-Integers/#ISize___minValue "Documentation for ISize.minValue").[toInt](Basic-Types/Fixed-Precision-Integers/#ISize___toInt "Documentation for ISize.toInt") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") i)
  (_hr : i [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") [ISize.maxValue](Basic-Types/Fixed-Precision-Integers/#ISize___maxValue "Documentation for ISize.maxValue").[toInt](Basic-Types/Fixed-Precision-Integers/#ISize___toInt "Documentation for ISize.toInt")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.ofIntLE (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int"))
  (_hl : [ISize.minValue](Basic-Types/Fixed-Precision-Integers/#ISize___minValue "Documentation for ISize.minValue").[toInt](Basic-Types/Fixed-Precision-Integers/#ISize___toInt "Documentation for ISize.toInt") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") i)
  (_hr : i [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") [ISize.maxValue](Basic-Types/Fixed-Precision-Integers/#ISize___maxValue "Documentation for ISize.maxValue").[toInt](Basic-Types/Fixed-Precision-Integers/#ISize___toInt "Documentation for ISize.toInt")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Constructs an `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` from an `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` that is known to be in bounds.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.ofIntLE "Permalink")def
```


Int8.ofIntLE (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) (_hl : [Int8.minValue](Basic-Types/Fixed-Precision-Integers/#Int8___minValue "Documentation for Int8.minValue").[toInt](Basic-Types/Fixed-Precision-Integers/#Int8___toInt "Documentation for Int8.toInt") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") i)
  (_hr : i [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") [Int8.maxValue](Basic-Types/Fixed-Precision-Integers/#Int8___maxValue "Documentation for Int8.maxValue").[toInt](Basic-Types/Fixed-Precision-Integers/#Int8___toInt "Documentation for Int8.toInt")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.ofIntLE (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int"))
  (_hl : [Int8.minValue](Basic-Types/Fixed-Precision-Integers/#Int8___minValue "Documentation for Int8.minValue").[toInt](Basic-Types/Fixed-Precision-Integers/#Int8___toInt "Documentation for Int8.toInt") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") i)
  (_hr : i [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") [Int8.maxValue](Basic-Types/Fixed-Precision-Integers/#Int8___maxValue "Documentation for Int8.maxValue").[toInt](Basic-Types/Fixed-Precision-Integers/#Int8___toInt "Documentation for Int8.toInt")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Constructs an `[Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")` from an `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` that is known to be in bounds.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.ofIntLE "Permalink")def
```


Int16.ofIntLE (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) (_hl : [Int16.minValue](Basic-Types/Fixed-Precision-Integers/#Int16___minValue "Documentation for Int16.minValue").[toInt](Basic-Types/Fixed-Precision-Integers/#Int16___toInt "Documentation for Int16.toInt") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") i)
  (_hr : i [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") [Int16.maxValue](Basic-Types/Fixed-Precision-Integers/#Int16___maxValue "Documentation for Int16.maxValue").[toInt](Basic-Types/Fixed-Precision-Integers/#Int16___toInt "Documentation for Int16.toInt")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.ofIntLE (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int"))
  (_hl : [Int16.minValue](Basic-Types/Fixed-Precision-Integers/#Int16___minValue "Documentation for Int16.minValue").[toInt](Basic-Types/Fixed-Precision-Integers/#Int16___toInt "Documentation for Int16.toInt") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") i)
  (_hr : i [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") [Int16.maxValue](Basic-Types/Fixed-Precision-Integers/#Int16___maxValue "Documentation for Int16.maxValue").[toInt](Basic-Types/Fixed-Precision-Integers/#Int16___toInt "Documentation for Int16.toInt")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Constructs an `[Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")` from an `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` that is known to be in bounds.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.ofIntLE "Permalink")def
```


Int32.ofIntLE (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) (_hl : [Int32.minValue](Basic-Types/Fixed-Precision-Integers/#Int32___minValue "Documentation for Int32.minValue").[toInt](Basic-Types/Fixed-Precision-Integers/#Int32___toInt "Documentation for Int32.toInt") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") i)
  (_hr : i [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") [Int32.maxValue](Basic-Types/Fixed-Precision-Integers/#Int32___maxValue "Documentation for Int32.maxValue").[toInt](Basic-Types/Fixed-Precision-Integers/#Int32___toInt "Documentation for Int32.toInt")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.ofIntLE (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int"))
  (_hl : [Int32.minValue](Basic-Types/Fixed-Precision-Integers/#Int32___minValue "Documentation for Int32.minValue").[toInt](Basic-Types/Fixed-Precision-Integers/#Int32___toInt "Documentation for Int32.toInt") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") i)
  (_hr : i [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") [Int32.maxValue](Basic-Types/Fixed-Precision-Integers/#Int32___maxValue "Documentation for Int32.maxValue").[toInt](Basic-Types/Fixed-Precision-Integers/#Int32___toInt "Documentation for Int32.toInt")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Constructs an `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` from an `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` that is known to be in bounds.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.ofIntLE "Permalink")def
```


Int64.ofIntLE (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) (_hl : [Int64.minValue](Basic-Types/Fixed-Precision-Integers/#Int64___minValue "Documentation for Int64.minValue").[toInt](Basic-Types/Fixed-Precision-Integers/#Int64___toInt "Documentation for Int64.toInt") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") i)
  (_hr : i [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") [Int64.maxValue](Basic-Types/Fixed-Precision-Integers/#Int64___maxValue "Documentation for Int64.maxValue").[toInt](Basic-Types/Fixed-Precision-Integers/#Int64___toInt "Documentation for Int64.toInt")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.ofIntLE (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int"))
  (_hl : [Int64.minValue](Basic-Types/Fixed-Precision-Integers/#Int64___minValue "Documentation for Int64.minValue").[toInt](Basic-Types/Fixed-Precision-Integers/#Int64___toInt "Documentation for Int64.toInt") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") i)
  (_hr : i [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") [Int64.maxValue](Basic-Types/Fixed-Precision-Integers/#Int64___maxValue "Documentation for Int64.maxValue").[toInt](Basic-Types/Fixed-Precision-Integers/#Int64___toInt "Documentation for Int64.toInt")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Constructs an `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` from an `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` that is known to be in bounds.
####  20.4.4.3.2. To and From `Nat`[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Fixed-Precision-Integers--API-Reference--Conversions--To-and-From--Nat "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.ofNat "Permalink")def
```


USize.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


USize.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Converts an arbitrary-precision natural number to an unsigned word-sized integer, wrapping around on overflow.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.ofNat "Permalink")def
```


ISize.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Converts an arbitrary-precision natural number to a word-sized signed integer, wrapping around on overflow.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.ofNat "Permalink")def
```


UInt8.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt8.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Converts a natural number to an 8-bit unsigned integer, wrapping on overflow.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[UInt8.ofNat](Basic-Types/Fixed-Precision-Integers/#UInt8___ofNat "Documentation for UInt8.ofNat") 5 = 5`
  * `[UInt8.ofNat](Basic-Types/Fixed-Precision-Integers/#UInt8___ofNat "Documentation for UInt8.ofNat") 255 = 255`
  * `[UInt8.ofNat](Basic-Types/Fixed-Precision-Integers/#UInt8___ofNat "Documentation for UInt8.ofNat") 256 = 0`
  * `[UInt8.ofNat](Basic-Types/Fixed-Precision-Integers/#UInt8___ofNat "Documentation for UInt8.ofNat") 259 = 3`
  * `[UInt8.ofNat](Basic-Types/Fixed-Precision-Integers/#UInt8___ofNat "Documentation for UInt8.ofNat") 32770 = 2`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.ofNat "Permalink")def
```


Int8.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Converts a natural number to an 8-bit signed integer, wrapping around on overflow.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int8.ofNat](Basic-Types/Fixed-Precision-Integers/#Int8___ofNat "Documentation for Int8.ofNat") 53 = 53`
  * `[Int8.ofNat](Basic-Types/Fixed-Precision-Integers/#Int8___ofNat "Documentation for Int8.ofNat") 127 = 127`
  * `[Int8.ofNat](Basic-Types/Fixed-Precision-Integers/#Int8___ofNat "Documentation for Int8.ofNat") 128 = -128`
  * `[Int8.ofNat](Basic-Types/Fixed-Precision-Integers/#Int8___ofNat "Documentation for Int8.ofNat") 255 = -1`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.ofNat "Permalink")def
```


UInt16.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt16.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Converts a natural number to a 16-bit unsigned integer, wrapping on overflow.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[UInt16.ofNat](Basic-Types/Fixed-Precision-Integers/#UInt16___ofNat "Documentation for UInt16.ofNat") 5 = 5`
  * `[UInt16.ofNat](Basic-Types/Fixed-Precision-Integers/#UInt16___ofNat "Documentation for UInt16.ofNat") 255 = 255`
  * `[UInt16.ofNat](Basic-Types/Fixed-Precision-Integers/#UInt16___ofNat "Documentation for UInt16.ofNat") 32770 = 32770`
  * `[UInt16.ofNat](Basic-Types/Fixed-Precision-Integers/#UInt16___ofNat "Documentation for UInt16.ofNat") 65537 = 1`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.ofNat "Permalink")def
```


Int16.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Converts a natural number to a 16-bit signed integer, wrapping around on overflow.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int16.ofNat](Basic-Types/Fixed-Precision-Integers/#Int16___ofNat "Documentation for Int16.ofNat") 127 = 127`
  * `[Int16.ofNat](Basic-Types/Fixed-Precision-Integers/#Int16___ofNat "Documentation for Int16.ofNat") 32767 = 32767`
  * `[Int16.ofNat](Basic-Types/Fixed-Precision-Integers/#Int16___ofNat "Documentation for Int16.ofNat") 32768 = -32768`
  * `[Int16.ofNat](Basic-Types/Fixed-Precision-Integers/#Int16___ofNat "Documentation for Int16.ofNat") 32770 = -32766`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.ofNat "Permalink")def
```


UInt32.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt32.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Converts a natural number to a 32-bit unsigned integer, wrapping on overflow.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[UInt32.ofNat](Basic-Types/Fixed-Precision-Integers/#UInt32___ofNat "Documentation for UInt32.ofNat") 5 = 5`
  * `[UInt32.ofNat](Basic-Types/Fixed-Precision-Integers/#UInt32___ofNat "Documentation for UInt32.ofNat") 65539 = 65539`
  * `[UInt32.ofNat](Basic-Types/Fixed-Precision-Integers/#UInt32___ofNat "Documentation for UInt32.ofNat") 4_294_967_299 = 3`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.ofNat "Permalink")def
```


Int32.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Converts a natural number to a 32-bit signed integer, wrapping around on overflow.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int32.ofNat](Basic-Types/Fixed-Precision-Integers/#Int32___ofNat "Documentation for Int32.ofNat") 127 = 127`
  * `[Int32.ofNat](Basic-Types/Fixed-Precision-Integers/#Int32___ofNat "Documentation for Int32.ofNat") 32770 = 32770`
  * `[Int32.ofNat](Basic-Types/Fixed-Precision-Integers/#Int32___ofNat "Documentation for Int32.ofNat") 2_147_483_647 = 2_147_483_647`
  * `[Int32.ofNat](Basic-Types/Fixed-Precision-Integers/#Int32___ofNat "Documentation for Int32.ofNat") 2_147_483_648 = -2_147_483_648`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.ofNat "Permalink")def
```


UInt64.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt64.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Converts a natural number to a 64-bit unsigned integer, wrapping on overflow.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[UInt64.ofNat](Basic-Types/Fixed-Precision-Integers/#UInt64___ofNat "Documentation for UInt64.ofNat") 5 = 5`
  * `[UInt64.ofNat](Basic-Types/Fixed-Precision-Integers/#UInt64___ofNat "Documentation for UInt64.ofNat") 65539 = 65539`
  * `[UInt64.ofNat](Basic-Types/Fixed-Precision-Integers/#UInt64___ofNat "Documentation for UInt64.ofNat") 4_294_967_299 = 4_294_967_299`
  * `[UInt64.ofNat](Basic-Types/Fixed-Precision-Integers/#UInt64___ofNat "Documentation for UInt64.ofNat") 18_446_744_073_709_551_620 = 4`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.ofNat "Permalink")def
```


Int64.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Converts a natural number to a 64-bit signed integer, wrapping around to negative numbers on overflow.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int64.ofNat](Basic-Types/Fixed-Precision-Integers/#Int64___ofNat "Documentation for Int64.ofNat") 127 = 127`
  * `[Int64.ofNat](Basic-Types/Fixed-Precision-Integers/#Int64___ofNat "Documentation for Int64.ofNat") 2_147_483_648 = 2_147_483_648`
  * `[Int64.ofNat](Basic-Types/Fixed-Precision-Integers/#Int64___ofNat "Documentation for Int64.ofNat") 9_223_372_036_854_775_807 = 9_223_372_036_854_775_807`
  * `[Int64.ofNat](Basic-Types/Fixed-Precision-Integers/#Int64___ofNat "Documentation for Int64.ofNat") 9_223_372_036_854_775_808 = -9_223_372_036_854_775_808`
  * `[Int64.ofNat](Basic-Types/Fixed-Precision-Integers/#Int64___ofNat "Documentation for Int64.ofNat") 18_446_744_073_709_551_618 = 0`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.ofNat32 "Permalink")def
```


USize.ofNat32 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (h : n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 4294967296) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


USize.ofNat32 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (h : n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 4294967296) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Converts a natural number to a `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")`. Overflow is impossible on any supported platform because `[USize.size](Basic-Types/Fixed-Precision-Integers/#USize___size "Documentation for USize.size")` is either `2^32` or `2^64`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.ofNatLT "Permalink")def
```


USize.ofNatLT (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (h : n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") [USize.size](Basic-Types/Fixed-Precision-Integers/#USize___size "Documentation for USize.size")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


USize.ofNatLT (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (h : n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") [USize.size](Basic-Types/Fixed-Precision-Integers/#USize___size "Documentation for USize.size")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Converts a natural number to a `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")`. Requires a proof that the number is small enough to be representable without overflow.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.ofNatLT "Permalink")def
```


UInt8.ofNatLT (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (h : n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") [UInt8.size](Basic-Types/Fixed-Precision-Integers/#UInt8___size "Documentation for UInt8.size")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt8.ofNatLT (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (h : n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") [UInt8.size](Basic-Types/Fixed-Precision-Integers/#UInt8___size "Documentation for UInt8.size")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Converts a natural number to an 8-bit unsigned integer. Requires a proof that the number is small enough to be representable without overflow; it must be smaller than `2^8`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.ofNatLT "Permalink")def
```


UInt16.ofNatLT (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (h : n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") [UInt16.size](Basic-Types/Fixed-Precision-Integers/#UInt16___size "Documentation for UInt16.size")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt16.ofNatLT (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (h : n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") [UInt16.size](Basic-Types/Fixed-Precision-Integers/#UInt16___size "Documentation for UInt16.size")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Converts a natural number to a 16-bit unsigned integer. Requires a proof that the number is small enough to be representable without overflow; it must be smaller than `2^16`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.ofNatLT "Permalink")def
```


UInt32.ofNatLT (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (h : n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") [UInt32.size](Basic-Types/Fixed-Precision-Integers/#UInt32___size "Documentation for UInt32.size")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt32.ofNatLT (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (h : n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") [UInt32.size](Basic-Types/Fixed-Precision-Integers/#UInt32___size "Documentation for UInt32.size")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Converts a natural number to a 32-bit unsigned integer. Requires a proof that the number is small enough to be representable without overflow; it must be smaller than `2^32`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.ofNatLT "Permalink")def
```


UInt64.ofNatLT (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (h : n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") [UInt64.size](Basic-Types/Fixed-Precision-Integers/#UInt64___size "Documentation for UInt64.size")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt64.ofNatLT (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (h : n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") [UInt64.size](Basic-Types/Fixed-Precision-Integers/#UInt64___size "Documentation for UInt64.size")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Converts a natural number to a 64-bit unsigned integer. Requires a proof that the number is small enough to be representable without overflow; it must be smaller than `2^64`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.ofNatTruncate "Permalink")def
```


USize.ofNatTruncate (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


USize.ofNatTruncate (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Converts a natural number to `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")`, returning the largest representable value if the number is too large.
Returns `[USize.size](Basic-Types/Fixed-Precision-Integers/#USize___size "Documentation for USize.size") - 1`, which is `2^64 - 1` or `2^32 - 1` depending on the platform, for natural numbers greater than or equal to `[USize.size](Basic-Types/Fixed-Precision-Integers/#USize___size "Documentation for USize.size")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.ofNatTruncate "Permalink")def
```


UInt8.ofNatTruncate (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt8.ofNatTruncate (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Converts a natural number to an 8-bit unsigned integer, returning the largest representable value if the number is too large.
Returns `2^8 - 1` for natural numbers greater than or equal to `2^8`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.ofNatTruncate "Permalink")def
```


UInt16.ofNatTruncate (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt16.ofNatTruncate (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Converts a natural number to a 16-bit unsigned integer, returning the largest representable value if the number is too large.
Returns `2^16 - 1` for natural numbers greater than or equal to `2^16`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.ofNatTruncate "Permalink")def
```


UInt32.ofNatTruncate (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt32.ofNatTruncate (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Converts a natural number to a 32-bit unsigned integer, returning the largest representable value if the number is too large.
Returns `2^32 - 1` for natural numbers greater than or equal to `2^32`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.ofNatTruncate "Permalink")def
```


UInt64.ofNatTruncate (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt64.ofNatTruncate (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Converts a natural number to a 64-bit unsigned integer, returning the largest representable value if the number is too large.
Returns `2^64 - 1` for natural numbers greater than or equal to `2^64`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.toNat "Permalink")def
```


USize.toNat (n : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


USize.toNat (n : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Converts a word-sized unsigned integer to an arbitrary-precision natural number.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=ISize.toNat%E2%86%AAISize.toNatClampNeg "Permalink")def
```


ISize.toNatClampNeg (i : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


ISize.toNatClampNeg (i : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Converts a word-sized signed integer to a natural number, mapping all negative numbers to `0`.
Use `[ISize.toBitVec](Basic-Types/Fixed-Precision-Integers/#ISize___toBitVec "Documentation for ISize.toBitVec")` to obtain the two's complement representation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.toNat "Permalink")def
```


UInt8.toNat (n : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


UInt8.toNat (n : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Converts an 8-bit unsigned integer to an arbitrary-precision natural number.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=Int8.toNat%E2%86%AAInt8.toNatClampNeg "Permalink")def
```


Int8.toNatClampNeg (i : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Int8.toNatClampNeg (i : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Converts an 8-bit signed integer to a natural number, mapping all negative numbers to `0`.
Use `[Int8.toBitVec](Basic-Types/Fixed-Precision-Integers/#Int8___toBitVec "Documentation for Int8.toBitVec")` to obtain the two's complement representation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.toNat "Permalink")def
```


UInt16.toNat (n : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


UInt16.toNat (n : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Converts a 16-bit unsigned integer to an arbitrary-precision natural number.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=Int16.toNat%E2%86%AAInt16.toNatClampNeg "Permalink")def
```


Int16.toNatClampNeg (i : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Int16.toNatClampNeg (i : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Converts a 16-bit signed integer to a natural number, mapping all negative numbers to `0`.
Use `[Int16.toBitVec](Basic-Types/Fixed-Precision-Integers/#Int16___toBitVec "Documentation for Int16.toBitVec")` to obtain the two's complement representation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.toNat "Permalink")def
```


UInt32.toNat (n : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


UInt32.toNat (n : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Converts a 32-bit unsigned integer to an arbitrary-precision natural number.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=Int32.toNat%E2%86%AAInt32.toNatClampNeg "Permalink")def
```


Int32.toNatClampNeg (i : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Int32.toNatClampNeg (i : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Converts a 32-bit signed integer to a natural number, mapping all negative numbers to `0`.
Use `[Int32.toBitVec](Basic-Types/Fixed-Precision-Integers/#Int32___toBitVec "Documentation for Int32.toBitVec")` to obtain the two's complement representation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.toNat "Permalink")def
```


UInt64.toNat (n : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


UInt64.toNat (n : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Converts a 64-bit unsigned integer to an arbitrary-precision natural number.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=Int64.toNat%E2%86%AAInt64.toNatClampNeg "Permalink")def
```


Int64.toNatClampNeg (i : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Int64.toNatClampNeg (i : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Converts a 64-bit signed integer to a natural number, mapping all negative numbers to `0`.
Use `[Int64.toBitVec](Basic-Types/Fixed-Precision-Integers/#Int64___toBitVec "Documentation for Int64.toBitVec")` to obtain the two's complement representation.
####  20.4.4.3.3. To Other Fixed-Width Integers[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Fixed-Precision-Integers--API-Reference--Conversions--To-Other-Fixed-Width-Integers "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.toUInt8 "Permalink")def
```


USize.toUInt8 (a : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


USize.toUInt8 (a : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Converts word-sized unsigned integers to 8-bit unsigned integers. Wraps around on overflow.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.toUInt16 "Permalink")def
```


USize.toUInt16 (a : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


USize.toUInt16 (a : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Converts word-sized unsigned integers to 16-bit unsigned integers. Wraps around on overflow.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.toUInt32 "Permalink")def
```


USize.toUInt32 (a : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


USize.toUInt32 (a : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Converts word-sized unsigned integers to 32-bit unsigned integers. Wraps around on overflow, which might occur on 64-bit architectures.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.toUInt64 "Permalink")def
```


USize.toUInt64 (a : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


USize.toUInt64 (a : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Converts word-sized unsigned integers to 32-bit unsigned integers. This cannot overflow because `[USize.size](Basic-Types/Fixed-Precision-Integers/#USize___size "Documentation for USize.size")` is either `2^32` or `2^64`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.toISize "Permalink")def
```


USize.toISize (i : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


USize.toISize (i : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Obtains the `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` that is 2's complement equivalent to the `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.toInt8 "Permalink")def
```


UInt8.toInt8 (i : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


UInt8.toInt8 (i : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Obtains the `[Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")` that is 2's complement equivalent to the `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.toUInt16 "Permalink")def
```


UInt8.toUInt16 (a : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt8.toUInt16 (a : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Converts 8-bit unsigned integers to 16-bit unsigned integers.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.toUInt32 "Permalink")def
```


UInt8.toUInt32 (a : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt8.toUInt32 (a : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Converts 8-bit unsigned integers to 32-bit unsigned integers.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.toUInt64 "Permalink")def
```


UInt8.toUInt64 (a : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt8.toUInt64 (a : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Converts 8-bit unsigned integers to 64-bit unsigned integers.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.toUSize "Permalink")def
```


UInt8.toUSize (a : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


UInt8.toUSize (a : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Converts 8-bit unsigned integers to word-sized unsigned integers.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.toUInt8 "Permalink")def
```


UInt16.toUInt8 (a : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt16.toUInt8 (a : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Converts 16-bit unsigned integers to 8-bit unsigned integers. Wraps around on overflow.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.toInt16 "Permalink")def
```


UInt16.toInt16 (i : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


UInt16.toInt16 (i : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Obtains the `[Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")` that is 2's complement equivalent to the `[UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.toUInt32 "Permalink")def
```


UInt16.toUInt32 (a : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt16.toUInt32 (a : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Converts 16-bit unsigned integers to 32-bit unsigned integers.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.toUInt64 "Permalink")def
```


UInt16.toUInt64 (a : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt16.toUInt64 (a : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Converts 16-bit unsigned integers to 64-bit unsigned integers. Wraps around on overflow.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.toUSize "Permalink")def
```


UInt16.toUSize (a : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


UInt16.toUSize (a : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Converts 16-bit unsigned integers to word-sized unsigned integers.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.toUInt8 "Permalink")def
```


UInt32.toUInt8 (a : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt32.toUInt8 (a : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Converts a 32-bit unsigned integer to an 8-bit unsigned integer, wrapping on overflow.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.toUInt16 "Permalink")def
```


UInt32.toUInt16 (a : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt32.toUInt16 (a : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Converts 32-bit unsigned integers to 16-bit unsigned integers. Wraps around on overflow.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.toInt32 "Permalink")def
```


UInt32.toInt32 (i : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


UInt32.toInt32 (i : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Obtains the `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` that is 2's complement equivalent to the `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.toUInt64 "Permalink")def
```


UInt32.toUInt64 (a : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt32.toUInt64 (a : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Converts 32-bit unsigned integers to 64-bit unsigned integers. Wraps around on overflow.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.toUSize "Permalink")def
```


UInt32.toUSize (a : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


UInt32.toUSize (a : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Converts 32-bit unsigned integers to word-sized unsigned integers.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.toUInt8 "Permalink")def
```


UInt64.toUInt8 (a : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt64.toUInt8 (a : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Converts 64-bit unsigned integers to 8-bit unsigned integers. Wraps around on overflow.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.toUInt16 "Permalink")def
```


UInt64.toUInt16 (a : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt64.toUInt16 (a : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Converts 64-bit unsigned integers to 16-bit unsigned integers. Wraps around on overflow.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.toUInt32 "Permalink")def
```


UInt64.toUInt32 (a : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt64.toUInt32 (a : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Converts 64-bit unsigned integers to 32-bit unsigned integers. Wraps around on overflow.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.toInt64 "Permalink")def
```


UInt64.toInt64 (i : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


UInt64.toInt64 (i : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Obtains the `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` that is 2's complement equivalent to the `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.toUSize "Permalink")def
```


UInt64.toUSize (a : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


UInt64.toUSize (a : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Converts 64-bit unsigned integers to word-sized unsigned integers. On 32-bit machines, this may overflow, which results in the value wrapping around (that is, it is reduced modulo `[USize.size](Basic-Types/Fixed-Precision-Integers/#USize___size "Documentation for USize.size")`).
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.toInt8 "Permalink")def
```


ISize.toInt8 (a : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


ISize.toInt8 (a : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Converts a word-sized signed integer to an 8-bit signed integer by truncating its bitvector representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.toInt16 "Permalink")def
```


ISize.toInt16 (a : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


ISize.toInt16 (a : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Converts a word-sized integer to a 16-bit integer by truncating its bitvector representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.toInt32 "Permalink")def
```


ISize.toInt32 (a : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


ISize.toInt32 (a : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Converts a word-sized signed integer to a 32-bit signed integer.
On 32-bit platforms, this conversion is lossless. On 64-bit platforms, the integer's bitvector representation is truncated to 32 bits. This function is overridden at runtime with an efficient implementation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.toInt64 "Permalink")def
```


ISize.toInt64 (a : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


ISize.toInt64 (a : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Converts word-sized signed integers to 64-bit signed integers that denote the same number. This conversion is lossless, because `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` is either `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` or `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.toInt16 "Permalink")def
```


Int8.toInt16 (a : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int8.toInt16 (a : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Converts 8-bit signed integers to 16-bit signed integers that denote the same number.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.toInt32 "Permalink")def
```


Int8.toInt32 (a : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int8.toInt32 (a : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Converts 8-bit signed integers to 32-bit signed integers that denote the same number.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.toInt64 "Permalink")def
```


Int8.toInt64 (a : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int8.toInt64 (a : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Converts 8-bit signed integers to 64-bit signed integers that denote the same number.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.toISize "Permalink")def
```


Int8.toISize (a : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


Int8.toISize (a : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Converts 8-bit signed integers to word-sized signed integers that denote the same number. This conversion is lossless, because `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` is either `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` or `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.toInt8 "Permalink")def
```


Int16.toInt8 (a : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int16.toInt8 (a : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Converts 16-bit signed integers to 8-bit signed integers by truncating their bitvector representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.toInt32 "Permalink")def
```


Int16.toInt32 (a : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int16.toInt32 (a : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Converts 8-bit signed integers to 32-bit signed integers that denote the same number.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.toInt64 "Permalink")def
```


Int16.toInt64 (a : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int16.toInt64 (a : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Converts 16-bit signed integers to 64-bit signed integers that denote the same number.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.toISize "Permalink")def
```


Int16.toISize (a : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


Int16.toISize (a : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Converts 16-bit signed integers to word-sized signed integers that denote the same number. This conversion is lossless, because `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` is either `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` or `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.toInt8 "Permalink")def
```


Int32.toInt8 (a : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int32.toInt8 (a : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Converts a 32-bit signed integer to an 8-bit signed integer by truncating its bitvector representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.toInt16 "Permalink")def
```


Int32.toInt16 (a : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int32.toInt16 (a : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Converts a 32-bit signed integer to an 16-bit signed integer by truncating its bitvector representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.toInt64 "Permalink")def
```


Int32.toInt64 (a : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int32.toInt64 (a : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Converts 32-bit signed integers to 64-bit signed integers that denote the same number.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.toISize "Permalink")def
```


Int32.toISize (a : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


Int32.toISize (a : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Converts 32-bit signed integers to word-sized signed integers that denote the same number. This conversion is lossless, because `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` is either `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` or `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.toInt8 "Permalink")def
```


Int64.toInt8 (a : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int64.toInt8 (a : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Converts a 64-bit signed integer to an 8-bit signed integer by truncating its bitvector representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.toInt16 "Permalink")def
```


Int64.toInt16 (a : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int64.toInt16 (a : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Converts a 64-bit signed integer to a 16-bit signed integer by truncating its bitvector representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.toInt32 "Permalink")def
```


Int64.toInt32 (a : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int64.toInt32 (a : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Converts a 64-bit signed integer to a 32-bit signed integer by truncating its bitvector representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.toISize "Permalink")def
```


Int64.toISize (a : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


Int64.toISize (a : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Converts 64-bit signed integers to word-sized signed integers, truncating the bitvector representation on 32-bit platforms. This conversion is lossless on 64-bit platforms.
This function is overridden at runtime with an efficient implementation.
####  20.4.4.3.4. To Floating-Point Numbers[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Fixed-Precision-Integers--API-Reference--Conversions--To-Floating-Point-Numbers "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.toFloat "Permalink")opaque
```


ISize.toFloat (n : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


ISize.toFloat (n : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Obtains a `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` whose value is near the given `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")`.
It will be exactly the value of the given `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` if such a `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` exists. If no such `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` exists, the returned value will either be the smallest `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` that is larger than the given value, or the largest `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` that is smaller than the given value.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.toFloat32 "Permalink")opaque
```


ISize.toFloat32 (n : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


ISize.toFloat32 (n : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Obtains a `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` whose value is near the given `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")`.
It will be exactly the value of the given `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` if such a `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` exists. If no such `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` exists, the returned value will either be the smallest `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` that is larger than the given value, or the largest `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` that is smaller than the given value.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.toFloat "Permalink")opaque
```


Int8.toFloat (n : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Int8.toFloat (n : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Obtains the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` whose value is the same as the given `[Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")`.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.toFloat32 "Permalink")opaque
```


Int8.toFloat32 (n : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Int8.toFloat32 (n : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Obtains the `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` whose value is the same as the given `[Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")`.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.toFloat "Permalink")opaque
```


Int16.toFloat (n : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Int16.toFloat (n : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Obtains the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` whose value is the same as the given `[Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")`.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.toFloat32 "Permalink")opaque
```


Int16.toFloat32 (n : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Int16.toFloat32 (n : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Obtains the `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` whose value is the same as the given `[Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")`.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.toFloat "Permalink")opaque
```


Int32.toFloat (n : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Int32.toFloat (n : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Obtains the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` whose value is the same as the given `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")`.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.toFloat32 "Permalink")opaque
```


Int32.toFloat32 (n : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Int32.toFloat32 (n : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Obtains a `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` whose value is near the given `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")`.
It will be exactly the value of the given `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` if such a `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` exists. If no such `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` exists, the returned value will either be the smallest `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` that is larger than the given value, or the largest `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` that is smaller than the given value.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.toFloat "Permalink")opaque
```


Int64.toFloat (n : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Int64.toFloat (n : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Obtains a `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` whose value is near the given `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")`.
It will be exactly the value of the given `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` if such a `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` exists. If no such `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` exists, the returned value will either be the smallest `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` that is larger than the given value, or the largest `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` that is smaller than the given value.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.toFloat32 "Permalink")opaque
```


Int64.toFloat32 (n : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Int64.toFloat32 (n : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Obtains a `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` whose value is near the given `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")`.
It will be exactly the value of the given `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` if such a `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` exists. If no such `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` exists, the returned value will either be the smallest `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` that is larger than the given value, or the largest `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` that is smaller than the given value.
This function does not reduce in the kernel.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.toFloat "Permalink")opaque
```


USize.toFloat (n : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


USize.toFloat (n : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Obtains a `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` whose value is near the given `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")`.
It will be exactly the value of the given `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")` if such a `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` exists. If no such `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` exists, the returned value will either be the smallest `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` that is larger than the given value, or the largest `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` that is smaller than the given value.
This function is opaque in the kernel, but is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.toFloat32 "Permalink")opaque
```


USize.toFloat32 (n : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


USize.toFloat32 (n : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Obtains a `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` whose value is near the given `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")`.
It will be exactly the value of the given `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")` if such a `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` exists. If no such `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` exists, the returned value will either be the smallest `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` that is larger than the given value, or the largest `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` that is smaller than the given value.
This function is opaque in the kernel, but is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.toFloat "Permalink")opaque
```


UInt8.toFloat (n : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


UInt8.toFloat (n : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Obtains the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` whose value is the same as the given `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.toFloat32 "Permalink")opaque
```


UInt8.toFloat32 (n : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


UInt8.toFloat32 (n : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Obtains the `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` whose value is the same as the given `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.toFloat "Permalink")opaque
```


UInt16.toFloat (n : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


UInt16.toFloat (n : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Obtains the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` whose value is the same as the given `[UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.toFloat32 "Permalink")opaque
```


UInt16.toFloat32 (n : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


UInt16.toFloat32 (n : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Obtains the `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` whose value is the same as the given `[UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.toFloat "Permalink")opaque
```


UInt32.toFloat (n : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


UInt32.toFloat (n : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Obtains the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` whose value is the same as the given `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.toFloat32 "Permalink")opaque
```


UInt32.toFloat32 (n : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


UInt32.toFloat32 (n : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Obtains a `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` whose value is near the given `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")`.
It will be exactly the value of the given `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")` if such a `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` exists. If no such `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` exists, the returned value will either be the smallest `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` that is larger than the given value, or the largest `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` that is smaller than the given value.
This function is opaque in the kernel, but is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.toFloat "Permalink")opaque
```


UInt64.toFloat (n : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


UInt64.toFloat (n : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Obtains a `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` whose value is near the given `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`.
It will be exactly the value of the given `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")` if such a `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` exists. If no such `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` exists, the returned value will either be the smallest `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` that is larger than the given value, or the largest `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` that is smaller than the given value.
This function is opaque in the kernel, but is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.toFloat32 "Permalink")opaque
```


UInt64.toFloat32 (n : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


UInt64.toFloat32 (n : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Obtains a `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` whose value is near the given `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`.
It will be exactly the value of the given `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")` if such a `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` exists. If no such `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` exists, the returned value will either be the smallest `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` that is larger than the given value, or the largest `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` that is smaller than the given value.
This function is opaque in the kernel, but is overridden at runtime with an efficient implementation.
####  20.4.4.3.5. To and From Bitvectors[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Fixed-Precision-Integers--API-Reference--Conversions--To-and-From-Bitvectors "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.toBitVec "Permalink")def
```


ISize.toBitVec (x : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [System.Platform.numBits](IO/System-and-Platform-Information/#System___Platform___numBits "Documentation for System.Platform.numBits")


ISize.toBitVec (x : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) :
  [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [System.Platform.numBits](IO/System-and-Platform-Information/#System___Platform___numBits "Documentation for System.Platform.numBits")


```

Obtain the `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec")` that contains the 2's complement representation of the `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.ofBitVec "Permalink")def
```


ISize.ofBitVec (b : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [System.Platform.numBits](IO/System-and-Platform-Information/#System___Platform___numBits "Documentation for System.Platform.numBits")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.ofBitVec
  (b : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [System.Platform.numBits](IO/System-and-Platform-Information/#System___Platform___numBits "Documentation for System.Platform.numBits")) :
  [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Obtains the `[ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` whose 2's complement representation is the given `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.toBitVec "Permalink")def
```


Int8.toBitVec (x : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 8


Int8.toBitVec (x : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 8


```

Obtain the `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec")` that contains the 2's complement representation of the `[Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.ofBitVec "Permalink")def
```


Int8.ofBitVec (b : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 8) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.ofBitVec (b : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 8) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Obtains the `[Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")` whose 2's complement representation is the given `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 8`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.toBitVec "Permalink")def
```


Int16.toBitVec (x : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 16


Int16.toBitVec (x : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 16


```

Obtain the `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec")` that contains the 2's complement representation of the `[Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.ofBitVec "Permalink")def
```


Int16.ofBitVec (b : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 16) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.ofBitVec (b : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 16) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Obtains the `[Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")` whose 2's complement representation is the given `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 16`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.toBitVec "Permalink")def
```


Int32.toBitVec (x : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32


Int32.toBitVec (x : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32


```

Obtain the `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec")` that contains the 2's complement representation of the `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.ofBitVec "Permalink")def
```


Int32.ofBitVec (b : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.ofBitVec (b : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Obtains the `[Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` whose 2's complement representation is the given `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.toBitVec "Permalink")def
```


Int64.toBitVec (x : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 64


Int64.toBitVec (x : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 64


```

Obtain the `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec")` that contains the 2's complement representation of the `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.ofBitVec "Permalink")def
```


Int64.ofBitVec (b : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 64) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.ofBitVec (b : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 64) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Obtains the `[Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` whose 2's complement representation is the given `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 64`.
####  20.4.4.3.6. To and From Finite Numbers[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Fixed-Precision-Integers--API-Reference--Conversions--To-and-From-Finite-Numbers "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.toFin "Permalink")def
```


USize.toFin (x : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [USize.size](Basic-Types/Fixed-Precision-Integers/#USize___size "Documentation for USize.size")


USize.toFin (x : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [USize.size](Basic-Types/Fixed-Precision-Integers/#USize___size "Documentation for USize.size")


```

Converts a `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")` into the corresponding `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [USize.size](Basic-Types/Fixed-Precision-Integers/#USize___size "Documentation for USize.size")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.toFin "Permalink")def
```


UInt8.toFin (x : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt8.size](Basic-Types/Fixed-Precision-Integers/#UInt8___size "Documentation for UInt8.size")


UInt8.toFin (x : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt8.size](Basic-Types/Fixed-Precision-Integers/#UInt8___size "Documentation for UInt8.size")


```

Converts a `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")` into the corresponding `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt8.size](Basic-Types/Fixed-Precision-Integers/#UInt8___size "Documentation for UInt8.size")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.toFin "Permalink")def
```


UInt16.toFin (x : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt16.size](Basic-Types/Fixed-Precision-Integers/#UInt16___size "Documentation for UInt16.size")


UInt16.toFin (x : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) :
  [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt16.size](Basic-Types/Fixed-Precision-Integers/#UInt16___size "Documentation for UInt16.size")


```

Converts a `[UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")` into the corresponding `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt16.size](Basic-Types/Fixed-Precision-Integers/#UInt16___size "Documentation for UInt16.size")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.toFin "Permalink")def
```


UInt32.toFin (x : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt32.size](Basic-Types/Fixed-Precision-Integers/#UInt32___size "Documentation for UInt32.size")


UInt32.toFin (x : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) :
  [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt32.size](Basic-Types/Fixed-Precision-Integers/#UInt32___size "Documentation for UInt32.size")


```

Converts a `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")` into the corresponding `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt32.size](Basic-Types/Fixed-Precision-Integers/#UInt32___size "Documentation for UInt32.size")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.toFin "Permalink")def
```


UInt64.toFin (x : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt64.size](Basic-Types/Fixed-Precision-Integers/#UInt64___size "Documentation for UInt64.size")


UInt64.toFin (x : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) :
  [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt64.size](Basic-Types/Fixed-Precision-Integers/#UInt64___size "Documentation for UInt64.size")


```

Converts a `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")` into the corresponding `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt64.size](Basic-Types/Fixed-Precision-Integers/#UInt64___size "Documentation for UInt64.size")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.ofFin "Permalink")def
```


USize.ofFin (a : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [USize.size](Basic-Types/Fixed-Precision-Integers/#USize___size "Documentation for USize.size")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


USize.ofFin (a : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [USize.size](Basic-Types/Fixed-Precision-Integers/#USize___size "Documentation for USize.size")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Converts a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [USize.size](Basic-Types/Fixed-Precision-Integers/#USize___size "Documentation for USize.size")` into the corresponding `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.ofFin "Permalink")def
```


UInt8.ofFin (a : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt8.size](Basic-Types/Fixed-Precision-Integers/#UInt8___size "Documentation for UInt8.size")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt8.ofFin (a : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt8.size](Basic-Types/Fixed-Precision-Integers/#UInt8___size "Documentation for UInt8.size")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Converts a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt8.size](Basic-Types/Fixed-Precision-Integers/#UInt8___size "Documentation for UInt8.size")` into the corresponding `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.ofFin "Permalink")def
```


UInt16.ofFin (a : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt16.size](Basic-Types/Fixed-Precision-Integers/#UInt16___size "Documentation for UInt16.size")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt16.ofFin (a : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt16.size](Basic-Types/Fixed-Precision-Integers/#UInt16___size "Documentation for UInt16.size")) :
  [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Converts a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt16.size](Basic-Types/Fixed-Precision-Integers/#UInt16___size "Documentation for UInt16.size")` into the corresponding `[UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.ofFin "Permalink")def
```


UInt32.ofFin (a : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt32.size](Basic-Types/Fixed-Precision-Integers/#UInt32___size "Documentation for UInt32.size")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt32.ofFin (a : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt32.size](Basic-Types/Fixed-Precision-Integers/#UInt32___size "Documentation for UInt32.size")) :
  [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Converts a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt32.size](Basic-Types/Fixed-Precision-Integers/#UInt32___size "Documentation for UInt32.size")` into the corresponding `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.ofFin "Permalink")def
```


UInt64.ofFin (a : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt64.size](Basic-Types/Fixed-Precision-Integers/#UInt64___size "Documentation for UInt64.size")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt64.ofFin (a : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt64.size](Basic-Types/Fixed-Precision-Integers/#UInt64___size "Documentation for UInt64.size")) :
  [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Converts a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") [UInt64.size](Basic-Types/Fixed-Precision-Integers/#UInt64___size "Documentation for UInt64.size")` into the corresponding `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.repr "Permalink")def
```


USize.repr (n : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


USize.repr (n : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Converts a word-sized unsigned integer into a decimal string.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[USize.repr](Basic-Types/Fixed-Precision-Integers/#USize___repr "Documentation for USize.repr") 0 = "0"`
  * `[USize.repr](Basic-Types/Fixed-Precision-Integers/#USize___repr "Documentation for USize.repr") 28 = "28"`
  * `[USize.repr](Basic-Types/Fixed-Precision-Integers/#USize___repr "Documentation for USize.repr") 307 = "307"`


####  20.4.4.3.7. To Characters[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Fixed-Precision-Integers--API-Reference--Conversions--To-Characters "Permalink")
The `[Char](Basic-Types/Characters/#Char___mk "Documentation for Char")` type is a wrapper around `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")` that requires a proof that the wrapped integer represents a Unicode code point. This predicate is part of the `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")` API.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.isValidChar "Permalink")def
```


UInt32.isValidChar (n : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : Prop


UInt32.isValidChar (n : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : Prop


```

A `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")` denotes a valid Unicode code point if it is less than `0x110000` and it is also not a surrogate code point (the range `0xd800` to `0xdfff` inclusive).
###  20.4.4.4. Comparisons[🔗](find/?domain=Verso.Genre.Manual.section&name=fixed-int-comparisons "Permalink")
The operators in this section are rarely invoked by name. Typically, comparisons operations on fixed-width integers should use the decidability of the corresponding relations, which consist of the equality type `[Eq](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")` and those implemented in instances of `[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE")` and `[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.le "Permalink")def
```


USize.le (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : Prop


USize.le (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : Prop


```

Non-strict inequality of word-sized unsigned integers, defined as inequality of the corresponding natural numbers. Usually accessed via the `≤` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.le "Permalink")def
```


ISize.le (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : Prop


ISize.le (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : Prop


```

Non-strict inequality of word-sized signed integers, defined as inequality of the corresponding integers. Usually accessed via the `≤` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.le "Permalink")def
```


UInt8.le (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : Prop


UInt8.le (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : Prop


```

Non-strict inequality of 8-bit unsigned integers, defined as inequality of the corresponding natural numbers. Usually accessed via the `≤` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.le "Permalink")def
```


Int8.le (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : Prop


Int8.le (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : Prop


```

Non-strict inequality of 8-bit signed integers, defined as inequality of the corresponding integers. Usually accessed via the `≤` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.le "Permalink")def
```


UInt16.le (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : Prop


UInt16.le (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : Prop


```

Non-strict inequality of 16-bit unsigned integers, defined as inequality of the corresponding natural numbers. Usually accessed via the `≤` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.le "Permalink")def
```


Int16.le (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : Prop


Int16.le (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : Prop


```

Non-strict inequality of 16-bit signed integers, defined as inequality of the corresponding integers. Usually accessed via the `≤` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.le "Permalink")def
```


UInt32.le (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : Prop


UInt32.le (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : Prop


```

Non-strict inequality of 32-bit unsigned integers, defined as inequality of the corresponding natural numbers. Usually accessed via the `≤` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.le "Permalink")def
```


Int32.le (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : Prop


Int32.le (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : Prop


```

Non-strict inequality of 32-bit signed integers, defined as inequality of the corresponding integers. Usually accessed via the `≤` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.le "Permalink")def
```


UInt64.le (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : Prop


UInt64.le (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : Prop


```

Non-strict inequality of 64-bit unsigned integers, defined as inequality of the corresponding natural numbers. Usually accessed via the `≤` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.le "Permalink")def
```


Int64.le (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : Prop


Int64.le (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : Prop


```

Non-strict inequality of 64-bit signed integers, defined as inequality of the corresponding integers. Usually accessed via the `≤` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.lt "Permalink")def
```


USize.lt (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : Prop


USize.lt (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : Prop


```

Strict inequality of word-sized unsigned integers, defined as inequality of the corresponding natural numbers. Usually accessed via the `<` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.lt "Permalink")def
```


ISize.lt (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : Prop


ISize.lt (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : Prop


```

Strict inequality of word-sized signed integers, defined as inequality of the corresponding integers. Usually accessed via the `<` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.lt "Permalink")def
```


UInt8.lt (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : Prop


UInt8.lt (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : Prop


```

Strict inequality of 8-bit unsigned integers, defined as inequality of the corresponding natural numbers. Usually accessed via the `<` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.lt "Permalink")def
```


Int8.lt (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : Prop


Int8.lt (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : Prop


```

Strict inequality of 8-bit signed integers, defined as inequality of the corresponding integers. Usually accessed via the `<` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.lt "Permalink")def
```


UInt16.lt (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : Prop


UInt16.lt (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : Prop


```

Strict inequality of 16-bit unsigned integers, defined as inequality of the corresponding natural numbers. Usually accessed via the `<` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.lt "Permalink")def
```


Int16.lt (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : Prop


Int16.lt (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : Prop


```

Strict inequality of 16-bit signed integers, defined as inequality of the corresponding integers. Usually accessed via the `<` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.lt "Permalink")def
```


UInt32.lt (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : Prop


UInt32.lt (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : Prop


```

Strict inequality of 32-bit unsigned integers, defined as inequality of the corresponding natural numbers. Usually accessed via the `<` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.lt "Permalink")def
```


Int32.lt (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : Prop


Int32.lt (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : Prop


```

Strict inequality of 32-bit signed integers, defined as inequality of the corresponding integers. Usually accessed via the `<` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.lt "Permalink")def
```


UInt64.lt (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : Prop


UInt64.lt (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : Prop


```

Strict inequality of 64-bit unsigned integers, defined as inequality of the corresponding natural numbers. Usually accessed via the `<` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.lt "Permalink")def
```


Int64.lt (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : Prop


Int64.lt (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : Prop


```

Strict inequality of 64-bit signed integers, defined as inequality of the corresponding integers. Usually accessed via the `<` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.decEq "Permalink")def
```


USize.decEq (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


USize.decEq (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


```

Decides whether two word-sized unsigned integers are equal. Usually accessed via the `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[USize.decEq](Basic-Types/Fixed-Precision-Integers/#USize___decEq "Documentation for USize.decEq") 123 123 = [.isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (6 : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) = 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show (7 : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) = 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.decEq "Permalink")def
```


ISize.decEq (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


ISize.decEq (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


```

Decides whether two word-sized signed integers are equal. Usually accessed via the `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[ISize.decEq](Basic-Types/Fixed-Precision-Integers/#ISize___decEq "Documentation for ISize.decEq") 123 123 = [.isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") ((-7) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) = 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show (7 : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) = 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.decEq "Permalink")def
```


UInt8.decEq (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


UInt8.decEq (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


```

Decides whether two 8-bit unsigned integers are equal. Usually accessed via the `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[UInt8.decEq](Basic-Types/Fixed-Precision-Integers/#UInt8___decEq "Documentation for UInt8.decEq") 123 123 = [.isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (6 : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) = 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show (7 : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) = 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.decEq "Permalink")def
```


Int8.decEq (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


Int8.decEq (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


```

Decides whether two 8-bit signed integers are equal. Usually accessed via the `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int8.decEq](Basic-Types/Fixed-Precision-Integers/#Int8___decEq "Documentation for Int8.decEq") 123 123 = [.isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") ((-7) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) = 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show (7 : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) = 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.decEq "Permalink")def
```


UInt16.decEq (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


UInt16.decEq (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


```

Decides whether two 16-bit unsigned integers are equal. Usually accessed via the `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[UInt16.decEq](Basic-Types/Fixed-Precision-Integers/#UInt16___decEq "Documentation for UInt16.decEq") 123 123 = [.isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (6 : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) = 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show (7 : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) = 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.decEq "Permalink")def
```


Int16.decEq (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


Int16.decEq (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


```

Decides whether two 16-bit signed integers are equal. Usually accessed via the `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int16.decEq](Basic-Types/Fixed-Precision-Integers/#Int16___decEq "Documentation for Int16.decEq") 123 123 = [.isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") ((-7) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) = 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show (7 : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) = 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.decEq "Permalink")def
```


UInt32.decEq (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


UInt32.decEq (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


```

Decides whether two 32-bit unsigned integers are equal. Usually accessed via the `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[UInt32.decEq](Basic-Types/Fixed-Precision-Integers/#UInt32___decEq "Documentation for UInt32.decEq") 123 123 = [.isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (6 : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) = 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show (7 : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) = 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.decEq "Permalink")def
```


Int32.decEq (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


Int32.decEq (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


```

Decides whether two 32-bit signed integers are equal. Usually accessed via the `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int32.decEq](Basic-Types/Fixed-Precision-Integers/#Int32___decEq "Documentation for Int32.decEq") 123 123 = [.isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") ((-7) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) = 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show (7 : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) = 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.decEq "Permalink")def
```


UInt64.decEq (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


UInt64.decEq (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


```

Decides whether two 64-bit unsigned integers are equal. Usually accessed via the `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[UInt64.decEq](Basic-Types/Fixed-Precision-Integers/#UInt64___decEq "Documentation for UInt64.decEq") 123 123 = [.isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (6 : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) = 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show (7 : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) = 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.decEq "Permalink")def
```


Int64.decEq (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


Int64.decEq (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


```

Decides whether two 64-bit signed integers are equal. Usually accessed via the `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int64.decEq](Basic-Types/Fixed-Precision-Integers/#Int64___decEq "Documentation for Int64.decEq") 123 123 = [.isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") ((-7) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) = 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show (7 : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) = 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.decLe "Permalink")def
```


USize.decLe (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


USize.decLe (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


```

Decides whether one word-sized unsigned integer is less than or equal to another. Usually accessed via the `[DecidableLE](Type-Classes/Basic-Classes/#DecidableLE "Documentation for DecidableLE") [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) ≤ 15 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) ≤ 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (5 : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) ≤ 15 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `show (7 : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) ≤ 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.decLe "Permalink")def
```


ISize.decLe (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


ISize.decLe (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


```

Decides whether one word-sized signed integer is less than or equal to another. Usually accessed via the `[DecidableLE](Type-Classes/Basic-Classes/#DecidableLE "Documentation for DecidableLE") [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") ((-7) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) ≤ 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) ≤ 15 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) ≤ 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show (7 : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) ≤ 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.decLe "Permalink")def
```


UInt8.decLe (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


UInt8.decLe (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


```

Decides whether one 8-bit unsigned integer is less than or equal to another. Usually accessed via the `[DecidableLE](Type-Classes/Basic-Classes/#DecidableLE "Documentation for DecidableLE") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) ≤ 15 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) ≤ 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (5 : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) ≤ 15 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `show (7 : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) ≤ 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.decLe "Permalink")def
```


Int8.decLe (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


Int8.decLe (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


```

Decides whether one 8-bit signed integer is less than or equal to another. Usually accessed via the `[DecidableLE](Type-Classes/Basic-Classes/#DecidableLE "Documentation for DecidableLE") [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") ((-7) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) ≤ 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) ≤ 15 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) ≤ 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show (7 : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) ≤ 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.decLe "Permalink")def
```


UInt16.decLe (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


UInt16.decLe (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


```

Decides whether one 16-bit unsigned integer is less than or equal to another. Usually accessed via the `[DecidableLE](Type-Classes/Basic-Classes/#DecidableLE "Documentation for DecidableLE") [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) ≤ 15 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) ≤ 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (5 : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) ≤ 15 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `show (7 : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) ≤ 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.decLe "Permalink")def
```


Int16.decLe (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


Int16.decLe (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


```

Decides whether one 16-bit signed integer is less than or equal to another. Usually accessed via the `[DecidableLE](Type-Classes/Basic-Classes/#DecidableLE "Documentation for DecidableLE") [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") ((-7) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) ≤ 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) ≤ 15 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) ≤ 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show (7 : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) ≤ 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.decLe "Permalink")def
```


UInt32.decLe (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


UInt32.decLe (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


```

Decides whether one 32-bit signed integer is less than or equal to another. Usually accessed via the `[DecidableLE](Type-Classes/Basic-Classes/#DecidableLE "Documentation for DecidableLE") [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) ≤ 15 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) ≤ 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (5 : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) ≤ 15 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `show (7 : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) ≤ 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.decLe "Permalink")def
```


Int32.decLe (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


Int32.decLe (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


```

Decides whether one 32-bit signed integer is less than or equal to another. Usually accessed via the `[DecidableLE](Type-Classes/Basic-Classes/#DecidableLE "Documentation for DecidableLE") [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") ((-7) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) ≤ 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) ≤ 15 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) ≤ 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show (7 : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) ≤ 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.decLe "Permalink")def
```


UInt64.decLe (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


UInt64.decLe (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


```

Decides whether one 64-bit unsigned integer is less than or equal to another. Usually accessed via the `[DecidableLE](Type-Classes/Basic-Classes/#DecidableLE "Documentation for DecidableLE") [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) ≤ 15 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) ≤ 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (5 : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) ≤ 15 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `show (7 : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) ≤ 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.decLe "Permalink")def
```


Int64.decLe (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


Int64.decLe (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") b[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


```

Decides whether one 8-bit signed integer is less than or equal to another. Usually accessed via the `[DecidableLE](Type-Classes/Basic-Classes/#DecidableLE "Documentation for DecidableLE") [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") ((-7) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) ≤ 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) ≤ 15 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (15 : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) ≤ 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show (7 : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) ≤ 7 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.decLt "Permalink")def
```


USize.decLt (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


USize.decLt (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


```

Decides whether one word-sized unsigned integer is strictly less than another. Usually accessed via the `[DecidableLT](Type-Classes/Basic-Classes/#DecidableLT "Documentation for DecidableLT") [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (6 : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) < 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (5 : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) < 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show ¬((7 : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) < 7) by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.decLt "Permalink")def
```


ISize.decLt (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


ISize.decLt (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


```

Decides whether one word-sized signed integer is strictly less than another. Usually accessed via the `[DecidableLT](Type-Classes/Basic-Classes/#DecidableLT "Documentation for DecidableLT") [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") ((-7) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) < 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (5 : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) < 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show ¬((7 : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) < 7) by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.decLt "Permalink")def
```


UInt8.decLt (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


UInt8.decLt (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


```

Decides whether one 8-bit unsigned integer is strictly less than another. Usually accessed via the `[DecidableLT](Type-Classes/Basic-Classes/#DecidableLT "Documentation for DecidableLT") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (6 : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) < 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (5 : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) < 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show ¬((7 : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) < 7) by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.decLt "Permalink")def
```


Int8.decLt (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


Int8.decLt (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


```

Decides whether one 8-bit signed integer is strictly less than another. Usually accessed via the `[DecidableLT](Type-Classes/Basic-Classes/#DecidableLT "Documentation for DecidableLT") [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") ((-7) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) < 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (5 : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) < 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show ¬((7 : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) < 7) by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.decLt "Permalink")def
```


UInt16.decLt (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


UInt16.decLt (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


```

Decides whether one 16-bit unsigned integer is strictly less than another. Usually accessed via the `[DecidableLT](Type-Classes/Basic-Classes/#DecidableLT "Documentation for DecidableLT") [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (6 : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) < 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (5 : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) < 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show ¬((7 : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) < 7) by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.decLt "Permalink")def
```


Int16.decLt (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


Int16.decLt (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


```

Decides whether one 16-bit signed integer is strictly less than another. Usually accessed via the `[DecidableLT](Type-Classes/Basic-Classes/#DecidableLT "Documentation for DecidableLT") [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") ((-7) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) < 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (5 : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) < 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show ¬((7 : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) < 7) by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.decLt "Permalink")def
```


UInt32.decLt (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


UInt32.decLt (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


```

Decides whether one 8-bit unsigned integer is strictly less than another. Usually accessed via the `[DecidableLT](Type-Classes/Basic-Classes/#DecidableLT "Documentation for DecidableLT") [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (6 : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) < 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (5 : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) < 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show ¬((7 : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) < 7) by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.decLt "Permalink")def
```


Int32.decLt (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


Int32.decLt (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


```

Decides whether one 32-bit signed integer is strictly less than another. Usually accessed via the `[DecidableLT](Type-Classes/Basic-Classes/#DecidableLT "Documentation for DecidableLT") [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") ((-7) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) < 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (5 : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) < 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show ¬((7 : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) < 7) by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.decLt "Permalink")def
```


UInt64.decLt (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


UInt64.decLt (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


```

Decides whether one 64-bit unsigned integer is strictly less than another. Usually accessed via the `[DecidableLT](Type-Classes/Basic-Classes/#DecidableLT "Documentation for DecidableLT") [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (6 : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) < 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (5 : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) < 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show ¬((7 : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) < 7) by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.decLt "Permalink")def
```


Int64.decLt (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


Int64.decLt (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")a [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


```

Decides whether one 8-bit signed integer is strictly less than another. Usually accessed via the `[DecidableLT](Type-Classes/Basic-Classes/#DecidableLT "Documentation for DecidableLT") [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")` instance.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") ((-7) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) < 7 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (5 : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) < 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show ¬((7 : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) < 7) by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


###  20.4.4.5. Arithmetic[🔗](find/?domain=Verso.Genre.Manual.section&name=fixed-int-arithmetic "Permalink")
Typically, arithmetic operations on fixed-width integers should be accessed using Lean's overloaded arithmetic notation, particularly their instances of `[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add")`, `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub")`, `[Mul](Type-Classes/Basic-Classes/#Mul___mk "Documentation for Mul")`, `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div")`, and `[Mod](Type-Classes/Basic-Classes/#Mod___mk "Documentation for Mod")`, as well as `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg")` for signed types.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.neg "Permalink")def
```


ISize.neg (i : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.neg (i : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Negates word-sized signed integers. Usually accessed via the `-` prefix operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.neg "Permalink")def
```


Int8.neg (i : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.neg (i : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Negates 8-bit signed integers. Usually accessed via the `-` prefix operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.neg "Permalink")def
```


Int16.neg (i : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.neg (i : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Negates 16-bit signed integers. Usually accessed via the `-` prefix operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.neg "Permalink")def
```


Int32.neg (i : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.neg (i : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Negates 32-bit signed integers. Usually accessed via the `-` prefix operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.neg "Permalink")def
```


Int64.neg (i : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.neg (i : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Negates 64-bit signed integers. Usually accessed via the `-` prefix operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.neg "Permalink")def
```


USize.neg (a : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


USize.neg (a : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Negation of word-sized unsigned integers, computed modulo `[USize.size](Basic-Types/Fixed-Precision-Integers/#USize___size "Documentation for USize.size")`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.neg "Permalink")def
```


UInt8.neg (a : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt8.neg (a : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Negation of 8-bit unsigned integers, computed modulo `[UInt8.size](Basic-Types/Fixed-Precision-Integers/#UInt8___size "Documentation for UInt8.size")`.
`[UInt8.neg](Basic-Types/Fixed-Precision-Integers/#UInt8___neg "Documentation for UInt8.neg") a` is equivalent to `255 - a + 1`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.neg "Permalink")def
```


UInt16.neg (a : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt16.neg (a : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Negation of 16-bit unsigned integers, computed modulo `[UInt16.size](Basic-Types/Fixed-Precision-Integers/#UInt16___size "Documentation for UInt16.size")`.
`[UInt16.neg](Basic-Types/Fixed-Precision-Integers/#UInt16___neg "Documentation for UInt16.neg") a` is equivalent to `65_535 - a + 1`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.neg "Permalink")def
```


UInt32.neg (a : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt32.neg (a : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Negation of 32-bit unsigned integers, computed modulo `[UInt32.size](Basic-Types/Fixed-Precision-Integers/#UInt32___size "Documentation for UInt32.size")`.
`[UInt32.neg](Basic-Types/Fixed-Precision-Integers/#UInt32___neg "Documentation for UInt32.neg") a` is equivalent to `429_4967_295 - a + 1`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.neg "Permalink")def
```


UInt64.neg (a : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt64.neg (a : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Negation of 64-bit unsigned integers, computed modulo `[UInt64.size](Basic-Types/Fixed-Precision-Integers/#UInt64___size "Documentation for UInt64.size")`.
`[UInt64.neg](Basic-Types/Fixed-Precision-Integers/#UInt64___neg "Documentation for UInt64.neg") a` is equivalent to `18_446_744_073_709_551_615 - a + 1`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.add "Permalink")def
```


USize.add (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


USize.add (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Adds two word-sized unsigned integers, wrapping around on overflow. Usually accessed via the `+` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.add "Permalink")def
```


ISize.add (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.add (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Adds two word-sized signed integers, wrapping around on over- or underflow. Usually accessed via the `+` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.add "Permalink")def
```


UInt8.add (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt8.add (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Adds two 8-bit unsigned integers, wrapping around on overflow. Usually accessed via the `+` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.add "Permalink")def
```


Int8.add (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.add (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Adds two 8-bit signed integers, wrapping around on over- or underflow. Usually accessed via the `+` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.add "Permalink")def
```


UInt16.add (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt16.add (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Adds two 16-bit unsigned integers, wrapping around on overflow. Usually accessed via the `+` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.add "Permalink")def
```


Int16.add (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.add (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Adds two 16-bit signed integers, wrapping around on over- or underflow. Usually accessed via the `+` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.add "Permalink")def
```


UInt32.add (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt32.add (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Adds two 32-bit unsigned integers, wrapping around on overflow. Usually accessed via the `+` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.add "Permalink")def
```


Int32.add (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.add (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Adds two 32-bit signed integers, wrapping around on over- or underflow. Usually accessed via the `+` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.add "Permalink")def
```


UInt64.add (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt64.add (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Adds two 64-bit unsigned integers, wrapping around on overflow. Usually accessed via the `+` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.add "Permalink")def
```


Int64.add (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.add (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Adds two 64-bit signed integers, wrapping around on over- or underflow. Usually accessed via the `+` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.sub "Permalink")def
```


USize.sub (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


USize.sub (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Subtracts one word-sized-bit unsigned integer from another, wrapping around on underflow. Usually accessed via the `-` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.sub "Permalink")def
```


ISize.sub (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.sub (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Subtracts one word-sized signed integer from another, wrapping around on over- or underflow. Usually accessed via the `-` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.sub "Permalink")def
```


UInt8.sub (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt8.sub (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Subtracts one 8-bit unsigned integer from another, wrapping around on underflow. Usually accessed via the `-` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.sub "Permalink")def
```


Int8.sub (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.sub (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Subtracts one 8-bit signed integer from another, wrapping around on over- or underflow. Usually accessed via the `-` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.sub "Permalink")def
```


UInt16.sub (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt16.sub (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Subtracts one 16-bit unsigned integer from another, wrapping around on underflow. Usually accessed via the `-` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.sub "Permalink")def
```


Int16.sub (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.sub (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Subtracts one 16-bit signed integer from another, wrapping around on over- or underflow. Usually accessed via the `-` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.sub "Permalink")def
```


UInt32.sub (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt32.sub (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Subtracts one 32-bit unsigned integer from another, wrapping around on underflow. Usually accessed via the `-` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.sub "Permalink")def
```


Int32.sub (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.sub (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Subtracts one 32-bit signed integer from another, wrapping around on over- or underflow. Usually accessed via the `-` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.sub "Permalink")def
```


UInt64.sub (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt64.sub (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Subtracts one 64-bit unsigned integer from another, wrapping around on underflow. Usually accessed via the `-` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.sub "Permalink")def
```


Int64.sub (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.sub (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Subtracts one 64-bit signed integer from another, wrapping around on over- or underflow. Usually accessed via the `-` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.mul "Permalink")def
```


USize.mul (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


USize.mul (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Multiplies two word-sized unsigned integers, wrapping around on overflow. Usually accessed via the `*` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.mul "Permalink")def
```


ISize.mul (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.mul (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Multiplies two word-sized signed integers, wrapping around on over- or underflow. Usually accessed via the `*` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.mul "Permalink")def
```


UInt8.mul (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt8.mul (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Multiplies two 8-bit unsigned integers, wrapping around on overflow. Usually accessed via the `*` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.mul "Permalink")def
```


Int8.mul (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.mul (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Multiplies two 8-bit signed integers, wrapping around on over- or underflow. Usually accessed via the `*` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.mul "Permalink")def
```


UInt16.mul (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt16.mul (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Multiplies two 16-bit unsigned integers, wrapping around on overflow. Usually accessed via the `*` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.mul "Permalink")def
```


Int16.mul (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.mul (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Multiplies two 16-bit signed integers, wrapping around on over- or underflow. Usually accessed via the `*` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.mul "Permalink")def
```


UInt32.mul (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt32.mul (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Multiplies two 32-bit unsigned integers, wrapping around on overflow. Usually accessed via the `*` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.mul "Permalink")def
```


Int32.mul (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.mul (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Multiplies two 32-bit signed integers, wrapping around on over- or underflow. Usually accessed via the `*` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.mul "Permalink")def
```


UInt64.mul (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt64.mul (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Multiplies two 64-bit unsigned integers, wrapping around on overflow. Usually accessed via the `*` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.mul "Permalink")def
```


Int64.mul (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.mul (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Multiplies two 64-bit signed integers, wrapping around on over- or underflow. Usually accessed via the `*` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.div "Permalink")def
```


USize.div (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


USize.div (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Unsigned division for word-sized unsigned integers, discarding the remainder. Usually accessed via the `/` operator.
This operation is sometimes called “floor division.” Division by zero is defined to be zero.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.div "Permalink")def
```


ISize.div (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.div (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Truncating division for word-sized signed integers, rounding towards zero. Usually accessed via the `/` operator.
Division by zero is defined to be zero.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[ISize.div](Basic-Types/Fixed-Precision-Integers/#ISize___div "Documentation for ISize.div") 10 3 = 3`
  * `[ISize.div](Basic-Types/Fixed-Precision-Integers/#ISize___div "Documentation for ISize.div") 10 (-3) = (-3)`
  * `[ISize.div](Basic-Types/Fixed-Precision-Integers/#ISize___div "Documentation for ISize.div") (-10) (-3) = 3`
  * `[ISize.div](Basic-Types/Fixed-Precision-Integers/#ISize___div "Documentation for ISize.div") (-10) 3 = (-3)`
  * `[ISize.div](Basic-Types/Fixed-Precision-Integers/#ISize___div "Documentation for ISize.div") 10 0 = 0`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.div "Permalink")def
```


UInt8.div (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt8.div (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Unsigned division for 8-bit unsigned integers, discarding the remainder. Usually accessed via the `/` operator.
This operation is sometimes called “floor division.” Division by zero is defined to be zero.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.div "Permalink")def
```


Int8.div (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.div (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Truncating division for 8-bit signed integers, rounding towards zero. Usually accessed via the `/` operator.
Division by zero is defined to be zero.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int8.div](Basic-Types/Fixed-Precision-Integers/#Int8___div "Documentation for Int8.div") 10 3 = 3`
  * `[Int8.div](Basic-Types/Fixed-Precision-Integers/#Int8___div "Documentation for Int8.div") 10 (-3) = (-3)`
  * `[Int8.div](Basic-Types/Fixed-Precision-Integers/#Int8___div "Documentation for Int8.div") (-10) (-3) = 3`
  * `[Int8.div](Basic-Types/Fixed-Precision-Integers/#Int8___div "Documentation for Int8.div") (-10) 3 = (-3)`
  * `[Int8.div](Basic-Types/Fixed-Precision-Integers/#Int8___div "Documentation for Int8.div") 10 0 = 0`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.div "Permalink")def
```


UInt16.div (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt16.div (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Unsigned division for 16-bit unsigned integers, discarding the remainder. Usually accessed via the `/` operator.
This operation is sometimes called “floor division.” Division by zero is defined to be zero.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.div "Permalink")def
```


Int16.div (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.div (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Truncating division for 16-bit signed integers, rounding towards zero. Usually accessed via the `/` operator.
Division by zero is defined to be zero.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int16.div](Basic-Types/Fixed-Precision-Integers/#Int16___div "Documentation for Int16.div") 10 3 = 3`
  * `[Int16.div](Basic-Types/Fixed-Precision-Integers/#Int16___div "Documentation for Int16.div") 10 (-3) = (-3)`
  * `[Int16.div](Basic-Types/Fixed-Precision-Integers/#Int16___div "Documentation for Int16.div") (-10) (-3) = 3`
  * `[Int16.div](Basic-Types/Fixed-Precision-Integers/#Int16___div "Documentation for Int16.div") (-10) 3 = (-3)`
  * `[Int16.div](Basic-Types/Fixed-Precision-Integers/#Int16___div "Documentation for Int16.div") 10 0 = 0`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.div "Permalink")def
```


UInt32.div (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt32.div (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Unsigned division for 32-bit unsigned integers, discarding the remainder. Usually accessed via the `/` operator.
This operation is sometimes called “floor division.” Division by zero is defined to be zero.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.div "Permalink")def
```


Int32.div (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.div (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Truncating division for 32-bit signed integers, rounding towards zero. Usually accessed via the `/` operator.
Division by zero is defined to be zero.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int32.div](Basic-Types/Fixed-Precision-Integers/#Int32___div "Documentation for Int32.div") 10 3 = 3`
  * `[Int32.div](Basic-Types/Fixed-Precision-Integers/#Int32___div "Documentation for Int32.div") 10 (-3) = (-3)`
  * `[Int32.div](Basic-Types/Fixed-Precision-Integers/#Int32___div "Documentation for Int32.div") (-10) (-3) = 3`
  * `[Int32.div](Basic-Types/Fixed-Precision-Integers/#Int32___div "Documentation for Int32.div") (-10) 3 = (-3)`
  * `[Int32.div](Basic-Types/Fixed-Precision-Integers/#Int32___div "Documentation for Int32.div") 10 0 = 0`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.div "Permalink")def
```


UInt64.div (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt64.div (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Unsigned division for 64-bit unsigned integers, discarding the remainder. Usually accessed via the `/` operator.
This operation is sometimes called “floor division.” Division by zero is defined to be zero.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.div "Permalink")def
```


Int64.div (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.div (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Truncating division for 64-bit signed integers, rounding towards zero. Usually accessed via the `/` operator.
Division by zero is defined to be zero.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int64.div](Basic-Types/Fixed-Precision-Integers/#Int64___div "Documentation for Int64.div") 10 3 = 3`
  * `[Int64.div](Basic-Types/Fixed-Precision-Integers/#Int64___div "Documentation for Int64.div") 10 (-3) = (-3)`
  * `[Int64.div](Basic-Types/Fixed-Precision-Integers/#Int64___div "Documentation for Int64.div") (-10) (-3) = 3`
  * `[Int64.div](Basic-Types/Fixed-Precision-Integers/#Int64___div "Documentation for Int64.div") (-10) 3 = (-3)`
  * `[Int64.div](Basic-Types/Fixed-Precision-Integers/#Int64___div "Documentation for Int64.div") 10 0 = 0`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.mod "Permalink")def
```


USize.mod (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


USize.mod (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

The modulo operator for word-sized unsigned integers, which computes the remainder when dividing one integer by another. Usually accessed via the `%` operator.
When the divisor is `0`, the result is the dividend rather than an error.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[USize.mod](Basic-Types/Fixed-Precision-Integers/#USize___mod "Documentation for USize.mod") 5 2 = 1`
  * `[USize.mod](Basic-Types/Fixed-Precision-Integers/#USize___mod "Documentation for USize.mod") 4 2 = 0`
  * `[USize.mod](Basic-Types/Fixed-Precision-Integers/#USize___mod "Documentation for USize.mod") 4 0 = 4`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.mod "Permalink")def
```


ISize.mod (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.mod (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

The modulo operator for word-sized signed integers, which computes the remainder when dividing one integer by another with the T-rounding convention used by `[ISize.div](Basic-Types/Fixed-Precision-Integers/#ISize___div "Documentation for ISize.div")`. Usually accessed via the `%` operator.
When the divisor is `0`, the result is the dividend rather than an error.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[ISize.mod](Basic-Types/Fixed-Precision-Integers/#ISize___mod "Documentation for ISize.mod") 5 2 = 1`
  * `[ISize.mod](Basic-Types/Fixed-Precision-Integers/#ISize___mod "Documentation for ISize.mod") 5 (-2) = 1`
  * `[ISize.mod](Basic-Types/Fixed-Precision-Integers/#ISize___mod "Documentation for ISize.mod") (-5) 2 = (-1)`
  * `[ISize.mod](Basic-Types/Fixed-Precision-Integers/#ISize___mod "Documentation for ISize.mod") (-5) (-2) = (-1)`
  * `[ISize.mod](Basic-Types/Fixed-Precision-Integers/#ISize___mod "Documentation for ISize.mod") 4 2 = 0`
  * `[ISize.mod](Basic-Types/Fixed-Precision-Integers/#ISize___mod "Documentation for ISize.mod") 4 (-2) = 0`
  * `[ISize.mod](Basic-Types/Fixed-Precision-Integers/#ISize___mod "Documentation for ISize.mod") 4 0 = 4`
  * `[ISize.mod](Basic-Types/Fixed-Precision-Integers/#ISize___mod "Documentation for ISize.mod") (-4) 0 = (-4)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.mod "Permalink")def
```


UInt8.mod (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt8.mod (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

The modulo operator for 8-bit unsigned integers, which computes the remainder when dividing one integer by another. Usually accessed via the `%` operator.
When the divisor is `0`, the result is the dividend rather than an error.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[UInt8.mod](Basic-Types/Fixed-Precision-Integers/#UInt8___mod "Documentation for UInt8.mod") 5 2 = 1`
  * `[UInt8.mod](Basic-Types/Fixed-Precision-Integers/#UInt8___mod "Documentation for UInt8.mod") 4 2 = 0`
  * `[UInt8.mod](Basic-Types/Fixed-Precision-Integers/#UInt8___mod "Documentation for UInt8.mod") 4 0 = 4`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.mod "Permalink")def
```


Int8.mod (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.mod (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

The modulo operator for 8-bit signed integers, which computes the remainder when dividing one integer by another with the T-rounding convention used by `[Int8.div](Basic-Types/Fixed-Precision-Integers/#Int8___div "Documentation for Int8.div")`. Usually accessed via the `%` operator.
When the divisor is `0`, the result is the dividend rather than an error.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int8.mod](Basic-Types/Fixed-Precision-Integers/#Int8___mod "Documentation for Int8.mod") 5 2 = 1`
  * `[Int8.mod](Basic-Types/Fixed-Precision-Integers/#Int8___mod "Documentation for Int8.mod") 5 (-2) = 1`
  * `[Int8.mod](Basic-Types/Fixed-Precision-Integers/#Int8___mod "Documentation for Int8.mod") (-5) 2 = (-1)`
  * `[Int8.mod](Basic-Types/Fixed-Precision-Integers/#Int8___mod "Documentation for Int8.mod") (-5) (-2) = (-1)`
  * `[Int8.mod](Basic-Types/Fixed-Precision-Integers/#Int8___mod "Documentation for Int8.mod") 4 2 = 0`
  * `[Int8.mod](Basic-Types/Fixed-Precision-Integers/#Int8___mod "Documentation for Int8.mod") 4 (-2) = 0`
  * `[Int8.mod](Basic-Types/Fixed-Precision-Integers/#Int8___mod "Documentation for Int8.mod") 4 0 = 4`
  * `[Int8.mod](Basic-Types/Fixed-Precision-Integers/#Int8___mod "Documentation for Int8.mod") (-4) 0 = (-4)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.mod "Permalink")def
```


UInt16.mod (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt16.mod (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

The modulo operator for 16-bit unsigned integers, which computes the remainder when dividing one integer by another. Usually accessed via the `%` operator.
When the divisor is `0`, the result is the dividend rather than an error.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[UInt16.mod](Basic-Types/Fixed-Precision-Integers/#UInt16___mod "Documentation for UInt16.mod") 5 2 = 1`
  * `[UInt16.mod](Basic-Types/Fixed-Precision-Integers/#UInt16___mod "Documentation for UInt16.mod") 4 2 = 0`
  * `[UInt16.mod](Basic-Types/Fixed-Precision-Integers/#UInt16___mod "Documentation for UInt16.mod") 4 0 = 4`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.mod "Permalink")def
```


Int16.mod (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.mod (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

The modulo operator for 16-bit signed integers, which computes the remainder when dividing one integer by another with the T-rounding convention used by `[Int16.div](Basic-Types/Fixed-Precision-Integers/#Int16___div "Documentation for Int16.div")`. Usually accessed via the `%` operator.
When the divisor is `0`, the result is the dividend rather than an error.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int16.mod](Basic-Types/Fixed-Precision-Integers/#Int16___mod "Documentation for Int16.mod") 5 2 = 1`
  * `[Int16.mod](Basic-Types/Fixed-Precision-Integers/#Int16___mod "Documentation for Int16.mod") 5 (-2) = 1`
  * `[Int16.mod](Basic-Types/Fixed-Precision-Integers/#Int16___mod "Documentation for Int16.mod") (-5) 2 = (-1)`
  * `[Int16.mod](Basic-Types/Fixed-Precision-Integers/#Int16___mod "Documentation for Int16.mod") (-5) (-2) = (-1)`
  * `[Int16.mod](Basic-Types/Fixed-Precision-Integers/#Int16___mod "Documentation for Int16.mod") 4 2 = 0`
  * `[Int16.mod](Basic-Types/Fixed-Precision-Integers/#Int16___mod "Documentation for Int16.mod") 4 (-2) = 0`
  * `[Int16.mod](Basic-Types/Fixed-Precision-Integers/#Int16___mod "Documentation for Int16.mod") 4 0 = 4`
  * `[Int16.mod](Basic-Types/Fixed-Precision-Integers/#Int16___mod "Documentation for Int16.mod") (-4) 0 = (-4)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.mod "Permalink")def
```


UInt32.mod (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt32.mod (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

The modulo operator for 32-bit unsigned integers, which computes the remainder when dividing one integer by another. Usually accessed via the `%` operator.
When the divisor is `0`, the result is the dividend rather than an error.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[UInt32.mod](Basic-Types/Fixed-Precision-Integers/#UInt32___mod "Documentation for UInt32.mod") 5 2 = 1`
  * `[UInt32.mod](Basic-Types/Fixed-Precision-Integers/#UInt32___mod "Documentation for UInt32.mod") 4 2 = 0`
  * `[UInt32.mod](Basic-Types/Fixed-Precision-Integers/#UInt32___mod "Documentation for UInt32.mod") 4 0 = 4`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.mod "Permalink")def
```


Int32.mod (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.mod (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

The modulo operator for 32-bit signed integers, which computes the remainder when dividing one integer by another with the T-rounding convention used by `[Int32.div](Basic-Types/Fixed-Precision-Integers/#Int32___div "Documentation for Int32.div")`. Usually accessed via the `%` operator.
When the divisor is `0`, the result is the dividend rather than an error.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int32.mod](Basic-Types/Fixed-Precision-Integers/#Int32___mod "Documentation for Int32.mod") 5 2 = 1`
  * `[Int32.mod](Basic-Types/Fixed-Precision-Integers/#Int32___mod "Documentation for Int32.mod") 5 (-2) = 1`
  * `[Int32.mod](Basic-Types/Fixed-Precision-Integers/#Int32___mod "Documentation for Int32.mod") (-5) 2 = (-1)`
  * `[Int32.mod](Basic-Types/Fixed-Precision-Integers/#Int32___mod "Documentation for Int32.mod") (-5) (-2) = (-1)`
  * `[Int32.mod](Basic-Types/Fixed-Precision-Integers/#Int32___mod "Documentation for Int32.mod") 4 2 = 0`
  * `[Int32.mod](Basic-Types/Fixed-Precision-Integers/#Int32___mod "Documentation for Int32.mod") 4 (-2) = 0`
  * `[Int32.mod](Basic-Types/Fixed-Precision-Integers/#Int32___mod "Documentation for Int32.mod") 4 0 = 4`
  * `[Int32.mod](Basic-Types/Fixed-Precision-Integers/#Int32___mod "Documentation for Int32.mod") (-4) 0 = (-4)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.mod "Permalink")def
```


UInt64.mod (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt64.mod (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

The modulo operator for 64-bit unsigned integers, which computes the remainder when dividing one integer by another. Usually accessed via the `%` operator.
When the divisor is `0`, the result is the dividend rather than an error.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[UInt64.mod](Basic-Types/Fixed-Precision-Integers/#UInt64___mod "Documentation for UInt64.mod") 5 2 = 1`
  * `[UInt64.mod](Basic-Types/Fixed-Precision-Integers/#UInt64___mod "Documentation for UInt64.mod") 4 2 = 0`
  * `[UInt64.mod](Basic-Types/Fixed-Precision-Integers/#UInt64___mod "Documentation for UInt64.mod") 4 0 = 4`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.mod "Permalink")def
```


Int64.mod (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.mod (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

The modulo operator for 64-bit signed integers, which computes the remainder when dividing one integer by another with the T-rounding convention used by `[Int64.div](Basic-Types/Fixed-Precision-Integers/#Int64___div "Documentation for Int64.div")`. Usually accessed via the `%` operator.
When the divisor is `0`, the result is the dividend rather than an error.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int64.mod](Basic-Types/Fixed-Precision-Integers/#Int64___mod "Documentation for Int64.mod") 5 2 = 1`
  * `[Int64.mod](Basic-Types/Fixed-Precision-Integers/#Int64___mod "Documentation for Int64.mod") 5 (-2) = 1`
  * `[Int64.mod](Basic-Types/Fixed-Precision-Integers/#Int64___mod "Documentation for Int64.mod") (-5) 2 = (-1)`
  * `[Int64.mod](Basic-Types/Fixed-Precision-Integers/#Int64___mod "Documentation for Int64.mod") (-5) (-2) = (-1)`
  * `[Int64.mod](Basic-Types/Fixed-Precision-Integers/#Int64___mod "Documentation for Int64.mod") 4 2 = 0`
  * `[Int64.mod](Basic-Types/Fixed-Precision-Integers/#Int64___mod "Documentation for Int64.mod") 4 (-2) = 0`
  * `[Int64.mod](Basic-Types/Fixed-Precision-Integers/#Int64___mod "Documentation for Int64.mod") 4 0 = 4`
  * `[Int64.mod](Basic-Types/Fixed-Precision-Integers/#Int64___mod "Documentation for Int64.mod") (-4) 0 = (-4)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.log2 "Permalink")def
```


USize.log2 (a : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


USize.log2 (a : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Base-two logarithm of word-sized unsigned integers. Returns `⌊max 0 (log₂ a)⌋`.
This function is overridden at runtime with an efficient implementation. This definition is the logical model.
Examples:
  * `[USize.log2](Basic-Types/Fixed-Precision-Integers/#USize___log2 "Documentation for USize.log2") 0 = 0`
  * `[USize.log2](Basic-Types/Fixed-Precision-Integers/#USize___log2 "Documentation for USize.log2") 1 = 0`
  * `[USize.log2](Basic-Types/Fixed-Precision-Integers/#USize___log2 "Documentation for USize.log2") 2 = 1`
  * `[USize.log2](Basic-Types/Fixed-Precision-Integers/#USize___log2 "Documentation for USize.log2") 4 = 2`
  * `[USize.log2](Basic-Types/Fixed-Precision-Integers/#USize___log2 "Documentation for USize.log2") 7 = 2`
  * `[USize.log2](Basic-Types/Fixed-Precision-Integers/#USize___log2 "Documentation for USize.log2") 8 = 3`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.log2 "Permalink")def
```


UInt8.log2 (a : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt8.log2 (a : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Base-two logarithm of 8-bit unsigned integers. Returns `⌊max 0 (log₂ a)⌋`.
This function is overridden at runtime with an efficient implementation. This definition is the logical model.
Examples:
  * `[UInt8.log2](Basic-Types/Fixed-Precision-Integers/#UInt8___log2 "Documentation for UInt8.log2") 0 = 0`
  * `[UInt8.log2](Basic-Types/Fixed-Precision-Integers/#UInt8___log2 "Documentation for UInt8.log2") 1 = 0`
  * `[UInt8.log2](Basic-Types/Fixed-Precision-Integers/#UInt8___log2 "Documentation for UInt8.log2") 2 = 1`
  * `[UInt8.log2](Basic-Types/Fixed-Precision-Integers/#UInt8___log2 "Documentation for UInt8.log2") 4 = 2`
  * `[UInt8.log2](Basic-Types/Fixed-Precision-Integers/#UInt8___log2 "Documentation for UInt8.log2") 7 = 2`
  * `[UInt8.log2](Basic-Types/Fixed-Precision-Integers/#UInt8___log2 "Documentation for UInt8.log2") 8 = 3`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.log2 "Permalink")def
```


UInt16.log2 (a : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt16.log2 (a : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Base-two logarithm of 16-bit unsigned integers. Returns `⌊max 0 (log₂ a)⌋`.
This function is overridden at runtime with an efficient implementation. This definition is the logical model.
Examples:
  * `[UInt16.log2](Basic-Types/Fixed-Precision-Integers/#UInt16___log2 "Documentation for UInt16.log2") 0 = 0`
  * `[UInt16.log2](Basic-Types/Fixed-Precision-Integers/#UInt16___log2 "Documentation for UInt16.log2") 1 = 0`
  * `[UInt16.log2](Basic-Types/Fixed-Precision-Integers/#UInt16___log2 "Documentation for UInt16.log2") 2 = 1`
  * `[UInt16.log2](Basic-Types/Fixed-Precision-Integers/#UInt16___log2 "Documentation for UInt16.log2") 4 = 2`
  * `[UInt16.log2](Basic-Types/Fixed-Precision-Integers/#UInt16___log2 "Documentation for UInt16.log2") 7 = 2`
  * `[UInt16.log2](Basic-Types/Fixed-Precision-Integers/#UInt16___log2 "Documentation for UInt16.log2") 8 = 3`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.log2 "Permalink")def
```


UInt32.log2 (a : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt32.log2 (a : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Base-two logarithm of 32-bit unsigned integers. Returns `⌊max 0 (log₂ a)⌋`.
This function is overridden at runtime with an efficient implementation. This definition is the logical model.
Examples:
  * `[UInt32.log2](Basic-Types/Fixed-Precision-Integers/#UInt32___log2 "Documentation for UInt32.log2") 0 = 0`
  * `[UInt32.log2](Basic-Types/Fixed-Precision-Integers/#UInt32___log2 "Documentation for UInt32.log2") 1 = 0`
  * `[UInt32.log2](Basic-Types/Fixed-Precision-Integers/#UInt32___log2 "Documentation for UInt32.log2") 2 = 1`
  * `[UInt32.log2](Basic-Types/Fixed-Precision-Integers/#UInt32___log2 "Documentation for UInt32.log2") 4 = 2`
  * `[UInt32.log2](Basic-Types/Fixed-Precision-Integers/#UInt32___log2 "Documentation for UInt32.log2") 7 = 2`
  * `[UInt32.log2](Basic-Types/Fixed-Precision-Integers/#UInt32___log2 "Documentation for UInt32.log2") 8 = 3`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.log2 "Permalink")def
```


UInt64.log2 (a : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt64.log2 (a : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Base-two logarithm of 64-bit unsigned integers. Returns `⌊max 0 (log₂ a)⌋`.
This function is overridden at runtime with an efficient implementation. This definition is the logical model.
Examples:
  * `[UInt64.log2](Basic-Types/Fixed-Precision-Integers/#UInt64___log2 "Documentation for UInt64.log2") 0 = 0`
  * `[UInt64.log2](Basic-Types/Fixed-Precision-Integers/#UInt64___log2 "Documentation for UInt64.log2") 1 = 0`
  * `[UInt64.log2](Basic-Types/Fixed-Precision-Integers/#UInt64___log2 "Documentation for UInt64.log2") 2 = 1`
  * `[UInt64.log2](Basic-Types/Fixed-Precision-Integers/#UInt64___log2 "Documentation for UInt64.log2") 4 = 2`
  * `[UInt64.log2](Basic-Types/Fixed-Precision-Integers/#UInt64___log2 "Documentation for UInt64.log2") 7 = 2`
  * `[UInt64.log2](Basic-Types/Fixed-Precision-Integers/#UInt64___log2 "Documentation for UInt64.log2") 8 = 3`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.abs "Permalink")def
```


ISize.abs (a : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.abs (a : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Computes the absolute value of a word-sized signed integer.
This function is equivalent to `[if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") a < 0 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") -a [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") a`, so in particular `[ISize.minValue](Basic-Types/Fixed-Precision-Integers/#ISize___minValue "Documentation for ISize.minValue")` will be mapped to `[ISize.minValue](Basic-Types/Fixed-Precision-Integers/#ISize___minValue "Documentation for ISize.minValue")`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.abs "Permalink")def
```


Int8.abs (a : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.abs (a : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Computes the absolute value of an 8-bit signed integer.
This function is equivalent to `[if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") a < 0 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") -a [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") a`, so in particular `[Int8.minValue](Basic-Types/Fixed-Precision-Integers/#Int8___minValue "Documentation for Int8.minValue")` will be mapped to `[Int8.minValue](Basic-Types/Fixed-Precision-Integers/#Int8___minValue "Documentation for Int8.minValue")`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.abs "Permalink")def
```


Int16.abs (a : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.abs (a : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Computes the absolute value of a 16-bit signed integer.
This function is equivalent to `[if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") a < 0 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") -a [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") a`, so in particular `[Int16.minValue](Basic-Types/Fixed-Precision-Integers/#Int16___minValue "Documentation for Int16.minValue")` will be mapped to `[Int16.minValue](Basic-Types/Fixed-Precision-Integers/#Int16___minValue "Documentation for Int16.minValue")`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.abs "Permalink")def
```


Int32.abs (a : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.abs (a : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Computes the absolute value of a 32-bit signed integer.
This function is equivalent to `[if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") a < 0 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") -a [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") a`, so in particular `[Int32.minValue](Basic-Types/Fixed-Precision-Integers/#Int32___minValue "Documentation for Int32.minValue")` will be mapped to `[Int32.minValue](Basic-Types/Fixed-Precision-Integers/#Int32___minValue "Documentation for Int32.minValue")`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.abs "Permalink")def
```


Int64.abs (a : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.abs (a : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Computes the absolute value of a 64-bit signed integer.
This function is equivalent to `[if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") a < 0 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") -a [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") a`, so in particular `[Int64.minValue](Basic-Types/Fixed-Precision-Integers/#Int64___minValue "Documentation for Int64.minValue")` will be mapped to `[Int64.minValue](Basic-Types/Fixed-Precision-Integers/#Int64___minValue "Documentation for Int64.minValue")`.
This function is overridden at runtime with an efficient implementation.
###  20.4.4.6. Bitwise Operations[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Fixed-Precision-Integers--API-Reference--Bitwise-Operations "Permalink")
Typically, bitwise operations on fixed-width integers should be accessed using Lean's overloaded operators, particularly their instances of `[ShiftLeft](Type-Classes/Basic-Classes/#ShiftLeft___mk "Documentation for ShiftLeft")`, `[ShiftRight](Type-Classes/Basic-Classes/#ShiftRight___mk "Documentation for ShiftRight")`, `[AndOp](Type-Classes/Basic-Classes/#AndOp___mk "Documentation for AndOp")`, `[OrOp](Type-Classes/Basic-Classes/#OrOp___mk "Documentation for OrOp")`, and `[XorOp](Type-Classes/Basic-Classes/#XorOp___mk "Documentation for XorOp")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.land "Permalink")def
```


USize.land (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


USize.land (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Bitwise and for word-sized unsigned integers. Usually accessed via the `&&&` operator.
Each bit of the resulting integer is set if the corresponding bits of both input integers are set.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.land "Permalink")def
```


ISize.land (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.land (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Bitwise and for word-sized signed integers. Usually accessed via the `&&&` operator.
Each bit of the resulting integer is set if the corresponding bits of both input integers are set, according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.land "Permalink")def
```


UInt8.land (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt8.land (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Bitwise and for 8-bit unsigned integers. Usually accessed via the `&&&` operator.
Each bit of the resulting integer is set if the corresponding bits of both input integers are set.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.land "Permalink")def
```


Int8.land (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.land (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Bitwise and for 8-bit signed integers. Usually accessed via the `&&&` operator.
Each bit of the resulting integer is set if the corresponding bits of both input integers are set, according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.land "Permalink")def
```


UInt16.land (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt16.land (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Bitwise and for 16-bit unsigned integers. Usually accessed via the `&&&` operator.
Each bit of the resulting integer is set if the corresponding bits of both input integers are set.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.land "Permalink")def
```


Int16.land (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.land (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Bitwise and for 16-bit signed integers. Usually accessed via the `&&&` operator.
Each bit of the resulting integer is set if the corresponding bits of both input integers are set, according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.land "Permalink")def
```


UInt32.land (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt32.land (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Bitwise and for 32-bit unsigned integers. Usually accessed via the `&&&` operator.
Each bit of the resulting integer is set if the corresponding bits of both input integers are set.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.land "Permalink")def
```


Int32.land (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.land (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Bitwise and for 32-bit signed integers. Usually accessed via the `&&&` operator.
Each bit of the resulting integer is set if the corresponding bits of both input integers are set, according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.land "Permalink")def
```


UInt64.land (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt64.land (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Bitwise and for 64-bit unsigned integers. Usually accessed via the `&&&` operator.
Each bit of the resulting integer is set if the corresponding bits of both input integers are set.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.land "Permalink")def
```


Int64.land (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.land (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Bitwise and for 64-bit signed integers. Usually accessed via the `&&&` operator.
Each bit of the resulting integer is set if the corresponding bits of both input integers are set, according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.lor "Permalink")def
```


USize.lor (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


USize.lor (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Bitwise or for word-sized unsigned integers. Usually accessed via the `|||` operator.
Each bit of the resulting integer is set if at least one of the corresponding bits of both input integers are set.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.lor "Permalink")def
```


ISize.lor (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.lor (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Bitwise or for word-sized signed integers. Usually accessed via the `|||` operator.
Each bit of the resulting integer is set if at least one of the corresponding bits of the input integers is set, according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.lor "Permalink")def
```


UInt8.lor (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt8.lor (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Bitwise or for 8-bit unsigned integers. Usually accessed via the `|||` operator.
Each bit of the resulting integer is set if at least one of the corresponding bits of both input integers are set.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.lor "Permalink")def
```


Int8.lor (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.lor (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Bitwise or for 8-bit signed integers. Usually accessed via the `|||` operator.
Each bit of the resulting integer is set if at least one of the corresponding bits of the input integers is set, according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.lor "Permalink")def
```


UInt16.lor (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt16.lor (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Bitwise or for 16-bit unsigned integers. Usually accessed via the `|||` operator.
Each bit of the resulting integer is set if at least one of the corresponding bits of both input integers are set.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.lor "Permalink")def
```


Int16.lor (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.lor (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Bitwise or for 16-bit signed integers. Usually accessed via the `|||` operator.
Each bit of the resulting integer is set if at least one of the corresponding bits of the input integers is set, according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.lor "Permalink")def
```


UInt32.lor (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt32.lor (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Bitwise or for 32-bit unsigned integers. Usually accessed via the `|||` operator.
Each bit of the resulting integer is set if at least one of the corresponding bits of both input integers are set.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.lor "Permalink")def
```


Int32.lor (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.lor (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Bitwise or for 32-bit signed integers. Usually accessed via the `|||` operator.
Each bit of the resulting integer is set if at least one of the corresponding bits of the input integers is set, according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.lor "Permalink")def
```


UInt64.lor (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt64.lor (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Bitwise or for 64-bit unsigned integers. Usually accessed via the `|||` operator.
Each bit of the resulting integer is set if at least one of the corresponding bits of both input integers are set.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.lor "Permalink")def
```


Int64.lor (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.lor (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Bitwise or for 64-bit signed integers. Usually accessed via the `|||` operator.
Each bit of the resulting integer is set if at least one of the corresponding bits of the input integers is set, according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.xor "Permalink")def
```


USize.xor (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


USize.xor (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Bitwise exclusive or for word-sized unsigned integers. Usually accessed via the `^^^` operator.
Each bit of the resulting integer is set if exactly one of the corresponding bits of both input integers are set.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.xor "Permalink")def
```


ISize.xor (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.xor (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Bitwise exclusive or for word-sized signed integers. Usually accessed via the `^^^` operator.
Each bit of the resulting integer is set if exactly one of the corresponding bits of the input integers is set, according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.xor "Permalink")def
```


UInt8.xor (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt8.xor (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Bitwise exclusive or for 8-bit unsigned integers. Usually accessed via the `^^^` operator.
Each bit of the resulting integer is set if exactly one of the corresponding bits of both input integers are set.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.xor "Permalink")def
```


Int8.xor (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.xor (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Bitwise exclusive or for 8-bit signed integers. Usually accessed via the `^^^` operator.
Each bit of the resulting integer is set if exactly one of the corresponding bits of the input integers is set, according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.xor "Permalink")def
```


UInt16.xor (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt16.xor (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Bitwise exclusive or for 16-bit unsigned integers. Usually accessed via the `^^^` operator.
Each bit of the resulting integer is set if exactly one of the corresponding bits of both input integers are set.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.xor "Permalink")def
```


Int16.xor (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.xor (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Bitwise exclusive or for 16-bit signed integers. Usually accessed via the `^^^` operator.
Each bit of the resulting integer is set if exactly one of the corresponding bits of the input integers is set, according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.xor "Permalink")def
```


UInt32.xor (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt32.xor (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Bitwise exclusive or for 32-bit unsigned integers. Usually accessed via the `^^^` operator.
Each bit of the resulting integer is set if exactly one of the corresponding bits of both input integers are set.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.xor "Permalink")def
```


Int32.xor (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.xor (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Bitwise exclusive or for 32-bit signed integers. Usually accessed via the `^^^` operator.
Each bit of the resulting integer is set if exactly one of the corresponding bits of the input integers is set, according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.xor "Permalink")def
```


UInt64.xor (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt64.xor (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Bitwise exclusive or for 64-bit unsigned integers. Usually accessed via the `^^^` operator.
Each bit of the resulting integer is set if exactly one of the corresponding bits of both input integers are set.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.xor "Permalink")def
```


Int64.xor (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.xor (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Bitwise exclusive or for 64-bit signed integers. Usually accessed via the `^^^` operator.
Each bit of the resulting integer is set if exactly one of the corresponding bits of the input integers is set, according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.complement "Permalink")def
```


USize.complement (a : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


USize.complement (a : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Bitwise complement, also known as bitwise negation, for word-sized unsigned integers. Usually accessed via the `~~~` prefix operator.
Each bit of the resulting integer is the opposite of the corresponding bit of the input integer.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.complement "Permalink")def
```


ISize.complement (a : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.complement (a : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Bitwise complement, also known as bitwise negation, for word-sized signed integers. Usually accessed via the `~~~` prefix operator.
Each bit of the resulting integer is the opposite of the corresponding bit of the input integer. Integers use the two's complement representation, so `[ISize.complement](Basic-Types/Fixed-Precision-Integers/#ISize___complement "Documentation for ISize.complement") a = -(a + 1)`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.complement "Permalink")def
```


UInt8.complement (a : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt8.complement (a : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Bitwise complement, also known as bitwise negation, for 8-bit unsigned integers. Usually accessed via the `~~~` prefix operator.
Each bit of the resulting integer is the opposite of the corresponding bit of the input integer.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.complement "Permalink")def
```


Int8.complement (a : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.complement (a : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Bitwise complement, also known as bitwise negation, for 8-bit signed integers. Usually accessed via the `~~~` prefix operator.
Each bit of the resulting integer is the opposite of the corresponding bit of the input integer. Integers use the two's complement representation, so `[Int8.complement](Basic-Types/Fixed-Precision-Integers/#Int8___complement "Documentation for Int8.complement") a = -(a + 1)`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.complement "Permalink")def
```


UInt16.complement (a : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt16.complement (a : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Bitwise complement, also known as bitwise negation, for 16-bit unsigned integers. Usually accessed via the `~~~` prefix operator.
Each bit of the resulting integer is the opposite of the corresponding bit of the input integer.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.complement "Permalink")def
```


Int16.complement (a : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.complement (a : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Bitwise complement, also known as bitwise negation, for 16-bit signed integers. Usually accessed via the `~~~` prefix operator.
Each bit of the resulting integer is the opposite of the corresponding bit of the input integer. Integers use the two's complement representation, so `[Int16.complement](Basic-Types/Fixed-Precision-Integers/#Int16___complement "Documentation for Int16.complement") a = -(a + 1)`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.complement "Permalink")def
```


UInt32.complement (a : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt32.complement (a : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Bitwise complement, also known as bitwise negation, for 32-bit unsigned integers. Usually accessed via the `~~~` prefix operator.
Each bit of the resulting integer is the opposite of the corresponding bit of the input integer.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.complement "Permalink")def
```


Int32.complement (a : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.complement (a : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Bitwise complement, also known as bitwise negation, for 32-bit signed integers. Usually accessed via the `~~~` prefix operator.
Each bit of the resulting integer is the opposite of the corresponding bit of the input integer. Integers use the two's complement representation, so `[Int32.complement](Basic-Types/Fixed-Precision-Integers/#Int32___complement "Documentation for Int32.complement") a = -(a + 1)`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.complement "Permalink")def
```


UInt64.complement (a : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt64.complement (a : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Bitwise complement, also known as bitwise negation, for 64-bit unsigned integers. Usually accessed via the `~~~` prefix operator.
Each bit of the resulting integer is the opposite of the corresponding bit of the input integer.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.complement "Permalink")def
```


Int64.complement (a : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.complement (a : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Bitwise complement, also known as bitwise negation, for 64-bit signed integers. Usually accessed via the `~~~` prefix operator.
Each bit of the resulting integer is the opposite of the corresponding bit of the input integer. Integers use the two's complement representation, so `[Int64.complement](Basic-Types/Fixed-Precision-Integers/#Int64___complement "Documentation for Int64.complement") a = -(a + 1)`.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.shiftLeft "Permalink")def
```


USize.shiftLeft (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


USize.shiftLeft (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Bitwise left shift for word-sized unsigned integers. Usually accessed via the `<<<` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.shiftLeft "Permalink")def
```


ISize.shiftLeft (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.shiftLeft (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Bitwise left shift for word-sized signed integers. Usually accessed via the `<<<` operator.
Signed integers are interpreted as bitvectors according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.shiftLeft "Permalink")def
```


UInt8.shiftLeft (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt8.shiftLeft (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Bitwise left shift for 8-bit unsigned integers. Usually accessed via the `<<<` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.shiftLeft "Permalink")def
```


Int8.shiftLeft (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.shiftLeft (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Bitwise left shift for 8-bit signed integers. Usually accessed via the `<<<` operator.
Signed integers are interpreted as bitvectors according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.shiftLeft "Permalink")def
```


UInt16.shiftLeft (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt16.shiftLeft (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Bitwise left shift for 16-bit unsigned integers. Usually accessed via the `<<<` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.shiftLeft "Permalink")def
```


Int16.shiftLeft (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.shiftLeft (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Bitwise left shift for 16-bit signed integers. Usually accessed via the `<<<` operator.
Signed integers are interpreted as bitvectors according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.shiftLeft "Permalink")def
```


UInt32.shiftLeft (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt32.shiftLeft (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Bitwise left shift for 32-bit unsigned integers. Usually accessed via the `<<<` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.shiftLeft "Permalink")def
```


Int32.shiftLeft (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.shiftLeft (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Bitwise left shift for 32-bit signed integers. Usually accessed via the `<<<` operator.
Signed integers are interpreted as bitvectors according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.shiftLeft "Permalink")def
```


UInt64.shiftLeft (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt64.shiftLeft (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Bitwise left shift for 64-bit unsigned integers. Usually accessed via the `<<<` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.shiftLeft "Permalink")def
```


Int64.shiftLeft (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.shiftLeft (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Bitwise left shift for 64-bit signed integers. Usually accessed via the `<<<` operator.
Signed integers are interpreted as bitvectors according to the two's complement representation.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=USize.shiftRight "Permalink")def
```


USize.shiftRight (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


USize.shiftRight (a b : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Bitwise right shift for word-sized unsigned integers. Usually accessed via the `>>>` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ISize.shiftRight "Permalink")def
```


ISize.shiftRight (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


ISize.shiftRight (a b : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Arithmetic right shift for word-sized signed integers. Usually accessed via the `<<<` operator.
The high bits are filled with the value of the most significant bit.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt8.shiftRight "Permalink")def
```


UInt8.shiftRight (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


UInt8.shiftRight (a b : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Bitwise right shift for 8-bit unsigned integers. Usually accessed via the `>>>` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int8.shiftRight "Permalink")def
```


Int8.shiftRight (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int8.shiftRight (a b : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Arithmetic right shift for 8-bit signed integers. Usually accessed via the `<<<` operator.
The high bits are filled with the value of the most significant bit.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt16.shiftRight "Permalink")def
```


UInt16.shiftRight (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


UInt16.shiftRight (a b : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Bitwise right shift for 16-bit unsigned integers. Usually accessed via the `>>>` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int16.shiftRight "Permalink")def
```


Int16.shiftRight (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int16.shiftRight (a b : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Arithmetic right shift for 16-bit signed integers. Usually accessed via the `<<<` operator.
The high bits are filled with the value of the most significant bit.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt32.shiftRight "Permalink")def
```


UInt32.shiftRight (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


UInt32.shiftRight (a b : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Bitwise right shift for 32-bit unsigned integers. Usually accessed via the `>>>` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int32.shiftRight "Permalink")def
```


Int32.shiftRight (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int32.shiftRight (a b : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Arithmetic right shift for 32-bit signed integers. Usually accessed via the `<<<` operator.
The high bits are filled with the value of the most significant bit.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=UInt64.shiftRight "Permalink")def
```


UInt64.shiftRight (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


UInt64.shiftRight (a b : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Bitwise right shift for 64-bit unsigned integers. Usually accessed via the `>>>` operator.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int64.shiftRight "Permalink")def
```


Int64.shiftRight (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int64.shiftRight (a b : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Arithmetic right shift for 64-bit signed integers. Usually accessed via the `<<<` operator.
The high bits are filled with the value of the most significant bit.
This function is overridden at runtime with an efficient implementation.
[←20.3. Finite Natural Numbers](Basic-Types/Finite-Natural-Numbers/#Fin "20.3. Finite Natural Numbers")[20.5. Bitvectors→](Basic-Types/Bitvectors/#BitVec "20.5. Bitvectors")

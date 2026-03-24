[←20.1. Natural Numbers](Basic-Types/Natural-Numbers/#Nat "20.1. Natural Numbers")[20.3. Finite Natural Numbers→](Basic-Types/Finite-Natural-Numbers/#Fin "20.3. Finite Natural Numbers")
#  20.2. Integers[🔗](find/?domain=Verso.Genre.Manual.section&name=Int "Permalink")
The integers are whole numbers, both positive and negative. Integers are arbitrary-precision, limited only by the capability of the hardware on which Lean is running; for fixed-width integers that are used in programming and computer science, please see the [section on fixed-precision integers](Basic-Types/Fixed-Precision-Integers/#fixed-ints).
Integers are specially supported by Lean's implementation. The logical model of the integers is based on the natural numbers: each integer is modeled as either a natural number or the negative successor of a natural number. Operations on the integers are specified using this model, which is used in the kernel and in interpreted code. In these contexts, integer code inherits the performance benefits of the natural numbers' special support. In compiled code, integers are represented as efficient arbitrary-precision integers, and sufficiently small numbers are stored as values that don't require indirection through a pointer. Arithmetic operations are implemented by primitives that take advantage of the efficient representations.
##  20.2.1. Logical Model[🔗](find/?domain=Verso.Genre.Manual.section&name=int-model "Permalink")
Integers are represented either as a natural number or as the negation of the successor of a natural number.
[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=%E2%84%A4%E2%86%AAInt "Permalink")inductive type
```


Int : Type


Int : Type


```

The integers.
This type is special-cased by the compiler and overridden with an efficient implementation. The runtime has a special representation for `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` that stores “small” signed numbers directly, while larger numbers use a fast arbitrary-precision arithmetic library (usually [GMP](https://gmplib.org/)). A “small number” is an integer that can be encoded with one fewer bits than the platform's pointer size (i.e. 63 bits on 64-bit architectures and 31 bits on 32-bit architectures).
#  Constructors

```
ofNat : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")
```

A natural number is an integer.
This constructor covers the non-negative integers (from `0` to `∞`).

```
negSucc : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")
```

The negation of the successor of a natural number is an integer.
This constructor covers the negative integers (from `-1` to `-∞`).
This representation of the integers has a number of useful properties. It is relatively simple to use and to understand. Unlike a pair of a sign and a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, there is a unique representation for `000`, which simplifies reasoning about equality. Integers can also be represented as a pair of natural numbers in which one is subtracted from the other, but this requires a [quotient type](The-Type-System/Quotients/#quotients) to be well-behaved, and quotient types can be laborious to work with due to the need to prove that functions respect the equivalence relation.
##  20.2.2. Run-Time Representation[🔗](find/?domain=Verso.Genre.Manual.section&name=int-runtime "Permalink")
Like [natural numbers](Basic-Types/Natural-Numbers/#nat-runtime), sufficiently-small integers are represented without pointers: the lowest-order bit in an object pointer is used to indicate that the value is not, in fact, a pointer. If an integer is too large to fit in the remaining bits, it is instead allocated as an ordinary Lean object that consists of an object header and an arbitrary-precision integer.
##  20.2.3. Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=int-syntax "Permalink")
The `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` instance allows numerals to be used as literals, both in expression and in pattern contexts. `([OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") n : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int"))` reduces to the constructor application `[Int.ofNat](Basic-Types/Integers/#Int___ofNat "Documentation for Int.ofNat") n`. The `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` instance allows negation to be used as well.
On top of these instances, there is special syntax for the constructor `[Int.negSucc](Basic-Types/Integers/#Int___ofNat "Documentation for Int.negSucc")` that is available when the `Int` namespace is opened. The notation `-[ n +1]` is suggestive of `−(n+1)-(n + 1)−(n+1)`, which is the meaning of `[Int.negSucc](Basic-Types/Integers/#Int___ofNat "Documentation for Int.negSucc") n`.
syntaxNegative Successor
`-[ n +1]` is notation for `[Int.negSucc](Basic-Types/Integers/#Int___ofNat "Documentation for Int.negSucc") n`.

```
term ::= ...
    | 


-[n+1] is suggestive notation for negSucc n, which is the second constructor of
Int for making strictly negative numbers by mapping n : Nat to -(n + 1).


-[ term +1]
```

##  20.2.4. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Integers--API-Reference "Permalink")
###  20.2.4.1. Properties[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Integers--API-Reference--Properties "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.sign "Permalink")def
```


Int.sign : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int.sign : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Returns the “sign” of the integer as another integer:
  * `1` for positive numbers,
  * `-1` for negative numbers, and
  * `0` for `0`.


Examples:
  * `[Int.sign](Basic-Types/Integers/#Int___sign "Documentation for Int.sign") 34 = 1`
  * `[Int.sign](Basic-Types/Integers/#Int___sign "Documentation for Int.sign") 2 = 1`
  * `[Int.sign](Basic-Types/Integers/#Int___sign "Documentation for Int.sign") 0 = 0`
  * `[Int.sign](Basic-Types/Integers/#Int___sign "Documentation for Int.sign") -1 = -1`
  * `[Int.sign](Basic-Types/Integers/#Int___sign "Documentation for Int.sign") -362 = -1`


###  20.2.4.2. Conversions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Integers--API-Reference--Conversions "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.natAbs "Permalink")def
```


Int.natAbs (m : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Int.natAbs (m : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The absolute value of an integer is its distance from `0`.
This function is overridden by the compiler with an efficient implementation. This definition is the logical model.
Examples:
  * `(7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[natAbs](Basic-Types/Integers/#Int___natAbs "Documentation for Int.natAbs") = 7`
  * `(0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[natAbs](Basic-Types/Integers/#Int___natAbs "Documentation for Int.natAbs") = 0`
  * `(-11 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[natAbs](Basic-Types/Integers/#Int___natAbs "Documentation for Int.natAbs") = 11`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.toNat "Permalink")def
```


Int.toNat : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Int.toNat : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Converts an integer into a natural number. Negative numbers are converted to `0`.
Examples:
  * `(7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[toNat](Basic-Types/Integers/#Int___toNat "Documentation for Int.toNat") = 7`
  * `(0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[toNat](Basic-Types/Integers/#Int___toNat "Documentation for Int.toNat") = 0`
  * `(-7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[toNat](Basic-Types/Integers/#Int___toNat "Documentation for Int.toNat") = 0`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.toNat? "Permalink")def
```


Int.toNat? : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Int.toNat? : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Converts an integer into a natural number. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` for negative numbers.
Examples:
  * `(7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[toNat?](Basic-Types/Integers/#Int___toNat___ "Documentation for Int.toNat?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 7`
  * `(0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[toNat?](Basic-Types/Integers/#Int___toNat___ "Documentation for Int.toNat?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 0`
  * `(-7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[toNat?](Basic-Types/Integers/#Int___toNat___ "Documentation for Int.toNat?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.toISize "Permalink")def
```


Int.toISize (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


Int.toISize (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Converts an arbitrary-precision integer to a word-sized signed integer, wrapping around on over- or underflow.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.toInt8 "Permalink")def
```


Int.toInt8 (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Int.toInt8 (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Converts an arbitrary-precision integer to an 8-bit integer, wrapping on overflow or underflow.
Examples:
  * `[Int.toInt8](Basic-Types/Integers/#Int___toInt8 "Documentation for Int.toInt8") 48 = 48`
  * `[Int.toInt8](Basic-Types/Integers/#Int___toInt8 "Documentation for Int.toInt8") (-115) = -115`
  * `[Int.toInt8](Basic-Types/Integers/#Int___toInt8 "Documentation for Int.toInt8") (-129) = 127`
  * `[Int.toInt8](Basic-Types/Integers/#Int___toInt8 "Documentation for Int.toInt8") (128) = -128`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.toInt16 "Permalink")def
```


Int.toInt16 (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Int.toInt16 (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Converts an arbitrary-precision integer to a 16-bit integer, wrapping on overflow or underflow.
Examples:
  * `[Int.toInt16](Basic-Types/Integers/#Int___toInt16 "Documentation for Int.toInt16") 48 = 48`
  * `[Int.toInt16](Basic-Types/Integers/#Int___toInt16 "Documentation for Int.toInt16") (-129) = -129`
  * `[Int.toInt16](Basic-Types/Integers/#Int___toInt16 "Documentation for Int.toInt16") (128) = 128`
  * `[Int.toInt16](Basic-Types/Integers/#Int___toInt16 "Documentation for Int.toInt16") 70000 = 4464`
  * `[Int.toInt16](Basic-Types/Integers/#Int___toInt16 "Documentation for Int.toInt16") (-40000) = 25536`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.toInt32 "Permalink")def
```


Int.toInt32 (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Int.toInt32 (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Converts an arbitrary-precision integer to a 32-bit integer, wrapping on overflow or underflow.
Examples:
  * `[Int.toInt32](Basic-Types/Integers/#Int___toInt32 "Documentation for Int.toInt32") 48 = 48`
  * `[Int.toInt32](Basic-Types/Integers/#Int___toInt32 "Documentation for Int.toInt32") (-129) = -129`
  * `[Int.toInt32](Basic-Types/Integers/#Int___toInt32 "Documentation for Int.toInt32") 70000 = 70000`
  * `[Int.toInt32](Basic-Types/Integers/#Int___toInt32 "Documentation for Int.toInt32") (-40000) = -40000`
  * `[Int.toInt32](Basic-Types/Integers/#Int___toInt32 "Documentation for Int.toInt32") 2147483648 = -2147483648`
  * `[Int.toInt32](Basic-Types/Integers/#Int___toInt32 "Documentation for Int.toInt32") (-2147483649) = 2147483647`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.toInt64 "Permalink")def
```


Int.toInt64 (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Int.toInt64 (i : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Converts an arbitrary-precision integer to a 64-bit integer, wrapping on overflow or underflow.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Int.toInt64](Basic-Types/Integers/#Int___toInt64 "Documentation for Int.toInt64") 48 = 48`
  * `[Int.toInt64](Basic-Types/Integers/#Int___toInt64 "Documentation for Int.toInt64") (-40_000) = -40_000`
  * `[Int.toInt64](Basic-Types/Integers/#Int___toInt64 "Documentation for Int.toInt64") 2_147_483_648 = 2_147_483_648`
  * `[Int.toInt64](Basic-Types/Integers/#Int___toInt64 "Documentation for Int.toInt64") (-2_147_483_649) = -2_147_483_649`
  * `[Int.toInt64](Basic-Types/Integers/#Int___toInt64 "Documentation for Int.toInt64") 9_223_372_036_854_775_808 = -9_223_372_036_854_775_808`
  * `[Int.toInt64](Basic-Types/Integers/#Int___toInt64 "Documentation for Int.toInt64") (-9_223_372_036_854_775_809) = 9_223_372_036_854_775_807`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.repr "Permalink")def
```


Int.repr : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


Int.repr : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Returns the decimal string representation of an integer.
###  20.2.4.3. Arithmetic[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Integers--API-Reference--Arithmetic "Permalink")
Typically, arithmetic operations on integers are accessed using Lean's overloaded arithmetic notation. In particular, the instances of `[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`, `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`, `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`, and `[Mul](Type-Classes/Basic-Classes/#Mul___mk "Documentation for Mul") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` allow ordinary infix operators to be used. [Division](Basic-Types/Integers/#int-div) is somewhat more intricate, because there are multiple sensible notions of division on integers.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.add "Permalink")def
```


Int.add (m n : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int.add (m n : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Addition of integers, usually accessed via the `+` operator.
This function is overridden by the compiler with an efficient implementation. This definition is the logical model.
Examples:
  * `(7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) + (6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 13`
  * `(6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) + (-6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.sub "Permalink")def
```


Int.sub (m n : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int.sub (m n : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Subtraction of integers, usually accessed via the `-` operator.
This function is overridden by the compiler with an efficient implementation. This definition is the logical model.
Examples:
  * `(63 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) - (6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 57`
  * `(7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) - (0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 7`
  * `(0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) - (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -7`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.subNatNat "Permalink")def
```


Int.subNatNat (m n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int.subNatNat (m n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Non-truncating subtraction of two natural numbers.
Examples:
  * `[Int.subNatNat](Basic-Types/Integers/#Int___subNatNat "Documentation for Int.subNatNat") 5 2 = 3`
  * `[Int.subNatNat](Basic-Types/Integers/#Int___subNatNat "Documentation for Int.subNatNat") 2 5 = -3`
  * `[Int.subNatNat](Basic-Types/Integers/#Int___subNatNat "Documentation for Int.subNatNat") 0 13 = -13`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.neg "Permalink")def
```


Int.neg (n : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int.neg (n : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Negation of integers, usually accessed via the `-` prefix operator.
This function is overridden by the compiler with an efficient implementation. This definition is the logical model.
Examples:
  * `-(6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -6`
  * `-(-6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 6`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[neg](Basic-Types/Integers/#Int___neg "Documentation for Int.neg") = -12`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.negOfNat "Permalink")def
```


Int.negOfNat : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int.negOfNat : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Negation of natural numbers.
Examples:
  * `[Int.negOfNat](Basic-Types/Integers/#Int___negOfNat "Documentation for Int.negOfNat") 6 = -6`
  * `[Int.negOfNat](Basic-Types/Integers/#Int___negOfNat "Documentation for Int.negOfNat") 0 = 0`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.mul "Permalink")def
```


Int.mul (m n : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int.mul (m n : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Multiplication of integers, usually accessed via the `*` operator.
This function is overridden by the compiler with an efficient implementation. This definition is the logical model.
Examples:
  * `(63 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) * (6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 378`
  * `(6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) * (-6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -36`
  * `(7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) * (0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.pow "Permalink")def
```


Int.pow : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int.pow : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Power of an integer to a natural number, usually accessed via the `^` operator.
Examples:
  * `(2 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) ^ 4 = 16`
  * `(10 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) ^ 0 = 1`
  * `(0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) ^ 10 = 0`
  * `(-7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) ^ 3 = -343`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.gcd "Permalink")def
```


Int.gcd (m n : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Int.gcd (m n : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Computes the greatest common divisor of two integers as a natural number. The GCD of two integers is the largest natural number that evenly divides both. However, the GCD of a number and `0` is the number's absolute value.
This implementation uses `[Nat.gcd](Basic-Types/Natural-Numbers/#Nat___gcd "Documentation for Nat.gcd")`, which is overridden in both the kernel and the compiler to efficiently evaluate using arbitrary-precision arithmetic.
Examples:
  * `[Int.gcd](Basic-Types/Integers/#Int___gcd "Documentation for Int.gcd") 10 15 = 5`
  * `[Int.gcd](Basic-Types/Integers/#Int___gcd "Documentation for Int.gcd") 10 (-15) = 5`
  * `[Int.gcd](Basic-Types/Integers/#Int___gcd "Documentation for Int.gcd") (-6) (-9) = 3`
  * `[Int.gcd](Basic-Types/Integers/#Int___gcd "Documentation for Int.gcd") 0 5 = 5`
  * `[Int.gcd](Basic-Types/Integers/#Int___gcd "Documentation for Int.gcd") (-7) 0 = 7`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.lcm "Permalink")def
```


Int.lcm (m n : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Int.lcm (m n : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Computes the least common multiple of two integers as a natural number. The LCM of two integers is the smallest natural number that's evenly divisible by the absolute values of both.
Examples:
  * `[Int.lcm](Basic-Types/Integers/#Int___lcm "Documentation for Int.lcm") 9 6 = 18`
  * `[Int.lcm](Basic-Types/Integers/#Int___lcm "Documentation for Int.lcm") 9 (-6) = 18`
  * `[Int.lcm](Basic-Types/Integers/#Int___lcm "Documentation for Int.lcm") 9 3 = 9`
  * `[Int.lcm](Basic-Types/Integers/#Int___lcm "Documentation for Int.lcm") 9 (-3) = 9`
  * `[Int.lcm](Basic-Types/Integers/#Int___lcm "Documentation for Int.lcm") 0 3 = 0`
  * `[Int.lcm](Basic-Types/Integers/#Int___lcm "Documentation for Int.lcm") (-3) 0 = 0`


####  20.2.4.3.1. Division[🔗](find/?domain=Verso.Genre.Manual.section&name=int-div "Permalink")
The `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` and `[Mod](Type-Classes/Basic-Classes/#Mod___mk "Documentation for Mod") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` instances implement Euclidean division, described in the reference for `[Int.ediv](Basic-Types/Integers/#Int___ediv "Documentation for Int.ediv")`. This is not, however, the only sensible convention for rounding and remainders in division. Four pairs of division and modulus functions are available, implementing various conventions.
Division by 0
In all integer division conventions, division by `0` is defined to be `0`:
``0`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Int.ediv](Basic-Types/Integers/#Int___ediv "Documentation for Int.ediv") 5 0 `0`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Int.ediv](Basic-Types/Integers/#Int___ediv "Documentation for Int.ediv") 0 0 `0`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Int.ediv](Basic-Types/Integers/#Int___ediv "Documentation for Int.ediv") (-5) 0 `0`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Int.bdiv](Basic-Types/Integers/#Int___bdiv "Documentation for Int.bdiv") 5 0 `0`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Int.bdiv](Basic-Types/Integers/#Int___bdiv "Documentation for Int.bdiv") 0 0 `0`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Int.bdiv](Basic-Types/Integers/#Int___bdiv "Documentation for Int.bdiv") (-5) 0 `0`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Int.fdiv](Basic-Types/Integers/#Int___fdiv "Documentation for Int.fdiv") 5 0 `0`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Int.fdiv](Basic-Types/Integers/#Int___fdiv "Documentation for Int.fdiv") 0 0 `0`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Int.fdiv](Basic-Types/Integers/#Int___fdiv "Documentation for Int.fdiv") (-5) 0 `0`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Int.tdiv](Basic-Types/Integers/#Int___tdiv "Documentation for Int.tdiv") 5 0 `0`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Int.tdiv](Basic-Types/Integers/#Int___tdiv "Documentation for Int.tdiv") 0 0 `0`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Int.tdiv](Basic-Types/Integers/#Int___tdiv "Documentation for Int.tdiv") (-5) 0 `
All evaluate to 0.

```
0
```

[Live ↪](javascript:openLiveLink\("MQUwbghgNgBAkgOwC4DoQBMCWYYFYYAMAUKJLIqhtoYSeNPMmljgBQC0uAlLaQxSgBGLPL3rkmw6gTFlGqKW049ifCagBmI/KvHyUW6bP5NDS7sfUok2y/ptHdcgQ/MqgA"\))
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.ediv "Permalink")def
```


Int.ediv : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int.ediv : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Integer division that uses the E-rounding convention. Usually accessed via the `/` operator. Division by zero is defined to be zero, rather than an error.
In the E-rounding convention (Euclidean division), `[Int.emod](Basic-Types/Integers/#Int___emod "Documentation for Int.emod") x y` satisfies `0 ≤ Int.emod x y < Int.natAbs y` for `y ≠ 0` and `[Int.ediv](Basic-Types/Integers/#Int___ediv "Documentation for Int.ediv")` is the unique function satisfying `[Int.emod](Basic-Types/Integers/#Int___emod "Documentation for Int.emod") x y + ([Int.ediv](Basic-Types/Integers/#Int___ediv "Documentation for Int.ediv") x y) * y = x` for `y ≠ 0`.
This means that `[Int.ediv](Basic-Types/Integers/#Int___ediv "Documentation for Int.ediv") x y` is `⌊x / y⌋` when `y > 0` and `⌈x / y⌉` when `y < 0`.
This function is overridden by the compiler with an efficient implementation. This definition is the logical model.
Examples:
  * `(7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) / (0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) / (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) / (6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 2`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) / (-6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -2`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) / (6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -2`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) / (-6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 2`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) / (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 1`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) / (-7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -1`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) / (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -2`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) / (-7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 2`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.emod "Permalink")def
```


Int.emod : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int.emod : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Integer modulus that uses the E-rounding convention. Usually accessed via the `%` operator.
In the E-rounding convention (Euclidean division), `[Int.emod](Basic-Types/Integers/#Int___emod "Documentation for Int.emod") x y` satisfies `0 ≤ Int.emod x y < Int.natAbs y` for `y ≠ 0` and `[Int.ediv](Basic-Types/Integers/#Int___ediv "Documentation for Int.ediv")` is the unique function satisfying `[Int.emod](Basic-Types/Integers/#Int___emod "Documentation for Int.emod") x y + ([Int.ediv](Basic-Types/Integers/#Int___ediv "Documentation for Int.ediv") x y) * y = x` for `y ≠ 0`.
This function is overridden by the compiler with an efficient implementation. This definition is the logical model.
Examples:
  * `(7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) % (0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 7`
  * `(0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) % (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) % (6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) % (-6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) % (6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) % (-6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) % (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 5`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) % (-7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 5`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) % (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 2`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) % (-7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 2`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.tdiv "Permalink")def
```


Int.tdiv : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int.tdiv : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Integer division using the T-rounding convention.
In [the T-rounding convention](https://dl.acm.org/doi/pdf/10.1145/128861.128862) (division with truncation), all rounding is towards zero. Division by 0 is defined to be 0. In this convention, `[Int.tmod](Basic-Types/Integers/#Int___tmod "Documentation for Int.tmod") a b + b * ([Int.tdiv](Basic-Types/Integers/#Int___tdiv "Documentation for Int.tdiv") a b) = a`.
This function is overridden by the compiler with an efficient implementation. This definition is the logical model.
Examples:
  * `(7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tdiv](Basic-Types/Integers/#Int___tdiv "Documentation for Int.tdiv") (0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tdiv](Basic-Types/Integers/#Int___tdiv "Documentation for Int.tdiv") (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tdiv](Basic-Types/Integers/#Int___tdiv "Documentation for Int.tdiv") (6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 2`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tdiv](Basic-Types/Integers/#Int___tdiv "Documentation for Int.tdiv") (-6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -2`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tdiv](Basic-Types/Integers/#Int___tdiv "Documentation for Int.tdiv") (6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -2`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tdiv](Basic-Types/Integers/#Int___tdiv "Documentation for Int.tdiv") (-6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 2`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tdiv](Basic-Types/Integers/#Int___tdiv "Documentation for Int.tdiv") (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 1`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tdiv](Basic-Types/Integers/#Int___tdiv "Documentation for Int.tdiv") (-7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -1`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tdiv](Basic-Types/Integers/#Int___tdiv "Documentation for Int.tdiv") (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -1`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tdiv](Basic-Types/Integers/#Int___tdiv "Documentation for Int.tdiv") (-7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 1`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.tmod "Permalink")def
```


Int.tmod : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int.tmod : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Integer modulo using the T-rounding convention.
In [the T-rounding convention](https://dl.acm.org/doi/pdf/10.1145/128861.128862) (division with truncation), all rounding is towards zero. Division by 0 is defined to be 0 and `[Int.tmod](Basic-Types/Integers/#Int___tmod "Documentation for Int.tmod") a 0 = a`.
In this convention, `[Int.tmod](Basic-Types/Integers/#Int___tmod "Documentation for Int.tmod") a b + b * ([Int.tdiv](Basic-Types/Integers/#Int___tdiv "Documentation for Int.tdiv") a b) = a`. Additionally, `[Int.natAbs](Basic-Types/Integers/#Int___natAbs "Documentation for Int.natAbs") ([Int.tmod](Basic-Types/Integers/#Int___tmod "Documentation for Int.tmod") a b) = [Int.natAbs](Basic-Types/Integers/#Int___natAbs "Documentation for Int.natAbs") a % [Int.natAbs](Basic-Types/Integers/#Int___natAbs "Documentation for Int.natAbs") b`, and when `b` does not divide `a`, `[Int.tmod](Basic-Types/Integers/#Int___tmod "Documentation for Int.tmod") a b` has the same sign as `a`.
This function is overridden by the compiler with an efficient implementation. This definition is the logical model.
Examples:
  * `(7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tmod](Basic-Types/Integers/#Int___tmod "Documentation for Int.tmod") (0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 7`
  * `(0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tmod](Basic-Types/Integers/#Int___tmod "Documentation for Int.tmod") (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tmod](Basic-Types/Integers/#Int___tmod "Documentation for Int.tmod") (6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tmod](Basic-Types/Integers/#Int___tmod "Documentation for Int.tmod") (-6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tmod](Basic-Types/Integers/#Int___tmod "Documentation for Int.tmod") (6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tmod](Basic-Types/Integers/#Int___tmod "Documentation for Int.tmod") (-6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tmod](Basic-Types/Integers/#Int___tmod "Documentation for Int.tmod") (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 5`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tmod](Basic-Types/Integers/#Int___tmod "Documentation for Int.tmod") (-7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 5`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tmod](Basic-Types/Integers/#Int___tmod "Documentation for Int.tmod") (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -5`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[tmod](Basic-Types/Integers/#Int___tmod "Documentation for Int.tmod") (-7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -5`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.bdiv "Permalink")def
```


Int.bdiv (x : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int.bdiv (x : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Balanced division.
This returns the unique integer so that `b * ([Int.bdiv](Basic-Types/Integers/#Int___bdiv "Documentation for Int.bdiv") a b) + [Int.bmod](Basic-Types/Integers/#Int___bmod "Documentation for Int.bmod") a b = a`.
Examples:
  * `(7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bdiv](Basic-Types/Integers/#Int___bdiv "Documentation for Int.bdiv") 0 = 0`
  * `(0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bdiv](Basic-Types/Integers/#Int___bdiv "Documentation for Int.bdiv") 7 = 0`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bdiv](Basic-Types/Integers/#Int___bdiv "Documentation for Int.bdiv") 6 = 2`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bdiv](Basic-Types/Integers/#Int___bdiv "Documentation for Int.bdiv") 7 = 2`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bdiv](Basic-Types/Integers/#Int___bdiv "Documentation for Int.bdiv") 8 = 2`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bdiv](Basic-Types/Integers/#Int___bdiv "Documentation for Int.bdiv") 9 = 1`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bdiv](Basic-Types/Integers/#Int___bdiv "Documentation for Int.bdiv") 6 = -2`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bdiv](Basic-Types/Integers/#Int___bdiv "Documentation for Int.bdiv") 7 = -2`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bdiv](Basic-Types/Integers/#Int___bdiv "Documentation for Int.bdiv") 8 = -1`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bdiv](Basic-Types/Integers/#Int___bdiv "Documentation for Int.bdiv") 9 = -1`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.bmod "Permalink")def
```


Int.bmod (x : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int.bmod (x : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Balanced modulus.
This version of integer modulus uses the balanced rounding convention, which guarantees that `-m / 2 ≤ Int.bmod x m < m/2` for `m ≠ 0` and `[Int.bmod](Basic-Types/Integers/#Int___bmod "Documentation for Int.bmod") x m` is congruent to `x` modulo `m`.
If `m = 0`, then `[Int.bmod](Basic-Types/Integers/#Int___bmod "Documentation for Int.bmod") x m = x`.
Examples:
  * `(7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bmod](Basic-Types/Integers/#Int___bmod "Documentation for Int.bmod") 0 = 7`
  * `(0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bmod](Basic-Types/Integers/#Int___bmod "Documentation for Int.bmod") 7 = 0`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bmod](Basic-Types/Integers/#Int___bmod "Documentation for Int.bmod") 6 = 0`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bmod](Basic-Types/Integers/#Int___bmod "Documentation for Int.bmod") 7 = -2`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bmod](Basic-Types/Integers/#Int___bmod "Documentation for Int.bmod") 8 = -4`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bmod](Basic-Types/Integers/#Int___bmod "Documentation for Int.bmod") 9 = 3`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bmod](Basic-Types/Integers/#Int___bmod "Documentation for Int.bmod") 6 = 0`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bmod](Basic-Types/Integers/#Int___bmod "Documentation for Int.bmod") 7 = 2`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bmod](Basic-Types/Integers/#Int___bmod "Documentation for Int.bmod") 8 = -4`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bmod](Basic-Types/Integers/#Int___bmod "Documentation for Int.bmod") 9 = -3`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.fdiv "Permalink")def
```


Int.fdiv : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int.fdiv : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Integer division using the F-rounding convention.
In the F-rounding convention (flooring division), `[Int.fdiv](Basic-Types/Integers/#Int___fdiv "Documentation for Int.fdiv") x y` satisfies `Int.fdiv x y = ⌊x / y⌋` and `[Int.fmod](Basic-Types/Integers/#Int___fmod "Documentation for Int.fmod")` is the unique function satisfying `[Int.fmod](Basic-Types/Integers/#Int___fmod "Documentation for Int.fmod") x y + ([Int.fdiv](Basic-Types/Integers/#Int___fdiv "Documentation for Int.fdiv") x y) * y = x`.
Examples:
  * `(7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fdiv](Basic-Types/Integers/#Int___fdiv "Documentation for Int.fdiv") (0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fdiv](Basic-Types/Integers/#Int___fdiv "Documentation for Int.fdiv") (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fdiv](Basic-Types/Integers/#Int___fdiv "Documentation for Int.fdiv") (6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 2`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fdiv](Basic-Types/Integers/#Int___fdiv "Documentation for Int.fdiv") (-6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -2`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fdiv](Basic-Types/Integers/#Int___fdiv "Documentation for Int.fdiv") (6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -2`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fdiv](Basic-Types/Integers/#Int___fdiv "Documentation for Int.fdiv") (-6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 2`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fdiv](Basic-Types/Integers/#Int___fdiv "Documentation for Int.fdiv") (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 1`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fdiv](Basic-Types/Integers/#Int___fdiv "Documentation for Int.fdiv") (-7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -2`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fdiv](Basic-Types/Integers/#Int___fdiv "Documentation for Int.fdiv") (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -2`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fdiv](Basic-Types/Integers/#Int___fdiv "Documentation for Int.fdiv") (-7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 1`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.fmod "Permalink")def
```


Int.fmod : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int.fmod : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Integer modulus using the F-rounding convention.
In the F-rounding convention (flooring division), `[Int.fdiv](Basic-Types/Integers/#Int___fdiv "Documentation for Int.fdiv") x y` satisfies `Int.fdiv x y = ⌊x / y⌋` and `[Int.fmod](Basic-Types/Integers/#Int___fmod "Documentation for Int.fmod")` is the unique function satisfying `[Int.fmod](Basic-Types/Integers/#Int___fmod "Documentation for Int.fmod") x y + ([Int.fdiv](Basic-Types/Integers/#Int___fdiv "Documentation for Int.fdiv") x y) * y = x`.
Examples:
  * `(7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fmod](Basic-Types/Integers/#Int___fmod "Documentation for Int.fmod") (0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 7`
  * `(0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fmod](Basic-Types/Integers/#Int___fmod "Documentation for Int.fmod") (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fmod](Basic-Types/Integers/#Int___fmod "Documentation for Int.fmod") (6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fmod](Basic-Types/Integers/#Int___fmod "Documentation for Int.fmod") (-6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fmod](Basic-Types/Integers/#Int___fmod "Documentation for Int.fmod") (6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fmod](Basic-Types/Integers/#Int___fmod "Documentation for Int.fmod") (-6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fmod](Basic-Types/Integers/#Int___fmod "Documentation for Int.fmod") (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 5`
  * `(12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fmod](Basic-Types/Integers/#Int___fmod "Documentation for Int.fmod") (-7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -2`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fmod](Basic-Types/Integers/#Int___fmod "Documentation for Int.fmod") (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 2`
  * `(-12 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[fmod](Basic-Types/Integers/#Int___fmod "Documentation for Int.fmod") (-7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -5`


###  20.2.4.4. Bitwise Operators[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Integers--API-Reference--Bitwise-Operators "Permalink")
Bitwise operators on `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` can be understood as bitwise operators on an infinite stream of bits that are the twos-complement representation of integers.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.not "Permalink")def
```


Int.not : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int.not : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Bitwise not, usually accessed via the `~~~` prefix operator.
Interprets the integer as an infinite sequence of bits in two's complement and complements each bit.
Examples:
  * `~~~(0 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -1`
  * `~~~(1 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = -2`
  * `~~~(-1 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 0`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.shiftRight "Permalink")def
```


Int.shiftRight : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Int.shiftRight : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Bitwise right shift, usually accessed via the `>>>` operator.
Interprets the integer as an infinite sequence of bits in two's complement and shifts the value to the right.
Examples:
  * `( 0b0111 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) >>> 1 =  0b0011`
  * `( 0b1000 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) >>> 1 =  0b0100`
  * `(-0b1000 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) >>> 1 = -0b0100`
  * `(-0b0111 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) >>> 1 = -0b0100`


###  20.2.4.5. Comparisons[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Integers--API-Reference--Comparisons "Permalink")
Equality and inequality tests on `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` are typically performed using the decidability of its equality and ordering relations or using the `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` and `[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` instances.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.le "Permalink")def
```


Int.le (a b : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : Prop


Int.le (a b : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : Prop


```

Non-strict inequality of integers, usually accessed via the `≤` operator.
`a ≤ b` is defined as `b - a ≥ 0`, using `Int.NonNeg`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.lt "Permalink")def
```


Int.lt (a b : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : Prop


Int.lt (a b : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : Prop


```

Strict inequality of integers, usually accessed via the `<` operator.
`a < b` when `a + 1 ≤ b`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.decEq "Permalink")def
```


Int.decEq (a b : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


Int.decEq (a b : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


```

Decides whether two integers are equal. Usually accessed via the `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` instance.
This function is overridden by the compiler with an efficient implementation. This definition is the logical model.
Examples:
  * `show (7 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = (3 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) + (4 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`
  * `[if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = (3 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) * (2 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no" = "yes"`
  * `(¬ (6 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = (3 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int"))) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


[←20.1. Natural Numbers](Basic-Types/Natural-Numbers/#Nat "20.1. Natural Numbers")[20.3. Finite Natural Numbers→](Basic-Types/Finite-Natural-Numbers/#Fin "20.3. Finite Natural Numbers")

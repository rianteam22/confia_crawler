[←20. Basic Types](Basic-Types/#basic-types "20. Basic Types")[20.2. Integers→](Basic-Types/Integers/#Int "20.2. Integers")
#  20.1. Natural Numbers[🔗](find/?domain=Verso.Genre.Manual.section&name=Nat "Permalink")
The natural numbers are nonnegative integers. Logically, they are the numbers 0, 1, 2, 3, …, generated from the constructors `[Nat.zero](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.zero")` and `[Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")`. Lean imposes no upper bound on the representation of natural numbers other than physical constraints imposed by the available memory of the computer.
Because the natural numbers are fundamental to both mathematical reasoning and programming, they are specially supported by Lean's implementation. The logical model of the natural numbers is as an [inductive type](The-Type-System/Inductive-Types/#--tech-term-Inductive-types), and arithmetic operations are specified using this model. In Lean's kernel, the interpreter, and compiled code, closed natural numbers are represented as efficient arbitrary-precision integers. Sufficiently small numbers are values that don't require indirection through a pointer. Arithmetic operations are implemented by primitives that take advantage of the efficient representations.
##  20.1.1. Logical Model[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-model "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=%E2%84%95%E2%86%AANat "Permalink")inductive type
```


Nat : Type


Nat : Type


```

The natural numbers, starting at zero.
This type is special-cased by both the kernel and the compiler, and overridden with an efficient implementation. Both use a fast arbitrary-precision arithmetic library (usually [GMP](https://gmplib.org/)); at runtime, `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` values that are sufficiently small are unboxed.
#  Constructors

```
zero : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

Zero, the smallest natural number.
Using `[Nat.zero](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.zero")` explicitly should usually be avoided in favor of the literal `0`, which is the [simp normal form](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=simp-normal-forms).

```
succ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

The successor of a natural number `n`.
Using `[Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") n` should usually be avoided in favor of `n + 1`, which is the [simp normal form](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=simp-normal-forms).
Proofs by Induction
The natural numbers are an [inductive type](The-Type-System/Inductive-Types/#--tech-term-Inductive-types), so the `[induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic")` tactic can be used to prove universally-quantified statements. A proof by induction requires a base case and an induction step. The base case is a proof that the statement is true for `0`. The induction step is a proof that the truth of the statement for some arbitrary number `i` implies its truth for `i + 1`.
This proof uses the lemma `Nat.succ_lt_succ` in its induction step.
`example (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : n < n + 1 := byi:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1   [induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic") n with   | [zero](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.zero") =>zeroi:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1     [show](Tactic-Proofs/Tactic-Reference/#show "Documentation for tactic") 0 < 1zeroi:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 1     [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")All goals completed! 🐙   | [succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") i ih =>succi✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")i:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")ih:i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") i [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1⊢ i [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") i [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 -- ih : i < i + 1     [show](Tactic-Proofs/Tactic-Reference/#show "Documentation for tactic") i + 1 < i + 1 + 1succi✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")i:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")ih:i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") i [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1⊢ i [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") i [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1     [exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic") Nat.succ_lt_succ ihAll goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAKAdvAXPAcmALgSnXlQB4j4BqeARnQF54AjATwCh54BLZAEwFcBjHBwD2qVAHcOOABZt4AH3gAvYACdh8WgD457AM7Th4+AAZ4pKrvjdg/DjbmK9A/p07TNW+AFpv7whzmbpSW7PqGxoEhQVHUFNRWoGCCWLgAdM78/AD6MDjZma4c0kA"\))
###  20.1.1.1. Peano Axioms[🔗](find/?domain=Verso.Genre.Manual.section&name=peano-axioms "Permalink")
The Peano axioms are a consequence of this definition. The induction principle generated for `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` is the one demanded by the axiom of induction:
`Nat.rec.{u} {motive : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u}   (zero : motive [zero](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.zero"))   (succ : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → motive n → motive n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ"))   (t : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :   motive t`
This induction principle also implements primitive recursion. The injectivity of `[Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")` and the disjointness of `[Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")` and `Nat.zero` are consequences of the induction principle, using a construction typically called “no confusion”:
`def NoConfusion : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Prop   | 0, 0 => [True](Basic-Propositions/Truth/#True___intro "Documentation for True")   | 0, _ + 1 | _ + 1, 0 => [False](Basic-Propositions/Truth/#False "Documentation for False")   | n + 1, k + 1 => n = k  theorem noConfusionDiagonal (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :     [NoConfusion](Basic-Types/Natural-Numbers/#NoConfusion "Definition of example") n n :=   Nat.rec [True.intro](Basic-Propositions/Truth/#True___intro "Documentation for True.intro") (fun _ _ => [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")) n  theorem noConfusion (n k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (eq : n = k) :     [NoConfusion](Basic-Types/Natural-Numbers/#NoConfusion "Definition of example") n k :=   eq ▸ [noConfusionDiagonal](Basic-Types/Natural-Numbers/#noConfusionDiagonal "Definition of example") n  theorem succ_injective : n + 1 = k + 1 → n = k :=   [noConfusion](Basic-Types/Natural-Numbers/#noConfusion "Definition of example") (n + 1) (k + 1)  theorem succ_not_zero : ¬n + 1 = 0 :=   [noConfusion](Basic-Types/Natural-Numbers/#noConfusion "Definition of example") (n + 1) 0 `
##  20.1.2. Run-Time Representation[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-runtime "Permalink")
The representation suggested by the declaration of `Nat` would be horrendously inefficient, as it's essentially a linked list. The length of the list would be the number. With this representation, addition would take time linear in the size of one of the addends, and numbers would take at least as many machine words as their magnitude in memory. Thus, natural numbers have special support in both the kernel and the compiler that avoids this overhead.
In the kernel, there are special `Nat` literal values that use a widely-trusted, efficient arbitrary-precision integer library (usually [GMP](https://gmplib.org/)). Basic functions such as addition are overridden by primitives that use this representation. Because they are part of the kernel, if these primitives did not correspond to their definitions as Lean functions, it could undermine soundness.
In compiled code, sufficiently-small natural numbers are represented without pointer indirections: the lowest-order bit in an object pointer is used to indicate that the value is not, in fact, a pointer, and the remaining bits are used to store the number. 31 bits are available on 32-bits architectures for pointer-free `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`s, while 63 bits are available on 64-bit architectures. In other words, natural numbers smaller than `231=2,147,483,6482^{31} = 2,147,483,648231=2,147,483,648` or `263=9,223,372,036,854,775,8082^{63} = 9,223,372,036,854,775,808263=9,223,372,036,854,775,808` do not require allocations. If an natural number is too large for this representation, it is instead allocated as an ordinary Lean object that consists of an object header and an arbitrary-precision integer value.
###  20.1.2.1. Performance Notes[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-performance "Permalink")
Using Lean's built-in arithmetic operators, rather than redefining them, is essential. The logical model of `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` is essentially a linked list, so addition would take time linear in the size of one argument. Still worse, multiplication takes quadratic time in this model. While defining arithmetic from scratch can be a useful learning exercise, these redefined operations will not be nearly as fast.
##  20.1.3. Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-syntax "Permalink")
Natural number literals are overridden using the `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat")` type class, which is described in the [section on literal syntax](Terms/Numeric-Literals/#nat-literals).
##  20.1.4. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-api "Permalink")
###  20.1.4.1. Arithmetic[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-api-arithmetic "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.pred "Permalink")def
```


Nat.pred : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.pred : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The predecessor of a natural number is one less than it. The predecessor of `0` is defined to be `0`.
This definition is overridden in the compiler with an efficient implementation. This definition is the logical model.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.add "Permalink")def
```


Nat.add : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.add : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Addition of natural numbers, typically used via the `+` operator.
This function is overridden in both the kernel and the compiler to efficiently evaluate using the arbitrary-precision arithmetic library. The definition provided here is the logical model.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.sub "Permalink")def
```


Nat.sub : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.sub : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Subtraction of natural numbers, truncated at `0`. Usually used via the `-` operator.
If a result would be less than zero, then the result is zero.
This definition is overridden in both the kernel and the compiler to efficiently evaluate using the arbitrary-precision arithmetic library. The definition provided here is the logical model.
Examples:
  * `5 - 3 = 2`
  * `8 - 2 = 6`
  * `8 - 8 = 0`
  * `8 - 20 = 0`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.mul "Permalink")def
```


Nat.mul : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.mul : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Multiplication of natural numbers, usually accessed via the `*` operator.
This function is overridden in both the kernel and the compiler to efficiently evaluate using the arbitrary-precision arithmetic library. The definition provided here is the logical model.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.div "Permalink")def
```


Nat.div (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.div (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Division of natural numbers, discarding the remainder. Division by `0` returns `0`. Usually accessed via the `/` operator.
This operation is sometimes called “floor division.”
This function is overridden at runtime with an efficient implementation. This definition is the logical model.
Examples:
  * `21 / 3 = 7`
  * `21 / 5 = 4`
  * `0 / 22 = 0`
  * `5 / 0 = 0`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.mod "Permalink")def
```


Nat.mod : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.mod : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The modulo operator, which computes the remainder when dividing one natural number by another. Usually accessed via the `%` operator. When the divisor is `0`, the result is the dividend rather than an error.
`[Nat.mod](Basic-Types/Natural-Numbers/#Nat___mod "Documentation for Nat.mod")` is a wrapper around `[Nat.modCore](Basic-Types/Natural-Numbers/#Nat___modCore "Documentation for Nat.modCore")` that special-cases two situations, giving better definitional reductions:
  * `[Nat.mod](Basic-Types/Natural-Numbers/#Nat___mod "Documentation for Nat.mod") 0 m` should reduce to `m`, for all terms `m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`.
  * `[Nat.mod](Basic-Types/Natural-Numbers/#Nat___mod "Documentation for Nat.mod") n (m + n + 1)` should reduce to `n` for concrete `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` literals `n`.


These reductions help `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` literals work well, because the `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat")` instance for `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` uses `[Nat.mod](Basic-Types/Natural-Numbers/#Nat___mod "Documentation for Nat.mod")`. In particular, `(0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n + 1)).[val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val")` should reduce definitionally to `0`. `[Nat.modCore](Basic-Types/Natural-Numbers/#Nat___modCore "Documentation for Nat.modCore")` can handle all numbers, but its definitional reductions are not as convenient.
This function is overridden at runtime with an efficient implementation. This definition is the logical model.
Examples:
  * `7 % 2 = 1`
  * `9 % 3 = 0`
  * `5 % 7 = 5`
  * `5 % 0 = 5`
  * `show ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), 0 % n = 0 from fun _ => [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`
  * `show ∀ (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), 5 % (m + 6) = 5 from fun _ => [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.modCore "Permalink")def
```


Nat.modCore (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.modCore (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The modulo operator, which computes the remainder when dividing one natural number by another. Usually accessed via the `%` operator. When the divisor is `0`, the result is the dividend rather than an error.
This is the core implementation of `[Nat.mod](Basic-Types/Natural-Numbers/#Nat___mod "Documentation for Nat.mod")`. It computes the correct result for any two closed natural numbers, but it does not have some convenient [definitional reductions](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=type-system) when the `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`s contain free variables. The wrapper `[Nat.mod](Basic-Types/Natural-Numbers/#Nat___mod "Documentation for Nat.mod")` handles those cases specially and then calls `[Nat.modCore](Basic-Types/Natural-Numbers/#Nat___modCore "Documentation for Nat.modCore")`.
This function is overridden at runtime with an efficient implementation. This definition is the logical model.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.pow "Permalink")def
```


Nat.pow (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.pow (m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The power operation on natural numbers, usually accessed via the `^` operator.
This function is overridden in both the kernel and the compiler to efficiently evaluate using the arbitrary-precision arithmetic library. The definition provided here is the logical model.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.log2 "Permalink")def
```


Nat.log2 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.log2 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Base-two logarithm of natural numbers. Returns `⌊max 0 (log₂ n)⌋`.
This function is overridden at runtime with an efficient implementation. This definition is the logical model.
Examples:
  * `[Nat.log2](Basic-Types/Natural-Numbers/#Nat___log2 "Documentation for Nat.log2") 0 = 0`
  * `[Nat.log2](Basic-Types/Natural-Numbers/#Nat___log2 "Documentation for Nat.log2") 1 = 0`
  * `[Nat.log2](Basic-Types/Natural-Numbers/#Nat___log2 "Documentation for Nat.log2") 2 = 1`
  * `[Nat.log2](Basic-Types/Natural-Numbers/#Nat___log2 "Documentation for Nat.log2") 4 = 2`
  * `[Nat.log2](Basic-Types/Natural-Numbers/#Nat___log2 "Documentation for Nat.log2") 7 = 2`
  * `[Nat.log2](Basic-Types/Natural-Numbers/#Nat___log2 "Documentation for Nat.log2") 8 = 3`


####  20.1.4.1.1. Bitwise Operations[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-api-bitwise "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.shiftLeft "Permalink")def
```


Nat.shiftLeft : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.shiftLeft : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Shifts the binary representation of a value left by the specified number of bits. Usually accessed via the `<<<` operator.
Examples:
  * `1 <<< 2 = 4`
  * `1 <<< 3 = 8`
  * `0 <<< 3 = 0`
  * `0xf1 <<< 4 = 0xf10`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.shiftRight "Permalink")def
```


Nat.shiftRight : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.shiftRight : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Shifts the binary representation of a value right by the specified number of bits. Usually accessed via the `>>>` operator.
Examples:
  * `4 >>> 2 = 1`
  * `8 >>> 2 = 2`
  * `8 >>> 3 = 1`
  * `0 >>> 3 = 0`
  * `0xf13a >>> 8 = 0xf1`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.xor "Permalink")def
```


Nat.xor : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.xor : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Bitwise exclusive or. Usually accessed via the `^^^` operator.
Each bit of the resulting value is set if the corresponding bit is set in exactly one of the inputs.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.lor "Permalink")def
```


Nat.lor : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.lor : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Bitwise or. Usually accessed via the `|||` operator.
Each bit of the resulting value is set if the corresponding bit is set in at least one of the inputs.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.land "Permalink")def
```


Nat.land : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.land : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Bitwise and. Usually accessed via the `&&&` operator.
Each bit of the resulting value is set if the corresponding bit is set in both of the inputs.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.bitwise "Permalink")def
```


Nat.bitwise (f : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.bitwise (f : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

A helper for implementing bitwise operators on `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`.
Each bit of the resulting `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` is the result of applying `f` to the corresponding bits of the input `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`s, up to the position of the highest set bit in either input.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.testBit "Permalink")def
```


Nat.testBit (m n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Nat.testBit (m n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the `(n+1)`th least significant bit is `1`, or `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` if it is `0`.
###  20.1.4.2. Minimum and Maximum[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-api-minmax "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.min "Permalink")def
```


Nat.min (n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.min (n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the lesser of two natural numbers. Usually accessed via `[Min.min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min.min")`.
Returns `n` if `n ≤ m`, or `m` if `m ≤ n`.
Examples:
  * `[min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min.min") 0 5 = 0`
  * `[min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min.min") 4 5 = 4`
  * `[min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min.min") 4 3 = 3`
  * `[min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min.min") 8 8 = 8`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.max "Permalink")def
```


Nat.max (n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.max (n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the greater of two natural numbers. Usually accessed via `[Max.max](Type-Classes/Basic-Classes/#Max___mk "Documentation for Max.max")`.
Returns `m` if `n ≤ m`, or `n` if `m ≤ n`.
Examples:
  * `[max](Type-Classes/Basic-Classes/#Max___mk "Documentation for Max.max") 0 5 = 5`
  * `[max](Type-Classes/Basic-Classes/#Max___mk "Documentation for Max.max") 4 5 = 5`
  * `[max](Type-Classes/Basic-Classes/#Max___mk "Documentation for Max.max") 4 3 = 4`
  * `[max](Type-Classes/Basic-Classes/#Max___mk "Documentation for Max.max") 8 8 = 8`


###  20.1.4.3. GCD and LCM[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-api-gcd-lcm "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.gcd "Permalink")def
```


Nat.gcd (m n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.gcd (m n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Computes the greatest common divisor of two natural numbers. The GCD of two natural numbers is the largest natural number that evenly divides both.
In particular, the GCD of a number and `0` is the number itself.
This reference implementation via the Euclidean algorithm is overridden in both the kernel and the compiler to efficiently evaluate using arbitrary-precision arithmetic. The definition provided here is the logical model.
Examples:
  * `[Nat.gcd](Basic-Types/Natural-Numbers/#Nat___gcd "Documentation for Nat.gcd") 10 15 = 5`
  * `[Nat.gcd](Basic-Types/Natural-Numbers/#Nat___gcd "Documentation for Nat.gcd") 0 5 = 5`
  * `[Nat.gcd](Basic-Types/Natural-Numbers/#Nat___gcd "Documentation for Nat.gcd") 7 0 = 7`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.lcm "Permalink")def
```


Nat.lcm (m n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.lcm (m n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The least common multiple of `m` and `n` is the smallest natural number that's evenly divisible by both `m` and `n`. Returns `0` if either `m` or `n` is `0`.
Examples:
  * `[Nat.lcm](Basic-Types/Natural-Numbers/#Nat___lcm "Documentation for Nat.lcm") 9 6 = 18`
  * `[Nat.lcm](Basic-Types/Natural-Numbers/#Nat___lcm "Documentation for Nat.lcm") 9 3 = 9`
  * `[Nat.lcm](Basic-Types/Natural-Numbers/#Nat___lcm "Documentation for Nat.lcm") 0 3 = 0`
  * `[Nat.lcm](Basic-Types/Natural-Numbers/#Nat___lcm "Documentation for Nat.lcm") 3 0 = 0`


###  20.1.4.4. Powers of Two[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-api-pow2 "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.isPowerOfTwo "Permalink")def
```


Nat.isPowerOfTwo (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : Prop


Nat.isPowerOfTwo (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : Prop


```

A natural number `n` is a power of two if there exists some `k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` such that `n = 2 ^ k`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.nextPowerOfTwo "Permalink")def
```


Nat.nextPowerOfTwo (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Nat.nextPowerOfTwo (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the least power of two that's greater than or equal to `n`.
Examples:
  * `[Nat.nextPowerOfTwo](Basic-Types/Natural-Numbers/#Nat___nextPowerOfTwo "Documentation for Nat.nextPowerOfTwo") 0 = 1`
  * `[Nat.nextPowerOfTwo](Basic-Types/Natural-Numbers/#Nat___nextPowerOfTwo "Documentation for Nat.nextPowerOfTwo") 1 = 1`
  * `[Nat.nextPowerOfTwo](Basic-Types/Natural-Numbers/#Nat___nextPowerOfTwo "Documentation for Nat.nextPowerOfTwo") 2 = 2`
  * `[Nat.nextPowerOfTwo](Basic-Types/Natural-Numbers/#Nat___nextPowerOfTwo "Documentation for Nat.nextPowerOfTwo") 3 = 4`
  * `[Nat.nextPowerOfTwo](Basic-Types/Natural-Numbers/#Nat___nextPowerOfTwo "Documentation for Nat.nextPowerOfTwo") 5 = 8`


###  20.1.4.5. Comparisons[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-api-comparison "Permalink")
####  20.1.4.5.1. Boolean Comparisons[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-api-comparison-bool "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.beq "Permalink")def
```


Nat.beq : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Nat.beq : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Boolean equality of natural numbers, usually accessed via the `==` operator.
This function is overridden in both the kernel and the compiler to efficiently evaluate using the arbitrary-precision arithmetic library. The definition provided here is the logical model.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.ble "Permalink")def
```


Nat.ble : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Nat.ble : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

The Boolean less-than-or-equal-to comparison on natural numbers.
This function is overridden in both the kernel and the compiler to efficiently evaluate using the arbitrary-precision arithmetic library. The definition provided here is the logical model.
Examples:
  * `[Nat.ble](Basic-Types/Natural-Numbers/#Nat___ble "Documentation for Nat.ble") 2 5 = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[Nat.ble](Basic-Types/Natural-Numbers/#Nat___ble "Documentation for Nat.ble") 5 2 = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `[Nat.ble](Basic-Types/Natural-Numbers/#Nat___ble "Documentation for Nat.ble") 5 5 = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.blt "Permalink")def
```


Nat.blt (a b : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Nat.blt (a b : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

The Boolean less-than comparison on natural numbers.
This function is overridden in both the kernel and the compiler to efficiently evaluate using the arbitrary-precision arithmetic library. The definition provided here is the logical model.
Examples:
  * `[Nat.blt](Basic-Types/Natural-Numbers/#Nat___blt "Documentation for Nat.blt") 2 5 = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[Nat.blt](Basic-Types/Natural-Numbers/#Nat___blt "Documentation for Nat.blt") 5 2 = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `[Nat.blt](Basic-Types/Natural-Numbers/#Nat___blt "Documentation for Nat.blt") 5 5 = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


####  20.1.4.5.2. Decidable Equality[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-api-deceq "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.decEq "Permalink")def
```


Nat.decEq (n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") m[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


Nat.decEq (n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") m[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


```

A decision procedure for equality of natural numbers, usually accessed via the `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` instance.
This function is overridden in both the kernel and the compiler to efficiently evaluate using the arbitrary-precision arithmetic library. The definition provided here is the logical model.
Examples:
  * `[Nat.decEq](Basic-Types/Natural-Numbers/#Nat___decEq "Documentation for Nat.decEq") 5 5 = [isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 3 = 4 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show 12 = 12 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.decLe "Permalink")def
```


Nat.decLe (n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")n [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") m[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


Nat.decLe (n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")n [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") m[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")


```

A decision procedure for non-strict inequality of natural numbers, usually accessed via the `[DecidableLE](Type-Classes/Basic-Classes/#DecidableLE "Documentation for DecidableLE") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` instance.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 3 ≤ 4 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 6 ≤ 4 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show 12 ≤ 12 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`
  * `show 5 ≤ 12 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.decLt "Permalink")def
```


Nat.decLt (n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") m[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


Nat.decLt (n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") m[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")


```

A decision procedure for strict inequality of natural numbers, usually accessed via the `[DecidableLT](Type-Classes/Basic-Classes/#DecidableLT "Documentation for DecidableLT") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` instance.
Examples:
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 3 < 4 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "yes"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 4 < 4 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 6 < 4 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "yes" [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "no") = "no"`
  * `show 5 < 12 by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`


####  20.1.4.5.3. Predicates[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-api-predicates "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.le.refl "Permalink")inductive predicate
```


Nat.le (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Prop


Nat.le (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Prop


```

Non-strict, or weak, inequality of natural numbers, usually accessed via the `≤` operator.
#  Constructors

```
refl {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : n.[le](Basic-Types/Natural-Numbers/#Nat___le___refl "Documentation for Nat.le") n
```

Non-strict inequality is reflexive: `n ≤ n`

```
step {n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : n.[le](Basic-Types/Natural-Numbers/#Nat___le___refl "Documentation for Nat.le") m → n.[le](Basic-Types/Natural-Numbers/#Nat___le___refl "Documentation for Nat.le") m.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")
```

If `n ≤ m`, then `n ≤ m + 1`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.lt "Permalink")def
```


Nat.lt (n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : Prop


Nat.lt (n m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : Prop


```

Strict inequality of natural numbers, usually accessed via the `<` operator.
It is defined as `n < m = n + 1 ≤ m`.
###  20.1.4.6. Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-api-iteration "Permalink")
Many iteration operators come in two versions: a structurally recursive version and a tail-recursive version. The structurally recursive version is typically easier to use in contexts where definitional equality is important, as it will compute when only some prefix of a natural number is known.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.repeat "Permalink")def
```


Nat.repeat.{u} {α : Type u} (f : α → α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) : α


Nat.repeat.{u} {α : Type u} (f : α → α)
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) : α


```

Applies a function to a starting value the specified number of times.
In other words, `f` is iterated `n` times on `a`.
Examples:
  * `Nat.repeat f 3 a = f <| f <| f <| a`
  * `[Nat.repeat](Basic-Types/Natural-Numbers/#Nat___repeat "Documentation for Nat.repeat") (· ++ "!") 4 "Hello" = "Hello!!!!"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.repeatTR "Permalink")def
```


Nat.repeatTR.{u} {α : Type u} (f : α → α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) : α


Nat.repeatTR.{u} {α : Type u} (f : α → α)
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) : α


```

Applies a function to a starting value the specified number of times.
In other words, `f` is iterated `n` times on `a`.
This is a tail-recursive version of `[Nat.repeat](Basic-Types/Natural-Numbers/#Nat___repeat "Documentation for Nat.repeat")` that's used at runtime.
Examples:
  * `Nat.repeatTR f 3 a = f <| f <| f <| a`
  * `[Nat.repeatTR](Basic-Types/Natural-Numbers/#Nat___repeatTR "Documentation for Nat.repeatTR") (· ++ "!") 4 "Hello" = "Hello!!!!"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.fold "Permalink")def
```


Nat.fold.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → α → α)
  (init : α) : α


Nat.fold.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → α → α)
  (init : α) : α


```

Iterates the application of a function `f` to a starting value `init`, `n` times. At each step, `f` is applied to the current value and to the next natural number less than `n`, in increasing order.
Examples:
  * `[Nat.fold](Basic-Types/Natural-Numbers/#Nat___fold "Documentation for Nat.fold") 3 f init = (init |> f 0 (by [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")) |> f 1 (by [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")) |> f 2 (by [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")))`
  * `[Nat.fold](Basic-Types/Natural-Numbers/#Nat___fold "Documentation for Nat.fold") 4 (fun i _ xs => xs.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") i) #[] = #[0, 1, 2, 3]`
  * `[Nat.fold](Basic-Types/Natural-Numbers/#Nat___fold "Documentation for Nat.fold") 0 (fun i _ xs => xs.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") i) #[] = #[]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.foldTR "Permalink")def
```


Nat.foldTR.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → α → α)
  (init : α) : α


Nat.foldTR.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → α → α)
  (init : α) : α


```

Iterates the application of a function `f` to a starting value `init`, `n` times. At each step, `f` is applied to the current value and to the next natural number less than `n`, in increasing order.
This is a tail-recursive version of `[Nat.fold](Basic-Types/Natural-Numbers/#Nat___fold "Documentation for Nat.fold")` that's used at runtime.
Examples:
  * `[Nat.foldTR](Basic-Types/Natural-Numbers/#Nat___foldTR "Documentation for Nat.foldTR") 3 f init = (init |> f 0 (by [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")) |> f 1 (by [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")) |> f 2 (by [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")))`
  * `[Nat.foldTR](Basic-Types/Natural-Numbers/#Nat___foldTR "Documentation for Nat.foldTR") 4 (fun i _ xs => xs.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") i) #[] = #[0, 1, 2, 3]`
  * `[Nat.foldTR](Basic-Types/Natural-Numbers/#Nat___foldTR "Documentation for Nat.foldTR") 0 (fun i _ xs => xs.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") i) #[] = #[]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.foldM "Permalink")def
```


Nat.foldM.{u, v} {α : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → α → m α) (init : α) : m α


Nat.foldM.{u, v} {α : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → α → m α)
  (init : α) : m α


```

Iterates the application of a monadic function `f` to a starting value `init`, `n` times. At each step, `f` is applied to the current value and to the next natural number less than `n`, in increasing order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.foldRev "Permalink")def
```


Nat.foldRev.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → α → α)
  (init : α) : α


Nat.foldRev.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → α → α)
  (init : α) : α


```

Iterates the application of a function `f` to a starting value `init`, `n` times. At each step, `f` is applied to the current value and to the next natural number less than `n`, in decreasing order.
Examples:
  * `[Nat.foldRev](Basic-Types/Natural-Numbers/#Nat___foldRev "Documentation for Nat.foldRev") 3 f init = (f 0 (by [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")) <| f 1 (by [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")) <| f 2 (by [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")) init)`
  * `[Nat.foldRev](Basic-Types/Natural-Numbers/#Nat___foldRev "Documentation for Nat.foldRev") 4 (fun i _ xs => xs.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") i) #[] = #[3, 2, 1, 0]`
  * `[Nat.foldRev](Basic-Types/Natural-Numbers/#Nat___foldRev "Documentation for Nat.foldRev") 0 (fun i _ xs => xs.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") i) #[] = #[]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.foldRevM "Permalink")def
```


Nat.foldRevM.{u, v} {α : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → α → m α) (init : α) : m α


Nat.foldRevM.{u, v} {α : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → α → m α)
  (init : α) : m α


```

Iterates the application of a monadic function `f` to a starting value `init`, `n` times. At each step, `f` is applied to the current value and to the next natural number less than `n`, in decreasing order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.forM "Permalink")def
```


Nat.forM.{u_1} {m : Type → Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")) : m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


Nat.forM.{u_1} {m : Type → Type u_1}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")) :
  m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Executes a monadic action on all the numbers less than some bound, in increasing order.
Example:
``0 1 2 3 4 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Nat.forM](Basic-Types/Natural-Numbers/#Nat___forM "Documentation for Nat.forM") 5 fun i _ => [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") i ``0 1 2 3 4`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.forRevM "Permalink")def
```


Nat.forRevM.{u_1} {m : Type → Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")) : m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


Nat.forRevM.{u_1} {m : Type → Type u_1}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")) :
  m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Executes a monadic action on all the numbers less than some bound, in decreasing order.
Example:
``4 3 2 1 0 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Nat.forRevM](Basic-Types/Natural-Numbers/#Nat___forRevM "Documentation for Nat.forRevM") 5 fun i _ => [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") i ``4 3 2 1 0`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.all "Permalink")def
```


Nat.all (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Nat.all (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether `f` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for every number strictly less than a bound.
Examples:
  * `[Nat.all](Basic-Types/Natural-Numbers/#Nat___all "Documentation for Nat.all") 4 (fun i _ => i < 5) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[Nat.all](Basic-Types/Natural-Numbers/#Nat___all "Documentation for Nat.all") 7 (fun i _ => i < 5) = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `[Nat.all](Basic-Types/Natural-Numbers/#Nat___all "Documentation for Nat.all") 7 (fun i _ => i % 2 = 0) = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `[Nat.all](Basic-Types/Natural-Numbers/#Nat___all "Documentation for Nat.all") 1 (fun i _ => i % 2 = 0) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.allTR "Permalink")def
```


Nat.allTR (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Nat.allTR (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether `f` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for every number strictly less than a bound.
This is a tail-recursive equivalent of `[Nat.all](Basic-Types/Natural-Numbers/#Nat___all "Documentation for Nat.all")` that's used at runtime.
Examples:
  * `[Nat.allTR](Basic-Types/Natural-Numbers/#Nat___allTR "Documentation for Nat.allTR") 4 (fun i _ => i < 5) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[Nat.allTR](Basic-Types/Natural-Numbers/#Nat___allTR "Documentation for Nat.allTR") 7 (fun i _ => i < 5) = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `[Nat.allTR](Basic-Types/Natural-Numbers/#Nat___allTR "Documentation for Nat.allTR") 7 (fun i _ => i % 2 = 0) = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `[Nat.allTR](Basic-Types/Natural-Numbers/#Nat___allTR "Documentation for Nat.allTR") 1 (fun i _ => i % 2 = 0) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.any "Permalink")def
```


Nat.any (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Nat.any (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether there is some number less that the given bound for which `f` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Examples:
  * `[Nat.any](Basic-Types/Natural-Numbers/#Nat___any "Documentation for Nat.any") 4 (fun i _ => i < 5) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[Nat.any](Basic-Types/Natural-Numbers/#Nat___any "Documentation for Nat.any") 7 (fun i _ => i < 5) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[Nat.any](Basic-Types/Natural-Numbers/#Nat___any "Documentation for Nat.any") 7 (fun i _ => i % 2 = 0) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[Nat.any](Basic-Types/Natural-Numbers/#Nat___any "Documentation for Nat.any") 1 (fun i _ => i % 2 = 1) = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.anyTR "Permalink")def
```


Nat.anyTR (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Nat.anyTR (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether there is some number less that the given bound for which `f` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
This is a tail-recursive equivalent of `[Nat.any](Basic-Types/Natural-Numbers/#Nat___any "Documentation for Nat.any")` that's used at runtime.
Examples:
  * `[Nat.anyTR](Basic-Types/Natural-Numbers/#Nat___anyTR "Documentation for Nat.anyTR") 4 (fun i _ => i < 5) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[Nat.anyTR](Basic-Types/Natural-Numbers/#Nat___anyTR "Documentation for Nat.anyTR") 7 (fun i _ => i < 5) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[Nat.anyTR](Basic-Types/Natural-Numbers/#Nat___anyTR "Documentation for Nat.anyTR") 7 (fun i _ => i % 2 = 0) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[Nat.anyTR](Basic-Types/Natural-Numbers/#Nat___anyTR "Documentation for Nat.anyTR") 1 (fun i _ => i % 2 = 1) = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.allM "Permalink")def
```


Nat.allM.{u_1} {m : Type → Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (p : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Nat.allM.{u_1} {m : Type → Type u_1}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (p : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the monadic predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for all numbers less that the given bound. Numbers are checked in increasing order until `p` returns false, after which no further are checked.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.anyM "Permalink")def
```


Nat.anyM.{u_1} {m : Type → Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (p : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Nat.anyM.{u_1} {m : Type → Type u_1}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (p : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether there is some number less that the given bound for which the monadic predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`. Numbers are checked in increasing order until `p` returns true, after which no further are checked.
###  20.1.4.7. Conversion[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-api-conversion "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.toUInt8 "Permalink")def
```


Nat.toUInt8 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


Nat.toUInt8 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Converts a natural number to an 8-bit unsigned integer, wrapping on overflow.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Nat.toUInt8](Basic-Types/Natural-Numbers/#Nat___toUInt8 "Documentation for Nat.toUInt8") 5 = 5`
  * `[Nat.toUInt8](Basic-Types/Natural-Numbers/#Nat___toUInt8 "Documentation for Nat.toUInt8") 255 = 255`
  * `[Nat.toUInt8](Basic-Types/Natural-Numbers/#Nat___toUInt8 "Documentation for Nat.toUInt8") 256 = 0`
  * `[Nat.toUInt8](Basic-Types/Natural-Numbers/#Nat___toUInt8 "Documentation for Nat.toUInt8") 259 = 3`
  * `[Nat.toUInt8](Basic-Types/Natural-Numbers/#Nat___toUInt8 "Documentation for Nat.toUInt8") 32770 = 2`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.toUInt16 "Permalink")def
```


Nat.toUInt16 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


Nat.toUInt16 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Converts a natural number to a 16-bit unsigned integer, wrapping on overflow.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Nat.toUInt16](Basic-Types/Natural-Numbers/#Nat___toUInt16 "Documentation for Nat.toUInt16") 5 = 5`
  * `[Nat.toUInt16](Basic-Types/Natural-Numbers/#Nat___toUInt16 "Documentation for Nat.toUInt16") 255 = 255`
  * `[Nat.toUInt16](Basic-Types/Natural-Numbers/#Nat___toUInt16 "Documentation for Nat.toUInt16") 32770 = 32770`
  * `[Nat.toUInt16](Basic-Types/Natural-Numbers/#Nat___toUInt16 "Documentation for Nat.toUInt16") 65537 = 1`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.toUInt32 "Permalink")def
```


Nat.toUInt32 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


Nat.toUInt32 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Converts a natural number to a 32-bit unsigned integer, wrapping on overflow.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Nat.toUInt32](Basic-Types/Natural-Numbers/#Nat___toUInt32 "Documentation for Nat.toUInt32") 5 = 5`
  * `[Nat.toUInt32](Basic-Types/Natural-Numbers/#Nat___toUInt32 "Documentation for Nat.toUInt32") 65_539 = 65_539`
  * `[Nat.toUInt32](Basic-Types/Natural-Numbers/#Nat___toUInt32 "Documentation for Nat.toUInt32") 4_294_967_299 = 3`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.toUInt64 "Permalink")def
```


Nat.toUInt64 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


Nat.toUInt64 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Converts a natural number to a 64-bit unsigned integer, wrapping on overflow.
This function is overridden at runtime with an efficient implementation.
Examples:
  * `[Nat.toUInt64](Basic-Types/Natural-Numbers/#Nat___toUInt64 "Documentation for Nat.toUInt64") 5 = 5`
  * `[Nat.toUInt64](Basic-Types/Natural-Numbers/#Nat___toUInt64 "Documentation for Nat.toUInt64") 65539 = 65539`
  * `[Nat.toUInt64](Basic-Types/Natural-Numbers/#Nat___toUInt64 "Documentation for Nat.toUInt64") 4_294_967_299 = 4_294_967_299`
  * `[Nat.toUInt64](Basic-Types/Natural-Numbers/#Nat___toUInt64 "Documentation for Nat.toUInt64") 18_446_744_073_709_551_620 = 4`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.toUSize "Permalink")def
```


Nat.toUSize (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


Nat.toUSize (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Converts an arbitrary-precision natural number to an unsigned word-sized integer, wrapping around on overflow.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.toInt8 "Permalink")def
```


Nat.toInt8 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Nat.toInt8 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Converts a natural number to an 8-bit signed integer, wrapping around to negative numbers on overflow.
Examples:
  * `[Nat.toInt8](Basic-Types/Natural-Numbers/#Nat___toInt8 "Documentation for Nat.toInt8") 53 = 53`
  * `[Nat.toInt8](Basic-Types/Natural-Numbers/#Nat___toInt8 "Documentation for Nat.toInt8") 127 = 127`
  * `[Nat.toInt8](Basic-Types/Natural-Numbers/#Nat___toInt8 "Documentation for Nat.toInt8") 128 = -128`
  * `[Nat.toInt8](Basic-Types/Natural-Numbers/#Nat___toInt8 "Documentation for Nat.toInt8") 255 = -1`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.toInt16 "Permalink")def
```


Nat.toInt16 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Nat.toInt16 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Converts a natural number to a 16-bit signed integer, wrapping around to negative numbers on overflow.
Examples:
  * `[Nat.toInt16](Basic-Types/Natural-Numbers/#Nat___toInt16 "Documentation for Nat.toInt16") 127 = 127`
  * `[Nat.toInt16](Basic-Types/Natural-Numbers/#Nat___toInt16 "Documentation for Nat.toInt16") 32767 = 32767`
  * `[Nat.toInt16](Basic-Types/Natural-Numbers/#Nat___toInt16 "Documentation for Nat.toInt16") 32768 = -32768`
  * `[Nat.toInt16](Basic-Types/Natural-Numbers/#Nat___toInt16 "Documentation for Nat.toInt16") 32770 = -32766`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.toInt32 "Permalink")def
```


Nat.toInt32 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Nat.toInt32 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Converts a natural number to a 32-bit signed integer, wrapping around to negative numbers on overflow.
Examples:
  * `[Nat.toInt32](Basic-Types/Natural-Numbers/#Nat___toInt32 "Documentation for Nat.toInt32") 127 = 127`
  * `[Nat.toInt32](Basic-Types/Natural-Numbers/#Nat___toInt32 "Documentation for Nat.toInt32") 32770 = 32770`
  * `[Nat.toInt32](Basic-Types/Natural-Numbers/#Nat___toInt32 "Documentation for Nat.toInt32") 2_147_483_647 = 2_147_483_647`
  * `[Nat.toInt32](Basic-Types/Natural-Numbers/#Nat___toInt32 "Documentation for Nat.toInt32") 2_147_483_648 = -2_147_483_648`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.toInt64 "Permalink")def
```


Nat.toInt64 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Nat.toInt64 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Converts a natural number to a 64-bit signed integer, wrapping around to negative numbers on overflow.
Examples:
  * `[Nat.toInt64](Basic-Types/Natural-Numbers/#Nat___toInt64 "Documentation for Nat.toInt64") 127 = 127`
  * `[Nat.toInt64](Basic-Types/Natural-Numbers/#Nat___toInt64 "Documentation for Nat.toInt64") 2_147_483_648 = 2_147_483_648`
  * `[Nat.toInt64](Basic-Types/Natural-Numbers/#Nat___toInt64 "Documentation for Nat.toInt64") 9_223_372_036_854_775_807 = 9_223_372_036_854_775_807`
  * `[Nat.toInt64](Basic-Types/Natural-Numbers/#Nat___toInt64 "Documentation for Nat.toInt64") 9_223_372_036_854_775_808 = -9_223_372_036_854_775_808`
  * `[Nat.toInt64](Basic-Types/Natural-Numbers/#Nat___toInt64 "Documentation for Nat.toInt64") 18_446_744_073_709_551_618 = 0`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.toISize "Permalink")def
```


Nat.toISize (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


Nat.toISize (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Converts an arbitrary-precision natural number to a word-sized signed integer, wrapping around on overflow.
This function is overridden at runtime with an efficient implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.toFloat "Permalink")def
```


Nat.toFloat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


Nat.toFloat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")


```

Converts a natural number into the closest-possible 64-bit floating-point number, or an infinite floating-point value if the range of `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` is exceeded.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.toFloat32 "Permalink")def
```


Nat.toFloat32 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


Nat.toFloat32 (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")


```

Converts a natural number into the closest-possible 32-bit floating-point number, or an infinite floating-point value if the range of `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")` is exceeded.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.isValidChar "Permalink")def
```


Nat.isValidChar (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : Prop


Nat.isValidChar (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : Prop


```

A `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` denotes a valid Unicode code point if it is less than `0x110000` and it is also not a surrogate code point (the range `0xd800` to `0xdfff` inclusive).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.repr "Permalink")def
```


Nat.repr (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


Nat.repr (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Converts a natural number to its decimal string representation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.toDigits "Permalink")def
```


Nat.toDigits (base n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


Nat.toDigits (base n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Returns the decimal representation of a natural number as a list of digit characters in the given base. If the base is greater than `16` then `'*'` is returned for digits greater than `0xf`.
Examples:
  * `[Nat.toDigits](Basic-Types/Natural-Numbers/#Nat___toDigits "Documentation for Nat.toDigits") 10 0xff = ['2', '5', '5']`
  * `[Nat.toDigits](Basic-Types/Natural-Numbers/#Nat___toDigits "Documentation for Nat.toDigits") 8 0xc = ['1', '4']`
  * `[Nat.toDigits](Basic-Types/Natural-Numbers/#Nat___toDigits "Documentation for Nat.toDigits") 16 0xcafe = ['c', 'a', 'f', 'e']`
  * `[Nat.toDigits](Basic-Types/Natural-Numbers/#Nat___toDigits "Documentation for Nat.toDigits") 80 200 = ['2', '*']`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.digitChar "Permalink")def
```


Nat.digitChar (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


Nat.digitChar (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Returns a single digit representation of `n`, which is assumed to be in a base less than or equal to `16`. Returns `'*'` if `n > 15`.
Examples:
  * `[Nat.digitChar](Basic-Types/Natural-Numbers/#Nat___digitChar "Documentation for Nat.digitChar") 5 = '5'`
  * `[Nat.digitChar](Basic-Types/Natural-Numbers/#Nat___digitChar "Documentation for Nat.digitChar") 12 = 'c'`
  * `[Nat.digitChar](Basic-Types/Natural-Numbers/#Nat___digitChar "Documentation for Nat.digitChar") 15 = 'f'`
  * `[Nat.digitChar](Basic-Types/Natural-Numbers/#Nat___digitChar "Documentation for Nat.digitChar") 16 = '*'`
  * `[Nat.digitChar](Basic-Types/Natural-Numbers/#Nat___digitChar "Documentation for Nat.digitChar") 85 = '*'`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.toSubscriptString "Permalink")def
```


Nat.toSubscriptString (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


Nat.toSubscriptString (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Converts a natural number to a string that contains the its decimal representation as Unicode subscript digit characters.
Examples:
  * `[Nat.toSubscriptString](Basic-Types/Natural-Numbers/#Nat___toSubscriptString "Documentation for Nat.toSubscriptString") 0 = "₀"`
  * `[Nat.toSubscriptString](Basic-Types/Natural-Numbers/#Nat___toSubscriptString "Documentation for Nat.toSubscriptString") 35 = "₃₅"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.toSuperscriptString "Permalink")def
```


Nat.toSuperscriptString (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


Nat.toSuperscriptString (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Converts a natural number to a string that contains the its decimal representation as Unicode superscript digit characters.
Examples:
  * `[Nat.toSuperscriptString](Basic-Types/Natural-Numbers/#Nat___toSuperscriptString "Documentation for Nat.toSuperscriptString") 0 = "⁰"`
  * `[Nat.toSuperscriptString](Basic-Types/Natural-Numbers/#Nat___toSuperscriptString "Documentation for Nat.toSuperscriptString") 35 = "³⁵"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.toSuperDigits "Permalink")def
```


Nat.toSuperDigits (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


Nat.toSuperDigits (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Converts a natural number to the list of Unicode superscript digit characters that corresponds to its decimal representation.
Examples:
  * `[Nat.toSuperDigits](Basic-Types/Natural-Numbers/#Nat___toSuperDigits "Documentation for Nat.toSuperDigits") 0 = ['⁰']`
  * `[Nat.toSuperDigits](Basic-Types/Natural-Numbers/#Nat___toSuperDigits "Documentation for Nat.toSuperDigits") 35 = ['³', '⁵']`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.toSubDigits "Permalink")def
```


Nat.toSubDigits (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


Nat.toSubDigits (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Converts a natural number to the list of Unicode subscript digit characters that corresponds to its decimal representation.
Examples:
  * `[Nat.toSubDigits](Basic-Types/Natural-Numbers/#Nat___toSubDigits "Documentation for Nat.toSubDigits") 0 = ['₀']`
  * `[Nat.toSubDigits](Basic-Types/Natural-Numbers/#Nat___toSubDigits "Documentation for Nat.toSubDigits") 35 = ['₃', '₅']`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.subDigitChar "Permalink")def
```


Nat.subDigitChar (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


Nat.subDigitChar (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Converts a natural number less than `10` to the corresponding Unicode subscript digit character. Returns `'*'` for other numbers.
Examples:
  * `[Nat.subDigitChar](Basic-Types/Natural-Numbers/#Nat___subDigitChar "Documentation for Nat.subDigitChar") 3 = '₃'`
  * `[Nat.subDigitChar](Basic-Types/Natural-Numbers/#Nat___subDigitChar "Documentation for Nat.subDigitChar") 7 = '₇'`
  * `[Nat.subDigitChar](Basic-Types/Natural-Numbers/#Nat___subDigitChar "Documentation for Nat.subDigitChar") 10 = '*'`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.superDigitChar "Permalink")def
```


Nat.superDigitChar (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


Nat.superDigitChar (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Converts a natural number less than `10` to the corresponding Unicode superscript digit character. Returns `'*'` for other numbers.
Examples:
  * `[Nat.superDigitChar](Basic-Types/Natural-Numbers/#Nat___superDigitChar "Documentation for Nat.superDigitChar") 3 = '³'`
  * `[Nat.superDigitChar](Basic-Types/Natural-Numbers/#Nat___superDigitChar "Documentation for Nat.superDigitChar") 7 = '⁷'`
  * `[Nat.superDigitChar](Basic-Types/Natural-Numbers/#Nat___superDigitChar "Documentation for Nat.superDigitChar") 10 = '*'`


###  20.1.4.8. Elimination[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-api-elim "Permalink")
The recursion principle that is automatically generated for `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` results in proof goals that are phrased in terms of `[Nat.zero](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.zero")` and `[Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")`. This is not particularly user-friendly, so an alternative logically-equivalent recursion principle is provided that results in goals that are phrased in terms of `0` and `n + 1`. [Custom eliminators](Tactic-Proofs/Tactic-Reference/#--tech-term-Custom-eliminators) for the `[induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic")` and `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")` tactics can be supplied using the `induction_eliminator` and `cases_eliminator` attributes.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.recAux "Permalink")def
```


Nat.recAux.{u} {motive : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u} (zero : motive 0)
  (succ : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → motive n → motive [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) (t : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : motive t


Nat.recAux.{u} {motive : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u}
  (zero : motive 0)
  (succ :
    (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → motive n → motive [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd"))
  (t : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : motive t


```

A recursor for `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` that uses the notations `0` for `[Nat.zero](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.zero")` and `n + 1` for `[Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")`.
It is otherwise identical to the default recursor `Nat.rec`. It is used by the `[induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic")` tactic by default for `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.casesAuxOn "Permalink")def
```


Nat.casesAuxOn.{u} {motive : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u} (t : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (zero : motive 0)
  (succ : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → motive [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) : motive t


Nat.casesAuxOn.{u} {motive : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u}
  (t : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (zero : motive 0)
  (succ : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → motive [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) :
  motive t


```

A case analysis principle for `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` that uses the notations `0` for `[Nat.zero](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.zero")` and `n + 1` for `[Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")`.
It is otherwise identical to the default recursor `Nat.casesOn`. It is used as the default `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` case analysis principle for `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` by the `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")` tactic.
####  20.1.4.8.1. Alternative Induction Principles[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-api-induction "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.strongRecOn "Permalink")def
```


Nat.strongRecOn.{u} {motive : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (ind : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → ((m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → m [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → motive m) → motive n) :
  motive n


Nat.strongRecOn.{u}
  {motive : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (ind :
    (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) →
      ((m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → m [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n → motive m) →
        motive n) :
  motive n


```

Strong induction on the natural numbers.
The induction hypothesis is that all numbers less than a given number satisfy the motive, which should be demonstrated for the given number.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.caseStrongRecOn "Permalink")def
```


Nat.caseStrongRecOn.{u} {motive : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u} (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (zero : motive 0)
  (ind : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → ((m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → m [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") n → motive m) → motive n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")) :
  motive a


Nat.caseStrongRecOn.{u}
  {motive : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u} (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (zero : motive 0)
  (ind :
    (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) →
      ((m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → m [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") n → motive m) →
        motive n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")) :
  motive a


```

Case analysis based on strong induction for the natural numbers.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.div.inductionOn "Permalink")def
```


Nat.div.inductionOn.{u} {motive : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u} (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (ind : (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") y [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") x → motive [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") y[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") y → motive x y)
  (base : (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[(](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And")0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") y [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") x[)](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") → motive x y) : motive x y


Nat.div.inductionOn.{u}
  {motive : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u}
  (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (ind :
    (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) →
      0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") y [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") x →
        motive [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") y[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") y → motive x y)
  (base :
    (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) →
      [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[(](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And")0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") y [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") x[)](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") → motive x y) :
  motive x y


```

An induction principle customized for reasoning about the recursion pattern of natural number division by iterated subtraction.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.div2Induction "Permalink")def
```


Nat.div2Induction.{u} {motive : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (ind : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → (n > 0 → motive [(](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv.hDiv")n [/](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv.hDiv") 2[)](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv.hDiv")) → motive n) : motive n


Nat.div2Induction.{u}
  {motive : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (ind :
    (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) →
      (n > 0 → motive [(](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv.hDiv")n [/](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv.hDiv") 2[)](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv.hDiv")) →
        motive n) :
  motive n


```

An induction principle for the natural numbers with two cases:
  * `n = 0`, and the motive is satisfied for `0`
  * `n > 0`, and the motive should be satisfied for `n` on the assumption that it is satisfied for `n / 2`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.mod.inductionOn "Permalink")def
```


Nat.mod.inductionOn.{u} {motive : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u} (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (ind : (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") y [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") x → motive [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") y[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") y → motive x y)
  (base : (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[(](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And")0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") y [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") x[)](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") → motive x y) : motive x y


Nat.mod.inductionOn.{u}
  {motive : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u}
  (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (ind :
    (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) →
      0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") y [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") x →
        motive [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") y[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") y → motive x y)
  (base :
    (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) →
      [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[(](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And")0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") y [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") x[)](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") → motive x y) :
  motive x y


```

An induction principle customized for reasoning about the recursion pattern of `[Nat.mod](Basic-Types/Natural-Numbers/#Nat___mod "Documentation for Nat.mod")`.
[←20. Basic Types](Basic-Types/#basic-types "20. Basic Types")[20.2. Integers→](Basic-Types/Integers/#Int "20.2. Integers")

[←20.10. The Empty Type](Basic-Types/The-Empty-Type/#empty "20.10. The Empty Type")[20.12. Optional Values→](Basic-Types/Optional-Values/#option "20.12. Optional Values")
#  20.11. Booleans[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Booleans "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bool.true "Permalink")inductive type
```


Bool : Type


Bool : Type


```

The Boolean values, `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` and `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
Logically speaking, this is equivalent to `Prop` (the type of propositions). The distinction is public important for programming: both propositions and their proofs are erased in the code generator, while `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` corresponds to the Boolean type in most programming languages and carries precisely one bit of run-time information.
#  Constructors

```
false : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

The Boolean value `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, not to be confused with the proposition `[False](Basic-Propositions/Truth/#False "Documentation for False")`.

```
true : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

The Boolean value `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, not to be confused with the proposition `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")`.
The constructors `[Bool.true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` and `[Bool.false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` are exported from the `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` namespace, so they can be written `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` and `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
##  20.11.1. Run-Time Representation[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Booleans--Run-Time-Representation "Permalink")
Because `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` is an [enum inductive](The-Type-System/Inductive-Types/#--tech-term-enum-inductive) type, it is represented by a single byte in compiled code.
##  20.11.2. Booleans and Propositions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Booleans--Booleans-and-Propositions "Permalink")
Both `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` and `Prop` represent notions of truth. From a purely logical perspective, they are equivalent: [propositional extensionality](The-Type-System/Propositions/#--tech-term-Extensionality) means that there are fundamentally only two propositions, namely `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")` and `[False](Basic-Propositions/Truth/#False "Documentation for False")`. However, there is an important pragmatic difference: `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` classifies _values_ that can be computed by programs, while `Prop` classifies statements for which code generation doesn't make sense. In other words, `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` is the notion of truth and falsehood that's appropriate for programs, while `Prop` is the notion that's appropriate for mathematics. Because proofs are erased from compiled programs, keeping `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` and `Prop` distinct makes it clear which parts of a Lean file are intended for computation.
A `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` can be used wherever a `Prop` is expected. There is a [coercion](Coercions/#--tech-term-coercion) from every `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` `b` to the proposition `b = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`. By `[propext](The-Type-System/Propositions/#propext "Documentation for propext")`, `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` is equal to `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")`, and `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` is equal to `[False](Basic-Propositions/Truth/#False "Documentation for False")`.
Not every proposition can be used by programs to make run-time decisions. Otherwise, a program could branch on whether the Collatz conjecture is true or false! Many propositions, however, can be checked algorithmically. These propositions are called [_decidable_](Type-Classes/Basic-Classes/#--tech-term-decidable) propositions, and have instances of the `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` type class. The function `[Decidable.decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide")` converts a proof-carrying `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` result into a `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`. This function is also a coercion from decidable propositions to `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`, so `(2 = 2 : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))` evaluates to `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
##  20.11.3. Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Booleans--Syntax "Permalink")
syntaxBoolean Infix Operators
The infix operators `&&`, `||`, and `^^` are notations for `[Bool.and](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")`, `[Bool.or](Basic-Types/Booleans/#Bool___or "Documentation for Bool.or")`, and `[Bool.xor](Basic-Types/Booleans/#Bool___xor "Documentation for Bool.xor")`, respectively.

```
term ::= ...
    | 


Boolean “and”, also known as conjunction. and x y can be written x && y.


The corresponding propositional connective is And : Prop → Prop → Prop, written with the ∧
operator.


The Boolean and is a @[macro_inline] function in order to give it short-circuiting evaluation:
if x is false then y is not evaluated at runtime.


Conventions for notations in identifiers:




  * The recommended spelling of && in identifiers is and.




term && term
```

```
term ::= ...
    | 


Boolean “or”, also known as disjunction. or x y can be written x || y.


The corresponding propositional connective is Or : Prop → Prop → Prop, written with the ∨
operator.


The Boolean or is a @[macro_inline] function in order to give it short-circuiting evaluation:
if x is true then y is not evaluated at runtime.


Conventions for notations in identifiers:




  * The recommended spelling of || in identifiers is or.




term || term
```

```
term ::= ...
    | 


Boolean “exclusive or”. xor x y can be written x ^^ y.


x ^^ y is true when precisely one of x or y is true. Unlike and and or, it does not
have short-circuiting behavior, because one argument's value never determines the final value. Also
unlike and and or, there is no commonly-used corresponding propositional connective.


Examples:




  * false ^^ false = false


  * true ^^ false = true


  * false ^^ true = true


  * true ^^ true = false




Conventions for notations in identifiers:




  * The recommended spelling of ^^ in identifiers is xor.




term ^^ term
```

syntaxBoolean Negation
The prefix operator `!` is notation for `[Bool.not](Basic-Types/Booleans/#Bool___not "Documentation for Bool.not")`.

```
term ::= ...
    | 


Boolean negation, also known as Boolean complement. not x can be written !x.


This is a function that maps the value true to false and the value false to true. The
propositional connective is Not : Prop → Prop.


Conventions for notations in identifiers:




  * The recommended spelling of ! in identifiers is not.




!term
```

##  20.11.4. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Booleans--API-Reference "Permalink")
###  20.11.4.1. Logical Operations[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Booleans--API-Reference--Logical-Operations "Permalink")
The functions `[cond](Basic-Types/Booleans/#cond "Documentation for cond")`, `[and](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")`, and `[or](Basic-Types/Booleans/#Bool___or "Documentation for Bool.or")` are short-circuiting. In other words, `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") && BIG_EXPENSIVE_COMPUTATION` does not need to execute `BIG_EXPENSIVE_COMPUTATION` before returning `false`. These functions are defined using the `macro_inline` attribute, which causes the compiler to replace calls to them with their definitions while generating code, and the definitions use nested pattern matching to achieve the short-circuiting behavior.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=cond "Permalink")def
```


cond.{u} {α : Sort u} (c : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (x y : α) : α


cond.{u} {α : Sort u} (c : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (x y : α) : α


```

The conditional function.
`[cond](Basic-Types/Booleans/#cond "Documentation for cond") c x y` is the same as `[if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") c [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") y`, but optimized for a Boolean condition rather than a decidable proposition. It can also be written using the notation `[bif](Terms/Conditionals/#boolIfThenElse "Documentation for syntax") c [then](Terms/Conditionals/#boolIfThenElse "Documentation for syntax") x [else](Terms/Conditionals/#boolIfThenElse "Documentation for syntax") y`.
Just like `ite`, `[cond](Basic-Types/Booleans/#cond "Documentation for cond")` is declared `@[macro_inline]`, which causes applications of `[cond](Basic-Types/Booleans/#cond "Documentation for cond")` to be unfolded. As a result, `x` and `y` are not evaluated at runtime until one of them is selected, and only the selected branch is evaluated.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bool.dcond "Permalink")def
```


Bool.dcond.{u} {α : Sort u} (c : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (x : c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → α)
  (y : c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") → α) : α


Bool.dcond.{u} {α : Sort u} (c : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (x : c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → α) (y : c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") → α) :
  α


```

The dependent conditional function, in which each branch is provided with a local assumption about the condition's value. This allows the value to be used in proofs as well as for control flow.
`dcond c (fun h => x) (fun h => y)` is the same as `[if](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") h : c [then](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") x [else](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") y`, but optimized for a Boolean condition rather than a decidable proposition. Unlike the non-dependent version `[cond](Basic-Types/Booleans/#cond "Documentation for cond")`, there is no special notation for `dcond`.
Just like `ite`, `dite`, and `[cond](Basic-Types/Booleans/#cond "Documentation for cond")`, `dcond` is declared `@[macro_inline]`, which causes applications of `dcond` to be unfolded. As a result, `x` and `y` are not evaluated at runtime until one of them is selected, and only the selected branch is evaluated. `dcond` is intended for metaprogramming use, rather than for use in verified programs, so behavioral lemmas are not provided.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bool.not "Permalink")def
```


Bool.not : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Bool.not : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Boolean negation, also known as Boolean complement. `[not](Basic-Types/Booleans/#Bool___not "Documentation for Bool.not") x` can be written `!x`.
This is a function that maps the value `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` and the value `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` to `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`. The propositional connective is `[Not](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not") : Prop → Prop`.
Conventions for notations in identifiers:
  * The recommended spelling of `!` in identifiers is `[not](Basic-Types/Booleans/#Bool___not "Documentation for Bool.not")`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bool.and "Permalink")def
```


Bool.and (x y : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Bool.and (x y : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Boolean “and”, also known as conjunction. `[and](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") x y` can be written `x && y`.
The corresponding propositional connective is `[And](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") : Prop → Prop → Prop`, written with the `∧` operator.
The Boolean `[and](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")` is a `@[macro_inline]` function in order to give it short-circuiting evaluation: if `x` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` then `y` is not evaluated at runtime.
Conventions for notations in identifiers:
  * The recommended spelling of `&&` in identifiers is `[and](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")`.
  * The recommended spelling of `||` in identifiers is `[or](Basic-Types/Booleans/#Bool___or "Documentation for Bool.or")`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bool.or "Permalink")def
```


Bool.or (x y : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Bool.or (x y : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Boolean “or”, also known as disjunction. `[or](Basic-Types/Booleans/#Bool___or "Documentation for Bool.or") x y` can be written `x || y`.
The corresponding propositional connective is `[Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") : Prop → Prop → Prop`, written with the `∨` operator.
The Boolean `[or](Basic-Types/Booleans/#Bool___or "Documentation for Bool.or")` is a `@[macro_inline]` function in order to give it short-circuiting evaluation: if `x` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` then `y` is not evaluated at runtime.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bool.xor "Permalink")def
```


Bool.xor : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Bool.xor : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Boolean “exclusive or”. `[xor](Basic-Types/Booleans/#Bool___xor "Documentation for Bool.xor") x y` can be written `x ^^ y`.
`x ^^ y` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` when precisely one of `x` or `y` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`. Unlike `[and](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")` and `[or](Basic-Types/Booleans/#Bool___or "Documentation for Bool.or")`, it does not have short-circuiting behavior, because one argument's value never determines the final value. Also unlike `[and](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")` and `[or](Basic-Types/Booleans/#Bool___or "Documentation for Bool.or")`, there is no commonly-used corresponding propositional connective.
Examples:
  * `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") ^^ [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") ^^ [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") ^^ [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") ^^ [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


Conventions for notations in identifiers:
  * The recommended spelling of `^^` in identifiers is `[xor](Basic-Types/Booleans/#Bool___xor "Documentation for Bool.xor")`.


###  20.11.4.2. Comparisons[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Booleans--API-Reference--Comparisons "Permalink")
Most comparisons on Booleans should be performed using the `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`, `[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`, `[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` instances.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bool.decEq "Permalink")def
```


Bool.decEq (a b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


Bool.decEq (a b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


```

Decides whether two Booleans are equal.
This function should normally be called via the `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` instance that it exists to support.
###  20.11.4.3. Conversions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Booleans--API-Reference--Conversions "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bool.toISize "Permalink")def
```


Bool.toISize (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


Bool.toISize (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [ISize](Basic-Types/Fixed-Precision-Integers/#ISize___ofUSize "Documentation for ISize")


```

Converts `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` to `1` and `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` to `0`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bool.toUInt8 "Permalink")def
```


Bool.toUInt8 (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


Bool.toUInt8 (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Converts `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` to `1` and `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` to `0`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bool.toUInt16 "Permalink")def
```


Bool.toUInt16 (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


Bool.toUInt16 (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [UInt16](Basic-Types/Fixed-Precision-Integers/#UInt16___ofBitVec "Documentation for UInt16")


```

Converts `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` to `1` and `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` to `0`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bool.toUInt32 "Permalink")def
```


Bool.toUInt32 (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


Bool.toUInt32 (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Converts `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` to `1` and `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` to `0`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bool.toUInt64 "Permalink")def
```


Bool.toUInt64 (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


Bool.toUInt64 (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Converts `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` to `1` and `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` to `0`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bool.toUSize "Permalink")def
```


Bool.toUSize (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


Bool.toUSize (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Converts `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` to `1` and `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` to `0`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bool.toInt8 "Permalink")def
```


Bool.toInt8 (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


Bool.toInt8 (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Int8](Basic-Types/Fixed-Precision-Integers/#Int8___ofUInt8 "Documentation for Int8")


```

Converts `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` to `1` and `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` to `0`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bool.toInt16 "Permalink")def
```


Bool.toInt16 (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


Bool.toInt16 (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Int16](Basic-Types/Fixed-Precision-Integers/#Int16___ofUInt16 "Documentation for Int16")


```

Converts `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` to `1` and `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` to `0`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bool.toInt32 "Permalink")def
```


Bool.toInt32 (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


Bool.toInt32 (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Int32](Basic-Types/Fixed-Precision-Integers/#Int32___ofUInt32 "Documentation for Int32")


```

Converts `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` to `1` and `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` to `0`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bool.toInt64 "Permalink")def
```


Bool.toInt64 (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


Bool.toInt64 (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Int64](Basic-Types/Fixed-Precision-Integers/#Int64___ofUInt64 "Documentation for Int64")


```

Converts `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` to `1` and `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` to `0`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bool.toNat "Permalink")def
```


Bool.toNat (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Bool.toNat (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Converts `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` to `1` and `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` to `0`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bool.toInt "Permalink")def
```


Bool.toInt (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


Bool.toInt (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Converts `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` to `1` and `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` to `0`.
[←20.10. The Empty Type](Basic-Types/The-Empty-Type/#empty "20.10. The Empty Type")[20.12. Optional Values→](Basic-Types/Optional-Values/#option "20.12. Optional Values")

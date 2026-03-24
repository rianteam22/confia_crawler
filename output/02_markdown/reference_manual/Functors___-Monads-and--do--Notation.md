[←17.5. Proof Mode](The--mvcgen--tactic/Proof-Mode/#mvcgen-proof-mode "17.5. Proof Mode")[18.1. Laws→](Functors___-Monads-and--do--Notation/Laws/#monad-laws "18.1. Laws")
#  18. Functors, Monads and `do`-Notation[🔗](find/?domain=Verso.Genre.Manual.section&name=monads-and-do "Permalink")
The type classes `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor")`, `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")`, and `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")` provide fundamental tools for functional programming.An introduction to programming with these abstractions is available in [_Functional Programming in Lean_](https://lean-lang.org/functional_programming_in_lean/functor-applicative-monad.html). While they are inspired by the concepts of functors and monads in category theory, the versions used for programming are more limited. The type classes in Lean's standard library represent the concepts as used for programming, rather than the general mathematical definition.
Instances of `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor")` allow an operation to be applied consistently throughout some polymorphic context. Examples include transforming each element of a list by applying a function and creating new `[IO](IO/Logical-Model/#IO "Documentation for IO")` actions by arranging for a pure function to be applied to the result of an existing `[IO](IO/Logical-Model/#IO "Documentation for IO")` action. Instances of `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")` allow side effects with data dependencies to be encoded; examples include using a tuple to simulate mutable state, a sum type to simulate exceptions, and representing actual side effects with `[IO](IO/Logical-Model/#IO "Documentation for IO")`. `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")` functors occupy a middle ground: like monads, they allow functions computed with effects to be applied to arguments that are computed with effects, but they do not allow sequential data dependencies where the output of an effect forms an input into another effectful operation.
The additional type classes `[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure")`, `[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind")`, `[SeqLeft](Functors___-Monads-and--do--Notation/#SeqLeft___mk "Documentation for SeqLeft")`, `[SeqRight](Functors___-Monads-and--do--Notation/#SeqRight___mk "Documentation for SeqRight")`, and `[Seq](Functors___-Monads-and--do--Notation/#Seq___mk "Documentation for Seq")` capture individual operations from `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")` and `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")`, allowing them to be overloaded and used with types that are not necessarily `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")` functors or `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")`s. The `[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative")` type class describes applicative functors that additionally have some notion of failure and recovery.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Functor "Permalink")type class
```


Functor.{u, v} (f : Type u → Type v) : Type (max (u + 1) v)


Functor.{u, v} (f : Type u → Type v) :
  Type (max (u + 1) v)


```

A functor in the sense used in functional programming, which means a function `f : Type u → Type v` has a way of mapping a function over its contents. This `map` operator is written `<$>`, and overloaded via `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor")` instances.
This `map` function should respect identity and function composition. In other words, for all terms `v : f α`, it should be the case that:
  * `id <$> v = v`
  * For all functions `h : β → γ` and `g : α → β`, `(h ∘ g) <$> v = h <$> g <$> v`


While all `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor")` instances should live up to these requirements, they are not required to _prove_ that they do. Proofs may be required or provided via the `[LawfulFunctor](Functors___-Monads-and--do--Notation/Laws/#LawfulFunctor___mk "Documentation for LawfulFunctor")` class.
Assuming that instances are lawful, this definition corresponds to the category-theoretic notion of [functor](https://en.wikipedia.org/wiki/Functor) in the special case where the category is the category of types and functions between them.
#  Instance Constructor

```
[Functor.mk](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.mk").{u, v}
```

#  Methods

```
map : {α β : Type u} → (α → β) → f α → f β
```

Applies a function inside a functor. This is used to overload the `<$>` operator.
When mapping a constant function, use `[Functor.mapConst](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.mapConst")` instead, because it may be more efficient.
Conventions for notations in identifiers:
  * The recommended spelling of `<$>` in identifiers is `map`.



```
mapConst : {α β : Type u} → α → f β → f α
```

Mapping a constant function.
Given `a : α` and `v : f α`, `mapConst a v` is equivalent to `[Function.const](The-Type-System/Functions/#Function___const "Documentation for Function.const") _ a <$> v`. For some functors, this can be implemented more efficiently; for all other functors, the default implementation may be used.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Pure "Permalink")type class
```


Pure.{u, v} (f : Type u → Type v) : Type (max (u + 1) v)


Pure.{u, v} (f : Type u → Type v) :
  Type (max (u + 1) v)


```

The `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` function is overloaded via `[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure")` instances.
`[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure")` is typically accessed via `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")` or `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")` instances.
#  Instance Constructor

```
[Pure.mk](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.mk").{u, v}
```

#  Methods

```
pure : {α : Type u} → α → f α
```

Given `a : α`, then `pure a : f α` represents an action that does nothing and returns `a`.
Examples:
  * `(pure "hello" : Option String) = some "hello"`
  * `(pure "hello" : Except (Array String) String) = Except.ok "hello"`
  * `(pure "hello" : StateM Nat String).run 105 = ("hello", 105)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Seq.mk "Permalink")type class
```


Seq.{u, v} (f : Type u → Type v) : Type (max (u + 1) v)


Seq.{u, v} (f : Type u → Type v) :
  Type (max (u + 1) v)


```

The `<*>` operator is overloaded using the function `[Seq.seq](Functors___-Monads-and--do--Notation/#Seq___mk "Documentation for Seq.seq")`.
While `<$>` from the class `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor")` allows an ordinary function to be mapped over its contents, `<*>` allows a function that's “inside” the functor to be applied. When thinking about `f` as possible side effects, this captures evaluation order: `seq` arranges for the effects that produce the function to occur prior to those that produce the argument value.
For most applications, `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")` or `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")` should be used rather than `[Seq](Functors___-Monads-and--do--Notation/#Seq___mk "Documentation for Seq")` itself.
#  Instance Constructor

```
[Seq.mk](Functors___-Monads-and--do--Notation/#Seq___mk "Documentation for Seq.mk").{u, v}
```

#  Methods

```
seq : {α β : Type u} → f (α → β) → ([Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → f α) → f β
```

The implementation of the `<*>` operator.
In a monad, `mf <*> mx` is the same as `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let f ← mf; x ← mx; pure (f x)`: it evaluates the function first, then the argument, and applies one to the other.
To avoid surprising evaluation semantics, `mx` is taken "lazily", using a `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → f α` function.
Conventions for notations in identifiers:
  * The recommended spelling of `<*>` in identifiers is `seq`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=SeqLeft "Permalink")type class
```


SeqLeft.{u, v} (f : Type u → Type v) : Type (max (u + 1) v)


SeqLeft.{u, v} (f : Type u → Type v) :
  Type (max (u + 1) v)


```

The `<*` operator is overloaded using `seqLeft`.
When thinking about `f` as potential side effects, `<*` evaluates first the left and then the right argument for their side effects, discarding the value of the right argument and returning the value of the left argument.
For most applications, `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")` or `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")` should be used rather than `[SeqLeft](Functors___-Monads-and--do--Notation/#SeqLeft___mk "Documentation for SeqLeft")` itself.
#  Instance Constructor

```
[SeqLeft.mk](Functors___-Monads-and--do--Notation/#SeqLeft___mk "Documentation for SeqLeft.mk").{u, v}
```

#  Methods

```
seqLeft : {α β : Type u} → f α → ([Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → f β) → f α
```

Sequences the effects of two terms, discarding the value of the second. This function is usually invoked via the `<*` operator.
Given `x : f α` and `y : f β`, `x <* y` runs `x`, then runs `y`, and finally returns the result of `x`.
The evaluation of the second argument is delayed by wrapping it in a function, enabling “short-circuiting” behavior from `f`.
Conventions for notations in identifiers:
  * The recommended spelling of `<*` in identifiers is `seqLeft`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=SeqRight "Permalink")type class
```


SeqRight.{u, v} (f : Type u → Type v) : Type (max (u + 1) v)


SeqRight.{u, v} (f : Type u → Type v) :
  Type (max (u + 1) v)


```

The `*>` operator is overloaded using `seqRight`.
When thinking about `f` as potential side effects, `*>` evaluates first the left and then the right argument for their side effects, discarding the value of the left argument and returning the value of the right argument.
For most applications, `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")` or `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")` should be used rather than `[SeqRight](Functors___-Monads-and--do--Notation/#SeqRight___mk "Documentation for SeqRight")` itself.
#  Instance Constructor

```
[SeqRight.mk](Functors___-Monads-and--do--Notation/#SeqRight___mk "Documentation for SeqRight.mk").{u, v}
```

#  Methods

```
seqRight : {α β : Type u} → f α → ([Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → f β) → f β
```

Sequences the effects of two terms, discarding the value of the first. This function is usually invoked via the `*>` operator.
Given `x : f α` and `y : f β`, `x *> y` runs `x`, then runs `y`, and finally returns the result of `y`.
The evaluation of the second argument is delayed by wrapping it in a function, enabling “short-circuiting” behavior from `f`.
Conventions for notations in identifiers:
  * The recommended spelling of `*>` in identifiers is `seqRight`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Applicative.mk "Permalink")type class
```


Applicative.{u, v} (f : Type u → Type v) : Type (max (u + 1) v)


Applicative.{u, v} (f : Type u → Type v) :
  Type (max (u + 1) v)


```

An [applicative functor](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=monads-and-do) is more powerful than a `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor")`, but less powerful than a `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")`.
Applicative functors capture sequencing of effects with the `<*>` operator, overloaded as `seq`, but not data-dependent effects. The results of earlier computations cannot be used to control later effects.
Applicative functors should satisfy four laws. Instances of `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")` are not required to prove that they satisfy these laws, which are part of the `[LawfulApplicative](Functors___-Monads-and--do--Notation/Laws/#LawfulApplicative___mk "Documentation for LawfulApplicative")` class.
#  Instance Constructor

```
[Applicative.mk](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative.mk").{u, v}
```

#  Extends
  * `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") f`
  * `[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") f`
  * `[Seq](Functors___-Monads-and--do--Notation/#Seq___mk "Documentation for Seq") f`
  * `[SeqLeft](Functors___-Monads-and--do--Notation/#SeqLeft___mk "Documentation for SeqLeft") f`
  * `[SeqRight](Functors___-Monads-and--do--Notation/#SeqRight___mk "Documentation for SeqRight") f`


#  Methods

```
map : {α β : Type u} → (α → β) → f α → f β
```

Inherited from 
  1. `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") f`
  2. `[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") f`
  3. `[Seq](Functors___-Monads-and--do--Notation/#Seq___mk "Documentation for Seq") f`
  4. `[SeqLeft](Functors___-Monads-and--do--Notation/#SeqLeft___mk "Documentation for SeqLeft") f`
  5. `[SeqRight](Functors___-Monads-and--do--Notation/#SeqRight___mk "Documentation for SeqRight") f`



```
mapConst : {α β : Type u} → α → f β → f α
```

Inherited from 
  1. `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") f`
  2. `[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") f`
  3. `[Seq](Functors___-Monads-and--do--Notation/#Seq___mk "Documentation for Seq") f`
  4. `[SeqLeft](Functors___-Monads-and--do--Notation/#SeqLeft___mk "Documentation for SeqLeft") f`
  5. `[SeqRight](Functors___-Monads-and--do--Notation/#SeqRight___mk "Documentation for SeqRight") f`



```
pure : {α : Type u} → α → f α
```

Inherited from 
  1. `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") f`
  2. `[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") f`
  3. `[Seq](Functors___-Monads-and--do--Notation/#Seq___mk "Documentation for Seq") f`
  4. `[SeqLeft](Functors___-Monads-and--do--Notation/#SeqLeft___mk "Documentation for SeqLeft") f`
  5. `[SeqRight](Functors___-Monads-and--do--Notation/#SeqRight___mk "Documentation for SeqRight") f`



```
seq : {α β : Type u} → f (α → β) → ([Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → f α) → f β
```

Inherited from 
  1. `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") f`
  2. `[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") f`
  3. `[Seq](Functors___-Monads-and--do--Notation/#Seq___mk "Documentation for Seq") f`
  4. `[SeqLeft](Functors___-Monads-and--do--Notation/#SeqLeft___mk "Documentation for SeqLeft") f`
  5. `[SeqRight](Functors___-Monads-and--do--Notation/#SeqRight___mk "Documentation for SeqRight") f`



```
seqLeft : {α β : Type u} → f α → ([Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → f β) → f α
```

Inherited from 
  1. `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") f`
  2. `[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") f`
  3. `[Seq](Functors___-Monads-and--do--Notation/#Seq___mk "Documentation for Seq") f`
  4. `[SeqLeft](Functors___-Monads-and--do--Notation/#SeqLeft___mk "Documentation for SeqLeft") f`
  5. `[SeqRight](Functors___-Monads-and--do--Notation/#SeqRight___mk "Documentation for SeqRight") f`



```
seqRight : {α β : Type u} → f α → ([Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → f β) → f β
```

Inherited from 
  1. `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") f`
  2. `[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") f`
  3. `[Seq](Functors___-Monads-and--do--Notation/#Seq___mk "Documentation for Seq") f`
  4. `[SeqLeft](Functors___-Monads-and--do--Notation/#SeqLeft___mk "Documentation for SeqLeft") f`
  5. `[SeqRight](Functors___-Monads-and--do--Notation/#SeqRight___mk "Documentation for SeqRight") f`


Lists with Lengths as Applicative Functors
The structure `[LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example")` pairs a list with a proof that it has the desired length. As a consequence, its `zipWith` operator doesn't require a fallback in case the lengths of its inputs differ.
`structure LenList (length : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (α : Type u) where   list : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α   lengthOk : list.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") = length  def LenList.head (xs : [LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") (n + 1) α) : α :=   xs.[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example").[head](Basic-Types/Linked-Lists/#List___head "Documentation for List.head") <| byα:Type uβ:Type un:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")xs:[LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") α⊢ xs.[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") ≠ [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")     [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") hα:Type uβ:Type un:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")xs:[LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") αh:xs.[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")     [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") xsmkα:Type uβ:Type un:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")list✝:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") αlengthOk✝:list✝.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1h:{ [list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") := list✝, [lengthOk](Functors___-Monads-and--do--Notation/#LenList___lengthOk-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") := lengthOk✝ }.[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")     [simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic")mkα:Type uβ:Type un:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")list✝:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") αlengthOk✝:list✝.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1h:list✝ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")     [subst_eqs](Tactic-Proofs/Tactic-Reference/#subst_eqs "Documentation for tactic")All goals completed! 🐙  def LenList.tail (xs : [LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") (n + 1) α) : [LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") n α :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") xs [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | ⟨_ :: xs', _⟩ => ⟨xs', byα:Type uβ:Type un:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")xs:[LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") αhead✝:αxs':[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") αlengthOk✝:[(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")head✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs'[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1⊢ xs'.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n [simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic")All goals completed! 🐙⟩  def LenList.map (f : α → β) (xs : [LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") n α) : [LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") n β where   [list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") := xs.[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example").[map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map") f   [lengthOk](Functors___-Monads-and--do--Notation/#LenList___lengthOk-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") := byα:Type uβ:Type un:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")f:α → βxs:[LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") n α⊢ ([List.map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map") f xs.[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example")).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n     [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") xsmkα:Type uβ:Type un:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")f:α → βlist✝:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") αlengthOk✝:list✝.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n⊢ ([List.map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map") f { [list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") := list✝, [lengthOk](Functors___-Monads-and--do--Notation/#LenList___lengthOk-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") := lengthOk✝ }.[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example")).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n     [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [List.length_map, *]All goals completed! 🐙  def LenList.zipWith (f : α → β → γ)     (xs : [LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") n α) (ys : [LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") n β) :     [LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") n γ where   [list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") := xs.[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example").[zipWith](Basic-Types/Linked-Lists/#List___zipWith "Documentation for List.zipWith") f ys.[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example")   [lengthOk](Functors___-Monads-and--do--Notation/#LenList___lengthOk-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") := byα:Type uβ:Type uγ:Type ?u.1796n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")f:α → β → γxs:[LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") n αys:[LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") n β⊢ ([List.zipWith](Basic-Types/Linked-Lists/#List___zipWith "Documentation for List.zipWith") f xs.[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") ys.[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example")).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n     [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") xsmkα:Type uβ:Type uγ:Type ?u.1796n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")f:α → β → γys:[LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") n βlist✝:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") αlengthOk✝:list✝.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n⊢ ([List.zipWith](Basic-Types/Linked-Lists/#List___zipWith "Documentation for List.zipWith") f { [list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") := list✝, [lengthOk](Functors___-Monads-and--do--Notation/#LenList___lengthOk-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") := lengthOk✝ }.[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") ys.[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example")).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n; [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") ysmk.mkα:Type uβ:Type uγ:Type ?u.1796n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")f:α → β → γlist✝¹:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") αlengthOk✝¹:list✝.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") nlist✝:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") βlengthOk✝:list✝.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n⊢ ([List.zipWith](Basic-Types/Linked-Lists/#List___zipWith "Documentation for List.zipWith") f { [list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") := list✝¹, [lengthOk](Functors___-Monads-and--do--Notation/#LenList___lengthOk-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") := lengthOk✝¹ }.[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") { [list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") := list✝, [lengthOk](Functors___-Monads-and--do--Notation/#LenList___lengthOk-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") := lengthOk✝ }.[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example")).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")   n     [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [List.length_zipWith, *]All goals completed! 🐙 `
The well-behaved `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")` instance applies functions to arguments element-wise. Because `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")` extends `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor")`, a separate `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor")` instance is not necessary, and `[map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map")` can be defined as part of the `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")` instance.
`instance : [Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") ([LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") n) where   [map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") := [LenList.map](Functors___-Monads-and--do--Notation/#LenList___map-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example")   [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x := {     [list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") := [List.replicate](Basic-Types/Linked-Lists/#List___replicate "Documentation for List.replicate") n x     [lengthOk](Functors___-Monads-and--do--Notation/#LenList___lengthOk-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") := List.length_replicate   }   [seq](Functors___-Monads-and--do--Notation/#Seq___mk "Documentation for Seq.seq") {α β} fs xs := fs.[zipWith](Functors___-Monads-and--do--Notation/#LenList___zipWith-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") (· ·) (xs ()) `
The well-behaved `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")` instance takes the diagonal of the results of applying the function:
`@[simp] theorem LenList.list_length_eq (xs : [LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") n α) :     xs.[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") = n := byα:Type un:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")xs:[LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") n α⊢ xs.[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n   [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") xsmkα:Type un:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")list✝:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") αlengthOk✝:list✝.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n⊢ { [list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") := list✝, [lengthOk](Functors___-Monads-and--do--Notation/#LenList___lengthOk-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") := lengthOk✝ }.[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n   [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [*]All goals completed! 🐙  def LenList.diagonal (square : [LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") n ([LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") n α)) : [LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") n α :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") n [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | 0 => ⟨[], [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")⟩   | n' + 1 => {     [list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") :=       square.[head](Functors___-Monads-and--do--Notation/#LenList___head-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example").[head](Functors___-Monads-and--do--Notation/#LenList___head-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") :: (square.[tail](Functors___-Monads-and--do--Notation/#LenList___tail-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example").[map](Functors___-Monads-and--do--Notation/#LenList___map-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") (·.[tail](Functors___-Monads-and--do--Notation/#LenList___tail-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example"))).[diagonal](Functors___-Monads-and--do--Notation/#LenList___diagonal-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example").[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example")     [lengthOk](Functors___-Monads-and--do--Notation/#LenList___lengthOk-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") := byα:Type uβ:Type un:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")square:[LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n' [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") ([LenList](Functors___-Monads-and--do--Notation/#LenList-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n' [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") α)⊢ [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")square.[head](Functors___-Monads-and--do--Notation/#LenList___head-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example").[head](Functors___-Monads-and--do--Notation/#LenList___head-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") ([diagonal](Functors___-Monads-and--do--Notation/#LenList___diagonal-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") ([map](Functors___-Monads-and--do--Notation/#LenList___map-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example") (fun x => x.[tail](Functors___-Monads-and--do--Notation/#LenList___tail-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example")) square.[tail](Functors___-Monads-and--do--Notation/#LenList___tail-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example"))).[list](Functors___-Monads-and--do--Notation/#LenList___list-_LPAR_in-Lists-with-Lengths-as-Applicative-Functors_RPAR_ "Definition of example")[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n' [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")All goals completed! 🐙   } `
[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgDLwHbIJakQCgDboDmIAFogFyIByAhiAJR6CNwJYgCoCeADkhEwHdS8BAChEifNhBssOZuMnEyAeQDWbKaAB0hNCXIBeJfrKjRAE3gAzFOjkhtw2hbwAPYLPvS8aRAGpEAEYmZiYqVgpDRQ9daSd4F0QAHgAfRAAjTkUJTDRwAHtEUhzEKFpgeE8PUuBMAFtuAH1afHxaiAzQJvgAR2BzK1tUDHiQWkx8d08qEYdfAODQ8LtRnD9I6Il6+ihyD0QBTDMJdMAL8ibKKg8AcgAaRCbAS/JEQwA+RDPbh6zEOsaWm0noMbKsHNodtw8LYIohAEmEiEATcBMXAHWbedaIMJeNYyPyIw7CMQSLQyKKIWKkiG0KHWRR6AzqSjGLKlcqVaoDCQSf5QgDa4IZZCakIeACoALog4YYxwAL0w3AA6sdyLgYVj4UitYBm4AYpVRMzBPg2KM4RrmJqR4VKlsxOsJIng9J85Mp8QVytViFs5rioHpylITPJrO5ZQqVQpwAA3BGOYhzbUGvzBUGmp6VWRxVLRHlQLQ0FAkFQAILcbhScogTAANyQuDteMEROd2xpzONOkhim4cCQbk7AG9SqTO+CEJXMNWkH43KOgyHjGnTKQmpOq/Q24gAL6KSq9RBD1iInc+zmd6zAbSZ724ADtiHvKIOuAY+tEAAE+bypWR4AUCD1F2jikk0Qprn00w4vMpqUKU7o6BBryIH4obZBI7JRjUPIpogfKStKIHaBYmC0EQBRoK0eDAL0EC0AgMFWo2sqoVi75MZimyKDsIB7GxRwnIg6QAAyvB8Zx8hKDxgNY+DAqcqE3IsQTiUeo6uls4Z/HRDHwAkLgGa4FBULgtH0Qg2jjJM1JQg+VkTPg74kWRFFUfg/ogAuq5LpknB/Cmig7kAA"\))
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Alternative.toApplicative "Permalink")type class
```


Alternative.{u, v} (f : Type u → Type v) : Type (max (u + 1) v)


Alternative.{u, v} (f : Type u → Type v) :
  Type (max (u + 1) v)


```

An `[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative")` functor is an `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")` functor that can "fail" or be "empty" and a binary operation `<|>` that “collects values” or finds the “left-most success”.
Important instances include
  * `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")`, where `failure := none` and `<|>` returns the left-most `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")`.
  * Parser combinators typically provide an `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")` instance for error-handling and backtracking.


Error recovery and state can interact subtly. For example, the implementation of `[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative")` for `[OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") ([StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id"))` keeps modifications made to the state while recovering from failure, while `[StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ ([OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id"))` discards them.
#  Instance Constructor

```
[Alternative.mk](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative.mk").{u, v}
```

#  Extends
  * `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") f`


#  Methods

```
map : {α β : Type u} → (α → β) → f α → f β
```

Inherited from 
  1. `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") f`



```
mapConst : {α β : Type u} → α → f β → f α
```

Inherited from 
  1. `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") f`



```
pure : {α : Type u} → α → f α
```

Inherited from 
  1. `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") f`



```
seq : {α β : Type u} → f (α → β) → ([Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → f α) → f β
```

Inherited from 
  1. `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") f`



```
seqLeft : {α β : Type u} → f α → ([Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → f β) → f α
```

Inherited from 
  1. `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") f`



```
seqRight : {α β : Type u} → f α → ([Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → f β) → f β
```

Inherited from 
  1. `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") f`



```
failure : {α : Type u} → f α
```

Produces an empty collection or recoverable failure. The `<|>` operator collects values or recovers from failures. See `[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative")` for more details.

```
orElse : {α : Type u} → f α → ([Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → f α) → f α
```

Depending on the `[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative")` instance, collects values or recovers from `failure`s by returning the leftmost success. Can be written using the `<|>` operator syntax.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bind "Permalink")type class
```


Bind.{u, v} (m : Type u → Type v) : Type (max (u + 1) v)


Bind.{u, v} (m : Type u → Type v) :
  Type (max (u + 1) v)


```

The `>>=` operator is overloaded via instances of `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")`.
`[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind")` is typically used via `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")`, which extends it.
#  Instance Constructor

```
[Bind.mk](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.mk").{u, v}
```

#  Methods

```
bind : {α β : Type u} → m α → (α → m β) → m β
```

Sequences two computations, allowing the second to depend on the value computed by the first.
If `x : m α` and `f : α → m β`, then `x >>= f : m β` represents the result of executing `x` to get a value of type `α` and then passing it to `f`.
Conventions for notations in identifiers:
  * The recommended spelling of `>>=` in identifiers is `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Monad.mk "Permalink")type class
```


Monad.{u, v} (m : Type u → Type v) : Type (max (u + 1) v)


Monad.{u, v} (m : Type u → Type v) :
  Type (max (u + 1) v)


```

[Monads](https://en.wikipedia.org/wiki/Monad_\(functional_programming\)) are an abstraction of sequential control flow and side effects used in functional programming. Monads allow both sequencing of effects and data-dependent effects: the values that result from an early step may influence the effects carried out in a later step.
The `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")` API may be used directly. However, it is most commonly accessed through [`do`-notation](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=do-notation).
Most `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")` instances provide implementations of `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` and `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")`, and use default implementations for the other methods inherited from `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")`. Monads should satisfy certain laws, but instances are not required to prove this. An instance of `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad")` expresses that a given monad's operations are lawful.
#  Instance Constructor

```
[Monad.mk](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad.mk").{u, v}
```

#  Extends
  * `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m`
  * `[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind") m`


#  Methods

```
map : {α β : Type u} → (α → β) → m α → m β
```

Inherited from 
  1. `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m`
  2. `[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind") m`



```
mapConst : {α β : Type u} → α → m β → m α
```

Inherited from 
  1. `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m`
  2. `[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind") m`



```
pure : {α : Type u} → α → m α
```

Inherited from 
  1. `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m`
  2. `[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind") m`



```
seq : {α β : Type u} → m (α → β) → ([Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → m α) → m β
```

Inherited from 
  1. `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m`
  2. `[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind") m`



```
seqLeft : {α β : Type u} → m α → ([Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → m β) → m α
```

Inherited from 
  1. `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m`
  2. `[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind") m`



```
seqRight : {α β : Type u} → m α → ([Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → m β) → m β
```

Inherited from 
  1. `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m`
  2. `[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind") m`



```
bind : {α β : Type u} → m α → (α → m β) → m β
```

Inherited from 
  1. `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m`
  2. `[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind") m`


  1. [18.1. Laws](Functors___-Monads-and--do--Notation/Laws/#monad-laws)
  2. [18.2. Lifting Monads](Functors___-Monads-and--do--Notation/Lifting-Monads/#lifting-monads)
  3. [18.3. Syntax](Functors___-Monads-and--do--Notation/Syntax/#The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Syntax)
  4. [18.4. API Reference](Functors___-Monads-and--do--Notation/API-Reference/#The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--API-Reference)
  5. [18.5. Varieties of Monads](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#monad-varieties)

[←17.5. Proof Mode](The--mvcgen--tactic/Proof-Mode/#mvcgen-proof-mode "17.5. Proof Mode")[18.1. Laws→](Functors___-Monads-and--do--Notation/Laws/#monad-laws "18.1. Laws")

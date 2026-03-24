[←18. Functors, Monads and do-Notation](Functors___-Monads-and--do--Notation/#monads-and-do "18. Functors, Monads and do-Notation")[18.2. Lifting Monads→](Functors___-Monads-and--do--Notation/Lifting-Monads/#lifting-monads "18.2. Lifting Monads")
#  18.1. Laws[🔗](find/?domain=Verso.Genre.Manual.section&name=monad-laws "Permalink")
Having `[map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map")`, `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")`, `[seq](Functors___-Monads-and--do--Notation/#Seq___mk "Documentation for Seq.seq")`, and `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")` operators with the appropriate types is not really sufficient to have a functor, applicative functor, or monad. These operators must additionally satisfy certain axioms, which are often called the _laws_ of the type class.
For a functor, the `[map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map")` operation must preserve identity and function composition. In other words, given a purported `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor")` `f`, for all `x`​`:`​`f α`:
  * `id <$> x = x`, and
  * for all function `g` and `h`, `(h ∘ g) <$> x = h <$> g <$> x`.


Instances that violate these assumptions can be very surprising! Additionally, because `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor")` includes `[mapConst](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.mapConst")` to enable instances to provide a more efficient implementation, a lawful functor's `[mapConst](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.mapConst")` should be equivalent to its default implementation.
The Lean standard library does not require proofs of these properties in every instance of `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor")`. Nonetheless, if an instance violates them, then it should be considered a bug. When proofs of these properties are necessary, an instance implicit parameter of type `[LawfulFunctor](Functors___-Monads-and--do--Notation/Laws/#LawfulFunctor___mk "Documentation for LawfulFunctor") f` can be used. The `[LawfulFunctor](Functors___-Monads-and--do--Notation/Laws/#LawfulFunctor___mk "Documentation for LawfulFunctor")` class includes the necessary proofs.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=LawfulFunctor.comp_map "Permalink")type class
```


LawfulFunctor.{u, v} (f : Type u → Type v) [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") f] : Prop


LawfulFunctor.{u, v} (f : Type u → Type v)
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") f] : Prop


```

A functor satisfies the functor laws.
The `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor")` class contains the operations of a functor, but does not require that instances prove they satisfy the laws of a functor. A `[LawfulFunctor](Functors___-Monads-and--do--Notation/Laws/#LawfulFunctor___mk "Documentation for LawfulFunctor")` instance includes proofs that the laws are satisfied. Because `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor")` instances may provide optimized implementations of `mapConst`, `[LawfulFunctor](Functors___-Monads-and--do--Notation/Laws/#LawfulFunctor___mk "Documentation for LawfulFunctor")` instances must also prove that the optimized implementation is equivalent to the standard implementation.
#  Instance Constructor

```
[LawfulFunctor.mk](Functors___-Monads-and--do--Notation/Laws/#LawfulFunctor___mk "Documentation for LawfulFunctor.mk").{u, v}
```

#  Methods

```
map_const : ∀ {α β : Type u}, [Functor.mapConst](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.mapConst") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Functor.map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") [∘](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [Function.const](The-Type-System/Functions/#Function___const "Documentation for Function.const") β
```

The `mapConst` implementation is equivalent to the default implementation.

```
id_map : ∀ {α : Type u} (x : f α), id [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x
```

The `map` implementation preserves identity.

```
comp_map : ∀ {α β γ : Type u} (g : α → β) (h : β → γ) (x : f α), [(](The-Type-System/Functions/#Function___comp "Documentation for Function.comp")h [∘](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") g[)](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") h [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") g [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x
```

The `map` implementation preserves function composition.
In addition to proving that the potentially-optimized `[SeqLeft.seqLeft](Functors___-Monads-and--do--Notation/#SeqLeft___mk "Documentation for SeqLeft.seqLeft")` and `[SeqRight.seqRight](Functors___-Monads-and--do--Notation/#SeqRight___mk "Documentation for SeqRight.seqRight")` operations are equivalent to their default implementations, Applicative functors `[f](releases/v4.27.0/#f "Definition of example")` must satisfy four laws.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=LawfulApplicative.mk "Permalink")type class
```


LawfulApplicative.{u, v} (f : Type u → Type v) [[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") f] : Prop


LawfulApplicative.{u, v}
  (f : Type u → Type v) [[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") f] :
  Prop


```

An applicative functor satisfies the laws of an applicative functor.
The `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")` class contains the operations of an applicative functor, but does not require that instances prove they satisfy the laws of an applicative functor. A `[LawfulApplicative](Functors___-Monads-and--do--Notation/Laws/#LawfulApplicative___mk "Documentation for LawfulApplicative")` instance includes proofs that the laws are satisfied.
Because `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")` instances may provide optimized implementations of `seqLeft` and `seqRight`, `[LawfulApplicative](Functors___-Monads-and--do--Notation/Laws/#LawfulApplicative___mk "Documentation for LawfulApplicative")` instances must also prove that the optimized implementation is equivalent to the standard implementation.
#  Instance Constructor

```
[LawfulApplicative.mk](Functors___-Monads-and--do--Notation/Laws/#LawfulApplicative___mk "Documentation for LawfulApplicative.mk").{u, v}
```

#  Extends
  * `[LawfulFunctor](Functors___-Monads-and--do--Notation/Laws/#LawfulFunctor___mk "Documentation for LawfulFunctor") f`


#  Methods

```
map_const : ∀ {α β : Type u}, [Functor.mapConst](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.mapConst") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Functor.map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") [∘](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [Function.const](The-Type-System/Functions/#Function___const "Documentation for Function.const") β
```

Inherited from 
  1. `[LawfulFunctor](Functors___-Monads-and--do--Notation/Laws/#LawfulFunctor___mk "Documentation for LawfulFunctor") f`



```
id_map : ∀ {α : Type u} (x : f α), id [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x
```

Inherited from 
  1. `[LawfulFunctor](Functors___-Monads-and--do--Notation/Laws/#LawfulFunctor___mk "Documentation for LawfulFunctor") f`



```
comp_map : ∀ {α β γ : Type u} (g : α → β) (h : β → γ) (x : f α), [(](The-Type-System/Functions/#Function___comp "Documentation for Function.comp")h [∘](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") g[)](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") h [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") g [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x
```

Inherited from 
  1. `[LawfulFunctor](Functors___-Monads-and--do--Notation/Laws/#LawfulFunctor___mk "Documentation for LawfulFunctor") f`



```
seqLeft_eq : ∀ {α β : Type u} (x : f α) (y : f β), x <* y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Function.const](The-Type-System/Functions/#Function___const "Documentation for Function.const") β [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x <*> y
```

`seqLeft` is equivalent to the default implementation.

```
seqRight_eq : ∀ {α β : Type u} (x : f α) (y : f β), x *> y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Function.const](The-Type-System/Functions/#Function___const "Documentation for Function.const") α id [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x <*> y
```

`seqRight` is equivalent to the default implementation.

```
pure_seq : ∀ {α β : Type u} (g : α → β) (x : f α), [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") g <*> x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x
```

`[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` before `seq` is equivalent to `[Functor.map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map")`.
This means that `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` really is pure when occurring immediately prior to `seq`.

```
map_pure : ∀ {α β : Type u} (g : α → β) (x : α), g [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") (g x)
```

Mapping a function over the result of `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` is equivalent to applying the function under `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")`.
This means that `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` really is pure with respect to `[Functor.map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map")`.

```
seq_pure : ∀ {α β : Type u} (g : f (α → β)) (x : α), g <*> [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") (fun h => h x) [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") g
```

`[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` after `seq` is equivalent to `[Functor.map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map")`.
This means that `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` really is pure when occurring just after `seq`.

```
seq_assoc : ∀ {α β γ : Type u} (x : f α) (g : f (α → β)) (h : f (β → γ)), h <*> (g <*> x) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Function.comp](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") h <*> g <*> x
```

`seq` is associative.
Changing the nesting of `seq` calls while maintaining the order of computations results in an equivalent computation. This means that `seq` is not doing any more than sequencing.
The monad laws specify that `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` followed by `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")` should be equivalent to function application (that is, `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` has no effects), that `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")` followed by `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` around a function application is equivalent to `[map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map")`, and that `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")` is associative.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=LawfulMonad.toLawfulApplicative "Permalink")type class
```


LawfulMonad.{u, v} (m : Type u → Type v) [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] : Prop


LawfulMonad.{u, v} (m : Type u → Type v)
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] : Prop


```

Lawful monads are those that satisfy a certain behavioral specification. While all instances of `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")` should satisfy these laws, not all implementations are required to prove this.
`[LawfulMonad.mk'](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk___ "Documentation for LawfulMonad.mk'")` is an alternative constructor that contains useful defaults for many fields.
#  Instance Constructor

```
[LawfulMonad.mk](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad.mk").{u, v}
```

#  Extends
  * `[LawfulApplicative](Functors___-Monads-and--do--Notation/Laws/#LawfulApplicative___mk "Documentation for LawfulApplicative") m`


#  Methods

```
map_const : ∀ {α β : Type u}, [Functor.mapConst](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.mapConst") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Functor.map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") [∘](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [Function.const](The-Type-System/Functions/#Function___const "Documentation for Function.const") β
```

Inherited from 
  1. `[LawfulApplicative](Functors___-Monads-and--do--Notation/Laws/#LawfulApplicative___mk "Documentation for LawfulApplicative") m`



```
id_map : ∀ {α : Type u} (x : m α), id [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x
```

Inherited from 
  1. `[LawfulApplicative](Functors___-Monads-and--do--Notation/Laws/#LawfulApplicative___mk "Documentation for LawfulApplicative") m`



```
comp_map : ∀ {α β γ : Type u} (g : α → β) (h : β → γ) (x : m α), [(](The-Type-System/Functions/#Function___comp "Documentation for Function.comp")h [∘](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") g[)](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") h [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") g [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x
```

Inherited from 
  1. `[LawfulApplicative](Functors___-Monads-and--do--Notation/Laws/#LawfulApplicative___mk "Documentation for LawfulApplicative") m`



```
seqLeft_eq : ∀ {α β : Type u} (x : m α) (y : m β), x <* y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Function.const](The-Type-System/Functions/#Function___const "Documentation for Function.const") β [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x <*> y
```

Inherited from 
  1. `[LawfulApplicative](Functors___-Monads-and--do--Notation/Laws/#LawfulApplicative___mk "Documentation for LawfulApplicative") m`



```
seqRight_eq : ∀ {α β : Type u} (x : m α) (y : m β), x *> y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Function.const](The-Type-System/Functions/#Function___const "Documentation for Function.const") α id [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x <*> y
```

Inherited from 
  1. `[LawfulApplicative](Functors___-Monads-and--do--Notation/Laws/#LawfulApplicative___mk "Documentation for LawfulApplicative") m`



```
pure_seq : ∀ {α β : Type u} (g : α → β) (x : m α), [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") g <*> x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x
```

Inherited from 
  1. `[LawfulApplicative](Functors___-Monads-and--do--Notation/Laws/#LawfulApplicative___mk "Documentation for LawfulApplicative") m`



```
map_pure : ∀ {α β : Type u} (g : α → β) (x : α), g [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") (g x)
```

Inherited from 
  1. `[LawfulApplicative](Functors___-Monads-and--do--Notation/Laws/#LawfulApplicative___mk "Documentation for LawfulApplicative") m`



```
seq_pure : ∀ {α β : Type u} (g : m (α → β)) (x : α), g <*> [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") (fun h => h x) [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") g
```

Inherited from 
  1. `[LawfulApplicative](Functors___-Monads-and--do--Notation/Laws/#LawfulApplicative___mk "Documentation for LawfulApplicative") m`



```
seq_assoc : ∀ {α β γ : Type u} (x : m α) (g : m (α → β)) (h : m (β → γ)), h <*> (g <*> x) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Function.comp](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") h <*> g <*> x
```

Inherited from 
  1. `[LawfulApplicative](Functors___-Monads-and--do--Notation/Laws/#LawfulApplicative___mk "Documentation for LawfulApplicative") m`



```
bind_pure_comp : ∀ {α β : Type u} (f : α → β) (x : m α),
  (do
      let a ← x
      [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") (f a)) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
    f [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x
```

A `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")` followed by `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` composed with a function is equivalent to a functorial map.
This means that `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` really is pure after a `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")` and has no effects.

```
bind_map : ∀ {α β : Type u} (f : m (α → β)) (x : m α),
  (do
      let x_1 ← f
      x_1 [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
    f <*> x
```

A `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")` followed by a functorial map is equivalent to `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")` sequencing.
This means that the effect sequencing from `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")` and `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")` are the same.

```
pure_bind : ∀ {α β : Type u} (x : α) (f : α → m β), [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") f [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f x
```

`[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` followed by `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")` is equivalent to function application.
This means that `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` really is pure before a `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")` and has no effects.

```
bind_assoc : ∀ {α β γ : Type u} (x : m α) (f : α → m β) (g : β → m γ), x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") f [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") g [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") fun x => f x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") g
```

`[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")` is associative.
Changing the nesting of `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")` calls while maintaining the order of computations results in an equivalent computation. This means that `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")` is not doing more than data-dependent sequencing.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=LawfulMonad.mk' "Permalink")theorem
```


LawfulMonad.mk'.{u, v} (m : Type u → Type v) [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (id_map : ∀ {α : Type u} (x : m α), id [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x)
  (pure_bind :
    ∀ {α β : Type u} (x : α) (f : α → m β), [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") f [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f x)
  (bind_assoc :
    ∀ {α β γ : Type u} (x : m α) (f : α → m β) (g : β → m γ),
      x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") f [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") g [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") fun x => f x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") g)
  (map_const :
    ∀ {α β : Type u} (x : α) (y : m β),
      [Functor.mapConst](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.mapConst") x y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Function.const](The-Type-System/Functions/#Function___const "Documentation for Function.const") β x [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") y := by
    intros; rfl)
  (seqLeft_eq :
    ∀ {α β : Type u} (x : m α) (y : m β),
      x <* y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") do
        let a ← x
        let _ ← y
        [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") a := by
    intros; rfl)
  (seqRight_eq :
    ∀ {α β : Type u} (x : m α) (y : m β),
      x *> y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") do
        let _ ← x
        y := by
    intros; rfl)
  (bind_pure_comp :
    ∀ {α β : Type u} (f : α → β) (x : m α),
      (do
          let y ← x
          [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") (f y)) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
        f [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x := by
    intros; rfl)
  (bind_map :
    ∀ {α β : Type u} (f : m (α → β)) (x : m α),
      (do
          let x_1 ← f
          x_1 [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
        f <*> x := by
    intros; rfl) :
  [LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") m


LawfulMonad.mk'.{u, v}
  (m : Type u → Type v) [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (id_map :
    ∀ {α : Type u} (x : m α),
      id [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x)
  (pure_bind :
    ∀ {α β : Type u} (x : α)
      (f : α → m β), [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") f [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f x)
  (bind_assoc :
    ∀ {α β γ : Type u} (x : m α)
      (f : α → m β) (g : β → m γ),
      x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") f [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") g [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
        x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") fun x => f x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") g)
  (map_const :
    ∀ {α β : Type u} (x : α) (y : m β),
      [Functor.mapConst](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.mapConst") x y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
        [Function.const](The-Type-System/Functions/#Function___const "Documentation for Function.const") β x [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") y := by
    intros; rfl)
  (seqLeft_eq :
    ∀ {α β : Type u} (x : m α) (y : m β),
      x <* y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") do
        let a ← x
        let _ ← y
        [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") a := by
    intros; rfl)
  (seqRight_eq :
    ∀ {α β : Type u} (x : m α) (y : m β),
      x *> y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") do
        let _ ← x
        y := by
    intros; rfl)
  (bind_pure_comp :
    ∀ {α β : Type u} (f : α → β)
      (x : m α),
      (do
          let y ← x
          [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") (f y)) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
        f [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x := by
    intros; rfl)
  (bind_map :
    ∀ {α β : Type u} (f : m (α → β))
      (x : m α),
      (do
          let x_1 ← f
          x_1 [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
        f <*> x := by
    intros; rfl) :
  [LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") m


```

An alternative constructor for `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad")` which has more defaultable fields in the common case.
[←18. Functors, Monads and do-Notation](Functors___-Monads-and--do--Notation/#monads-and-do "18. Functors, Monads and do-Notation")[18.2. Lifting Monads→](Functors___-Monads-and--do--Notation/Lifting-Monads/#lifting-monads "18.2. Lifting Monads")

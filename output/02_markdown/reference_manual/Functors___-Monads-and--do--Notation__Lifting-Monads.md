[←18.1. Laws](Functors___-Monads-and--do--Notation/Laws/#monad-laws "18.1. Laws")[18.3. Syntax→](Functors___-Monads-and--do--Notation/Syntax/#The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Syntax "18.3. Syntax")
#  18.2. Lifting Monads[🔗](find/?domain=Verso.Genre.Manual.section&name=lifting-monads "Permalink")
When one monad is at least as capable as another, then actions from the latter monad can be used in a context that expects actions from the former. This is called _lifting_ the action from one monad to another. Lean automatically inserts lifts when they are available; lifts are defined in the `[MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift")` type class. Automatic monad lifting is attempted before the general [coercion](Coercions/#--tech-term-coercion) mechanism.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadLift "Permalink")type class
```


MonadLift.{u, v, w} (m : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Type u → Type v))
  (n : Type u → Type w) : Type (max (max (u + 1) v) w)


MonadLift.{u, v, w}
  (m : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Type u → Type v))
  (n : Type u → Type w) :
  Type (max (max (u + 1) v) w)


```

Computations in the monad `m` can be run in the monad `n`. These translations are inserted automatically by the compiler.
Usually, `n` consists of some number of monad transformers applied to `m`, but this is not mandatory.
New instances should use this class, `[MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift")`. Clients that require one monad to be liftable into another should instead request `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT")`, which is the reflexive, transitive closure of `[MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift")`.
#  Instance Constructor

```
[MonadLift.mk](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift.mk").{u, v, w}
```

#  Methods

```
monadLift : {α : Type u} → m α → n α
```

Translates an action from monad `m` into monad `n`.
[Lifting](Functors___-Monads-and--do--Notation/Lifting-Monads/#--tech-term-lifting) between monads is reflexive and transitive:
  * Any monad can run its own actions.
  * Lifts from `m` to `m'` and from `m'` to `n` can be composed to yield a lift from `m` to `n`. The utility type class `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT")` constructs lifts via the reflexive and transitive closure of `[MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift")` instances. Users should not define new instances of `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT")`, but it is useful as an instance implicit parameter to a polymorphic function that needs to run actions from multiple monads in some user-provided monad.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadLiftT.monadLift "Permalink")type class
```


MonadLiftT.{u, v, w} (m : Type u → Type v) (n : Type u → Type w) :
  Type (max (max (u + 1) v) w)


MonadLiftT.{u, v, w} (m : Type u → Type v)
  (n : Type u → Type w) :
  Type (max (max (u + 1) v) w)


```

Computations in the monad `m` can be run in the monad `n`. These translations are inserted automatically by the compiler.
Usually, `n` consists of some number of monad transformers applied to `m`, but this is not mandatory.
This is the reflexive, transitive closure of `[MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift")`. Clients that require one monad to be liftable into another should request an instance of `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT")`. New instances should instead be defined for `[MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift")` itself.
#  Instance Constructor

```
[MonadLiftT.mk](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT.mk").{u, v, w}
```

#  Methods

```
monadLift : {α : Type u} → m α → n α
```

Translates an action from monad `m` into monad `n`.
Monad Lifts in Function Signatures
The function `[IO.withStdin](IO/Files___-File-Handles___-and-Streams/#IO___withStdin "Documentation for IO.withStdin")` has the following signature:
`[IO.withStdin](IO/Files___-File-Handles___-and-Streams/#IO___withStdin "Documentation for IO.withStdin").{u} {m : Type → Type u} {α : Type}   [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[MonadFinally](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally") m] [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") m]   (h : [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")) (x : m α) :   m α`
Because it doesn't require its parameter to precisely be in `[IO](IO/Logical-Model/#IO "Documentation for IO")`, it can be used in many monads, and the body does not need to restrict itself to `[IO](IO/Logical-Model/#IO "Documentation for IO")`. The instance implicit parameter `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") m` allows the reflexive transitive closure of `[MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift")` to be used to assemble the lift.
When a term of type `n β` is expected, but the provided term has type `m α`, and the two types are not definitionally equal, Lean attempts to insert lifts and coercions before reporting an error. There are the following possibilities:
  1. If `m` and `n` can be unified to the same monad, then `α` and `β` are not the same. In this case, no monad lifts are necessary, but the value in the monad must be [coerced](Coercions/#--tech-term-coercion). If the appropriate coercion is found, then a call to `Lean.Internal.coeM` is inserted, which has the following signature:
`Lean.Internal.coeM.{u, v} {m : Type u → Type v} {α β : Type u}   [(a : α) → [CoeT](Coercions/Coercing-Between-Types/#CoeT___mk "Documentation for CoeT") α a β] [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]   (x : m α) :   m β`
  2. If `α` and `β` can be unified, then the monads differ. In this case, a monad lift is necessary to transform an expression with type `m α` to `n α`. If `m` can be lifted to `n` (that is, there is an instance of `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n`) then a call to `liftM`, which is an alias for `[MonadLiftT.monadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT.monadLift")`, is inserted.
`liftM.{u, v, w}   {m : Type u → Type v} {n : Type u → Type w}   [self : [MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n] {α : Type u} :   m α → n α`
  3. If neither `m` and `n` nor `α` and `β` can be unified, but `m` can be lifted into `n` and `α` can be [coerced](Coercions/#--tech-term-coercion) to `β`, then a lift and a coercion can be combined. This is done by inserting a call to `Lean.Internal.liftCoeM`:
`Lean.Internal.liftCoeM.{u, v, w}   {m : Type u → Type v} {n : Type u → Type w}   {α β : Type u}   [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n] [(a : α) → [CoeT](Coercions/Coercing-Between-Types/#CoeT___mk "Documentation for CoeT") α a β] [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") n]   (x : m α) :   n β`


As their names suggest, `Lean.Internal.coeM` and `Lean.Internal.liftCoeM` are implementation details, not part of the public API. In the resulting terms, occurrences of `Lean.Internal.coeM`, `Lean.Internal.liftCoeM`, and coercions are unfolded.
Lifting `IO` Monads
There is an instance of `[MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift") [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [IO](IO/Logical-Model/#IO "Documentation for IO")`, so any `BaseIO` action can be run in `IO` as well:
`def fromBaseIO (act : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") α) : [IO](IO/Logical-Model/#IO "Documentation for IO") α := act `
Behind the scenes, `liftM` is inserted:
``fun {α} act => liftM act : {α : Type} → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") α → [EIO](IO/Logical-Model/#EIO "Documentation for EIO") [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") α`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") fun {α} (act : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") α) => (act : [IO](IO/Logical-Model/#IO "Documentation for IO") α) `
```
fun {α} act => liftM act : {α : Type} → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") α → [EIO](IO/Logical-Model/#EIO "Documentation for EIO") [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") α
```

[Live ↪](javascript:openLiveLink\("CYUwZgBGBOD2C2AhAhgZxASQPIQBTIGMAXCALghXWwkEbgASjImprIF4JCiAoLgYgIAWIAgGsoAVwB2EAN40Avnk6NKmHPQisAfEuKNmdIA"\))
Lifting Transformed Monads
There are also instances of `[MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift")` for most of the standard library's [monad transformers](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#--tech-term-monad-transformer), so base monad actions can be used in transformed monads without additional work. For example, state monad actions can be lifted across reader and exception transformers, allowing compatible monads to be intermixed freely:
`def incrBy (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [modify](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#modify "Documentation for modify") (· + n)  def incrOrFail : [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ([ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") ([StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))) [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   if (← [read](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadReader___mk "Documentation for MonadReader.read")) > 5 then [throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") "Too much!"   incrBy (← [read](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadReader___mk "Documentation for MonadReader.read")) `
Disabling lifting causes an error:
`set_option [autoLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#autoLift "Documentation for option autoLift") false  def incrBy (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [modify](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#modify "Documentation for modify") (. + n)  def incrOrFail : [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ([ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") ([StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))) [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   if (← [read](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadReader___mk "Documentation for MonadReader.read")) > 5 then [throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") "Too much!"   `Type mismatch   incrBy __do_lift✝ has type   [StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") but is expected to have type   [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ([ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") ([StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))) [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")`incrBy (← [read](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadReader___mk "Documentation for MonadReader.read")) `
```
Type mismatch
  incrBy __do_lift✝
has type
  [StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")
but is expected to have type
  [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ([ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") ([StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))) [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")
```

Automatic lifting can be disabled by setting `[autoLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#autoLift "Documentation for option autoLift")` to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=autoLift "Permalink")option
```
autoLift
```

Default value: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
Insert monadic lifts (i.e., `liftM` and coercions) when needed.
##  18.2.1. Reversing Lifts[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Lifting-Monads--Reversing-Lifts "Permalink")
Monad lifting is not always sufficient to combine monads. Many operations provided by monads are higher order, taking an action _in the same monad_ as a parameter. Even if these operations are lifted to some more powerful monad, their arguments are still restricted to the original monad.
There are two type classes that support this kind of “reverse lifting”: `[MonadFunctor](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadFunctor___mk "Documentation for MonadFunctor")` and `[MonadControl](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControl___mk "Documentation for MonadControl")`. An instance of `[MonadFunctor](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadFunctor___mk "Documentation for MonadFunctor") m n` explains how to interpret a fully-polymorphic function in `m` into `n`. This polymorphic function must work for _all_ types `α`: it has type `{α : Type u} → m α → n α`. Such a function can be thought of as one that may have effects, but can't do so based on specific values that are provided. An instance of `[MonadControl](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControl___mk "Documentation for MonadControl") m n` explains how to interpret an arbitrary action from `m` into `n`, while at the same time providing a “reverse interpreter” that allows the `m` action to run `n` actions.
###  18.2.1.1. Monad Functors[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Lifting-Monads--Reversing-Lifts--Monad-Functors "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadFunctor "Permalink")type class
```


MonadFunctor.{u, v, w} (m : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Type u → Type v))
  (n : Type u → Type w) : Type (max (max (u + 1) v) w)


MonadFunctor.{u, v, w}
  (m : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Type u → Type v))
  (n : Type u → Type w) :
  Type (max (max (u + 1) v) w)


```

A way to interpret a fully-polymorphic function in `m` into `n`. Such a function can be thought of as one that may change the effects in `m`, but can't do so based on specific values that are provided.
Clients of `[MonadFunctor](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadFunctor___mk "Documentation for MonadFunctor")` should typically use `[MonadFunctorT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadFunctorT___mk "Documentation for MonadFunctorT")`, which is the reflexive, transitive closure of `[MonadFunctor](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadFunctor___mk "Documentation for MonadFunctor")`. New instances should be defined for `[MonadFunctor](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadFunctor___mk "Documentation for MonadFunctor").`
#  Instance Constructor

```
[MonadFunctor.mk](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadFunctor___mk "Documentation for MonadFunctor.mk").{u, v, w}
```

#  Methods

```
monadMap : {α : Type u} → ({β : Type u} → m β → m β) → n α → n α
```

Lifts a fully-polymorphic transformation of `m` into `n`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadFunctorT "Permalink")type class
```


MonadFunctorT.{u, v, w} (m : Type u → Type v) (n : Type u → Type w) :
  Type (max (max (u + 1) v) w)


MonadFunctorT.{u, v, w}
  (m : Type u → Type v)
  (n : Type u → Type w) :
  Type (max (max (u + 1) v) w)


```

A way to interpret a fully-polymorphic function in `m` into `n`. Such a function can be thought of as one that may change the effects in `m`, but can't do so based on specific values that are provided.
This is the reflexive, transitive closure of `[MonadFunctor](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadFunctor___mk "Documentation for MonadFunctor")`. It automatically chains together `[MonadFunctor](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadFunctor___mk "Documentation for MonadFunctor")` instances as needed. Clients of `[MonadFunctor](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadFunctor___mk "Documentation for MonadFunctor")` should typically use `[MonadFunctorT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadFunctorT___mk "Documentation for MonadFunctorT")`, but new instances should be defined for `[MonadFunctor](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadFunctor___mk "Documentation for MonadFunctor")`.
#  Instance Constructor

```
[MonadFunctorT.mk](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadFunctorT___mk "Documentation for MonadFunctorT.mk").{u, v, w}
```

#  Methods

```
monadMap : {α : Type u} → ({β : Type u} → m β → m β) → n α → n α
```

Lifts a fully-polymorphic transformation of `m` into `n`.
###  18.2.1.2. Reversible Lifting with `MonadControl`[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Lifting-Monads--Reversing-Lifts--Reversible-Lifting-with--MonadControl "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadControl.stM "Permalink")type class
```


MonadControl.{u, v, w} (m : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Type u → Type v))
  (n : Type u → Type w) : Type (max (max (u + 1) v) w)


MonadControl.{u, v, w}
  (m : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Type u → Type v))
  (n : Type u → Type w) :
  Type (max (max (u + 1) v) w)


```

A way to lift a computation from one monad to another while providing the lifted computation with a means of interpreting computations from the outer monad. This provides a means of lifting higher-order operations automatically.
Clients should typically use `[control](Functors___-Monads-and--do--Notation/Lifting-Monads/#control "Documentation for control")` or `[controlAt](Functors___-Monads-and--do--Notation/Lifting-Monads/#controlAt "Documentation for controlAt")`, which request an instance of `[MonadControlT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT")`: the reflexive, transitive closure of `[MonadControl](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControl___mk "Documentation for MonadControl")`. New instances should be defined for `[MonadControl](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControl___mk "Documentation for MonadControl")` itself.
#  Instance Constructor

```
[MonadControl.mk](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControl___mk "Documentation for MonadControl.mk").{u, v, w}
```

#  Methods

```
stM : Type u → Type u
```

A type that can be used to reconstruct both a returned value and any state used by the outer monad.

```
liftWith : {α : Type u} → (({β : Type u} → n β → m ([MonadControl.stM](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControl___mk "Documentation for MonadControl.stM") m n β)) → m α) → n α
```

Lifts an action from the inner monad `m` to the outer monad `n`. The inner monad has access to a reverse lifting operator that can run an `n` action, returning a value and state together.

```
restoreM : {α : Type u} → m ([MonadControl.stM](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControl___mk "Documentation for MonadControl.stM") m n α) → n α
```

Lifts a monadic action that returns a state and a value in the inner monad to an action in the outer monad. The extra state information is used to restore the results of effects from the reverse lift passed to `[liftWith](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT.liftWith")`'s parameter.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadControlT "Permalink")type class
```


MonadControlT.{u, v, w} (m : Type u → Type v) (n : Type u → Type w) :
  Type (max (max (u + 1) v) w)


MonadControlT.{u, v, w}
  (m : Type u → Type v)
  (n : Type u → Type w) :
  Type (max (max (u + 1) v) w)


```

A way to lift a computation from one monad to another while providing the lifted computation with a means of interpreting computations from the outer monad. This provides a means of lifting higher-order operations automatically.
Clients should typically use `[control](Functors___-Monads-and--do--Notation/Lifting-Monads/#control "Documentation for control")` or `[controlAt](Functors___-Monads-and--do--Notation/Lifting-Monads/#controlAt "Documentation for controlAt")`, which request an instance of `[MonadControlT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT")`: the reflexive, transitive closure of `[MonadControl](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControl___mk "Documentation for MonadControl")`. New instances should be defined for `[MonadControl](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControl___mk "Documentation for MonadControl")` itself.
#  Instance Constructor

```
[MonadControlT.mk](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT.mk").{u, v, w}
```

#  Methods

```
stM : Type u → Type u
```

A type that can be used to reconstruct both a returned value and any state used by the outer monad.

```
liftWith : {α : Type u} → (({β : Type u} → n β → m ([stM](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT.stM") m n β)) → m α) → n α
```

Lifts an action from the inner monad `m` to the outer monad `n`. The inner monad has access to a reverse lifting operator that can run an `n` action, returning a value and state together.

```
restoreM : {α : Type u} → [stM](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT.stM") m n α → n α
```

Lifts a monadic action that returns a state and a value in the inner monad to an action in the outer monad. The extra state information is used to restore the results of effects from the reverse lift passed to `[liftWith](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT.liftWith")`'s parameter.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=control "Permalink")def
```


control.{u, v, w} {m : Type u → Type v} {n : Type u → Type w}
  [[MonadControlT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT") m n] [[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind") n] {α : Type u}
  (f : ({β : Type u} → n β → m ([stM](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT.stM") m n β)) → m ([stM](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT.stM") m n α)) : n α


control.{u, v, w} {m : Type u → Type v}
  {n : Type u → Type w}
  [[MonadControlT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT") m n] [[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind") n]
  {α : Type u}
  (f :
    ({β : Type u} → n β → m ([stM](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT.stM") m n β)) →
      m ([stM](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT.stM") m n α)) :
  n α


```

Lifts an operation from an inner monad to an outer monad, providing it with a reverse lifting operator that allows outer monad computations to be run in the inner monad. The lifted operation is required to return extra information that is required in order to reconstruct the reverse lift's effects in the outer monad; this extra information is determined by `[stM](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT.stM")`.
This function takes the inner monad as an implicit parameter. Use `[controlAt](Functors___-Monads-and--do--Notation/Lifting-Monads/#controlAt "Documentation for controlAt")` to specify it explicitly.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=controlAt "Permalink")def
```


controlAt.{u, v, w} (m : Type u → Type v) {n : Type u → Type w}
  [[MonadControlT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT") m n] [[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind") n] {α : Type u}
  (f : ({β : Type u} → n β → m ([stM](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT.stM") m n β)) → m ([stM](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT.stM") m n α)) : n α


controlAt.{u, v, w} (m : Type u → Type v)
  {n : Type u → Type w}
  [[MonadControlT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT") m n] [[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind") n]
  {α : Type u}
  (f :
    ({β : Type u} → n β → m ([stM](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT.stM") m n β)) →
      m ([stM](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT.stM") m n α)) :
  n α


```

Lifts an operation from an inner monad to an outer monad, providing it with a reverse lifting operator that allows outer monad computations to be run in the inner monad. The lifted operation is required to return extra information that is required in order to reconstruct the reverse lift's effects in the outer monad; this extra information is determined by `[stM](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControlT___mk "Documentation for MonadControlT.stM")`.
This function takes the inner monad as an explicit parameter. Use `[control](Functors___-Monads-and--do--Notation/Lifting-Monads/#control "Documentation for control")` to infer the monad.
Exceptions and Lifting
One example is `[Except.tryCatch](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___tryCatch "Documentation for Except.tryCatch")`:
`[Except.tryCatch](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___tryCatch "Documentation for Except.tryCatch").{u, v} {ε : Type u} {α : Type v}   (ma : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α) (handle : ε → [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α) :   [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α`
Both of its parameters are in `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε`. `[MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift")` can lift the entire application of the handler. The function `[getBytes](Functors___-Monads-and--do--Notation/Lifting-Monads/#getBytes-_LPAR_in-Exceptions-and-Lifting_RPAR_ "Definition of example")`, which extracts the single bytes from an array of `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`s using state and exceptions, is written without ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do)-notation or automatic lifting in order to make its structure explicit.
`set_option [autoLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#autoLift "Documentation for option autoLift") false  def getByte (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") :=   [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n < 256 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax")     [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") n.[toUInt8](Basic-Types/Natural-Numbers/#Nat___toUInt8 "Documentation for Nat.toUInt8")   [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") s!"Out of range: {n}"  def getBytes (input : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :     [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   input.[forM](Basic-Types/Arrays/#Array___forM "Documentation for Array.forM") fun i =>     liftM ([Except.tryCatch](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___tryCatch "Documentation for Except.tryCatch") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") <$> [getByte](Functors___-Monads-and--do--Notation/Lifting-Monads/#getByte-_LPAR_in-Exceptions-and-Lifting_RPAR_ "Definition of example") i) fun _ => [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) >>=       fun         | [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") b => [modify](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#modify "Documentation for modify") (·.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") b)         | [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") => [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") () ```Except.ok #[1, 58, 255, 2]`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [getBytes](Functors___-Monads-and--do--Notation/Lifting-Monads/#getBytes-_LPAR_in-Exceptions-and-Lifting_RPAR_ "Definition of example") #[1, 58, 255, 300, 2, 1000000] |>.[run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT___run "Documentation for StateT.run") #[] |>.[map](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___map "Documentation for Except.map") (·.2) `
```
Except.ok #[1, 58, 255, 2]
```

`[getBytes](Functors___-Monads-and--do--Notation/Lifting-Monads/#getBytes-_LPAR_in-Exceptions-and-Lifting_RPAR_ "Definition of example")` uses an `Option` returned from the lifted action to signal the desired state updates. This quickly becomes unwieldy if there is more than one way to react to the inner action, such as saving handled exceptions. Ideally, state updates would be performed within the `[tryCatch](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.tryCatch")` call directly.
Attempting to save bytes and handled exceptions does not work, however, because the arguments to `[Except.tryCatch](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___tryCatch "Documentation for Except.tryCatch")` have type `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")`:
`def getBytes' (input : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :     [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))       ([StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8"))         ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))) [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   input.[forM](Basic-Types/Arrays/#Array___forM "Documentation for Array.forM") fun i =>     liftM       ([Except.tryCatch](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___tryCatch "Documentation for Except.tryCatch")         ([getByte](Functors___-Monads-and--do--Notation/Lifting-Monads/#getByte-_LPAR_in-Exceptions-and-Lifting_RPAR_ "Definition of example") i >>= fun b =>          `failed to synthesize instance of type class   [MonadStateOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`[modifyThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#modifyThe "Documentation for modifyThe") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) (·.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") b)) fun e => `failed to synthesize instance of type class   [MonadStateOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`[modifyThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#modifyThe "Documentation for modifyThe") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (·.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") e)) `
```
failed to synthesize instance of type class
  [MonadStateOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```

Because `[StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT")` has a `[MonadControl](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControl___mk "Documentation for MonadControl")` instance, `[control](Functors___-Monads-and--do--Notation/Lifting-Monads/#control "Documentation for control")` can be used instead of `liftM`. It provides the inner action with an interpreter for the outer monad. In the case of `[StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT")`, this interpreter expects that the inner monad returns a tuple that includes the updated state, and takes care of providing the initial state and extracting the updated state from the tuple.
`def getBytes' (input : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :     [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))       ([StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8"))         ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))) [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   input.[forM](Basic-Types/Arrays/#Array___forM "Documentation for Array.forM") fun i =>     [control](Functors___-Monads-and--do--Notation/Lifting-Monads/#control "Documentation for control") fun run =>       ([Except.tryCatch](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___tryCatch "Documentation for Except.tryCatch")         ([getByte](Functors___-Monads-and--do--Notation/Lifting-Monads/#getByte-_LPAR_in-Exceptions-and-Lifting_RPAR_ "Definition of example") i >>= fun b =>          run ([modifyThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#modifyThe "Documentation for modifyThe") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) (·.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") b))))         fun e =>           run ([modifyThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#modifyThe "Documentation for modifyThe") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (·.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") e)) ```Except.ok (#["Out of range: 300", "Out of range: 1000000"], #[1, 58, 255, 2])`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") getBytes' #[1, 58, 255, 300, 2, 1000000] |>.[run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT___run "Documentation for StateT.run") #[] |>.[run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT___run "Documentation for StateT.run") #[] |>.[map](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___map "Documentation for Except.map") (fun (((), bytes), errs) => (bytes, errs)) `
```
Except.ok (#["Out of range: 300", "Out of range: 1000000"], #[1, 58, 255, 2])
```

[Live ↪](javascript:openLiveLink\("M4UwLg+g9gDmCWUB2ACAhgVzFAMvAZmCvmgDagBQFAJiPigObgBCAnmCCgBSoBcKAOTRgAlCn4BRAB4BjEHBQBlMACd4SBigCqASSRgAHOIC8FFCgIpUAHhQAmAKwA2FGAAWIJGfMoYGFZxIAHTYuvoG3iDknO4qUADuKMAAhABEAPJYKFD0KmgaIPwA3kgAvqlUtPRMYGwcwNzqfkT8AIIqeayCwmK83ubKwiAAKtztndp6hmJc0nIKymoaYlpI8C3GKNRQ3k1YQfhQKgCyxBio8CjGAHz9KKQEYKezsvJgISqsAMLCMm7cwCgAFtONYACTXRgsdiceBifDnFAQK6QvwBKzIEBia7XUw+HwIrz4/EAHySwM4ACMUSggVBqAQulwAO1BPzAf6UkR3UkYpCcG6+fycLjcigAYhAADcyFDajCGuKANoARgANCgHAYNY4HBqAMwABkNOo1KuNFsNAF0UCTrkEVIjlTa7UEgWgYNxWXYxVU5XUQMAAOSNJDNcQocZoLpCUTiO6DDijLhRrqLdQMbnE7iJkZjDrRybhLPZ7hzN5KVQZkQrNYbLY7cx7d6HE5nC4ou4yZCqKCkdsoR2oG48suvOAfb6/Nyj8xcGoBiwoHGbQkoakj0vmIfcOkM/CsYYefMTMLTL1sjAc9c1muzgcC25b7eIrh7xlHkWpytLTMX9n/FiYqSjKpDeAuCohsq6qatq9gOHqKBGia9hmpaxpWt4ro7s6tr2jhSqYeYrrup6XBrlwlEiBqlIKtRKAgB0wBiIKXC0fUGqMSozEiEAA"\))
[←18.1. Laws](Functors___-Monads-and--do--Notation/Laws/#monad-laws "18.1. Laws")[18.3. Syntax→](Functors___-Monads-and--do--Notation/Syntax/#The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Syntax "18.3. Syntax")

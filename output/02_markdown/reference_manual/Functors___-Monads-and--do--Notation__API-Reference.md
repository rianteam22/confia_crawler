[←18.3. Syntax](Functors___-Monads-and--do--Notation/Syntax/#The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Syntax "18.3. Syntax")[18.5. Varieties of Monads→](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#monad-varieties "18.5. Varieties of Monads")
#  18.4. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--API-Reference "Permalink")
In addition to the general functions described here, there are some functions that are conventionally defined as part of the API of in the namespace of each collection type:
  * `mapM` maps a monadic function.
  * `forM` maps a monadic function, throwing away the result.
  * `filterM` filters using a monadic predicate, returning the values that satisfy it.

Monadic Collection Operations
`[Array.filterM](Basic-Types/Arrays/#Array___filterM "Documentation for Array.filterM")` can be used to write a filter that depends on a side effect.
`def values := #[1, 2, 3, 5, 8] def main : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let filtered ← [values](Functors___-Monads-and--do--Notation/API-Reference/#values-_LPAR_in-Monadic-Collection-Operations_RPAR_ "Definition of example").[filterM](Basic-Types/Arrays/#Array___filterM "Documentation for Array.filterM") fun v => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")     repeat       [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Keep {v}? [y/n]"       let answer := (← (← [IO.getStdin](IO/Files___-File-Handles___-and-Streams/#IO___getStdin "Documentation for IO.getStdin")).[getLine](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream.getLine")).[trimAscii](Basic-Types/Strings/#String___trimAscii "Documentation for String.trimAscii").[copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")       if answer == "y" then return [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")       if answer == "n" then return [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")     return [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "These values were kept:"   for v in filtered do     [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!" * {v}" `
`stdin``y``n``oops``y``n``y`
`stdout``Keep 1? [y/n]``Keep 2? [y/n]``Keep 3? [y/n]``Keep 3? [y/n]``Keep 5? [y/n]``Keep 8? [y/n]``These values were kept:`` * 1`` * 3`` * 8`
##  18.4.1. Discarding Results[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--API-Reference--Discarding-Results "Permalink")
The `[discard](Functors___-Monads-and--do--Notation/API-Reference/#Functor___discard "Documentation for Functor.discard")` function is especially useful when using an action that returns a value only for its side effects.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Functor.discard "Permalink")def
```


Functor.discard.{u, v} {f : Type u → Type v} {α : Type u} [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") f]
  (x : f α) : f [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


Functor.discard.{u, v}
  {f : Type u → Type v} {α : Type u}
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") f] (x : f α) : f [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Discards the value in a functor, retaining the functor's structure.
Discarding values is especially useful when using `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")` functors or `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")`s to implement effects, and some operation should be carried out only for its effects. In `do`-notation, statements whose values are discarded must return `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")`, and `[discard](Functors___-Monads-and--do--Notation/API-Reference/#Functor___discard "Documentation for Functor.discard")` can be used to explicitly discard their values.
##  18.4.2. Control Flow[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--API-Reference--Control-Flow "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=guard "Permalink")def
```


guard.{v} {f : Type → Type v} [[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative") f] (p : Prop) [[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") p] :
  f [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


guard.{v} {f : Type → Type v}
  [[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative") f] (p : Prop)
  [[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") p] : f [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

If the proposition `p` is true, does nothing, else fails (using `failure`).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=optional "Permalink")def
```


optional.{u, v} {f : Type u → Type v} [[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative") f] {α : Type u}
  (x : f α) : f ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)


optional.{u, v} {f : Type u → Type v}
  [[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative") f] {α : Type u} (x : f α) :
  f ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)


```

Returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x` if `f` succeeds with value `x`, else returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
##  18.4.3. Lifting Boolean Operations[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--API-Reference--Lifting-Boolean-Operations "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=andM "Permalink")def
```


andM.{u, v} {m : Type u → Type v} {β : Type u} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [ToBool β]
  (x y : m β) : m β


andM.{u, v} {m : Type u → Type v}
  {β : Type u} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [ToBool β]
  (x y : m β) : m β


```

Converts the result of the monadic action `x` to a `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`. If it is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, returns `y`; otherwise, returns the original result of `x`.
This is a monadic counterpart to the short-circuiting `&&` operator, usually accessed via the `<&&>` operator.
Conventions for notations in identifiers:
  * The recommended spelling of `<&&>` in identifiers is `[andM](Functors___-Monads-and--do--Notation/API-Reference/#andM "Documentation for andM")`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=orM "Permalink")def
```


orM.{u, v} {m : Type u → Type v} {β : Type u} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [ToBool β]
  (x y : m β) : m β


orM.{u, v} {m : Type u → Type v}
  {β : Type u} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [ToBool β]
  (x y : m β) : m β


```

Converts the result of the monadic action `x` to a `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`. If it is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, returns it and ignores `y`; otherwise, runs `y` and returns its result.
This is a monadic counterpart to the short-circuiting `||` operator, usually accessed via the `<||>` operator.
Conventions for notations in identifiers:
  * The recommended spelling of `<||>` in identifiers is `[orM](Functors___-Monads-and--do--Notation/API-Reference/#orM "Documentation for orM")`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=notM "Permalink")def
```


notM.{v} {m : Type → Type v} [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] (x : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


notM.{v} {m : Type → Type v} [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m]
  (x : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Runs a monadic action and returns the negation of its result.
##  18.4.4. Kleisli Composition[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--API-Reference--Kleisli-Composition "Permalink")
_Kleisli composition_ is the composition of monadic functions, analogous to `[Function.comp](The-Type-System/Functions/#Function___comp "Documentation for Function.comp")` for ordinary functions.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bind.kleisliRight "Permalink")def
```


Bind.kleisliRight.{u, u_1, u_2} {α : Type u} {m : Type u_1 → Type u_2}
  {β γ : Type u_1} [[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind") m] (f₁ : α → m β) (f₂ : β → m γ) (a : α) : m γ


Bind.kleisliRight.{u, u_1, u_2}
  {α : Type u} {m : Type u_1 → Type u_2}
  {β γ : Type u_1} [[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind") m] (f₁ : α → m β)
  (f₂ : β → m γ) (a : α) : m γ


```

Left-to-right composition of Kleisli arrows.
Conventions for notations in identifiers:
  * The recommended spelling of `>=>` in identifiers is `kleisliRight`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bind.kleisliLeft "Permalink")def
```


Bind.kleisliLeft.{u, u_1, u_2} {α : Type u} {m : Type u_1 → Type u_2}
  {β γ : Type u_1} [[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind") m] (f₂ : β → m γ) (f₁ : α → m β) (a : α) : m γ


Bind.kleisliLeft.{u, u_1, u_2}
  {α : Type u} {m : Type u_1 → Type u_2}
  {β γ : Type u_1} [[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind") m] (f₂ : β → m γ)
  (f₁ : α → m β) (a : α) : m γ


```

Right-to-left composition of Kleisli arrows.
Conventions for notations in identifiers:
  * The recommended spelling of `<=<` in identifiers is `kleisliLeft`.


##  18.4.5. Re-Ordered Operations[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--API-Reference--Re-Ordered-Operations "Permalink")
Sometimes, it can be convenient to partially apply a function to its second argument. These functions reverse the order of arguments, making it this easier.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Functor.mapRev "Permalink")def
```


Functor.mapRev.{u, v} {f : Type u → Type v} [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") f] {α β : Type u} :
  f α → (α → β) → f β


Functor.mapRev.{u, v}
  {f : Type u → Type v} [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") f]
  {α β : Type u} : f α → (α → β) → f β


```

Maps a function over a functor, with parameters swapped so that the function comes last.
This function is `[Functor.map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map")` with the parameters reversed, typically used via the `<&>` operator.
Conventions for notations in identifiers:
  * The recommended spelling of `<&>` in identifiers is `mapRev`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Bind.bindLeft "Permalink")def
```


Bind.bindLeft.{u, u_1} {α : Type u} {m : Type u → Type u_1} {β : Type u}
  [[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind") m] (f : α → m β) (ma : m α) : m β


Bind.bindLeft.{u, u_1} {α : Type u}
  {m : Type u → Type u_1} {β : Type u}
  [[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind") m] (f : α → m β) (ma : m α) : m β


```

Same as `[Bind.bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")` but with arguments swapped.
Conventions for notations in identifiers:
  * The recommended spelling of `=<<` in identifiers is `bindLeft`.


[←18.3. Syntax](Functors___-Monads-and--do--Notation/Syntax/#The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Syntax "18.3. Syntax")[18.5. Varieties of Monads→](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#monad-varieties "18.5. Varieties of Monads")

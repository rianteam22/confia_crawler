[←20.9. The Unit Type](Basic-Types/The-Unit-Type/#The-Lean-Language-Reference--Basic-Types--The-Unit-Type "20.9. The Unit Type")[20.11. Booleans→](Basic-Types/Booleans/#The-Lean-Language-Reference--Basic-Types--Booleans "20.11. Booleans")
#  20.10. The Empty Type[🔗](find/?domain=Verso.Genre.Manual.section&name=empty "Permalink")
The empty type `[Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")` represents impossible values. It is an inductive type with no constructors whatsoever.
While the trivial type `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")`, which has a single constructor that takes no parameters, can be used to model computations where a result is unwanted or uninteresting, `[Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")` can be used in situations where no computation should be possible at all. Instantiating a polymorphic type with `[Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")` can mark some of its constructors—those with a parameter of the corresponding type—as impossible; this can rule out certain code paths that are not desired.
The presence of a term with type `[Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")` indicates that an impossible code path has been reached. There will never be a value with this type, due to the lack of constructors. On an impossible code path, there's no reason to write further code; the function `[Empty.elim](Basic-Types/The-Empty-Type/#Empty___elim "Documentation for Empty.elim")` can be used to escape an impossible path.
The universe-polymorphic equivalent of `[Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")` is `[PEmpty](Basic-Types/The-Empty-Type/#PEmpty "Documentation for PEmpty")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Empty "Permalink")inductive type
```


Empty : Type


Empty : Type


```

The empty type. It has no constructors.
Use `[Empty.elim](Basic-Types/The-Empty-Type/#Empty___elim "Documentation for Empty.elim")` in contexts where a value of type `[Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")` is in scope.
#  Constructors
[🔗](find/?domain=Verso.Genre.Manual.doc&name=PEmpty "Permalink")inductive type
```


PEmpty.{u} : Sort u


PEmpty.{u} : Sort u


```

The universe-polymorphic empty type, with no constructors.
`[PEmpty](Basic-Types/The-Empty-Type/#PEmpty "Documentation for PEmpty")` can be used in any universe, but this flexibility can lead to worse error messages and more challenges with universe level unification. Prefer the type `[Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")` or the proposition `[False](Basic-Propositions/Truth/#False "Documentation for False")` when possible.
#  Constructors
Impossible Code Paths
The type signature of the function `[f](Basic-Types/The-Empty-Type/#f-_LPAR_in-Impossible-Code-Paths_RPAR_ "Definition of example")` indicates that it might throw exceptions, but allows the exception type to be anything:
`def f (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") n `
Instantiating `[f](Basic-Types/The-Empty-Type/#f-_LPAR_in-Impossible-Code-Paths_RPAR_ "Definition of example")`'s exception type with `[Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")` exploits the fact that `[f](Basic-Types/The-Empty-Type/#f-_LPAR_in-Impossible-Code-Paths_RPAR_ "Definition of example")` never actually throws an exception to convert it to a function whose type indicates that no exceptions will be thrown. In particular, it allows `[Empty.elim](Basic-Types/The-Empty-Type/#Empty___elim "Documentation for Empty.elim")` to be used to avoid handing the impossible exception value.
`def g (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") [f](Basic-Types/The-Empty-Type/#f-_LPAR_in-Impossible-Code-Paths_RPAR_ "Definition of example") (ε := [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")) n [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | [.error](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.error") e =>     [Empty.elim](Basic-Types/The-Empty-Type/#Empty___elim "Documentation for Empty.elim") e   | [.ok](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.ok") v => v `
[Live ↪](javascript:openLiveLink\("CYUwZgBJAUB2EC4IDkCGAXAlIiBRAHgMYgAO6EgrcAoaIC8EJArgE4gSwBQHokA5hHBxosQmglocIEALYZCACygCq4vNLIBPbPADuAS3TzJEAD4QAdCGbMA9swhtaAPmNTc69BssAbPdIfGZuY2ANYQAG4QzhFAA"\))
##  20.10.1. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--The-Empty-Type--API-Reference "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Empty.elim "Permalink")def
```


Empty.elim.{u} {C : Sort u} : [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") → C


Empty.elim.{u} {C : Sort u} : [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") → C


```

`[Empty.elim](Basic-Types/The-Empty-Type/#Empty___elim "Documentation for Empty.elim") : [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") → C` says that a value of any type can be constructed from `[Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")`. This can be thought of as a compiler-checked assertion that a code path is unreachable.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=PEmpty.elim "Permalink")def
```


PEmpty.elim.{u_1, u_2} {C : Sort u_1} : [PEmpty](Basic-Types/The-Empty-Type/#PEmpty "Documentation for PEmpty") → C


PEmpty.elim.{u_1, u_2} {C : Sort u_1} :
  [PEmpty](Basic-Types/The-Empty-Type/#PEmpty "Documentation for PEmpty") → C


```

`PEmpty.elim : Empty → C` says that a value of any type can be constructed from `[PEmpty](Basic-Types/The-Empty-Type/#PEmpty "Documentation for PEmpty")`. This can be thought of as a compiler-checked assertion that a code path is unreachable.
[←20.9. The Unit Type](Basic-Types/The-Unit-Type/#The-Lean-Language-Reference--Basic-Types--The-Unit-Type "20.9. The Unit Type")[20.11. Booleans→](Basic-Types/Booleans/#The-Lean-Language-Reference--Basic-Types--Booleans "20.11. Booleans")

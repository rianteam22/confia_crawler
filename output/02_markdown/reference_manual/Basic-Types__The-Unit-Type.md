[←20.8. Strings](Basic-Types/Strings/#String "20.8. Strings")[20.10. The Empty Type→](Basic-Types/The-Empty-Type/#empty "20.10. The Empty Type")
#  20.9. The Unit Type[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--The-Unit-Type "Permalink")
The unit type is the canonical type with exactly one element, named `[unit](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")` and represented by the empty tuple `()`. It describes only a single value, which consists of said constructor applied to no arguments whatsoever.
`[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")` is analogous to `void` in languages derived from C: even though `void` has no elements that can be named, it represents the return of control flow from a function with no additional information. In functional programming, `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")` is the return type of things that “return nothing”. Mathematically, this is represented by a single completely uninformative value, as opposed to an empty type such as `[Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")`, which represents unreachable code.
When programming with [monads](Functors___-Monads-and--do--Notation/#monads-and-do), `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")` is especially useful. For any type `α`, `m α` represents an action that has side effects and returns a value of type `α`. The type `m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")` represents an action that has some side effects but does not return a value.
There are two variants of the unit type:
  * `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")` is a `Type` that exists in the smallest non-propositional [universe](The-Type-System/Universes/#--tech-term-universes).
  * `[PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")` is [universe polymorphic](The-Type-System/Universes/#--tech-term-universe-polymorphism) and can be used in any non-propositional [universe](The-Type-System/Universes/#--tech-term-universes).


Behind the scenes, `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")` is actually defined as `[PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit").{1}`. `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")` should be preferred over `[PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")` when possible to avoid unnecessary universe parameters. If in doubt, use `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")` until universe errors occur.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Unit "Permalink")def
```


Unit : Type


Unit : Type


```

The canonical type with one element. This element is written `()`.
`[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")` has a number of uses:
  * It can be used to model control flow that returns from a function call without providing other information.
  * Monadic actions that return `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")` have side effects without computing values.
  * In polymorphic types, it can be used to indicate that no data is to be stored in a particular field.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Unit.unit "Permalink")def
```


Unit.unit : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


Unit.unit : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

The only element of the unit type.
It can be written as an empty tuple: `()`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=PUnit "Permalink")inductive type
```


PUnit.{u} : Sort u


PUnit.{u} : Sort u


```

The canonical universe-polymorphic type with just one element.
It should be used in contexts that require a type to be universe polymorphic, thus disallowing `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")`.
#  Constructors

```
unit.{u} : [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")
```

The only element of the universe-polymorphic unit type.
##  20.9.1. Definitional Equality[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--The-Unit-Type--Definitional-Equality "Permalink")
_Unit-like types_ are inductive types that have a single constructor which takes no non-proof parameters. `[PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")` is one such type. All elements of unit-like types are [definitionally equal](The-Type-System/#--tech-term-definitional-equality) to all other elements.
Definitional Equality of `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")`
Every term with type `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")` is definitionally equal to every other term with type `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")`:
`example (e1 e2 : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")) : e1 = e2 := [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAKYBGewBM8Bc8CqAdgJYAuAlDumgLzpba0BOAZjEA"\))
Definitional Equality of Unit-Like Types
Both `[CustomUnit](Basic-Types/The-Unit-Type/#CustomUnit-_LPAR_in-Definitional-Equality-of-Unit-Like-Types_RPAR_ "Definition of example")` and `[AlsoUnit](Basic-Types/The-Unit-Type/#AlsoUnit-_LPAR_in-Definitional-Equality-of-Unit-Like-Types_RPAR_ "Definition of example")` are unit-like types, with a single constructor that takes no parameters. Every pair of terms with either type is definitionally equal.
`inductive CustomUnit where   | customUnit  example (e1 e2 : [CustomUnit](Basic-Types/The-Unit-Type/#CustomUnit-_LPAR_in-Definitional-Equality-of-Unit-Like-Types_RPAR_ "Definition of example")) : e1 = e2 := [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")  structure AlsoUnit where  example (e1 e2 : [AlsoUnit](Basic-Types/The-Unit-Type/#AlsoUnit-_LPAR_in-Definitional-Equality-of-Unit-Like-Types_RPAR_ "Definition of example")) : e1 = e2 := [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
Types with parameters, such as `[WithParam](Basic-Types/The-Unit-Type/#WithParam-_LPAR_in-Definitional-Equality-of-Unit-Like-Types_RPAR_ "Definition of example")`, are also unit-like if they have a single constructor that does not take parameters.
`inductive WithParam (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) where   | mk  example (x y : [WithParam](Basic-Types/The-Unit-Type/#WithParam-_LPAR_in-Definitional-Equality-of-Unit-Like-Types_RPAR_ "Definition of example") 3) : x = y := [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
Constructors with non-proof parameters are not unit-like, even if the parameters are all unit-like types.
`inductive NotUnitLike where   | mk (u : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")) ``example (e1 e2 : [NotUnitLike](Basic-Types/The-Unit-Type/#NotUnitLike-_LPAR_in-Definitional-Equality-of-Unit-Like-Types_RPAR_ "Definition of example")) : e1 = e2 := `Type mismatch   [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") has type   ?m.3 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ?m.3 but is expected to have type   e1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") e2`[rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
```
Type mismatch
  [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")
has type
  ?m.3 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ?m.3
but is expected to have type
  e1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") e2
```

Constructors of unit-like types may take parameters that are proofs.
`inductive ProofUnitLike where   | mk : 2 = 2 → [ProofUnitLike](Basic-Types/The-Unit-Type/#ProofUnitLike-_LPAR_in-Definitional-Equality-of-Unit-Like-Types_RPAR_ "Definition of example")  example (e1 e2 : [ProofUnitLike](Basic-Types/The-Unit-Type/#ProofUnitLike-_LPAR_in-Definitional-Equality-of-Unit-Like-Types_RPAR_ "Definition of example")) : e1 = e2 := [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABAYQgZxgewLYFURgZkB3AC0QCdEAoZZAH2SkxwKJltsQA8BDXAAcANigAUiAIzJEAJmQAuNGzyFiASiWyZAXlkLF+qgDMR3LFWgwINZAEERGbOpIVqdHgOFjkkmfLajs6uWsrSyPqBRsim5rSgkLAIKADqxOQACvxUgn4g2gBy/DBa7jT0TMi4ANbcfIKiErzIAJ7a6TBZOXkAzGHILfrtMXHcidYpyIXYMK4AMsA1KOV0DMy1fhDaoePgk0jImVTY2CYLSyuUFevVNdoK+gqASYRHJ2cXy/XeTX4R0W9TudOItlgMIlFDMYzEA"\))
[←20.8. Strings](Basic-Types/Strings/#String "20.8. Strings")[20.10. The Empty Type→](Basic-Types/The-Empty-Type/#empty "20.10. The Empty Type")

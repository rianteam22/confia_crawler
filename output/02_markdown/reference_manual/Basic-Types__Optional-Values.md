[←20.11. Booleans](Basic-Types/Booleans/#The-Lean-Language-Reference--Basic-Types--Booleans "20.11. Booleans")[20.13. Tuples→](Basic-Types/Tuples/#tuples "20.13. Tuples")
#  20.12. Optional Values[🔗](find/?domain=Verso.Genre.Manual.section&name=option "Permalink")
`[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α` is the type of values which are either `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v` for some `v`﻿`:`﻿`α`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`. In functional programming, this type is used similarly to nullable types: `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` represents the absence of a value. Additionally, partial functions from `α` to `β` can be represented by the type `α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β`, where `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` results when the function is undefined for some input. Computationally, these partial functions represent the possibility of failure or errors, and they correspond to a program that can terminate early but not throw an informative exception.
`[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` can also be thought of as being similar to a list that contains at most one element. From this perspective, iterating over `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` consists of carrying out an operation only when a value is present. The `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` API makes frequent use of this perspective.
Options as Nullability
The function `[Std.HashMap.get?](Basic-Types/Maps-and-Sets/#Std___HashMap___get___-next "Documentation for Std.HashMap.get?")` looks up a specified key `a : α` inside a `[HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β`:
`[Std.HashMap.get?](Basic-Types/Maps-and-Sets/#Std___HashMap___get___-next "Documentation for Std.HashMap.get?").{u, v} {α : Type u} {β : Type v}   [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]   (m : [HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a : α) :   [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β`
Because there is no way to know in advance whether the key is actually in the map, the return type is `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β`, where `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` means the key was not in the map, and `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") b` means that the key was found and `b` is the value retrieved.
The `xs[i]` syntax, which is used to index into collections when there is an available proof that `i` is a valid index into `xs`, has a variant `xs[i]?` that returns an optional value depending on whether the given index is valid. If `m`﻿`:`﻿`[HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β` and `a`﻿`:`﻿`α`, then `m[a]?` is equivalent to `[HashMap.get?](Basic-Types/Maps-and-Sets/#Std___HashMap___get___-next "Documentation for Std.HashMap.get?") m a`.
[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAZRgEwFComApgO0SuACgAkBDAZwAsBZUsASlQDdSphSAjAGyzgG8AwhC5cAvnADaAIQCiARziBG4AC6kslU48lqwqTgAuJfSIcDcQE3AxvgA9yZoSPESA4lhgyeIOA65KLcADMAVzwAfThwgF4APjgAFSggrFU+YDNFcT4vQ3UaOj9zUSA"\))
Options as Safe Nullability
In many programming languages, it is important to remember to check for the null value. When using `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")`, the type system requires these checks in the right places: `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α` and `α` are not the same type, and converting from one to the other requires handling the case of `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`. This can be done via helpers such as `[Option.getD](Basic-Types/Optional-Values/#Option___getD "Documentation for Option.getD")`, or with pattern matching.
`def postalCodes : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=   [Std.HashMap.emptyWithCapacity](Basic-Types/Maps-and-Sets/#Std___HashMap___emptyWithCapacity "Documentation for Std.HashMap.emptyWithCapacity") 1 |>.[insert](Basic-Types/Maps-and-Sets/#Std___HashMap___insert "Documentation for Std.HashMap.insert") 12345 "Schenectady" ```"not found"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [postalCodes](Basic-Types/Optional-Values/#postalCodes-_LPAR_in-Options-as-Safe-Nullability_RPAR_ "Definition of example")[12346]?.[getD](Basic-Types/Optional-Values/#Option___getD "Documentation for Option.getD") "not found" `
```
"not found"
```
``"not found"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") [postalCodes](Basic-Types/Optional-Values/#postalCodes-_LPAR_in-Options-as-Safe-Nullability_RPAR_ "Definition of example")[12346]? [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") | [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") => "not found" | [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") city => city `
```
"not found"
```
``"Schenectady"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [if](Terms/Conditionals/#termIfLet "Documentation for syntax") [let](Terms/Conditionals/#termIfLet "Documentation for syntax") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") city := [postalCodes](Basic-Types/Optional-Values/#postalCodes-_LPAR_in-Options-as-Safe-Nullability_RPAR_ "Definition of example")[12345]? [then](Terms/Conditionals/#termIfLet "Documentation for syntax") city [else](Terms/Conditionals/#termIfLet "Documentation for syntax") "not found" `
```
"Schenectady"
```

[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAZRgEwFCuQUwGZ0gZxgEMAbAYQi3zgC5EUA6ACSPwAsBZIsOAOSPhIowAHYBzWgF5UcesmatO3BpnAwAngHVgMNmW5EAxjvVwAjHAA+APgaj8mWOYBMAZgAsAVjgAiBIbZMEUxDYmR1H3QAYkwAN1I8CEJSCioAbTM3dwA2AF0AfgYxTBgAEV8RCHhsCABXEWRI1Bj4khk4EAEAxOTySkx8DKy8/LgAdx02dss4SuC4SWsKqrga+sbpuHwIEEw4Yw0FpYP1aLjSduBcEhKtnb2TqR7iPvTMj08CuF0g9tkT9qYEgOP7Lap1Bo+IA"\))
[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=Optional%E2%86%AAOption "Permalink")inductive type
```


Option.{u} (α : Type u) : Type u


Option.{u} (α : Type u) : Type u


```

Optional values, which are either `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` around a value from the underlying type or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
`[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` can represent nullable types or computations that might fail. In the codomain of a function type, it can also represent partiality.
#  Constructors

```
none.{u} {α : Type u} : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α
```

No value.

```
some.{u} {α : Type u} (val : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α
```

Some value of type `α`.
##  20.12.1. Coercions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Optional-Values--Coercions "Permalink")
There is a [coercion](Coercions/#--tech-term-coercion) from `α` to `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α` that wraps a value in `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")`. This allows `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` to be used in a style similar to nullable types in other languages, where values that are missing are indicated by `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` and values that are present are not specially marked.
Coercions and `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")`
In `[getAlpha](Basic-Types/Optional-Values/#getAlpha-_LPAR_in-Coercions-and--Option_RPAR_ "Definition of example")`, a line of input is read. If the line consists only of letters (after removing whitespace from the beginning and end of it), then it is returned; otherwise, the function returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
`def getAlpha : [IO](IO/Logical-Model/#IO "Documentation for IO") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let line := (← (← [IO.getStdin](IO/Files___-File-Handles___-and-Streams/#IO___getStdin "Documentation for IO.getStdin")).[getLine](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream.getLine")).``String.trim` has been deprecated: Use `[String.trimAscii](Basic-Types/Strings/#String___trimAscii "Documentation for String.trimAscii")` instead  Note: The updated constant has a different type:   [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") instead of   [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`trim if line.[length](Basic-Types/Strings/#String___length "Documentation for String.length") > 0 && line.[all](Basic-Types/Strings/#String___all "Documentation for String.all") [Char.isAlpha](Basic-Types/Characters/#Char___isAlpha "Documentation for Char.isAlpha") then return line else return [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") `
In the successful case, there is no explicit `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` wrapped around `line`. The `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` is automatically inserted by the coercion.
[Live ↪](javascript:openLiveLink\("CYUwZgBA5iAuCCAbADgCwIYQFwQJIHkIAKfZWASwHsA7CAZVgCdzqoBKbAXgmEoCgIERHCEsQXYoATCKXnwA6GLAbAWbBXAAyYtU3IBbARHKREYucNaxUEAHwQADBABkT0dRBz0iRBADCGRjlyAGckNEwrEGpDQUY4AFdGWlN3QxBEYJAYiDjYRNpqGhAgA"\))
##  20.12.2. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Optional-Values--API-Reference "Permalink")
###  20.12.2.1. Extracting Values[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Optional-Values--API-Reference--Extracting-Values "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.get "Permalink")def
```


Option.get.{u} {α : Type u} (o : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) : o.[isSome](Basic-Types/Optional-Values/#Option___isSome "Documentation for Option.isSome") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → α


Option.get.{u} {α : Type u}
  (o : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) : o.[isSome](Basic-Types/Optional-Values/#Option___isSome "Documentation for Option.isSome") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → α


```

Extracts the value from an option that can be proven to be `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.get! "Permalink")def
```


Option.get!.{u} {α : Type u} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → α


Option.get!.{u} {α : Type u}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → α


```

Extracts the value from an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")`, panicking on `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.getD "Permalink")def
```


Option.getD.{u_1} {α : Type u_1} (opt : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) (dflt : α) : α


Option.getD.{u_1} {α : Type u_1}
  (opt : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) (dflt : α) : α


```

Gets an optional value, returning a given default on `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
This function is `@[macro_inline]`, so `dflt` will not be evaluated unless `opt` turns out to be `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
Examples:
  * `([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "hello").[getD](Basic-Types/Optional-Values/#Option___getD "Documentation for Option.getD") "goodbye" = "hello"`
  * `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none").[getD](Basic-Types/Optional-Values/#Option___getD "Documentation for Option.getD") "goodbye" = "goodbye"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.getDM "Permalink")def
```


Option.getDM.{u_1, u_2} {m : Type u_1 → Type u_2} {α : Type u_1}
  [[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") m] (x : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) (y : m α) : m α


Option.getDM.{u_1, u_2}
  {m : Type u_1 → Type u_2} {α : Type u_1}
  [[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") m] (x : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) (y : m α) : m α


```

Gets the value in an option, monadically computing a default value on `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
This is the monadic analogue of `[Option.getD](Basic-Types/Optional-Values/#Option___getD "Documentation for Option.getD")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.getM "Permalink")def
```


Option.getM.{u_1, u_2} {m : Type u_1 → Type u_2} {α : Type u_1}
  [[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative") m] : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → m α


Option.getM.{u_1, u_2}
  {m : Type u_1 → Type u_2} {α : Type u_1}
  [[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative") m] : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → m α


```

Lifts an optional value to any `[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative")`, sending `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` to `failure`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.elim "Permalink")def
```


Option.elim.{u_1, u_2} {α : Type u_1} {β : Sort u_2} :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → β → (α → β) → β


Option.elim.{u_1, u_2} {α : Type u_1}
  {β : Sort u_2} :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → β → (α → β) → β


```

A case analysis function for `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")`.
Given a value for `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` and a function to apply to the contents of `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")`, `[Option.elim](Basic-Types/Optional-Values/#Option___elim "Documentation for Option.elim")` checks which constructor a given `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` consists of, and uses the appropriate argument.
`[Option.elim](Basic-Types/Optional-Values/#Option___elim "Documentation for Option.elim")` is an elimination principle for `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")`. In particular, it is a non-dependent version of `Option.recOn`. It can also be seen as a combination of `[Option.map](Basic-Types/Optional-Values/#Option___map "Documentation for Option.map")` and `[Option.getD](Basic-Types/Optional-Values/#Option___getD "Documentation for Option.getD")`.
Examples:
  * `([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "hello").[elim](Basic-Types/Optional-Values/#Option___elim "Documentation for Option.elim") 0 [String.length](Basic-Types/Strings/#String___length "Documentation for String.length") = 5`
  * `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none").[elim](Basic-Types/Optional-Values/#Option___elim "Documentation for Option.elim") 0 [String.length](Basic-Types/Strings/#String___length "Documentation for String.length") = 0`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.elimM "Permalink")def
```


Option.elimM.{u_1, u_2} {m : Type u_1 → Type u_2} {α β : Type u_1}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (x : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)) (y : m β) (z : α → m β) : m β


Option.elimM.{u_1, u_2}
  {m : Type u_1 → Type u_2}
  {α β : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (x : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)) (y : m β)
  (z : α → m β) : m β


```

A monadic case analysis function for `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")`.
Given a fallback computation for `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` and a monadic operation to apply to the contents of `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")`, `[Option.elimM](Basic-Types/Optional-Values/#Option___elimM "Documentation for Option.elimM")` checks which constructor a given `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` consists of, and uses the appropriate argument.
`[Option.elimM](Basic-Types/Optional-Values/#Option___elimM "Documentation for Option.elimM")` can also be seen as a combination of `[Option.mapM](Basic-Types/Optional-Values/#Option___mapM "Documentation for Option.mapM")` and `[Option.getDM](Basic-Types/Optional-Values/#Option___getDM "Documentation for Option.getDM")`. It is a monadic analogue of `[Option.elim](Basic-Types/Optional-Values/#Option___elim "Documentation for Option.elim")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.merge "Permalink")def
```


Option.merge.{u_1} {α : Type u_1} (fn : α → α → α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Option.merge.{u_1} {α : Type u_1}
  (fn : α → α → α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Applies a function to a two optional values if both are present. Otherwise, if one value is present, it is returned and the function is not used.
The value is `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (fn a b)` if the inputs are `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a` and `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") b`. Otherwise, the behavior is equivalent to `[Option.orElse](Basic-Types/Optional-Values/#Option___orElse "Documentation for Option.orElse")`: if only one input is `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x`, then the value is `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x`, and if both are `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, then the value is `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
Examples:
  * `[Option.merge](Basic-Types/Optional-Values/#Option___merge "Documentation for Option.merge") (· + ·) [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 3) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 3`
  * `[Option.merge](Basic-Types/Optional-Values/#Option___merge "Documentation for Option.merge") (· + ·) ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2) ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 3) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5`
  * `[Option.merge](Basic-Types/Optional-Values/#Option___merge "Documentation for Option.merge") (· + ·) ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2) [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2`
  * `Option.merge (· + ·) none none = none`


###  20.12.2.2. Properties and Comparisons[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Optional-Values--API-Reference--Properties-and-Comparisons "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.isNone "Permalink")def
```


Option.isNone.{u_1} {α : Type u_1} : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Option.isNone.{u_1} {α : Type u_1} :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` on `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` and `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` on `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x`.
This function is more flexible than `(· == none)` because it does not require a `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α` instance.
Examples:
  * `([none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")).[isNone](Basic-Types/Optional-Values/#Option___isNone "Documentation for Option.isNone") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add")).[isNone](Basic-Types/Optional-Values/#Option___isNone "Documentation for Option.isNone") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.isSome "Permalink")def
```


Option.isSome.{u_1} {α : Type u_1} : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Option.isSome.{u_1} {α : Type u_1} :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` on `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x` and `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` on `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.isEqSome "Permalink")def
```


Option.isEqSome.{u_1} {α : Type u_1} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Option.isEqSome.{u_1} {α : Type u_1}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether an optional value is both present and equal to some other value.
Given `x? : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α` and `y : α`, `x?.[isEqSome](Basic-Types/Optional-Values/#Option___isEqSome "Documentation for Option.isEqSome") y` is equivalent to `x? == [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") y`. It is more efficient because it avoids an allocation.
Ordering of optional values typically uses the `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)`, `[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)`, `[Min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)`, and `[Max](Type-Classes/Basic-Classes/#Max___mk "Documentation for Max") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)` instances.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.min "Permalink")def
```


Option.min.{u_1} {α : Type u_1} [[Min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min") α] : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Option.min.{u_1} {α : Type u_1} [[Min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min") α] :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

The minimum of two optional values, with `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` treated as the least element. This function is usually accessed through the `[Min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)` instance, rather than directly.
Prior to `nightly-2025-02-27`, `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` was treated as the greatest element, so `min none (some x) = min (some x) none = some x`.
Examples:
  * `[Option.min](Basic-Types/Optional-Values/#Option___min "Documentation for Option.min") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2) ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2`
  * `[Option.min](Basic-Types/Optional-Values/#Option___min "Documentation for Option.min") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5) ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2`
  * `[Option.min](Basic-Types/Optional-Values/#Option___min "Documentation for Option.min") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2) [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `[Option.min](Basic-Types/Optional-Values/#Option___min "Documentation for Option.min") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `Option.min none none = none`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.max "Permalink")def
```


Option.max.{u_1} {α : Type u_1} [[Max](Type-Classes/Basic-Classes/#Max___mk "Documentation for Max") α] : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Option.max.{u_1} {α : Type u_1} [[Max](Type-Classes/Basic-Classes/#Max___mk "Documentation for Max") α] :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

The maximum of two optional values.
This function is usually accessed through the `[Max](Type-Classes/Basic-Classes/#Max___mk "Documentation for Max") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)` instance, rather than directly.
Examples:
  * `[Option.max](Basic-Types/Optional-Values/#Option___max "Documentation for Option.max") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2) ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5`
  * `[Option.max](Basic-Types/Optional-Values/#Option___max "Documentation for Option.max") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5) ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5`
  * `[Option.max](Basic-Types/Optional-Values/#Option___max "Documentation for Option.max") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2) [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2`
  * `[Option.max](Basic-Types/Optional-Values/#Option___max "Documentation for Option.max") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5`
  * `Option.max none none = none`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.lt "Permalink")def
```


Option.lt.{u_1, u_2} {α : Type u_1} {β : Type u_2} (r : α → β → Prop) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β → Prop


Option.lt.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} (r : α → β → Prop) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β → Prop


```

Lifts an ordering relation to `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")`, such that `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` is the least element.
It can be understood as adding a distinguished least element, represented by `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, to both `α` and `β`.
This definition is part of the implementation of the `[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)` instance. However, because it can be used with heterogeneous relations, it is sometimes useful on its own.
Examples:
  * `[Option.lt](Basic-Types/Optional-Values/#Option___lt "Documentation for Option.lt") (fun n k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") => n < k) [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") = [False](Basic-Propositions/Truth/#False "Documentation for False")`
  * `[Option.lt](Basic-Types/Optional-Values/#Option___lt "Documentation for Option.lt") (fun n k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") => n < k) [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 3) = [True](Basic-Propositions/Truth/#True___intro "Documentation for True")`
  * `[Option.lt](Basic-Types/Optional-Values/#Option___lt "Documentation for Option.lt") (fun n k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") => n < k) ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 3) [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") = [False](Basic-Propositions/Truth/#False "Documentation for False")`
  * `[Option.lt](Basic-Types/Optional-Values/#Option___lt "Documentation for Option.lt") (fun n k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") => n < k) ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 4) ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5) = [True](Basic-Propositions/Truth/#True___intro "Documentation for True")`
  * `[Option.lt](Basic-Types/Optional-Values/#Option___lt "Documentation for Option.lt") (fun n k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") => n < k) ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 4) ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 4) = [False](Basic-Propositions/Truth/#False "Documentation for False")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.decidableEqNone "Permalink")def
```


Option.decidableEqNone.{u_1} {α : Type u_1} (o : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")o [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


Option.decidableEqNone.{u_1}
  {α : Type u_1} (o : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")o [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


```

Equality with `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` is decidable even if the wrapped type does not have decidable equality.
###  20.12.2.3. Conversion[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Optional-Values--API-Reference--Conversion "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.toArray "Permalink")def
```


Option.toArray.{u_1} {α : Type u_1} : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Option.toArray.{u_1} {α : Type u_1} :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Converts an optional value to an array with zero or one element.
Examples:
  * `([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "value").[toArray](Basic-Types/Optional-Values/#Option___toArray "Documentation for Option.toArray") = #["value"]`
  * `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none").[toArray](Basic-Types/Optional-Values/#Option___toArray "Documentation for Option.toArray") = #[]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.toList "Permalink")def
```


Option.toList.{u_1} {α : Type u_1} : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


Option.toList.{u_1} {α : Type u_1} :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Converts an optional value to a list with zero or one element.
Examples:
  * `([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "value").[toList](Basic-Types/Optional-Values/#Option___toList "Documentation for Option.toList") = ["value"]`
  * `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none").[toList](Basic-Types/Optional-Values/#Option___toList "Documentation for Option.toList") = []`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.repr "Permalink")def
```


Option.repr.{u_1} {α : Type u_1} [[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") α] : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


Option.repr.{u_1} {α : Type u_1}
  [[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") α] : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


```

Returns a representation of an optional value that should be able to be parsed as an equivalent optional value.
This function is typically accessed through the `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)` instance.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.format "Permalink")def
```


Option.format.{u} {α : Type u} [[Std.ToFormat](Interacting-with-Lean/#Std___ToFormat___mk "Documentation for Std.ToFormat") α] : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


Option.format.{u} {α : Type u}
  [[Std.ToFormat](Interacting-with-Lean/#Std___ToFormat___mk "Documentation for Std.ToFormat") α] : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


```

Formats an optional value, with no expectation that the Lean parser should be able to parse the result.
This function is usually accessed through the `ToFormat (Option α)` instance.
###  20.12.2.4. Control[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Optional-Values--API-Reference--Control "Permalink")
`[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` can be thought of as describing a computation that may fail to return a value. The `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` instance, along with `[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative") [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")`, is based on this understanding. Returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` can also be thought of as throwing an exception that contains no interesting information, which is captured in the `[MonadExcept](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` instance.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.guard "Permalink")def
```


Option.guard.{u_1} {α : Type u_1} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (a : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Option.guard.{u_1} {α : Type u_1}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (a : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if a value doesn't satisfy a Boolean predicate, or the value itself otherwise.
From the perspective of `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` as computations that might fail, this function is a run-time assertion operator in the `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` monad.
Examples:
  * `[Option.guard](Basic-Types/Optional-Values/#Option___guard "Documentation for Option.guard") (· > 2) 1 = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `[Option.guard](Basic-Types/Optional-Values/#Option___guard "Documentation for Option.guard") (· > 2) 5 = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.bind "Permalink")def
```


Option.bind.{u_1, u_2} {α : Type u_1} {β : Type u_2} :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → (α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β) → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


Option.bind.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → (α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β) → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


```

Sequencing of `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` computations.
From the perspective of `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` as computations that might fail, this function sequences potentially-failing computations, failing if either fails. From the perspective of `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` as a collection with at most one element, the function is applied to the element if present, and the final result is empty if either the initial or the resulting collections are empty.
This function is often accessed via the `>>=` operator from the `[Bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)` instance, or implicitly via `do`-notation, but it is also idiomatic to call it using [generalized field notation](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=generalized-field-notation).
Examples:
  * `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none").[bind](Basic-Types/Optional-Values/#Option___bind "Documentation for Option.bind") (fun x => [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 4).[bind](Basic-Types/Optional-Values/#Option___bind "Documentation for Option.bind") (fun x => [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 4`
  * `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none").[bind](Basic-Types/Optional-Values/#Option___bind "Documentation for Option.bind") ([Option.guard](Basic-Types/Optional-Values/#Option___guard "Documentation for Option.guard") (· > 2)) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2).[bind](Basic-Types/Optional-Values/#Option___bind "Documentation for Option.bind") ([Option.guard](Basic-Types/Optional-Values/#Option___guard "Documentation for Option.guard") (· > 2)) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 4).[bind](Basic-Types/Optional-Values/#Option___bind "Documentation for Option.bind") ([Option.guard](Basic-Types/Optional-Values/#Option___guard "Documentation for Option.guard") (· > 2)) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 4`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.bindM "Permalink")def
```


Option.bindM.{u_1, u_2, u_3} {m : Type u_1 → Type u_2} {α : Type u_3}
  {β : Type u_1} [[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") m] (f : α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


Option.bindM.{u_1, u_2, u_3}
  {m : Type u_1 → Type u_2} {α : Type u_3}
  {β : Type u_1} [[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") m]
  (f : α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


```

Runs the monadic action `f` on `o`'s value, if any, and returns the result, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if there is no value.
From the perspective of `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` as a collection with at most one element, the monadic the function is applied to the element if present, and the final result is empty if either the initial or the resulting collections are empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.join "Permalink")def
```


Option.join.{u_1} {α : Type u_1} (x : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Option.join.{u_1} {α : Type u_1}
  (x : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Flattens nested optional values, preserving any value found.
This is analogous to `[List.flatten](Basic-Types/Linked-Lists/#List___flatten "Documentation for List.flatten")`.
Examples:
  * `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none").[join](Basic-Types/Optional-Values/#Option___join "Documentation for Option.join") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")).[join](Basic-Types/Optional-Values/#Option___join "Documentation for Option.join") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v)).[join](Basic-Types/Optional-Values/#Option___join "Documentation for Option.join") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.sequence "Permalink")def
```


Option.sequence.{u, u_1} {m : Type u → Type u_1} [[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m]
  {α : Type u} : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (m α) → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)


Option.sequence.{u, u_1}
  {m : Type u → Type u_1} [[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m]
  {α : Type u} :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (m α) → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)


```

Converts an optional monadic computation into a monadic computation of an optional value.
This function only requires `m` to be an applicative functor.
Example:
``some "world"``hello `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") show [IO](IO/Logical-Model/#IO "Documentation for IO") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) from [Option.sequence](Basic-Types/Optional-Values/#Option___sequence "Documentation for Option.sequence") <| [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "hello" return "world" `
```
hello

```
`[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "world"`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.tryCatch "Permalink")def
```


Option.tryCatch.{u_1} {α : Type u_1} (x : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)
  (handle : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Option.tryCatch.{u_1} {α : Type u_1}
  (x : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)
  (handle : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Recover from failing `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` computations with a handler function.
This function is usually accessed through the `[MonadExceptOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExceptOf___mk "Documentation for MonadExceptOf") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` instance.
Examples:
  * `[Option.tryCatch](Basic-Types/Optional-Values/#Option___tryCatch "Documentation for Option.tryCatch") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") (fun () => [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "handled") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "handled"`
  * `[Option.tryCatch](Basic-Types/Optional-Values/#Option___tryCatch "Documentation for Option.tryCatch") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "succeeded") (fun () => [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "handled") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "succeeded"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.or "Permalink")def
```


Option.or.{u_1} {α : Type u_1} : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Option.or.{u_1} {α : Type u_1} :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Returns the first of its arguments that is `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if neither is `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")`.
This is similar to the `<|>` operator, also known as `OrElse.orElse`, but both arguments are always evaluated without short-circuiting.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.orElse "Permalink")def
```


Option.orElse.{u_1} {α : Type u_1} :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → ([Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Option.orElse.{u_1} {α : Type u_1} :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → ([Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Implementation of `OrElse`'s `<|>` syntax for `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")`. If the first argument is `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a`, returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a`, otherwise evaluates and returns the second argument.
See also `[or](Basic-Types/Booleans/#Bool___or "Documentation for Bool.or")` for a version that is strict in the second argument.
###  20.12.2.5. Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Optional-Values--API-Reference--Iteration "Permalink")
`[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` can be thought of as a collection that contains at most one value. From this perspective, iteration operators can be understood as performing some operation on the contained value, if present, or doing nothing if not.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.all "Permalink")def
```


Option.all.{u_1} {α : Type u_1} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Option.all.{u_1} {α : Type u_1}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether an optional value either satisfies a Boolean predicate or is `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
Examples:
  * `(some 33).all (· % 2 == 0) = false
  * `(some 22).all (· % 2 == 0) = true
  * `none.all (fun x : Nat => x % 2 == 0) = true


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.any "Permalink")def
```


Option.any.{u_1} {α : Type u_1} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Option.any.{u_1} {α : Type u_1}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether an optional value is not `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` and satisfies a Boolean predicate.
Examples:
  * `(some 33).any (· % 2 == 0) = false
  * `(some 22).any (· % 2 == 0) = true
  * `none.any (fun x : Nat => true) = false


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.filter "Permalink")def
```


Option.filter.{u_1} {α : Type u_1} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Option.filter.{u_1} {α : Type u_1}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Keeps an optional value only if it satisfies a Boolean predicate.
If `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` is thought of as a collection that contains at most one element, then `[Option.filter](Basic-Types/Optional-Values/#Option___filter "Documentation for Option.filter")` is analogous to `[List.filter](Basic-Types/Linked-Lists/#List___filter "Documentation for List.filter")` or `[Array.filter](Basic-Types/Arrays/#Array___filter "Documentation for Array.filter")`.
Examples:
  * `([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5).[filter](Basic-Types/Optional-Values/#Option___filter "Documentation for Option.filter") (· % 2 == 0) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 4).[filter](Basic-Types/Optional-Values/#Option___filter "Documentation for Option.filter") (· % 2 == 0) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 4`
  * `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none").[filter](Basic-Types/Optional-Values/#Option___filter "Documentation for Option.filter") (fun x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") => x % 2 == 0) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none").[filter](Basic-Types/Optional-Values/#Option___filter "Documentation for Option.filter") (fun x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.filterM "Permalink")def
```


Option.filterM.{u_1} {m : Type → Type u_1} {α : Type} [[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m]
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)


Option.filterM.{u_1} {m : Type → Type u_1}
  {α : Type} [[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m]
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)


```

Keeps an optional value only if it satisfies a monadic Boolean predicate.
If `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` is thought of as a collection that contains at most one element, then `[Option.filterM](Basic-Types/Optional-Values/#Option___filterM "Documentation for Option.filterM")` is analogous to `[List.filterM](Basic-Types/Linked-Lists/#List___filterM "Documentation for List.filterM")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.forM "Permalink")def
```


Option.forM.{u_1, u_2, u_3} {m : Type u_1 → Type u_2} {α : Type u_3}
  [[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") m] : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → (α → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


Option.forM.{u_1, u_2, u_3}
  {m : Type u_1 → Type u_2} {α : Type u_3}
  [[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") m] :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → (α → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Executes a monadic action on an optional value if it is present, or does nothing if there is no value.
Examples:
``([()](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit"), 5)`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5).[forM](Basic-Types/Optional-Values/#Option___forM "Documentation for Option.forM") [set](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf.set") : [StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")).[run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT___run "Documentation for StateT.run") 0 ``((), 5)```([()](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit"), 0)`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ([none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none").[forM](Basic-Types/Optional-Values/#Option___forM "Documentation for Option.forM") (fun x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") => [set](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf.set") x) : [StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")).[run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT___run "Documentation for StateT.run") 0 ``((), 0)`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.map "Permalink")def
```


Option.map.{u_1, u_2} {α : Type u_1} {β : Type u_2} (f : α → β) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


Option.map.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} (f : α → β) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


```

Apply a function to an optional value, if present.
From the perspective of `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` as a container with at most one value, this is analogous to `[List.map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map")`. It can also be accessed via the `[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` instance.
Examples:
  * `([none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")).[map](Basic-Types/Optional-Values/#Option___map "Documentation for Option.map") (· + 1) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 3).[map](Basic-Types/Optional-Values/#Option___map "Documentation for Option.map") (· + 1) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 4`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.mapA "Permalink")def
```


Option.mapA.{u_1, u_2, u_3} {m : Type u_1 → Type u_2} {α : Type u_3}
  {β : Type u_1} [[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m] (f : α → m β) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


Option.mapA.{u_1, u_2, u_3}
  {m : Type u_1 → Type u_2} {α : Type u_3}
  {β : Type u_1} [[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m]
  (f : α → m β) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


```

Applies a function in some applicative functor to an optional value, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` with no effects if the value is missing.
This is an alias for `[Option.mapM](Basic-Types/Optional-Values/#Option___mapM "Documentation for Option.mapM")`, which already works for applicative functors.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.mapM "Permalink")def
```


Option.mapM.{u_1, u_2, u_3} {m : Type u_1 → Type u_2} {α : Type u_3}
  {β : Type u_1} [[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m] (f : α → m β) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


Option.mapM.{u_1, u_2, u_3}
  {m : Type u_1 → Type u_2} {α : Type u_3}
  {β : Type u_1} [[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m]
  (f : α → m β) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


```

Applies a function in some applicative functor to an optional value, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` with no effects if the value is missing.
Runs a monadic function `f` on an optional value, returning the result. If the optional value is `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, the function is not called and the result is also `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
From the perspective of `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` as a container with at most one element, this is analogous to `[List.mapM](Basic-Types/Linked-Lists/#List___mapM "Documentation for List.mapM")`, returning the result of running the monadic function on all elements of the container.
This function only requires `m` to be an applicative functor. An alias `[Option.mapA](Basic-Types/Optional-Values/#Option___mapA "Documentation for Option.mapA")` is provided.
###  20.12.2.6. Recursion Helpers[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Optional-Values--API-Reference--Recursion-Helpers "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.attach "Permalink")def
```


Option.attach.{u_1} {α : Type u_1} (xs : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") xs [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


Option.attach.{u_1} {α : Type u_1}
  (xs : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") xs [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


```

“Attaches” a proof that an optional value, if present, is indeed this value, returning a subtype that expresses this fact.
This function is primarily used to allow definitions by well-founded recursion that use iteration operators (such as `[Option.map](Basic-Types/Optional-Values/#Option___map "Documentation for Option.map")`) to prove that an optional value drawn from a parameter is smaller than the parameter. This allows the well-founded recursion mechanism to prove that the function terminates.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.attachWith "Permalink")def
```


Option.attachWith.{u_1} {α : Type u_1} (xs : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) (P : α → Prop)
  (H : ∀ (x : α), xs [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x → P x) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") P x [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


Option.attachWith.{u_1} {α : Type u_1}
  (xs : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) (P : α → Prop)
  (H : ∀ (x : α), xs [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x → P x) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") P x [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


```

“Attaches” a proof that some predicate holds for an optional value, if present, returning a subtype that expresses this fact.
This function is primarily used to implement `[Option.attach](Basic-Types/Optional-Values/#Option___attach "Documentation for Option.attach")`, which allows definitions by well-founded recursion that use iteration operators (such as `[Option.map](Basic-Types/Optional-Values/#Option___map "Documentation for Option.map")`) to prove that an optional value drawn from a parameter is smaller than the parameter. This allows the well-founded recursion mechanism to prove that the function terminates.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.unattach "Permalink")def
```


Option.unattach.{u_1} {α : Type u_1} {p : α → Prop}
  (o : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") p x [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Option.unattach.{u_1} {α : Type u_1}
  {p : α → Prop}
  (o : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") p x [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Remove an attached proof that the value in an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` is indeed that value.
This function is usually inserted automatically by Lean, rather than explicitly in code. It is introduced as an intermediate step during the elaboration of definitions by well-founded recursion.
If this function is encountered in a proof state, the right approach is usually the tactic `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [Option.unattach, -Option.map_subtype]`.
It is a synonym for `[Option.map](Basic-Types/Optional-Values/#Option___map "Documentation for Option.map") [Subtype.val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val")`.
###  20.12.2.7. Reasoning[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Optional-Values--API-Reference--Reasoning "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.choice "Permalink")def
```


Option.choice.{u_1} (α : Type u_1) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Option.choice.{u_1} (α : Type u_1) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

An optional arbitrary element of a given type.
If `α` is non-empty, then there exists some `v : α` and this arbitrary element is `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v`. Otherwise, it is `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.pbind "Permalink")def
```


Option.pbind.{u_1, u_2} {α : Type u_1} {β : Type u_2} (o : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)
  (f : (a : α) → o [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


Option.pbind.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} (o : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)
  (f : (a : α) → o [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


```

Given an optional value and a function that can be applied when the value is `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")`, returns the result of applying the function if this is possible.
The function `f` is _partial_ because it is only defined for the values `a : α` such that `o = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a`. This restriction allows the function to use the fact that it can only be called when `o` is not `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`: it can relate its argument to the optional value `o`. Its runtime behavior is equivalent to that of `[Option.bind](Basic-Types/Optional-Values/#Option___bind "Documentation for Option.bind")`.
Examples:
`def attach (v : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") { y : α // v = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") y } :=   v.[pbind](Basic-Types/Optional-Values/#Option___pbind "Documentation for Option.pbind") fun x h => [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ⟨x, h⟩ `
```
#reduce attach (some 3)

```
`[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ⟨3, ⋯⟩`
```
#reduce attach none

```
`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.pelim "Permalink")def
```


Option.pelim.{u_1, u_2} {α : Type u_1} {β : Sort u_2} (o : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)
  (b : β) (f : (a : α) → o [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a → β) : β


Option.pelim.{u_1, u_2} {α : Type u_1}
  {β : Sort u_2} (o : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) (b : β)
  (f : (a : α) → o [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a → β) : β


```

Given an optional value and a function that can be applied when the value is `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")`, returns the result of applying the function if this is possible, or a fallback value otherwise.
The function `f` is _partial_ because it is only defined for the values `a : α` such that `o = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a`. This restriction allows the function to use the fact that it can only be called when `o` is not `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`: it can relate its argument to the optional value `o`. Its runtime behavior is equivalent to that of `[Option.elim](Basic-Types/Optional-Values/#Option___elim "Documentation for Option.elim")`.
Examples:
`def attach (v : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") { y : α // v = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") y } :=   v.[pelim](Basic-Types/Optional-Values/#Option___pelim "Documentation for Option.pelim") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") fun x h => [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ⟨x, h⟩ `
```
#reduce attach (some 3)

```
`[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ⟨3, ⋯⟩`
```
#reduce attach none

```
`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Option.pmap "Permalink")def
```


Option.pmap.{u_1, u_2} {α : Type u_1} {β : Type u_2} {p : α → Prop}
  (f : (a : α) → p a → β) (o : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) :
  (∀ (a : α), o [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a → p a) → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


Option.pmap.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} {p : α → Prop}
  (f : (a : α) → p a → β) (o : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) :
  (∀ (a : α), o [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a → p a) → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


```

Given a function from the elements of `α` that satisfy `p` to `β` and a proof that an optional value satisfies `p` if it's present, applies the function to the value.
Examples:
`def attach (v : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") { y : α // v = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") y } :=   v.[pmap](Basic-Types/Optional-Values/#Option___pmap "Documentation for Option.pmap") (fun a (h : a ∈ v) => ⟨_, h⟩) (fun _ h => h) `
```
#reduce attach (some 3)

```
`[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ⟨3, ⋯⟩`
```
#reduce attach none

```
`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
[←20.11. Booleans](Basic-Types/Booleans/#The-Lean-Language-Reference--Basic-Types--Booleans "20.11. Booleans")[20.13. Tuples→](Basic-Types/Tuples/#tuples "20.13. Tuples")

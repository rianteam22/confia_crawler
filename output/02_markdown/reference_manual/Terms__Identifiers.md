[←13. Terms](Terms/#terms "13. Terms")[13.2. Function Types→](Terms/Function-Types/#function-types "13.2. Function Types")
#  13.1. Identifiers[🔗](find/?domain=Verso.Genre.Manual.section&name=identifiers-and-resolution "Permalink")
syntaxIdentifiers

```
$x:ident

```

An identifier term is a reference to a name.The specific lexical syntax of identifiers is described [in the section on Lean's concrete syntax](Source-Files-and-Modules/#keywords-and-identifiers). Identifiers also occur in contexts where they bind names, such as ``Lean.Parser.Term.let : term`
`let` is used to declare a local definition. Example:

```
let x := 1
let y := x + 1
x + y

```

Since functions are first class citizens in Lean, you can use `let` to declare local functions too.

```
let double := fun x => 2*x
double (double 3)

```

For recursive definitions, you should use `let rec`. You can also perform pattern matching using `let`. For example, assume `p` has type `Nat × Nat`, then you can write

```
let (x, y) := p
x + y

```

The _anaphoric let_ `let := v` defines a variable called `this`.
``let` and ``Lean.Parser.Term.fun : term```fun`; however, these binding occurrences are not complete terms in and of themselves. The mapping from identifiers to names is not trivial: at any point in a [module](Source-Files-and-Modules/#--tech-term-module), some number of [namespaces](Namespaces-and-Sections/#--tech-term-namespaces) will be open, there may be [section variables](Namespaces-and-Sections/#--tech-term-Section-variables), and there may be local bindings. Furthermore, identifiers may contain multiple dot-separated atomic identifiers; the dot both separates namespaces from their contents and variables from fields or functions that use [field notation](Terms/Function-Application/#--tech-term-field-notation). This creates ambiguity, because an identifier `A.B.C.D.e.f` could refer to any of the following:
  * A name `f` in the namespace `A.B.C.D.e` (for instance, a function defined in `e`'s ``Lean.Parser.Command.declaration : command```where` block).
  * An application of `T.f` to `A.B.C.D.e` if `A.B.C.D.e` has type `T`
  * A projection of field `f` from a structure named `A.B.C.D.e`
  * A series of field projections `B.C.D.e` from structure value `A`, followed by an application of `f` using field notation
  * If namespace `Q` is opened, it could be a reference to any of the above with a `Q` prefix, such as a name `f` in the namespace `Q.A.B.C.D.e`


This list is not exhaustive. Given an identifier, the elaborator must discover which name or names an identifier refers to, and whether any of the trailing components are fields or functions applied via field notation. This is called _resolving_ the name.
Some declarations in the global environment are lazily created the first time they are referenced. Resolving an identifier in a way that both creates one of these declarations and results in a reference to it is called _realizing_ the name. The rules for resolving and realizing a name are the same, so even though this section refers only to resolving names, it applies to both.
Name resolution is affected by the following:
  * [Pre-resolved names](Notations-and-Macros/Macros/#--tech-term-pre-resolved-identifiers) attached to the identifier
  * The [macro scopes](Notations-and-Macros/Macros/#--tech-term-macro-scopes) attached to the identifier
  * The local bindings in scope, including auxiliary definitions created as part of the elaboration of ``Lean.Parser.Term.letrec : term```let rec`.
  * Aliases created with ``Lean.Parser.Command.export : command`
Adds names from other namespaces to the current namespace.
The command `export Some.Namespace (name₁ name₂)` makes `name₁` and `name₂`:
    * visible in the current namespace without prefix `Some.Namespace`, like `open`, and
    * visible from outside the current namespace `N` as `N.name₁` and `N.name₂`.
## Examples

```
namespace Morning.Sky
  def star := "venus"
end Morning.Sky

namespace Evening.Sky
  export Morning.Sky (star)
  -- `star` is now in scope
  #check star
end Evening.Sky

-- `star` is visible in `Evening.Sky`
#check Evening.Sky.star

```

`[`export`](Namespaces-and-Sections/#Lean___Parser___Command___export) in modules transitively imported by the current module
  * The current [section scope](Namespaces-and-Sections/#--tech-term-section-scope), in particular the [current namespace](Namespaces-and-Sections/#--tech-term-current-namespace), opened namespaces, and section variables


Any prefix of an identifier can resolve to a set of names. The suffix that was not included in the resolution process is then treated as field projections or field notation. Resolutions of longer prefixes take precedence over resolutions of shorter prefixes; in other words, as few components as of the identifier as possible are treated as field notation. An identifier prefix may refer to any of the following, with earlier items taking precedence over later ones:
  1. A locally-bound variable whose name is identical to the identifier prefix, including macro scopes, with closer local bindings taking precedence over outer local bindings.
  2. A local auxiliary definition whose name is identical to the identifier prefix
  3. A [section variable](Namespaces-and-Sections/#--tech-term-Section-variables) whose name is identical to the identifier prefix
  4. A global name that is identical to a prefix of the [current namespace](Namespaces-and-Sections/#--tech-term-current-namespace) appended to the identifier prefix, or for which an alias exists in a prefix of the current namespace, with longer prefixes of the current namespace taking precedence over shorter ones
  5. A global name that has been brought into scope via ``Lean.Parser.Command.open : command`
Makes names from other namespaces visible without writing the namespace prefix.
Names that are made available with `open` are visible within the current `section` or `namespace` block. This makes referring to (type) definitions and theorems easier, but note that it can also make [scoped instances], notations, and attributes from a different namespace available.
The `open` command can be used in a few different ways:
     * `open Some.Namespace.Path1 Some.Namespace.Path2` makes all non-protected names in `Some.Namespace.Path1` and `Some.Namespace.Path2` available without the prefix, so that `Some.Namespace.Path1.x` and `Some.Namespace.Path2.y` can be referred to by writing only `x` and `y`.
     * `open Some.Namespace.Path hiding def1 def2` opens all non-protected names in `Some.Namespace.Path` except `def1` and `def2`.
     * `open Some.Namespace.Path (def1 def2)` only makes `Some.Namespace.Path.def1` and `Some.Namespace.Path.def2` available without the full prefix, so `Some.Namespace.Path.def3` would be unaffected.
This works even if `def1` and `def2` are `protected`.
     * `open Some.Namespace.Path renaming def1 → def1', def2 → def2'` same as `open Some.Namespace.Path (def1 def2)` but `def1`/`def2`'s names are changed to `def1'`/`def2'`.
This works even if `def1` and `def2` are `protected`.
     * `open scoped Some.Namespace.Path1 Some.Namespace.Path2` **only** opens [scoped instances], notations, and attributes from `Namespace1` and `Namespace2`; it does **not** make any other name available.
     * `open <any of the open shapes above> in` makes the names `open`-ed visible only in the next command or expression.
## Examples

```
/-- SKI combinators https://en.wikipedia.org/wiki/SKI_combinator_calculus -/
namespace Combinator.Calculus
  def I (a : α) : α := a
  def K (a : α) : β → α := fun _ => a
  def S (x : α → β → γ) (y : α → β) (z : α) : γ := x z (y z)
end Combinator.Calculus

section
  -- open everything under `Combinator.Calculus`, *i.e.* `I`, `K` and `S`,
  -- until the section ends
  open Combinator.Calculus

  theorem SKx_eq_K : S K x = I := rfl
end

-- open everything under `Combinator.Calculus` only for the next command (the next `theorem`, here)
open Combinator.Calculus in
theorem SKx_eq_K' : S K x = I := rfl

section
  -- open only `S` and `K` under `Combinator.Calculus`
  open Combinator.Calculus (S K)

  theorem SKxy_eq_y : S K x y = y := rfl

  -- `I` is not in scope, we have to use its full path
  theorem SKxy_eq_Iy : S K x y = Combinator.Calculus.I y := rfl
end

section
  open Combinator.Calculus
    renaming
      I → identity,
      K → konstant

  #check identity
  #check konstant
end

section
  open Combinator.Calculus
    hiding S

  #check I
  #check K
end

section
  namespace Demo
    inductive MyType
    | val

    namespace N1
      scoped infix:68 " ≋ " => BEq.beq

      scoped instance : BEq MyType where
        beq _ _ := true

      def Alias := MyType
    end N1
  end Demo

  -- bring `≋` and the instance in scope, but not `Alias`
  open scoped Demo.N1

  #check Demo.MyType.val == Demo.MyType.val
  #check Demo.MyType.val ≋ Demo.MyType.val
  -- #check Alias -- unknown identifier 'Alias'
end

```

`[`open`](Namespaces-and-Sections/#Lean___Parser___Command___open) commands that is identical to the identifier prefix


If an identifier resolves to multiple names, then the elaborator attempts to use all of them. If exactly one of them succeeds, then it is used as the meaning of the identifier. It is an error if more than one succeed or if all fail.
Local Names Take Precedence
Local bindings take precedence over global bindings:
`def x := "global"  `"local"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") let x := "local" x `
```
"local"
```

The innermost local binding of a name takes precedence over others:
``"inner"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") let x := "outer" let x := "inner" x `
```
"inner"
```

[Live ↪](javascript:openLiveLink\("CYUwZgBAHhBcC8EBEBzANgewEYEM1ICgCBiEANzwIgjRABdo5ElMBjPQ6qI0itKmvUYJkGAK50QAJ06CGMEUgCWAOxXTZUIA"\))
Longer Prefixes of Current Namespace Take Precedence
The namespaces `A`, `B`, and `C` are nested. Both `A` and `C` contain a definition of `x`.
`[namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") A def x := "A.x" [namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") B [namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") C def x := "A.B.C.x" `
When the current namespace is `A.B.C`, `[x](Terms/Identifiers/#A___x-_LPAR_in-Longer-Prefixes-of-Current-Namespace-Take-Precedence_RPAR_ "Definition of example")` resolves to `[A.B.C.x](Terms/Identifiers/#A___B___C___x-_LPAR_in-Longer-Prefixes-of-Current-Namespace-Take-Precedence_RPAR_ "Definition of example")`.
``"A.B.C.x"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [x](Terms/Identifiers/#A___B___C___x-_LPAR_in-Longer-Prefixes-of-Current-Namespace-Take-Precedence_RPAR_ "Definition of example") `
```
"A.B.C.x"
```

When the current namespace is `A.B`, `[x](Terms/Identifiers/#A___x-_LPAR_in-Longer-Prefixes-of-Current-Namespace-Take-Precedence_RPAR_ "Definition of example")` resolves to `[A.x](Terms/Identifiers/#A___x-_LPAR_in-Longer-Prefixes-of-Current-Namespace-Take-Precedence_RPAR_ "Definition of example")`.
`end C `"A.x"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [x](Terms/Identifiers/#A___x-_LPAR_in-Longer-Prefixes-of-Current-Namespace-Take-Precedence_RPAR_ "Definition of example") `
```
"A.x"
```

[Live ↪](javascript:openLiveLink\("HYQwtgpgzgDiDGEAEBBAUAEwgMyQDyQC4BeJAIhQDo8y1RJYFkAhO8aORJAYUx3yKkKlZpW7VaaAMQQAbiAA2+NGgjAMPaXMX4gA"\))
Longer Identifier Prefixes Take Precedence
When an identifier could refer to different projections from names, the one with the longest name takes precedence:
`structure A where   y : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") deriving [Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")  structure B where   y : [A](Terms/Identifiers/#A-_LPAR_in-Longer-Identifier-Prefixes-Take-Precedence_RPAR_ "Definition of example") deriving [Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")  def y : [B](Terms/Identifiers/#B-_LPAR_in-Longer-Identifier-Prefixes-Take-Precedence_RPAR_ "Definition of example") := ⟨⟨"shorter"⟩⟩ def y.y : [A](Terms/Identifiers/#A-_LPAR_in-Longer-Identifier-Prefixes-Take-Precedence_RPAR_ "Definition of example") := ⟨"longer"⟩ `
Given the above declarations, `[y.y](Terms/Identifiers/#y___y-_LPAR_in-Longer-Identifier-Prefixes-Take-Precedence_RPAR_ "Definition of example").[y](Terms/Identifiers/#A___y-_LPAR_in-Longer-Identifier-Prefixes-Take-Precedence_RPAR_ "Definition of example")` could in principle refer either to the `[y](Terms/Identifiers/#A___y-_LPAR_in-Longer-Identifier-Prefixes-Take-Precedence_RPAR_ "Definition of example")` field of the `[y](Terms/Identifiers/#B___y-_LPAR_in-Longer-Identifier-Prefixes-Take-Precedence_RPAR_ "Definition of example")` field of `[y](Terms/Identifiers/#y-_LPAR_in-Longer-Identifier-Prefixes-Take-Precedence_RPAR_ "Definition of example")`, or to the `[y](Terms/Identifiers/#A___y-_LPAR_in-Longer-Identifier-Prefixes-Take-Precedence_RPAR_ "Definition of example")` field of `[y.y](Terms/Identifiers/#y___y-_LPAR_in-Longer-Identifier-Prefixes-Take-Precedence_RPAR_ "Definition of example")`. It refers to the `[y](Terms/Identifiers/#A___y-_LPAR_in-Longer-Identifier-Prefixes-Take-Precedence_RPAR_ "Definition of example")` field of `[y.y](Terms/Identifiers/#y___y-_LPAR_in-Longer-Identifier-Prefixes-Take-Precedence_RPAR_ "Definition of example")`, because the name `[y.y](Terms/Identifiers/#y___y-_LPAR_in-Longer-Identifier-Prefixes-Take-Precedence_RPAR_ "Definition of example")` is a longer prefix of `y.y.y` than the name `[y](Terms/Identifiers/#y-_LPAR_in-Longer-Identifier-Prefixes-Take-Precedence_RPAR_ "Definition of example")`:
``"longer"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [y.y](Terms/Identifiers/#y___y-_LPAR_in-Longer-Identifier-Prefixes-Take-Precedence_RPAR_ "Definition of example").[y](Terms/Identifiers/#A___y-_LPAR_in-Longer-Identifier-Prefixes-Take-Precedence_RPAR_ "Definition of example") `
```
"longer"
```

[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgIKIO4At4IFCMQJ6IBciAyuAJYB2A5jgCbaUBuNtiASvAA5g45QkGHCQAhdFlz4ipZI2Zs6XXvwUAzQiUQTiAXkSAL8kMAiYBgD2YENhOBL8jsbCAOlkoSB0wBsLdW45wAYngWAEMvFwJXIA"\))
Current Namespace Contents Take Precedence Over Opened Namespaces
When an identifier could refer either to a name defined in a prefix of the current namespace or to an opened namespace, the former takes precedence.
`[namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") A def x := "A.x" end A  [namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") B def x := "B.x" [namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") C [open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") A `"B.x"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [x](Terms/Identifiers/#B___x-_LPAR_in-Current-Namespace-Contents-Take-Precedence-Over-Opened-Namespaces_RPAR_ "Definition of example") `
Even though `A` was opened more recently than the declaration of `[B.x](Terms/Identifiers/#B___x-_LPAR_in-Current-Namespace-Contents-Take-Precedence-Over-Opened-Namespaces_RPAR_ "Definition of example")`, the identifier `x` resolves to `[B.x](Terms/Identifiers/#B___x-_LPAR_in-Current-Namespace-Contents-Take-Precedence-Over-Opened-Namespaces_RPAR_ "Definition of example")` rather than `[A.x](Terms/Identifiers/#A___x-_LPAR_in-Current-Namespace-Contents-Take-Precedence-Over-Opened-Namespaces_RPAR_ "Definition of example")` because `B` is a prefix of the current namespace `B.C`.
``"B.x"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [x](Terms/Identifiers/#B___x-_LPAR_in-Current-Namespace-Contents-Take-Precedence-Over-Opened-Namespaces_RPAR_ "Definition of example") `
```
"B.x"
```

[Live ↪](javascript:openLiveLink\("HYQwtgpgzgDiDGEAEBBAUAEwgMyQDyQC4BeJAIhQDo8y0JgNU01RJYFkAhTHfI0sp2q1W0OIiQBhNAHsY9JgGIIANxAAbfM2VrNeIA"\))
Ambiguous Identifiers
In this example, `x` could refer either to `[A.x](Terms/Identifiers/#A___x-_LPAR_in-Ambiguous-Identifiers_RPAR_ "Definition of example")` or `[B.x](Terms/Identifiers/#B___x-_LPAR_in-Ambiguous-Identifiers_RPAR_ "Definition of example")`, and neither takes precedence. Because both have the same type, it is an error.
`def A.x := "A.x" def B.x := "B.x" [open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") A [open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") B [#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") `Ambiguous term   x Possible interpretations:   [B.x](Terms/Identifiers/#B___x-_LPAR_in-Ambiguous-Identifiers_RPAR_ "Definition of example") : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")      [A.x](Terms/Identifiers/#A___x-_LPAR_in-Ambiguous-Identifiers_RPAR_ "Definition of example") : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`x `
```
Ambiguous term
  x
Possible interpretations:
  [B.x](Terms/Identifiers/#B___x-_LPAR_in-Ambiguous-Identifiers_RPAR_ "Definition of example") : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
  
  [A.x](Terms/Identifiers/#A___x-_LPAR_in-Ambiguous-Identifiers_RPAR_ "Definition of example") : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

Disambiguation via Typing
When otherwise-ambiguous names have different types, the types are used to disambiguate:
`def C.x := "C.x" def D.x := 3 [open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") C [open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") D `"C.x"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ([x](Terms/Identifiers/#C___x-_LPAR_in-Disambiguation-via-Typing_RPAR_ "Definition of example") : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) `
```
"C.x"
```

[Live ↪](javascript:openLiveLink\("CYUwZgBAwgdAHhAXAXggIlnNAoUkAi8SqAzNgPYAOIAdtBdXftgMQgBuAhgDYQAUCRBADKAFwBOASxoBzAJRA"\))
##  13.1.1. Leading `.`[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Terms--Identifiers--Leading--___ "Permalink")
When an identifier begins with a dot (`.`), the type that the elaborator expects for the expression is used to resolve it, rather than the current namespace and set of open namespaces. [Generalized field notation](Terms/Function-Application/#--tech-term-generalized-field-notation) is related: this _leading dot notation_ uses the expected type of the identifier to resolve it to a name, while field notation uses the inferred type of the term immediately prior to the dot.
Identifiers with a leading `.` are to be looked up in the _expected type's namespace_. If the type expected for a term is a constant applied to zero or more arguments, then its namespace is the constant's name. If the type is not an application of a constant (e.g., a function, a metavariable, or a universe) then it doesn't have a namespace.
If the name is not found in the expected type's namespace, but the constant can be unfolded to yield another constant, then its namespace is consulted. This process is repeated until something other than an application of a constant is encountered, or until the constant can't be unfolded.
Leading `.`
The expected type for `[.replicate](Basic-Types/Linked-Lists/#List___replicate "Documentation for List.replicate")` is `List Unit`. This type's namespace is `List`, so `[.replicate](Basic-Types/Linked-Lists/#List___replicate "Documentation for List.replicate")` resolves to `[List.replicate](Basic-Types/Linked-Lists/#List___replicate "Documentation for List.replicate")`.
``[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") show [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") from [.replicate](Basic-Types/Linked-Lists/#List___replicate "Documentation for List.replicate") 3 () `
```
[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

[Live ↪](javascript:openLiveLink\("MQUwbghgNgBAzgCwPYHcYBkCWcAuMCqAdpngGYBOSAtjAHTkgAOUmAxhDiDAMwwAUASiA"\))
Leading `.` and Unfolding Definitions
The expected type for `[.replicate](Basic-Types/Linked-Lists/#List___replicate "Documentation for List.replicate")` is `MyList Unit`. This type's namespace is `MyList`, but there is no definition `MyList.replicate`. Unfolding `[MyList](Terms/Identifiers/#MyList-_LPAR_in-Leading--___--and-Unfolding-Definitions_RPAR_ "Definition of example") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")` yields `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")`, so `[.replicate](Basic-Types/Linked-Lists/#List___replicate "Documentation for List.replicate")` resolves to `[List.replicate](Basic-Types/Linked-Lists/#List___replicate "Documentation for List.replicate")`.
`def MyList α := [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α `[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") show [MyList](Terms/Identifiers/#MyList-_LPAR_in-Leading--___--and-Unfolding-Definitions_RPAR_ "Definition of example") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") from [.replicate](Basic-Types/Linked-Lists/#List___replicate "Documentation for List.replicate") 3 () `
```
[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

[Live ↪](javascript:openLiveLink\("CYUwZgBAsgngMgSwM4BcKEbgCAuAvBRqGAUAMQgBuAhgDYRIAWA9gO7TzJoCqAdgmmACdGAWwgA6ASAAO1BAGNKKEBADMEABQBKIA"\))
[←13. Terms](Terms/#terms "13. Terms")[13.2. Function Types→](Terms/Function-Types/#function-types "13.2. Function Types")

[←5. Source Files and Modules](Source-Files-and-Modules/#files "5. Source Files and Modules")[7. Definitions→](Definitions/#definitions "7. Definitions")
#  6. Namespaces and Sections[🔗](find/?domain=Verso.Genre.Manual.section&name=namespaces-sections "Permalink")
Names are organized into hierarchical _namespaces_ , which are collections of names. Namespaces are the primary means of organizing APIs in Lean: they provide an ontology of operations, grouping related items. Additionally, while this is not done by giving them names in the namespace, the effects of features such as [syntax extensions](Notations-and-Macros/#language-extension), [instances](Type-Classes/#--tech-term-instances), and [attributes](Attributes/#--tech-term-Attributes) can be attached to a namespace.
Sorting operations into namespaces organizes libraries conceptually, from a global perspective. Any given Lean file will, however, typically not use all names equally. [Sections](Namespaces-and-Sections/#--tech-term-section) provide a means of ordering a local view of the globally-available collection of names, as well as a way to precisely control the scope of compiler options along with language extensions, instances, and attributes. They also allow parameters shared by many declarations to be declared centrally and propagated as needed using the ``Lean.Parser.Command.variable : command`
Declares one or more typed variables, or modifies whether already-declared variables are implicit.
Introduces variables that can be used in definitions within the same `namespace` or `section` block. When a definition mentions a variable, Lean will add it as an argument of the definition. This is useful in particular when writing many definitions that have parameters in common (see below for an example).
Variable declarations have the same flexibility as regular function parameters. In particular they can be [explicit, implicit][binder docs], or [instance implicit][tpil classes] (in which case they can be anonymous). This can be changed, for instance one can turn explicit variable `x` into an implicit one with `variable {x}`. Note that currently, you should avoid changing how variables are bound and declare new variables at the same time; see [issue 2789] for more on this topic.
In _theorem bodies_ (i.e. proofs), variables are not included based on usage in order to ensure that changes to the proof cannot change the statement of the overall theorem. Instead, variables are only available to the proof if they have been mentioned in the theorem header or in an `include` command or are instance implicit and depend only on such variables.
See [_Variables and Sections_ from Theorem Proving in Lean](https://lean-lang.org/theorem_proving_in_lean4/dependent_type_theory.html#variables-and-sections) for a more detailed discussion.
(Variables and Sections on Theorem Proving in Lean) [tpil classes]: <https://lean-lang.org/theorem_proving_in_lean4/type_classes.html> (Type classes on Theorem Proving in Lean) [binder docs]: <https://leanprover-community.github.io/mathlib4_docs/Lean/Expr.html#Lean.BinderInfo> (Documentation for the BinderInfo type) [issue 2789]: <https://github.com/leanprover/lean4/issues/2789> (Issue 2789 on github)
## Examples

```
section
  variable
    {α : Type u}      -- implicit
    (a : α)           -- explicit
    [instBEq : BEq α] -- instance implicit, named
    [Hashable α]      -- instance implicit, anonymous

  def isEqual (b : α) : Bool :=
    a == b

  #check isEqual
  -- isEqual.{u} {α : Type u} (a : α) [instBEq : BEq α] (b : α) : Bool

  variable
    {a} -- `a` is implicit now

  def eqComm {b : α} := a == b ↔ b == a

  #check eqComm
  -- eqComm.{u} {α : Type u} {a : α} [instBEq : BEq α] {b : α} : Prop
end

```

The following shows a typical use of `variable` to factor out definition arguments:

```
variable (Src : Type)

structure Logger where
  trace : List (Src × String)
#check Logger
-- Logger (Src : Type) : Type

namespace Logger
  -- switch `Src : Type` to be implicit until the `end Logger`
  variable {Src}

  def empty : Logger Src where
    trace := []
  #check empty
  -- Logger.empty {Src : Type} : Logger Src

  variable (log : Logger Src)

  def len :=
    log.trace.length
  #check len
  -- Logger.len {Src : Type} (log : Logger Src) : Nat

  variable (src : Src) [BEq Src]

  -- at this point all of `log`, `src`, `Src` and the `BEq` instance can all become arguments

  def filterSrc :=
    log.trace.filterMap
      fun (src', str') => if src' == src then some str' else none
  #check filterSrc
  -- Logger.filterSrc {Src : Type} (log : Logger Src) (src : Src) [inst✝ : BEq Src] : List String

  def lenSrc :=
    log.filterSrc src |>.length
  #check lenSrc
  -- Logger.lenSrc {Src : Type} (log : Logger Src) (src : Src) [inst✝ : BEq Src] : Nat
end Logger

```

The following example demonstrates availability of variables in proofs:

```
variable
  {α : Type}    -- available in the proof as indirectly mentioned through `a`
  [ToString α]  -- available in the proof as `α` is included
  (a : α)       -- available in the proof as mentioned in the header
  {β : Type}    -- not available in the proof
  [ToString β]  -- not available in the proof

theorem ex : a = a := rfl

```

After elaboration of the proof, the following warning will be generated to highlight the unused hypothesis:

```
included section variable '[ToString α]' is not used in 'ex', consider excluding it

```

In such cases, the offending variable declaration should be moved down or into a section so that only theorems that do depend on it follow it until the end of the section.
`[`variable`](Namespaces-and-Sections/#Lean___Parser___Command___variable) command.
##  6.1. Namespaces[🔗](find/?domain=Verso.Genre.Manual.section&name=namespaces "Permalink")
Names that contain periods (that aren't inside [guillemets](Source-Files-and-Modules/#--tech-term-guillemets)) are hierarchical names; the periods separate the _components_ of a name. All but the final component of a name are the namespace, while the final component is the name itself.
Namespaces serve to group related definitions, theorems, types, and other declarations. When a namespace corresponds to a type's name, [generalized field notation](Terms/Function-Application/#--tech-term-generalized-field-notation) can be used to access its contents. In addition to organizing names, namespaces also group [syntax extensions](Notations-and-Macros/#language-extension), [attributes](Attributes/#attributes), and [instances](Type-Classes/#type-classes).
Namespaces are orthogonal to [modules](Source-Files-and-Modules/#--tech-term-module): a module is a unit of code that is elaborated, compiled, and loaded together, but there is no necessary connection between a module's name and the names that it provides. A module may contain names in any namespace, and the nesting structure of hierarchical modules is unrelated to that of hierarchical namespaces.
There is a root namespace, ordinarily denoted by simply omitting a namespace. It can be explicitly indicated by beginning a name with `_root_`. This can be necessary in contexts where a name would otherwise be interpreted relative to an ambient namespace (e.g. from a [section scope](Namespaces-and-Sections/#--tech-term-section-scope)) or local scope.
Explicit Root Namespace
Names in the current namespace take precedence over names in the root namespace. In this example, `[color](Namespaces-and-Sections/#Forest___color-_LPAR_in-Explicit-Root-Namespace_RPAR_ "Definition of example")` in the definition of `[Forest.statement](Namespaces-and-Sections/#Forest___statement-_LPAR_in-Explicit-Root-Namespace_RPAR_ "Definition of example")` refers to `[Forest.color](Namespaces-and-Sections/#Forest___color-_LPAR_in-Explicit-Root-Namespace_RPAR_ "Definition of example")`:
`def color := "yellow" [namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") Forest def color := "green" def statement := s!"Lemons are {[color](Namespaces-and-Sections/#Forest___color-_LPAR_in-Explicit-Root-Namespace_RPAR_ "Definition of example")}" end Forest ```"Lemons are green"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Forest.statement](Namespaces-and-Sections/#Forest___statement-_LPAR_in-Explicit-Root-Namespace_RPAR_ "Definition of example") `
```
"Lemons are green"
```

Within the `Forest` namespace, references to `[color](Namespaces-and-Sections/#color-_LPAR_in-Explicit-Root-Namespace_RPAR_ "Definition of example")` in the root namespace must be qualified with `_root_`:
`[namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") Forest def nextStatement :=   s!"Ripe lemons are {[_root_.color](Namespaces-and-Sections/#color-_LPAR_in-Explicit-Root-Namespace_RPAR_ "Definition of example")}, not {[color](Namespaces-and-Sections/#Forest___color-_LPAR_in-Explicit-Root-Namespace_RPAR_ "Definition of example")}" end Forest ```"Ripe lemons are yellow, not green"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Forest.nextStatement](Namespaces-and-Sections/#Forest___nextStatement-_LPAR_in-Explicit-Root-Namespace_RPAR_ "Definition of example") `
```
"Ripe lemons are yellow, not green"
```

[Live ↪](javascript:openLiveLink\("CYUwZgBAxg9gNjAThAXAXggIgJ4jggd0wCgA7AQwFsQBnAB3KhAgDElaAXY0SWBZdFgDmiECFIkeEGh3IcQ1Uh1QYaAQkwAZBTFI0I5URADefJAF8S44K3YzixAMQgAbuTi3RMgHQy5C8S4yKloGJk9ObnAIUhAADw4AZVl5RWV0YghpDQAlAEs6ZjgdPQMjYwB9RBgYDgrvM0RzABoY2pNGy2JrCPsnV3dejm9YhOT/NKA"\))
###  6.1.1. Namespaces and Section Scopes[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Namespaces-and-Sections--Namespaces--Namespaces-and-Section-Scopes "Permalink")
Every [section scope](Namespaces-and-Sections/#--tech-term-section-scope) has a [current namespace](Namespaces-and-Sections/#--tech-term-current-namespace), which is determined by the ``Lean.Parser.Command.namespace : command`
`namespace <id>` opens a section with label `<id>` that influences naming and name resolution inside the section:
  * Declarations names are prefixed: `def seventeen : ℕ := 17` inside a namespace `Nat` is given the full name `Nat.seventeen`.
  * Names introduced by `export` declarations are also prefixed by the identifier.
  * All names starting with `<id>.` become available in the namespace without the prefix. These names are preferred over names introduced by outer namespaces or `open`.
  * Within a namespace, declarations can be `protected`, which excludes them from the effects of opening the namespace.


As with `section`, namespaces can be nested and the scope of a namespace is terminated by a corresponding `end <id>` or the end of the file.
`namespace` also acts like `section` in delimiting the scope of `variable`, `open`, and other scoped commands.
`[`namespace`](Namespaces-and-Sections/#Lean___Parser___Command___namespace) command.The ``Lean.Parser.Command.namespace : command`
`namespace <id>` opens a section with label `<id>` that influences naming and name resolution inside the section:
  * Declarations names are prefixed: `def seventeen : ℕ := 17` inside a namespace `Nat` is given the full name `Nat.seventeen`.
  * Names introduced by `export` declarations are also prefixed by the identifier.
  * All names starting with `<id>.` become available in the namespace without the prefix. These names are preferred over names introduced by outer namespaces or `open`.
  * Within a namespace, declarations can be `protected`, which excludes them from the effects of opening the namespace.


As with `section`, namespaces can be nested and the scope of a namespace is terminated by a corresponding `end <id>` or the end of the file.
`namespace` also acts like `section` in delimiting the scope of `variable`, `open`, and other scoped commands.
`[`namespace`](Namespaces-and-Sections/#Lean___Parser___Command___namespace) command is described in the [section on commands that introduce section scopes](Namespaces-and-Sections/#scope-commands). Names that are declared within the section scope are added to the current namespace. If the declared name has more than one component, then its namespace is nested within the current namespace; the body of the declaration's current namespace is the nested namespace. Section scopes also include a set of _opened namespaces_ , which are namespaces whose contents are in scope without additional qualification. [Resolving](Terms/Identifiers/#--tech-term-resolving) an identifier to a particular name takes the current namespace and opened namespaces into account. However, protected declarations (that is, those with the `protected` [modifier](Definitions/Modifiers/#declaration-modifiers)) are not brought into scope when their namespace is opened. The rules for resolving identifiers into names that take the current namespace and opened namespaces into account are described in the [section on identifiers as terms](Terms/Identifiers/#identifiers-and-resolution).
Current Namespace
Defining an inductive type results in the type's constructors being placed in its namespace, in this case as `[HotDrink.coffee](Namespaces-and-Sections/#HotDrink___coffee-_LPAR_in-Current-Namespace_RPAR_ "Definition of example")`, `[HotDrink.tea](Namespaces-and-Sections/#HotDrink___tea-_LPAR_in-Current-Namespace_RPAR_ "Definition of example")`, and `[HotDrink.cocoa](Namespaces-and-Sections/#HotDrink___cocoa-_LPAR_in-Current-Namespace_RPAR_ "Definition of example")`.
`inductive HotDrink where   | coffee   | tea   | cocoa `
Outside the namespace, these names must be qualified unless the namespace is opened:
``[HotDrink.tea](Namespaces-and-Sections/#HotDrink___tea-_LPAR_in-Current-Namespace_RPAR_ "Definition of example") : [HotDrink](Namespaces-and-Sections/#HotDrink-_LPAR_in-Current-Namespace_RPAR_ "Definition of example")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [HotDrink.tea](Namespaces-and-Sections/#HotDrink___tea-_LPAR_in-Current-Namespace_RPAR_ "Definition of example") `
```
[HotDrink.tea](Namespaces-and-Sections/#HotDrink___tea-_LPAR_in-Current-Namespace_RPAR_ "Definition of example") : [HotDrink](Namespaces-and-Sections/#HotDrink-_LPAR_in-Current-Namespace_RPAR_ "Definition of example")
```
`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") `Unknown identifier `tea``tea `
```
Unknown identifier `tea`
```
`[section](Namespaces-and-Sections/#Lean___Parser___Command___section "Documentation for syntax") [open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") HotDrink `[HotDrink.tea](Namespaces-and-Sections/#HotDrink___tea-_LPAR_in-Current-Namespace_RPAR_ "Definition of example") : [HotDrink](Namespaces-and-Sections/#HotDrink-_LPAR_in-Current-Namespace_RPAR_ "Definition of example")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [tea](Namespaces-and-Sections/#HotDrink___tea-_LPAR_in-Current-Namespace_RPAR_ "Definition of example") end `
```
[HotDrink.tea](Namespaces-and-Sections/#HotDrink___tea-_LPAR_in-Current-Namespace_RPAR_ "Definition of example") : [HotDrink](Namespaces-and-Sections/#HotDrink-_LPAR_in-Current-Namespace_RPAR_ "Definition of example")
```

If a function is defined directly inside the `HotDrink` namespace, then the body of the function is elaborated with the current namespace set to `HotDrink`. The constructors are in scope:
`def HotDrink.ofString? : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [HotDrink](Namespaces-and-Sections/#HotDrink-_LPAR_in-Current-Namespace_RPAR_ "Definition of example")   | "coffee" => [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [coffee](Namespaces-and-Sections/#HotDrink___coffee-_LPAR_in-Current-Namespace_RPAR_ "Definition of example")   | "tea" => [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [tea](Namespaces-and-Sections/#HotDrink___tea-_LPAR_in-Current-Namespace_RPAR_ "Definition of example")   | "cocoa" => [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [cocoa](Namespaces-and-Sections/#HotDrink___cocoa-_LPAR_in-Current-Namespace_RPAR_ "Definition of example")   | _ => [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") `
Defining another inductive type creates a new namespace:
`inductive ColdDrink where   | water   | juice `
From within the `HotDrink` namespace, `[HotDrink.toString](Namespaces-and-Sections/#HotDrink___toString-_LPAR_in-Current-Namespace_RPAR_ "Definition of example")` can be defined without an explicit prefix. Defining a function in the `ColdDrink` namespace requires an explicit `_root_` qualifier to avoid defining `HotDrink.ColdDrink.toString`:
`[namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") HotDrink  def toString : [HotDrink](Namespaces-and-Sections/#HotDrink-_LPAR_in-Current-Namespace_RPAR_ "Definition of example") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")   | [coffee](Namespaces-and-Sections/#HotDrink___coffee-_LPAR_in-Current-Namespace_RPAR_ "Definition of example") => "coffee"   | [tea](Namespaces-and-Sections/#HotDrink___tea-_LPAR_in-Current-Namespace_RPAR_ "Definition of example") => "tea"   | [cocoa](Namespaces-and-Sections/#HotDrink___cocoa-_LPAR_in-Current-Namespace_RPAR_ "Definition of example") => "cocoa"  def _root_.ColdDrink.toString : [ColdDrink](Namespaces-and-Sections/#ColdDrink-_LPAR_in-Current-Namespace_RPAR_ "Definition of example") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")   | [.water](Namespaces-and-Sections/#ColdDrink___water-_LPAR_in-Current-Namespace_RPAR_ "Definition of example") => "water"   | [.juice](Namespaces-and-Sections/#ColdDrink___juice-_LPAR_in-Current-Namespace_RPAR_ "Definition of example") => "juice"  end HotDrink `
[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABACQPYwCICdQGtkB3AC0R0QChlkAfZKdAMycSpvpkQENq6H0jXpQDEUMlEIZseEPgB0XYQGdEsYOhCV0AB0Qg0mXAVHi1hJZX1hKlMIiaGZBecwDKMWQHMA/MgBcyB7eyIBJhMgA8jpwmk7Gcnz0AESMLGxJyAC8AHzIyugAtiiprOz8SUoZOXmFKJYcyCmC6NxVuflFAkKJyAD6WbkgmlSUoJDqSMgAwugANmDxhKTkZfRE3Fw4PQBWEMBQIyDcRco63Adxsvi29o4w6MGgXgGXBGFBnk89JWwDjT+IJI9JR/Co8IENRhCUFQlpAuwOPo4dCYXryGbzRaKB6fEDPQIYhZXd6PPE9eTrTagynkCH8eS7fYoapJRkHeHWV5yIA"\))
The ``Lean.Parser.Command.open : command`
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

`[`open`](Namespaces-and-Sections/#Lean___Parser___Command___open) command opens a namespace, making its contents available in the current section scope. There are many variations on opening namespaces, providing flexibility in managing the local scope.
syntaxOpening Namespaces
The ``Lean.Parser.Command.open : command`
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

`[`open`](Namespaces-and-Sections/#Lean___Parser___Command___open) command is used to open a namespace:

```
command ::= ...
    | 


Makes names from other namespaces visible without writing the namespace prefix.


Names that are made available with open are visible within the current section or namespace
block. This makes referring to (type) definitions and theorems easier, but note that it can also
make [scoped instances], notations, and attributes from a different namespace available.


The open command can be used in a few different ways:




  * 

open Some.Namespace.Path1 Some.Namespace.Path2 makes all non-protected names in
Some.Namespace.Path1 and Some.Namespace.Path2 available without the prefix, so that
Some.Namespace.Path1.x and Some.Namespace.Path2.y can be referred to by writing only x and
y.




  * 

open Some.Namespace.Path hiding def1 def2 opens all non-protected names in Some.Namespace.Path
except def1 and def2.




  * 

open Some.Namespace.Path (def1 def2) only makes Some.Namespace.Path.def1 and
Some.Namespace.Path.def2 available without the full prefix, so Some.Namespace.Path.def3 would
be unaffected.


This works even if def1 and def2 are protected.




  * 

open Some.Namespace.Path renaming def1 → def1', def2 → def2' same as open Some.Namespace.Path (def1 def2) but def1/def2's names are changed to def1'/def2'.


This works even if def1 and def2 are protected.




  * 

open scoped Some.Namespace.Path1 Some.Namespace.Path2 **only** opens [scoped instances],
notations, and attributes from Namespace1 and Namespace2; it does **not** make any other name
available.




  * 

open <any of the open shapes above> in makes the names open-ed visible only in the next
command or expression.






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

` open openDecl
```

open declarationOpening Entire Namespaces
A sequence of one or more identifiers results in each namespace in the sequence being opened:

```



openDecl is the body of an open declaration (see open) 


openDecl ::= ...
    | ident ident*
```

Each namespace in the sequence is considered relative to all currently-open namespaces, yielding a set of namespaces. Every namespace in this set is opened before the next namespace in the sequence is processed.
Opening Nested Namespaces
Namespaces to be opened are considered relative to the currently-open namespaces. If the same component occurs in different namespace paths, a single ``Lean.Parser.Command.open : command`
`[`open`](Namespaces-and-Sections/#Lean___Parser___Command___open) command can be used to open all of them by iteratively bringing each into scope. This example defines names in a variety of namespaces:
`[namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") A -- _root_.A def a1 := 0 [namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") B -- _root_.A.B def a2 := 0 [namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") C -- _root_.A.B.C def a3 := 0 end C end B end A [namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") B -- _root_.B def a4 := 0 [namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") C -- _root_.B.C def a5 := 0 end C end B [namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") C -- _root_.C def a6 := 0 end C `
The names are:
  * `[A.a1](Namespaces-and-Sections/#A___a1-_LPAR_in-Opening-Nested-Namespaces_RPAR_ "Definition of example")`
  * `[A.B.a2](Namespaces-and-Sections/#A___B___a2-_LPAR_in-Opening-Nested-Namespaces_RPAR_ "Definition of example")`
  * `[A.B.C.a3](Namespaces-and-Sections/#A___B___C___a3-_LPAR_in-Opening-Nested-Namespaces_RPAR_ "Definition of example")`
  * `[B.a4](Namespaces-and-Sections/#B___a4-_LPAR_in-Opening-Nested-Namespaces_RPAR_ "Definition of example")`
  * `[B.C.a5](Namespaces-and-Sections/#B___C___a5-_LPAR_in-Opening-Nested-Namespaces_RPAR_ "Definition of example")`
  * `[C.a6](Namespaces-and-Sections/#C___a6-_LPAR_in-Opening-Nested-Namespaces_RPAR_ "Definition of example")`


All six names can be brought into scope with a single iterated ``Lean.Parser.Command.open : command`
`[`open`](Namespaces-and-Sections/#Lean___Parser___Command___open) command:
`[section](Namespaces-and-Sections/#Lean___Parser___Command___section "Documentation for syntax") [open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") A B C example := [[a1](Namespaces-and-Sections/#A___a1-_LPAR_in-Opening-Nested-Namespaces_RPAR_ "Definition of example"), [a2](Namespaces-and-Sections/#A___B___a2-_LPAR_in-Opening-Nested-Namespaces_RPAR_ "Definition of example"), [a3](Namespaces-and-Sections/#A___B___C___a3-_LPAR_in-Opening-Nested-Namespaces_RPAR_ "Definition of example"), [a4](Namespaces-and-Sections/#B___a4-_LPAR_in-Opening-Nested-Namespaces_RPAR_ "Definition of example"), [a5](Namespaces-and-Sections/#B___C___a5-_LPAR_in-Opening-Nested-Namespaces_RPAR_ "Definition of example"), [a6](Namespaces-and-Sections/#C___a6-_LPAR_in-Opening-Nested-Namespaces_RPAR_ "Definition of example")] end `
If the initial namespace in the command is `A.B` instead, then neither `_root_.A`, `_root_.B`, nor `_root_.B.C` is opened:
`[section](Namespaces-and-Sections/#Lean___Parser___Command___section "Documentation for syntax") [open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") A.B C example := [`Unknown identifier `a1``a1, [a2](Namespaces-and-Sections/#A___B___a2-_LPAR_in-Opening-Nested-Namespaces_RPAR_ "Definition of example"), [a3](Namespaces-and-Sections/#A___B___C___a3-_LPAR_in-Opening-Nested-Namespaces_RPAR_ "Definition of example"), `Unknown identifier `a4``a4, `Unknown identifier `a5``a5, [a6](Namespaces-and-Sections/#C___a6-_LPAR_in-Opening-Nested-Namespaces_RPAR_ "Definition of example")] end `
```
Unknown identifier `a1`
```

```
Unknown identifier `a4`
```

```
Unknown identifier `a5`
```

Opening `A.B` makes `A.B.C` visible as `C` along with `_root_.C`, so the subsequent `C` opens both.
[Live ↪](javascript:openLiveLink\("HYQwtgpgzgDiDGEAEBBJBadSD6AnA9vgC7YB0KAUACYQBmSIAjEgFwC8SADBaJLAsgBCGLHkIlypQdToMATKw7de0OIiQBhETgLEyKKaQ0z6IAMyKuFCMCqbrtpNJt3KK/uuGYd4stJqmACyWyuCqApraYnqGxgEMAKwhDnbGLk48YR7IWt7REnGyIABsyenGFFAQ8EQAlvjAFPgwNqhO9hAAHuAwADbI7EgA2kwANPLj5pOBkwmTxQC6KUA"\))
open declarationHiding Names
A `hiding` declaration specifies a set of names that should _not_ be brought into scope. In contrast to opening an entire namespace, the provided identifier must uniquely designate a namespace to be opened.

```



openDecl is the body of an open declaration (see open) 


openDecl ::= ...
    | ident hiding ident ident*
```

open declarationRenaming
A `renaming` declaration allows some names from the opened namespace to be renamed; they are accessible under the new name in the current section scope. The provided identifier must uniquely designate a namespace to be opened.

```



openDecl is the body of an open declaration (see open) 


openDecl ::= ...
    | ident renaming (ident → ident),*
```

An ASCII arrow (`->`) may be used instead of the Unicode arrow (`→`).
open declarationRestricted Opening
Parentheses indicate that _only_ the names listed in the parentheses should be brought into scope.

```



openDecl is the body of an open declaration (see open) 


openDecl ::= ...
    | ident (ident ident*)
```

The indicated namespace is added to each currently-opened namespace, and each name is considered in each resulting namespace. All of the listed names must be unambiguous; that is, they must exist in exactly one of the considered namespaces.
open declarationScoped Declarations Only
The `scoped` keyword indicates that all scoped attributes, instances, and syntax from the provided namespaces should be opened, while not making any of the names available.

```



openDecl is the body of an open declaration (see open) 


openDecl ::= ...
    | scoped ident ident*
```

Opening Scoped Declarations
In this example, a scoped [notation](Notations-and-Macros/Notations/#--tech-term-notation) and a definition are created in the namespace `NS`:
`[namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") NS scoped [notation](Notations-and-Macros/Notations/#Lean___Parser___Command___notation "Documentation for syntax") "{!{" e "}!}" => (e, e) def three := 3 end NS `
Outside of the namespace, the notation is not available:

```
def x := {!{ "pear" }unexpected token '!'; expected '}'!}
```

```
<example>:1:21-1:22: unexpected token '!'; expected '}'
```

An `open scoped` command makes the notation available:
`[open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") [scoped](Namespaces-and-Sections/#Lean___Parser___Command___openScoped "Documentation for syntax") NS def x := {!{ "pear" }!} `
However, the name `[NS.three](Namespaces-and-Sections/#NS___three-_LPAR_in-Opening-Scoped-Declarations_RPAR_ "Definition of example")` is not in scope:
`def y := `Unknown identifier `three``three `
```
Unknown identifier `three`
```

[Live ↪](javascript:openLiveLink\("HYQwtgpgzgDiDGEAEA5AygKCvA9jCAJksDgC4ikCWOwSARAN4CEDdSydAvk52wLwA+JAAoIAGnYBKDAQgAzJKQAWAJwjIAXHyQBmDBGBF0QA"\))
###  6.1.2. Exporting Names[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Namespaces-and-Sections--Namespaces--Exporting-Names "Permalink")
_Exporting_ a name makes it available in the current namespace. Unlike a definition, this alias is completely transparent: uses are resolved directly to the original name. Exporting a name to the root namespace makes it available without qualification; the Lean standard library does this for names such as the constructors of `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` and key type class methods such as `get`.
syntaxExporting Names
The `export` command adds names from other namespaces to the current namespace, as if they had been declared in it. When the current namespace is opened, these exported names are also brought into scope.

```
command ::= ...
    | 


Adds names from other namespaces to the current namespace.


The command export Some.Namespace (name₁ name₂) makes name₁ and name₂:




  * visible in the current namespace without prefix Some.Namespace, like open, and


  * visible from outside the current namespace N as N.name₁ and N.name₂.




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

`export ident (ident*)
```

Internally, exported names are registered as aliases of their targets. From the perspective of the kernel, only the original name exists; the elaborator resolves aliases as part of [resolving](Terms/Identifiers/#--tech-term-resolving) identifiers to names.
Exported Names
The declaration of the [inductive type](The-Type-System/Inductive-Types/#--tech-term-Inductive-types) `[Veg.Leafy](Namespaces-and-Sections/#Veg___Leafy-_LPAR_in-Exported-Names_RPAR_ "Definition of example")` establishes the constructors `[Veg.Leafy.spinach](Namespaces-and-Sections/#Veg___Leafy___spinach-_LPAR_in-Exported-Names_RPAR_ "Definition of example")` and `[Veg.Leafy.cabbage](Namespaces-and-Sections/#Veg___Leafy___cabbage-_LPAR_in-Exported-Names_RPAR_ "Definition of example")`:
`[namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") Veg inductive Leafy where   | spinach   | cabbage [export](Namespaces-and-Sections/#Lean___Parser___Command___export "Documentation for syntax") Leafy ([spinach](Namespaces-and-Sections/#Veg___Leafy___spinach-_LPAR_in-Exported-Names_RPAR_ "Definition of example")) end Veg [export](Namespaces-and-Sections/#Lean___Parser___Command___export "Documentation for syntax") Veg.Leafy ([cabbage](Namespaces-and-Sections/#Veg___Leafy___cabbage-_LPAR_in-Exported-Names_RPAR_ "Definition of example")) `
The first `export` command makes `[Veg.Leafy.spinach](Namespaces-and-Sections/#Veg___Leafy___spinach-_LPAR_in-Exported-Names_RPAR_ "Definition of example")` accessible as `[Veg.spinach](Namespaces-and-Sections/#Veg___Leafy___spinach-_LPAR_in-Exported-Names_RPAR_ "Definition of example")` because the [current namespace](Namespaces-and-Sections/#--tech-term-current-namespace) is `Veg`. The second makes `[Veg.Leafy.cabbage](Namespaces-and-Sections/#Veg___Leafy___cabbage-_LPAR_in-Exported-Names_RPAR_ "Definition of example")` accessible as `[cabbage](Namespaces-and-Sections/#Veg___Leafy___cabbage-_LPAR_in-Exported-Names_RPAR_ "Definition of example")`, because the current namespace is the root namespace.
[Live ↪](javascript:openLiveLink\("HYQwtgpgzgDiDGEAEA1CBzAUAS2AEwFd4AXbAN2QBkIQAzATyQHcALCAJwkySQB8lYuBC258k8EACNJIdFwgAPGAHt2xJNTqMAFINDwWASkwR8qDCaWr1adADpNDJNonTZEQ0A"\))
##  6.2. Section Scopes[🔗](find/?domain=Verso.Genre.Manual.section&name=scopes "Permalink")
Many commands have an effect for the current _section scope_ (sometimes just called “scope” when clear). Every Lean module has a section scope. Nested scopes are created via the ``Lean.Parser.Command.namespace : command`
`namespace <id>` opens a section with label `<id>` that influences naming and name resolution inside the section:
  * Declarations names are prefixed: `def seventeen : ℕ := 17` inside a namespace `Nat` is given the full name `Nat.seventeen`.
  * Names introduced by `export` declarations are also prefixed by the identifier.
  * All names starting with `<id>.` become available in the namespace without the prefix. These names are preferred over names introduced by outer namespaces or `open`.
  * Within a namespace, declarations can be `protected`, which excludes them from the effects of opening the namespace.


As with `section`, namespaces can be nested and the scope of a namespace is terminated by a corresponding `end <id>` or the end of the file.
`namespace` also acts like `section` in delimiting the scope of `variable`, `open`, and other scoped commands.
`[`namespace`](Namespaces-and-Sections/#Lean___Parser___Command___namespace) and ``Lean.Parser.Command.section : command`
A `section`/`end` pair delimits the scope of `variable`, `include`, `open`, `set_option`, and `local` commands. Sections can be nested. `section <id>` provides a label to the section that has to appear with the matching `end`. In either case, the `end` can be omitted, in which case the section is closed at the end of the file.
`[`section`](Namespaces-and-Sections/#Lean___Parser___Command___section) commands, as well as the ``Lean.Parser.Command.in : command``[`in`](Namespaces-and-Sections/#Lean___Parser___Command___in) command combinator.
The following data are tracked in section scopes: 

The Current Namespace
    
The _current namespace_ is the namespace into which new declarations will be defined. Additionally, [name resolution](Terms/Identifiers/#--tech-term-resolving) includes all prefixes of the current namespace in the scope for global names. 

Opened Namespaces
    
When a namespace is _opened_ , its names become available without an explicit prefix in the current scope. Additionally, scoped attributes and [scoped syntax extensions](Notations-and-Macros/Defining-New-Syntax/#syntax-rules) in namespaces that have been opened are active in the current section scope. 

Options
    
Compiler options are reverted to their original values at the end of the scope in which they were modified. 

Section Variables
    
[Section variables](Namespaces-and-Sections/#--tech-term-Section-variables) are names (or [instance implicit](Type-Classes/#--tech-term-instance-implicit) parameters) that are automatically added as parameters to definitions. They are also added as universally-quantified assumptions to theorems when they occur in the theorem's statement.
###  6.2.1. Controlling Section Scopes[🔗](find/?domain=Verso.Genre.Manual.section&name=scope-commands "Permalink")
The ``Lean.Parser.Command.section : command`
A `section`/`end` pair delimits the scope of `variable`, `include`, `open`, `set_option`, and `local` commands. Sections can be nested. `section <id>` provides a label to the section that has to appear with the matching `end`. In either case, the `end` can be omitted, in which case the section is closed at the end of the file.
`[`section`](Namespaces-and-Sections/#Lean___Parser___Command___section) command creates a new section scope, but does not modify the current namespace, opened namespaces, or section variables. Changes made to the section scope are reverted when the section ends. Additionally, a section may cause a set of modifiers to be applied by default to all declarations in the section. Sections may optionally be named; the ``Lean.Parser.Command.end : command`
`end` closes a `section` or `namespace` scope. If the scope is named `<id>`, it has to be closed with `end <id>`. The `end` command is optional at the end of a file.
``end` command that closes a named section must use the same name. If section names have multiple components (that is, if they contain `.`-separated names), then multiple nested sections are introduced. Section names have no other effect, and are a readability aid.
syntaxSections
The ``Lean.Parser.Command.section : command`
A `section`/`end` pair delimits the scope of `variable`, `include`, `open`, `set_option`, and `local` commands. Sections can be nested. `section <id>` provides a label to the section that has to appear with the matching `end`. In either case, the `end` can be omitted, in which case the section is closed at the end of the file.
`[`section`](Namespaces-and-Sections/#Lean___Parser___Command___section) command creates a section scope that lasts either until an `end` command or the end of the file. The section header, if present, modifies the declarations in the section.

```
command ::= ...
    | 


A section/end pair delimits the scope of variable, include, open, set_option, and local
commands. Sections can be nested. section <id> provides a label to the section that has to appear
with the matching end. In either case, the end can be omitted, in which case the section is
closed at the end of the file.


[sectionHeader](Namespaces-and-Sections/#Lean___Parser___Command___sectionHeader-next) section ident?
```

syntaxSection Headers
A section header, if present, modifies the declarations in the section.

```
[sectionHeader](Namespaces-and-Sections/#Lean___Parser___Command___sectionHeader-next) ::= ...
    | (@[expose])?
      public? noncomputable? meta?
```

If the header includes `noncomputable`, then the definitions in the section are all considered to be noncomputable, and no compiled code is generated for them. This is needed for definitions that rely on noncomputational reasoning principles such as the Axiom of Choice.
The remaining modifiers are only useful in [modules](Source-Files-and-Modules/#--tech-term-module). If the header includes `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")expose[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")`, then all definitions in the section are [exposed](Source-Files-and-Modules/#--tech-term-exposed). If it includes `public`, then the declarations in such a public section are public, rather than private, by default. If it includes `meta`, then the section's declarations are all placed in the [meta phase](Source-Files-and-Modules/#--tech-term-meta-phase).
Named Section
The name `[english](Namespaces-and-Sections/#Greetings___english-_LPAR_in-Named-Section_RPAR_ "Definition of example")` is defined in the `Greetings` namespace.
`def Greetings.english := "Hello" `
Outside its namespace, it cannot be evaluated.
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") `Unknown identifier `english``english `
```
Unknown identifier `english`
```

Opening a section allows modifications to the global scope to be contained. This section is named `Greetings`.
`[section](Namespaces-and-Sections/#Lean___Parser___Command___section "Documentation for syntax") Greetings `
Even though the section name matches the definition's namespace, the name is not in scope because section names are purely for readability and ease of refactoring.
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") `Unknown identifier `english``english `
```
Unknown identifier `english`
```

Opening the namespace `Greetings` brings `[Greetings.english](Namespaces-and-Sections/#Greetings___english-_LPAR_in-Named-Section_RPAR_ "Definition of example")` as `[english](Namespaces-and-Sections/#Greetings___english-_LPAR_in-Named-Section_RPAR_ "Definition of example")`:
`[open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Greetings  `"Hello"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [english](Namespaces-and-Sections/#Greetings___english-_LPAR_in-Named-Section_RPAR_ "Definition of example") `
```
"Hello"
```

The section's name must be used to close it.
``Missing name after `end`: Expected the current scope name `Greetings`  Hint: To end the current scope `Greetings`, specify its name:   end ̲G̲r̲e̲e̲t̲i̲n̲g̲s̲`end `
```
Missing name after `end`: Expected the current scope name `Greetings`

Hint: To end the current scope `Greetings`, specify its name:
  end ̲G̲r̲e̲e̲t̲i̲n̲g̲s̲
```
`end Greetings `
When the section is closed, the effects of the ``Lean.Parser.Command.open : command`
`[`open`](Namespaces-and-Sections/#Lean___Parser___Command___open) command are reverted.
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") `Unknown identifier `english``english `
```
Unknown identifier `english`
```

[Live ↪](javascript:openLiveLink\("CYUwZgBA4gTiIBcCWA7A5gZwHQnQGyQwAsIAuAXggCIAJEPPAeyoCgWMQBjZRlaORKkxtGAB1z94ydBjYBiEADcAhngi40BYm1zBJgmUA"\))
The ``Lean.Parser.Command.namespace : command`
`namespace <id>` opens a section with label `<id>` that influences naming and name resolution inside the section:
  * Declarations names are prefixed: `def seventeen : ℕ := 17` inside a namespace `Nat` is given the full name `Nat.seventeen`.
  * Names introduced by `export` declarations are also prefixed by the identifier.
  * All names starting with `<id>.` become available in the namespace without the prefix. These names are preferred over names introduced by outer namespaces or `open`.
  * Within a namespace, declarations can be `protected`, which excludes them from the effects of opening the namespace.


As with `section`, namespaces can be nested and the scope of a namespace is terminated by a corresponding `end <id>` or the end of the file.
`namespace` also acts like `section` in delimiting the scope of `variable`, `open`, and other scoped commands.
`[`namespace`](Namespaces-and-Sections/#Lean___Parser___Command___namespace) command creates a new section scope. Within this section scope, the current namespace is the name provided in the command, interpreted relative to the current namespace in the surrounding section scope. Like sections, changes made to the section scope are reverted when the namespace's scope ends.
To close a namespace, the ``Lean.Parser.Command.end : command`
`end` closes a `section` or `namespace` scope. If the scope is named `<id>`, it has to be closed with `end <id>`. The `end` command is optional at the end of a file.
``end` command requires a suffix of the current namespace, which is removed. All section scopes introduced by the ``Lean.Parser.Command.namespace : command`
`namespace <id>` opens a section with label `<id>` that influences naming and name resolution inside the section:
  * Declarations names are prefixed: `def seventeen : ℕ := 17` inside a namespace `Nat` is given the full name `Nat.seventeen`.
  * Names introduced by `export` declarations are also prefixed by the identifier.
  * All names starting with `<id>.` become available in the namespace without the prefix. These names are preferred over names introduced by outer namespaces or `open`.
  * Within a namespace, declarations can be `protected`, which excludes them from the effects of opening the namespace.


As with `section`, namespaces can be nested and the scope of a namespace is terminated by a corresponding `end <id>` or the end of the file.
`namespace` also acts like `section` in delimiting the scope of `variable`, `open`, and other scoped commands.
`[`namespace`](Namespaces-and-Sections/#Lean___Parser___Command___namespace) command that introduced part of that suffix are closed.
syntaxNamespace Declarations
The `namespace` command modifies the current namespace by appending the provided identifier. It creates a section scope that lasts either until an ``Lean.Parser.Command.end : command`
`end` closes a `section` or `namespace` scope. If the scope is named `<id>`, it has to be closed with `end <id>`. The `end` command is optional at the end of a file.
``end` command or the end of the file.

```
command ::= ...
    | 


namespace <id> opens a section with label <id> that influences naming and name resolution inside
the section:




  * Declarations names are prefixed: def seventeen : ℕ := 17 inside a namespace Nat is given the
full name Nat.seventeen.


  * Names introduced by export declarations are also prefixed by the identifier.


  * All names starting with <id>. become available in the namespace without the prefix. These names
are preferred over names introduced by outer namespaces or open.


  * Within a namespace, declarations can be protected, which excludes them from the effects of
opening the namespace.




As with section, namespaces can be nested and the scope of a namespace is terminated by a
corresponding end <id> or the end of the file.


namespace also acts like section in delimiting the scope of variable, open, and other scoped commands.


namespace ident
```

syntaxSection and Namespace Terminators
Without an identifier, ``Lean.Parser.Command.end : command`
`end` closes a `section` or `namespace` scope. If the scope is named `<id>`, it has to be closed with `end <id>`. The `end` command is optional at the end of a file.
``end` closes the most recently opened section, which must be anonymous.

```
command ::= ...
    | 


end closes a section or namespace scope. If the scope is named <id>, it has to be closed
with end <id>. The end command is optional at the end of a file.


end
```

With an identifier, it closes the most recently opened section or namespace. If it is a section, the identifier must be a suffix of the concatenated names of the sections opened since the most recent ``Lean.Parser.Command.namespace : command`
`namespace <id>` opens a section with label `<id>` that influences naming and name resolution inside the section:
  * Declarations names are prefixed: `def seventeen : ℕ := 17` inside a namespace `Nat` is given the full name `Nat.seventeen`.
  * Names introduced by `export` declarations are also prefixed by the identifier.
  * All names starting with `<id>.` become available in the namespace without the prefix. These names are preferred over names introduced by outer namespaces or `open`.
  * Within a namespace, declarations can be `protected`, which excludes them from the effects of opening the namespace.


As with `section`, namespaces can be nested and the scope of a namespace is terminated by a corresponding `end <id>` or the end of the file.
`namespace` also acts like `section` in delimiting the scope of `variable`, `open`, and other scoped commands.
`[`namespace`](Namespaces-and-Sections/#Lean___Parser___Command___namespace) command. If it is a namespace, then the identifier must be a suffix of the current namespace's extensions since the most recent ``Lean.Parser.Command.section : command`
A `section`/`end` pair delimits the scope of `variable`, `include`, `open`, `set_option`, and `local` commands. Sections can be nested. `section <id>` provides a label to the section that has to appear with the matching `end`. In either case, the `end` can be omitted, in which case the section is closed at the end of the file.
`[`section`](Namespaces-and-Sections/#Lean___Parser___Command___section) that is still open; afterwards, the current namespace will have had this suffix removed.

```
command ::= ...
    | 


end closes a section or namespace scope. If the scope is named <id>, it has to be closed
with end <id>. The end command is optional at the end of a file.


end ident
```

The ``Lean.Parser.Command.mutual : command``[`end`](Definitions/Recursive-Definitions/#Lean___Parser___Command___mutual) that closes a ``Lean.Parser.Command.mutual : command``[`mutual`](Definitions/Recursive-Definitions/#Lean___Parser___Command___mutual) block is part of the syntax of ``Lean.Parser.Command.mutual : command``[`mutual`](Definitions/Recursive-Definitions/#Lean___Parser___Command___mutual), rather than the ``Lean.Parser.Command.end : command`
`end` closes a `section` or `namespace` scope. If the scope is named `<id>`, it has to be closed with `end <id>`. The `end` command is optional at the end of a file.
``end` command.
Nesting Namespaces and Sections
Namespaces and sections may be nested. A single ``Lean.Parser.Command.end : command`
``end` command may close one or more namespaces or one or more sections, but not a mix of the two.
After setting the current namespace to `A.B.C` with two separate commands, `B.C` may be removed with a single ``Lean.Parser.Command.end : command`
``end`:
`[namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") A.B [namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") C end B.C `
At this point, the current namespace is `A`.
Next, an anonymous section and the namespace `D.E` are opened:
`[section](Namespaces-and-Sections/#Lean___Parser___Command___section "Documentation for syntax") [namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") D.E `
At this point, the current namespace is `A.D.E`. An ``Lean.Parser.Command.end : command`
``end` command cannot close all three due to the intervening section:
``Invalid name after `end`: Expected `D.E`, but found `A.D.E``end A.D.E `
```
Invalid name after `end`: Expected `D.E`, but found `A.D.E`
```

Instead, namespaces and sections must be ended separately.
`end D.E end end A `
[Live ↪](javascript:openLiveLink\("HYQwtgpgzgDiDGEAEBBAdAIQFCkrByAwlhMACZIZrFZQTwAuAlgPbA7jRyJIAiaAUSwlyfQSLITUQA"\))
Rather than opening a section for a single command, the ``Lean.Parser.Command.in : command``[`in`](Namespaces-and-Sections/#Lean___Parser___Command___in) combinator can be used to create single-command section scope. The ``Lean.Parser.Command.in : command``[`in`](Namespaces-and-Sections/#Lean___Parser___Command___in) combinator is right-associative, allowing multiple scope modifications to be stacked.
syntaxLocal Section Scopes
The `in` command combinator introduces a section scope for a single command.

```
command ::= ...
    | command in
      command
```

Using ``Lean.Parser.Command.in : command``[`in`](Namespaces-and-Sections/#Lean___Parser___Command___in) for Local Scopes
The contents of a namespace can be made available for a single command using ``Lean.Parser.Command.in : command``[`in`](Namespaces-and-Sections/#Lean___Parser___Command___in).
`def Dessert.cupcake := "delicious"  [open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Dessert [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") `"delicious"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [cupcake](Namespaces-and-Sections/#Dessert___cupcake-_LPAR_in-Using--in--for-Local-Scopes_RPAR_ "Definition of example") `
After the single command, the effects of ``Lean.Parser.Command.open : command`
`[`open`](Namespaces-and-Sections/#Lean___Parser___Command___open) are reverted.
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") `Unknown identifier `cupcake``cupcake `
```
Unknown identifier `cupcake`
```

[Live ↪](javascript:openLiveLink\("CYUwZgBAIiDOsgE4BcB0BjArgB3QQwGsQIAuAXggCJQAbAS3ToHtNZKAodp7EAO2jgIUEOr3YBiEADc8NCFlyEQQA"\))
###  6.2.2. Section Variables[🔗](find/?domain=Verso.Genre.Manual.section&name=section-variables "Permalink")
_Section variables_ are parameters that are automatically added to declarations that mention them. This occurs whether or not the option `[autoImplicit](Definitions/Headers-and-Signatures/#autoImplicit "Documentation for option autoImplicit")` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`. Section variables may be implicit, strict implicit, or explicit; instance implicit section variables are treated specially.
When the name of a section variable is encountered in a non-theorem declaration, it is added as a parameter. Any instance implicit section variables that mention the variable are also added. If any of the variables that were added depend on other variables, then those variables are added as well; this process is iterated until no more dependencies remain. All section variables are added in the order in which they are declared, before all other parameters. Section variables are added only when they occur in the _statement_ of a theorem. Otherwise, modifying the proof of a theorem could change its statement if the proof term made use of a section variable.
Variables are declared using the ``Lean.Parser.Command.variable : command`
Declares one or more typed variables, or modifies whether already-declared variables are implicit.
Introduces variables that can be used in definitions within the same `namespace` or `section` block. When a definition mentions a variable, Lean will add it as an argument of the definition. This is useful in particular when writing many definitions that have parameters in common (see below for an example).
Variable declarations have the same flexibility as regular function parameters. In particular they can be [explicit, implicit][binder docs], or [instance implicit][tpil classes] (in which case they can be anonymous). This can be changed, for instance one can turn explicit variable `x` into an implicit one with `variable {x}`. Note that currently, you should avoid changing how variables are bound and declare new variables at the same time; see [issue 2789] for more on this topic.
In _theorem bodies_ (i.e. proofs), variables are not included based on usage in order to ensure that changes to the proof cannot change the statement of the overall theorem. Instead, variables are only available to the proof if they have been mentioned in the theorem header or in an `include` command or are instance implicit and depend only on such variables.
See [_Variables and Sections_ from Theorem Proving in Lean](https://lean-lang.org/theorem_proving_in_lean4/dependent_type_theory.html#variables-and-sections) for a more detailed discussion.
(Variables and Sections on Theorem Proving in Lean) [tpil classes]: <https://lean-lang.org/theorem_proving_in_lean4/type_classes.html> (Type classes on Theorem Proving in Lean) [binder docs]: <https://leanprover-community.github.io/mathlib4_docs/Lean/Expr.html#Lean.BinderInfo> (Documentation for the BinderInfo type) [issue 2789]: <https://github.com/leanprover/lean4/issues/2789> (Issue 2789 on github)
## Examples

```
section
  variable
    {α : Type u}      -- implicit
    (a : α)           -- explicit
    [instBEq : BEq α] -- instance implicit, named
    [Hashable α]      -- instance implicit, anonymous

  def isEqual (b : α) : Bool :=
    a == b

  #check isEqual
  -- isEqual.{u} {α : Type u} (a : α) [instBEq : BEq α] (b : α) : Bool

  variable
    {a} -- `a` is implicit now

  def eqComm {b : α} := a == b ↔ b == a

  #check eqComm
  -- eqComm.{u} {α : Type u} {a : α} [instBEq : BEq α] {b : α} : Prop
end

```

The following shows a typical use of `variable` to factor out definition arguments:

```
variable (Src : Type)

structure Logger where
  trace : List (Src × String)
#check Logger
-- Logger (Src : Type) : Type

namespace Logger
  -- switch `Src : Type` to be implicit until the `end Logger`
  variable {Src}

  def empty : Logger Src where
    trace := []
  #check empty
  -- Logger.empty {Src : Type} : Logger Src

  variable (log : Logger Src)

  def len :=
    log.trace.length
  #check len
  -- Logger.len {Src : Type} (log : Logger Src) : Nat

  variable (src : Src) [BEq Src]

  -- at this point all of `log`, `src`, `Src` and the `BEq` instance can all become arguments

  def filterSrc :=
    log.trace.filterMap
      fun (src', str') => if src' == src then some str' else none
  #check filterSrc
  -- Logger.filterSrc {Src : Type} (log : Logger Src) (src : Src) [inst✝ : BEq Src] : List String

  def lenSrc :=
    log.filterSrc src |>.length
  #check lenSrc
  -- Logger.lenSrc {Src : Type} (log : Logger Src) (src : Src) [inst✝ : BEq Src] : Nat
end Logger

```

The following example demonstrates availability of variables in proofs:

```
variable
  {α : Type}    -- available in the proof as indirectly mentioned through `a`
  [ToString α]  -- available in the proof as `α` is included
  (a : α)       -- available in the proof as mentioned in the header
  {β : Type}    -- not available in the proof
  [ToString β]  -- not available in the proof

theorem ex : a = a := rfl

```

After elaboration of the proof, the following warning will be generated to highlight the unused hypothesis:

```
included section variable '[ToString α]' is not used in 'ex', consider excluding it

```

In such cases, the offending variable declaration should be moved down or into a section so that only theorems that do depend on it follow it until the end of the section.
`[`variable`](Namespaces-and-Sections/#Lean___Parser___Command___variable) command.
syntaxVariable Declarations

```
command ::= ...
    | 


Declares one or more typed variables, or modifies whether already-declared variables are
  implicit.


Introduces variables that can be used in definitions within the same namespace or section block.
When a definition mentions a variable, Lean will add it as an argument of the definition. This is
useful in particular when writing many definitions that have parameters in common (see below for an
example).


Variable declarations have the same flexibility as regular function parameters. In particular they
can be [explicit, implicit][binder docs], or [instance implicit][tpil classes] (in which case they
can be anonymous). This can be changed, for instance one can turn explicit variable x into an
implicit one with variable {x}. Note that currently, you should avoid changing how variables are
bound and declare new variables at the same time; see [issue 2789] for more on this topic.


In _theorem bodies_ (i.e. proofs), variables are not included based on usage in order to ensure that
changes to the proof cannot change the statement of the overall theorem. Instead, variables are only
available to the proof if they have been mentioned in the theorem header or in an include command
or are instance implicit and depend only on such variables.


See [_Variables and Sections_ from Theorem Proving in Lean](https://lean-lang.org/theorem_proving_in_lean4/dependent_type_theory.html#variables-and-sections) for a more detailed
discussion.


(Variables and Sections on Theorem Proving in Lean) [tpil classes]:
https://lean-lang.org/theorem_proving_in_lean4/type_classes.html[](https://lean-lang.org/theorem_proving_in_lean4/type_classes.html) (Type classes on Theorem Proving in
Lean) [binder docs]:
https://leanprover-community.github.io/mathlib4_docs/Lean/Expr.html#Lean.BinderInfo[](https://leanprover-community.github.io/mathlib4_docs/Lean/Expr.html#Lean.BinderInfo) (Documentation
for the BinderInfo type) [issue 2789]: https://github.com/leanprover/lean4/issues/2789[](https://github.com/leanprover/lean4/issues/2789) (Issue 2789
on github)


## Examples


```
section
  variable
    {α : Type u}      -- implicit
    (a : α)           -- explicit
    [instBEq : BEq α] -- instance implicit, named
    [Hashable α]      -- instance implicit, anonymous

  def isEqual (b : α) : Bool :=
    a == b

  #check isEqual
  -- isEqual.{u} {α : Type u} (a : α) [instBEq : BEq α] (b : α) : Bool

  variable
    {a} -- `a` is implicit now

  def eqComm {b : α} := a == b ↔ b == a

  #check eqComm
  -- eqComm.{u} {α : Type u} {a : α} [instBEq : BEq α] {b : α} : Prop
end

```

The following shows a typical use of `variable` to factor out definition arguments:

```
variable (Src : Type)

structure Logger where
  trace : List (Src × String)
#check Logger
-- Logger (Src : Type) : Type

namespace Logger
  -- switch `Src : Type` to be implicit until the `end Logger`
  variable {Src}

  def empty : Logger Src where
    trace := []
  #check empty
  -- Logger.empty {Src : Type} : Logger Src

  variable (log : Logger Src)

  def len :=
    log.trace.length
  #check len
  -- Logger.len {Src : Type} (log : Logger Src) : Nat

  variable (src : Src) [BEq Src]

  -- at this point all of `log`, `src`, `Src` and the `BEq` instance can all become arguments

  def filterSrc :=
    log.trace.filterMap
      fun (src', str') => if src' == src then some str' else none
  #check filterSrc
  -- Logger.filterSrc {Src : Type} (log : Logger Src) (src : Src) [inst✝ : BEq Src] : List String

  def lenSrc :=
    log.filterSrc src |>.length
  #check lenSrc
  -- Logger.lenSrc {Src : Type} (log : Logger Src) (src : Src) [inst✝ : BEq Src] : Nat
end Logger

```

The following example demonstrates availability of variables in proofs:

```
variable
  {α : Type}    -- available in the proof as indirectly mentioned through `a`
  [ToString α]  -- available in the proof as `α` is included
  (a : α)       -- available in the proof as mentioned in the header
  {β : Type}    -- not available in the proof
  [ToString β]  -- not available in the proof

theorem ex : a = a := rfl

```

After elaboration of the proof, the following warning will be generated to highlight the unused hypothesis:

```
included section variable '[ToString α]' is not used in 'ex', consider excluding it

```

In such cases, the offending variable declaration should be moved down or into a section so that only theorems that do depend on it follow it until the end of the section.
`variable bracketedBinder bracketedBinder*
```

The bracketed binders allowed after `variable` match the [syntax used in definition headers](Definitions/Headers-and-Signatures/#bracketed-parameter-syntax).
Section Variables
In this section, automatic implicit parameters are disabled, but a number of section variables are defined.
`[section](Namespaces-and-Sections/#Lean___Parser___Command___section "Documentation for syntax") set_option [autoImplicit](Definitions/Headers-and-Signatures/#autoImplicit "Documentation for option autoImplicit") false [universe](The-Type-System/Universes/#Lean___Parser___Command___universe-next "Documentation for syntax") u [variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax") {α : Type u} (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) [[Zero](Type-Classes/Basic-Classes/#Zero___mk "Documentation for Zero") α] [[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") α] `
Because automatic implicit parameters are disabled and `β` is neither a section variable nor bound as a parameter of the function, the following definition fails:
`def addAll (lst : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") `Unknown identifier `β`  Note: It is not possible to treat `β` as an implicitly bound variable here because the `autoImplicit` option is set to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.`β) : `Unknown identifier `β`  Note: It is not possible to treat `β` as an implicitly bound variable here because the `autoImplicit` option is set to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.`β := lst.[foldr](Basic-Types/Linked-Lists/#List___foldr "Documentation for List.foldr") (init := 0) (· + ·) `
```
Unknown identifier `β`

Note: It is not possible to treat `β` as an implicitly bound variable here because the `autoImplicit` option is set to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
```

On the other hand, not even `xs` needs to be written directly in the definition when it uses the section variables:
`def addAll :=   xs.[foldr](Basic-Types/Linked-Lists/#List___foldr "Documentation for List.foldr") (init := 0) (· + ·) `
[Live ↪](javascript:openLiveLink\("M4UwxgLglg9gdgKFBA+jADteACAhgVwhgEkBbdAGyjCgmwDNcLQF84oA3EAJ1G3wQdc3KLgBGFENgDegRuBsALmwAVAJ7op+AL7YAFAA9gi7ABkowOrICU2ANoAtHjGyyAunYCCAEy8vXQA"\))
To add a section variable to a theorem even if it is not explicitly mentioned in the statement, mark the variable with the ``Lean.Parser.Command.include : command`
`include eeny meeny` instructs Lean to include the section `variable`s `eeny` and `meeny` in all theorems in the remainder of the current section, differing from the default behavior of conditionally including variables based on use in the theorem header. Other commands are not affected. `include` is usually followed by `in theorem ...` to limit the inclusion to the subsequent declaration.
``include` command. All variables marked for inclusion are added to all theorems. The ``Lean.Parser.Command.omit : command`
`omit` instructs Lean to not include a variable previously `include`d. Apart from variable names, it can also refer to typeclass instance variables by type using the syntax `omit [TypeOfInst]`, in which case all instance variables that unify with the given type are omitted. `omit` should usually only be used in conjunction with `in` in order to keep the section structure simple.
``omit` command removes the inclusion mark from a variable; it's typically a good idea to use it with ``Lean.Parser.Command.in : command``[`in`](Namespaces-and-Sections/#Lean___Parser___Command___in).
Included and Omitted Section Variables
This section's variables include a predicate as well as everything needed to prove that it holds universally, along with a useless extra assumption.
`[section](Namespaces-and-Sections/#Lean___Parser___Command___section "Documentation for syntax") [variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax") {p : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Prop} [variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax") (pZero : p 0) (pStep : ∀ n, p n → p (n + 1)) [variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax") (pFifteen : p 15) `
However, only `p` is added to this theorem's assumptions, so it cannot be proved.
`theorem p_all : ∀ n, p n := `unsolved goals zerop:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Prop⊢ p 0  succp:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Propn✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:p n✝⊢ p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")`byp:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Prop⊢ ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), p n [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") np:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Propn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ p n [induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic") nzerop:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Prop⊢ p 0succp:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Propn✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:p n✝⊢ p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") `
The ``Lean.Parser.Command.include : command`
``include` command causes the additional assumptions to be added unconditionally:
`include pZero pStep pFifteen  `automatically included section variable(s) unused in theorem `p_all`:   pFifteen consider restructuring your `variable` declarations so that the variables are not in scope or explicitly omit them:   omit pFifteen in theorem ...  Note: This linter can be disabled with `set_option linter.unusedSectionVars false``theorem p_all : ∀ n, p n := byp✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → ProppFifteen:p✝ 15p:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → ProppZero:p 0pStep:∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), p n → p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")⊢ ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), p n [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") np✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → ProppFifteen:p✝ 15p:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → ProppZero:p 0pStep:∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), p n → p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ p n [induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic") nzerop✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → ProppFifteen:p✝ 15p:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → ProppZero:p 0pStep:∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), p n → p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")⊢ p 0succp✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → ProppFifteen:p✝ 15p:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → ProppZero:p 0pStep:∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), p n → p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:p n✝⊢ p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") <;>zerop✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → ProppFifteen:p✝ 15p:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → ProppZero:p 0pStep:∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), p n → p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")⊢ p 0succp✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → ProppFifteen:p✝ 15p:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → ProppZero:p 0pStep:∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), p n → p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:p n✝⊢ p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [*]All goals completed! 🐙 `
Because the spurious assumption `pFifteen` was inserted, Lean issues a warning:

```
automatically included section variable(s) unused in theorem `p_all`:
  pFifteen
consider restructuring your `variable` declarations so that the variables are not in scope or explicitly omit them:
  omit pFifteen in theorem ...

Note: This linter can be disabled with `set_option linter.unusedSectionVars false`
```

This can be avoided by using ``Lean.Parser.Command.omit : command`
``omit` to remove `pFifteen`:
`include pZero pStep pFifteen  omit pFifteen [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") theorem p_all : ∀ n, p n := byp:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → ProppZero:p 0pStep:∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), p n → p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")⊢ ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), p n   [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") np:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → ProppZero:p 0pStep:∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), p n → p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ p n   [induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic") nzerop:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → ProppZero:p 0pStep:∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), p n → p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")⊢ p 0succp:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → ProppZero:p 0pStep:∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), p n → p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:p n✝⊢ p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") <;>zerop:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → ProppZero:p 0pStep:∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), p n → p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")⊢ p 0succp:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → ProppZero:p 0pStep:∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), p n → p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:p n✝⊢ p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [*]All goals completed! 🐙 ``end `
[Live ↪](javascript:openLiveLink\("M4UwxgLglg9gdgKAG4EMBOUUCMA2IAEA3gA74Bc+AcihPoEmE+ACmjMQL7Lqa4EAUxALRAty+UgAYAlPn4BlCCFIVAAET44AGjFr6W3nHwBqfAEZJkzhmx4ZxAGJQAZgpD6KpYwFZzCFwBMgA"\))
[←5. Source Files and Modules](Source-Files-and-Modules/#files "5. Source Files and Modules")[7. Definitions→](Definitions/#definitions "7. Definitions")

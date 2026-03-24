[←4.2. Propositions](The-Type-System/Propositions/#propositions "4.2. Propositions")[4.4. Inductive Types→](The-Type-System/Inductive-Types/#inductive-types "4.4. Inductive Types")
#  4.3. Universes[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The-Type-System--Universes "Permalink")
Types are classified by _universes_. Universes are also referred to as _sorts_. Each universe has a _level_ ,  which is a natural number. The `Sort` operator constructs a universe from a given level.  If the level of a universe is smaller than that of another, the universe itself is said to be smaller. With the exception of propositions (described later in this chapter), types in a given universe may only quantify over types in smaller universes. `Sort 0` is the type of propositions, while each `Sort (u + 1)` is a type that describes data.
Every universe is an element of the next larger universe, so `Sort 5` includes `Sort 4`. This means that the following examples are accepted:
`example : Sort 5 := Sort 4 example : Sort 2 := Sort 1 `
On the other hand, `Sort 3` is not an element of `Sort 5`:
`example : Sort 5 := `Type mismatch   Type 2 has type   Type 3 of sort `Type 4` but is expected to have type   Type 4 of sort `Type 5``Sort 3 `
```
Type mismatch
  Type 2
has type
  Type 3
of sort `Type 4` but is expected to have type
  Type 4
of sort `Type 5`
```

Similarly, because `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")` is in `Sort 1`, it is not in `Sort 2`:
`example : Sort 1 := [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") ``example : Sort 2 := `Type mismatch   [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") has type   Type of sort `Type 1` but is expected to have type   Type 1 of sort `Type 2``[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") `
```
Type mismatch
  [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")
has type
  Type
of sort `Type 1` but is expected to have type
  Type 1
of sort `Type 2`
```

Because propositions and data are used differently and are governed by different rules, the abbreviations `Type` and `Prop` are provided to make the distinction more convenient.  `Type u` is an abbreviation for `Sort (u + 1)`, so `Type 0` is `Sort 1` and `Type 3` is `Sort 4`. `Type 0` can also be abbreviated `Type`, so `Unit : Type` and `Type : Type 1`. `Prop` is an abbreviation for `Sort 0`.
##  4.3.1. Predicativity[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The-Type-System--Universes--Predicativity "Permalink")
Each universe contains dependent function types, which additionally represent universal quantification and implication. A function type's universe is determined by the universes of its argument and return types. The specific rules depend on whether the return type of the function is a proposition.
Predicates, which are functions that return propositions (that is, where the result of the function is some type in `Prop`) may have argument types in any universe whatsoever, but the function type itself remains in `Prop`. In other words, propositions feature _impredicative_ quantification, because propositions can themselves be statements about all propositions (and all other types).
Impredicativity
Proof irrelevance can be written as a proposition that quantifies over all propositions:
`example : Prop := ∀ (P : Prop) (p1 p2 : P), p1 = p2 `
A proposition may also quantify over all types, at any given level:
`example : Prop := ∀ (α : Type), ∀ (x : α), x = x example : Prop := ∀ (α : Type 5), ∀ (x : α), x = x `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAueAFATgeykgvPQAETwAUKSqmUAlMVAIzxQBMZKlANA/XkwFA+iRYCZOiy4CxQI3AZACoBPKMHYSiIMpOVq8IfuGhwWFcYSLTk8xfACsyk2uQaOW+CCA"\))
For universes at [level](The-Type-System/Universes/#--tech-term-level) `1` and higher (that is, the `Type u` hierarchy), quantification is _predicative_.  For these universes, the universe of a function type is the least upper bound of the argument and return types' universes.
Universe levels of function types
Both of these types are in `Type 2`:
`example (α : Type 1) (β : Type 2) : Type 2 := α → β example (α : Type 2) (β : Type 1) : Type 2 := α → β `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAKQjcDwFzwCoE8oIIwCUSgTcDpa4IBMxGOe8V6AvPKoEmE8JAUKJLAhTl61YojJ1K8IsKlM0rDlyA"\))
Predicativity of `Type`
This example is not accepted, because `α`'s level is greater than `1`. In other words, the annotated universe is smaller than the function type's universe:
`example (α : Type 2) (β : Type 1) : Type 1 := `Type mismatch   α → β has type   Type 2 of sort `Type 3` but is expected to have type   Type 1 of sort `Type 2``α → β `
```
Type mismatch
  α → β
has type
  Type 2
of sort `Type 3` but is expected to have type
  Type 1
of sort `Type 2`
```

Lean's universes are not cumulative; a type in `Type u` is not automatically also in `Type (u + 1)`. Each type inhabits precisely one universe.
No cumulativity
This example is not accepted because the annotated universe is larger than the function type's universe:
`example (α : Type 2) (β : Type 1) : Type 3 := `Type mismatch   α → β has type   Type 2 of sort `Type 3` but is expected to have type   Type 3 of sort `Type 4``α → β `
```
Type mismatch
  α → β
has type
  Type 2
of sort `Type 3` but is expected to have type
  Type 3
of sort `Type 4`
```

##  4.3.2. Polymorphism[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The-Type-System--Universes--Polymorphism "Permalink")
Lean supports _universe polymorphism_ ,  which means that constants defined in the Lean environment can take universe parameters. These parameters can then be instantiated with universe levels when the constant is used. Universe parameters are written in curly braces following a dot after a constant name.
Universe-polymorphic identity function
When fully explicit, the identity function takes a universe parameter `u`. Its signature is:
`id.{u} {α : Sort u} (x : α) : α`
Universe variables may additionally occur in [universe level expressions](The-Type-System/Universes/#level-expressions), which provide specific universe levels in definitions. When the polymorphic definition is instantiated with concrete levels, these universe level expressions are also evaluated to yield concrete levels.
Universe level expressions
In this example, `Codec` is in a universe that is one greater than the universe of the type it contains:
`structure Codec.{u} : Type (u + 1) where   type : Type u   encode : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32") → type → [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")   decode : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (type × [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) `
Lean automatically infers most level parameters. In the following example, it is not necessary to annotate the type as `Codec.{0}`, because `[Char](Basic-Types/Characters/#Char___mk "Documentation for Char")`'s type is `Type 0`, so `u` must be `0`:
`def Codec.char : Codec where   [type](The-Type-System/Universes/#Codec___type-_LPAR_in-Universe-level-expressions_RPAR_ "Definition of example") := [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")   [encode](The-Type-System/Universes/#Codec___encode-_LPAR_in-Universe-level-expressions_RPAR_ "Definition of example") buf ch := buf.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") ch.[val](Basic-Types/Characters/#Char___mk "Documentation for Char.val")   [decode](The-Type-System/Universes/#Codec___decode-_LPAR_in-Universe-level-expressions_RPAR_ "Definition of example") buf i := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")     let v ← buf[i]?     if h : v.[isValidChar](Basic-Types/Fixed-Precision-Integers/#UInt32___isValidChar "Documentation for UInt32.isValidChar") then       let ch : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") := ⟨v, h⟩       return (ch, i + 1)     else       failure `
[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgMIHsAm8oDoDeEBfRALkQBUBPAByQAoJEBqRARgEpEB3AC3gQChEiENSSlKNRBEGJ4AOygYxiAIJgwAQwqIAqgEk5IAMwAmRICTCYaIur1W3QeMmZmRZhK3N2/YdM2AchogNgDyVCAAlqhyiLQikgDriIEgbPz8mABmKEo4UNwaYB5orly8AkLxYgC8KAVgMvJuSABGENn5JLVtmdhUEMDciPnYAG4aADYuWEqIPYgRXYjoqDJCE/DBo4iACYRz7QDaEQC6APxrC9lDpKPYEcAAapMR6Mj1wrxyF+ubw9d1hSWgAvyUYAGkQ3EAl+TfRAIWBgGK0fLgxbMdgXeATYDwGGZDQRCZweBAA"\))
Universe-polymorphic definitions in fact create a _schematic definition_ that can be instantiated at a variety of levels, and different instantiations of universes create incompatible values.
Universe polymorphism and definitional equality
This can be seen in the following example, in which `[T](The-Type-System/Universes/#T-_LPAR_in-Universe-polymorphism-and-definitional-equality_RPAR_ "Definition of example")` is a gratuitously-universe-polymorphic function that always returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`. Because it is marked ``Lean.Parser.Command.declaration : command```opaque`, Lean can't check equality by unfolding the definitions. Both instantiations of `[T](The-Type-System/Universes/#T-_LPAR_in-Universe-polymorphism-and-definitional-equality_RPAR_ "Definition of example")` have the parameters and the same type, but their differing universe instantiations make them incompatible.
`opaque T.{u} (_ : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") :=   (fun (α : Sort u) => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit").{u}  set_option pp.universes true  def `Not a definitional equality: the left-hand side   [T.{u}](The-Type-System/Universes/#T-_LPAR_in-Universe-polymorphism-and-definitional-equality_RPAR_ "Definition of example") 0 is not definitionally equal to the right-hand side   [T.{v}](The-Type-System/Universes/#T-_LPAR_in-Universe-polymorphism-and-definitional-equality_RPAR_ "Definition of example") 0`test.{u, v} : [T](The-Type-System/Universes/#T-_LPAR_in-Universe-polymorphism-and-definitional-equality_RPAR_ "Definition of example").{u} 0 = [T](The-Type-System/Universes/#T-_LPAR_in-Universe-polymorphism-and-definitional-equality_RPAR_ "Definition of example").{v} 0 := `Type mismatch   [rfl.{?u.48}](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") has type   [Eq.{?u.48}](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ?m.7 ?m.7 but is expected to have type   [Eq.{1}](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ([T.{u}](The-Type-System/Universes/#T-_LPAR_in-Universe-polymorphism-and-definitional-equality_RPAR_ "Definition of example") 0) ([T.{v}](The-Type-System/Universes/#T-_LPAR_in-Universe-polymorphism-and-definitional-equality_RPAR_ "Definition of example") 0)`[rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
```
Type mismatch
  [rfl.{?u.48}](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")
has type
  [Eq.{?u.48}](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ?m.7 ?m.7
but is expected to have type
  [Eq.{1}](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ([T.{u}](The-Type-System/Universes/#T-_LPAR_in-Universe-polymorphism-and-definitional-equality_RPAR_ "Definition of example") 0) ([T.{v}](The-Type-System/Universes/#T-_LPAR_in-Universe-polymorphism-and-definitional-equality_RPAR_ "Definition of example") 0)
```

Auto-bound implicit arguments are as universe-polymorphic as possible. Defining the identity function as follows:
`def id' (x : α) := x `
results in the signature:
`[id'](The-Type-System/Universes/#id___ "Definition of example").{u} {α : Sort u} (x : α) : α`Universe monomorphism in auto-bound implicit parameters
On the other hand, because `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` is in universe `Type 0`, this function automatically ends up with a concrete universe level for `α`, because `m` is applied to both `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` and `α`, so both must have the same type and thus be in the same universe:
`partial def count [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (act : m α) : m [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   if p (← act) then     return 1 + (← [count](The-Type-System/Universes/#count-_LPAR_in-Universe-monomorphism-in-auto-bound-implicit-parameters_RPAR_ "Definition of example") p act)   else     return 0 `
[Live ↪](javascript:openLiveLink\("A4QwTgLgliA2AEATApgM3gYwPYFcB2E8A2gLJZ4iLwC2AuvABTDwBc8gjcDyBJhPAEJZZYASkYgMhNtQ4jJ8AHIgJAXiRYAUPHhR0zBoATCeGIgiIAC2R4Nm+GGQQcYPPACM8ANSMD2fIWZGhVsiwAM7IVpq29o7wAAxAA"\))
###  4.3.2.1. Level Expressions[🔗](find/?domain=Verso.Genre.Manual.section&name=level-expressions "Permalink")
Levels that occur in a definition are not restricted to just variables and addition of constants. More complex relationships between universes can be defined using level expressions.

```
Level ::= 0 | 1 | 2 | ...  -- Concrete levels
        | u, v             -- Variables
        | Level + n        -- Addition of constants
        | max Level Level  -- Least upper bound
        | imax Level Level -- Impredicative LUB

```

Given an assignment of level variables to concrete numbers, evaluating these expressions follows the usual rules of arithmetic. The `imax` operation is defined as follows:
`imax u v={0when v=0max u votherwise\mathtt{imax}\ u\ v = \begin{cases}0 & \mathrm{when\ }v = 0\\\mathtt{max}\ u\ v&\mathrm{otherwise}\end{cases}imax u v={0max u v​when v=0otherwise​`
`imax` is used to implement [impredicative](The-Type-System/Universes/#--tech-term-impredicative) quantification for `Prop`. In particular, if `A : Sort u` and `B : Sort v`, then `(x : A) → B : Sort (imax u v)`. If `B : Prop`, then the function type is itself a `Prop`; otherwise, the function type's level is the maximum of `u` and `v`.
###  4.3.2.2. Universe Variable Bindings[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The-Type-System--Universes--Polymorphism--Universe-Variable-Bindings "Permalink")
Universe-polymorphic definitions bind universe variables. These bindings may be either explicit or implicit. Explicit universe variable binding and instantiation occurs as a suffix to the definition's name. Universe parameters are defined or provided by suffixing the name of a constant with a period (`.`) followed by a comma-separated sequence of universe variables between curly braces.
Universe-polymorphic `map`
The following declaration of `[map](The-Type-System/Universes/#map-_LPAR_in-Universe-polymorphic--map_RPAR_ "Definition of example")` declares two universe parameters (`u` and `v`) and instantiates the polymorphic `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List")` with each in turn:
`def map.{u, v} {α : Type u} {β : Type v}     (f : α → β) :     [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List").{u} α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List").{v} β   | [] => []   | x :: xs => f x :: [map](The-Type-System/Universes/#map-_LPAR_in-Universe-polymorphic--map_RPAR_ "Definition of example") f xs `
[Live ↪](javascript:openLiveLink\("CYUwZgBAtghgDgOgN4FcA0EBuBfCTCNwBAFwQAqAnnCBCrkoE3AxZl1OAUBJxABSQmGAkwgj0AlMQ5cAMgEsAzgBdktCIIgyFyHMIkAfCAG0AuhAC8APgOHdEAB7ESN2aYuQ7RErDgRXsoA"\))
Just as Lean automatically instantiates implicit parameters, it also automatically instantiates universe parameters. When [automatic implicit parameter insertion](Definitions/Headers-and-Signatures/#automatic-implicit-parameters) is enabled (i.e. the `[autoImplicit](Definitions/Headers-and-Signatures/#autoImplicit "Documentation for option autoImplicit")` option is set to `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, which is the default), it is not necessary to explicitly bind universe variables; they are inserted automatically. When it is set to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, then they must be added explicitly or declared using the `universe` command. 
Automatic Implicit Parameters and Universe Polymorphism
When `autoImplicit` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (which is the default setting), this definition is accepted even though it does not bind its universe parameters:
`set_option [autoImplicit](Definitions/Headers-and-Signatures/#autoImplicit "Documentation for option autoImplicit") true def map {α : Type u} {β : Type v} (f : α → β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β   | [] => []   | x :: xs => f x :: map f xs `
When `autoImplicit` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, the definition is rejected because `u` and `v` are not in scope:
`set_option [autoImplicit](Definitions/Headers-and-Signatures/#autoImplicit "Documentation for option autoImplicit") false def map {α : Type `unknown universe level `u``u} {β : Type `unknown universe level `v``v} (f : α → β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β | [] => [] | x :: xs => f x :: map f xs `
```
unknown universe level `u`
```

```
unknown universe level `v`
```

In addition to using `autoImplicit`, particular identifiers can be declared as universe variables in a particular [section scope](Namespaces-and-Sections/#--tech-term-section-scope) using the `universe` command.
syntaxUniverse Parameter Declarations

```
command ::= ...
    | Declares one or more universe variables.

`universe u v`

`Prop`, `Type`, `Type u` and `Sort u` are types that classify other types, also known as
*universes*. In `Type u` and `Sort u`, the variable `u` stands for the universe's *level*, and a
universe at level `u` can only classify universes that are at levels lower than `u`. For more
details on type universes, please refer to [the relevant chapter of Theorem Proving in Lean][tpil
universes].

Just as type arguments allow polymorphic definitions to be used at many different types, universe
parameters, represented by universe variables, allow a definition to be used at any required level.
While Lean mostly handles universe levels automatically, declaring them explicitly can provide more
control when writing signatures. The `universe` keyword allows the declared universe variables to be
used in a collection of definitions, and Lean will ensure that these definitions use them
consistently.

[tpil universes]: https://lean-lang.org/theorem_proving_in_lean4/dependent_type_theory.html#types-as-objects
(Type universes on Theorem Proving in Lean)

```lean
/- Explicit type-universe parameter. -/
def id₁.{u} (α : Type u) (a : α) := a

/- Implicit type-universe parameter, equivalent to `id₁`.
  Requires option `autoImplicit true`, which is the default. -/
def id₂ (α : Type u) (a : α) := a

/- Explicit standalone universe variable declaration, equivalent to `id₁` and `id₂`. -/
universe u
def id₃ (α : Type u) (a : α) := a
```

On a more technical note, using a universe variable only in the right-hand side of a definition
causes an error if the universe has not been declared previously.

```lean
def L₁.{u} := List (Type u)

-- def L₂ := List (Type u) -- error: `unknown universe level 'u'`

universe u
def L₃ := List (Type u)
```

## Examples

```lean
universe u v w

structure Pair (α : Type u) (β : Type v) : Type (max u v) where
  a : α
  b : β

#check Pair.{v, w}
-- Pair : Type v → Type w → Type (max v w)
```
universe ident ident*
```

Declares one or more universe variables for the extent of the current scope.
Just as the `variable` command causes a particular identifier to be treated as a parameter with a particular type, the `universe` command causes the subsequent identifiers to be implicitly quantified as universe parameters in declarations that mention them, even if the option `autoImplicit` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
The `universe` command when `autoImplicit` is `false`
`set_option [autoImplicit](Definitions/Headers-and-Signatures/#autoImplicit "Documentation for option autoImplicit") false [universe](The-Type-System/Universes/#Lean___Parser___Command___universe-next "Documentation for syntax") u def id₃ (α : Type u) (a : α) := a `
Because the automatic implicit parameter feature only inserts parameters that are used in the declaration's [header](Definitions/Headers-and-Signatures/#--tech-term-header), universe variables that occur only on the right-hand side of a definition are not inserted as arguments unless they have been declared with `universe` even when `autoImplicit` is `true`.
Automatic universe parameters and the `universe` command
This definition with an explicit universe parameter is accepted:
`def L.{u} := [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u) `
Even with automatic implicit parameters, this definition is rejected, because `u` is not mentioned in the header, which precedes the `:=`:
`set_option [autoImplicit](Definitions/Headers-and-Signatures/#autoImplicit "Documentation for option autoImplicit") true def L := [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type `unknown universe level `u``u) `
```
unknown universe level `u`
```

With a universe declaration, `u` is accepted as a parameter even on the right-hand side:
`[universe](The-Type-System/Universes/#Lean___Parser___Command___universe-next "Documentation for syntax") u def L := [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u) `
The resulting definition of `L` is universe-polymorphic, with `u` inserted as a universe parameter.
Declarations in the scope of a `universe` command are not made polymorphic if the universe variables do not occur in them or in other automatically-inserted arguments.
`[universe](The-Type-System/Universes/#Lean___Parser___Command___universe-next "Documentation for syntax") u def L := [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type 0) `L : Type 1`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") L `
[Live ↪](javascript:openLiveLink\("K4OwlgbgpgTgzlABMAUAEygM0QGUQLgF5cw4AXRACgBUBPAByQAYBKFAYgGMALKTga1xA"\))
###  4.3.2.3. Universe Lifting[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The-Type-System--Universes--Polymorphism--Universe-Lifting "Permalink")
When a type's universe is smaller than the one expected in some context, _universe lifting_ operators can bridge the gap. These are wrappers around terms of a given type that are in larger universes than the wrapped type. There are two lifting operators:
  * `[PLift](The-Type-System/Universes/#PLift___up "Documentation for PLift")` can lift any type, including [propositions](The-Type-System/Propositions/#--tech-term-Propositions), by one level. It can be used to include proofs in data structures such as lists.
  * `[ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift")` can lift any non-proposition type by any number of levels.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=PLift.up "Permalink")structure
```


PLift.{u} (α : Sort u) : Type u


PLift.{u} (α : Sort u) : Type u


```

Lifts a proposition or type to a higher universe level.
`[PLift](The-Type-System/Universes/#PLift___up "Documentation for PLift") α` wraps a proof or value of type `α`. The resulting type is in the next largest universe after that of `α`. In particular, propositions become data.
The related type `[ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift")` can be used to lift a non-proposition type by any number of levels.
Examples:
  * `([False](Basic-Propositions/Truth/#False "Documentation for False") : Prop)`
  * `([PLift](The-Type-System/Universes/#PLift___up "Documentation for PLift") [False](Basic-Propositions/Truth/#False "Documentation for False") : Type)`
  * `([[.up](The-Type-System/Universes/#PLift___up "Documentation for PLift.up") (by [trivial](Tactic-Proofs/Tactic-Reference/#trivial "Documentation for tactic")), [.up](The-Type-System/Universes/#PLift___up "Documentation for PLift.up") (by [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")), [.up](The-Type-System/Universes/#PLift___up "Documentation for PLift.up") (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic"))] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([PLift](The-Type-System/Universes/#PLift___up "Documentation for PLift") [True](Basic-Propositions/Truth/#True___intro "Documentation for True")))`
  * `([Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") : Type 0)`
  * `([PLift](The-Type-System/Universes/#PLift___up "Documentation for PLift") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") : Type 1)`


#  Constructor

```
[PLift.up](The-Type-System/Universes/#PLift___up "Documentation for PLift.up").{u}
```

Wraps a proof or value to increase its type's universe level by 1.
#  Fields

```
down : α
```

Extracts a wrapped proof or value from a universe-lifted proposition or type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ULift "Permalink")structure
```


ULift.{r, s} (α : Type s) : Type (max s r)


ULift.{r, s} (α : Type s) : Type (max s r)


```

Lifts a type to a higher universe level.
`[ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") α` wraps a value of type `α`. Instead of occupying the same universe as `α`, which would be the minimal level, it takes a further level parameter and occupies their maximum. The resulting type may occupy any universe that's at least as large as that of `α`.
The resulting universe of the lifting operator is the first parameter, and may be written explicitly while allowing `α`'s level to be inferred.
The related type `[PLift](The-Type-System/Universes/#PLift___up "Documentation for PLift")` can be used to lift a proposition or type by one level.
Examples:
  * `([Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") : Type 0)`
  * `([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") : Type 0)`
  * `([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") : Type 1)`
  * `([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") : Type 5)`
  * `([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift").{7} ([PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit") : Type 3) : Type 7)`


#  Constructor

```
[ULift.up](The-Type-System/Universes/#ULift___up "Documentation for ULift.up").{r, s}
```

Wraps a value to increase its type's universe level.
#  Fields

```
down : α
```

Extracts a wrapped value from a universe-lifted type.
[←4.2. Propositions](The-Type-System/Propositions/#propositions "4.2. Propositions")[4.4. Inductive Types→](The-Type-System/Inductive-Types/#inductive-types "4.4. Inductive Types")

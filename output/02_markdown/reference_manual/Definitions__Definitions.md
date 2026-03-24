[←7.2. Headers and Signatures](Definitions/Headers-and-Signatures/#signature-syntax "7.2. Headers and Signatures")[7.4. Theorems→](Definitions/Theorems/#The-Lean-Language-Reference--Definitions--Theorems "7.4. Theorems")
#  7.3. Definitions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Definitions--Definitions "Permalink")
Definitions add a new constant to the global environment as a name that stands for a term. As part of the kernel's definitional equality, this new constant may be replaced via [δ-reduction](The-Type-System/#--tech-term-___-next) with the term that it stands for. In the elaborator, this replacement is governed by the constant's [reducibility](Definitions/Recursive-Definitions/#--tech-term-reducibility). The new constant may be [universe polymorphic](The-Type-System/Universes/#--tech-term-universe-polymorphism), in which case occurrences may instantiate it with different universe level parameters.
Function definitions may be recursive. To preserve the consistency of Lean's type theory as a logic, recursive functions must either be opaque to the kernel (e.g. by [declaring them `partial`](Definitions/Recursive-Definitions/#partial-functions)) or proven to terminate with one of the strategies described in [the section on recursive definitions](Definitions/Recursive-Definitions/#recursive-definitions).
The headers and bodies of definitions are elaborated together. If the header is incompletely specified (e.g. a parameter's type or the codomain is missing), then the body may provide sufficient information for the elaborator to reconstruct the missing parts. However, [instance implicit](Type-Classes/#--tech-term-instance-implicit) parameters must be specified in the header or as [section variables](Namespaces-and-Sections/#--tech-term-Section-variables).
syntaxDefinitions
Definitions that use `:=` associate the term on the right-hand side with the constant's name. The term is wrapped in a ``Lean.Parser.Term.fun : term```fun` for each parameter, and the type is found by binding the parameters in a function type. Definitions with `def` are [semireducible](Definitions/Recursive-Definitions/#--tech-term-Semireducible).

```
command ::= ...
    | [
declModifiers is the collection of modifiers on a declaration:



  * a doc comment /-- ... -/



  * a list of attributes @[attr1, attr2]



  * a visibility specifier, private or public



  * protected


  * noncomputable


  * unsafe


  * 
partial or nonrec




All modifiers are optional, and have to come in the listed order.
nestedDeclModifiers is the same as declModifiers, but attributes are printed
on the same line as the declaration. It is used for declarations nested inside other syntax,
such as inductive constructors, structure projections, and let rec / where definitions. 
declModifiers](Definitions/Modifiers/#Lean___Parser___Command___declModifiers)
      def 


declId matches foo or foo.{u,v}: an identifier possibly followed by a list of universe names 


declId [
optDeclSig matches the signature of a declaration with optional type: a list of binders and then possibly : type 
optDeclSig](Definitions/Headers-and-Signatures/#Lean___Parser___Command___optDeclSig) := term


Termination hints are termination_by and decreasing_by, in that order.



```

Definitions may use pattern matching. These definitions are desugared to uses of ``Lean.Parser.Term.match : term`
Pattern matching. `match e, ... with | p, ... => f | ...` matches each given term `e` against each pattern `p` of a match alternative. When all patterns of an alternative match, the `match` term evaluates to the value of the corresponding right-hand side `f` with the pattern variables bound to the respective matched values. If used as `match h : e, ... with | p, ... => f | ...`, `h : e = p` is available within `f`.
When not constructing a proof, `match` does not automatically substitute variables matched on in dependent variables' types. Use `match (generalizing := true) ...` to enforce this.
Syntax quotations can also be used in a pattern match. This matches a `Syntax` value against quotations, pattern variables, or `_`.
Quoted identifiers only match identical identifiers - custom matching such as by the preresolved names only should be done explicitly.
`Syntax.atom`s are ignored during matching by default except when part of a built-in literal. For users introducing new atoms, we recommend wrapping them in dedicated syntax kinds if they should participate in matching. For example, in

```
syntax "c" ("foo" <|> "bar") ...

```

`foo` and `bar` are indistinguishable during matching, but in

```
syntax foo := "foo"
syntax "c" (foo <|> "bar") ...

```

they are not.
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match).

```
command ::= ...
    | [
declModifiers is the collection of modifiers on a declaration:



  * a doc comment /-- ... -/



  * a list of attributes @[attr1, attr2]



  * a visibility specifier, private or public



  * protected


  * noncomputable


  * unsafe


  * 
partial or nonrec




All modifiers are optional, and have to come in the listed order.
nestedDeclModifiers is the same as declModifiers, but attributes are printed
on the same line as the declaration. It is used for declarations nested inside other syntax,
such as inductive constructors, structure projections, and let rec / where definitions. 
declModifiers](Definitions/Modifiers/#Lean___Parser___Command___declModifiers)
      def 


declId matches foo or foo.{u,v}: an identifier possibly followed by a list of universe names 


declId [
optDeclSig matches the signature of a declaration with optional type: a list of binders and then possibly : type 
optDeclSig](Definitions/Headers-and-Signatures/#Lean___Parser___Command___optDeclSig)
        (| term => term)*


Termination hints are termination_by and decreasing_by, in that order.



```

Values of structure types, or functions that return them, may be defined by providing values for their fields, following `where`:

```
command ::= ...
    | [
declModifiers is the collection of modifiers on a declaration:



  * a doc comment /-- ... -/



  * a list of attributes @[attr1, attr2]



  * a visibility specifier, private or public



  * protected


  * noncomputable


  * unsafe


  * 
partial or nonrec




All modifiers are optional, and have to come in the listed order.
nestedDeclModifiers is the same as declModifiers, but attributes are printed
on the same line as the declaration. It is used for declarations nested inside other syntax,
such as inductive constructors, structure projections, and let rec / where definitions. 
declModifiers](Definitions/Modifiers/#Lean___Parser___Command___declModifiers)
      def 


declId matches foo or foo.{u,v}: an identifier possibly followed by a list of universe names 


declId [
optDeclSig matches the signature of a declaration with optional type: a list of binders and then possibly : type 
optDeclSig](Definitions/Headers-and-Signatures/#Lean___Parser___Command___optDeclSig) where
        structInstField*
```

In [modules](Source-Files-and-Modules/#--tech-term-module), the bodies of definitions defined with `def` are not exposed by default.
syntaxAbbreviations
Abbreviations are identical to definitions with `def`, except they are [reducible](Definitions/Recursive-Definitions/#--tech-term-Reducible).

```
command ::= ...
    | [
declModifiers is the collection of modifiers on a declaration:



  * a doc comment /-- ... -/



  * a list of attributes @[attr1, attr2]



  * a visibility specifier, private or public



  * protected


  * noncomputable


  * unsafe


  * 
partial or nonrec




All modifiers are optional, and have to come in the listed order.
nestedDeclModifiers is the same as declModifiers, but attributes are printed
on the same line as the declaration. It is used for declarations nested inside other syntax,
such as inductive constructors, structure projections, and let rec / where definitions. 
declModifiers](Definitions/Modifiers/#Lean___Parser___Command___declModifiers)
      abbrev 


declId matches foo or foo.{u,v}: an identifier possibly followed by a list of universe names 


declId [
optDeclSig matches the signature of a declaration with optional type: a list of binders and then possibly : type 
optDeclSig](Definitions/Headers-and-Signatures/#Lean___Parser___Command___optDeclSig) := term


Termination hints are termination_by and decreasing_by, in that order.



```

```
command ::= ...
    | [
declModifiers is the collection of modifiers on a declaration:



  * a doc comment /-- ... -/



  * a list of attributes @[attr1, attr2]



  * a visibility specifier, private or public



  * protected


  * noncomputable


  * unsafe


  * 
partial or nonrec




All modifiers are optional, and have to come in the listed order.
nestedDeclModifiers is the same as declModifiers, but attributes are printed
on the same line as the declaration. It is used for declarations nested inside other syntax,
such as inductive constructors, structure projections, and let rec / where definitions. 
declModifiers](Definitions/Modifiers/#Lean___Parser___Command___declModifiers)
      abbrev 


declId matches foo or foo.{u,v}: an identifier possibly followed by a list of universe names 


declId [
optDeclSig matches the signature of a declaration with optional type: a list of binders and then possibly : type 
optDeclSig](Definitions/Headers-and-Signatures/#Lean___Parser___Command___optDeclSig)
        (| term => term)*


Termination hints are termination_by and decreasing_by, in that order.



```

```
command ::= ...
    | [
declModifiers is the collection of modifiers on a declaration:



  * a doc comment /-- ... -/



  * a list of attributes @[attr1, attr2]



  * a visibility specifier, private or public



  * protected


  * noncomputable


  * unsafe


  * 
partial or nonrec




All modifiers are optional, and have to come in the listed order.
nestedDeclModifiers is the same as declModifiers, but attributes are printed
on the same line as the declaration. It is used for declarations nested inside other syntax,
such as inductive constructors, structure projections, and let rec / where definitions. 
declModifiers](Definitions/Modifiers/#Lean___Parser___Command___declModifiers)
      abbrev 


declId matches foo or foo.{u,v}: an identifier possibly followed by a list of universe names 


declId [
optDeclSig matches the signature of a declaration with optional type: a list of binders and then possibly : type 
optDeclSig](Definitions/Headers-and-Signatures/#Lean___Parser___Command___optDeclSig) where
        structInstField*
```

In [modules](Source-Files-and-Modules/#--tech-term-module), the bodies of definitions defined with `abbrev` are exposed by default.
_Opaque constants_ are defined constants that are not subject to [δ-reduction](The-Type-System/#--tech-term-___-next) in the kernel. They are useful for specifying the existence of some function. Unlike [axioms](Axioms/#--tech-term-Axioms), opaque declarations can only be used for types that are inhabited, so they do not risk introducing inconsistency. Also unlike axioms, the inhabitant of the type is used in compiled code. The `implemented_by` attribute can be used to instruct the compiler to emit a call to some other function as the compilation of an opaque constant.
syntaxOpaque Constants
Opaque definitions with right-hand sides are elaborated like other definitions. This demonstrates that the type is inhabited; the inhabitant plays no further role.

```
command ::= ...
    | [
declModifiers is the collection of modifiers on a declaration:



  * a doc comment /-- ... -/



  * a list of attributes @[attr1, attr2]



  * a visibility specifier, private or public



  * protected


  * noncomputable


  * unsafe


  * 
partial or nonrec




All modifiers are optional, and have to come in the listed order.
nestedDeclModifiers is the same as declModifiers, but attributes are printed
on the same line as the declaration. It is used for declarations nested inside other syntax,
such as inductive constructors, structure projections, and let rec / where definitions. 
declModifiers](Definitions/Modifiers/#Lean___Parser___Command___declModifiers)
      opaque 


declId matches foo or foo.{u,v}: an identifier possibly followed by a list of universe names 


declId [
declSig matches the signature of a declaration with required type: a list of binders and then : type 
declSig](Definitions/Headers-and-Signatures/#Lean___Parser___Command___declSig) := term


Termination hints are termination_by and decreasing_by, in that order.



```

Opaque constants may also be specified without right-hand sides. The elaborator fills in the right-hand side by synthesizing an instance of `[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited")`, or `[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty")` if that fails.

```
command ::= ...
    | [
declModifiers is the collection of modifiers on a declaration:



  * a doc comment /-- ... -/



  * a list of attributes @[attr1, attr2]



  * a visibility specifier, private or public



  * protected


  * noncomputable


  * unsafe


  * 
partial or nonrec




All modifiers are optional, and have to come in the listed order.
nestedDeclModifiers is the same as declModifiers, but attributes are printed
on the same line as the declaration. It is used for declarations nested inside other syntax,
such as inductive constructors, structure projections, and let rec / where definitions. 
declModifiers](Definitions/Modifiers/#Lean___Parser___Command___declModifiers)
      opaque 


declId matches foo or foo.{u,v}: an identifier possibly followed by a list of universe names 


declId [
declSig matches the signature of a declaration with required type: a list of binders and then : type 
declSig](Definitions/Headers-and-Signatures/#Lean___Parser___Command___declSig)
```

[←7.2. Headers and Signatures](Definitions/Headers-and-Signatures/#signature-syntax "7.2. Headers and Signatures")[7.4. Theorems→](Definitions/Theorems/#The-Lean-Language-Reference--Definitions--Theorems "7.4. Theorems")

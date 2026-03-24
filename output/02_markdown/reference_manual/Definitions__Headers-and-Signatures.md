[←7.1. Modifiers](Definitions/Modifiers/#declaration-modifiers "7.1. Modifiers")[7.3. Definitions→](Definitions/Definitions/#The-Lean-Language-Reference--Definitions--Definitions "7.3. Definitions")
#  7.2. Headers and Signatures[🔗](find/?domain=Verso.Genre.Manual.section&name=signature-syntax "Permalink")
The _header_ of a definition or declaration consists of the constant being declared or defined, if relevant, together with its signature. The _signature_ of a constant specifies how it can be used. The information present in the signature is more than just the type, including information such as [universe level parameters](The-Type-System/Universes/#--tech-term-universe-parameters) and the default values of its optional parameters. In Lean, signatures are written in a consistent format in different kinds of declarations.
##  7.2.1. Declaration Names[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Definitions--Headers-and-Signatures--Declaration-Names "Permalink")
Most headers begin with a _declaration name_ , which is followed by the signature proper: its parameters and the resulting type. A declaration name is a name that may optionally include universe parameters.
syntaxDeclaration Names
Declaration names without universe parameters consist of an identifier:

```
declId ::=
    


declId matches foo or foo.{u,v}: an identifier possibly followed by a list of universe names 


ident
```

Declaration names with universe parameters consist of an identifier followed by a period and one or more universe parameter names in braces:

```
declId ::= ...
    | 


declId matches foo or foo.{u,v}: an identifier possibly followed by a list of universe names 


ident.{ident, ident,*}
```

These universe parameter names are binding occurrences.
Examples do not include declaration names, and names are optional for instance declarations.
##  7.2.2. Parameters and Types[🔗](find/?domain=Verso.Genre.Manual.section&name=parameter-syntax "Permalink")
After the name, if present, is the header's signature. The signature specifies the declaration's parameters and type.
syntaxDeclaration Signatures
A signature consists of zero or more parameters, followed by a colon and a type.

```
declSig ::=
    


declSig matches the signature of a declaration with required type: a list of binders and then : type 


(ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole) | bracketedBinder)* : term
```

syntaxOptional Signatures
Signatures are often optional. In these cases, parameters may be supplied even if the type is omitted.

```
optDeclSig ::=
    


optDeclSig matches the signature of a declaration with optional type: a list of binders and then possibly : type 


(ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole) | bracketedBinder)* (: term)?
```

Parameters may have three forms:
  * An identifier, which names a parameter but does not provide a type. These parameters' types must be inferred during elaboration.
  * An underscore (`_`), which indicates a parameter that is not accessible by name in the local scope. These parameters' types must also be inferred during elaboration.
  * A bracketed binder, which may specify every aspect of one or more parameters, including their names, their types, default values, and whether they are explicit, implicit, strictly implicit, or instance-implicit.


##  7.2.3. Bracketed Parameter Bindings[🔗](find/?domain=Verso.Genre.Manual.section&name=bracketed-parameter-syntax "Permalink")
Parameters other than identifiers or underscores are collectively referred to as _bracketed binders_ because every syntactic form for specifying them has some kind of brackets, braces, or parentheses. All bracketed binders specify the type of a parameter, and most include parameter names. The name is optional for instance implicit parameters. Using an underscore (`_`) instead of a parameter name indicates an anonymous parameter.
syntaxExplicit Parameters
Parenthesized parameters indicate explicit parameters. If more than one identifier or underscore is provided, then all of them become parameters with the same type.

```
bracketedBinder ::=
    


Explicit binder, like (x y : A) or (x y).
Default values can be specified using (x : A := v) syntax, and tactics using (x : A := by tac).


((ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole)) (ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole))* : term)
```

syntaxOptional and Automatic Parameters
Parenthesized parameters with a `:=` assign default values to parameters. Parameters with default values are called _optional parameters_. At a call site, if the parameter is not provided, then the provided term is used to fill it in. Prior parameters in the signature are in scope for the default value, and their values at the call site are substituted into the default value term.
If a [tactic script](Tactic-Proofs/#tactics) is provided, then the tactics are executed at the call site to synthesize a parameter value; parameters that are filled in via tactics are called _automatic parameters_.

```
bracketedBinder ::= ...
    | 


Explicit binder, like (x y : A) or (x y).
Default values can be specified using (x : A := v) syntax, and tactics using (x : A := by tac).


((ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole)) (ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole))* : term := term)
```

syntaxImplicit Parameters
Parameters in curly braces indicate [implicit](Terms/Functions/#--tech-term-implicit) parameters. Unless provided by name at a call site, these parameters are expected to be synthesized via unification at call sites. Implicit parameters are synthesized at all call sites.

```
bracketedBinder ::= ...
    | 


Implicit binder, like {x y : A} or {x y}.
In regular applications, whenever all parameters before it have been specified,
then a _ placeholder is automatically inserted for this parameter.
Implicit parameters should be able to be determined from the other arguments and the return type
by unification.


In @ explicit mode, implicit binders behave like explicit binders.


{(ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole)) (ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole))* : term}
```

syntaxStrict Implicit Parameters
Parameters in double curly braces indicate [strict implicit](Terms/Functions/#--tech-term-Strict-implicit) parameters. `⦃ … ⦄` and `{{ … }}` are equivalent. Like implicit parameters, these parameters are expected to be synthesized via unification at call sites when they are not provided by name. Strict implicit parameters are only synthesized at call sites when subsequent parameters in the signature are also provided.

```
bracketedBinder ::= ...
    | 


Strict-implicit binder, like ⦃x y : A⦄ or ⦃x y⦄.
In contrast to { ... } implicit binders, strict-implicit binders do not automatically insert
a _ placeholder until at least one subsequent explicit parameter is specified.
Do _not_ use strict-implicit binders unless there is a subsequent explicit parameter.
Assuming this rule is followed, for fully applied expressions implicit and strict-implicit binders have the same behavior.


Example: If h : ∀ ⦃x : A⦄, x ∈ s → p x and hs : y ∈ s,
then h by itself elaborates to itself without inserting _ for the x : A parameter,
and h hs has type p y.
In contrast, if h' : ∀ {x : A}, x ∈ s → p x, then h by itself elaborates to have type ?m ∈ s → p ?m
with ?m a fresh metavariable.


⦃(ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole)) (ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole))* : term⦄
```

```
bracketedBinder ::= ...
    | 


Strict-implicit binder, like ⦃x y : A⦄ or ⦃x y⦄.
In contrast to { ... } implicit binders, strict-implicit binders do not automatically insert
a _ placeholder until at least one subsequent explicit parameter is specified.
Do _not_ use strict-implicit binders unless there is a subsequent explicit parameter.
Assuming this rule is followed, for fully applied expressions implicit and strict-implicit binders have the same behavior.


Example: If h : ∀ ⦃x : A⦄, x ∈ s → p x and hs : y ∈ s,
then h by itself elaborates to itself without inserting _ for the x : A parameter,
and h hs has type p y.
In contrast, if h' : ∀ {x : A}, x ∈ s → p x, then h by itself elaborates to have type ?m ∈ s → p ?m
with ?m a fresh metavariable.


{{(ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole)) (ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole))* : term}}
```

syntaxInstance Implicit Parameters
Parameters in square brackets indicate [instance implicit](Type-Classes/#--tech-term-instance-implicit) parameters, which are synthesized at call sites using [instance synthesis](Type-Classes/#--tech-term-synthesizes).

```
bracketedBinder ::= ...
    | 


Instance-implicit binder, like [C] or [inst : C].
In regular applications without @ explicit mode, it is automatically inserted
and solved for by typeclass inference for the specified class C.
In @ explicit mode, if _ is used for an instance-implicit parameter, then it is still solved for by typeclass inference;
use (_) to inhibit this and have it be solved for by unification instead, like an implicit argument.


[(ident :)? term]
```

The parameters are always in scope in the signature's type, which occurs after the colon. They are also in scope in the declaration's body, while names bound in the type itself are only in scope in the type. Thus, parameter names are used twice:
  * As names in the declaration's function type, bound as part of a [dependent function type](The-Type-System/Functions/#--tech-term-Dependent).
  * As names in the declaration's body. In function definitions, they are bound by a ``Lean.Parser.Term.fun : term```fun`.

Parameter Scope
The signature of `[add](Definitions/Headers-and-Signatures/#add-_LPAR_in-Parameter-Scope_RPAR_ "Definition of example")` contains one parameter, `n`. Additionally, the signature's type is `(k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, which is a function type that includes `k`. The parameter `n` is in scope in the function's body, but `k` is not.
`def add (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : (k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   | 0 => n   | k' + 1 => 1 + [add](Definitions/Headers-and-Signatures/#add-_LPAR_in-Parameter-Scope_RPAR_ "Definition of example") n k' `
Like `[add](Definitions/Headers-and-Signatures/#add-_LPAR_in-Parameter-Scope_RPAR_ "Definition of example")`, the signature of `[mustBeEqual](Definitions/Headers-and-Signatures/#mustBeEqual-_LPAR_in-Parameter-Scope_RPAR_ "Definition of example")` contains one parameter, `n`. It is in scope both in the type, where it occurs in a proposition, and in the body, where it occurs as part of the message.
`def mustBeEqual (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : (k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → n = k → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=   fun _ =>     fun     | [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") => s!"Equal - both are {n}!"  `
[Live ↪](javascript:openLiveLink\("CYUwZgBAhswQFAOwgLggOSgFwJSoQNb6a4SBJhBtgFAQQA+EADBALwB8EiN9EBA5BADUEAIysOY4TDjJ+VKqEgBbAK4BnLACEQAUQCOKqABsEyNCTxp4Rc9jwVkLXuQgBlLACcAlogDmqFm4wFWQAfXFuWmCuWloGDzATdgg1AEIAIn1DEwBaCAAjAHssAAtoDxAIAG9EAF8MoA"\))
The section on [function application](Terms/Function-Application/#function-application) describes the interpretation of [optional](Definitions/Headers-and-Signatures/#--tech-term-optional-parameters), [automatic](Definitions/Headers-and-Signatures/#--tech-term-automatic-parameters), [implicit](Terms/Functions/#--tech-term-implicit), and [instance implicit](Type-Classes/#--tech-term-instance-implicit) parameters in detail.
##  7.2.4. Automatic Implicit Parameters[🔗](find/?domain=Verso.Genre.Manual.section&name=automatic-implicit-parameters "Permalink")
By default, otherwise-unbound names that occur in signatures are converted into implicit parameters when possible These parameters are called _automatic implicit parameters_. This is possible when they are not in the function position of an application and when there is sufficient information available in the signature to infer their type and any ordering constraints on them. This process is iterated: if the inferred type for the freshly-inserted implicit parameter has dependencies that are not uniquely determined, then these dependencies are replaced with further implicit parameters.
Implicit parameters that don't correspond to names written in signatures are assigned names akin to those of [inaccessible](Tactic-Proofs/Reading-Proof-States/#--tech-term-inaccessible) hypotheses in proofs, which cannot be referred to. They show up in signatures with a trailing dagger (`'✝'`). This prevents an arbitrary choice of name by Lean from becoming part of the API by being usable as a [named argument](Terms/Function-Application/#--tech-term-named-arguments).
Automatic Implicit Parameters
In this definition of `[map](Definitions/Headers-and-Signatures/#map-_LPAR_in-Automatic-Implicit-Parameters_RPAR_ "Definition of example")`, `α` and `β` are not explicitly bound. Rather than this being an error, they are converted into implicit parameters. Because they must be types, but nothing constrains their universes, the universe parameters `u` and `v` are also inserted.
`def map (f : α → β) : (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β   | [] => []   | x :: xs => f x :: [map](Definitions/Headers-and-Signatures/#map-_LPAR_in-Automatic-Implicit-Parameters_RPAR_ "Definition of example") f xs `
The full signature of `[map](Definitions/Headers-and-Signatures/#map-_LPAR_in-Automatic-Implicit-Parameters_RPAR_ "Definition of example")` is:
`[map](Definitions/Headers-and-Signatures/#map-_LPAR_in-Automatic-Implicit-Parameters_RPAR_ "Definition of example").{u, v} {α : Type u} {β : Type v}   (f : α → β) (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :   [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β`
[Live ↪](javascript:openLiveLink\("CYUwZgBAtghgDhAFJAXBQjcAUEmEFBNwASgjUQA8BnIiAGQEsyAXDQnWhvAKAggB8IBtALoQAvAD5+AzjwgkiaciPGRZKNLATKyQA"\))
No Automatic Implicit Parameters
In this definition, `α` and `β` are not explicitly bound. Because `[autoImplicit](Definitions/Headers-and-Signatures/#autoImplicit "Documentation for option autoImplicit")` is disabled, this is an error:
`set_option [autoImplicit](Definitions/Headers-and-Signatures/#autoImplicit "Documentation for option autoImplicit") false  def map (f : `Unknown identifier `α`  Note: It is not possible to treat `α` as an implicitly bound variable here because the `autoImplicit` option is set to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.`α → `Unknown identifier `β`  Note: It is not possible to treat `β` as an implicitly bound variable here because the `autoImplicit` option is set to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.`β) : (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") `Unknown identifier `α`  Note: It is not possible to treat `α` as an implicitly bound variable here because the `autoImplicit` option is set to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.`α) → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") `Unknown identifier `β`  Note: It is not possible to treat `β` as an implicitly bound variable here because the `autoImplicit` option is set to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.`β | [] => [] | x :: xs => f x :: map f xs `
```
Unknown identifier `α`

Note: It is not possible to treat `α` as an implicitly bound variable here because the `autoImplicit` option is set to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
```

```
Unknown identifier `β`

Note: It is not possible to treat `β` as an implicitly bound variable here because the `autoImplicit` option is set to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
```

The full signature allows the definition to be accepted:
`set_option [autoImplicit](Definitions/Headers-and-Signatures/#autoImplicit "Documentation for option autoImplicit") false  def map.{u, v} {α : Type u} {β : Type v}     (f : α → β) :     (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β   | [] => []   | x :: xs => f x :: map f xs `
Universe parameters are inserted automatically for parameters without explicit type annotations. The type parameters' universes can be inferred, and the appropriate universe parameters inserted, even when `[autoImplicit](Definitions/Headers-and-Signatures/#autoImplicit "Documentation for option autoImplicit")` is disabled:
`set_option [autoImplicit](Definitions/Headers-and-Signatures/#autoImplicit "Documentation for option autoImplicit") false  def map {α β} (f : α → β) :     (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β   | [] => []   | x :: xs => f x :: map f xs `
Iterated Automatic Implicit Parameters
Given a number bounded by `n`, represented by the type `Fin n`, an `[AtLeast](Definitions/Headers-and-Signatures/#AtLeast-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") i` is a natural number paired with a proof that it is at least as large as `i`.
`structure AtLeast (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) where   val : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   val_gt_i : val ≥ i.[val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val") `
These numbers can be added:
`def AtLeast.add (x y : [AtLeast](Definitions/Headers-and-Signatures/#AtLeast-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") i) : [AtLeast](Definitions/Headers-and-Signatures/#AtLeast-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") i :=   AtLeast.mk (x.[val](Definitions/Headers-and-Signatures/#AtLeast___val-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") + y.[val](Definitions/Headers-and-Signatures/#AtLeast___val-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example")) <| byn✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")i:[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n✝x:[AtLeast](Definitions/Headers-and-Signatures/#AtLeast-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") iy:[AtLeast](Definitions/Headers-and-Signatures/#AtLeast-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") i⊢ x.[val](Definitions/Headers-and-Signatures/#AtLeast___val-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y.[val](Definitions/Headers-and-Signatures/#AtLeast___val-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") ≥ ↑i     [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") xmkn✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")i:[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n✝y:[AtLeast](Definitions/Headers-and-Signatures/#AtLeast-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") ival✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")val_gt_i✝:val✝ ≥ ↑i⊢ { [val](Definitions/Headers-and-Signatures/#AtLeast___val-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") := val✝, [val_gt_i](Definitions/Headers-and-Signatures/#AtLeast___val_gt_i-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") := val_gt_i✝ }.[val](Definitions/Headers-and-Signatures/#AtLeast___val-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y.[val](Definitions/Headers-and-Signatures/#AtLeast___val-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") ≥ ↑i     [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") ymk.mkn✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")i:[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n✝val✝¹:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")val_gt_i✝¹:val✝ ≥ ↑ival✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")val_gt_i✝:val✝ ≥ ↑i⊢ { [val](Definitions/Headers-and-Signatures/#AtLeast___val-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") := val✝¹, [val_gt_i](Definitions/Headers-and-Signatures/#AtLeast___val_gt_i-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") := val_gt_i✝¹ }.[val](Definitions/Headers-and-Signatures/#AtLeast___val-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") { [val](Definitions/Headers-and-Signatures/#AtLeast___val-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") := val✝, [val_gt_i](Definitions/Headers-and-Signatures/#AtLeast___val_gt_i-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") := val_gt_i✝ }.[val](Definitions/Headers-and-Signatures/#AtLeast___val-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") ≥ ↑i     [dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic") onlymk.mkn✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")i:[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n✝val✝¹:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")val_gt_i✝¹:val✝ ≥ ↑ival✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")val_gt_i✝:val✝ ≥ ↑i⊢ val✝¹ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") val✝ ≥ ↑i     [omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic")All goals completed! 🐙 `
The signature of `[AtLeast.add](Definitions/Headers-and-Signatures/#AtLeast___add-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example")` requires multiple rounds of automatic implicit parameter insertion. First, `i` is inserted; but its type depends on the upper bound `n` of `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n`. In the second round, `n` is inserted, using a machine-chosen name. Because `n`'s type is `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, which has no dependencies, the process terminates. The final signature can be seen with ``Lean.Parser.Command.check : command``[`#check`](Interacting-with-Lean/#Lean___Parser___Command___check):
``[AtLeast.add](Definitions/Headers-and-Signatures/#AtLeast___add-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") {n✝ : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} {i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n✝} (x y : [AtLeast](Definitions/Headers-and-Signatures/#AtLeast-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") i) : [AtLeast](Definitions/Headers-and-Signatures/#AtLeast-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") i`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [AtLeast.add](Definitions/Headers-and-Signatures/#AtLeast___add-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") `
```
[AtLeast.add](Definitions/Headers-and-Signatures/#AtLeast___add-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") {n✝ : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} {i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n✝} (x y : [AtLeast](Definitions/Headers-and-Signatures/#AtLeast-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") i) : [AtLeast](Definitions/Headers-and-Signatures/#AtLeast-_LPAR_in-Iterated-Automatic-Implicit-Parameters_RPAR_ "Definition of example") i
```

[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgIIgDLwIakQCgJaIBciAYvgHaIUCUiA7gBbwIBQiiAbpgDbGIA5TCHZdeAfQDmIcYRLc+gUyJE+AHQLWrACbwAZinRZQqzFq14AHogCe/VBmwgVdEvaNO5AXlFvHqgLYA1pbqvIgA1DahPHQAPAA+iABG1qIcUNjwwIgWaYgZwFk2eVrA+P4ADogA9hQ8qRwc1f7wkphAA"\))
Automatic implicit parameter insertion takes place after the insertion of parameters due to [section variables](Namespaces-and-Sections/#--tech-term-Section-variables). Parameters that correspond to section variables have the same name as the corresponding variable, even when they do not correspond to a name written directly in the signature, and disabling automatic implicit parameters has no effect the parameters that correspond to section variables. However, when automatic implicit parameters are enabled, section variable declarations that contain otherwise-unbound variables receive additional section variables that follow the same rules as those for implicit parameters.
Automatic implicit parameters insertion is controlled by two options. By default, automatic implicit parameter insertion is _relaxed_ , which means that any unbound identifier may be a candidate for automatic insertion. Setting the option `[relaxedAutoImplicit](Definitions/Headers-and-Signatures/#relaxedAutoImplicit "Documentation for option relaxedAutoImplicit")` to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` disables relaxed mode and causes only identifiers that consist of a single character followed by zero or more digits to be considered for automatic insertion.
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=relaxedAutoImplicit "Permalink")option
```
relaxedAutoImplicit
```

Default value: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
When "relaxed" mode is enabled, any atomic nonempty identifier is eligible for auto bound implicit locals (see option `[autoImplicit](Definitions/Headers-and-Signatures/#autoImplicit "Documentation for option autoImplicit")`).
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=autoImplicit "Permalink")option
```
autoImplicit
```

Default value: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
Unbound local variables in declaration headers become implicit arguments. In "relaxed" mode (default), any atomic identifier is eligible, otherwise only single character followed by numeric digits are eligible. For example, `def f (x : Vector α n) : Vector α n :=` automatically introduces the implicit variables {α n}.
Relaxed vs Non-Relaxed Automatic Implicit Parameters
Misspelled identifiers or missing imports can end up as unwanted implicit parameters, as in this example:
`inductive Answer where   | yes   | maybe   | no ``def select (choices : α × α × α) : Asnwer →  α   | `Invalid dotted identifier notation: The expected type of `.yes`   Asnwer is not of the form `C ...` or `... → C ...` where C is a constant`.yes => choices.1 | .maybe => choices.2.1 | .no => choices.2.2 `
The resulting error message states that the argument's type is not a constant, so dot notation cannot be used in the pattern:

```
Invalid dotted identifier notation: The expected type of `.yes`
  Asnwer
is not of the form `C ...` or `... → C ...` where C is a constant
```

This is because the signature is:
`select.{u_1, u_2}   {α : Type u_1}   {Asnwer : Sort u_2}   (choices : α × α × α) :   Asnwer → α`
Disabling relaxed automatic implicit parameters makes the error more clear, while still allowing the type to be inserted automatically:
`set_option [relaxedAutoImplicit](Definitions/Headers-and-Signatures/#relaxedAutoImplicit "Documentation for option relaxedAutoImplicit") false  def select (choices : α × α × α) : `Unknown identifier `Asnwer`  Note: It is not possible to treat `Asnwer` as an implicitly bound variable here because it has multiple characters while the `relaxedAutoImplicit` option is set to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.`Asnwer → α | .yes => choices.1 | .maybe => choices.2.1 | .no => choices.2.2 `
```
Unknown identifier `Asnwer`

Note: It is not possible to treat `Asnwer` as an implicitly bound variable here because it has multiple characters while the `relaxedAutoImplicit` option is set to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
```

Correcting the error allows the definition to be accepted.
`set_option [relaxedAutoImplicit](Definitions/Headers-and-Signatures/#relaxedAutoImplicit "Documentation for option relaxedAutoImplicit") false  def select (choices : α × α × α) : [Answer](Definitions/Headers-and-Signatures/#Answer-_LPAR_in-Relaxed-vs-Non-Relaxed-Automatic-Implicit-Parameters_RPAR_ "Definition of example") →  α   | [.yes](Definitions/Headers-and-Signatures/#Answer___yes-_LPAR_in-Relaxed-vs-Non-Relaxed-Automatic-Implicit-Parameters_RPAR_ "Definition of example") => choices.1   | [.maybe](Definitions/Headers-and-Signatures/#Answer___maybe-_LPAR_in-Relaxed-vs-Non-Relaxed-Automatic-Implicit-Parameters_RPAR_ "Definition of example") => choices.2.1   | [.no](Definitions/Headers-and-Signatures/#Answer___no-_LPAR_in-Relaxed-vs-Non-Relaxed-Automatic-Implicit-Parameters_RPAR_ "Definition of example") => choices.2.2 `
Turning off automatic implicit parameters entirely leads to the definition being rejected:
`set_option [autoImplicit](Definitions/Headers-and-Signatures/#autoImplicit "Documentation for option autoImplicit") false  def select (choices : `Unknown identifier `α`  Note: It is not possible to treat `α` as an implicitly bound variable here because the `autoImplicit` option is set to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.`α × `Unknown identifier `α`  Note: It is not possible to treat `α` as an implicitly bound variable here because the `autoImplicit` option is set to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.`α × `Unknown identifier `α`  Note: It is not possible to treat `α` as an implicitly bound variable here because the `autoImplicit` option is set to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.`α) : [Answer](Definitions/Headers-and-Signatures/#Answer-_LPAR_in-Relaxed-vs-Non-Relaxed-Automatic-Implicit-Parameters_RPAR_ "Definition of example") → `Unknown identifier `α`  Note: It is not possible to treat `α` as an implicitly bound variable here because the `autoImplicit` option is set to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.`α | [.yes](Definitions/Headers-and-Signatures/#Answer___yes-_LPAR_in-Relaxed-vs-Non-Relaxed-Automatic-Implicit-Parameters_RPAR_ "Definition of example") => choices.1 | [.maybe](Definitions/Headers-and-Signatures/#Answer___maybe-_LPAR_in-Relaxed-vs-Non-Relaxed-Automatic-Implicit-Parameters_RPAR_ "Definition of example") => choices.2.1 | [.no](Definitions/Headers-and-Signatures/#Answer___no-_LPAR_in-Relaxed-vs-Non-Relaxed-Automatic-Implicit-Parameters_RPAR_ "Definition of example") => choices.2.2 `
```
Unknown identifier `α`

Note: It is not possible to treat `α` as an implicitly bound variable here because the `autoImplicit` option is set to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
```

[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABAQRAZwO6IE7KwAs9EAoZZAH2QE9ENyrkBbAQxoCMyLqQB7IA"\))
[←7.1. Modifiers](Definitions/Modifiers/#declaration-modifiers "7.1. Modifiers")[7.3. Definitions→](Definitions/Definitions/#The-Lean-Language-Reference--Definitions--Definitions "7.3. Definitions")

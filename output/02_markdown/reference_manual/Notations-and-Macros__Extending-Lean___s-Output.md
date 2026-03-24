[←23.6. Elaborators](Notations-and-Macros/Elaborators/#elaborators "23.6. Elaborators")[24. Build Tools and Distribution→](Build-Tools-and-Distribution/#build-tools-and-distribution "24. Build Tools and Distribution")
#  23.7. Extending Lean's Output[🔗](find/?domain=Verso.Genre.Manual.section&name=unexpand-and-delab "Permalink")
Extending Lean with new syntax and implementing the new syntax with macros and elaborators allows users to express ideas to Lean more conveniently. However, Lean is an _interactive_ theorem prover: it is also important that the feedback it provides can be readily understood. Syntax extensions should be used in _output_ as well as in _input_.
There are two primary mechanisms for instructing Lean to use a syntax extension in its output: 

Unexpanders
    
Unexpanders are the inverse of [macros](Notations-and-Macros/Macros/#--tech-term-Macros). Macros implement new syntax in terms of the old syntax by translation, _expanding_ the new feature into encodings in pre-existing features. Like macros, _unexpanders_ translate `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")` into `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")`; unlike macros, they transform the encodings into the new extensions. 

Delaborators
    
Delaborators are the inverse of [elaborators](Notations-and-Macros/Elaborators/#--tech-term-elaborators). While elaborators translate `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")` into the core type theory's `Expr`, _delaborators_ translate `Expr`s into `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")`.
Before an `Expr` is displayed, it is first delaborated and then unexpanded. The delaborator tracks the position in the original `Expr` that its output originated from; this position is encoded in the resulting syntax's `[SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo")`. Just as macro expansion automatically annotates the resulting syntax with synthetic source information that correspond to the original syntax's position, the unexpansion mechanism preserves the resulting syntax's association with the underlying `Expr`. This association enables Lean's interactive features that provide information about the resulting syntax when it is shown in [proof states](Tactic-Proofs/#--tech-term-proof-state) and diagnostics.
##  23.7.1. Unexpanders[🔗](find/?domain=Verso.Genre.Manual.section&name=Unexpanders "Permalink")
Just as macros are registered in a table that maps [syntax kinds](Notations-and-Macros/Defining-New-Syntax/#--tech-term-syntax-kind) to macro implementations, unexpanders are registered in a table that maps the names of constants to unexpander implementations. Before Lean displays syntax to users, it attempts to rewrite each application of a constant in the syntax according to this table. Occurrences of the context that are not applications are treated as applications with zero arguments.
Unexpansion proceeds from the inside out. The unexpander is passed the syntax of the application, with implicit arguments hidden, after the arguments have been unexpanded. If the option `pp.explicit` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` or `pp.notation` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, then unexpanders are not used.
An unexpander has type `[Lean.PrettyPrinter.Unexpander](Notations-and-Macros/Extending-Lean___s-Output/#Lean___PrettyPrinter___Unexpander "Documentation for Lean.PrettyPrinter.Unexpander")`, which is an abbreviation for `Syntax → Lean.PrettyPrinter.UnexpandM Syntax`. In the remainder of this section, the names `[Unexpander](Notations-and-Macros/Extending-Lean___s-Output/#Lean___PrettyPrinter___Unexpander "Documentation for Lean.PrettyPrinter.Unexpander")` and `[UnexpandM](Notations-and-Macros/Extending-Lean___s-Output/#Lean___PrettyPrinter___UnexpandM "Documentation for Lean.PrettyPrinter.UnexpandM")` are used unqualified. `[UnexpandM](Notations-and-Macros/Extending-Lean___s-Output/#Lean___PrettyPrinter___UnexpandM "Documentation for Lean.PrettyPrinter.UnexpandM")` is a monad that supports quotation and failure via its `MonadQuotation` and `[MonadExcept](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")` instances.
An unexpander should either return unexpanded syntax or fail using `[throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") ()`. If the unexpander succeeds, then the resulting syntax is unexpanded again; if it fails, then the next unexpander is tried. When no unexpander succeeds for the syntax, its child nodes are unexpanded until all opportunities for unexpansion are exhausted.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.PrettyPrinter.Unexpander "Permalink")def
```


Lean.PrettyPrinter.Unexpander : Type


Lean.PrettyPrinter.Unexpander : Type


```

Function that tries to reverse macro expansions as a post-processing step of delaboration. While less general than an arbitrary delaborator, it can be declared without importing `Lean`. Used by the `[app_unexpander]` attribute.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.PrettyPrinter.UnexpandM "Permalink")def
```


Lean.PrettyPrinter.UnexpandM (α : Type) : Type


Lean.PrettyPrinter.UnexpandM (α : Type) :
  Type


```

The unexpander monad, essentially `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax") → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α`. The `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")` is the `ref`, and it has the possibility of failure without an error message.
An unexpander for a constant is registered by applying the `app_unexpander` attribute. [Custom operators](Notations-and-Macros/Custom-Operators/#operators) and [notations](Notations-and-Macros/Notations/#notations) automatically create unexpanders for the syntax that they introduce.
attributeUnexpander Registration

```
attr ::= ...
    | app_unexpander ident
```

Registers an unexpander of type `[Unexpander](Notations-and-Macros/Extending-Lean___s-Output/#Lean___PrettyPrinter___Unexpander "Documentation for Lean.PrettyPrinter.Unexpander")` for applications of a constant.
Custom Unit Type
A type equivalent to `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")`, but with its own notation, can be defined as a zero-field structure and a macro:
`structure Solo where   mk ::  [syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") "‹" "›" : term  [macro_rules](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules "Documentation for syntax")   | `(term|‹›) => ``([Solo.mk](Notations-and-Macros/Extending-Lean___s-Output/#Solo___mk-_LPAR_in-Custom-Unit-Type_RPAR_ "Definition of example")) `
While the new notation can be used to write theorem statements, it does not appear in proof states. For example, when proving that all values of type `[Solo](Notations-and-Macros/Extending-Lean___s-Output/#Solo-_LPAR_in-Custom-Unit-Type_RPAR_ "Definition of example")` are equal to `‹›`, the initial proof state is:
v:[Solo](Notations-and-Macros/Extending-Lean___s-Output/#Solo-_LPAR_in-Custom-Unit-Type_RPAR_ "Definition of example")⊢ v [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [{](Notations-and-Macros/Extending-Lean___s-Output/#Solo___mk-_LPAR_in-Custom-Unit-Type_RPAR_ "Definition of example") [}](Notations-and-Macros/Extending-Lean___s-Output/#Solo___mk-_LPAR_in-Custom-Unit-Type_RPAR_ "Definition of example")
This proof state shows the constructor using [structure instance](The-Type-System/Inductive-Types/#--tech-term-structure-instance) syntax. An unexpander can be used to override this choice. Because `[Solo.mk](Notations-and-Macros/Extending-Lean___s-Output/#Solo___mk-_LPAR_in-Custom-Unit-Type_RPAR_ "Definition of example")` cannot be applied to any arguments, the unexpander is free to ignore the syntax, which will always be ``(Solo.mk)`.
`@[app_unexpander [Solo.mk](Notations-and-Macros/Extending-Lean___s-Output/#Solo___mk-_LPAR_in-Custom-Unit-Type_RPAR_ "Definition of example")] def unexpandSolo : [Lean.PrettyPrinter.Unexpander](Notations-and-Macros/Extending-Lean___s-Output/#Lean___PrettyPrinter___Unexpander "Documentation for Lean.PrettyPrinter.Unexpander")   | _ => `(‹›) `
With this unexpander, the initial state of the proof now renders with the correct syntax:
v:[Solo](Notations-and-Macros/Extending-Lean___s-Output/#Solo-_LPAR_in-Custom-Unit-Type_RPAR_ "Definition of example")⊢ v [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [‹](Notations-and-Macros/Extending-Lean___s-Output/#Solo___mk-_LPAR_in-Custom-Unit-Type_RPAR_ "Definition of example")[›](Notations-and-Macros/Extending-Lean___s-Output/#Solo___mk-_LPAR_in-Custom-Unit-Type_RPAR_ "Definition of example")
Unexpansion and Arguments
A `[ListCursor](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example")` represents a position in a `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List")`. `[ListCursor.before](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor___before-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example")` contains the reversed list of elements prior to the position, and `[ListCursor.after](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor___after-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example")` contains the elements after the position.
`structure ListCursor (α) where   before : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α   after : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α deriving [Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") `
List cursors can be moved to the left or to the right:
`def ListCursor.left : [ListCursor](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([ListCursor](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") α)   | ⟨[], _⟩ => [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")   | ⟨l :: ls, rs⟩ => [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ⟨ls, l :: rs⟩  def ListCursor.right : [ListCursor](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([ListCursor](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") α)   | ⟨_, []⟩ => [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")   | ⟨ls, r :: rs⟩ => [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ⟨r :: ls, rs⟩ `
They can also be moved all the way to the left or all the way to the right:
`def ListCursor.rewind : [ListCursor](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") α → [ListCursor](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") α   | xs@⟨[], _⟩ => xs   | ⟨l :: ls, rs⟩ => [rewind](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor___rewind-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") ⟨ls, l :: rs⟩ termination_by xs => xs.[before](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor___before-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example")  def ListCursor.fastForward : [ListCursor](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") α → [ListCursor](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") α   | xs@⟨_, []⟩ => xs   | ⟨ls, r :: rs⟩ => [fastForward](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor___fastForward-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") ⟨r :: ls, rs⟩ termination_by xs => xs.[after](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor___after-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") `
However, the need to reverse the list of previous elements can make list cursors difficult to understand. A cursor can be given a notation in which a flag (`🚩`) marks the cursor's location in a list:
`[syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") "[" term,* " 🚩 " term,* "]": term [macro_rules](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules "Documentation for syntax")   | `([$ls,* 🚩 $rs,*]) =>     ``(ListCursor.mk [$[$((ls : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")).[reverse](Basic-Types/Arrays/#Array___reverse "Documentation for Array.reverse"))],*] [$rs,*]) `
In the macro, the sequences of elements have type `[Syntax.TSepArray](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___mk "Documentation for Lean.Syntax.TSepArray") `term ","`. The type annotation as `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")` causes a coercion to fire so that `[Array.reverse](Basic-Types/Arrays/#Array___reverse "Documentation for Array.reverse")` can be applied, and a similar coercion reinserts the separating commas. These coercions are described in the section on [typed syntax](Notations-and-Macros/Defining-New-Syntax/#typed-syntax).
While the syntax works, it is not used in Lean's output:
``{ [before](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor___before-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") := [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")3[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons"), [after](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor___after-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") := [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")4[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 5[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") } : [ListCursor](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [1, 2, 3 🚩 4, 5] `
```
{ [before](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor___before-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") := [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")3[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons"), [after](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor___after-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") := [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")4[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 5[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") } : [ListCursor](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

An unexpander solves this problem. The unexpander relies on the built-in unexpanders for list literals already having rewritten the two lists:
`@[app_unexpander ListCursor.mk] def unexpandListCursor : [Lean.PrettyPrinter.Unexpander](Notations-and-Macros/Extending-Lean___s-Output/#Lean___PrettyPrinter___Unexpander "Documentation for Lean.PrettyPrinter.Unexpander")   | `($_ [$ls,*] [$rs,*]) =>     `([$((ls : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")).[reverse](Basic-Types/Arrays/#Array___reverse "Documentation for Array.reverse")),* 🚩 $(rs),*])   | _ => [throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") () ```[1, 2, 3 🚩 4[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 5] : [ListCursor](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [1, 2, 3 🚩 4, 5] `
```
[1, 2, 3 🚩 4[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 5] : [ListCursor](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```
``[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [1, 2, 3, 4 🚩 5]`[#reduce](Interacting-with-Lean/#Lean___reduceCmd "Documentation for syntax") [1, 2, 3 🚩 4, 5].[right](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor___right-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") `
```
[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [1, 2, 3, 4 🚩 5]
```
``[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [1 🚩 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 4[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 5]`[#reduce](Interacting-with-Lean/#Lean___reduceCmd "Documentation for syntax") [1, 2, 3 🚩 4, 5].[left](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor___left-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example") >>= (·.[left](Notations-and-Macros/Extending-Lean___s-Output/#ListCursor___left-_LPAR_in-Unexpansion-and-Arguments_RPAR_ "Definition of example")) `
```
[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [1 🚩 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 4[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 5]
```

[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgDIEtQGE7APZkQBSCNwAJSIDuAFvAgFCKIBG8AZnkgFwroiJH2IAhixA1EXNKD60AJjVQA3VADsA5ogBK8AA5has1t0zY8AOgA2rXhJ5YwufEUSAkwkQB5bSFQ5lhSSDsHPhIBAB9EQAvyAG0AXQAaRAB9QEvyRABeAD5EZR94MMjzcS5zYAT7VMzEXABbJAiShMKOLnL9ORYjAJMwUzBUVUprTsC8Phd3T29fAn8RxxCGcIjEhNiKrJzlPMWC0sR8Zv3gdaqcWsiD4r3Wgw7Z7t74chUZcWHusdd7+1H+HYAPYAAAWi8SSJ0B+XqRUQDSOJwQz2Ur3qeyaLWOtFEYGqKkEXh8iUYAE9EID0llAaZmGw6Ld3j8eixBKAAGJ4ciCMCvGzGRmfBlBP6IcKAkErRBrClk4BQuGXeHS5lsjlclEK+WY7G45T4qZE0nkypU4TYtqGb4OUw4Fj+Qjk3m8UhvS2/CjUOgMGnscRpSUxASmsQcP2Q+munogHB2rgEB2C35kL48aQ7UFlY7S+xy5qak5Ru2oxow1ravEE5QGmXSqneunAYnKECCf6IABEUTbiG1cQAVO3EIBKt4HPf7bZiba42to1UEUDAOESkEssp2AAMCFEACQNfvDrf2PsxMiZAQMNcbiOmaoAa0lW+3BAIJTeAEEwGBBKTkPBBMpTAAKjQ1QkI8Cg0MA8AkPEvYxPeh6wSEtAAMRQNQUB3lEACMCQAEwJAAzEOiAACwJAArAGtBAlEgjaNoiQQFs/zaH+cj4Fet4Bu0iBMfALFsRGLq/v+AAKCAgCAxLiSo2KmAAqsxrHIjQ+QbluiT3rucHbghx4UmeiAbo+z7AG+H5figImAcBoEIOB9hQX2xFbgQ9gkEeCwikk0ogJQC7kIQSGoehmE4Yg+GIERw5kYglH6MhCAyNASDYXhhHEbFlG9P0gwJUlKWSuFkXRaRFExBYViIBkGR+gQADtlUiCQQA"\))
##  23.7.2. Delaborators[🔗](find/?domain=Verso.Genre.Manual.section&name=delaborators "Permalink")
A delaborator is function of type `Lean.PrettyPrinter.Delaborator.Delab`, which is an abbreviation for `Lean.PrettyPrinter.Delaborator.DelabM [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")`. Unlike unexpanders, delaborators are not implemented as functions. This is to make it easier to implement them correctly: the monad `DelabM` tracks the current position in the expression that's being delaborated so the delaboration mechanism can annotate the resulting syntax.
Delaborators are registered with the `delab` attribute. An internal table maps the names of the constructors of `Expr` (without namespaces) to delaborators. Additionally, the name `app.`﻿`ccc` is consulted to find delaborators for applications of the constant `ccc`, and the name `mdata.`﻿`kkk` is consulted to find delaborators for `Expr.mdata` constructors with a single key `kkk` in their metadata.
attributeDelaborator Registration
The `delab` attribute registers a delaborator for the indicated constructor or metadata key of `Expr`.

```
attr ::= ...
    | delab ident
```

The `app_delab ` attribute registers a delaborator for applications of the indicated constant after [resolving](Terms/Identifiers/#--tech-term-resolving) it in the current [scope](Namespaces-and-Sections/#--tech-term-section-scope).

```
attr ::= ...
    | 


@[app_delab c] registers a delaborator for applications with head constant c.
Such delaborators also apply to the constant c itself (known as a "nullary application").


This attribute should be applied to definitions of type Lean.PrettyPrinter.Delaborator.Delab.


When defining delaborators for constant applications, one should prefer this attribute over @[delab app.c],
as @[app_delab c] first performs name resolution on c in the current scope.


app_delab ident
```

The monad `DelabM` is a [reader monad](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#--tech-term-Reader-monads) that includes access to the current position in the `Expr`. Recursive delaboration is performed by adjusting the reader monad's tracked position, rather than by explicitly passing a subexpression to another function. The most important functions for working with subexpressions in delaborators are in the namespace `Lean.PrettyPrinter.Delaborator.SubExp`:
  * `getExpr` retrieves the current expression for analysis.
  * `withAppFn` adjusts the current position to be that of the function in an application.
  * `withAppArg` adjusts the current position to be that of the argument in an application
  * `withAppFnArgs` decomposes the current expression into a non-application function and its arguments, focusing on each.
  * `withBindingBody` descends into the body of a function or function type.


Further functions to descend into the remaining constructors of `Expr` are available.
[←23.6. Elaborators](Notations-and-Macros/Elaborators/#elaborators "23.6. Elaborators")[24. Build Tools and Distribution→](Build-Tools-and-Distribution/#build-tools-and-distribution "24. Build Tools and Distribution")

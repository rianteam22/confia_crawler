[←23.4. Defining New Syntax](Notations-and-Macros/Defining-New-Syntax/#syntax-ext "23.4. Defining New Syntax")[23.6. Elaborators→](Notations-and-Macros/Elaborators/#elaborators "23.6. Elaborators")
#  23.5. Macros[🔗](find/?domain=Verso.Genre.Manual.section&name=macros "Permalink")
_Macros_ are transformations from `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")` to `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")` that occur during [elaboration](Notations-and-Macros/Elaborators/#--tech-term-elaborators) and during [tactic execution](Tactic-Proofs/Custom-Tactics/#tactic-macros). Replacing syntax with the result of transforming it with a macro is called _macro expansion_. Multiple macros may be associated with a single [syntax kind](Notations-and-Macros/Defining-New-Syntax/#--tech-term-syntax-kind), and they are attempted in order of definition. Macros are run in a [monad](Functors___-Monads-and--do--Notation/#--tech-term-Monad) that has access to some compile-time metadata and has the ability to either emit an error message or to delegate to subsequent macros, but the macro monad is much less powerful than the elaboration monads.
Macros are associated with [syntax kinds](Notations-and-Macros/Defining-New-Syntax/#--tech-term-syntax-kind). An internal table maps syntax kinds to macros of type `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax") → [MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") [Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")`. Macros delegate to the next entry in the table by throwing the `[unsupportedSyntax](Notations-and-Macros/Macros/#Lean___Macro___Exception___unsupportedSyntax "Documentation for Lean.Macro.Exception.unsupportedSyntax")` exception. A given `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")` value _is a macro_ when there is a macro associated with its syntax kind that does not throw `[unsupportedSyntax](Notations-and-Macros/Macros/#Lean___Macro___Exception___unsupportedSyntax "Documentation for Lean.Macro.Exception.unsupportedSyntax")`. If a macro throws any other exception, an error is reported to the user. [Syntax categories](Notations-and-Macros/Defining-New-Syntax/#--tech-term-syntax-categories) are irrelevant to macro expansion; however, because each syntax kind is typically associated with a single syntax category, they do not interfere in practice.
Macro Error Reporting
The following macro reports an error when its parameter is the literal numeral five. It expands to its argument in all other cases.
`[syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") &"notFive" term:[arg](Notations-and-Macros/Precedence/#precArg "Documentation for syntax") : term [open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Lean [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") [macro_rules](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules "Documentation for syntax")   | `(term|notFive 5) =>     [Macro.throwError](Notations-and-Macros/Macros/#Lean___Macro___throwError "Documentation for Lean.Macro.throwError") "'5' is not allowed here"   | `(term|notFive $e) =>     [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") e `
When applied to terms that are not syntactically the numeral five, elaboration succeeds:
``5`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") notFive (2 + 3) `
```
5
```

When the error case is triggered, the user receives an error message:
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") `'5' is not allowed here`notFive 5 `
```
'5' is not allowed here
```

[Live ↪](javascript:openLiveLink\("M4TwdgLghgHgBAMgERgPYQGIEsBuBTJOCPAJwFsAuKEgczgqNLIChUAHPMOAGTyi6xhmZKAGMSqAPokArgBs8wZnDgAfOAAMAFMXKq0mXHjgBWAJRwAvAD5lKuAFkxEgHQQAFhIDuAURISSOCQAchNguCxgOAM4KDk5VC88ABM4d1ICO3VtXTJ9dGx8OAASPAsbOxU2GRJjPGZmAGI8HDjogqM4LQAmOABqOABmMyA"\))
Before elaborating a piece of syntax, the elaborator checks whether its [syntax kind](Notations-and-Macros/Defining-New-Syntax/#--tech-term-syntax-kind) has macros associated with it. These are attempted in order. If a macro succeeds, potentially returning syntax with a different kind, the check is repeated and macros are expanded again until the outermost layer of syntax is no longer a macro. Elaboration or tactic execution can then proceed. Only the outermost layer of syntax (typically a `[node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node")`) is expanded, and the output of macro expansion may contain nested syntax that is a macro. These nested macros are expanded in turn when the elaborator reaches them.
In particular, macro expansion occurs in three situations in Lean:
  1. During term elaboration, macros in the outermost layer of the syntax to be elaborated are expanded prior to invoking the [syntax's term elaborator](Notations-and-Macros/Elaborators/#elaborators).
  2. During command elaboration, macros in the outermost layer of the syntax to be elaborated are expanded prior to invoking the [syntax's command elaborator](Notations-and-Macros/Elaborators/#elaborators).
  3. During tactic execution, macros in the outermost layer of the syntax to be elaborated are expanded [prior to executing the syntax as a tactic](Tactic-Proofs/Custom-Tactics/#tactic-macros).


##  23.5.1. Hygiene[🔗](find/?domain=Verso.Genre.Manual.section&name=macro-hygiene "Permalink")
A macro is _hygienic_ if its expansion cannot result in identifier capture. Identifier capture is when an identifier ends up referring to a binding site other than that which is in scope where the identifier occurs in the source code. There are two types of identifier capture:
  * If a macro's expansion introduces binders, then identifiers that are parameters to the macro may end up referring to the introduced binders if their names happen to match.
  * If a macro's expansion is intended to refer to a name, but the macro is used in a context that either locally binds this name or in which a new global name has been introduced, it may end up referring to the wrong name.


The first kind of variable capture can be avoided by ensuring that every binding introduced by a macro uses a freshly generated, globally-unique name, while the second can be avoided by always using fully-qualified names to refer to constants. The fresh names must be generated again at each invocation of the macro to avoid variable capture in recursive macros. These techniques are error-prone. Variable capture issues are difficult to test for because they rely on coincidences of name choices, and consistently applying these techniques results in noisy code.
Lean features automatic hygiene: in almost all cases, macros are automatically hygienic. Capture by introduced bindings is avoided by annotating identifiers introduced by a macro with _macro scopes_ , which uniquely identify each invocation of macro expansion. If the binding and the use of the identifier have the same macro scopes, then they were introduced by the same step of macro expansion and should refer to one another. Similarly, uses of global names in code generated by a macro are not captured by local bindings in the context in which they are expanded because these use sites have macro scopes that are not present in the binding occurrence. Capture by newly-introduced global names is prevented by annotating potential global name references with the set of global names that match at quotation time in code produced in the macro's body. Identifiers annotated with potential referents are called _pre-resolved identifiers_ , and the `[Syntax.Preresolved](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Preresolved___namespace "Documentation for Lean.Syntax.Preresolved")` field on the `[Syntax.ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.ident")` constructor is used to store the potential referents. During elaboration, if an identifier has pre-resolved global names associated with it, then other global names are not considered as valid reference targets.
The introduction of macro scopes and pre-resolved identifiers to generated syntax occurs during [quotation](Notations-and-Macros/Macros/#--tech-term-Quotation). Macros that construct syntax by other means than quotation should also ensure hygiene by some other means. For more details on Lean's hygiene algorithm, please consult Ullrich and de Moura (2020)Sebastian Ullrich and Leonardo de Moura, 2020. “Beyond notations: Hygienic macro expansion for theorem proving languages”. In  _Proceedings of the International Joint Conference on Automated Reasoning._ and Ullrich (2023)Sebastian Ullrich, 2023. _[An Extensible Theorem Proving Frontend](https://www.lean-lang.org/papers/thesis-sebastian.pdf)_. Dr. Ing. dissertation, Karlsruhe Institute of Technology.
##  23.5.2. The Macro Monad[🔗](find/?domain=Verso.Genre.Manual.section&name=macro-monad "Permalink")
The macro monad `[MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM")` is sufficiently powerful to implement hygiene and report errors. Macro expansion does not have the ability to modify the environment directly, to carry out unification, to examine the current local context, or to do anything else that only makes sense in one particular context. This allows the same macro mechanism to be used throughout Lean, and it makes macros much easier to write than [elaborators](Notations-and-Macros/Elaborators/#--tech-term-elaborators).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.MacroM "Permalink")def
```


Lean.MacroM (α : Type) : Type


Lean.MacroM (α : Type) : Type


```

The `MacroM` monad is the main monad for macro expansion. It has the information needed to handle hygienic name generation, and is the monad that `macro` definitions live in.
Notably, this is a (relatively) pure monad: there is no `[IO](IO/Logical-Model/#IO "Documentation for IO")` and no access to the `Environment`. That means that things like declaration lookup are impossible here, as well as `[IO.Ref](IO/Mutable-References/#IO___Ref "Documentation for IO.Ref")` or other side-effecting operations. For more capabilities, macros can instead be written as `elab` using `adaptExpander`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Macro.expandMacro? "Permalink")def
```


Lean.Macro.expandMacro? (stx : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")) :
  [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax"))


Lean.Macro.expandMacro?
  (stx : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")) :
  [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax"))


```

`expandMacro? stx` returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") stxNew` if `stx` is a macro, and `stxNew` is its expansion.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Macro.trace "Permalink")def
```


Lean.Macro.trace (clsName : Lean.Name) (msg : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


Lean.Macro.trace (clsName : Lean.Name)
  (msg : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Add a new trace message, with the given trace class and message.
###  23.5.2.1. Exceptions and Errors[🔗](find/?domain=Verso.Genre.Manual.section&name=macro-exceptions "Permalink")
The `[unsupportedSyntax](Notations-and-Macros/Macros/#Lean___Macro___Exception___unsupportedSyntax "Documentation for Lean.Macro.Exception.unsupportedSyntax")` exception is used for control flow during macro expansion. It indicates that the current macro is incapable of expanding the received syntax, but that an error has not occurred. The exceptions thrown by `[throwError](Notations-and-Macros/Macros/#Lean___Macro___throwError "Documentation for Lean.Macro.throwError")` and `[throwErrorAt](Notations-and-Macros/Macros/#Lean___Macro___throwErrorAt "Documentation for Lean.Macro.throwErrorAt")` terminate macro expansion, reporting the error to the user.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Macro.throwUnsupported "Permalink")def
```


Lean.Macro.throwUnsupported {α : Type} : [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") α


Lean.Macro.throwUnsupported {α : Type} :
  [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") α


```

Throw an `unsupportedSyntax` exception.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Macro.Exception.unsupportedSyntax "Permalink")constructor of Lean.Macro.Exception
```


Lean.Macro.Exception.unsupportedSyntax : Lean.Macro.Exception


Lean.Macro.Exception.unsupportedSyntax :
  Lean.Macro.Exception


```

An unsupported syntax exception. We keep this separate because it is used for control flow: if one macro does not support a syntax then we try the next one.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Macro.throwError "Permalink")def
```


Lean.Macro.throwError {α : Type} (msg : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") α


Lean.Macro.throwError {α : Type}
  (msg : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") α


```

Throw an error with the given message, using the `ref` for the location information.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Macro.throwErrorAt "Permalink")def
```


Lean.Macro.throwErrorAt {α : Type} (ref : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")) (msg : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") α


Lean.Macro.throwErrorAt {α : Type}
  (ref : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")) (msg : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") α


```

Throw an error with the given message and location information.
###  23.5.2.2. Hygiene-Related Operations[🔗](find/?domain=Verso.Genre.Manual.section&name=macro-monad-hygiene "Permalink")
[Hygiene](Notations-and-Macros/Macros/#--tech-term-hygienic) is implemented by adding [macro scopes](Notations-and-Macros/Macros/#--tech-term-macro-scopes) to the identifiers that occur in syntax. Ordinarily, the process of [quotation](Notations-and-Macros/Macros/#--tech-term-Quotation) adds all necessary scopes, but macros that construct syntax directly must add macro scopes to the identifiers that they introduce.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Macro.withFreshMacroScope "Permalink")def
```


Lean.Macro.withFreshMacroScope {α : Type} (x : [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") α) :
  [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") α


Lean.Macro.withFreshMacroScope {α : Type}
  (x : [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") α) : [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") α


```

Increments the macro scope counter so that inside the body of `x` the macro scope is fresh.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Macro.addMacroScope "Permalink")def
```


Lean.Macro.addMacroScope (n : Lean.Name) : [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") Lean.Name


Lean.Macro.addMacroScope (n : Lean.Name) :
  [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") Lean.Name


```

Add a new macro scope to the name `n`.
###  23.5.2.3. Querying the Environment[🔗](find/?domain=Verso.Genre.Manual.section&name=macro-environment "Permalink")
Macros have only limited support for querying the environment. They can check whether a constant exists and resolve names, but further introspection is unavailable.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Macro.hasDecl "Permalink")def
```


Lean.Macro.hasDecl (declName : Lean.Name) : [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Lean.Macro.hasDecl
  (declName : Lean.Name) :
  [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the environment contains a declaration with name `declName`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Macro.getCurrNamespace "Permalink")def
```


Lean.Macro.getCurrNamespace : [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") Lean.Name


Lean.Macro.getCurrNamespace :
  [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") Lean.Name


```

Gets the current namespace given the position in the file.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Macro.resolveNamespace "Permalink")def
```


Lean.Macro.resolveNamespace (n : Lean.Name) :
  [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") Lean.Name)


Lean.Macro.resolveNamespace
  (n : Lean.Name) :
  [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") Lean.Name)


```

Resolves the given name to an overload list of namespaces.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Macro.resolveGlobalName "Permalink")def
```


Lean.Macro.resolveGlobalName (n : Lean.Name) :
  [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")Lean.Name [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod"))


Lean.Macro.resolveGlobalName
  (n : Lean.Name) :
  [Lean.MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM")
    ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")Lean.Name [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod"))


```

Resolves the given name to an overload list of global definitions. The `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` in each alternative is the deduced list of projections (which are ambiguous with name components).
Remark: it will not trigger actions associated with reserved names. Recall that Lean has reserved names. For example, a definition `foo` has a reserved name `foo.def` for theorem containing stating that `foo` is equal to its definition. The action associated with `foo.def` automatically proves the theorem. At the macro level, the name is resolved, but the action is not executed. The actions are executed by the elaborator when converting `Syntax` into `Expr`.
##  23.5.3. Quotation[🔗](find/?domain=Verso.Genre.Manual.section&name=quotation "Permalink")
_Quotation_ marks code for representation as data of type `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")`. Quoted code is parsed, but not elaborated—while it must be syntactically correct, it need not make sense. Quotation makes it much easier to programmatically generate code: rather than reverse-engineering the specific nesting of `[node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node")` values that Lean's parser would produce, the parser can be directly invoked to create them. This is also more robust in the face of refactoring of the grammar that may change the internals of the parse tree without affecting the user-visible concrete syntax. Quotation in Lean is surrounded by ``(` and `)`.
The syntactic category or parser being quoted may be indicated by placing its name after the opening backtick and parenthesis, followed by a vertical bar (`|`). As a special case, the name `tactic` may be used to parse either tactics or sequences of tactics. If no syntactic category or parser is provided, Lean attempts to parse the quotation both as a term and as a non-empty sequence of commands. Term quotations have higher priority than command quotations, so in cases of ambiguity, the interpretation as a term is chosen; this can be overridden by explicitly indicating that the quotation is of a command sequence.
Term vs Command Quotation Syntax
In the following example, the contents of the quotation could either be a function application or a sequence of commands. Both match the same region of the file, so the [local longest-match rule](Notations-and-Macros/Custom-Operators/#--tech-term-local-longest-match-rule) is not relevant. Term quotation has a higher priority than command quotation, so the quotation is interpreted as a term. Terms expect their [antiquotations](Notations-and-Macros/Macros/#--tech-term-antiquotations) to have type `[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `term` rather than `[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `command`.
`example (cmd1 cmd2 : [TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `command) : [MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") ([TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `command) :=   `($`Application type mismatch: The argument   cmd1 has type   [TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `command but is expected to have type   [TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `term in the application   cmd1.[raw](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.raw")`cmd1 $`Application type mismatch: The argument   cmd2 has type   [TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `command but is expected to have type   [TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `term in the application   cmd2.[raw](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.raw")`cmd2) `
The result is two type errors like the following:

```
Application type mismatch: The argument
  cmd1
has type
  [TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `command
but is expected to have type
  [TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `term
in the application
  cmd1.[raw](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.raw")
```

The type of the quotation (`[MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") ([TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `command)`) is not used to select a result because syntax priorities are applied prior to elaboration. In this case, specifying that the antiquotations are commands resolves the ambiguity because function application would require terms in these positions:
`example (cmd1 cmd2 : [TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `command) : [MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") ([TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `command) :=   `($cmd1:command $cmd2:command) `
Similarly, inserting a command into the quotation eliminates the possibility that it could be a term:
`example (cmd1 cmd2 : [TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `command) : [MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM") ([TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `command) :=   `($cmd1 $cmd2 [#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") "hello!") `
[Live ↪](javascript:openLiveLink\("PYBwpgdgBAMmCGEBQSwA94FsQBsxQAoBjTAEwEYoTSAmKALigBUBlATwgBd40oADIsEyZEpAJQMoAWXhEATsCmFWHbrwFCREcQwC8SKPwIASauXqDhoqKbI0Lm0WJTosufMTKVqdRiq48/JZaOowy8orK7AHqwU56Bka2FDY+UADEYABu8DhQAEQAFmA4OMAAhPliQA"\))
syntaxQuotations
Lean's syntax includes quotations for terms, commands, tactics, and sequences of tactics, as well as a general quotation syntax that allows any input that Lean can parse to be quoted. Term quotations have the highest priority, followed by tactic quotations, general quotations, and finally command quotations.

```
term ::=
      


Syntax quotation for terms. 


`(term)
    | `(command+)
    | `(tactic|tactic)
    | `(tactic|tactic;*)
    | `(p : identp:ident|Parse a p : identp here )
```

Rather than having type `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")`, quotations are monadic actions with type `m [Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")`. Quotation is monadic because it implements [hygiene](Notations-and-Macros/Macros/#--tech-term-hygienic) by adding [macro scopes](Notations-and-Macros/Macros/#--tech-term-macro-scopes) and pre-resolving identifiers, as described in [the section on hygiene](Notations-and-Macros/Macros/#macro-hygiene). The specific monad to be used is an implicit parameter to the quotation, and any monad for which there is an instance of the `MonadQuotation` type class is suitable. `MonadQuotation` extends `MonadRef`, which gives the quotation access to the source location of the syntax that the macro expander or elaborator is currently processing. `MonadQuotation` additionally includes the ability to add [macro scopes](Notations-and-Macros/Macros/#--tech-term-macro-scopes) to identifiers and use a fresh macro scope for a sub-task. Monads that support quotation include `[MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM")`, `TermElabM`, `CommandElabM`, and `TacticM`.
###  23.5.3.1. Quasiquotation[🔗](find/?domain=Verso.Genre.Manual.section&name=quasiquotation "Permalink")
_Quasiquotation_ is a form of quotation that may contain _antiquotations_ , which are regions of the quotation that are not quoted, but instead are expressions that are evaluated to yield syntax. A quasiquotation is essentially a template; the outer quoted region provides a fixed framework that always yields the same outer syntax, while the antiquotations yield the parts of the final syntax that vary. All quotations in Lean are quasiquotations, so no special syntax is needed to distinguish quasiquotations from other quotations. The quotation process does not add macro scopes to identifiers that are inserted via antiquotations, because these identifiers either come from another quotation (in which case they already have macro scopes) or from the macro's input (in which case they should not have macro scopes, because they are not introduced by the macro).
Basic antiquotations consist of a dollar sign (`$`) immediately followed by an identifier. This means that the value of the corresponding variable, which should be a syntax tree, is to be substituted into this position of the quoted syntax. Entire expressions may be used as antiquotations by wrapping them in parentheses.
Lean's parser assigns every antiquotation a syntax category based on what the parser expects at the given position. If the parser expects syntax category `c`, then the antiquotation's type is `[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") c`.
Some syntax categories can be matched by elements of other categories. For example, numeric and string literals are valid terms in addition to being their own syntax categories. Antiquotations may be annotated with the expected category by suffixing them with a colon and the category name, which causes the parser to validate that the annotated category is acceptable in the given position and construct any intermediate layers that are required in the parse tree.
syntaxAntiquotations

```
antiquot ::=
      $ident(:ident)?
    | $(term)(:ident)?
```

Whitespace is not permitted between the dollar sign ('$') that initiates an antiquotation and the identifier or parenthesized term that follows. Similarly, no whitespace is permitted around the colon that annotates the syntax category of the antiquotation.
Quasiquotation
Both forms of antiquotation are used in this example. Because natural numbers are not syntax, `[quote](Notations-and-Macros/Defining-New-Syntax/#Lean___Quote___mk "Documentation for Lean.Quote.quote")` is used to transform a number into syntax that represents it.
`[open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Lean [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") example [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadQuotation m] (x : [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : m [Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax") :=   `($x + $([quote](Notations-and-Macros/Defining-New-Syntax/#Lean___Quote___mk "Documentation for Lean.Quote.quote") (n + 2))) `
[Live ↪](javascript:openLiveLink\("PYBwpgdgBAMmCG0CWEBQYAe8C2IA2YUA2gLLATwAmU2AusWRZQIoCuwALvB0uTfQAoMUAFxQAKmABO2AJRQB0MQDlu8sdigBlAJ4QuwkQF5UUKAAMBAEmEBqKFYEBHdh0KKo9gEyzfQA"\))
Antiquotation Annotations
This example requires that `m` is a monad that can perform quotation.
`[variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax") {m : Type → Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadQuotation m] `
By default, the antiquotation `$e` is expected to be a term, because that's the syntactic category that's immediately expected as the second argument to addition.
`def ex1 (e) := show m _ from `(2 + $e) `[ex1](Notations-and-Macros/Macros/#ex1-_LPAR_in-Antiquotation-Annotations_RPAR_ "Definition of example") {m : Type → Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadQuotation m] (e : [TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `term) : m [(](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `term[)](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [ex1](Notations-and-Macros/Macros/#ex1-_LPAR_in-Antiquotation-Annotations_RPAR_ "Definition of example") `
```
[ex1](Notations-and-Macros/Macros/#ex1-_LPAR_in-Antiquotation-Annotations_RPAR_ "Definition of example") {m : Type → Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadQuotation m] (e : [TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `term) : m [(](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `term[)](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")
```

Annotating `$e` as a numeric literal succeeds, because numeric literals are also valid terms. The expected type of the parameter `e` changes to `TSyntax `num`.
`def ex2 (e) := show m _ from `(2 + $e:num) `[ex2](Notations-and-Macros/Macros/#ex2-_LPAR_in-Antiquotation-Annotations_RPAR_ "Definition of example") {m : Type → Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadQuotation m] (e : [TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `num) : m [(](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `term[)](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [ex2](Notations-and-Macros/Macros/#ex2-_LPAR_in-Antiquotation-Annotations_RPAR_ "Definition of example") `
```
[ex2](Notations-and-Macros/Macros/#ex2-_LPAR_in-Antiquotation-Annotations_RPAR_ "Definition of example") {m : Type → Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadQuotation m] (e : [TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `num) : m [(](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `term[)](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")
```

Spaces are not allowed between the dollar sign and the identifier.

```
def ex2 (e) := show m _ from `(2 +unexpected token '$'; expected '`(tactic|' or no space before spliced term $ e:num)
```

```
<example>:1:34-1:36: unexpected token '$'; expected '`(tactic|' or no space before spliced term
```

Spaces are also not allowed before the colon:

```
def ex2 (e) := show m _ from `(2 + $eunexpected token ':'; expected ')' :num)
```

```
<example>:1:37-1:39: unexpected token ':'; expected ')'
```

[Live ↪](javascript:openLiveLink\("PYBwpgdgBAMmCGEBQSBu8BOBLeAjANmFAN4C2UAXFACoCe4UgSYQ31gC+UA2gLLATwATKKQC6XXvwEBFAK7AALvHlY+wkSgFgAZlDAAPAIxQAFGACUlALxQAzgAtgAd2FQA+lC0Zg5AAbGATFAA1FAAJOZIAMQAxnZg0QDWuoYa2smBphYU1vZOLu6e3lB+gSHhFBAypGZRsfFJ+v5AA"\))
Expanding Quasiquotation
Printing the definition of `[f](Notations-and-Macros/Macros/#f-_LPAR_in-Expanding-Quasiquotation_RPAR_ "Definition of example")` demonstrates the expansion of a quasiquotation.
`[open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Lean [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") def f [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadQuotation m]     (x : [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : m [Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax") :=   `(fun k => $x + $([quote](Notations-and-Macros/Defining-New-Syntax/#Lean___Quote___mk "Documentation for Lean.Quote.quote") (n + 2)) + k) `def f : {m : Type → Type} → [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] → [Lean.MonadQuotation m] → [Lean.Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → m [Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax") := fun {m} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [Lean.MonadQuotation m] x n => do   let info ← Lean.MonadRef.mkInfoFromRefPos   let scp ← Lean.getCurrMacroScope   let quotCtx ← Lean.MonadQuotation.getContext   [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")       [{](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.mk")           [raw](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.raw") [:=](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.mk")             Syntax.node2 info `Lean.Parser.Term.fun ([Syntax.atom](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.atom") info "fun")               (Syntax.node4 info `Lean.Parser.Term.basicFun                 (Syntax.node1 info `null ([Syntax.ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.ident") info "k".[toRawSubstring'](Basic-Types/Strings/#String___toRawSubstring___ "Documentation for String.toRawSubstring'") (Lean.addMacroScope quotCtx `k scp) [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")))                 ([Syntax.node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node") info `null #[]) ([Syntax.atom](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.atom") info "=>")                 (Syntax.node3 info `«term_+_»                   (Syntax.node3 info `«term_+_» x.[raw](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.raw") ([Syntax.atom](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.atom") info "+") ([Lean.quote](Notations-and-Macros/Defining-New-Syntax/#Lean___Quote___mk "Documentation for Lean.Quote.quote") `term [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")).[raw](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.raw"))                   ([Syntax.atom](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.atom") info "+")                   ([Syntax.ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.ident") info "k".[toRawSubstring'](Basic-Types/Strings/#String___toRawSubstring___ "Documentation for String.toRawSubstring'") (Lean.addMacroScope quotCtx `k scp) [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")))) [}](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.mk").[raw](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.raw")`#print [f](Notations-and-Macros/Macros/#f-_LPAR_in-Expanding-Quasiquotation_RPAR_ "Definition of example") `
```
def f : {m : Type → Type} → [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] → [Lean.MonadQuotation m] → [Lean.Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → m [Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax") :=
fun {m} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [Lean.MonadQuotation m] x n => do
  let info ← Lean.MonadRef.mkInfoFromRefPos
  let scp ← Lean.getCurrMacroScope
  let quotCtx ← Lean.MonadQuotation.getContext
  [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")
      [{](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.mk")
          [raw](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.raw") [:=](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.mk")
            Syntax.node2 info `Lean.Parser.Term.fun ([Syntax.atom](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.atom") info "fun")
              (Syntax.node4 info `Lean.Parser.Term.basicFun
                (Syntax.node1 info `null ([Syntax.ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.ident") info "k".[toRawSubstring'](Basic-Types/Strings/#String___toRawSubstring___ "Documentation for String.toRawSubstring'") (Lean.addMacroScope quotCtx `k scp) [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")))
                ([Syntax.node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node") info `null #[]) ([Syntax.atom](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.atom") info "=>")
                (Syntax.node3 info `«term_+_»
                  (Syntax.node3 info `«term_+_» x.[raw](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.raw") ([Syntax.atom](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.atom") info "+") ([Lean.quote](Notations-and-Macros/Defining-New-Syntax/#Lean___Quote___mk "Documentation for Lean.Quote.quote") `term [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")).[raw](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.raw"))
                  ([Syntax.atom](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.atom") info "+")
                  ([Syntax.ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.ident") info "k".[toRawSubstring'](Basic-Types/Strings/#String___toRawSubstring___ "Documentation for String.toRawSubstring'") (Lean.addMacroScope quotCtx `k scp) [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")))) [}](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.mk").[raw](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.raw")
```

In this output, the quotation is a ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block. It begins by constructing the source information for the resulting syntax, obtained by querying the compiler about the current user syntax being processed. It then obtains the current macro scope and the name of the module being processed, because macro scopes are added with respect to a module to enable independent compilation and avoid the need for a global counter. It then constructs a node using helpers such as `Syntax.node1` and `Syntax.node2`, which create a `[Syntax.node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node")` with the indicated number of children. The macro scope is added to each identifier, and `[TSyntax.raw](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.raw")` is used to extract the contents of typed syntax wrappers. The antiquotations of `x` and `[quote](Notations-and-Macros/Defining-New-Syntax/#Lean___Quote___mk "Documentation for Lean.Quote.quote") (n + 2)` occur directly in the expansion, as parameters to `Syntax.node3`.
[Live ↪](javascript:openLiveLink\("PYBwpgdgBAMmCG0CWEBQATMAzKODaAssBPOlALYC6UhxpAigK7AAu8LSxFlqUfUACgAeUAFxQAKmABO5AJSDo4gHLsF48lADKATwhsRogLy8oAAwFZG0ANZQjAPigASEQGoXAgI7MWYRVAeAExyCh42cqgAxCDSKCy4QA"\))
###  23.5.3.2. Splices[🔗](find/?domain=Verso.Genre.Manual.section&name=splices "Permalink")
In addition to including other syntax via antiquotations, quasiquotations can include _splices_. Splices indicate that the elements of an array are to be inserted in order. The repeated elements may include separators, such as the commas between list or array elements. Splices may consist of an ordinary antiquotation with a _splice suffix_ , or they may be _extended splices_ that provide additional repeated structure.
Splice suffixes consist of either an asterisk or a valid atom followed by an asterisk (`*`). Suffixes may follow any identifier or term antiquotation. An antiquotation with the splice suffix `*` corresponds to a use of `many` or `many1`; both the `*` and `+` suffixes in syntax rules correspond to the `*` splice suffix. An antiquotation with a splice suffix that includes an atom prior to the asterisk corresponds to a use of `sepBy` or `sepBy1`. The splice suffix `?` corresponds to a use of `optional` or the `?` suffix in a syntax rule. Because `?` is a valid identifier character, identifiers must be parenthesized to use it as a suffix.
While there is overlap between repetition specifiers for syntax and antiquotation suffixes, they have distinct syntaxes. When defining syntax, the suffixes `*`, `+`, `,*`, `,+`, `,*,?`, and `,+,?` are built in to Lean. There is no shorter way to specify separators other than `,`. Antiquotation suffixes are either just `*` or whatever atom was provided to `sepBy` or `sepBy1` followed by `*`. The syntax repetitions `+` and `*` correspond to the splice suffix `*`; the repetitions `,*`, `,+`, `,*,?`, and `,+,?` correspond to `,*`. The optional suffix `?` in syntax and splices correspond with each other.  
|  Syntax Repetition  |  Splice Suffix  |  
| --- | --- |  
|  `+` `*`  |  `*`  |  
|  `,*` `,+` `,*,?` `,+,?`  |  `,*`  |  
|  `sepBy(_, "S")` `sepBy1(_, "S")`  |  `S*`  |  
|  `?`  |  `?`  |  
Suffixed Splices
This example requires that `m` is a monad that can perform quotation.
`[variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax") {m : Type → Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadQuotation m] `
By default, the antiquotation `$e` is expected to be an array of terms separated by commas, as is expected in the body of a list:
`def ex1 (xs) := show m _ from `(#[$xs,*]) `[ex1](Notations-and-Macros/Macros/#ex1-_LPAR_in-Suffixed-Splices_RPAR_ "Definition of example") {m : Type → Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadQuotation m] (xs : [Syntax.TSepArray](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___mk "Documentation for Lean.Syntax.TSepArray") `term ",") : m [(](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `term[)](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [ex1](Notations-and-Macros/Macros/#ex1-_LPAR_in-Suffixed-Splices_RPAR_ "Definition of example") `
```
[ex1](Notations-and-Macros/Macros/#ex1-_LPAR_in-Suffixed-Splices_RPAR_ "Definition of example") {m : Type → Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadQuotation m] (xs : [Syntax.TSepArray](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___mk "Documentation for Lean.Syntax.TSepArray") `term ",") : m [(](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `term[)](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")
```

However, Lean includes a collection of coercions between various representations of arrays that will automatically insert or remove separators, so an ordinary array of terms is also acceptable:
`def ex2 (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ([TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `term)) :=   show m _ from `(#[$xs,*]) `[ex2](Notations-and-Macros/Macros/#ex2-_LPAR_in-Suffixed-Splices_RPAR_ "Definition of example") {m : Type → Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadQuotation m] (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [(](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `term[)](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")) : m [(](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `term[)](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [ex2](Notations-and-Macros/Macros/#ex2-_LPAR_in-Suffixed-Splices_RPAR_ "Definition of example") `
```
[ex2](Notations-and-Macros/Macros/#ex2-_LPAR_in-Suffixed-Splices_RPAR_ "Definition of example") {m : Type → Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadQuotation m] (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [(](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `term[)](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")) : m [(](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `term[)](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")
```

Repetition annotations may also be used with term antiquotations and syntax category annotations. This example is in `CommandElabM` so the result can be conveniently logged.
`def ex3 (size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) := show CommandElabM _ from [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let mut nums : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := #[]   for i in [0:size] do     nums := nums.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") i   let stx ← `(#[$(nums.[map](Basic-Types/Arrays/#Array___map "Documentation for Array.map") ([Syntax.mkNumLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___mkNumLit "Documentation for Lean.Syntax.mkNumLit") ∘ toString)):num,*])   -- Using logInfo here causes the syntax to be rendered via   -- the pretty printer.   logInfo stx  `#[0, 1, 2, 3]`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [ex3](Notations-and-Macros/Macros/#ex3-_LPAR_in-Suffixed-Splices_RPAR_ "Definition of example") 4 `
```
#[0, 1, 2, 3]
```

[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAGQKYEMB2A6AogGxQIwChCIwk1FU0SyLl1s98MBhCEEdAEzgAo2O3XAQCyASmIA3FFGAEcSOAG8QcAFxwAKgE8ycQEmEW3UgC+cANoiIaFDxABdC1ZtcAigFcIMFDGDW4DsRcSABmcEgAHgCMfBEAzmLqALxwcQAWEADuAXAA+nAhUOxwAAa8AMTmACTxADQAVPYS5QDGaUgtANbh0UGhPQBMsXHqcACCUFAo2nyaAMraaN4RpTBIUCBiiWpJhHCpGdmq+YXFZZU1cQ1NhK3tXYN9YZEAzHxxwABeihoAcj7bFLpLJwAScNBcYT4ER5ApFVRcCB7OAKeAgdzwNDuEAjDQTKYzf7wHZwSr2ZEhaBwYDUijmAAMag+30ciOR+yxOOScE5cQwYHc6WpyNRqRgK0ACYSlCrVXi8jCcMB8BZLFARBWdX7YhDAeCADCI4DAIHMYLI0ABzLZqTnXCT7AC09rgAFUPhaURBzQBJNCUuDtKCKFooQVIEYwdqpRbLQ0QOD4RSBiHrJA8SRyZGOw2RsCBmAwGa54BLdYYEWen1+uLi4jlJDSHA9N4AFiAA"\))
Non-Comma Separators
The following unconventional syntax for lists separates numeric elements by either em dashes or double asterisks, rather than by commas.
`[syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") "⟦" sepBy1(num, " — ") "⟧": term [syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") "⟦" sepBy1(num, " ** ") "⟧": term `
This means that `—*` and `***` are valid splice suffixes between the `⟦` and `⟧` atoms. In the case of `***`, the first two asterisks are the atom in the syntax rule, while the third is the repetition suffix.
`[macro_rules](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules "Documentation for syntax")   | `(⟦$n:num—*⟧) => `(⟦$n***⟧)   | `(⟦$n:num***⟧) => `([$n,*]) ```[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ⟦1 — 2 — 3⟧ `
```
[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

[Live ↪](javascript:openLiveLink\("M4TwdgLghgHgBAIkGfkC7AKYAcBCICMAFGAK4C2ANInICgEiAlIoOfkCAXHBOgE6kBQoksRCjRZchEhSoAqKfSat2XXj1JQAxpwD2AfU7EANumA84cAD5wABgSQASMCwnUpjBgF4AfFZv2ZLuibm3nYOEn6ucJ7eANr25FIAugE8AMToAG5Q+nBIeDRwAEz5AMyMQA"\))
Optional Splices
The following syntax declaration optionally matches a term between two tokens. The parentheses around the nested `term` are needed because `term?` is a valid identifier.
`[syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") "⟨| " (term)? " |⟩": term `
The `?` splice suffix for a term expects an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")`:
`def mkStx [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadQuotation m]     (e : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")) : m [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term") :=   `(⟨| $(e)? |⟩) ```[mkStx](Notations-and-Macros/Macros/#mkStx-_LPAR_in-Optional-Splices_RPAR_ "Definition of example") {m : Type → Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadQuotation m] (e : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")) : m [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [mkStx](Notations-and-Macros/Macros/#mkStx-_LPAR_in-Optional-Splices_RPAR_ "Definition of example") `
```
[mkStx](Notations-and-Macros/Macros/#mkStx-_LPAR_in-Optional-Splices_RPAR_ "Definition of example") {m : Type → Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadQuotation m] (e : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")) : m [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")
```

Supplying `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` results in the optional term being present.
``⟨| 5 |⟩`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") logInfo (← [mkStx](Notations-and-Macros/Macros/#mkStx-_LPAR_in-Optional-Splices_RPAR_ "Definition of example") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ([quote](Notations-and-Macros/Defining-New-Syntax/#Lean___Quote___mk "Documentation for Lean.Quote.quote") 5))) `
```
⟨| 5 |⟩
```

Supplying `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` results in the optional term being absent.
``⟨| |⟩`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") logInfo (← [mkStx](Notations-and-Macros/Macros/#mkStx-_LPAR_in-Optional-Splices_RPAR_ "Definition of example") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) `
```
⟨| |⟩
```

[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAGQKYEMB2A6AogGxQIwChCIwk1FU1iBnATzRhQA84AiQC/IAfduAChhIoIAJQB+Xl0CX5GwBccQcOIATJADM4IANYBlGKwDaAWQhoUyzQF04x0+YCKAVwhMYwU1cJxv/JHHkA8mBuHgAqQqL+mnDhwv4AvF5wAAZ83HAAJHxI4nDSIsQAxADGABZIxVqauvpFSABuKDhwyhBwOBAA5gCSaGptfIAJhNV6rHw0ECB+fACOzoJwAKwiK3WNza3tXb39/MPao3BopjlAA"\))
###  23.5.3.3. Token Antiquotations[🔗](find/?domain=Verso.Genre.Manual.section&name=token-antiquotations "Permalink")
In addition to antiquotations of complete syntax, Lean features _token antiquotations_ which allow the source information of an atom to be replaced with the source information from some other syntax. The resulting synthetic source information is marked [canonical](Notations-and-Macros/Defining-New-Syntax/#--tech-term-canonical) so that it will be used for error messages, proof states, and other feedback. This is primarily useful to control the placement of error messages or other information that Lean reports to users. A token antiquotation does not allow an arbitrary atom to be inserted via evaluation. A token antiquotation consists of an atom (that is, a keyword)
syntaxToken Antiquotations
Token antiquotations replace the source information (of type `[SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo")`) on a token with the source information from some other syntax.

```
antiquot ::= ...
    | atom%$ident
```

##  23.5.4. Matching Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=quote-patterns "Permalink")
#  See Also
New syntax is defined using [syntax extensions](Notations-and-Macros/Defining-New-Syntax/#syntax-rules).
Quasiquotations can be used in pattern matching to recognize syntax that matches a template. Just as antiquotations in a quotation that's used as a term are regions that are treated as ordinary non-quoted expressions, antiquotations in patterns are regions that are treated as ordinary Lean patterns. Quote patterns are compiled differently from other patterns, so they can't be intermixed with non-quote patterns in a single ``Lean.Parser.Term.match : term`
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
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match) expression. Like ordinary quotations, quote patterns are first processed by Lean's parser. The parser's output is then compiled into code that determines whether there is a match. Syntax matching assumes that the syntax being matched was produced by Lean's parser, either via quotation or directly in user code, and uses this to omit some checks. For example, if nothing but a particular keyword can be present in a given position, the check may be omitted.
Syntax matches a quote pattern in the following cases: 

Atoms
    
Keyword atoms (such as ``termIfThenElse : term`
`if c then t else e` is notation for `ite c t e`, "if-then-else", which decides to return `t` or `e` depending on whether `c` is true or false. The explicit argument `c : Prop` does not have any actual computational content, but there is an additional `[Decidable c]` argument synthesized by typeclass inference which actually determines how to evaluate `c` to true or false. Write `if h : c then t else e` instead for a "dependent if-then-else" `dite`, which allows `t`/`e` to use the fact that `c` is true/false.
`[`if`](Terms/Conditionals/#termIfThenElse) or ``Lean.Parser.Term.match : term`
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
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match)) result in singleton nodes whose kind is `token.` followed by the atom. In many cases, it is not necessary to check for specific atom values because the grammar allows only a single keyword, and no checking will be performed. If the syntax of the term being matched requires the check, then the node kind is compared.
Literals, such as string or numeric literals, are compared via their underlying string representation. The pattern ``(0x15)` and the quotation ``(21)` do not match. 

Nodes
    
If both the pattern and the value being matched represent `[Syntax.node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node")`, there is a match when both have the same syntax kind, the same number of children, and each child pattern matches the corresponding child value. 

Identifiers
    
If both the pattern and the value being matched are identifiers, then their literal `Name` values are compared for equality modulo macro scopes. Identifiers that “look” the same match, and it does not matter if they refer to the same binding. This design choice allows quote pattern matching to be used in contexts that don't have access to a compile-time environment in which names can be compared by reference.
Because quotation pattern matching is based on the node kinds emitted by the parser, quotations that look identical may not match if they come from different syntax categories. If in doubt, including the syntax category in the quotation can help.
Variables bound by syntax pattern matches are of type `[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") k`, where `k` describes the potential syntax kinds. Variables in repetitions are of type `[TSyntaxArray](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntaxArray "Documentation for Lean.TSyntaxArray") k`, or `[TSepArray](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___mk "Documentation for Lean.Syntax.TSepArray") k sep` if the repetition is separated with the string `sep`. `[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")` is described in more detail in [the section on typed syntax](Notations-and-Macros/Defining-New-Syntax/#typed-syntax).
Syntax Pattern Matching
List comprehensions are a notation for writing lists that is inspired by standard set builder notation. A list comprehension consists of square brackets that contain a result term followed by some nubmer of _qualifiers_ ; each qualifier either introduces a variable from some other list or imposes a condition that must be satisfied. Qualifiers are nested: each new variable's value is evaluated for every prior value.
`syntax qbind := ident "←" term  syntax qpred := term  syntax qualifier := atomic([qbind](Notations-and-Macros/Macros/#qbind-_LPAR_in-Syntax-Pattern-Matching_RPAR_ "Definition of example")) <|> [qpred](Notations-and-Macros/Macros/#qpred-_LPAR_in-Syntax-Pattern-Matching_RPAR_ "Definition of example")  [syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") "[" term "|" [qualifier](Notations-and-Macros/Macros/#qualifier-_LPAR_in-Syntax-Pattern-Matching_RPAR_ "Definition of example"),* "]" : term `
List comprehensions can be desugared to a sequence of calls to `[List.flatMap](Basic-Types/Linked-Lists/#List___flatMap "Documentation for List.flatMap")`. Variable introductions are translated to a `[flatMap](Basic-Types/Linked-Lists/#List___flatMap "Documentation for List.flatMap")` on the variable's value expression, while predicates are translated to a conditional that returns one or zero values if the predicate is true or false. The body of the final `[flatMap](Basic-Types/Linked-Lists/#List___flatMap "Documentation for List.flatMap")` is the result term.
This desugaring can be implemented as a macro that uses quasiquotation patterns:
`[macro_rules](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules "Documentation for syntax")   | `(term|[$e | $qs,* ]) => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")     let init ← `([$e])     qs.[getElems](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___getElems "Documentation for Lean.Syntax.TSepArray.getElems").[foldrM](Basic-Types/Arrays/#Array___foldrM "Documentation for Array.foldrM") (β := [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")) (init := init) fun       | `([qualifier](Notations-and-Macros/Macros/#qualifier-_LPAR_in-Syntax-Pattern-Matching_RPAR_ "Definition of example")|$x ← $e'), r =>         `(($e' : List _) |>.flatMap fun $x => $r)       | `([qualifier](Notations-and-Macros/Macros/#qualifier-_LPAR_in-Syntax-Pattern-Matching_RPAR_ "Definition of example")|$e':term), r =>         `(([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") $e' [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [()] [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") []) |>.flatMap fun () => $r)       | other, _ =>         [Macro.throwErrorAt](Notations-and-Macros/Macros/#Lean___Macro___throwErrorAt "Documentation for Lean.Macro.throwErrorAt") other "Unknown qualifier" `
Initially, the sequence of qualifiers has type `[TSepArray](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___mk "Documentation for Lean.Syntax.TSepArray") `qualifier ","`, indicating that it represents a comma-separated sequence of qualifiers. `[TSepArray.getElems](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___getElems "Documentation for Lean.Syntax.TSepArray.getElems")` transforms it into a `[TSyntaxArray](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntaxArray "Documentation for Lean.TSyntaxArray") `qualifier`, which is an abbreviation for `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ([TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") `qualifier)`. This allows [generalized field notation](Terms/Function-Application/#--tech-term-generalized-field-notation) to be used to call `[Array.foldrM](Basic-Types/Arrays/#Array___foldrM "Documentation for Array.foldrM")`. The `term` annotation in the branch for predicates is required to prevent the matched value from having syntax kind ``qualifier`; one `[node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node")` must be unwrapped from the value.
List comprehensions behave as expected:
``[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")"2; true"[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") "2; false"[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") "4; true"[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") "4; false"[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [ s!"{x}; {y}" | x ← (1...5).[toList](Basic-Types/Ranges/#Std___Rco___toList "Documentation for Std.Rco.toList"), x % 2 = 0, y ← [[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true"), [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")] ] `
```
[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")"2; true"[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") "2; false"[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") "4; true"[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") "4; false"[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

[Live ↪](javascript:openLiveLink\("PYBwpgdgBAMmCG0DKBPCAXeAPAUDgzmpllAI4BGAlhACZQBcAvFJTZOlAESAJhJ1OmABOAWzyEM2MiEFg6TfkNEEik0gFd4AG0oAzSkIbN46YMMoBjABQVqNAJRQAPAB8AfFJk0xKkpwDafAIiXM586lq6+oIANABUXAC6fPQKInjC8OaCwAD6gmqaYPg4UFDOUAAGlkHCzn4AJGBlUPWk+HFQCQ6M7jTAJaVQhRzUlBzclZYNYF0DpW0AdADmYOgAooXC+As6wJo0ggCyUJaATcCGUAAqig6Woxzy9w46ahBzg+VV4dp6Qs71JAmjQA5HZolBBFAeu9BpNLCCGLBKPgODkHG4dppjId4CAoC9oACoe56oI7DDml8ND8ov8wMD6DUwRDiRTSlU7joWvT+AALSBQPyWOwJKBgTT4Jp+LplVyY7G4/GvE7dElkinlYDofkxKA5Vmw2E4rLABba7IAdzWgmyggAghwtTquABVCAAawgwAt0G+kSEnDwAGIwAA3LSCqD4ACEnAA3lgAL4AbigcZQib4zgGgJOAEYFoWAKx2M3AGDI9DRHNQACkUAATFCoAAGaulFBQCZ+dD5MDgnRaSUJHAJIA"\))
##  23.5.5. Defining Macros[🔗](find/?domain=Verso.Genre.Manual.section&name=defining-macros "Permalink")
There are two primary ways to define macros: the ``Lean.Parser.Command.macro_rules : command``[`macro_rules`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules) command and the ``Lean.Parser.Command.macro : command``[`macro`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro) command. The ``Lean.Parser.Command.macro_rules : command``[`macro_rules`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules) command associates a macro with existing syntax, while the ``Lean.Parser.Command.macro : command``[`macro`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro) command simultaneously defines new syntax and a macro that translates it to existing syntax. The ``Lean.Parser.Command.macro : command``[`macro`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro) command can be seen as a generalization of ``Lean.Parser.Command.notation : command``[`notation`](Notations-and-Macros/Notations/#Lean___Parser___Command___notation) that allows the expansion to be generated programmatically, rather than simply by substitution.
###  23.5.5.1. The `macro_rules` Command[🔗](find/?domain=Verso.Genre.Manual.section&name=macro_rules "Permalink")
syntaxRule-Based Macros With `macro_rules`
The ``Lean.Parser.Command.macro_rules : command``[`macro_rules`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules) command takes a sequence of rewrite rules, specified as syntax pattern matches, and adds each as a macro. The rules are attempted in order, before previously-defined macros, and later macro definitions may add further macro rules.

```
command ::= ...
    | [
A docComment parses a "documentation comment" like /-- foo -/. This is not treated like
a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure.
At parse time, docComment checks the value of the doc.verso option. If it is true, the contents
are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use
plainDocComment to always treat the contents as plain text.
A plain text doc comment node contains a /-- atom and then the remainder of the comment, foo -/
in this example. Use TSyntax.getDocString to extract the body text from a doc string syntax node.
A Verso comment node contains the /-- atom, the document's syntax tree, and a closing -/ atom.
docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)?
      ([@[](Attributes/#Lean___Parser___Term___attributes-next)[attrInstance](Attributes/#Lean___Parser___Term___attrInstance-next),*[]](Attributes/#Lean___Parser___Term___attributes-next))?
      


attrKind matches ("scoped" <|> "local")?, used before an attribute like @[local simp]. 


attrKind macro_rules ((kind := ident))?
        (| 


Syntax quotation for terms. 


`((p : identp:ident|)?Suitable syntax for p : identp ) => term)*
```

The patterns in the macros must be quotation patterns. They may match syntax from any syntax category, but a given pattern can only ever match a single syntax kind. If no category or parser is specified for the quotation, then it may match terms or (sequences of) commands, but never both. In case of ambiguity, the term parser is chosen.
Internally, macros are tracked in a table that maps each [syntax kind](Notations-and-Macros/Defining-New-Syntax/#--tech-term-syntax-kind) to its macros. The ``Lean.Parser.Command.macro_rules : command``[`macro_rules`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules) command may be explicitly annotated with a syntax kind.
If a syntax kind is explicitly provided, the macro definition checks that each quotation pattern has that kind. If the parse result for the quotation was a [choice node](Elaboration-and-Compilation/#--tech-term-choice-node) (that is, if the parse was ambiguous), then the pattern is duplicated once for each alternative with the specified kind. It is an error if none of the alternatives have the specified kind.
If no kind is provided explicitly, then the kind determined by the parser is used for each pattern. The patterns are not required to all have the same syntax kind; macros are defined for each syntax kind used by at least one of the patterns. It is an error if the parse result for a quotation pattern was a [choice node](Elaboration-and-Compilation/#--tech-term-choice-node) (that is, if the parse was ambiguous).
The documentation comment associated with ``Lean.Parser.Command.macro_rules : command``[`macro_rules`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules) is displayed to users if the syntax itself has no documentation comment. Otherwise, the documentation comment for the syntax itself is shown.
As with [notations](Notations-and-Macros/Notations/#notations) and [operators](Notations-and-Macros/Custom-Operators/#operators), macro rules may be declared `scoped` or `local`. Scoped macros are only active when the current namespace is open, and local macro rules are only active in the current [section scope](Namespaces-and-Sections/#--tech-term-section-scope).
Idiom Brackets
Idiom brackets are an alternative syntax for working with applicative functors. If the idiom brackets contain a function application, then the function is wrapped in `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` and applied to each argument using `<*>`. Lean does not support idiom brackets by default, but they can be defined using a macro.
`[syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") (name := idiom) "⟦" (term:[arg](Notations-and-Macros/Precedence/#precArg "Documentation for syntax"))+ "⟧" : term  [macro_rules](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules "Documentation for syntax")   | `(⟦$f $args*⟧) => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")     let mut out ← `(pure $f)     for arg in args do       out ← `($out <*> $arg)     return out `
This new syntax can be used immediately.
`def addFirstThird [[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") α] (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α :=   ⟦[Add.add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add.add") xs[0]? xs[2]?⟧ ```[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [addFirstThird](Notations-and-Macros/Macros/#addFirstThird-_LPAR_in-Idiom-Brackets_RPAR_ "Definition of example") (α := [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) [] `
```
[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")
```
``[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [addFirstThird](Notations-and-Macros/Macros/#addFirstThird-_LPAR_in-Idiom-Brackets_RPAR_ "Definition of example") [1] `
```
[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")
```
``[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 4`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [addFirstThird](Notations-and-Macros/Macros/#addFirstThird-_LPAR_in-Idiom-Brackets_RPAR_ "Definition of example") [1,2,3,4] `
```
[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 4
```

[Live ↪](javascript:openLiveLink\("M4TwdgLghgHgBACjFAtgUzgLgLxwJYAmeA9igJRwBEgZ+SWIRoBOKmUjA5mQNRWDn5HZjgNmAKBEooAY0bEA+owCuAGzTARcOAB84AAwTUAJADM4Btu2AAqXhWwA+OAWLqNcFRDgoFH4t7iAEwl0EAAcFRgxjMhcNI2JGOHN8MASOYEdnV1dfD0C9A2y4AB5LBzMOKMzwiDDk7LECNBMoAgIAMTxGYAgAFQALDoI4AG0AQRa4QEbgAF1EGDTBABk8LsmKQQB5YIgSZImsbBdqMYIAOmbBuaGABimAfjhLgCY73jEAYjQANyglBJb2zo9fqMQYIPY4OAAOSgEAoQym7y+Pz+bQ6XT6A2GAEYESIPt9fucAejgYMhliADSPCkAZgpABYpkA"\))
Scoped Macros
Scoped macro rules are active only in their namespace. When the namespace `ConfusingNumbers` is open, numeric literals will be assigned an incorrect meaning.
`[namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") ConfusingNumbers `
The following macro recognizes terms that are odd numeric literals, and replaces them with double their value. If it unconditionally replaced them with double their value, then macro expansion would become an infinite loop because the same rule would always match the output.
`scoped [macro_rules](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules "Documentation for syntax")   | `($n:num) => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")     if n.[getNat](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___getNat "Documentation for Lean.TSyntax.getNat") % 2 = 0 then [Lean.Macro.throwUnsupported](Notations-and-Macros/Macros/#Lean___Macro___throwUnsupported "Documentation for Lean.Macro.throwUnsupported")     let n' := (n.[getNat](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___getNat "Documentation for Lean.TSyntax.getNat") * 2)     `($([Syntax.mkNumLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___mkNumLit "Documentation for Lean.Syntax.mkNumLit") (info := n.[raw](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.raw").getHeadInfo) (toString n'))) `
Once the namespace ends, the macro is no longer used.
`end ConfusingNumbers `
Without opening the namespace, numeric literals function in the usual way.
``[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")3[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") 4[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (3, 4) `
```
[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")3[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") 4[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")
```

When the namespace is open, the macro replaces `3` with `6`.
`[open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") ConfusingNumbers  `[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")6[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") 4[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (3, 4) `
```
[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")6[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") 4[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")
```

It is not typically useful to change the interpretation of numeric or other literals in macros. However, scoped macros can be very useful when adding new rules to extensible tactics such as `[trivial](Tactic-Proofs/Tactic-Reference/#trivial "Documentation for tactic")` that work well with the contents of the namespaces but should not always be used.
[Live ↪](javascript:openLiveLink\("PYBwpgdgBAMmCGEBQSLwLZgM4ngYzCgGFgIAzAVywEsIBzAOQvQCMwAnLFLPUMAEyjp87YAH12FADbYkUKAB8oAAwAUAEggAuCMwCUUALwA+KP2Bz5UamSgQAdHTAAXBvGdQApFABMRqAAMUM4AFpCwCA4AsiLA9qGiAO4AqhBYFCAgwOzOApbyMh4QAORQWoZQqg5Oru5QAFS+evkqGqoAygCeEM7wAB726ADWTOgw1B6qtGTAZRUO7PCJji4AEgj8AJLkwAaqzsDtzuy0dHbFepcokIIk5FSno2ycKADEYABu8FKVAMwANFAACzNJB8aB3Sg0ehPDhcJDvL4/VQA4F6IA"\))
Behind the scenes, a ``Lean.Parser.Command.macro_rules : command``[`macro_rules`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules) command generates one macro function for each syntax kind that is matched in its quote patterns. This function has a default case that throws the `[unsupportedSyntax](Notations-and-Macros/Macros/#Lean___Macro___Exception___unsupportedSyntax "Documentation for Lean.Macro.Exception.unsupportedSyntax")` exception, so further macros may be attempted.
A single ``Lean.Parser.Command.macro_rules : command``[`macro_rules`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules) command with two rules is not always equivalent to two separate single-match commands. First, the rules in a ``Lean.Parser.Command.macro_rules : command``[`macro_rules`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules) are tried from top to bottom, but recently-declared macros are attempted first, so the order would need to be reversed. Additionally, if an earlier rule in the macro throws the `[unsupportedSyntax](Notations-and-Macros/Macros/#Lean___Macro___Exception___unsupportedSyntax "Documentation for Lean.Macro.Exception.unsupportedSyntax")` exception, then the later rules are not tried; if they were instead in separate ``Lean.Parser.Command.macro_rules : command``[`macro_rules`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules) commands, then they would be attempted.
One vs. Two Sets of Macro Rules
The `arbitrary!` macro is intended to expand to some arbitrarily-determined value of a given type.
`[syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") (name := arbitrary!) "arbitrary! " term:[arg](Notations-and-Macros/Precedence/#precArg "Documentation for syntax") : term ``[macro_rules](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules "Documentation for syntax")   | `(arbitrary! ()) => `(())   | `(arbitrary! Nat) => `(42)   | `(arbitrary! ($t1 × $t2)) => `((arbitrary! $t1, arbitrary! $t2))   | `(arbitrary! Nat) => `(0) `
Users may extend it by defining further sets of macro rules, such as this rule for `[Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")` that fails:
`[macro_rules](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules "Documentation for syntax")   | `(arbitrary! Empty) => [throwUnsupported](Notations-and-Macros/Macros/#Lean___Macro___throwUnsupported "Documentation for Lean.Macro.throwUnsupported") ```[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")42[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") 42[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") arbitrary! (Nat × Nat) `
```
[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")42[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") 42[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")
```

If all of the macro rules had been defined as individual cases, then the result would have instead used the later case for `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`. This is because the rules in a single ``Lean.Parser.Command.macro_rules : command``[`macro_rules`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules) command are checked from top to bottom, but more recently-defined ``Lean.Parser.Command.macro_rules : command``[`macro_rules`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules) commands take precedence over earlier ones.
`[macro_rules](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules "Documentation for syntax")   | `(arbitrary! ()) =>     `(()) [macro_rules](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules "Documentation for syntax")   | `(arbitrary! Nat) =>     `(42) [macro_rules](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules "Documentation for syntax")   | `(arbitrary! ($t1 × $t2)) =>     `((arbitrary! $t1, arbitrary! $t2)) [macro_rules](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules "Documentation for syntax")   | `(arbitrary! Nat) =>     `(0) [macro_rules](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules "Documentation for syntax")   | `(arbitrary! Empty) =>     [throwUnsupported](Notations-and-Macros/Macros/#Lean___Macro___throwUnsupported "Documentation for Lean.Macro.throwUnsupported") ```[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")0[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") 0[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") arbitrary! (Nat × Nat) `
```
[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")0[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") 0[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")
```

Additionally, if any rule throws the `[unsupportedSyntax](Notations-and-Macros/Macros/#Lean___Macro___Exception___unsupportedSyntax "Documentation for Lean.Macro.Exception.unsupportedSyntax")` exception, no further rules in that command are checked.
`[macro_rules](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules "Documentation for syntax")   | `(arbitrary! (List Nat)) => [throwUnsupported](Notations-and-Macros/Macros/#Lean___Macro___throwUnsupported "Documentation for Lean.Macro.throwUnsupported")   | `(arbitrary! (List $_)) => `([])  [macro_rules](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules "Documentation for syntax")   | `(arbitrary! (Array Nat)) => `(#[42]) [macro_rules](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules "Documentation for syntax")   | `(arbitrary! (Array $_)) => [throwUnsupported](Notations-and-Macros/Macros/#Lean___Macro___throwUnsupported "Documentation for Lean.Macro.throwUnsupported") `
The case for `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` fails to elaborate, because macro expansion did not translate the ``arbitrary! : term```arbitrary!` syntax into something supported by the elaborator.
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") `elaboration function for `arbitrary!` has not been implemented   arbitrary! (List Nat)`arbitrary! (List Nat) `
```
elaboration function for `arbitrary!` has not been implemented
  arbitrary! (List Nat)
```

The case for `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` succeeds, because the first set of macro rules are attempted after the second throws the exception.
``[#[](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")42[]](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") arbitrary! (Array Nat) `
```
[#[](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")42[]](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")
```

[Live ↪](javascript:openLiveLink\("PYBwpgdgBAMmCGEB0BZeBjATsAUDgzgJ4QAu8AHlABQTwC2YUAXALxTyYBGAliZh4QCEASigAiDjz4DB4qCTCY6TDgHNm8xXTx0M2APqYArgBsw+HFCgAfKAAMqk3v0xDqMbvhJQAcvBLCoiwAfPIAFtgA7gCqEPhGICDAmAoAJpY29o5czjLunt4AJPqBUCFZANoAusI6esCGpuYZtg5O0q6yVACCmPyEvv6l5Q4AxBUALABMNTi6WA3GZhZWrdlSLm49ffADxcOhJBHAMXEJSSlg6TijYABu8CbsOR1bvf2DAUA"\))
###  23.5.5.2. The `macro` Command[🔗](find/?domain=Verso.Genre.Manual.section&name=macro-command "Permalink")
The ``Lean.Parser.Command.macro : command``[`macro`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro) command simultaneously defines a new [syntax rule](Notations-and-Macros/Defining-New-Syntax/#--tech-term-syntax-rules) and associates it with a [macro](Notations-and-Macros/Macros/#--tech-term-Macros). Unlike ``Lean.Parser.Command.notation : command``[`notation`](Notations-and-Macros/Notations/#Lean___Parser___Command___notation), which can define only new term syntax and in which the expansion is a term into which the parameters are to be substituted, the ``Lean.Parser.Command.macro : command``[`macro`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro) command may define syntax in any [syntax category](Notations-and-Macros/Defining-New-Syntax/#--tech-term-syntax-categories) and it may use arbitrary code in the `[MacroM](Notations-and-Macros/Macros/#Lean___MacroM "Documentation for Lean.MacroM")` monad to generate the expansion. Because macros are so much more flexible than notations, Lean cannot automatically generate an unexpander; this means that new syntax implemented via the ``Lean.Parser.Command.macro : command``[`macro`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro) command is available for use in _input_ to Lean, but Lean's output does not use it without further work.
syntaxMacro Declarations

```
command ::= ...
    | [
A docComment parses a "documentation comment" like /-- foo -/. This is not treated like
a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure.
At parse time, docComment checks the value of the doc.verso option. If it is true, the contents
are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use
plainDocComment to always treat the contents as plain text.
A plain text doc comment node contains a /-- atom and then the remainder of the comment, foo -/
in this example. Use TSyntax.getDocString to extract the body text from a doc string syntax node.
A Verso comment node contains the /-- atom, the document's syntax tree, and a closing -/ atom.
docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)?
      ([@[](Attributes/#Lean___Parser___Term___attributes-next)[attrInstance](Attributes/#Lean___Parser___Term___attrInstance-next),*[]](Attributes/#Lean___Parser___Term___attributes-next))?
      


attrKind matches ("scoped" <|> "local")?, used before an attribute like @[local simp]. 


attrKind macro(:prec)? ((name := ident))? ((priority := prio))? macroArg* : ident =>
        macroRhs
```

syntaxMacro Arguments
A macro's arguments are either syntax items (as used in the ``Lean.Parser.Command.syntax : command``[`syntax`](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax) command) or syntax items with attached names.

```
macroArg ::=
    stx
```

```
macroArg ::= ...
    | ident:stx
```

In the expansion, the names that are attached to syntax items are bound; they have type `[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")` for the appropriate syntax kinds. If the syntax matched by the parser does not have a defined kind (e.g. because the name is applied to a complex specification), then the type is `[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") Name.anonymous`.
The documentation comment is associated with the new syntax, and the attribute kind (none, `local`, or `scoped`) governs the visibility of the macro just as it does for notations: `scoped` macros are available in the namespace in which they are defined or in any [section scope](Namespaces-and-Sections/#--tech-term-section-scope) that opens that namespace, while `local` macros are available only in the local section scope.
Behind the scenes, the ``Lean.Parser.Command.macro : command``[`macro`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro) command is itself implemented by a macro that expands it to a ``Lean.Parser.Command.syntax : command``[`syntax`](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax) command and a ``Lean.Parser.Command.macro_rules : command``[`macro_rules`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules) command. Any attributes applied to the macro command are applied to the syntax definition, but not to the ``Lean.Parser.Command.macro_rules : command``[`macro_rules`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules) command.
###  23.5.5.3. The Macro Attribute[🔗](find/?domain=Verso.Genre.Manual.section&name=macro-attribute "Permalink")
[Macros](Notations-and-Macros/Macros/#--tech-term-Macros) can be manually added to a syntax kind using the ``Lean.Parser.Attr.macro : attr``[`macro`](Notations-and-Macros/Macros/#Lean___Parser___Attr___macro) attribute. This low-level means of specifying macros is typically not useful, except as a result of code generation by macros that themselves generate macro definitions.
attributeThe `macro` Attribute
The ``Lean.Parser.Attr.macro : attr``[`macro`](Notations-and-Macros/Macros/#Lean___Parser___Attr___macro) attribute specifies that a function is to be considered a [macro](Notations-and-Macros/Macros/#--tech-term-Macros) for the specified syntax kind.

```
attr ::= ...
    | macro ident
```

The Macro Attribute
`/-- Generate a list based on N syntactic copies of a term -/ [syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") (name := rep) "[" num " !!! " term "]" : term  @[[macro](Notations-and-Macros/Macros/#Lean___Parser___Attr___macro "Documentation for syntax") [rep](Notations-and-Macros/Macros/#rep-_LPAR_in-The-Macro-Attribute_RPAR_ "Definition of example")] def expandRep : Macro   | `([ $n:num !!! $e:term]) =>     let e' := [Array.replicate](Basic-Types/Arrays/#Array___replicate "Documentation for Array.replicate") n.[getNat](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___getNat "Documentation for Lean.TSyntax.getNat") e     `([$e',*])   | _ =>     [throwUnsupported](Notations-and-Macros/Macros/#Lean___Macro___throwUnsupported "Documentation for Lean.Macro.throwUnsupported") `
Evaluating this new expression demonstrates that the macro is present.
``[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")"hello"[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") "hello"[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") "hello"[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [3 !!! "hello"] `
```
[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")"hello"[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") "hello"[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") "hello"[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

[Live ↪](javascript:openLiveLink\("PYBwpgdgBAMmCG0Cy8DGAnYAoLB6AtPlAOKRjrwAuYU8UANgJYDOlUARvM2ACZTDQAclGYBPCJTSVGqKKlCMwzfgDNaUaugC2UfLixiJ8AB5QAFBHhaaALgC8UdGBABKKACIA2u6gQArjo+AIQhHhrkgQC6Pjbh2jgAAp5aaJiOzpFYPGBqYMYgiDwASs5QsSgY2FBQAD5QAAZmnlAAJBA2/johQa1gNppakW52AHxY1dX0YGxgAORlDgCC6BSiAHROIEyoVDQQawDm04JUUGDjE42eLXMANABUQxd1APpQoxfVlAAWmADuAFUIMw/CAQMB0NQeDgAMRgABu8HoUE8AGYoN0PN8wPR6MB3JEgA"\))
[←23.4. Defining New Syntax](Notations-and-Macros/Defining-New-Syntax/#syntax-ext "23.4. Defining New Syntax")[23.6. Elaborators→](Notations-and-Macros/Elaborators/#elaborators "23.6. Elaborators")

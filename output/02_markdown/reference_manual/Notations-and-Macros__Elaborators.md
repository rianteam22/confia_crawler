[←23.5. Macros](Notations-and-Macros/Macros/#macros "23.5. Macros")[23.7. Extending Lean's Output→](Notations-and-Macros/Extending-Lean___s-Output/#unexpand-and-delab "23.7. Extending Lean's Output")
#  23.6. Elaborators[🔗](find/?domain=Verso.Genre.Manual.section&name=elaborators "Permalink")
#  See Also
  * Elaborators process [new syntax extensions](Notations-and-Macros/Defining-New-Syntax/#syntax-ext).
  * [Quotation patterns](Notations-and-Macros/Macros/#quote-patterns) are the most typical way to destructure syntax.


While macros allow Lean to be extended by translating new syntax into existing syntax, _elaborators_ allow the new syntax to be processed directly. Elaborators have access to everything that Lean itself uses to implement each feature of the language. Defining a new elaborator allows a language extension to be just as powerful as any built-in feature of Lean.
Elaborators come in two varieties:
  * _Command elaborators_ are used to add new commands to Lean. Commands are implemented as side effects: they may add new constants to the global environment, extend compile-time tables such as the one that tracks [instances](Type-Classes/#--tech-term-instances), they can provide feedback in the form of information, warnings, or errors, and they have full access to the `[IO](IO/Logical-Model/#IO "Documentation for IO")` monad. Command elaborators are associated with the [syntax kinds](Elaboration-and-Compilation/#--tech-term-kind) that they can handle.
  * _Term elaborators_ are used to implement new terms by translating the syntax into Lean's core type theory. They can do everything that command elaborators can do, and they additionally have access to the local context in which the term is being elaborated. Term elaborators can look up bound variables, bind new variables, unify two terms, and much more. A term elaborator must return a value of type `Lean.Expr`, which is the AST of the core type theory.


This section provides an overview and a few examples of elaborators. Because Lean's own elaborator uses the same tools, the source code of the elaborator is a good source of further examples. Just like macros, multiple elaborators may be associated with a syntax kind; they are tried in order, and elaborators may delegate to the next elaborator in the table by throwing the `[unsupportedSyntax](Notations-and-Macros/Macros/#Lean___Macro___Exception___unsupportedSyntax "Documentation for Lean.Macro.Exception.unsupportedSyntax")` exception.
syntaxElaboration Rules
The ``Lean.Parser.Command.elab_rules : command``[`elab_rules`](Notations-and-Macros/Elaborators/#Lean___Parser___Command___elab_rules) command takes a sequence of elaboration rules, specified as syntax pattern matches, and adds each as an elaborator. The rules are attempted in order, before previously-defined elaborators, and later elaborators may add further options.

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


attrKind elab_rules ((kind := ident))? (: ident)? (<= ident)?
        (| 


Syntax quotation for terms. 


`((p : identp:ident|)?Suitable syntax for p : identp ) => term)*
```

Commands, terms, and tactics each maintain a table that maps syntax kinds to elaborators. The syntax category for which the elaborator should be used is specified after the colon, and must be `term`, `command`, or `tactic`. The ``Lean.Parser.Command.elab_rules : command``[`<=`](Notations-and-Macros/Elaborators/#Lean___Parser___Command___elab_rules) binds the provided identifier to the current expected type in the context in which a term is being elaborated; it may only be used for term elaborators, and if present, then `term` is implied as the syntax category.
attributeElaborator Attribute
Elaborators can be directly associated with syntax kinds by applying the appropriate attributes. Each takes the name of a syntax kind and associates the definition with the kind.

```
attr ::= ...
    | term_elab (prio
       | ident)
```

```
attr ::= ...
    | command_elab (prio
       | ident)
```

```
attr ::= ...
    | tactic (prio
       | ident)
```

##  23.6.1. Command Elaborators[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Notations-and-Macros--Elaborators--Command-Elaborators "Permalink")
A command elaborator has type `CommandElab`, which is an abbreviation for `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax") → CommandElabM [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")`. Command elaborators may be implicitly defined using ``Lean.Parser.Command.elab_rules : command``[`elab_rules`](Notations-and-Macros/Elaborators/#Lean___Parser___Command___elab_rules), or explicitly by defining a function and applying the `command_elab` attribute.
Querying the Environment
A command elaborator can be used to query the environment to discover how many constants have a given name. This example uses `getEnv` from the `MonadEnv` class to get the current environment. `Environment.constants` yields a mapping from names to information about them (e.g. their type and whether they are a definition, [inductive type](The-Type-System/Inductive-Types/#--tech-term-Inductive-types) declaration, etc). `logInfoAt` allows informational output to be associated with syntax from the original program, and a [token antiquotation](Notations-and-Macros/Macros/#--tech-term-token-antiquotations) is used to implement the Lean convention that output from interactive commands is associated with their keyword.
`[syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") "#count_constants " ident : command  [elab_rules](Notations-and-Macros/Elaborators/#Lean___Parser___Command___elab_rules "Documentation for syntax") : command   | `(#count_constants%$tok $x) => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")     let pattern := x.[getId](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___getId "Documentation for Lean.TSyntax.getId")     let env ← getEnv     let mut count := 0     for (y, _) in env.constants do       if pattern.isSuffixOf y then         count := count + 1     logInfoAt tok m!"Found {count} instances of '{pattern}'" ``def interestingName := 55 def NS.interestingName := "Another one"  `Found 2 instances of 'interestingName'`#count_constants interestingName `
```
Found 2 instances of 'interestingName'
```

[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAGQKYEMB2A6AogGxQIwChCIwk1FU1iBnATzRhQA84AiAYgGMIBXRgPo80NJoxrs4wACbl4ALjg8QIdNOJI8+AVF44kExctVp1cOAB84AAwAU3PoOGj0MGgFIAJDAgBrOJ7MAJRwALwAfHDSEITm5vrwYCgwMEhQFPKhcMwYAOZIMACSZnEJcOQAbnCACYRw+TBYaBWxpQVwILzwPPwKWQAMLeYAZtBwtnQANHACIcAUlRjOYm5RMXFxwENwSSlpmMA0AMq8Q0PAzADyW3RwMAAW5IPrSo69Lz1wANRwAIxPOBBcoU0CMAILwHz+EAAQjYADFHNI4ABvbqMAC+UhEYi4BjgEC2AHJkTtUul0YS2MRZFs5mSDDA5rkAHIoEBIOCZOAAVm5hBpcGZhwwdLSDKZrPZnKybFBaAg9zS+LQSCphAcPSEEGxrgkoqg4rQLLZSCAA"\))
##  23.6.2. Term Elaborators[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Notations-and-Macros--Elaborators--Term-Elaborators "Permalink")
A term elaborator has type `TermElab`, which is an abbreviation for `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax") → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") Expr → TermElabM Expr`. The optional `Expr` parameter is the type expected for the term being elaborated, which is `none` if no type is yet known. Like command elaborators, term elaborators may be implicitly defined using ``Lean.Parser.Command.elab_rules : command``[`elab_rules`](Notations-and-Macros/Elaborators/#Lean___Parser___Command___elab_rules), or explicitly by defining a function and applying the `term_elab` attribute.
Avoiding a Type
This examples demonstrates an elaborator for syntax that is the opposite of a type ascription. The provided term may have any type _other_ than the one indicated, and metavariables are solved pessimistically. In this example, `elabType` invokes the term elaborator and then ensures that the resulting term is a type. `Meta.inferType` infers a type for a term, and `Meta.isDefEq` attempts to make two terms [definitionally equal](The-Type-System/#--tech-term-definitional-equality) by unification, returning `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if it succeeds.
`[syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") (name := notType) "(" term  " !: " term ")" : term  @[term_elab [notType](Notations-and-Macros/Elaborators/#notType-_LPAR_in-Avoiding-a-Type_RPAR_ "Definition of example")] def elabNotType : TermElab := fun stx _ => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let `(($tm:term !: $ty:term)) := stx     | throwUnsupportedSyntax   let unexpected ← elabType ty   let e ← elabTerm tm [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")   let eTy ← Meta.inferType e   if (← Meta.isDefEq eTy unexpected) then     throwErrorAt tm m!"Got unwanted type {eTy}"   else [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") e `
If the type position does not contain a type, then `elabType` throws an error:
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ([1, 2, 3] !: `type expected, got   ("not a type" : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))`"not a type") `
```
type expected, got
  ("not a type" : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
```

If the term's type is definitely not equal to the provided type, then elaboration succeeds:
``[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ([1, 2, 3] !: [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) `
```
[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

If the types match, an error is thrown:
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (`Got unwanted type [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`5 !: [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) `
```
Got unwanted type [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

The type equality check may fill in missing information, so `sorry` (which may have any type) is also rejected:
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (`Got unwanted type [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`sorry !: [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) `
```
Got unwanted type [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAGQKYEMB2A6AogGxQIwChCIwk1FULcC4AVJKEYgZwE80YUAPOACjQoQSOAC4AvHDQQYdNmQCUcAER9lcGIxBwVcAISjdmpioXrDx5oQACAbUsB9JHnxSZcsgF1CAEyQAzOGcCADl3eRFDBiYaVwk4fwBXChYYXgc4cQA+OB8IQh0cJHgAAz4+ABIYEFFLfUMqtlqtBSV41O4CnTgAHw0ACygIAHcAVTQWRLBIWCQfAGUOLk7C4rhkpG4yAGNNHzhABMIglw8RGDYuovgRI+D8aO1qtzQkS7WkOUO4AFlilAxgGh/IxTkEusBAnwjr8uACWAARAJYACOQU+Gy2SF2cyUMH65C6OjxQ2GWCgQygAEF4E8QHplABxGTrNDDdB7DQROAAbw+bAAvsous4WCIwIkoCJXoQAMRIABuKBw/FsAEYADRwABMmoAzJ56nB5jAoICAOYKIA"\))
Using Any Local Variable
Term elaborators have access to the expected type and to the local context. This can be used to create a term analogue of the `[assumption](Tactic-Proofs/Tactic-Reference/#assumption "Documentation for tactic")` tactic.
The first step is to access the local context using `getLocalHyps`. It returns the context with the outermost bindings on the left, so it is traversed in reverse order. For each local assumption, a type is inferred with `Meta.inferType`. If it can be equal to the expected type, then the assumption is returned; if no assumption is suitable, then an error is produced.
`[syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") "anything!" : term  [elab_rules](Notations-and-Macros/Elaborators/#Lean___Parser___Command___elab_rules "Documentation for syntax") <= expected   | `(anything!) => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")     let hyps ← getLocalHyps     for h in hyps.[reverse](Basic-Types/Arrays/#Array___reverse "Documentation for Array.reverse") do       let t ← Meta.inferType h       if (← Meta.isDefEq t expected) then return h      throwError m!"No assumption in {hyps} has type {expected}" `
The new syntax finds the function's bound variable:
``7`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (fun (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) => 2 + anything!) 5 `
```
7
```

It chooses the most recent suitable variable, as desired:
``"It was y"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") let x := "x" let y := "y" "It was " ++ y `
```
"It was y"
```

When no assumption is suitable, it returns an error that describes the attempt:
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax")   let x := [Nat.zero](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.zero")   let y := "hello"   fun (f : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) =>     (`No assumption in [x, y, f] has type [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`anything! : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) `
```
No assumption in [x, y, f] has type [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")
```

Because it uses unification, the natural number literal is chosen here, because numeric literals may have any type with an `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat")` instance. Unfortunately, there is no `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat")` instance for functions, so instance synthesis later fails.
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax")   let x := `failed to synthesize instance of type class   [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") ([Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) 5 numerals are polymorphic in Lean, but the numeral `5` cannot be used in a context where the expected type is   [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") due to the absence of the instance above  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`5 let y := "hello" (anything! : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) `
```
failed to synthesize instance of type class
  [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") ([Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) 5
numerals are polymorphic in Lean, but the numeral `5` cannot be used in a context where the expected type is
  [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")
due to the absence of the instance above

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```

[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAGQKYEMB2A6AogGxQIwChCIwk1FU1iBnATzRhQA84AidOmAC2DQHMAhGzgAuODCRQQxJHnwB9KAFccSGnAA8AXjhJmZAMaSAJoThwAPnAAGACk48+QgJRxtAPjgmI5i3DV4bjowDUAEwjh+JBgECEMUHAAJEJo/CwAzaDhuOD5slIwoJAA3KRokb19/f0CJOAiAWWiUDD50qQAVEIruNP9gdLg7RubWmgARJHSsAEc6/SNTNx5yOCKYZSgKXr6eKAgAdywofag4EGEAOQg4FBoaZXAYYAgKPIBvYNCAX2y7iW6cHeCyQxiQJm+bGIAGISgkhullBQ7BRxJcUDA3J44AAmOAAaluaC4vAEgjcAFYYXCcH5aqxRLo2MwoRZanQxEy6Kz2ABJeAHf4ifGEuhAA"\))
##  23.6.3. Custom Tactics[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Notations-and-Macros--Elaborators--Custom-Tactics "Permalink")
Custom tactics are described in the [section on tactics](Tactic-Proofs/Custom-Tactics/#custom-tactics). 
[←23.5. Macros](Notations-and-Macros/Macros/#macros "23.5. Macros")[23.7. Extending Lean's Output→](Notations-and-Macros/Extending-Lean___s-Output/#unexpand-and-delab "23.7. Extending Lean's Output")

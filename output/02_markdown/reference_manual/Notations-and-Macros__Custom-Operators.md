[←23. Notations and Macros](Notations-and-Macros/#language-extension "23. Notations and Macros")[23.2. Precedence→](Notations-and-Macros/Precedence/#precedence "23.2. Precedence")
#  23.1. Custom Operators[🔗](find/?domain=Verso.Genre.Manual.section&name=operators "Permalink")
Lean supports custom infix, prefix, and postfix operators. New operators can be added by any Lean library, and the new operators have equal status to those that are part of the language. Each new operator is assigned an interpretation as a function, after which uses of the operator are translated into uses of the function. The operator's translation into a function call is referred to as its _expansion_. If this function is a [type class](Type-Classes/#--tech-term-type-class) [method](Type-Classes/#--tech-term-methods), then the resulting operator can be overloaded by defining instances of the class.
All operators have a _precedence_. Operator precedence determines the order of operations for unparenthesized expressions: because multiplication has a higher precedence than addition, `2 + 3 * 4` is equivalent to `2 + (3 * 4)`, and `2 * 3 + 4` is equivalent to `(2 * 3) + 4`. Infix operators additionally have an _associativity_ that determines the meaning of a chain of operators that have the same precedence: 

Left-associative 
    
These operators nest to the left. Addition is left- associative, so `2 + 3 + 4 + 5` is equivalent to `((2 + 3) + 4) + 5`. 

Right-associative 
    
These operators nest to the right. The product type is right-associative, so `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") × [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") × [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") × [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` is equivalent to `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") × ([String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") × ([Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") × [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")))`. 

Non-associative 
    
Chaining these operators is a syntax error. Explicit parenthesization is required. Equality is non-associative, so the following is an error:

```
1 + 2 = 3 expected end of input= 2 + 1
```

The parser error is:

```
<example>:1:10-1:11: expected end of input
```
Precedence for Prefix and Infix Operators
The proposition `¬A ∧ B` is equivalent to `(¬A) ∧ B`, because `¬` has a higher precedence than `∧`. Because `∧` has higher precedence than `=` and is right-associative, `¬A ∧ B = (¬A) ∧ B` is equivalent to `¬A ∧ ((B = ¬A) ∧ B)`.
[Live ↪](javascript:openLiveLink\("IYDwlg9gtgBAgjAXDACgJwgBwFCkrAISVQxwFMRgpMAbM4gCgBqFByIhiIF4Zm4BKGOwIDuvQTwZcYLAUL4DE3NADMa2ClVr1kYuTFG9ZHBUtVA"\))
Lean provides commands for defining new operators:
syntaxOperator Declarations
Non-associative infix operators are defined using ``Lean.Parser.Command.mixfix : command```infix`:

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
      [attributes](Attributes/#Lean___Parser___Term___attributes-next)?
      


attrKind matches ("scoped" <|> "local")?, used before an attribute like @[local simp]. 


attrKind 


infix:prec "op" => f is equivalent to notation:prec x:prec1 "op" y:prec1 => f x y, where prec1 := prec + 1.


infix:prec ((name := ident))? ((priority := prio))? str => term
```

Left-associative infix operators are defined using ``Lean.Parser.Command.mixfix : command```infixl`:

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
      [attributes](Attributes/#Lean___Parser___Term___attributes-next)?
      


attrKind matches ("scoped" <|> "local")?, used before an attribute like @[local simp]. 


attrKind 


infixl:prec "op" => f is equivalent to notation:prec x:prec "op" y:prec1 => f x y, where prec1 := prec + 1.


infixl:prec ((name := ident))? ((priority := prio))? str => term
```

Right-associative infix operators are defined using ``Lean.Parser.Command.mixfix : command```infixr`:

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
      [attributes](Attributes/#Lean___Parser___Term___attributes-next)?
      


attrKind matches ("scoped" <|> "local")?, used before an attribute like @[local simp]. 


attrKind 


infixr:prec "op" => f is equivalent to notation:prec x:prec1 "op" y:prec => f x y, where prec1 := prec + 1.


infixr:prec ((name := ident))? ((priority := prio))? str => term
```

Prefix operators are defined using ``Lean.Parser.Command.mixfix : command```prefix`:

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
      [attributes](Attributes/#Lean___Parser___Term___attributes-next)?
      


attrKind matches ("scoped" <|> "local")?, used before an attribute like @[local simp]. 


attrKind 


prefix:prec "op" => f is equivalent to notation:prec "op" x:prec => f x.


prefix:prec ((name := ident))? ((priority := prio))? str => term
```

Postfix operators are defined using ``Lean.Parser.Command.mixfix : command```postfix`:

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
      [attributes](Attributes/#Lean___Parser___Term___attributes-next)?
      


attrKind matches ("scoped" <|> "local")?, used before an attribute like @[local simp]. 


attrKind 


postfix:prec "op" => f is equivalent to notation:prec x:prec "op" => f x.


postfix:prec ((name := ident))? ((priority := prio))? str => term
```

Each of these commands may be preceded by [documentation comments](Definitions/Modifiers/#--tech-term-Documentation-comments) and [attributes](Attributes/#--tech-term-Attributes). The documentation comment is shown when the user hovers their mouse over the operator, and attributes may invoke arbitrary metaprograms, just as for any other declaration. The attribute `inherit_doc` causes the documentation of the function that implements the operator to be reused for the operator itself.
Operators interact with [section scopes](Namespaces-and-Sections/#--tech-term-section-scope) in the same manner as attributes. By default, operators are available in any module that transitively imports the one in which they are established, but they may be declared `scoped` or `local` to restrict their availability either to contexts in which the current namespace has been opened or to the current [section scope](Namespaces-and-Sections/#--tech-term-section-scope), respectively.
Custom operators require a [precedence](Notations-and-Macros/Precedence/#precedence) specifier, following a colon. There is no default precedence to fall back to for custom operators.
Operators may be explicitly named. This name denotes the extension to Lean's syntax, and is primarily used for metaprogramming. If no name is explicitly provided, then Lean generates one based on the operator. The specifics of the assignment of this name should not be relied upon, both because the internal name assignment algorithm may change and because the introduction of similar operators in upstream dependencies may lead to a clash, in which case Lean will modify the assigned name until it is unique.
Assigned Operator Names
Given this infix operator:
`infix:90 " ⤴ " => [Option.getD](Basic-Types/Optional-Values/#Option___getD "Documentation for Option.getD") `
the internal name `«term_⤴_»` is assigned to the resulting parser extension.
[Live ↪](javascript:openLiveLink\("JYOwZsAeBcCcAMACARIwLJQsQXgHyIPIAOALsAPYgB0A5gKbEAiQA"\))
Provided Operator Names
Given this infix operator:
`infix:90 (name := getDOp) " ⤴ " => [Option.getD](Basic-Types/Optional-Values/#Option___getD "Documentation for Option.getD") `
the resulting parser extension is named `[getDOp](Notations-and-Macros/Custom-Operators/#getDOp-_LPAR_in-Provided-Operator-Names_RPAR_ "Definition of example")`.
[Live ↪](javascript:openLiveLink\("JYOwZsAeBcCcAMACAFCAhgWwKaOgXkQHMsAXAEQHkAHASkQCJFAWSgcTwD5FqTgB7EAHTFyQA"\))
Inheriting Documentation
Given this infix operator:
`@[inherit_doc] infix:90 " ⤴ " => [Option.getD](Basic-Types/Optional-Values/#Option___getD "Documentation for Option.getD") `
the resulting parser extension has the same documentation as `[Option.getD](Basic-Types/Optional-Values/#Option___getD "Documentation for Option.getD")`.
[Live ↪](javascript:openLiveLink\("AIbQlgdgFgpgTmALgfQCYHsDGBdAUJAMzAA8AuATgAYACAImsBZKO6gXgD5qB5AB0THQgA6AOYxEAESA"\))
When multiple operators are defined that share the same syntax, Lean's parser attempts all of them. If more than one succeed, the one that used the most input is selected—this is called the _local longest-match rule_. In some cases, parsing multiple operators may succeed, all of them covering the same range of the input. In these cases, the operator's [priority](Type-Classes/Instance-Declarations/#--tech-term-priorities) is used to select the appropriate result. Finally, if multiple operators with the same priority tie for the longest match, the parser saves all of the results, and the elaborator attempts each in turn, failing if elaboration does not succeed on exactly one of them.
Ambiguous Operators and Priorities
Defining an alternative implementation of `+` as `[Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or")` requires only an infix operator declaration.
`infix:65  " + " => [Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") `
With this declaration, Lean attempts to elaborate addition both using the built-in syntax for `[HAdd.hAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")` and the new syntax for `[Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or")`:
``[True](Basic-Propositions/Truth/#True___intro "Documentation for True") [+](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") [False](Basic-Propositions/Truth/#False "Documentation for False") : Prop`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [True](Basic-Propositions/Truth/#True___intro "Documentation for True") + [False](Basic-Propositions/Truth/#False "Documentation for False") `
```
[True](Basic-Propositions/Truth/#True___intro "Documentation for True") [+](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") [False](Basic-Propositions/Truth/#False "Documentation for False") : Prop
```
``2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") 2 + 2 `
```
2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

However, because the new operator is not associative, the [local longest-match rule](Notations-and-Macros/Custom-Operators/#--tech-term-local-longest-match-rule) means that only `[HAdd.hAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")` applies to an unparenthesized three-argument version:
`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") `failed to synthesize instance of type class   [HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd") Prop Prop ?m.3  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`[True](Basic-Propositions/Truth/#True___intro "Documentation for True") + [False](Basic-Propositions/Truth/#False "Documentation for False") + [True](Basic-Propositions/Truth/#True___intro "Documentation for True") `
```
failed to synthesize instance of type class
  [HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd") Prop Prop ?m.3

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```

If the infix operator is declared with high priority, then Lean does not try the built-in `[HAdd.hAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")` operator in ambiguous cases:
`infix:65 (priority := [high](Type-Classes/Instance-Declarations/#prioHigh "Documentation for syntax"))  " + " => [Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") ```[True](Basic-Propositions/Truth/#True___intro "Documentation for True") [+](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") [False](Basic-Propositions/Truth/#False "Documentation for False") : Prop`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [True](Basic-Propositions/Truth/#True___intro "Documentation for True") + [False](Basic-Propositions/Truth/#False "Documentation for False") `
```
[True](Basic-Propositions/Truth/#True___intro "Documentation for True") [+](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") [False](Basic-Propositions/Truth/#False "Documentation for False") : Prop
```
``sorry [+](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") sorry : Prop`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") `failed to synthesize instance of type class   [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") Prop 2 numerals are polymorphic in Lean, but the numeral `2` cannot be used in a context where the expected type is   Prop due to the absence of the instance above  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`2 + `failed to synthesize instance of type class   [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") Prop 2 numerals are polymorphic in Lean, but the numeral `2` cannot be used in a context where the expected type is   Prop due to the absence of the instance above  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`2 `
```
failed to synthesize instance of type class
  [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") Prop 2
numerals are polymorphic in Lean, but the numeral `2` cannot be used in a context where the expected type is
  Prop
due to the absence of the instance above

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```

The new operator is not associative, so the [local longest-match rule](Notations-and-Macros/Custom-Operators/#--tech-term-local-longest-match-rule) means that only `[HAdd.hAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")` applies to the three-argument version:
`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") `failed to synthesize instance of type class   [HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd") Prop Prop ?m.3  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`[True](Basic-Propositions/Truth/#True___intro "Documentation for True") + [False](Basic-Propositions/Truth/#False "Documentation for False") + [True](Basic-Propositions/Truth/#True___intro "Documentation for True") `
```
failed to synthesize instance of type class
  [HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd") Prop Prop ?m.3

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```

The actual operator is provided as a string literal. The new operator must satisfy the following requirements:
  * It must contain at least one character.
  * The first character may not be a single or double quote (`'` or `"`), unless the operator is `''`.
  * It may not begin with a backtick (```) followed by a character that would be a valid prefix of a quoted name.
  * It may not begin with a digit.
  * It may not include internal whitespace.


The operator string literal may begin or end with a space. These are not part of the operator's syntax, and their presence does not require spaces around uses of the operator. However, the presence of spaces cause Lean to insert spaces when showing the operator to the user. Omitting them causes the operator's arguments to be displayed immediately next to the operator itself.
Finally, the operator's meaning is provided, separated from the operator by ``Lean.Parser.Command.mixfix : command```=>`. This may be any Lean term. Uses of the operator are desugared into function applications, with the provided term in the function position. Prefix and postfix operators apply the term to their single argument as an explicit argument. Infix operators apply the term to the left and right arguments, in that order. Other than its ability to accept arguments at each call site, there are no specific requirements imposed on the term. Operators may construct functions, so the term may expect more parameters than the operator. Implicit and [instance-implicit](Type-Classes/#--tech-term-instance-implicit) parameters are resolved at each application site, which allows the operator to be defined by a [type class](Type-Classes/#--tech-term-type-class) [method](Type-Classes/#--tech-term-methods).
If the term consists either of a name from the global environment or of an application of such a name to one or more arguments, then Lean automatically generates an [unexpander](Notations-and-Macros/Extending-Lean___s-Output/#--tech-term-unexpanders) for the operator. This means that the operator will be displayed in [proof states](Tactic-Proofs/#--tech-term-proof-state), error messages, and other output from Lean when the function term otherwise would have been displayed. Lean does not track whether the operator was used in the original term; it is inserted at every opportunity.
Custom Operators in Lean's Output
The function `[perhapsFactorial](Notations-and-Macros/Custom-Operators/#perhapsFactorial-_LPAR_in-Custom-Operators-in-Lean___s-Output_RPAR_ "Definition of example")` computes a factorial for a number if it's not too large.
`def fact : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   | 0 => 1   | n+1 => (n + 1) * [fact](Notations-and-Macros/Custom-Operators/#fact-_LPAR_in-Custom-Operators-in-Lean___s-Output_RPAR_ "Definition of example") n  def perhapsFactorial (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") :=   [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n < 8 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ([fact](Notations-and-Macros/Custom-Operators/#fact-_LPAR_in-Custom-Operators-in-Lean___s-Output_RPAR_ "Definition of example") n) [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") `
The postfix interrobang operator can be used to represent it.
`postfix:90 "‽" => [perhapsFactorial](Notations-and-Macros/Custom-Operators/#perhapsFactorial-_LPAR_in-Custom-Operators-in-Lean___s-Output_RPAR_ "Definition of example") `
When attempting to prove that `∀ n, n ≥ 8 → ([perhapsFactorial](Notations-and-Macros/Custom-Operators/#perhapsFactorial-_LPAR_in-Custom-Operators-in-Lean___s-Output_RPAR_ "Definition of example") n).[isNone](Basic-Types/Optional-Values/#Option___isNone "Documentation for Option.isNone")`, the initial proof state uses the new operator, even though the theorem as written does not:
⊢ ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), n ≥ 8 → n[‽](Notations-and-Macros/Custom-Operators/#perhapsFactorial-_LPAR_in-Custom-Operators-in-Lean___s-Output_RPAR_ "Definition of example").[isNone](Basic-Types/Optional-Values/#Option___isNone "Documentation for Option.isNone") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")
[Live ↪](javascript:openLiveLink\("CYUwZgBGCGDGAuEBcEBy1GCTCNGBQEIAfCABggF4A+CARnyIgDsBqGi6gCkYmdoEoIAKihxEjXLlCQADiABOAC2jSAzgDFRAezkBLaABsIXZDngCUAeWnwdm7ukRJy9HZG4AeCAA4I8BSG4VTQBbECMYBCYBEH0VMMY7EAlpTRV4MB0ADyQATjIAIkBeAnz2CFlFZXUtXQMgA"\))
Infix Operators, Defined Functions, and Unexpanders
When an operator does not expand to the application of a defiend function, no unexpander is generated. Here, the postfix interrobang expands to an anonymous function that takes a factorial if its argument is not too large.
`def fact : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   | 0 => 1   | n+1 => (n + 1) * [fact](Notations-and-Macros/Custom-Operators/#fact-_LPAR_in-Infix-Operators___-Defined-Functions___-and-Unexpanders_RPAR_ "Definition of example") n  set_option quotPrecheck false [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") postfix:90 "‽" => fun (n : Nat) => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n < 8 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") some (fact n) [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") none `
Because there is no named function in the expansion, no unexpander can be generated:
``(fun n => if n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 8 then [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ([fact](Notations-and-Macros/Custom-Operators/#fact-_LPAR_in-Infix-Operators___-Defined-Functions___-and-Unexpanders_RPAR_ "Definition of example") n) else [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) 7 : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") 7‽ `
```
(fun n => if n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 8 then [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ([fact](Notations-and-Macros/Custom-Operators/#fact-_LPAR_in-Infix-Operators___-Defined-Functions___-and-Unexpanders_RPAR_ "Definition of example") n) else [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) 7 : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

Using a named function results in an unexpander, which is used for terms that consist of applications of `[perhapsFactorial](Notations-and-Macros/Custom-Operators/#perhapsFactorial-_LPAR_in-Infix-Operators___-Defined-Functions___-and-Unexpanders_RPAR_ "Definition of example")`:
`def perhapsFactorial (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") :=   [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n < 8 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ([fact](Notations-and-Macros/Custom-Operators/#fact-_LPAR_in-Infix-Operators___-Defined-Functions___-and-Unexpanders_RPAR_ "Definition of example") n) [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")  postfix:90 "‽'" => [perhapsFactorial](Notations-and-Macros/Custom-Operators/#perhapsFactorial-_LPAR_in-Infix-Operators___-Defined-Functions___-and-Unexpanders_RPAR_ "Definition of example")  ```7[‽'](Notations-and-Macros/Custom-Operators/#perhapsFactorial-_LPAR_in-Infix-Operators___-Defined-Functions___-and-Unexpanders_RPAR_ "Definition of example") : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") 7‽' `
```
7[‽'](Notations-and-Macros/Custom-Operators/#perhapsFactorial-_LPAR_in-Infix-Operators___-Defined-Functions___-and-Unexpanders_RPAR_ "Definition of example") : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

[Live ↪](javascript:openLiveLink\("CYUwZgBGCGDGAuEBcEBy1GCTCNGBQEIAfCABggF4A+CARnyIgDsBqGi6gCkYmdoEoIAKihxEjXLgDOIeAH0A9gAd4AS3ncAjgFd58AAoAnELAAWxgNYiANtIgrxi+ZPhgVADyQBOMgCJAvAQ+7FBa3FzIOPACVHaQ3AA8EAAcEPBm3JLyALYgEBwwCEwCIDY5jOogEgDEphYQAOx+EqCQiiAGJtCKkgBiovIGKtBWudwo6JHhAPLKatzjyOT0KrEQCcmpIOlZOXmihRDFtmWMFbiOzq4e3hD+AOSB0a3tnT19A0NVNbCWDbdAA"\))
[←23. Notations and Macros](Notations-and-Macros/#language-extension "23. Notations and Macros")[23.2. Precedence→](Notations-and-Macros/Precedence/#precedence "23.2. Precedence")

[←23.2. Precedence](Notations-and-Macros/Precedence/#precedence "23.2. Precedence")[23.4. Defining New Syntax→](Notations-and-Macros/Defining-New-Syntax/#syntax-ext "23.4. Defining New Syntax")
#  23.3. Notations[🔗](find/?domain=Verso.Genre.Manual.section&name=notations "Permalink")
The term _notation_ is used in two ways in Lean: it can refer to the general concept of concise ways of writing down ideas, and it is the name of a language feature that allows notations to be conveniently implemented with little code. Like custom operators, Lean notations allow the grammar of terms to be extended with new forms. However, notations are more general: the new syntax may freely intermix required keywords or operators with subterms, and they provide more precise control over precedence levels. Notations may also rearrange their parameters in the resulting subterms, while infix operators provide them to the function term in a fixed order. Because notations may define operators that use a mix of prefix, infix, and postfix components, they can be called _mixfix_ operators.
syntaxNotation Declarations
Notations are defined using the ``Lean.Parser.Command.notation : command``[`notation`](Notations-and-Macros/Notations/#Lean___Parser___Command___notation) command.

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


attrKind notation(:prec)? ((name := ident))? ((priority := prio))? notationItem* => term
```

syntaxNotation Items
The body of a notation definition consists of a sequence of _notation items_ , which may be either string literals or identifiers with optional precedences.

```
notationItem ::=
    str
```

```
notationItem ::= ...
    | ident(:prec)?
```

As with operator declarations, the contents of the documentation comments are shown to users while they interact with the new syntax. Adding the `inherit_doc` attribute causes the documentation comment of the function at the head of the term into which the notation expands to be copied to the new syntax. Other attributes may be added to invoke other compile-time metaprograms on the resulting definition.
Notations interact with [section scopes](Namespaces-and-Sections/#--tech-term-section-scope) in the same manner as attributes and operators. By default, notations are available in any module that transitively imports the one in which they are established, but they may be declared `scoped` or `local` to restrict their availability either to contexts in which the current namespace has been opened or to the current [section scope](Namespaces-and-Sections/#--tech-term-section-scope), respectively.
Like operators, the [local longest-match rule](Notations-and-Macros/Custom-Operators/#--tech-term-local-longest-match-rule) is used while parsing notations. If more than one notation ties for the longest match, the declared priorities are used to determine which parse result applies. If this still does not resolve the ambiguity, then all are saved, and the elaborator is expected to attempt all of them, succeeding when exactly one can be elaborated.
Rather than a single operator with its fixity and token, the body of a notation declaration consists of a sequence of _notation items_ , which may be either new [atoms](Notations-and-Macros/Defining-New-Syntax/#--tech-term-Atoms) (including both keywords such as `if`, `#eval`, or `where` and symbols such as `=>`, `+`, `↗`, `⟦`, or `⋉`) or positions for terms. Just as they do in operators, string literals identify the placement of atoms. Leading and trailing spaces in the strings do not affect parsing, but they cause Lean to insert spaces in the corresponding position when displaying the syntax in [proof states](Tactic-Proofs/#--tech-term-proof-state) and error messages. Identifiers indicate positions where terms are expected, and name the corresponding term so it can be inserted in the notation's expansion.
While custom operators have a single notion of precedence, there are many involved in a notation. The notation itself has a precedence, as does each term to be parsed. The notation's precedence determines which contexts it may be parsed in: the parser only attempts to parse productions whose precedence is at least as high as the current context. For example, because multiplication has higher precedence than addition, the parser will attempt to parse an infix multiplication term while parsing the arguments to addition, but not vice versa. The precedence of each term to be parsed determines which other productions may occur in them.
If no precedence is supplied for the notation itself, the default value depends on the form of the notation. If the notation both begins and ends with an atom (represented by string literals), then the default precedence is `max`. This applies both to notations that consist only of a single atom and to notations with multiple items, in which the first and last items are both atoms. Otherwise, the default precedence of the whole notation is `lead`. If no precedence is provided for notation items that are terms, then they default to precedence `min`.
After the required double arrow (``Lean.Parser.Command.notation : command``[`=>`](Notations-and-Macros/Notations/#Lean___Parser___Command___notation)), the notation is provided with an expansion. While operators are always expanded by applying their function to the operator's arguments in order, notations may place their term items in any position in the expansion. The terms are referred to by name. Term items may occur any number of times in the expansion. Because notation expansion is a purely syntactic process that occurs prior to elaboration or code generation, duplicating terms in the expansion may lead to duplicated computation when the resulting term is evaluated, or even duplicated side effects when working in a monad.
Ignored Terms in Notation Expansion
This notation ignores its first parameter:
`[notation](Notations-and-Macros/Notations/#Lean___Parser___Command___notation "Documentation for syntax") (name := ignore) "ignore " _ign:[arg](Notations-and-Macros/Precedence/#precArg "Documentation for syntax") e:[arg](Notations-and-Macros/Precedence/#precArg "Documentation for syntax") => e `
The term in the ignored position is discarded, and Lean never attempts to elaborate it, so terms that would otherwise result in errors can be used here:
``5`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ignore (2 + "whatever") 5 `
```
5
```

However, the ignored term must still be syntactically valid:

```
#eval ignore (2 +unexpected token ')'; expected term) 5
```

```
<example>:1:17-1:18: unexpected token ')'; expected term
```

[Live ↪](javascript:openLiveLink\("HYewLghmCWLABACmBAtgU3gLgLz2gOagBO6AlPAESEmaXwD6NWExB86Lb8OAfBwCgBAYnQA3CABt8REKSQAmeAGoqAdwAWUcemKUKAViA"\))
Duplicated Terms in Notation Expansion
The ``dup : term```dup!` notation duplicates its sub-term.
`[notation](Notations-and-Macros/Notations/#Lean___Parser___Command___notation "Documentation for syntax") (name := dup) "dup!" t:[arg](Notations-and-Macros/Precedence/#precArg "Documentation for syntax") => (t, t) `
Because the term is duplicated, it can be elaborated separately with different types:
`def e : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") × [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") := dup! (2 + 2) `
Printing the resulting definition demonstrates that the work of addition will be performed twice:
``def e : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") := [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")`#print [e](Notations-and-Macros/Notations/#e-_LPAR_in-Duplicated-Terms-in-Notation-Expansion_RPAR_ "Definition of example") `
```
def e : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") :=
[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")
```

[Live ↪](javascript:openLiveLink\("HYewLghmCWLABACmBAtgU3gLgLzwCYCuADgJTwBERxAhBfGFhAE4Dm8OAfEmADQOkAUIPzoAZvExZ4AOSjwA6/ACSwMNjzUaSAEzwA1PB1DBAYmLNoayUA"\))
When the expansion consists of the application of a function defined in the global environment and each term in the notation occurs exactly once, an [unexpander](Notations-and-Macros/Extending-Lean___s-Output/#--tech-term-unexpanders) is generated. The new notation will be displayed in [proof states](Tactic-Proofs/#--tech-term-proof-state), error messages, and other output from Lean when matching function application terms otherwise would have been displayed. As with custom operators, Lean does not track whether the notation was used in the original term; it is used at every opportunity in Lean's output.
Notations, Defined Functions, and Unexpanders
When a notation does not expand to the application of a defined function, no unexpander is generated. Here, the notation expands to an anonymous function:
`[notation](Notations-and-Macros/Notations/#Lean___Parser___Command___notation "Documentation for syntax") "[" start " ⇒ " stop "]" => fun x => x > start && x < stop `
Because there is no named function in the expansion, no unexpander can be generated:
``fun x => [decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") (x > 5) [&&](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 8[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [5 ⇒ 8] `
```
fun x => [decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") (x > 5) [&&](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 8[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

Using a named function results in an unexpander, which is used for terms that consist of applications of `[between](Notations-and-Macros/Notations/#between-_LPAR_in-Notations___-Defined-Functions___-and-Unexpanders_RPAR_ "Definition of example")`:
`def between (start stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Prop :=   fun x => x > start && x < stop  [notation](Notations-and-Macros/Notations/#Lean___Parser___Command___notation "Documentation for syntax") "[" start " ⇒' " stop "]" => [between](Notations-and-Macros/Notations/#between-_LPAR_in-Notations___-Defined-Functions___-and-Unexpanders_RPAR_ "Definition of example") start stop ```[[](Notations-and-Macros/Notations/#between-_LPAR_in-Notations___-Defined-Functions___-and-Unexpanders_RPAR_ "Definition of example")5 [⇒'](Notations-and-Macros/Notations/#between-_LPAR_in-Notations___-Defined-Functions___-and-Unexpanders_RPAR_ "Definition of example") 8[]](Notations-and-Macros/Notations/#between-_LPAR_in-Notations___-Defined-Functions___-and-Unexpanders_RPAR_ "Definition of example") : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Prop`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [5 ⇒' 8] `
```
[[](Notations-and-Macros/Notations/#between-_LPAR_in-Notations___-Defined-Functions___-and-Unexpanders_RPAR_ "Definition of example")5 [⇒'](Notations-and-Macros/Notations/#between-_LPAR_in-Notations___-Defined-Functions___-and-Unexpanders_RPAR_ "Definition of example") 8[]](Notations-and-Macros/Notations/#between-_LPAR_in-Notations___-Defined-Functions___-and-Unexpanders_RPAR_ "Definition of example") : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Prop
```

[Live ↪](javascript:openLiveLink\("HYewLghmCWLABAIgNqPgZ0gJzE+glwj0xAAckBdNAXgD54AzAVwQA95b427MId4Ayfp3gAeDGFIAoSQGIAxgAsApnIDW8ZAFYC8ABzlpAEyX14AIyVgA7kqUIAFDz7EyALngA5KAEp47r7iASYTwAApYpH5UkvAMzMIcXOK8uILCYi7SoJAwcEioSXxo+ADkRBJkiJTsdBbWtghOuBmyiirqWgSl+kA"\))
##  23.3.1. Operators and Notations[🔗](find/?domain=Verso.Genre.Manual.section&name=operators-and-notations "Permalink")
Internally, operator declarations are translated into notation declarations. Term notation items are inserted where the operator would expect arguments, and in the corresponding positions in the expansion. For prefix and postfix operators, the notation's precedence as well as the precedences of its term items is the operator's declared precedence. For non-associative infix operators, the notation's precedence is the declared precedence, but both arguments are parsed at a precedence level that is one higher, which prevents successive uses of the notation without parentheses. Associative infix operators use the operator's precedence for the notation and for one argument, while a precedence that is one level higher is used for the other argument; this prevents successive applications in one direction only. Left-associative operators use the higher precedence for their right argument, while right-associative operators use the higher precedence for their left argument. 
[←23.2. Precedence](Notations-and-Macros/Precedence/#precedence "23.2. Precedence")[23.4. Defining New Syntax→](Notations-and-Macros/Defining-New-Syntax/#syntax-ext "23.4. Defining New Syntax")

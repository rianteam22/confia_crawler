[←13.9. Holes](Terms/Holes/#The-Lean-Language-Reference--Terms--Holes "13.9. Holes")[13.11. Quotation and Antiquotation→](Terms/Quotation-and-Antiquotation/#The-Lean-Language-Reference--Terms--Quotation-and-Antiquotation "13.11. Quotation and Antiquotation")
#  13.10. Type Ascription[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Terms--Type-Ascription "Permalink")
_Type ascriptions_ explicitly annotate terms with their types. They are a way to provide Lean with the expected type for a term. This type must be definitionally equal to the type that is expected based on the term's context. Type ascriptions are useful for more than just documenting a program:
  * There may not be sufficient information in the program text to derive a type for a term. Ascriptions are one way to provide the type.
  * An inferred type may not be the one that was desired for a term.
  * The expected type of a term is used to drive the insertion of [coercions](Coercions/#--tech-term-coercion), and ascriptions are one way to control where coercions are inserted.


syntaxPostfix Type Ascriptions
Type ascriptions must be surrounded by parentheses. They indicate that the first term's type is the second term.

```
term ::= ...
    | 


Type ascription notation: (0 : Int) instructs Lean to process 0 as a value of type Int.
An empty type ascription (e :) elaborates e without the expected type.
This is occasionally useful when Lean's heuristics for filling arguments from the expected type
do not yield the right result.


([anonymous]term : term)
```

In cases where the term that requires a type ascription is long, such as a tactic proof or a ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block, the postfix type ascription with its mandatory parentheses can be difficult to read. Additionally, for both proofs and ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) blocks, the term's type is essential to its interpretation. In these cases, the prefix versions can be easier to read.
syntaxPrefix Type Ascriptions

```
term ::= ...
    | show term from term
```

When the term in the body of ``Lean.Parser.Term.show : term```show` is a tactic proof, the keyword ``Lean.Parser.Term.show : term```from` may be omitted.

```
term ::= ...
    | show term by 


A sequence of tactics in brackets, or a delimiter-free indented sequence of tactics.
Delimiter-free indentation is determined by the _first_ tactic of the sequence. 


tacticSeq
```

Ascribing Statements to Proofs
This example is unable to execute the tactic proof because the desired proposition is not known. As part of running the earlier tactics, the proposition is automatically refined to be one that the tactics could prove. However, their default cases fill it out incorrectly, leading to a proof that fails.
`example (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) := byn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ ?m.2 n   [induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic") nzero⊢ ?m.2 0succn✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:?m.2 n✝⊢ ?m.2 [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")   [next](Tactic-Proofs/The-Tactic-Language/#next "Documentation for tactic") =>⊢ ?m.2 0 [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙   [next](Tactic-Proofs/The-Tactic-Language/#next "Documentation for tactic") n' ih =>n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")ih:?m.2 n✝⊢ ?m.2 [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")     [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") only [[HAdd.hAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd"), [Add.add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add.add"), [Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add")] at *n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")ih:0 [≍](Basic-Propositions/Propositional-Equality/#HEq___refl "Documentation for HEq") n'⊢ 0 [≍](Basic-Propositions/Propositional-Equality/#HEq___refl "Documentation for HEq") n'.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")     [rewrite](Tactic-Proofs/Tactic-Reference/#rewrite "Documentation for tactic") [`Invalid rewrite argument: Expected an equality or iff proof or definition name, but `ih` is a proof of   0 [≍](Basic-Propositions/Propositional-Equality/#HEq___refl "Documentation for HEq") n'`ih]n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")ih:0 [≍](Basic-Propositions/Propositional-Equality/#HEq___refl "Documentation for HEq") n'⊢ 0 [≍](Basic-Propositions/Propositional-Equality/#HEq___refl "Documentation for HEq") n'.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic") `
```
Invalid rewrite argument: Expected an equality or iff proof or definition name, but `ih` is a proof of
  0 [≍](Basic-Propositions/Propositional-Equality/#HEq___refl "Documentation for HEq") n'
```

A prefix type ascription with ``Lean.Parser.Term.show : term```show` can be used to provide the proposition being proved. This can be useful in syntactic contexts where adding it as a local definition would be inconvenient.
`example (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) := show 0 + n = n byAll goals completed! 🐙   [induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic") nzero⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0succn✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n✝ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n✝⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1   [next](Tactic-Proofs/The-Tactic-Language/#next "Documentation for tactic") =>⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙   [next](Tactic-Proofs/The-Tactic-Language/#next "Documentation for tactic") n' ih =>n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")ih:0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n✝ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n✝⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1     [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") only [[HAdd.hAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd"), [Add.add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add.add"), [Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add")] at *n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")ih:[Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add") 0 n' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n'⊢ ([Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add") 0 n').[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n'.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")     [rewrite](Tactic-Proofs/Tactic-Reference/#rewrite "Documentation for tactic") [ih]n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")ih:[Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add") 0 n' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n'⊢ n'.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n'.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")     [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAKAdvAXPAcmALgSnQF54BnACwHsB3eABngGp5VjUAjATwCh54BLZABMArgGMcfCqmQ9moHPEIA+eACcAZjFnJ5zAOT8yipbN4k+0eFJgd4AbQASAQUGCAdGReCANPC9uwV19sHADXAF14XHgAKlM1YCpVPhwEOz4ycPiNGCA"\))
Ascribing Types to ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) Blocks
This example lacks sufficient type information to synthesize the `[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure")` instance.
`example := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   `typeclass instance problem is stuck   [Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") ?m.12  Note: Lean will not try to resolve this typeclass instance problem because the type argument to `[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure")` is a metavariable. This argument must be fully determined before Lean will try to resolve the typeclass.  Hint: Adding type annotations and supplying implicit arguments to functions can give Lean more information for typeclass resolution. For example, if you have a variable `x` that you intend to be a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, but Lean reports it as having an unresolved type like `?m`, replacing `x` with `(x : Nat)` can get typeclass resolution un-stuck.`return 5 `
```
typeclass instance problem is stuck
  [Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") ?m.12

Note: Lean will not try to resolve this typeclass instance problem because the type argument to `[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure")` is a metavariable. This argument must be fully determined before Lean will try to resolve the typeclass.

Hint: Adding type annotations and supplying implicit arguments to functions can give Lean more information for typeclass resolution. For example, if you have a variable `x` that you intend to be a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, but Lean reports it as having an unresolved type like `?m`, replacing `x` with `(x : Nat)` can get typeclass resolution un-stuck.
```

A prefix type ascription with ``Lean.Parser.Term.show : term```show`, together with a [hole](Terms/Holes/#--tech-term-hole), can be used to indicate the monad. The [default](Type-Classes/Instance-Synthesis/#--tech-term-default-instances) `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") _ 5` instance provides enough type information to fill the hole with `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`.
`example := show [StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") _ from [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   return 5 `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAuAvPAzgCwPYHd4GUAXMQ4AWQMICcBLAOwHN4B9eAMyqwngBMsAoePCrBCAVyp14AViA"\))
There is an important difference between postfix type ascriptions and ``Lean.Parser.Term.show : term```show`. Ordinary postfix type ascriptions change the type that is expected for the term, which can change the way that the term elaborates. After elaboration, however, Lean infers the type of the resulting term and uses that inferred type for further elaboration tasks. On the other hand, ``Lean.Parser.Term.show : term```show` elaborates to a term whose inferred type is the ascribed type. The difference can be observed when using [generalized field notation](Terms/Function-Application/#--tech-term-generalized-field-notation), where the ascribed type is only guaranteed to be used to resolve fields when using ``Lean.Parser.Term.show : term```show`.
Postfix Ascription vs `show`
This definition establishes an alternative name for `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`:
`def Colors := [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") `
A postfix type ascription provides the type information that's needed to determine the implicit argument `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` to `[List.nil](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")`, but the resulting type is still `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`:
``[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil") : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") ([] : [Colors](Terms/Type-Ascription/#Colors-_LPAR_in-Postfix-Ascription-vs--show_RPAR_ "Definition of example")) `
```
[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil") : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

When using ``Lean.Parser.Term.show : term```show`, on the other hand, the elaborated term is constructed in such a way that the inferred type is `[Colors](Terms/Type-Ascription/#Colors-_LPAR_in-Postfix-Ascription-vs--show_RPAR_ "Definition of example")`:
``have this := [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil"); this : [Colors](Terms/Type-Ascription/#Colors-_LPAR_in-Postfix-Ascription-vs--show_RPAR_ "Definition of example")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") (show [Colors](Terms/Type-Ascription/#Colors-_LPAR_in-Postfix-Ascription-vs--show_RPAR_ "Definition of example") from []) `
```
have this := [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil");
this : [Colors](Terms/Type-Ascription/#Colors-_LPAR_in-Postfix-Ascription-vs--show_RPAR_ "Definition of example")
```

This function is designed to be invoked using [generalized field notation](Terms/Function-Application/#--tech-term-generalized-field-notation):
`def Colors.hasYellow (cs : [Colors](Terms/Type-Ascription/#Colors-_LPAR_in-Postfix-Ascription-vs--show_RPAR_ "Definition of example")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") :=   cs.[any](Basic-Types/Linked-Lists/#List___any "Documentation for List.any") (·.[toLower](Basic-Types/Strings/#String___toLower "Documentation for String.toLower") == "yellow") `
Due to the differences in their inferred types, it can be used with ``Lean.Parser.Term.show : term```show`, but not with the postfix type ascription:
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ([] : [Colors](Terms/Type-Ascription/#Colors-_LPAR_in-Postfix-Ascription-vs--show_RPAR_ "Definition of example")).`Invalid field `hasYellow`: The environment does not contain `List.hasYellow`, so it is not possible to project the field `hasYellow` from an expression   [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil") of type `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")``hasYellow `
```
Invalid field `hasYellow`: The environment does not contain `List.hasYellow`, so it is not possible to project the field `hasYellow` from an expression
  [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")
of type `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`
```
``[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (show [Colors](Terms/Type-Ascription/#Colors-_LPAR_in-Postfix-Ascription-vs--show_RPAR_ "Definition of example") from []).[hasYellow](Terms/Type-Ascription/#Colors___hasYellow-_LPAR_in-Postfix-Ascription-vs--show_RPAR_ "Definition of example") `
```
[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")
```

[←13.9. Holes](Terms/Holes/#The-Lean-Language-Reference--Terms--Holes "13.9. Holes")[13.11. Quotation and Antiquotation→](Terms/Quotation-and-Antiquotation/#The-Lean-Language-Reference--Terms--Quotation-and-Antiquotation "13.11. Quotation and Antiquotation")

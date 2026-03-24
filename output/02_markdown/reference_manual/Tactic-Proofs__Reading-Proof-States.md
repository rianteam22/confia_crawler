[←14.1. Running Tactics](Tactic-Proofs/Running-Tactics/#by "14.1. Running Tactics")[14.3. The Tactic Language→](Tactic-Proofs/The-Tactic-Language/#tactic-language "14.3. The Tactic Language")
#  14.2. Reading Proof States[🔗](find/?domain=Verso.Genre.Manual.section&name=proof-states "Permalink")
The goals in a proof state are displayed in order, with the main goal on top. Goals may be either named or anonymous. Named goals are indicated with `case` at the top (called a _case label_), while anonymous goals have no such indicator. Tactics assign goal names, typically on the basis of constructor names, parameter names, structure field names, or the nature of the reasoning step implemented by the tactic.
Named goals
This proof state contains four goals, all of which are named. This is part of a proof that the `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` instance is lawful (that is, to provide the `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` instance), and the case names (highlighted below) come from the names of the fields of `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad")`.
bind_pure_compα:Type ?u.43β:Type ?u.43f:α → βx:[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α⊢ (do let a ← x [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") (f a)) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") xbind_mapα:Type ?u.43β:Type ?u.43f:[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (α → β)x:[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α⊢ (do let x_1 ← f x_1 [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f <*> xpure_bindα:Type ?u.43β:Type ?u.43x:αf:α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β⊢ [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") f [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f xbind_assocα:Type ?u.43β:Type ?u.43γ:Type ?u.43x:[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") αf:α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") βg:β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ⊢ x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") f [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") g [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") fun x => f x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") g
Anonymous Goals
This proof state contains a single anonymous goal.
n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n
The `[case](Tactic-Proofs/The-Tactic-Language/#case "Documentation for tactic")` and `[case'](Tactic-Proofs/The-Tactic-Language/#case___ "Documentation for tactic")` tactics can be used to select a new main goal using the desired goal's name. When names are assigned in the context of a goal which itself has a name, the new goals' names are appended to the main goal's name with a dot (`'.', Unicode FULL STOP (0x2e)`) between them.
Hierarchical Goal Names
In the course of an attempt to prove `∀ (n k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), n + k = k + n`, this proof state can occur:
zerok:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0succk:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")n✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n✝⊢ n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")
After `[induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic") kzero.zero⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0zero.succn✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n✝ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0succk:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")n✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n✝⊢ n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")`, the two new cases' names have `zero` as a prefix, because they were created in a goal named `zero`:
zero.zero⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0zero.succn✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n✝ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0succk:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")n✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n✝⊢ n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")
Each goal consists of a sequence of assumptions and a desired conclusion. Each assumption has a name and a type; the conclusion is a type. Assumptions are either arbitrary elements of some type or statements that are presumed true.
Assumption Names and Conclusion
This goal has four assumptions:
consα:Type ?u.317x:αxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") αih:xs [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") xs⊢ x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs
They are:
  * `α`, an arbitrary type
  * `x`, an arbitrary `α`
  * `xs`, an arbitrary `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α`
  * `ih`, an induction hypothesis that asserts that appending the empty list to `xs` is equal to `xs`.


The conclusion is the statement that prepending `x` to both sides of the equality in the induction hypothesis results in equal lists.
Some assumptions are _inaccessible_ ,  which means that they cannot be referred to explicitly by name. Inaccessible assumptions occur when an assumption is created without a specified name or when the assumption's name is shadowed by a later assumption. Inaccessible assumptions should be regarded as anonymous; they are presented as if they had names because they may be referred to in later assumptions or in the conclusion, and displaying a name allows these references to be distinguished from one another. In particular, inaccessible assumptions are presented with daggers (`†`) after their names.
Accessible Assumption Names
In this proof state, all assumptions are accessible.
bind_pure_compα:Type ?u.470β:Type ?u.470f:α → βx:[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α⊢ (do let a ← x [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") (f a)) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x
Inaccessible Assumption Names
In this proof state, only the first and third assumptions are accessible. The second and fourth are inaccessible, and their names include a dagger to indicate that they cannot be referenced.
bind_pure_compα:Type ?u.579β✝:Type ?u.579f:α → β✝x✝:[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α⊢ (do let a ← x✝ [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") (f a)) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x✝
Inaccessible assumptions can still be used. Tactics such as `[assumption](Tactic-Proofs/Tactic-Reference/#assumption "Documentation for tactic")` or `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` can scan the entire list of assumptions, finding one that is useful, and `[contradiction](Tactic-Proofs/Tactic-Reference/#contradiction "Documentation for tactic")` can eliminate the current goal by finding an impossible assumption without naming it. Other tactics, such as `[rename_i](Tactic-Proofs/The-Tactic-Language/#rename_i "Documentation for tactic")` and `[next](Tactic-Proofs/The-Tactic-Language/#next "Documentation for tactic")`, can be used to name inaccessible assumptions, making them accessible. Additionally, assumptions can be referred to by their type, by writing the type in single guillemets.
syntaxAssumptions by Type
Single guillemets around a term represent a reference to some term in scope with that type.

```
term ::= ...
    | 


‹t› resolves to an (arbitrary) hypothesis of type t.
It is useful for referring to hypotheses without accessible names.
t may contain holes that are solved by unification with the expected type;
in particular, ‹_› is a shortcut for by assumption.


‹term›
```

This can be used to refer to local lemmas by their theorem statement rather than by name, or to refer to assumptions regardless of whether they have explicit names.
Assumptions by Type
In the following proof, `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")` is repeatedly used to analyze a number. At the beginning of the proof, the number is named `x`, but `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")` generates an inaccessible name for subsequent numbers. Rather than providing names, the proof takes advantage of the fact that there is a single assumption of type `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` at any given time and uses `‹Nat›` to refer to it. After the iteration, there is an assumption that `n + 3 < 3`, which `[contradiction](Tactic-Proofs/Tactic-Reference/#contradiction "Documentation for tactic")` can use to remove the goal from consideration.
`example : x < 3 → x ∈ [0, 1, 2] := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3 → x ∈ [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")   [intros](Tactic-Proofs/Tactic-Reference/#intros "Documentation for tactic")x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3⊢ x ∈ [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")   [iterate](Tactic-Proofs/The-Tactic-Language/#iterate "Documentation for tactic") 3     [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") ‹Nat›succ.succ.zeroa✝:0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 ∈ [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")succ.succ.succn✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3⊢ n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 ∈ [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")     .succ.succ.zeroa✝:0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 ∈ [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")All goals completed! 🐙   [contradiction](Tactic-Proofs/Tactic-Reference/#contradiction "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAueJ4B54GZ6CTCF9AIIngG0AGAGngEZKAmAXSQF54AjATwCh54BLAOwAuAJwD2AZ259BwYWBlYpPAMZhxwcfECcBADl5gLgIl8AHTwAJsGW8LU5aKFyzvZYN72gA"\))
Assumptions by Type, Outside Proofs
Single-guillemet syntax also works outside of proofs:
``2`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") let x := 1 let y := 2 ‹Nat› `
```
2
```

This is generally not a good idea for non-propositions, however—when it matters _which_ element of a type is selected, it's better to select it explicitly.
[Live ↪](javascript:openLiveLink\("MQUwbghgNgUABHKIAucAecBcBeOBGeRFOATy1wCZDBOAgDkJlAuAiA"\))
##  14.2.1. Hiding Proofs and Large Terms[🔗](find/?domain=Verso.Genre.Manual.section&name=hiding-terms-in-proof-states "Permalink")
Terms in proof states can be quite big, and there may be many assumptions. Because of definitional proof irrelevance, proof terms typically give little useful information. By default, they are not shown in goals in proof states unless they are _atomic_ , meaning that they contain no subterms. Hiding proofs is controlled by two options: `[pp.proofs](Tactic-Proofs/Reading-Proof-States/#pp___proofs "Documentation for option pp.proofs")` turns the feature on and off, while `[pp.proofs.threshold](Tactic-Proofs/Reading-Proof-States/#pp___proofs___threshold "Documentation for option pp.proofs.threshold")` determines a size threshold for proof hiding.
Hiding Proof Terms
In this proof state, the proof that `0 < n` is hidden.
n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")i:[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") ngt:↑i > 5⊢ [⟨](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.mk")0[,](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.mk") ⋯[⟩](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.mk") [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") i
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=pp.proofs "Permalink")option
```
pp.proofs
```

Default value: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
(pretty printer) display proofs when true, and replace proofs appearing within expressions by `⋯` when false
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=pp.proofs.threshold "Permalink")option
```
pp.proofs.threshold
```

Default value: `0`
(pretty printer) when `[pp.proofs](Tactic-Proofs/Reading-Proof-States/#pp___proofs "Documentation for option pp.proofs")` is false, controls the complexity of proofs at which they begin being replaced with `⋯`
Additionally, non-proof terms may be hidden when they are too large. In particular, Lean will hide terms that are below a configurable depth threshold, and it will hide the remainder of a term once a certain amount in total has been printed. Showing deep terms can be enabled or disabled with the option `[pp.deepTerms](Tactic-Proofs/Reading-Proof-States/#pp___deepTerms "Documentation for option pp.deepTerms")`, and the depth threshold can be configured with the option `[pp.deepTerms.threshold](Tactic-Proofs/Reading-Proof-States/#pp___deepTerms___threshold "Documentation for option pp.deepTerms.threshold")`. The maximum number of pretty printer steps can be configured with the option `[pp.maxSteps](Tactic-Proofs/Reading-Proof-States/#pp___maxSteps "Documentation for option pp.maxSteps")`. Printing very large terms can lead to slowdowns or even stack overflows in tooling; please be conservative when adjusting these options' values.
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=pp.deepTerms "Permalink")option
```
pp.deepTerms
```

Default value: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
(pretty printer) display deeply nested terms, replacing them with `⋯` if set to false
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=pp.deepTerms.threshold "Permalink")option
```
pp.deepTerms.threshold
```

Default value: `50`
(pretty printer) when `[pp.deepTerms](Tactic-Proofs/Reading-Proof-States/#pp___deepTerms "Documentation for option pp.deepTerms")` is false, the depth at which terms start being replaced with `⋯`
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=pp.maxSteps "Permalink")option
```
pp.maxSteps
```

Default value: `5000`
(pretty printer) maximum number of expressions to visit, after which terms will pretty print as `⋯`
##  14.2.2. Metavariables[🔗](find/?domain=Verso.Genre.Manual.section&name=metavariables-in-proofs "Permalink")
Terms that begin with a question mark are _metavariables_ that correspond to an unknown value. They may stand for either [universe](The-Type-System/Universes/#--tech-term-universes) levels or for terms. Some metavariables arise as part of Lean's elaboration process, when not enough information is yet available to determine a value. These metavariables' names have a numeric component at the end, such as `?m.392` or `?u.498`. Other metavariables come into existence as a result of tactics or [synthetic holes](Terms/Holes/#--tech-term-synthetic-holes). These metavariables' names do not have a numeric component. Metavariables that result from tactics frequently appear as goals whose [case labels](Tactic-Proofs/Reading-Proof-States/#--tech-term-case-label) match the name of the metavariable.
Universe Level Metavariables
In this proof state, the universe level of `α` is unknown:
α:Type ?u.919x:αxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") αelem:x ∈ xs⊢ xs.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") > 0
Type Metavariables
In this proof state, the type of list elements is unknown. The metavariable is repeated because the unknown type must be the same in both positions.
x:?m.8xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ?m.8elem:x ∈ xs⊢ xs.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") > 0
Metavariables in Proofs
In this proof state,
i:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")j:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") jh2:j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k⊢ i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k
applying the tactic `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") Nat.lt_transh₁i:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")j:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") jh2:j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k⊢ i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") ?mai:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")j:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") jh2:j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k⊢ ?m [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") kmi:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")j:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") jh2:j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k⊢ [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` results in the following proof state, in which the middle value of the transitivity step `?m` is unknown:
h₁i:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")j:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") jh2:j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k⊢ i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") ?mai:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")j:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") jh2:j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k⊢ ?m [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") kmi:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")j:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") jh2:j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k⊢ [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
Explicitly-Created Metavariables
Explicit named holes are represented by metavariables, and additionally give rise to proof goals. In this proof state,
i:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")j:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") jh2:j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k⊢ i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k
applying the tactic `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") @Nat.lt_trans i ?middle k ?p1 ?p2middlei:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")j:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") jh2:j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k⊢ [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")p1i:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")j:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") jh2:j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k⊢ i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") ?middlep2i:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")j:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") jh2:j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k⊢ ?middle [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k` results in the following proof state, in which the middle value of the transitivity step `?middle` is unknown and goals have been created for each of the named holes in the term:
middlei:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")j:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") jh2:j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k⊢ [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")p1i:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")j:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") jh2:j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k⊢ i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") ?middlep2i:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")j:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") jh2:j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k⊢ ?middle [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k
The display of metavariable numbers can be disabled using the `[pp.mvars](Tactic-Proofs/Reading-Proof-States/#pp___mvars "Documentation for option pp.mvars")`. This can be useful when using features such as ``Lean.guardMsgsCmd : command`
`/-- ... -/ #guard_msgs in cmd` captures the messages generated by the command `cmd` and checks that they match the contents of the docstring.
Basic example:

```
/--
error: Unknown identifier `x`
-/
#guard_msgs in
example : α := x

```

This checks that there is such an error and then consumes the message.
By default, the command captures all messages, but the filter condition can be adjusted. For example, we can select only warnings:

```
/--
warning: declaration uses 'sorry'
-/
#guard_msgs(warning) in
example : α := sorry

```

or only errors

```
#guard_msgs(error) in
example : α := sorry

```

In the previous example, since warnings are not captured there is a warning on `sorry`. We can drop the warning completely with

```
#guard_msgs(error, drop warning) in
example : α := sorry

```

In general, `#guard_msgs` accepts a comma-separated list of configuration clauses in parentheses:

```
#guard_msgs (configElt,*) in cmd

```

By default, the configuration list is `(check all, whitespace := normalized, ordering := exact, positions := false)`.
Message filters select messages by severity:
  * `info`, `warning`, `error`: (non-trace) messages with the given severity level.
  * `trace`: trace messages
  * `all`: all messages.


The filters can be prefixed with the action to take:
  * `check` (the default): capture and check the message
  * `drop`: drop the message
  * `pass`: let the message pass through


If no filter is specified, `check all` is assumed. Otherwise, these filters are processed in left-to-right order, with an implicit `pass all` at the end.
Whitespace handling (after trimming leading and trailing whitespace):
  * `whitespace := exact` requires an exact whitespace match.
  * `whitespace := normalized` converts all newline characters to a space before matching (the default). This allows breaking long lines.
  * `whitespace := lax` collapses whitespace to a single space before matching.


Message ordering:
  * `ordering := exact` uses the exact ordering of the messages (the default).
  * `ordering := sorted` sorts the messages in lexicographic order. This helps with testing commands that are non-deterministic in their ordering.


Position reporting:
  * `positions := true` reports the ranges of all messages relative to the line on which `#guard_msgs` appears.
  * `positions := false` does not report position info.


Substring matching:
  * `substring := true` checks that the docstring appears as a substring of the output (after whitespace normalization). This is useful when you only care about part of the message.
  * `substring := false` (the default) requires exact matching (modulo whitespace normalization).


Stabilizing output: When messages contain autogenerated names (e.g., metavariables like `?m.47`), the output may differ between runs or Lean versions. Use `set_option pp.mvars.anonymous false` to replace anonymous metavariables with `?_` while preserving user-named metavariables like `?a`. Alternatively, `set_option pp.mvars false` replaces all metavariables with `?_`. Similarly, `set_option pp.fvars.anonymous false` replaces loose free variable names like `_fvar.22` with `_fvar._`.
For example, `#guard_msgs (error, drop all) in cmd` means to check errors and drop everything else.
The command elaborator has special support for `#guard_msgs` for linting. The `#guard_msgs` itself wants to capture linter warnings, so it elaborates the command it is attached to as if it were a top-level command. However, the command elaborator runs linters for _all_ top-level commands, which would include `#guard_msgs` itself, and would cause duplicate and/or uncaptured linter warnings. The top-level command elaborator only runs the linters if `#guard_msgs` is not present.
`[`#guard_msgs`](Interacting-with-Lean/#Lean___guardMsgsCmd) that match Lean's output against a desired string, which is very useful when writing tests for custom tactics.
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=pp.mvars "Permalink")option
```
pp.mvars
```

Default value: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
(pretty printer) display names of metavariables when true, and otherwise display them as '?_' (for expression metavariables) and as '_ ' (for universe level metavariables)
[←14.1. Running Tactics](Tactic-Proofs/Running-Tactics/#by "14.1. Running Tactics")[14.3. The Tactic Language→](Tactic-Proofs/The-Tactic-Language/#tactic-language "14.3. The Tactic Language")

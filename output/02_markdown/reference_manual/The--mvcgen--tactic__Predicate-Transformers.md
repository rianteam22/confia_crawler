[←17.1. Overview](The--mvcgen--tactic/Overview/#The-Lean-Language-Reference--The--mvcgen--tactic--Overview "17.1. Overview")[17.3. Verification Conditions→](The--mvcgen--tactic/Verification-Conditions/#The-Lean-Language-Reference--The--mvcgen--tactic--Verification-Conditions "17.3. Verification Conditions")
#  17.2. Predicate Transformers[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--mvcgen--tactic--Predicate-Transformers "Permalink")
A _predicate transformer semantics_ is an interpretation of programs as functions from predicates to predicates, rather than values to values. A _postcondition_ is an assertion that holds after running a program, while a _precondition_ is an assertion that must hold prior to running the program in order for the postcondition to be guaranteed to hold.
The predicate transformer semantics used by `[mvcgen](Tactic-Proofs/Tactic-Reference/#mvcgen "Documentation for tactic")` transforms postconditions into the _weakest preconditions_ under which the program will ensure the postcondition. An assertion `PPP` is weaker than `P′P'P′` if, in all states, `P′P'P′` suffices to prove `PPP`, but `PPP` does not suffice to prove `P′P'P′`. Logically equivalent assertions are considered to be equal.
The predicates in question are stateful: they can mention the program's current state. Furthermore, postconditions can relate the return value and any exceptions thrown by the program to the final state. `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` is a type of predicates that is parameterized over a monadic state, expressed as a list of the types of the fields that make up the state. The usual logical connectives and quantifiers are defined for `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`. Each monad that can be used with `[mvcgen](Tactic-Proofs/Tactic-Reference/#mvcgen "Documentation for tactic")` is assigned a state type by an instance of `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP")`, and `[Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion")` is the corresponding type of assertions for that monad, which is used for preconditions. `[Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion")` is a wrapper around `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`: while `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` is parameterized by a list of states types, `[Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion")` is parameterized by a more informative type that it translates to a list of state types for `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`. A `[PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond")` pairs an `[Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion")` about a return value with assertions about potential exceptions; the available exceptions are also specified by the monad's `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP")` instance.
##  17.2.1. Stateful Predicates[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--mvcgen--tactic--Predicate-Transformers--Stateful-Predicates "Permalink")
The predicate transformer semantics of monadic programs is based on a logic in which propositions may mention the program's state. Here, “state” refers not only to mutable state, but also to read-only values such as those that are provided via `[ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT")`. Different monads have different state types available, but each individual state always has a type. Given a list of state types, `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` is a type of predicates over these states.
`[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` is not inherently tied to the monadic verification framework. The related `[Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion")` computes a suitable `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` for a monad's state as expressed via its `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP")` instance's `[PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")` output parameter.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.SPred "Permalink")def
```


Std.Do.SPred.{u} (σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)) : Type u


Std.Do.SPred.{u} (σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)) :
  Type u


```

A predicate over states, where each state is defined by a list of component state types.
Example:
`[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") [[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"), [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")] = ([Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") → [ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") Prop)`
Ordinary propositions that do not mention the state can be used as stateful predicates by adding a trivial universal quantification. This is written with the syntax `⌜P⌝`, which is syntactic sugar for `[SPred.pure](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")`.
syntaxNotation for `SPred`

```
term ::= ...
    | Embedding of pure Lean values into `SVal`. An alias for `SPred.pure`. ⌜term⌝
```

Embedding of pure Lean values into `[SVal](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SVal "Documentation for Std.Do.SVal")`. An alias for `[SPred.pure](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.SPred.pure "Permalink")def
```


Std.Do.SPred.pure.{u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)} (P : Prop) : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs


Std.Do.SPred.pure.{u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)}
  (P : Prop) : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs


```

A pure proposition `P : Prop` embedded into `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`. Prefer to use notation `⌜P⌝`.
Stateful Predicates
The predicate `[ItIsSecret](The--mvcgen--tactic/Predicate-Transformers/#ItIsSecret-_LPAR_in-Stateful-Predicates_RPAR_ "Definition of example")` expresses that a state of type `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` is `"secret"`:
`def ItIsSecret : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") [[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")] := fun s => ⌜s = "secret"⌝ `
[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAZRgEwHQBEIChSVolVAFQEMBjGYMjbLCMAUwDsC1MssBnBmAfXsoQWIAG5kA5s1QB3ElCbAm4uADMSAG24dkDFXACSMfZwQMyUHnABciAAoXkcANpIoi8QF1rAXlUBXFk44bwA+OEAcYiDfACJucx5owFxiIA"\))
###  17.2.1.1. Entailment[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--mvcgen--tactic--Predicate-Transformers--Stateful-Predicates--Entailment "Permalink")
Stateful predicates are related by _entailment_. Entailment of stateful predicates is defined as universally-quantified implication: if `PPP` and `QQQ` are predicates over a state `σ\sigmaσ`, then `PPP` entails `QQQ` (written `P⊢sQP \vdash_s QP⊢s​Q`) when `∀s:σ,P(s)→Q(s)∀ s : \sigma, P(s) → Q(s)∀s:σ,P(s)→Q(s)`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.SPred.entails "Permalink")def
```


Std.Do.SPred.entails.{u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)} (P Q : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs) : Prop


Std.Do.SPred.entails.{u}
  {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)} (P Q : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs) :
  Prop


```

Entailment in `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`.
One predicate `P` entails another predicate `Q` if `Q` is true in every state in which `P` is true. Unlike implication (`[SPred.imp](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___imp "Documentation for Std.Do.SPred.imp")`), entailment is not itself an `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`, but is instead an ordinary proposition.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.SPred.bientails "Permalink")def
```


Std.Do.SPred.bientails.{u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)} (P Q : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs) : Prop


Std.Do.SPred.bientails.{u}
  {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)} (P Q : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs) :
  Prop


```

Logical equivalence of `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`.
Logically equivalent predicates are equal. Use `SPred.bientails.to_eq` to convert bi-entailment to equality.
syntaxNotation for `SPred`

```
term ::= ...
    | Entailment in `SPred`; sugar for `SPred.entails`. term ⊢ₛ term
```

Entailment in `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`; sugar for `[SPred.entails](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")`.

```
term ::= ...
    | Tautology in `SPred`; sugar for `SPred.entails ⌜True⌝`. ⊢ₛ term
```

Tautology in `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`; sugar for `[SPred.entails](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") ⌜[True](Basic-Propositions/Truth/#True___intro "Documentation for True")⌝`.

```
term ::= ...
    | Bi-entailment in `SPred`; sugar for `SPred.bientails`. term ⊣⊢ₛ term
```

Bi-entailment in `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`; sugar for `[SPred.bientails](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___bientails "Documentation for Std.Do.SPred.bientails")`.
The logic of stateful predicates includes an implication connective. The difference between entailment and implication is that entailment is a statement in Lean's logic, while implication is internal to the stateful logic. Given stateful predicates `P` and `Q` for state `σ`, `P ⊢ₛ Q` is a `Prop` while `spred(P → Q)` is an `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σ`.
###  17.2.1.2. Notation[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--mvcgen--tactic--Predicate-Transformers--Stateful-Predicates--Notation "Permalink")
The syntax of stateful predicates overlaps with that of ordinary Lean terms. In particular, stateful predicates use the usual syntax for logical connectives and quantifiers. The syntax associated with stateful predicates is automatically enabled in contexts such as pre- and postconditions where they are clearly intended; other contexts must explicitly opt in to the syntax using ``Std.Do.«termSpred(_)» : term``An embedding of the special syntax for `SPred` into ordinary terms that provides alternative interpretations of logical connectives and quantifiers.  Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax. ```spred`. The usual meanings of these operators can be recovered by using the ``Std.Do.«termTerm(_)» : term``Escapes from a surrounding `spred(...)` term, returning to the usual interpretations of quantifiers and connectives. ``[`term`](The--mvcgen--tactic/Predicate-Transformers/#Std___Do____FLQQ_termTerm_LPAR___RPAR__FLQQ_) operator.
syntaxPredicate Terms
``Std.Do.«termSpred(_)» : term``An embedding of the special syntax for `SPred` into ordinary terms that provides alternative interpretations of logical connectives and quantifiers.  Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax. ```spred` indicates that logical connectives and quantifiers should be understood as those pertaining to stateful predicates, while ``Std.Do.«termTerm(_)» : term``Escapes from a surrounding `spred(...)` term, returning to the usual interpretations of quantifiers and connectives. ``[`term`](The--mvcgen--tactic/Predicate-Transformers/#Std___Do____FLQQ_termTerm_LPAR___RPAR__FLQQ_) indicates that they should have the usual meaning.

```
term ::= ...
    | An embedding of the special syntax for `SPred` into ordinary terms that provides alternative
interpretations of logical connectives and quantifiers.

Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax.
spred(term)
```

```
term ::= ...
    | Escapes from a surrounding `spred(...)` term, returning to the usual interpretations of quantifiers
and connectives.
term(term)
```

###  17.2.1.3. Connectives and Quantifiers[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--mvcgen--tactic--Predicate-Transformers--Stateful-Predicates--Connectives-and-Quantifiers "Permalink")
syntaxPredicate Connectives

```
term ::= ...
    | An embedding of the special syntax for `SPred` into ordinary terms that provides alternative
interpretations of logical connectives and quantifiers.

Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax.
spred(`And a b`, or `a ∧ b`, is the conjunction of propositions. It can be
constructed and destructed like a pair: if `ha : a` and `hb : b` then
`⟨ha, hb⟩ : a ∧ b`, and if `h : a ∧ b` then `h.left : a` and `h.right : b`.


Conventions for notations in identifiers:

 * The recommended spelling of `∧` in identifiers is `and`.term [∧](Basic-Propositions/Logical-Connectives/#_FLQQ_term______FLQQ_-next-next-next) term)
```

Syntactic sugar for `[SPred.and](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___and "Documentation for Std.Do.SPred.and")`.

```
term ::= ...
    | An embedding of the special syntax for `SPred` into ordinary terms that provides alternative
interpretations of logical connectives and quantifiers.

Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax.
spred(`Or a b`, or `a ∨ b`, is the disjunction of propositions. There are two
constructors for `Or`, called `Or.inl : a → a ∨ b` and `Or.inr : b → a ∨ b`,
and you can use `match` or `cases` to destruct an `Or` assumption into the
two cases.


Conventions for notations in identifiers:

 * The recommended spelling of `∨` in identifiers is `or`.term [∨](Basic-Propositions/Logical-Connectives/#_FLQQ_term______FLQQ_-next-next-next-next) term)
```

Syntactic sugar for `[SPred.or](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___or "Documentation for Std.Do.SPred.or")`.

```
term ::= ...
    | An embedding of the special syntax for `SPred` into ordinary terms that provides alternative
interpretations of logical connectives and quantifiers.

Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax.
spred(`Not p`, or `¬p`, is the negation of `p`. It is defined to be `p → False`,
so if your goal is `¬p` you can use `intro h` to turn the goal into
`h : p ⊢ False`, and if you have `hn : ¬p` and `h : p` then `hn h : False`
and `(hn h).elim` will prove anything.
For more information: [Propositional Logic](https://lean-lang.org/theorem_proving_in_lean4/propositions_and_proofs.html#propositional-logic)


Conventions for notations in identifiers:

 * The recommended spelling of `¬` in identifiers is `not`.[¬](Basic-Propositions/Logical-Connectives/#_FLQQ_term_____FLQQ_) term)
```

Syntactic sugar for `[SPred.not](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___not "Documentation for Std.Do.SPred.not")`.

```
term ::= ...
    | An embedding of the special syntax for `SPred` into ordinary terms that provides alternative
interpretations of logical connectives and quantifiers.

Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax.
spred(term [→](Terms/Function-Types/#Lean___Parser___Term___arrow) term)
```

Syntactic sugar for `[SPred.imp](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___imp "Documentation for Std.Do.SPred.imp")`.

```
term ::= ...
    | An embedding of the special syntax for `SPred` into ordinary terms that provides alternative
interpretations of logical connectives and quantifiers.

Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax.
spred(If and only if, or logical bi-implication. `a ↔ b` means that `a` implies `b` and vice versa.
By `propext`, this implies that `a` and `b` are equal and hence any expression involving `a`
is equivalent to the corresponding expression with `b` instead.


Conventions for notations in identifiers:

 * The recommended spelling of `↔` in identifiers is `iff`.term [↔](Basic-Propositions/Logical-Connectives/#_FLQQ_term______FLQQ_-next-next-next-next-next) term)
```

Syntactic sugar for `[SPred.iff](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___iff "Documentation for Std.Do.SPred.iff")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.SPred.and "Permalink")def
```


Std.Do.SPred.and.{u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)} (P Q : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs) : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs


Std.Do.SPred.and.{u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)}
  (P Q : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs) : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs


```

Conjunction in `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`: states that satisfy `P` and satisfy `Q` satisfy `spred(P ∧ Q)`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.SPred.conjunction "Permalink")def
```


Std.Do.SPred.conjunction.{u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)}
  (env : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs)) : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs


Std.Do.SPred.conjunction.{u}
  {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)}
  (env : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs)) : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs


```

Conjunction of a list of stateful predicates. A state satisfies `conjunction env` if it satisfies all predicates in `env`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.SPred.or "Permalink")def
```


Std.Do.SPred.or.{u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)} (P Q : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs) : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs


Std.Do.SPred.or.{u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)}
  (P Q : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs) : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs


```

Disjunction in `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`: states that either satisfy `P` or satisfy `Q` satisfy `spred(P ∨ Q)`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.SPred.not "Permalink")def
```


Std.Do.SPred.not.{u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)} (P : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs) : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs


Std.Do.SPred.not.{u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)}
  (P : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs) : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs


```

Negation in `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`: states that do not satisfy `P` satisfy `spred(¬ P)`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.SPred.imp "Permalink")def
```


Std.Do.SPred.imp.{u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)} (P Q : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs) : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs


Std.Do.SPred.imp.{u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)}
  (P Q : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs) : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs


```

Implication in `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`: states that satisfy `Q` whenever they satisfy `P` satisfy `spred(P → Q)`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.SPred.iff "Permalink")def
```


Std.Do.SPred.iff.{u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)} (P Q : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs) : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs


Std.Do.SPred.iff.{u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)}
  (P Q : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs) : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs


```

Biimplication in `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`: states that either satisfy both `P` and `Q` or satisfy neither satisfy `spred(P ↔ Q)`.
syntaxPredicate Quantifiers

```
term ::= ...
    | An embedding of the special syntax for `SPred` into ordinary terms that provides alternative
interpretations of logical connectives and quantifiers.

Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax.
spred(∀ ident, term)
```

```
term ::= ...
    | An embedding of the special syntax for `SPred` into ordinary terms that provides alternative
interpretations of logical connectives and quantifiers.

Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax.
spred(∀ ident : term,  term)
```

```
term ::= ...
    | An embedding of the special syntax for `SPred` into ordinary terms that provides alternative
interpretations of logical connectives and quantifiers.

Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax.
spred(∀ Explicit binder, like `(x y : A)` or `(x y)`.
Default values can be specified using `(x : A := v)` syntax, and tactics using `(x : A := by tac)`.
(ident (ident | [A *hole* (or *placeholder term*), which stands for an unknown term that is expected to be inferred based on context.
For example, in `@id _ Nat.zero`, the `_` must be the type of `Nat.zero`, which is `Nat`.

The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as *unification*.

Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:
* In `match` patterns, holes are catch-all patterns.
* In some tactics, such as `refine'` and `apply`, unsolved-for placeholders become new goals.

Related concept: implicit parameters are automatically filled in with holes during the elaboration process.

See also `?m` syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole))* : term),  term)
```

```
term ::= ...
    | An embedding of the special syntax for `SPred` into ordinary terms that provides alternative
interpretations of logical connectives and quantifiers.

Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax.
spred(∀ A *hole* (or *placeholder term*), which stands for an unknown term that is expected to be inferred based on context.
For example, in `@id _ Nat.zero`, the `_` must be the type of `Nat.zero`, which is `Nat`.

The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as *unification*.

Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:
* In `match` patterns, holes are catch-all patterns.
* In some tactics, such as `refine'` and `apply`, unsolved-for placeholders become new goals.

Related concept: implicit parameters are automatically filled in with holes during the elaboration process.

See also `?m` syntax (synthetic holes).
[_](Terms/Holes/#Lean___Parser___Term___hole), term)
```

```
term ::= ...
    | An embedding of the special syntax for `SPred` into ordinary terms that provides alternative
interpretations of logical connectives and quantifiers.

Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax.
spred(∀ A *hole* (or *placeholder term*), which stands for an unknown term that is expected to be inferred based on context.
For example, in `@id _ Nat.zero`, the `_` must be the type of `Nat.zero`, which is `Nat`.

The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as *unification*.

Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:
* In `match` patterns, holes are catch-all patterns.
* In some tactics, such as `refine'` and `apply`, unsolved-for placeholders become new goals.

Related concept: implicit parameters are automatically filled in with holes during the elaboration process.

See also `?m` syntax (synthetic holes).
[_](Terms/Holes/#Lean___Parser___Term___hole) : term,  term)
```

```
term ::= ...
    | An embedding of the special syntax for `SPred` into ordinary terms that provides alternative
interpretations of logical connectives and quantifiers.

Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax.
spred(∀ Explicit binder, like `(x y : A)` or `(x y)`.
Default values can be specified using `(x : A := v)` syntax, and tactics using `(x : A := by tac)`.
(A *hole* (or *placeholder term*), which stands for an unknown term that is expected to be inferred based on context.
For example, in `@id _ Nat.zero`, the `_` must be the type of `Nat.zero`, which is `Nat`.

The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as *unification*.

Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:
* In `match` patterns, holes are catch-all patterns.
* In some tactics, such as `refine'` and `apply`, unsolved-for placeholders become new goals.

Related concept: implicit parameters are automatically filled in with holes during the elaboration process.

See also `?m` syntax (synthetic holes).
[_](Terms/Holes/#Lean___Parser___Term___hole) (ident | [A *hole* (or *placeholder term*), which stands for an unknown term that is expected to be inferred based on context.
For example, in `@id _ Nat.zero`, the `_` must be the type of `Nat.zero`, which is `Nat`.

The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as *unification*.

Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:
* In `match` patterns, holes are catch-all patterns.
* In some tactics, such as `refine'` and `apply`, unsolved-for placeholders become new goals.

Related concept: implicit parameters are automatically filled in with holes during the elaboration process.

See also `?m` syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole))* : term),  term)
```

Each form of universal quantification is syntactic sugar for an invocation of `[SPred.forall](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___forall "Documentation for Std.Do.SPred.forall")` on a function that takes the quantified variable as a parameter.

```
term ::= ...
    | An embedding of the special syntax for `SPred` into ordinary terms that provides alternative
interpretations of logical connectives and quantifiers.

Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax.
spred(∃ `binderIdent` matches an `ident` or a `_`. It is used for identifiers in binding
position, where `_` means that the value should be left unnamed and inaccessible.
ident, term)
```

```
term ::= ...
    | An embedding of the special syntax for `SPred` into ordinary terms that provides alternative
interpretations of logical connectives and quantifiers.

Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax.
spred(∃ `binderIdent` matches an `ident` or a `_`. It is used for identifiers in binding
position, where `_` means that the value should be left unnamed and inaccessible.
ident : term,  term)
```

```
term ::= ...
    | An embedding of the special syntax for `SPred` into ordinary terms that provides alternative
interpretations of logical connectives and quantifiers.

Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax.
spred(∃ (`binderIdent` matches an `ident` or a `_`. It is used for identifiers in binding
position, where `_` means that the value should be left unnamed and inaccessible.
ident `binderIdent` matches an `ident` or a `_`. It is used for identifiers in binding
position, where `_` means that the value should be left unnamed and inaccessible.
binderIdent* : term),  term)
```

```
term ::= ...
    | An embedding of the special syntax for `SPred` into ordinary terms that provides alternative
interpretations of logical connectives and quantifiers.

Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax.
spred(∃ `binderIdent` matches an `ident` or a `_`. It is used for identifiers in binding
position, where `_` means that the value should be left unnamed and inaccessible.
A *hole* (or *placeholder term*), which stands for an unknown term that is expected to be inferred based on context.
For example, in `@id _ Nat.zero`, the `_` must be the type of `Nat.zero`, which is `Nat`.

The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as *unification*.

Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:
* In `match` patterns, holes are catch-all patterns.
* In some tactics, such as `refine'` and `apply`, unsolved-for placeholders become new goals.

Related concept: implicit parameters are automatically filled in with holes during the elaboration process.

See also `?m` syntax (synthetic holes).
[_](Terms/Holes/#Lean___Parser___Term___hole), term)
```

```
term ::= ...
    | An embedding of the special syntax for `SPred` into ordinary terms that provides alternative
interpretations of logical connectives and quantifiers.

Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax.
spred(∃ `binderIdent` matches an `ident` or a `_`. It is used for identifiers in binding
position, where `_` means that the value should be left unnamed and inaccessible.
A *hole* (or *placeholder term*), which stands for an unknown term that is expected to be inferred based on context.
For example, in `@id _ Nat.zero`, the `_` must be the type of `Nat.zero`, which is `Nat`.

The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as *unification*.

Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:
* In `match` patterns, holes are catch-all patterns.
* In some tactics, such as `refine'` and `apply`, unsolved-for placeholders become new goals.

Related concept: implicit parameters are automatically filled in with holes during the elaboration process.

See also `?m` syntax (synthetic holes).
[_](Terms/Holes/#Lean___Parser___Term___hole) : term,  term)
```

```
term ::= ...
    | An embedding of the special syntax for `SPred` into ordinary terms that provides alternative
interpretations of logical connectives and quantifiers.

Within `spred(...)`, `term(...)` escapes to the ordinary Lean interpretation of this syntax.
spred(∃ (`binderIdent` matches an `ident` or a `_`. It is used for identifiers in binding
position, where `_` means that the value should be left unnamed and inaccessible.
A *hole* (or *placeholder term*), which stands for an unknown term that is expected to be inferred based on context.
For example, in `@id _ Nat.zero`, the `_` must be the type of `Nat.zero`, which is `Nat`.

The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as *unification*.

Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:
* In `match` patterns, holes are catch-all patterns.
* In some tactics, such as `refine'` and `apply`, unsolved-for placeholders become new goals.

Related concept: implicit parameters are automatically filled in with holes during the elaboration process.

See also `?m` syntax (synthetic holes).
[_](Terms/Holes/#Lean___Parser___Term___hole) `binderIdent` matches an `ident` or a `_`. It is used for identifiers in binding
position, where `_` means that the value should be left unnamed and inaccessible.
binderIdent* : term),  term)
```

Each form of existential quantification is syntactic sugar for an invocation of `[SPred.exists](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___exists "Documentation for Std.Do.SPred.exists")` on a function that takes the quantified variable as a parameter.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.SPred.forall "Permalink")def
```


Std.Do.SPred.forall.{u, v} {α : Sort u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type v)}
  (P : α → [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs) : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs


Std.Do.SPred.forall.{u, v} {α : Sort u}
  {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type v)}
  (P : α → [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs) : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs


```

Universal quantifier in `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.SPred.exists "Permalink")def
```


Std.Do.SPred.exists.{u, v} {α : Sort u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type v)}
  (P : α → [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs) : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs


Std.Do.SPred.exists.{u, v} {α : Sort u}
  {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type v)}
  (P : α → [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs) : [SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs


```

Existential quantifier in `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`.
###  17.2.1.4. Stateful Values[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--mvcgen--tactic--Predicate-Transformers--Stateful-Predicates--Stateful-Values "Permalink")
Just as `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` represents predicate over states, `[SVal](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SVal "Documentation for Std.Do.SVal")` represents a value that is derived from a state.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.SVal "Permalink")def
```


Std.Do.SVal.{u} (σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)) (α : Type u) : Type u


Std.Do.SVal.{u} (σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u))
  (α : Type u) : Type u


```

A value indexed by a curried tuple of states.
Example:

```
example : SVal [Nat, Bool] String = (Nat → Bool → String) := rfl

```

[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.SVal.getThe "Permalink")def
```


Std.Do.SVal.getThe.{u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)} (σ : Type u)
  [SVal.GetTy σ σs] : [SVal](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SVal "Documentation for Std.Do.SVal") σs σ


Std.Do.SVal.getThe.{u}
  {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)} (σ : Type u)
  [SVal.GetTy σ σs] : [SVal](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SVal "Documentation for Std.Do.SVal") σs σ


```

Gets the top-most state of type `σ` from an `[SVal](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SVal "Documentation for Std.Do.SVal")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.SVal.StateTuple "Permalink")def
```


Std.Do.SVal.StateTuple.{u} (σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)) : Type u


Std.Do.SVal.StateTuple.{u}
  (σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)) : Type u


```

A tuple capturing the whole state of an `[SVal](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SVal "Documentation for Std.Do.SVal")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.SVal.curry "Permalink")def
```


Std.Do.SVal.curry.{u} {α : Type u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)}
  (f : [SVal.StateTuple](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SVal___StateTuple "Documentation for Std.Do.SVal.StateTuple") σs → α) : [SVal](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SVal "Documentation for Std.Do.SVal") σs α


Std.Do.SVal.curry.{u} {α : Type u}
  {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)}
  (f : [SVal.StateTuple](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SVal___StateTuple "Documentation for Std.Do.SVal.StateTuple") σs → α) : [SVal](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SVal "Documentation for Std.Do.SVal") σs α


```

Curries a function taking a `StateTuple` into an `[SVal](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SVal "Documentation for Std.Do.SVal")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.SVal.uncurry "Permalink")def
```


Std.Do.SVal.uncurry.{u} {α : Type u} {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)}
  (f : [SVal](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SVal "Documentation for Std.Do.SVal") σs α) : [SVal.StateTuple](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SVal___StateTuple "Documentation for Std.Do.SVal.StateTuple") σs → α


Std.Do.SVal.uncurry.{u} {α : Type u}
  {σs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)} (f : [SVal](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SVal "Documentation for Std.Do.SVal") σs α) :
  [SVal.StateTuple](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SVal___StateTuple "Documentation for Std.Do.SVal.StateTuple") σs → α


```

Uncurries an `[SVal](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SVal "Documentation for Std.Do.SVal")` into a function taking a `StateTuple`.
##  17.2.2. Assertions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--mvcgen--tactic--Predicate-Transformers--Assertions "Permalink")
The language of assertions about monadic programs is parameterized by a _postcondition shape_ , which describes the inputs to and outputs from a computation in a given monad. Preconditions may mention the initial values of the monad's state, while postconditions may mention the returned value, the final values of the monad's state, and must furthermore account for any exceptions that could have been thrown. The postcondition shape of a given monad determines the states and exceptions in the monad. `[PostShape.pure](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape.pure")` describes a monad in which assertions may not mention any states, `[PostShape.arg](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape.arg")` describes a state value, and `[PostShape.except](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape.except")` describes a possible exception. Because these constructors can be continually added, the postcondition shape of a monad transformer can be defined in terms of the postcondition shape of the underlying transformed monad. Behind the scenes, an `[Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion")` is translated into an appropriate `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` by translating the postcondition shape into a list of state types, discarding exceptions.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.PostShape.except "Permalink")inductive type
```


Std.Do.PostShape.{u} : Type (u + 1)


Std.Do.PostShape.{u} : Type (u + 1)


```

The “shape” of the postconditions that are used to reason about a monad.
A postcondition shape is an abstraction of many possible monadic effects, based on the structure of pure functions that can simulate them. The postcondition shape of a monad is given by its `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP")` instance. This shape is used to determine both its `[Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion")`s and its `[PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond")`s.
#  Constructors

```
pure.{u} : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")
```

The assertions and postconditions in this monad use neither state nor exceptions.

```
arg.{u} (σ : Type u) : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape") → [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")
```

The assertions in this monad may mention the current value of a state of type `σ`, and postconditions may mention the state's final value.

```
except.{u} (ε : Type u) : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape") → [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")
```

The postconditions in this monad include assertions about exceptional values of type `ε` that result from premature termination.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.PostShape.args "Permalink")def
```


Std.Do.PostShape.args.{u} : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape") → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)


Std.Do.PostShape.args.{u} :
  [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape") → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (Type u)


```

Extracts the list of state types under `[PostShape.arg](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape.arg")` constructors, discarding exception types.
The state types determine the shape of assertions in the monad.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.Assertion "Permalink")def
```


Std.Do.Assertion.{u} (ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")) : Type u


Std.Do.Assertion.{u} (ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")) :
  Type u


```

An assertion about the state fields for a monad whose postcondition shape is `ps`.
Concretely, this is an abbreviation for `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` applied to the `.arg`s in the given predicate shape, so all theorems about `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` apply.
Examples:

```
example : Assertion (.arg ρ .pure) = (ρ → ULift Prop) := rfl
example : Assertion (.except ε .pure) = ULift Prop := rfl
example : Assertion (.arg σ (.except ε .pure)) = (σ → ULift Prop) := rfl
example : Assertion (.except ε (.arg σ .pure)) = (σ → ULift Prop) := rfl

```

[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.PostCond "Permalink")def
```


Std.Do.PostCond.{u} (α : Type u) (ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")) : Type u


Std.Do.PostCond.{u} (α : Type u)
  (ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")) : Type u


```

A postcondition for the given predicate shape, with one `[Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion")` for the terminating case and one `[Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion")` for each `.except` layer in the predicate shape.

```
variable (α σ ε : Type)
example : PostCond α (.arg σ .pure) = ((α → σ → ULift Prop) × PUnit) := rfl
example : PostCond α (.except ε .pure) = ((α → ULift Prop) × (ε → ULift Prop) × PUnit) := rfl
example : PostCond α (.arg σ (.except ε .pure)) = ((α → σ → ULift Prop) × (ε → ULift Prop) × PUnit) := rfl
example : PostCond α (.except ε (.arg σ .pure)) = ((α → σ → ULift Prop) × (ε → σ → ULift Prop) × PUnit) := rfl

```

syntaxPostconditions

```
term ::= ...
    | A postcondition expressing total correctness.
That is, it expresses that the asserted computation finishes without throwing an exception
*and* the result satisfies the given predicate `p`.
⇓ term* => term
```

Syntactic sugar for a nested sequence of product constructors, terminating in `()`, in which the first element is an assertion about non-exceptional return values and the remaining elements are assertions about the exceptional cases for a postcondition.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.ExceptConds "Permalink")def
```


Std.Do.ExceptConds.{u} : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape") → Type u


Std.Do.ExceptConds.{u} :
  [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape") → Type u


```

An assertion about each potential exception that's declared in a postcondition shape.
Examples:

```
example : ExceptConds (.pure) = Unit := rfl
example : ExceptConds (.except ε .pure) = ((ε → ULift Prop) × Unit) := rfl
example : ExceptConds (.arg σ (.except ε .pure)) = ((ε → ULift Prop) × Unit) := rfl
example : ExceptConds (.except ε (.arg σ .pure)) = ((ε → σ → ULift Prop) × Unit) := rfl

```

Postconditions for programs that might throw exceptions come in two varieties. The _total correctness interpretation_ `⦃P⦄ prog ⦃⇓ r => Q' r⦄` asserts that, given `P` holds, then `prog` terminates _and_ `Q'` holds for the result. The _partial correctness interpretation_ `⦃P⦄ prog ⦃⇓? r => Q' r⦄` asserts that, given `P` holds, and _if_ `prog` terminates _then_ `Q'` holds for the result.
syntaxException-Free Postconditions

```
term ::= ...
    | A postcondition expressing total correctness.
That is, it expresses that the asserted computation finishes without throwing an exception
*and* the result satisfies the given predicate `p`.
⇓ term* => term
```

A postcondition expressing total correctness. That is, it expresses that the asserted computation finishes without throwing an exception _and_ the result satisfies the given predicate `p`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.PostCond.noThrow "Permalink")def
```


Std.Do.PostCond.noThrow.{u} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α : Type u}
  (p : α → [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps) : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps


Std.Do.PostCond.noThrow.{u}
  {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α : Type u}
  (p : α → [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps) : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps


```

A postcondition expressing total correctness. That is, it expresses that the asserted computation finishes without throwing an exception _and_ the result satisfies the given predicate `p`.
syntaxPartial Postconditions

```
term ::= ...
    | A postcondition expressing partial correctness.
That is, it expresses that *if* the asserted computation finishes without throwing an exception
*then* the result satisfies the given predicate `p`.
Nothing is asserted when the computation throws an exception.
⇓? term* => term
```

A postcondition expressing partial correctness. That is, it expresses that _if_ the asserted computation finishes without throwing an exception _then_ the result satisfies the given predicate `p`. Nothing is asserted when the computation throws an exception.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.PostCond.mayThrow "Permalink")def
```


Std.Do.PostCond.mayThrow.{u} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α : Type u}
  (p : α → [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps) : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps


Std.Do.PostCond.mayThrow.{u}
  {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α : Type u}
  (p : α → [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps) : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps


```

A postcondition expressing partial correctness. That is, it expresses that _if_ the asserted computation finishes without throwing an exception _then_ the result satisfies the given predicate `p`. Nothing is asserted when the computation throws an exception.
syntaxPostcondition Entailment

```
term ::= ...
    | Entailment of postconditions.

This consists of:
 * Entailment of the assertion about the return value, for all possible return values.
 * Entailment of the exception conditions.

While implication of postconditions (`PostCond.imp`) results in a new postcondition, entailment is
an ordinary proposition.
term ⊢ₚ term
```

Syntactic sugar for `[PostCond.entails](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___entails "Documentation for Std.Do.PostCond.entails")`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.PostCond.entails "Permalink")def
```


Std.Do.PostCond.entails.{u} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α : Type u}
  (p q : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps) : Prop


Std.Do.PostCond.entails.{u}
  {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α : Type u}
  (p q : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps) : Prop


```

Entailment of postconditions.
This consists of:
  * Entailment of the assertion about the return value, for all possible return values.
  * Entailment of the exception conditions.


While implication of postconditions (`[PostCond.imp](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___imp "Documentation for Std.Do.PostCond.imp")`) results in a new postcondition, entailment is an ordinary proposition.
syntaxPostcondition Conjunction

```
term ::= ...
    | Conjunction of postconditions.

This is defined pointwise, as the conjunction of the assertions about the return value and the
conjunctions of the assertions about each potential exception.
term ∧ₚ term
```

Syntactic sugar for `[PostCond.and](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___and "Documentation for Std.Do.PostCond.and")`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.PostCond.and "Permalink")def
```


Std.Do.PostCond.and.{u} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α : Type u}
  (p q : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps) : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps


Std.Do.PostCond.and.{u} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")}
  {α : Type u} (p q : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps) :
  [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps


```

Conjunction of postconditions.
This is defined pointwise, as the conjunction of the assertions about the return value and the conjunctions of the assertions about each potential exception.
syntaxPostcondition Implication

```
term ::= ...
    | Implication of postconditions.

This is defined pointwise, as the implication of the assertions about the return value and the
implications of each of the assertions about each potential exception.

While entailment of postconditions (`PostCond.entails`) is an ordinary proposition, implication of
postconditions is itself a postcondition.
term →ₚ term
```

Syntactic sugar for `[PostCond.imp](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___imp "Documentation for Std.Do.PostCond.imp")`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.PostCond.imp "Permalink")def
```


Std.Do.PostCond.imp.{u} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α : Type u}
  (p q : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps) : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps


Std.Do.PostCond.imp.{u} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")}
  {α : Type u} (p q : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps) :
  [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps


```

Implication of postconditions.
This is defined pointwise, as the implication of the assertions about the return value and the implications of each of the assertions about each potential exception.
While entailment of postconditions (`[PostCond.entails](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___entails "Documentation for Std.Do.PostCond.entails")`) is an ordinary proposition, implication of postconditions is itself a postcondition.
##  17.2.3. Predicate Transformers[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--mvcgen--tactic--Predicate-Transformers--Predicate-Transformers "Permalink")
A predicate transformer is a function from postconditions for some postcondition state into assertions for that state. The function must be _conjunctive_ , which means it must distribute over `[PostCond.and](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___and "Documentation for Std.Do.PostCond.and")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.PredTrans.conjunctiveRaw "Permalink")structure
```


Std.Do.PredTrans.{u} (ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")) (α : Type u) : Type u


Std.Do.PredTrans.{u} (ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape"))
  (α : Type u) : Type u


```

The type of predicate transformers for a given `ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")` and return type `α : Type`. A predicate transformer `x : [PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps α` is a function that takes a postcondition `Q : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps` and returns a precondition `x.apply Q : [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps`.
#  Constructor

```
[Std.Do.PredTrans.mk](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans.mk").{u}
```

#  Fields

```
trans : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps → [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps
```

The function implementing the predicate transformer.

```
conjunctiveRaw : [PredTrans.Conjunctive](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___Conjunctive "Documentation for Std.Do.PredTrans.Conjunctive") self.[trans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans.trans")
```

The predicate transformer is conjunctive: `t (Q₁ ∧ₚ Q₂) ⊣⊢ₛ t Q₁ ∧ t Q₂`. So the stronger the postcondition, the stronger the resulting precondition.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.PredTrans.Conjunctive "Permalink")def
```


Std.Do.PredTrans.Conjunctive.{u} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α : Type u}
  (t : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps → [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps) : Prop


Std.Do.PredTrans.Conjunctive.{u}
  {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α : Type u}
  (t : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps → [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps) :
  Prop


```

Transforming a conjunction of postconditions is the same as the conjunction of transformed postconditions.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.PredTrans.Monotonic "Permalink")def
```


Std.Do.PredTrans.Monotonic.{u} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α : Type u}
  (t : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps → [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps) : Prop


Std.Do.PredTrans.Monotonic.{u}
  {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α : Type u}
  (t : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps → [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps) :
  Prop


```

The stronger the postcondition, the stronger the transformed precondition.
Predicate transformers form a monad. The `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` operator is the identity transformer; it simply instantiates the postcondition with the its argument. The `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")` operator composes predicate transformers.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.PredTrans.pure "Permalink")def
```


Std.Do.PredTrans.pure.{u} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α : Type u} (a : α) :
  [PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps α


Std.Do.PredTrans.pure.{u} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")}
  {α : Type u} (a : α) : [PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps α


```

The identity predicate transformer that transforms the postcondition's assertion about the return value into an assertion about `a`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.PredTrans.bind "Permalink")def
```


Std.Do.PredTrans.bind.{u} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α β : Type u}
  (x : [PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps α) (f : α → [PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps β) : [PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps β


Std.Do.PredTrans.bind.{u} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")}
  {α β : Type u} (x : [PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps α)
  (f : α → [PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps β) :
  [PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps β


```

Sequences two predicate transformers by composing them.
The helper operators `[PredTrans.pushArg](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___pushArg "Documentation for Std.Do.PredTrans.pushArg")`, `[PredTrans.pushExcept](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___pushExcept "Documentation for Std.Do.PredTrans.pushExcept")`, and `[PredTrans.pushOption](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___pushOption "Documentation for Std.Do.PredTrans.pushOption")` modify a predicate transformer by adding a standard side effect. They are used to implement the `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP")` instances for transformers such as `[StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT")`, `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT")`, and `[OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT")`; they can also be used to implement monads that can be thought of in terms of one of these. For example, `[PredTrans.pushArg](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___pushArg "Documentation for Std.Do.PredTrans.pushArg")` is typically used for state monads, but can also be used to implement a reader monad's instance, treating the reader's value as read-only state.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.PredTrans.pushArg "Permalink")def
```


Std.Do.PredTrans.pushArg.{u} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α σ : Type u}
  (x : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ ([PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps) α) : [PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ([PostShape.arg](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape.arg") σ ps) α


Std.Do.PredTrans.pushArg.{u}
  {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α σ : Type u}
  (x : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ ([PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps) α) :
  [PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ([PostShape.arg](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape.arg") σ ps) α


```

Adds the ability to make assertions about a state of type `σ` to a predicate transformer with postcondition shape `ps`, resulting in postcondition shape `.arg σ ps`. This is done by interpreting `[StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ ([PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps) α` into `[PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ([.arg](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape.arg") σ ps) α`.
This can be used to for all kinds of state-like effects, including reader effects or append-only states, by interpreting them as states.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.PredTrans.pushExcept "Permalink")def
```


Std.Do.PredTrans.pushExcept.{u_1} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α ε : Type u_1}
  (x : [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε ([PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps) α) : [PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ([PostShape.except](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape.except") ε ps) α


Std.Do.PredTrans.pushExcept.{u_1}
  {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α ε : Type u_1}
  (x : [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε ([PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps) α) :
  [PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ([PostShape.except](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape.except") ε ps) α


```

Adds the ability to make assertions about exceptions of type `ε` to a predicate transformer with postcondition shape `ps`, resulting in postcondition shape `.except ε ps`. This is done by interpreting `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε ([PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps) α` into `[PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ([.except](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape.except") ε ps) α`.
This can be used for all kinds of exception-like effects, such as early termination, by interpreting them as exceptions.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.PredTrans.pushOption "Permalink")def
```


Std.Do.PredTrans.pushOption.{u_1} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α : Type u_1}
  (x : [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") ([PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps) α) :
  [PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ([PostShape.except](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape.except") [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit") ps) α


Std.Do.PredTrans.pushOption.{u_1}
  {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α : Type u_1}
  (x : [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") ([PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps) α) :
  [PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ([PostShape.except](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape.except") [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit") ps) α


```

Adds the ability to make assertions about early termination to a predicate transformer with postcondition shape `ps`, resulting in postcondition shape `.except PUnit ps`. This is done by interpreting `[OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") ([PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps) α` into `[PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ([.except](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape.except") [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit") ps) α`, which models the type `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` as being equivalent to `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")`.
###  17.2.3.1. Weakest Preconditions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--mvcgen--tactic--Predicate-Transformers--Predicate-Transformers--Weakest-Preconditions "Permalink")
The [weakest precondition](The--mvcgen--tactic/Predicate-Transformers/#--tech-term-weakest-preconditions) semantics of a monad are provided by the `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP")` type class. Instances of `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP")` determine the monad's postcondition shape and provide the logical rules for interpreting the monad's operations as a predicate transformer in its postcondition shape.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.WP "Permalink")type class
```


Std.Do.WP.{u, v} (m : Type u → Type v) (ps : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")) :
  Type (max (u + 1) v)


Std.Do.WP.{u, v} (m : Type u → Type v)
  (ps : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")) :
  Type (max (u + 1) v)


```

A weakest precondition interpretation of a monadic program `x : m α` in terms of a predicate transformer `[PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps α`. The monad `m` determines `ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")`.
For practical reasoning, an instance of `[WPMonad](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WPMonad___mk "Documentation for Std.Do.WPMonad") m ps` is typically needed in addition to `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps`.
#  Instance Constructor

```
[Std.Do.WP.mk](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP.mk").{u, v}
```

#  Methods

```
wp : {α : Type u} → m α → [PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps α
```

Interpret a monadic program `x : m α` in terms of a predicate transformer `[PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps α`.
syntaxWeakest Preconditions

```
term ::= ...
    | `wp⟦x⟧ Q` is defined as `(WP.wp x).apply Q`. wp⟦term (: term)?⟧
```

`wp⟦x⟧ Q` is defined as `(WP.wp x).apply Q`.
###  17.2.3.2. Weakest Precondition Monad Morphisms[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--mvcgen--tactic--Predicate-Transformers--Predicate-Transformers--Weakest-Precondition-Monad-Morphisms "Permalink")
Most of the built-in specification lemmas for `[mvcgen](Tactic-Proofs/Tactic-Reference/#mvcgen "Documentation for tactic")` relies on the presence of a `[WPMonad](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WPMonad___mk "Documentation for Std.Do.WPMonad")` instance, in addition to the `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP")` instance. In addition to being lawful, weakest preconditions of the monad's implementations of `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` and `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")` should correspond to the `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` and `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")` operators for the predicate transformer monad. Without a `[WPMonad](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WPMonad___mk "Documentation for Std.Do.WPMonad")` instance, `[mvcgen](Tactic-Proofs/Tactic-Reference/#mvcgen "Documentation for tactic")` typically returns the original proof goal unchanged.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.WPMonad "Permalink")type class
```


Std.Do.WPMonad.{u, v} (m : Type u → Type v) (ps : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape"))
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] : Type (max (u + 1) v)


Std.Do.WPMonad.{u, v}
  (m : Type u → Type v)
  (ps : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")) [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] :
  Type (max (u + 1) v)


```

A monad with weakest preconditions (`[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP")`) that is also a monad morphism, preserving `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` and `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")`.
In practice, `mvcgen` is not useful for reasoning about programs in a monad that is without a `[WPMonad](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WPMonad___mk "Documentation for Std.Do.WPMonad")` instance. The specification lemmas for `[Pure.pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` and `[Bind.bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")`, as well as those for operators like `[Functor.map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map")`, require that their monad have a `[WPMonad](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WPMonad___mk "Documentation for Std.Do.WPMonad")` instance.
#  Instance Constructor

```
[Std.Do.WPMonad.mk](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WPMonad___mk "Documentation for Std.Do.WPMonad.mk").{u, v}
```

#  Extends
  * `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") m`
  * `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps`


#  Methods

```
map_const : ∀ {α β : Type u}, [Functor.mapConst](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.mapConst") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Functor.map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") [∘](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [Function.const](The-Type-System/Functions/#Function___const "Documentation for Function.const") β
```

Inherited from 
  1. `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") m`
  2. `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps`



```
id_map : ∀ {α : Type u} (x : m α), id [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x
```

Inherited from 
  1. `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") m`
  2. `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps`



```
comp_map : ∀ {α β γ : Type u} (g : α → β) (h : β → γ) (x : m α), [(](The-Type-System/Functions/#Function___comp "Documentation for Function.comp")h [∘](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") g[)](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") h [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") g [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x
```

Inherited from 
  1. `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") m`
  2. `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps`



```
seqLeft_eq : ∀ {α β : Type u} (x : m α) (y : m β), x <* y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Function.const](The-Type-System/Functions/#Function___const "Documentation for Function.const") β [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x <*> y
```

Inherited from 
  1. `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") m`
  2. `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps`



```
seqRight_eq : ∀ {α β : Type u} (x : m α) (y : m β), x *> y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Function.const](The-Type-System/Functions/#Function___const "Documentation for Function.const") α id [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x <*> y
```

Inherited from 
  1. `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") m`
  2. `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps`



```
pure_seq : ∀ {α β : Type u} (g : α → β) (x : m α), [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") g <*> x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x
```

Inherited from 
  1. `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") m`
  2. `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps`



```
map_pure : ∀ {α β : Type u} (g : α → β) (x : α), g [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") (g x)
```

Inherited from 
  1. `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") m`
  2. `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps`



```
seq_pure : ∀ {α β : Type u} (g : m (α → β)) (x : α), g <*> [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") (fun h => h x) [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") g
```

Inherited from 
  1. `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") m`
  2. `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps`



```
seq_assoc : ∀ {α β γ : Type u} (x : m α) (g : m (α → β)) (h : m (β → γ)), h <*> (g <*> x) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Function.comp](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") h <*> g <*> x
```

Inherited from 
  1. `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") m`
  2. `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps`



```
bind_pure_comp : ∀ {α β : Type u} (f : α → β) (x : m α),
  (do
      let a ← x
      [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") (f a)) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
    f [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x
```

Inherited from 
  1. `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") m`
  2. `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps`



```
bind_map : ∀ {α β : Type u} (f : m (α → β)) (x : m α),
  (do
      let x_1 ← f
      x_1 [<$>](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") x) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
    f <*> x
```

Inherited from 
  1. `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") m`
  2. `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps`



```
pure_bind : ∀ {α β : Type u} (x : α) (f : α → m β), [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") f [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f x
```

Inherited from 
  1. `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") m`
  2. `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps`



```
bind_assoc : ∀ {α β γ : Type u} (x : m α) (f : α → m β) (g : β → m γ), x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") f [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") g [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") fun x => f x [>>=](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") g
```

Inherited from 
  1. `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") m`
  2. `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps`



```
wp : {α : Type u} → m α → [PredTrans](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___mk "Documentation for Std.Do.PredTrans") ps α
```

Inherited from 
  1. `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") m`
  2. `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps`



```
wp_pure : ∀ {α : Type u} (a : α), [wp](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP.wp") ([pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") a) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") a
```

`[WP.wp](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP.wp")` preserves `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")`.

```
wp_bind : ∀ {α β : Type u} (x : m α) (f : α → m β),
  ([wp](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP.wp") do
      let a ← x
      f a) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
    do
    let a ← [wp](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP.wp") x
    [wp](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP.wp") (f a)
```

`[WP.wp](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP.wp")` preserves `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")`.
Missing `WPMonad` Instance
This reimplementation of `[Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")` has a `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP")` instance, but no `[WPMonad](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WPMonad___mk "Documentation for Std.Do.WPMonad")` instance:
`def Identity (α : Type u) : Type u := α  [variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax") {α : Type u}  def Identity.run (act : [Identity](The--mvcgen--tactic/Predicate-Transformers/#Identity-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") α) : α := act  instance : [Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") [Identity](The--mvcgen--tactic/Predicate-Transformers/#Identity-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") where   [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x := x   [bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") x f := f x  instance : [WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") [Identity](The--mvcgen--tactic/Predicate-Transformers/#Identity-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") [.pure](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape.pure") where   [wp](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP.wp") x := [PredTrans.pure](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PredTrans___pure "Documentation for Std.Do.PredTrans.pure") x  theorem Identity.of_wp_run_eq {x : α} {prog : [Identity](The--mvcgen--tactic/Predicate-Transformers/#Identity-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") α}     (h : [Identity.run](The--mvcgen--tactic/Predicate-Transformers/#Identity___run-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") prog = x) (P : α → Prop) :     (⊢ₛ [wp⟦](The--mvcgen--tactic/Predicate-Transformers/#Std___Do____FLQQ_termWp____________FLQQ_ "Documentation for syntax")prog⟧ (⇓ a => ⟨P a⟩)) → P x := byα:Type ux:αprog:[Identity](The--mvcgen--tactic/Predicate-Transformers/#Identity-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") αh:prog.[run](The--mvcgen--tactic/Predicate-Transformers/#Identity___run-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") xP:α → Prop⊢ [(](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")[⊢ₛ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") wp⟦prog⟧ ([PostCond.noThrow](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___noThrow "Documentation for Std.Do.PostCond.noThrow") fun a => [{](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") [down](The-Type-System/Universes/#ULift___up "Documentation for ULift.down") [:=](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") P a [}](The-Type-System/Universes/#ULift___up "Documentation for ULift.up"))[)](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") → P x   [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") h'α:Type ux:αprog:[Identity](The--mvcgen--tactic/Predicate-Transformers/#Identity-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") αh:prog.[run](The--mvcgen--tactic/Predicate-Transformers/#Identity___run-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") xP:α → Proph':[⊢ₛ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") wp⟦prog⟧ ([PostCond.noThrow](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___noThrow "Documentation for Std.Do.PostCond.noThrow") fun a => [{](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") [down](The-Type-System/Universes/#ULift___up "Documentation for ULift.down") [:=](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") P a [}](The-Type-System/Universes/#ULift___up "Documentation for ULift.up"))⊢ P x   [simpa](Tactic-Proofs/Tactic-Reference/#simpa "Documentation for tactic") [← h] using h'All goals completed! 🐙 `
The missing instance prevents `[mvcgen](Tactic-Proofs/Tactic-Reference/#mvcgen "Documentation for tactic")` from using its specifications for `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` and `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")`. This tends to show up as a verification condition that's equal to the original goal. This function that reverses a list:
`def rev (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Identity](The--mvcgen--tactic/Predicate-Transformers/#Identity-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let mut out := []   for x in xs do     out := x :: out   return out `
It is correct if it is equal to `[List.reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse")`. However, `[mvcgen](Tactic-Proofs/Tactic-Reference/#mvcgen "Documentation for tactic")` does not make the goal easier to prove:
`theorem rev_correct :     ([rev](The--mvcgen--tactic/Predicate-Transformers/#rev-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") xs).[run](The--mvcgen--tactic/Predicate-Transformers/#Identity___run-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") = xs.[reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse") := `unsolved goals vc1.aα✝:Type u_1xs x:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝h:([rev](The--mvcgen--tactic/Predicate-Transformers/#rev-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") xs).[run](The--mvcgen--tactic/Predicate-Transformers/#Identity___run-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") xout✝:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝ := [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")⊢ (wp⟦do       let r ←         [forIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn.forIn") xs out✝ fun x r => do             [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") [PUnit.unit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit.unit")             [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ([ForInStep.yield](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep.yield") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") r[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons"))       [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") r⟧     ([PostCond.noThrow](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___noThrow "Documentation for Std.Do.PostCond.noThrow") fun a => [{](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") [down](The-Type-System/Universes/#ULift___up "Documentation for ULift.down") [:=](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") xs.[reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse") [}](The-Type-System/Universes/#ULift___up "Documentation for ULift.up"))).[down](The-Type-System/Universes/#ULift___up "Documentation for ULift.down")`byα✝:Type u_1xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝⊢ ([rev](The--mvcgen--tactic/Predicate-Transformers/#rev-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") xs).[run](The--mvcgen--tactic/Predicate-Transformers/#Identity___run-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") xs.[reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse") [generalize](Tactic-Proofs/Tactic-Reference/#generalize "Documentation for tactic") h : ([rev](The--mvcgen--tactic/Predicate-Transformers/#rev-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") xs).[run](The--mvcgen--tactic/Predicate-Transformers/#Identity___run-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") = xα✝:Type u_1xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝x:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝h:([rev](The--mvcgen--tactic/Predicate-Transformers/#rev-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") xs).[run](The--mvcgen--tactic/Predicate-Transformers/#Identity___run-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x⊢ x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") xs.[reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse") [apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") [Identity.of_wp_run_eq](The--mvcgen--tactic/Predicate-Transformers/#Identity___of_wp_run_eq-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") haα✝:Type u_1xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝x:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝h:([rev](The--mvcgen--tactic/Predicate-Transformers/#rev-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") xs).[run](The--mvcgen--tactic/Predicate-Transformers/#Identity___run-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x⊢ [⊢ₛ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") wp⟦[rev](The--mvcgen--tactic/Predicate-Transformers/#rev-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") xs⟧ ([PostCond.noThrow](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___noThrow "Documentation for Std.Do.PostCond.noThrow") fun a => [{](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") [down](The-Type-System/Universes/#ULift___up "Documentation for ULift.down") [:=](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") xs.[reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse") [}](The-Type-System/Universes/#ULift___up "Documentation for ULift.up")) mvcgen [[rev](The--mvcgen--tactic/Predicate-Transformers/#rev-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example")]vc1.aα✝:Type u_1xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝x:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝h:([rev](The--mvcgen--tactic/Predicate-Transformers/#rev-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") xs).[run](The--mvcgen--tactic/Predicate-Transformers/#Identity___run-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") xout✝:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝ := [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")⊢ (wp⟦do let r ← [forIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn.forIn") xs out✝ fun x r => do [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") [PUnit.unit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit.unit") [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ([ForInStep.yield](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep.yield") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") r[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")) [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") r⟧ ([PostCond.noThrow](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___noThrow "Documentation for Std.Do.PostCond.noThrow") fun a => [{](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") [down](The-Type-System/Universes/#ULift___up "Documentation for ULift.down") [:=](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") xs.[reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse") [}](The-Type-System/Universes/#ULift___up "Documentation for ULift.up"))).[down](The-Type-System/Universes/#ULift___up "Documentation for ULift.down") `
```
unsolved goals
vc1.aα✝:Type u_1xs x:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝h:([rev](The--mvcgen--tactic/Predicate-Transformers/#rev-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") xs).[run](The--mvcgen--tactic/Predicate-Transformers/#Identity___run-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") xout✝:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝ := [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")⊢ (wp⟦do
      let r ←
        [forIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn.forIn") xs out✝ fun x r => do
            [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") [PUnit.unit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit.unit")
            [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ([ForInStep.yield](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep.yield") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") r[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons"))
      [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") r⟧
    ([PostCond.noThrow](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___noThrow "Documentation for Std.Do.PostCond.noThrow") fun a => [{](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") [down](The-Type-System/Universes/#ULift___up "Documentation for ULift.down") [:=](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") xs.[reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse") [}](The-Type-System/Universes/#ULift___up "Documentation for ULift.up"))).[down](The-Type-System/Universes/#ULift___up "Documentation for ULift.down")
```

When the verification condition is just the original problem, without even any simplification of `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")`, the problem is usually a missing `[WPMonad](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WPMonad___mk "Documentation for Std.Do.WPMonad")` instance. The issue can be resolved by adding a suitable instance:
`instance : [WPMonad](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WPMonad___mk "Documentation for Std.Do.WPMonad") [Identity](The--mvcgen--tactic/Predicate-Transformers/#Identity-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") [.pure](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape.pure") where   wp_pure _ := [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")   wp_bind _ _ := [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
With this instance, and a suitable invariant, `[mvcgen](Tactic-Proofs/Tactic-Reference/#mvcgen "Documentation for tactic")` and `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` can prove the theorem.
`theorem rev_correct :     ([rev](The--mvcgen--tactic/Predicate-Transformers/#rev-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") xs).[run](The--mvcgen--tactic/Predicate-Transformers/#Identity___run-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") = xs.[reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse") := byα✝:Type u_1xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝⊢ ([rev](The--mvcgen--tactic/Predicate-Transformers/#rev-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") xs).[run](The--mvcgen--tactic/Predicate-Transformers/#Identity___run-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") xs.[reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse")   [generalize](Tactic-Proofs/Tactic-Reference/#generalize "Documentation for tactic") h : ([rev](The--mvcgen--tactic/Predicate-Transformers/#rev-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") xs).[run](The--mvcgen--tactic/Predicate-Transformers/#Identity___run-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") = xα✝:Type u_1xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝x:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝h:([rev](The--mvcgen--tactic/Predicate-Transformers/#rev-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") xs).[run](The--mvcgen--tactic/Predicate-Transformers/#Identity___run-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x⊢ x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") xs.[reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse")   [apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") [Identity.of_wp_run_eq](The--mvcgen--tactic/Predicate-Transformers/#Identity___of_wp_run_eq-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") haα✝:Type u_1xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝x:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝h:([rev](The--mvcgen--tactic/Predicate-Transformers/#rev-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") xs).[run](The--mvcgen--tactic/Predicate-Transformers/#Identity___run-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x⊢ [⊢ₛ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") wp⟦[rev](The--mvcgen--tactic/Predicate-Transformers/#rev-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") xs⟧ ([PostCond.noThrow](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___noThrow "Documentation for Std.Do.PostCond.noThrow") fun a => [{](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") [down](The-Type-System/Universes/#ULift___up "Documentation for ULift.down") [:=](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") xs.[reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse") [}](The-Type-System/Universes/#ULift___up "Documentation for ULift.up"))   [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") only [[rev](The--mvcgen--tactic/Predicate-Transformers/#rev-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example")]aα✝:Type u_1xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝x:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝h:([rev](The--mvcgen--tactic/Predicate-Transformers/#rev-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") xs).[run](The--mvcgen--tactic/Predicate-Transformers/#Identity___run-_LPAR_in-Missing--WPMonad--Instance_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x⊢ [⊢ₛ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")   wp⟦do       let r ←         [forIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn.forIn") xs [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil") fun x r => do             [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") [PUnit.unit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit.unit")             [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ([ForInStep.yield](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep.yield") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") r[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons"))       [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") r⟧     ([PostCond.noThrow](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___noThrow "Documentation for Std.Do.PostCond.noThrow") fun a => [{](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") [down](The-Type-System/Universes/#ULift___up "Documentation for ULift.down") [:=](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") xs.[reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse") [}](The-Type-System/Universes/#ULift___up "Documentation for ULift.up"))   mvcgen invariants   · ⇓⟨xs, out⟩ =>     ⌜out = xs.[prefix](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor.prefix").[reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse")⌝   with [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAZRgEwHQBEIChSVolVAFQEMBjGYMjbLCMAUwDsC1MssBnBmAfXsoQWIAG5kA5s1QB3ElCbAm4uADMSAG24dkDFXACSOppRgBPOAApAjcBwAXHCKnGcAK4BKOw6cNXdgLxwVhwicsAkAEbqPgDeNvaOzi4Avtq6BkYmpqhQLiwW5PD2hsyZgR72cQEFHIqcMCRMZD72ALJCJMjpJcBmcNIAFgxQDFhwcGAuw3AAHv4zo3Dhip2zerYBetM1THUNTZ4A6gAKXcY95qgTUwNDI2PSYDNzR8PIRFANnJeTPltYMINoAwQKdMqgICpeA9eDkmLwGABHODRWYVJLIsBQCDKIoZc6BFJjMYWfqeYpnMzZXLjLHKALTDwWE4VOCAJMI4C96OUFsTAEVEgGyCPpgQBn5JjsYBz8ksgGXCOAkOB+AB8cEAF+QnEiAS/I3B52SdUQFwqYFooYFi4P0AOQLTi4OUAbUACYRmgC6rmtSjNlpwO3qjWacAAMiRpCoXOo2kwOqD8esFoHg6Hwx1UCAANbmqNmHmWYDIXggEiPdaqam8eVKqAqdRuLMWK4MXhLJidIshlil0uKuAVqs1xu5kicTgQMhzVtwdvjstdyvVrA6PTDESWaacTz+4B1MpkvG9CzrzdWcoBZDYMZReAgFzwCBXua2p0LFTQJ6KGark9Zm+Fel2exfhbDDAkwsP+Xq7L6hxHImnTkqU3zXIMwwLNCdaTkW3bIWADbLJOpboZWHAAgwQIgouvBkNAwwUHYNaLm+bhUiw9JfIuQzcHMBoLJITBDBowAAF4+KS9gWHRK4MbC8rzGMBZgOo5iwec4KQtCsLwki/RWrgcBCPJcC2ouD5jKIEjMHAighFAYTGJwCwAO1wFKyorgANDpV7qmWWaADjEX5SSulzDCowDTNkDAiGxDCALjEyE9KS4hWU2QA"\))
###  17.2.3.3. Adequacy Lemmas[🔗](find/?domain=Verso.Genre.Manual.section&name=mvcgen-adequacy "Permalink")
Monads that can be invoked from pure code typically provide a invocation operator that takes any required input state as a parameter and returns either a value paired with an output state or some kind of exceptional value. Examples include `[StateT.run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT___run "Documentation for StateT.run")`, `[ExceptT.run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT___run "Documentation for ExceptT.run")`, and `[Id.run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id___run "Documentation for Id.run")`. _Adequacy lemmas_ provide a bridge between statements about invocations of monadic programs and those programs' [weakest precondition](The--mvcgen--tactic/Predicate-Transformers/#--tech-term-weakest-preconditions) semantics as given by their `[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP")` instances. They show that a property about the invocation is true if its weakest precondition is true.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.Id.of_wp_run_eq "Permalink")theorem
```


Std.Do.Id.of_wp_run_eq.{u} {α : Type u} {x : α} {prog : [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") α}
  (h : prog.[run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id___run "Documentation for Id.run") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x) (P : α → Prop) :
  [(](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")[⊢ₛ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") wp⟦prog⟧ ([PostCond.noThrow](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___noThrow "Documentation for Std.Do.PostCond.noThrow") fun a => [{](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") [down](The-Type-System/Universes/#ULift___up "Documentation for ULift.down") [:=](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") P a [}](The-Type-System/Universes/#ULift___up "Documentation for ULift.up"))[)](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") → P x


Std.Do.Id.of_wp_run_eq.{u} {α : Type u}
  {x : α} {prog : [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") α} (h : prog.[run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id___run "Documentation for Id.run") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x)
  (P : α → Prop) :
  [(](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")[⊢ₛ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")
      wp⟦prog⟧
        ([PostCond.noThrow](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___noThrow "Documentation for Std.Do.PostCond.noThrow") fun a =>
          [{](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") [down](The-Type-System/Universes/#ULift___up "Documentation for ULift.down") [:=](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") P a [}](The-Type-System/Universes/#ULift___up "Documentation for ULift.up"))[)](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") →
    P x


```

Adequacy lemma for `[Id.run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id___run "Documentation for Id.run")`. Useful if you want to prove a property about an expression `x` defined as `[Id.run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id___run "Documentation for Id.run") prog` and you want to use `mvcgen` to reason about `prog`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.StateM.of_wp_run_eq "Permalink")theorem
```


Std.Do.StateM.of_wp_run_eq.{u_1} {σ : Type u_1} {s : σ} {α : Type u_1}
  {x : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ} {prog : [StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") σ α} (h : [StateT.run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT___run "Documentation for StateT.run") prog s [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x)
  (P : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ → Prop) :
  [(](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")[⊢ₛ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") wp⟦prog⟧ ([PostCond.noThrow](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___noThrow "Documentation for Std.Do.PostCond.noThrow") fun a s' => [⌜](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")P [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")a[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") s'[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[⌝](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")) s[)](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") → P x


Std.Do.StateM.of_wp_run_eq.{u_1}
  {σ : Type u_1} {s : σ} {α : Type u_1}
  {x : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ} {prog : [StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") σ α}
  (h : [StateT.run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT___run "Documentation for StateT.run") prog s [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x)
  (P : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ → Prop) :
  [(](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")[⊢ₛ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")
      wp⟦prog⟧
        ([PostCond.noThrow](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___noThrow "Documentation for Std.Do.PostCond.noThrow") fun a s' =>
          [⌜](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")P [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")a[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") s'[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[⌝](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure"))
        s[)](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") →
    P x


```

Adequacy lemma for `[StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM").run`. Useful if you want to prove a property about an expression `x` defined as `[StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM").run prog s` and you want to use `mvcgen` to reason about `prog`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.StateM.of_wp_run'_eq "Permalink")theorem
```


Std.Do.StateM.of_wp_run'_eq.{u_1} {σ : Type u_1} {s : σ} {α : Type u_1}
  {x : α} {prog : [StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") σ α} (h : [StateT.run'](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT___run___ "Documentation for StateT.run'") prog s [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x)
  (P : α → Prop) :
  [(](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")[⊢ₛ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") wp⟦prog⟧ ([PostCond.noThrow](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___noThrow "Documentation for Std.Do.PostCond.noThrow") fun a => [⌜](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")P a[⌝](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")) s[)](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") → P x


Std.Do.StateM.of_wp_run'_eq.{u_1}
  {σ : Type u_1} {s : σ} {α : Type u_1}
  {x : α} {prog : [StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") σ α}
  (h : [StateT.run'](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT___run___ "Documentation for StateT.run'") prog s [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x)
  (P : α → Prop) :
  [(](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")[⊢ₛ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")
      wp⟦prog⟧
        ([PostCond.noThrow](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___noThrow "Documentation for Std.Do.PostCond.noThrow") fun a => [⌜](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")P a[⌝](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure"))
        s[)](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") →
    P x


```

Adequacy lemma for `[StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM").run'`. Useful if you want to prove a property about an expression `x` defined as `[StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM").run' prog s` and you want to use `mvcgen` to reason about `prog`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.ReaderM.of_wp_run_eq "Permalink")theorem
```


Std.Do.ReaderM.of_wp_run_eq.{u_1} {ρ : Type u_1} {r : ρ} {α : Type u_1}
  {x : α} {prog : [ReaderM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderM "Documentation for ReaderM") ρ α} (h : [ReaderT.run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT___run "Documentation for ReaderT.run") prog r [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x)
  (P : α → Prop) :
  [(](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")[⊢ₛ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") wp⟦prog⟧ ([PostCond.noThrow](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___noThrow "Documentation for Std.Do.PostCond.noThrow") fun a x => [⌜](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")P a[⌝](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")) r[)](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") → P x


Std.Do.ReaderM.of_wp_run_eq.{u_1}
  {ρ : Type u_1} {r : ρ} {α : Type u_1}
  {x : α} {prog : [ReaderM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderM "Documentation for ReaderM") ρ α}
  (h : [ReaderT.run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT___run "Documentation for ReaderT.run") prog r [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x)
  (P : α → Prop) :
  [(](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")[⊢ₛ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")
      wp⟦prog⟧
        ([PostCond.noThrow](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___noThrow "Documentation for Std.Do.PostCond.noThrow") fun a x =>
          [⌜](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")P a[⌝](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure"))
        r[)](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") →
    P x


```

Adequacy lemma for `[ReaderM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderM "Documentation for ReaderM").run`. Useful if you want to prove a property about an expression `x` defined as `[ReaderM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderM "Documentation for ReaderM").run prog r` and you want to use `mvcgen` to reason about `prog`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.Except.of_wp_eq "Permalink")theorem
```


Std.Do.Except.of_wp_eq.{u} {ε α : Type u} {x prog : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α}
  (h : prog [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x) (P : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α → Prop) :
  [(](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")[⊢ₛ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")
      wp⟦prog⟧
        [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fun a => [⌜](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")P ([Except.ok](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.ok") a)[⌝](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") fun e => [⌜](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")P ([Except.error](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.error") e)[⌝](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")
          [PUnit.unit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit.unit")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[)](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") →
    P x


Std.Do.Except.of_wp_eq.{u} {ε α : Type u}
  {x prog : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α} (h : prog [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x)
  (P : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α → Prop) :
  [(](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")[⊢ₛ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")
      wp⟦prog⟧
        [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fun a => [⌜](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")P ([Except.ok](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.ok") a)[⌝](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")
          fun e => [⌜](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")P ([Except.error](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.error") e)[⌝](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")
          [PUnit.unit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit.unit")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[)](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") →
    P x


```

Adequacy lemma for `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except")`. Useful if you want to prove a property about a complex expression `prog : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α` that you have generalized to a variable `x` and you want to use `mvcgen` to reason about `prog`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.EStateM.of_wp_run_eq "Permalink")theorem
```


Std.Do.EStateM.of_wp_run_eq.{u_1} {ε σ : Type u_1} {s : σ}
  {α : Type u_1} {x : [EStateM.Result](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Result___ok "Documentation for EStateM.Result") ε σ α} {prog : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α}
  (h : prog.[run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___run "Documentation for EStateM.run") s [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x) (P : [EStateM.Result](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Result___ok "Documentation for EStateM.Result") ε σ α → Prop) :
  [(](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")[⊢ₛ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")
      wp⟦prog⟧
        [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fun a s' => [⌜](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")P ([EStateM.Result.ok](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Result___ok "Documentation for EStateM.Result.ok") a s')[⌝](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") fun e s' =>
          [⌜](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")P ([EStateM.Result.error](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Result___ok "Documentation for EStateM.Result.error") e s')[⌝](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [PUnit.unit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit.unit")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")
        s[)](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") →
    P x


Std.Do.EStateM.of_wp_run_eq.{u_1}
  {ε σ : Type u_1} {s : σ} {α : Type u_1}
  {x : [EStateM.Result](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Result___ok "Documentation for EStateM.Result") ε σ α}
  {prog : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α}
  (h : prog.[run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___run "Documentation for EStateM.run") s [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x)
  (P : [EStateM.Result](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Result___ok "Documentation for EStateM.Result") ε σ α → Prop) :
  [(](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")[⊢ₛ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails")
      wp⟦prog⟧
        [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fun a s' =>
          [⌜](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")P ([EStateM.Result.ok](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Result___ok "Documentation for EStateM.Result.ok") a s')[⌝](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")
          fun e s' =>
          [⌜](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")P ([EStateM.Result.error](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Result___ok "Documentation for EStateM.Result.error") e s')[⌝](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")
          [PUnit.unit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit.unit")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")
        s[)](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___entails "Documentation for Std.Do.SPred.entails") →
    P x


```

Adequacy lemma for `[EStateM.run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___run "Documentation for EStateM.run")`. Useful if you want to prove a property about an expression `x` defined as `[EStateM.run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___run "Documentation for EStateM.run") prog s` and you want to use `mvcgen` to reason about `prog`.
##  17.2.4. Hoare Triples[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--mvcgen--tactic--Predicate-Transformers--Hoare-Triples "Permalink")
A _Hoare triple_ (Hoare, 1969)C. A. R. Hoare (1969). “An Axiomatic Basis for Computer Programming”. _Communications of the ACM._ **12**(10), pp. 576–583. consists of a precondition, a program, and a postcondition. Running the program in a state for which the precondition is true results in a state where the postcondition is true.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.Triple "Permalink")def
```


Std.Do.Triple.{u, v} {m : Type u → Type v} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} [[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps]
  {α : Type u} (x : m α) (P : [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps) (Q : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps) : Prop


Std.Do.Triple.{u, v} {m : Type u → Type v}
  {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} [[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps] {α : Type u}
  (x : m α) (P : [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps)
  (Q : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps) : Prop


```

A Hoare triple for reasoning about monadic programs. A Hoare triple `[Triple](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") x P Q` is a _specification_ for `x`: if assertion `P` holds before `x`, then postcondition `Q` holds after running `x`.
`⦃P⦄ x ⦃Q⦄` is convenient syntax for `[Triple](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") x P Q`.
syntaxHoare Triples

```
term ::= ...
    | A Hoare triple for reasoning about monadic programs. A Hoare triple `Triple x P Q` is a
*specification* for `x`: if assertion `P` holds before `x`, then postcondition `Q` holds after
running `x`.

`⦃P⦄ x ⦃Q⦄` is convenient syntax for `Triple x P Q`.
⦃ term ⦄ term ⦃ term ⦄
```

`⦃P⦄ x ⦃Q⦄` is syntactic sugar for `[Triple](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") x P Q`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.Triple.and "Permalink")theorem
```


Std.Do.Triple.and.{u, v} {m : Type u → Type v} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")}
  {α : Type u} {P₁ : [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps} {Q₁ : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps}
  {P₂ : [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps} {Q₂ : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps} [[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps] (x : m α)
  (h₁ : [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")P₁[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") x [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")Q₁[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")) (h₂ : [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")P₂[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") x [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")Q₂[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")) : [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")P₁ [∧](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___and "Documentation for Std.Do.SPred.and") P₂[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") x [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")Q₁ [∧ₚ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___and "Documentation for Std.Do.PostCond.and") Q₂[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")


Std.Do.Triple.and.{u, v}
  {m : Type u → Type v} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")}
  {α : Type u} {P₁ : [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps}
  {Q₁ : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps} {P₂ : [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps}
  {Q₂ : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps} [[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps] (x : m α)
  (h₁ : [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")P₁[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") x [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")Q₁[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")) (h₂ : [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")P₂[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") x [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")Q₂[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")) :
  [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")P₁ [∧](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___and "Documentation for Std.Do.SPred.and") P₂[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") x [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")Q₁ [∧ₚ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___and "Documentation for Std.Do.PostCond.and") Q₂[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")


```

Conjunction for two Hoare triple specifications of a program `x`. This theorem is useful for decomposing proofs, because unrelated facts about `x` can be proven separately and then combined with this theorem.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.Triple.mp "Permalink")theorem
```


Std.Do.Triple.mp.{u, v} {m : Type u → Type v} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")}
  {α : Type u} {P₁ : [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps} {Q₁ : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps}
  {P₂ : [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps} {Q₂ : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps} [[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps] (x : m α)
  (h₁ : [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")P₁[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") x [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")Q₁[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")) (h₂ : [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")P₂[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") x [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")Q₁ [→ₚ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___imp "Documentation for Std.Do.PostCond.imp") Q₂[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")) : [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")P₁ [∧](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___and "Documentation for Std.Do.SPred.and") P₂[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") x [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")Q₁ [∧ₚ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___and "Documentation for Std.Do.PostCond.and") Q₂[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")


Std.Do.Triple.mp.{u, v}
  {m : Type u → Type v} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")}
  {α : Type u} {P₁ : [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps}
  {Q₁ : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps} {P₂ : [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps}
  {Q₂ : [PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond") α ps} [[WP](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___WP___mk "Documentation for Std.Do.WP") m ps] (x : m α)
  (h₁ : [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")P₁[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") x [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")Q₁[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple"))
  (h₂ : [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")P₂[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") x [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")Q₁ [→ₚ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___imp "Documentation for Std.Do.PostCond.imp") Q₂[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")) :
  [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")P₁ [∧](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___and "Documentation for Std.Do.SPred.and") P₂[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") x [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")Q₁ [∧ₚ](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___and "Documentation for Std.Do.PostCond.and") Q₂[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")


```

Modus ponens for two Hoare triple specifications of a program `x`. This theorem is useful for separating proofs. If `h₁ : [Triple](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") x P₁ Q₁` proves a basic property about `x` and `h₂ : [Triple](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") x P₂ (Q₁ →ₚ Q₂)` is an advanced proof for `Q₂` that builds on the basic proof for `Q₁`, then `mp x h₁ h₂` is a proof for `Q₂` about `x`.
##  17.2.5. Specification Lemmas[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--mvcgen--tactic--Predicate-Transformers--Specification-Lemmas "Permalink")
_Specification lemmas_ are designated theorems that associate Hoare triples with functions. When `[mvcgen](Tactic-Proofs/Tactic-Reference/#mvcgen "Documentation for tactic")` encounters a function, it checks whether there are any registered specification lemmas and attempts to use them to discharge intermediate [verification conditions](The--mvcgen--tactic/Overview/#--tech-term-verification-conditions). If there is no applicable specification lemma, then the connection between the statement's pre- and postconditions will become a verification condition. Specification lemmas allow compositional reasoning about libraries of monadic code.
When applied to a theorem whose statement is a Hoare triple, the `spec` attribute registers the theorem as a specification lemma. These lemmas are used in order of priority.
The `spec` attribute may also be applied to definitions. On definitions, it indicates that the definition should be unfolded during verification condition generation.
attributeSpecification Lemmas

```
attr ::= ...
    | Theorems tagged with the `spec` attribute are used by the `mspec` and `mvcgen` tactics.

* When used on a theorem `foo_spec : Triple (foo a b c) P Q`, then `mspec` and `mvcgen` will use
  `foo_spec` as a specification for calls to `foo`.
* Otherwise, when used on a definition that `@[simp]` would work on, it is added to the internal
  simp set of `mvcgen` that is used within `wp⟦·⟧` contexts to simplify match discriminants and
  applications of constants.
spec prio?
```

Theorems tagged with the `[spec](The--mvcgen--tactic/Predicate-Transformers/#Lean___Parser___Attr___spec "Documentation for syntax")` attribute are used by the `mspec` and `mvcgen` tactics.
  * When used on a theorem `foo_spec : Triple (foo a b c) P Q`, then `mspec` and `mvcgen` will use `foo_spec` as a specification for calls to `foo`.
  * Otherwise, when used on a definition that `@[simp]` would work on, it is added to the internal simp set of `mvcgen` that is used within `[wp⟦](The--mvcgen--tactic/Predicate-Transformers/#Std___Do____FLQQ_termWp____________FLQQ_ "Documentation for syntax")·⟧` contexts to simplify match discriminants and applications of constants.


Universally-quantified variables in specification lemmas can be used to relate input states to output states and return values. These variables are referred to as _schematic variables_.
Schematic Variables
The function `[double](The--mvcgen--tactic/Predicate-Transformers/#double-_LPAR_in-Schematic-Variables_RPAR_ "Definition of example")` doubles the value of a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` state:
`def double : [StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   [modify](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#modify "Documentation for modify") (2 * ·) `
Its specification should _relate_ the initial and final states, but it cannot know their precise values. The specification uses a schematic variable to stand for the initial state:
`theorem double_spec :     ⦃ fun s => ⌜s = n⌝ ⦄ [double](The--mvcgen--tactic/Predicate-Transformers/#double-_LPAR_in-Schematic-Variables_RPAR_ "Definition of example") ⦃ ⇓ () s => ⌜s = 2 * n⌝ ⦄ := byn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")[fun](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") s [=>](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") [⌜](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")s [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n[⌝](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") [double](The--mvcgen--tactic/Predicate-Transformers/#double-_LPAR_in-Schematic-Variables_RPAR_ "Definition of example") [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")[PostCond.noThrow](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___noThrow "Documentation for Std.Do.PostCond.noThrow") fun x s => [⌜](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")s [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") n[⌝](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")   [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [[double](The--mvcgen--tactic/Predicate-Transformers/#double-_LPAR_in-Schematic-Variables_RPAR_ "Definition of example")]n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")[fun](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") s [=>](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") [⌜](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")s [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n[⌝](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple") [modify](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#modify "Documentation for modify") fun x => 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [⦃](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")[PostCond.noThrow](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond___noThrow "Documentation for Std.Do.PostCond.noThrow") fun x s => [⌜](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")s [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") n[⌝](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred___pure "Documentation for Std.Do.SPred.pure")[⦄](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Triple "Documentation for Std.Do.Triple")   mvcgen with [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
The assertion in the precondition is a function because the `[PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")` of `[StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` is `[.arg](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape.arg") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [.pure](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape.pure")`, and `[Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ([.arg](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape.arg") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [.pure](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape.pure"))` is `[SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") [[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")]`.
[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAZRgEwHQBEIChSVolVAFQEMBjGYMjbLCMAUwDsC1MssBnBmAfXsoQWIAG5kA5s1QB3ElCbAm4uADMSAG24dkDFXGQQArgCN1DOAC4CJGAwCycAHI24AVQXwLAXn3Y4cEAhkYBUATzgACgAmOAAqOAB2gEoOGAALBmgGEF8TM15ORjJLLH9/QGDKVUMWTjgvAD44QBxiWp8mQFxiOEAQylzTc0rAZcJIpLhWxpa6uBj4ju7LH2NQ0tHcOABtAzyGAF1l0QlmOGlgdLhxKEVkIA"\))
##  17.2.6. Invariant Specifications[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--mvcgen--tactic--Predicate-Transformers--Invariant-Specifications "Permalink")
These types are used in invariants. The [specification lemmas](The--mvcgen--tactic/Predicate-Transformers/#--tech-term-Specification-lemmas) for `[ForIn.forIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn.forIn")` and `[ForIn'.forIn'](Functors___-Monads-and--do--Notation/Syntax/#ForIn______mk "Documentation for ForIn'.forIn'")` take parameters of type `[Invariant](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Invariant "Documentation for Std.Do.Invariant")`, and `[mvcgen](Tactic-Proofs/Tactic-Reference/#mvcgen "Documentation for tactic")` ensures that invariants are not accidentally generated by other automation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.Invariant "Permalink")def
```


Std.Do.Invariant.{u₁, u₂} {α : Type u₁} (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (β : Type u₂)
  (ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")) : Type (max u₂ u₁)


Std.Do.Invariant.{u₁, u₂} {α : Type u₁}
  (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (β : Type u₂)
  (ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")) : Type (max u₂ u₁)


```

The type of loop invariants used by the specifications of `for ... in ...` loops. A loop invariant is a `[PostCond](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostCond "Documentation for Std.Do.PostCond")` that takes as parameters
  * A `[List.Cursor](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor") xs` representing the iteration state of the loop. It is parameterized by the list of elements `xs` that the `for` loop iterates over.
  * A state tuple of type `β`, which will be a nesting of `[MProd](Basic-Types/Tuples/#MProd___mk "Documentation for MProd")`s representing the elaboration of `let mut` variables and early return.


The loop specification lemmas will use this in the following way: Before entering the loop, the cursor's prefix is empty and the suffix is `xs`. After leaving the loop, the cursor's prefix is `xs` and the suffix is empty. During the induction step, the invariant holds for a suffix with head element `x`. After running the loop body, the invariant then holds after shifting `x` to the prefix.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Do.Invariant.withEarlyReturn "Permalink")def
```


Std.Do.Invariant.withEarlyReturn.{u₁, u₂} {β : Type (max u₁ u₂)}
  {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")} {α✝ : Type (max u₁ u₂)} {xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝}
  {γ : Type (max u₁ u₂)} (onContinue : xs.[Cursor](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor") → β → [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps)
  (onReturn : γ → β → [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps)
  (onExcept : [ExceptConds](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___ExceptConds "Documentation for Std.Do.ExceptConds") ps := ExceptConds.false) :
  [Invariant](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Invariant "Documentation for Std.Do.Invariant") xs ([MProd](Basic-Types/Tuples/#MProd___mk "Documentation for MProd") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ) β) ps


Std.Do.Invariant.withEarlyReturn.{u₁, u₂}
  {β : Type (max u₁ u₂)} {ps : [PostShape](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___PostShape___pure "Documentation for Std.Do.PostShape")}
  {α✝ : Type (max u₁ u₂)} {xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝}
  {γ : Type (max u₁ u₂)}
  (onContinue :
    xs.[Cursor](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor") → β → [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps)
  (onReturn : γ → β → [Assertion](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Assertion "Documentation for Std.Do.Assertion") ps)
  (onExcept : [ExceptConds](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___ExceptConds "Documentation for Std.Do.ExceptConds") ps :=
    ExceptConds.false) :
  [Invariant](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___Invariant "Documentation for Std.Do.Invariant") xs ([MProd](Basic-Types/Tuples/#MProd___mk "Documentation for MProd") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ) β) ps


```

Helper definition for specifying loop invariants for loops with early return.
`for ... in ...` loops with early return of type `γ` elaborate to a call like this:

```
forIn (β := MProd (Option γ) ...) (b := ⟨none, ...⟩) collection loopBody

```

Note that the first component of the `[MProd](Basic-Types/Tuples/#MProd___mk "Documentation for MProd")` state tuple is the optional early return value. It is `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` as long as there was no early return and `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") r` if the loop returned early with `r`.
This function allows to specify different invariants for the loop body depending on whether the loop terminated early or not. When there was an early return, the loop has effectively finished, which is encoded by the additional `⌜xs.suffix = []⌝` assertion in the invariant. This assertion is vital for successfully proving the induction step, as it contradicts with the assumption that `xs.suffix = x::rest` of the inductive hypothesis at the start of the loop body, meaning that users won't need to prove anything about the bogus case where the loop has returned early yet takes another iteration of the loop body.
Invariants use lists to model the sequence of values in a ``Lean.Parser.Term.doFor : doElem```for x in e do s`  iterates over `e` assuming `e`'s type has an instance of the `ForIn` typeclass. `break` and `continue` are supported inside `for` loops. `for x in e, x2 in e2, ... do s` iterates of the given collections in parallel, until at least one of them is exhausted. The types of `e2` etc. must implement the `Std.ToStream` typeclass. ```for` loop. The current position in the loop is tracked with a `[List.Cursor](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor")` that represents a position in a list as a combination of the elements to the left of the position and the elements to the right. This type is not a traditional zipper, in which the prefix is reversed for efficient movement: it is intended for use in specifications and proofs, not in run-time code, so the prefix is in the original order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.Cursor.prefix "Permalink")structure
```


List.Cursor.{u} {α : Type u} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : Type u


List.Cursor.{u} {α : Type u}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : Type u


```

A pointer at a specific location in a list. List cursors are used in loop invariants for the `mvcgen` tactic.
Moving the cursor to the left or right takes time linear in the current position of the cursor, so this data structure is not appropriate for run-time code.
#  Constructor

```
[List.Cursor.mk](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor.mk").{u}
```

#  Fields

```
prefix : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α
```

The elements before to the current position in the list.

```
suffix : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α
```

The elements starting at the current position. If the position is after the last element of the list, then the suffix is empty; otherwise, the first element of the suffix is the current element that the cursor points to.

```
property : self.[prefix](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor.prefix") [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") self.[suffix](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor.suffix") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") l
```

Appending the prefix to the suffix yields the original list.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.Cursor.at "Permalink")def
```


List.Cursor.at.{u_1} {α : Type u_1} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : l.[Cursor](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor")


List.Cursor.at.{u_1} {α : Type u_1}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : l.[Cursor](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor")


```

Creates a cursor at position `n` in the list `l`. The prefix contains the first `n` elements, and the suffix contains the remaining elements. If `n` is larger than the length of the list, the cursor is positioned at the end of the list.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.Cursor.pos "Permalink")def
```


List.Cursor.pos.{u_1} {α✝ : Type u_1} {l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝} (c : l.[Cursor](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


List.Cursor.pos.{u_1} {α✝ : Type u_1}
  {l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝} (c : l.[Cursor](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The position of the cursor in the list. It's a shortcut for the number of elements in the prefix.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.Cursor.current "Permalink")def
```


List.Cursor.current.{u_1} {α : Type u_1} {l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α} (c : l.[Cursor](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor"))
  (h : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") c.[suffix](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor.suffix").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := by get_elem_tactic) : α


List.Cursor.current.{u_1} {α : Type u_1}
  {l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α} (c : l.[Cursor](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor"))
  (h : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") c.[suffix](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor.suffix").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := by
    get_elem_tactic) :
  α


```

Returns the element at the current cursor position.
Requires that is a current element: the suffix must be non-empty, so the cursor is not at the end of the list.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.Cursor.tail "Permalink")def
```


List.Cursor.tail.{u_1} {α✝ : Type u_1} {l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝} (s : l.[Cursor](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor"))
  (h : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") s.[suffix](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor.suffix").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := by get_elem_tactic) : l.[Cursor](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor")


List.Cursor.tail.{u_1} {α✝ : Type u_1}
  {l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α✝} (s : l.[Cursor](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor"))
  (h : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") s.[suffix](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor.suffix").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := by
    get_elem_tactic) :
  l.[Cursor](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor")


```

Advances the cursor by one position, moving the current element from the suffix to the prefix.
Requires that the cursor is not already at the end of the list.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.Cursor.begin "Permalink")def
```


List.Cursor.begin.{u_1} {α : Type u_1} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : l.[Cursor](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor")


List.Cursor.begin.{u_1} {α : Type u_1}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : l.[Cursor](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor")


```

Creates a cursor at the beginning of the list (position 0). The prefix is empty and the suffix is the entire list.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.Cursor.end "Permalink")def
```


List.Cursor.end.{u_1} {α : Type u_1} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : l.[Cursor](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor")


List.Cursor.end.{u_1} {α : Type u_1}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : l.[Cursor](The--mvcgen--tactic/Predicate-Transformers/#List___Cursor___mk "Documentation for List.Cursor")


```

Creates a cursor at the end of the list. The prefix is the entire list and the suffix is empty.
[←17.1. Overview](The--mvcgen--tactic/Overview/#The-Lean-Language-Reference--The--mvcgen--tactic--Overview "17.1. Overview")[17.3. Verification Conditions→](The--mvcgen--tactic/Verification-Conditions/#The-Lean-Language-Reference--The--mvcgen--tactic--Verification-Conditions "17.3. Verification Conditions")

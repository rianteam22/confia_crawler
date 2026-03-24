[←14.2. Reading Proof States](Tactic-Proofs/Reading-Proof-States/#proof-states "14.2. Reading Proof States")[14.4. Options→](Tactic-Proofs/Options/#tactic-language-options "14.4. Options")
#  14.3. The Tactic Language[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-language "Permalink")
A tactic script consists of a sequence of tactics, separated either by semicolons or newlines. When separated by newlines, tactics must be indented to the same level. Explicit curly braces and semicolons may be used instead of indentation. Tactic sequences may be grouped by parentheses. This allows a sequence of tactics to be used in a position where a single tactic would otherwise be grammatically expected.
Generally, execution proceeds from top to bottom, with each tactic running in the proof state left behind by the prior tactic. The tactic language contains a number of control structures that can modify this flow.
Each tactic is a syntax extension in the `tactic` category. This means that tactics are free to define their own concrete syntax and parsing rules. However, with a few exceptions, the majority of tactics can be identified by a leading keyword; the exceptions are typically frequently-used built-in control structures such as `[<;>](Tactic-Proofs/The-Tactic-Language/#_LT__SEMI__GT_ "Documentation for tactic")`.
##  14.3.1. Control Structures[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-language-control "Permalink")
Strictly speaking, there is no fundamental distinction between control structures and other tactics. Any tactic is free to take others as arguments and arrange for their execution in any context that it sees fit. Even if a distinction is arbitrary, however, it can still be useful. The tactics in this section are those that resemble traditional control structures from programming, or those that _only_ recombine other tactics rather than making progress themselves.
###  14.3.1.1. Success and Failure[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-language-success-failure "Permalink")
When run in a proof state, every tactic either succeeds or fails. Tactic failure is akin to exceptions: failures typically “bubble up” until handled. Unlike exceptions, there is no operator to distinguish between reasons for failure; `[first](Tactic-Proofs/The-Tactic-Language/#first "Documentation for tactic")` simply takes the first branch that succeeds.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.fail "Permalink")tactic
```
[fail](Tactic-Proofs/The-Tactic-Language/#fail "Documentation for tactic")
```

`fail msg` is a tactic that always fails, and produces an error using the given message.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.failIfSuccess "Permalink")tactic
```
[fail_if_success](Tactic-Proofs/The-Tactic-Language/#fail_if_success "Documentation for tactic")
```

`fail_if_success t` fails if the tactic `t` succeeds.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticTry_ "Permalink")tactic
```
[try](Tactic-Proofs/The-Tactic-Language/#try "Documentation for tactic")
```

`try tac` runs `tac` and succeeds even if `tac` failed.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.first "Permalink")tactic
```
[first](Tactic-Proofs/The-Tactic-Language/#first "Documentation for tactic")
```

`first | tac | ...` runs each `tac` until one succeeds, or else fails.
###  14.3.1.2. Branching[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-language-branching "Permalink")
Tactic proofs may use pattern matching and conditionals. However, their meaning is not quite the same as it is in terms. While terms are expected to be executed once the values of their variables are known, proofs are executed with their variables left abstract and should consider _all_ cases simultaneously. Thus, when `if` and `match` are used in tactics, their meaning is reasoning by cases rather than selection of a concrete branch. All of their branches are executed, and the condition or pattern match is used to refine the main goal with more information in each branch, rather than to select a single branch.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacIfThenElse "Permalink")tactic
```
[if](Tactic-Proofs/The-Tactic-Language/#if "Documentation for tactic")
```

In tactic mode, `[if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") t [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") tac1 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") tac2` is alternative syntax for:
`by_cases t · tac1 · tac2`
It performs case distinction on `h† : t` or `h† : ¬t`, where `h†` is an anonymous hypothesis, and `tac1` and `tac2` are the subproofs. (It doesn't actually use nondependent `[if](Tactic-Proofs/The-Tactic-Language/#if "Documentation for tactic")`, since this wouldn't add anything to the context and hence would be useless for proving theorems. To actually insert an `ite` application use `[refine](Tactic-Proofs/Tactic-Reference/#refine "Documentation for tactic") [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") t [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") ?_ [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") ?_`.)
The assumptions in each subgoal can be named. `[if](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") h : t [then](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") tac1 [else](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") tac2` can be used as alternative syntax for:

```
by_cases h : t
· tac1
· tac2

```

It performs case distinction on `h : t` or `h : ¬t`.
You can use `?_` or `_` for either subproof to delay the goal to after the tactic, but if a tactic sequence is provided for `tac1` or `tac2` then it will require the goal to be closed by the end of the block.
Reasoning by cases with `if`
In each branch of the ``Lean.Parser.Tactic.tacIfThenElse : tactic``In tactic mode, `if t then tac1 else tac2` is alternative syntax for: ``` by_cases t · tac1 · tac2 ``` It performs case distinction on `h† : t` or `h† : ¬t`, where `h†` is an anonymous hypothesis, and `tac1` and `tac2` are the subproofs. (It doesn't actually use nondependent `if`, since this wouldn't add anything to the context and hence would be useless for proving theorems. To actually insert an `ite` application use `refine if t then ?_ else ?_`.)  The assumptions in each subgoal can be named. `if h : t then tac1 else tac2` can be used as alternative syntax for: ``` by_cases h : t · tac1 · tac2 ``` It performs case distinction on `h : t` or `h : ¬t`.  You can use `?_` or `_` for either subproof to delay the goal to after the tactic, but if a tactic sequence is provided for `tac1` or `tac2` then it will require the goal to be closed by the end of the block. ``[`if`](Tactic-Proofs/The-Tactic-Language/#if), an assumption is added that reflects whether `n = 0`.
`example (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n = 0 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n < 1 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n > 0 := byn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ if n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 then n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 1 else n > 0   [if](Tactic-Proofs/The-Tactic-Language/#if "Documentation for tactic") n = 0 [then](Tactic-Proofs/The-Tactic-Language/#if "Documentation for tactic")n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝:n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ if n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 then n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 1 else n > 0     [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [*]All goals completed! 🐙   [else](Tactic-Proofs/The-Tactic-Language/#if "Documentation for tactic")n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ if n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 then n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 1 else n > 0     [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") only [↓reduceIte, gt_iff_lt, *]n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n     [omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAKAdvAXPAcmALgSnXgEsAzeVAXngAZ4cALYVVAHngEZ5gYBnBVAHw10VAEYBPAFDxiZSsIZNpM+DyLR4AbQBUAXWXc+ymWo0B7ZDHFbAyYQAnYABMArgGNgASRzAANPADmOAD6pCRBMDh+esbwZhDA/mBAA"\))
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.match "Permalink")tactic
```
[match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic")
```

`[match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic")` performs case analysis on one or more expressions. See [Induction and Recursion](https://lean-lang.org/theorem_proving_in_lean4/induction_and_recursion.html). The syntax for the `[match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic")` tactic is the same as term-mode `[match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic")`, except that the match arms are tactics instead of expressions.
`example (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : n = n := byn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n   [match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic") n [with](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic")   | 0 =>n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙   | i+1 =>n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")i:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ i [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") i [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")All goals completed! 🐙 `
When pattern matching, instances of the [discriminant](Terms/Pattern-Matching/#--tech-term-match-discriminants) in the goal are replaced with the patterns that match them in each branch. Each branch must then prove the refined goal. Compared to the `cases` tactic, using `match` can allow a greater degree of flexibility in the cases analysis being performed, but the requirement that each branch solve its goal completely makes it more difficult to incorporate into larger automation scripts.
Reasoning by cases with `match`
In each branch of the ``Lean.Parser.Tactic.match : tactic```match` performs case analysis on one or more expressions. See [Induction and Recursion][tpil4]. The syntax for the `match` tactic is the same as term-mode `match`, except that the match arms are tactics instead of expressions. ``` example (n : Nat) : n = n := by   match n with   | 0 => rfl   | i+1 => simp ```  [tpil4]: https://lean-lang.org/theorem_proving_in_lean4/induction_and_recursion.html ``[`match`](Tactic-Proofs/The-Tactic-Language/#match), the discriminant `n` has been replaced by either `0` or `k + 1`.
`example (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n = 0 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n < 1 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n > 0 := byn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ if n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 then n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 1 else n > 0   [match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic") n [with](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic")   | 0 =>n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ if 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 then 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 1 else 0 > 0     [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")All goals completed! 🐙   | k + 1 =>n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ if k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 then k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 1 else k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 > 0     [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAKAdvAXPAcmALgSnXgEsAzeVAXngAZ4cALYVVAHngEZ5gYBnBVAHw10VAEYBPAFDx4EXAGN65eAHciDafAA+wigM0yeRaJp0BreAGoO8PQfhHoQA"\))
###  14.3.1.3. Goal Selection[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-language-goal-selection "Permalink")
Most tactics affect the [main goal](Tactic-Proofs/#--tech-term-main-goal). Goal selection tactics provide a way to treat a different goal as the main one, rearranging the sequence of goals in the proof state.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.case "Permalink")tactic
```
[case](Tactic-Proofs/The-Tactic-Language/#case "Documentation for tactic")
```

  * `case tag => tac` focuses on the goal with case name `tag` and solves it using `tac`, or else fails.
  * `case tag x₁ ... xₙ => tac` additionally renames the `n` most recent hypotheses with inaccessible names to the given names.
  * `case tag₁ | tag₂ => tac` is equivalent to `(case tag₁ => tac); (case tag₂ => tac)`.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.case' "Permalink")tactic
```
[case'](Tactic-Proofs/The-Tactic-Language/#case___ "Documentation for tactic")
```

`[case'](Tactic-Proofs/The-Tactic-Language/#case___ "Documentation for tactic")` is similar to the `case tag => tac` tactic, but does not ensure the goal has been solved after applying `tac`, nor admits the goal if `tac` failed. Recall that `[case](Tactic-Proofs/The-Tactic-Language/#case "Documentation for tactic")` closes the goal using `[sorry](Tactic-Proofs/Tactic-Reference/#sorry "Documentation for tactic")` when `tac` fails, and the tactic execution is not interrupted.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.rotateLeft "Permalink")tactic
```
[rotate_left](Tactic-Proofs/The-Tactic-Language/#rotate_left "Documentation for tactic")
```

`rotate_left n` rotates goals to the left by `n`. That is, `[rotate_left](Tactic-Proofs/The-Tactic-Language/#rotate_left "Documentation for tactic") 1` takes the main goal and puts it to the back of the subgoal list. If `n` is omitted, it defaults to `1`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.rotateRight "Permalink")tactic
```
[rotate_right](Tactic-Proofs/The-Tactic-Language/#rotate_right "Documentation for tactic")
```

Rotate the goals to the right by `n`. That is, take the goal at the back and push it to the front `n` times. If `n` is omitted, it defaults to `1`.
####  14.3.1.3.1. Sequencing[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-language-sequencing "Permalink")
In addition to running tactics one after the other, each being used to solve the main goal, the tactic language supports sequencing tactics according to the way in which goals are produced. The `[<;>](Tactic-Proofs/The-Tactic-Language/#_LT__SEMI__GT_ "Documentation for tactic")` tactic combinator allows a tactic to be applied to _every_ [subgoal](Tactic-Proofs/#--tech-term-subgoals) produced by some other tactic. If no new goals are produced, then the second tactic is not run.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.%C2%ABtactic_<;>_%C2%BB "Permalink")tactic
```
[<;>](Tactic-Proofs/The-Tactic-Language/#_LT__SEMI__GT_ "Documentation for tactic")
```

`tac <;> tac'` runs `tac` on the main goal and `tac'` on each produced goal, concatenating all goals produced by `tac'`.
If the tactic fails on any of the [subgoals](Tactic-Proofs/#--tech-term-subgoals), then the whole `[<;>](Tactic-Proofs/The-Tactic-Language/#_LT__SEMI__GT_ "Documentation for tactic")` tactic fails.
Subgoal Sequencing
In this proof state:
x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1 [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 2⊢ x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3
the tactic `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") hinlx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝:x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1⊢ x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3inrx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝:x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 2⊢ x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3` yields the following two goals:
inlx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝:x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1⊢ x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3inrx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝:x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 2⊢ x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3
Running `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") hinlx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝:x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1⊢ x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3inrx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝:x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 2⊢ x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3 ; [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [*]inrx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝:x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 2⊢ x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3` causes `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` to solve the first goal, leaving the second behind:
inrx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝:x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 2⊢ x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3
Replacing the `;` with `[<;>](Tactic-Proofs/The-Tactic-Language/#_LT__SEMI__GT_ "Documentation for tactic")` and running `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") hinlx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝:x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1⊢ x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3inrx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝:x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 2⊢ x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3 <;>inlx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝:x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1⊢ x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3inrx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝:x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 2⊢ x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3 [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [*]All goals completed! 🐙` solves **both** of the new goals with `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`:
All goals completed! 🐙
####  14.3.1.3.2. Working on Multiple Goals[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-language-multiple-goals "Permalink")
The tactics `[all_goals](Tactic-Proofs/The-Tactic-Language/#all_goals "Documentation for tactic")` and `[any_goals](Tactic-Proofs/The-Tactic-Language/#any_goals "Documentation for tactic")` allow a tactic to be applied to every goal in the proof state. The difference between them is that if the tactic fails for in any of the goals, `[all_goals](Tactic-Proofs/The-Tactic-Language/#all_goals "Documentation for tactic")` itself fails, while `[any_goals](Tactic-Proofs/The-Tactic-Language/#any_goals "Documentation for tactic")` fails only if the tactic fails in all of the goals.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.allGoals "Permalink")tactic
```
[all_goals](Tactic-Proofs/The-Tactic-Language/#all_goals "Documentation for tactic")
```

`all_goals tac` runs `tac` on each goal, concatenating the resulting goals. If the tactic fails on any goal, the entire `all_goals` tactic fails.
See also `any_goals tac`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.anyGoals "Permalink")tactic
```
[any_goals](Tactic-Proofs/The-Tactic-Language/#any_goals "Documentation for tactic")
```

`any_goals tac` applies the tactic `tac` to every goal, concatenating the resulting goals for successful tactic applications. If the tactic fails on all of the goals, the entire `any_goals` tactic fails.
This tactic is like `all_goals try tac` except that it fails if none of the applications of `tac` succeeds.
###  14.3.1.4. Focusing[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-language-focusing "Permalink")
Focusing tactics remove some subset of the proof goals (typically leaving only the main goal) from the consideration of some further tactics. In addition to the tactics described here, the `[case](Tactic-Proofs/The-Tactic-Language/#case "Documentation for tactic")` and `[case'](Tactic-Proofs/The-Tactic-Language/#case___ "Documentation for tactic")` tactics focus on the selected goal.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.cdot "Permalink")tactic
```
[·](Tactic-Proofs/The-Tactic-Language/#___ "Documentation for tactic")
```

`· tac` focuses on the main goal and tries to solve it using `tac`, or else fails.
It is generally considered good Lean style to use bullets whenever a tactic line results in more than one new subgoal. This makes it easier to read and maintain proofs, because the connections between steps of reasoning are more clear and any change in the number of subgoals while editing the proof will have a localized effect.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.%C2%ABtacticNext_=>_%C2%BB "Permalink")tactic
```
[next](Tactic-Proofs/The-Tactic-Language/#next "Documentation for tactic")
```

`next => tac` focuses on the next goal and solves it using `tac`, or else fails. `next x₁ ... xₙ => tac` additionally renames the `n` most recent hypotheses with inaccessible names to the given names.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.focus "Permalink")tactic
```
[focus](Tactic-Proofs/The-Tactic-Language/#focus "Documentation for tactic")
```

`focus tac` focuses on the main goal, suppressing all other goals, and runs `tac` on it. Usually `· tac`, which enforces that the goal is closed by `tac`, should be preferred.
###  14.3.1.5. Repetition and Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-language-iteration "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticIterate____ "Permalink")tactic
```
[iterate](Tactic-Proofs/The-Tactic-Language/#iterate "Documentation for tactic")
```

`iterate n tac` runs `tac` exactly `n` times. `iterate tac` runs `tac` repeatedly until failure.
`[iterate](Tactic-Proofs/The-Tactic-Language/#iterate "Documentation for tactic")`'s argument is a tactic sequence, so multiple tactics can be run using `iterate n (tac₁; tac₂; ⋯)` or
`iterate n   tac₁   tac₂   ⋯`
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticRepeat_ "Permalink")tactic
```
[repeat](Tactic-Proofs/The-Tactic-Language/#repeat "Documentation for tactic")
```

`repeat tac` repeatedly applies `tac` so long as it succeeds. The tactic `tac` may be a tactic sequence, and if `tac` fails at any point in its execution, `[repeat](Tactic-Proofs/The-Tactic-Language/#repeat "Documentation for tactic")` will revert any partial changes that `tac` made to the tactic state.
The tactic `tac` should eventually fail, otherwise `repeat tac` will run indefinitely.
See also:
  * `try tac` is like `repeat tac` but will apply `tac` at most once.
  * `repeat' tac` recursively applies `tac` to each goal.
  * `first | tac1 | tac2` implements the backtracking used by `[repeat](Tactic-Proofs/The-Tactic-Language/#repeat "Documentation for tactic")`


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.repeat' "Permalink")tactic
```
[repeat'](Tactic-Proofs/The-Tactic-Language/#repeat___ "Documentation for tactic")
```

`repeat' tac` recursively applies `tac` on all of the goals so long as it succeeds. That is to say, if `tac` produces multiple subgoals, then `repeat' tac` is applied to each of them.
See also:
  * `repeat tac` simply repeatedly applies `tac`.
  * `repeat1' tac` is `repeat' tac` but requires that `tac` succeed for some goal at least once.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.repeat1' "Permalink")tactic
```
[repeat1'](Tactic-Proofs/The-Tactic-Language/#repeat1___ "Documentation for tactic")
```

`repeat1' tac` recursively applies to `tac` on all of the goals so long as it succeeds, but `repeat1' tac` fails if `tac` succeeds on none of the initial goals.
See also:
  * `repeat tac` simply applies `tac` repeatedly.
  * `repeat' tac` is like `repeat1' tac` but it does not require that `tac` succeed at least once.


##  14.3.2. Names and Hygiene[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-language-hygiene "Permalink")
Behind the scenes, tactics generate proof terms. These proof terms exist in a local context, because assumptions in proof states correspond to local binders in terms. Uses of assumptions correspond to variable references. It is very important that the naming of assumptions be predictable; otherwise, small changes to the internal implementation of a tactic could either lead to variable capture or to a broken reference if they cause different names to be selected.
Lean's tactic language is _hygienic_.  This means that the tactic language respects lexical scope: names that occur in a tactic refer to the enclosing binding in the source code, rather than being determined by the generated code, and the tactic framework is responsible for maintaining this property. Variable references in tactic scripts refer either to names that were in scope at the beginning of the script or to bindings that were explicitly introduced as part of the tactics, rather than to the names chosen for use in the proof term behind the scenes.
A consequence of hygienic tactics is that the only way to refer to an assumption is to explicitly name it. Tactics cannot assign assumption names themselves, but must rather accept names from users; users are correspondingly obligated to provide names for assumptions that they wish to refer to. When an assumption does not have a user-provided name, it is shown in the proof state with a dagger (`'†', DAGGER	0x2020`). The dagger indicates that the name is _inaccessible_ and cannot be explicitly referred to.
Hygiene can be disabled by setting the option `[tactic.hygienic](Tactic-Proofs/The-Tactic-Language/#tactic___hygienic "Documentation for option tactic.hygienic")` to `false`. This is not recommended, as many tactics rely on the hygiene system to prevent capture and thus do not incur the overhead of careful manual name selection.
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=tactic.hygienic "Permalink")option
```
tactic.hygienic
```

Default value: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
make sure tactics are hygienic
Tactic hygiene: inaccessible assumptions
When proving that `∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), 0 + n = n`, the initial proof state is:
⊢ ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n
The tactic `[intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic")n✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n✝ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n✝` results in a proof state with an inaccessible assumption:
n✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n✝ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n✝
Tactic hygiene: accessible assumptions
When proving that `∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), 0 + n = n`, the initial proof state is:
⊢ ∀ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n
The tactic `[intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") nn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n`, with the explicit name `n`, results in a proof state with an accessibly-named assumption:
n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n
###  14.3.2.1. Accessing Assumptions[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-language-assumptions "Permalink")
Many tactics provide a means of specifying names for the assumptions that they introduce. For example, `[intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic")` and `[intros](Tactic-Proofs/Tactic-Reference/#intros "Documentation for tactic")` take assumption names as arguments, and `[induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic")`'s ``Lean.Parser.Tactic.induction : tactic``Assuming `x` is a variable in the local context with an inductive type, `induction x` applies induction on `x` to the main goal, producing one goal for each constructor of the inductive type, in which the target is replaced by a general instance of that constructor and an inductive hypothesis is added for each recursive argument to the constructor. If the type of an element in the local context depends on `x`, that element is reverted and reintroduced afterward, so that the inductive hypothesis incorporates that hypothesis as well.  For example, given `n : Nat` and a goal with a hypothesis `h : P n` and target `Q n`, `induction n` produces one goal with hypothesis `h : P 0` and target `Q 0`, and one goal with hypotheses `h : P (Nat.succ a)` and `ih₁ : P a → Q a` and target `Q (Nat.succ a)`. Here the names `a` and `ih₁` are chosen automatically and are not accessible. You can use `with` to provide the variables names for each constructor. - `induction e`, where `e` is an expression instead of a variable,   generalizes `e` in the goal, and then performs induction on the resulting variable. - `induction e using r` allows the user to specify the principle of induction that should be used.   Here `r` should be a term whose result type must be of the form `C t`,   where `C` is a bound variable and `t` is a (possibly empty) sequence of bound variables - `induction e generalizing z₁ ... zₙ`, where `z₁ ... zₙ` are variables in the local context,   generalizes over `z₁ ... zₙ` before applying the induction but then introduces them in each goal.   In other words, the net effect is that each inductive hypothesis is generalized. - Given `x : Nat`, `induction x with | zero => tac₁ | succ x' ih => tac₂`   uses tactic `tac₁` for the `zero` case, and `tac₂` for the `succ` case. ``[`with`](Tactic-Proofs/Tactic-Reference/#induction)-form allows simultaneous case selection, assumption naming, and focusing. When an assumption does not have a name, one can be assigned using `[next](Tactic-Proofs/The-Tactic-Language/#next "Documentation for tactic")`, `[case](Tactic-Proofs/The-Tactic-Language/#case "Documentation for tactic")`, or `[rename_i](Tactic-Proofs/The-Tactic-Language/#rename_i "Documentation for tactic")`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.renameI "Permalink")tactic
```
[rename_i](Tactic-Proofs/The-Tactic-Language/#rename_i "Documentation for tactic")
```

`rename_i x_1 ... x_n` renames the last `n` inaccessible names using the given names.
##  14.3.3. Assumption Management[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-language-assumption-management "Permalink")
Larger proofs can benefit from management of proof states, removing irrelevant assumptions and making their names easier to understand. Along with these operators, `[rename_i](Tactic-Proofs/The-Tactic-Language/#rename_i "Documentation for tactic")` allows inaccessible assumptions to be renamed, and `[intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic")`, `[intros](Tactic-Proofs/Tactic-Reference/#intros "Documentation for tactic")` and `[rintro](Tactic-Proofs/Tactic-Reference/#rintro "Documentation for tactic")` convert goals that are implications or universal quantification into goals with additional assumptions.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.rename "Permalink")tactic
```
[rename](Tactic-Proofs/The-Tactic-Language/#rename "Documentation for tactic")
```

`[rename](Tactic-Proofs/The-Tactic-Language/#rename "Documentation for tactic") t => x` renames the most recent hypothesis whose type matches `t` (which may contain placeholders) to `x`, or fails if no such hypothesis could be found.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.revert "Permalink")tactic
```
[revert](Tactic-Proofs/The-Tactic-Language/#revert "Documentation for tactic")
```

`revert x...` is the inverse of `intro x...`: it moves the given hypotheses into the main goal's target type.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.clear "Permalink")tactic
```
[clear](Tactic-Proofs/The-Tactic-Language/#clear "Documentation for tactic")
```

`clear x...` removes the given hypotheses, or fails if there are remaining references to a hypothesis.
##  14.3.4. Local Definitions and Proofs[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-language-local-defs "Permalink")
`have` and `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` both create local assumptions. Generally speaking, `have` should be used when proving an intermediate lemma; `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` should be reserved for local definitions.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticHave__ "Permalink")tactic
```
have
```

The `have` tactic is for adding opaque definitions and hypotheses to the local context of the main goal. The definitions forget their associated value and cannot be unfolded, unlike definitions added by the `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` tactic.
  * `have h : t := e` adds the hypothesis `h : t` if `e` is a term of type `t`.
  * `have h := e` uses the type of `e` for `t`.
  * `have : t := e` and `have := e` use `this` for the name of the hypothesis.
  * `have pat := e` for a pattern `pat` is equivalent to `[match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic") e [with](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic") | pat => _`, where `_` stands for the tactics that follow this one. It is convenient for types that have only one applicable constructor. For example, given `h : p ∧ q ∧ r`, `have ⟨h₁, h₂, h₃⟩ := h` produces the hypotheses `h₁ : p`, `h₂ : q`, and `h₃ : r`.
  * The syntax `have (eq := h) pat := e` is equivalent to `[match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic") h : e [with](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic") | pat => _`, which adds the equation `h : e = pat` to the local context.


The tactic supports all the same syntax variants and options as the `have` term.
**Properties and relations**
  * It is not possible to unfold a variable introduced using `have`, since the definition's value is forgotten. The `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` tactic introduces definitions that can be unfolded.
  * The `have h : t := e` is like doing `let h : t := e; clear_value h`.
  * The `have` tactic is preferred for propositions, and `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` is preferred for non-propositions.
  * Sometimes `have` is used for non-propositions to ensure that the variable is never unfolded, which may be important for performance reasons. Consider using the equivalent `let +nondep` to indicate the intent.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticHave__ "Permalink")tactic
```
have
```

The `have` tactic is for adding opaque definitions and hypotheses to the local context of the main goal. The definitions forget their associated value and cannot be unfolded, unlike definitions added by the `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` tactic.
  * `have h : t := e` adds the hypothesis `h : t` if `e` is a term of type `t`.
  * `have h := e` uses the type of `e` for `t`.
  * `have : t := e` and `have := e` use `this` for the name of the hypothesis.
  * `have pat := e` for a pattern `pat` is equivalent to `[match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic") e [with](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic") | pat => _`, where `_` stands for the tactics that follow this one. It is convenient for types that have only one applicable constructor. For example, given `h : p ∧ q ∧ r`, `have ⟨h₁, h₂, h₃⟩ := h` produces the hypotheses `h₁ : p`, `h₂ : q`, and `h₃ : r`.
  * The syntax `have (eq := h) pat := e` is equivalent to `[match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic") h : e [with](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic") | pat => _`, which adds the equation `h : e = pat` to the local context.


The tactic supports all the same syntax variants and options as the `have` term.
**Properties and relations**
  * It is not possible to unfold a variable introduced using `have`, since the definition's value is forgotten. The `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` tactic introduces definitions that can be unfolded.
  * The `have h : t := e` is like doing `let h : t := e; clear_value h`.
  * The `have` tactic is preferred for propositions, and `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` is preferred for non-propositions.
  * Sometimes `have` is used for non-propositions to ensure that the variable is never unfolded, which may be important for performance reasons. Consider using the equivalent `let +nondep` to indicate the intent.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticHave' "Permalink")tactic
```
[have'](Tactic-Proofs/The-Tactic-Language/#have___ "Documentation for tactic")
```

Similar to `have`, but using `[refine'](Tactic-Proofs/Tactic-Reference/#refine___ "Documentation for tactic")`
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticLet__ "Permalink")tactic
```
[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")
```

The `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` tactic is for adding definitions to the local context of the main goal. The definition can be unfolded, unlike definitions introduced by `have`.
  * `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic") x : t := e` adds the definition `x : t := e` if `e` is a term of type `t`.
  * `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic") x := e` uses the type of `e` for `t`.
  * `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic") : t := e` and `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic") := e` use `this` for the name of the hypothesis.
  * `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic") pat := e` for a pattern `pat` is equivalent to `[match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic") e [with](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic") | pat => _`, where `_` stands for the tactics that follow this one. It is convenient for types that let only one applicable constructor. For example, given `p : α × β × γ`, `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic") ⟨x, y, z⟩ := p` produces the local variables `x : α`, `y : β`, and `z : γ`.
  * The syntax `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic") (eq := h) pat := e` is equivalent to `[match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic") h : e [with](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic") | pat => _`, which adds the equation `h : e = pat` to the local context.


The tactic supports all the same syntax variants and options as the `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` term.
**Properties and relations**
  * Unlike `have`, it is possible to unfold definitions introduced using `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")`, using tactics such as `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`, `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")`, `[unfold](Tactic-Proofs/Tactic-Reference/#unfold "Documentation for tactic")`, and `[subst](Tactic-Proofs/Tactic-Reference/#subst "Documentation for tactic")`.
  * The `[clear_value](Tactic-Proofs/Tactic-Reference/#clear_value "Documentation for tactic")` tactic turns a `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` definition into a `have` definition after the fact. The tactic might fail if the local context depends on the value of the variable.
  * The `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` tactic is preferred for data (non-propositions).
  * Sometimes `have` is used for non-propositions to ensure that the variable is never unfolded, which may be important for performance reasons.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.letrec "Permalink")tactic
```
[let rec](Tactic-Proofs/The-Tactic-Language/#let-rec "Documentation for tactic")
```

`[let](Tactic-Proofs/The-Tactic-Language/#let-rec "Documentation for tactic") [rec](Tactic-Proofs/The-Tactic-Language/#let-rec "Documentation for tactic") f : t := e` adds a recursive definition `f` to the current goal. The syntax is the same as term-mode `[let rec](Tactic-Proofs/The-Tactic-Language/#let-rec "Documentation for tactic")`.
The tactic supports all the same syntax variants and options as the `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` term.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticLetI__ "Permalink")tactic
```
[letI](Tactic-Proofs/The-Tactic-Language/#letI "Documentation for tactic")
```

`[letI](Tactic-Proofs/The-Tactic-Language/#letI "Documentation for tactic")` behaves like `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")`, but inlines the value instead of producing a `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` term.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticLet'__ "Permalink")tactic
```
[let'](Tactic-Proofs/The-Tactic-Language/#let___ "Documentation for tactic")
```

Similar to `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")`, but using `[refine'](Tactic-Proofs/Tactic-Reference/#refine___ "Documentation for tactic")`
##  14.3.5. Configuration[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-config "Permalink")
Many tactics are configurable. By convention, tactics share a configuration syntax, described using `optConfig`. The specific options available to each tactic are described in the tactic's documentation.
syntaxTactic Configuration
A tactic configuration consists of zero or more configuration items:

```
[Configuration options for tactics. optConfig](Tactic-Proofs/The-Tactic-Language/#Lean___Parser___Tactic___optConfig-next) ::=
    Configuration options for tactics. A configuration item for a tactic configuration. configItem*
```

syntaxTactic Configuration Items
Each configuration item has a name that corresponds to an underlying tactic option. Boolean options may be enabled or disabled using prefix `+` and `-`:

```
A configuration item for a tactic configuration. configItem ::=
    A configuration item for a tactic configuration. `+opt` is short for `(opt := true)`. It sets the `opt` configuration option to `true`.
+ident
```

```
A configuration item for a tactic configuration. configItem ::= ...
    | A configuration item for a tactic configuration. `-opt` is short for `(opt := false)`. It sets the `opt` configuration option to `false`.
-ident
```

Options may be assigned specific values using a syntax similar to that for named function arguments:

```
A configuration item for a tactic configuration. configItem ::= ...
    | A configuration item for a tactic configuration. `(opt := val)` sets the `opt` configuration option to `val`.

As a special case, `(config := ...)` sets the entire configuration.
(ident := term)
```

Finally, the name `config` is reserved; it is used to pass an entire set of options as a data structure. The specific type expected depends on the tactic.

```
A configuration item for a tactic configuration. configItem ::= ...
    | A configuration item for a tactic configuration. `(opt := val)` sets the `opt` configuration option to `val`.

As a special case, `(config := ...)` sets the entire configuration.
(config := term)
```

##  14.3.6. Namespace and Option Management[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-language-namespaces-options "Permalink")
Namespaces and options can be adjusted in tactic scripts using the same syntax as in terms.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.set_option "Permalink")tactic
```
[set_option](Tactic-Proofs/The-Tactic-Language/#set_option "Documentation for tactic")
```

`set_option opt val in tacs` (the tactic) acts like `set_option opt val` at the command level, but it sets the option only within the tactics `tacs`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.open "Permalink")tactic
```
[open](Tactic-Proofs/The-Tactic-Language/#open "Documentation for tactic")
```

`open Foo in tacs` (the tactic) acts like `open Foo` at command level, but it opens a namespace only within the tactics `tacs`.
###  14.3.6.1. Controlling Unfolding[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-language-unfolding "Permalink")
By default, only definitions marked reducible are unfolded, except when checking definitional equality. These operators allow this default to be adjusted for some part of a tactic script.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.withReducibleAndInstances "Permalink")tactic
```
with_reducible_and_instances
```

`with_reducible_and_instances tacs` executes `tacs` using the `.instances` transparency setting. In this setting only definitions tagged as `[reducible]` or type class instances are unfolded.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.withReducible "Permalink")tactic
```
with_reducible
```

`with_reducible tacs` executes `tacs` using the reducible transparency setting. In this setting only definitions tagged as `[reducible]` are unfolded.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.withUnfoldingAll "Permalink")tactic
```
with_unfolding_all
```

`with_unfolding_all tacs` executes `tacs` using the `.all` transparency setting. In this setting all definitions that are not opaque are unfolded.
[←14.2. Reading Proof States](Tactic-Proofs/Reading-Proof-States/#proof-states "14.2. Reading Proof States")[14.4. Options→](Tactic-Proofs/Options/#tactic-language-options "14.4. Options")

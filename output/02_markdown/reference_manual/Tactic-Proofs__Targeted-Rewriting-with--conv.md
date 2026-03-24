[←14.5. Tactic Reference](Tactic-Proofs/Tactic-Reference/#tactic-ref "14.5. Tactic Reference")[14.7. Naming Bound Variables→](Tactic-Proofs/Naming-Bound-Variables/#bound-variable-name-hints "14.7. Naming Bound Variables")
#  14.6. Targeted Rewriting with `[conv](Tactic-Proofs/Targeted-Rewriting-with--conv/#conv-next "Documentation for tactic")`[🔗](find/?domain=Verso.Genre.Manual.section&name=conv "Permalink")
The `[conv](Tactic-Proofs/Targeted-Rewriting-with--conv/#conv-next "Documentation for tactic")`, or conversion, tactic allows targeted rewriting within a goal. The argument to `[conv](Tactic-Proofs/Targeted-Rewriting-with--conv/#conv-next "Documentation for tactic")` is written in a separate language that interoperates with the main tactic language; it features commands to navigate to specific subterms within the goal along with commands that allow these subterms to be rewritten. `[conv](Tactic-Proofs/Targeted-Rewriting-with--conv/#conv-next "Documentation for tactic")` is useful when rewrites should only be applied in part of a goal (e.g. only on one side of an equality), rather than across the board, or when rewrites should be applied underneath a binder that prevents tactics like `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")` from accessing the term.
The conversion tactic language is very similar to the main tactic language: it uses the same proof states, tactics work primarily on the main goal and may either fail or succeed with a sequence of new goals, and macro expansion is interleaved with tactic execution. Unlike the main tactic language, in which tactics are intended to eventually solve goals, the `[conv](Tactic-Proofs/Targeted-Rewriting-with--conv/#conv-next "Documentation for tactic")` tactic is used to _change_ a goal so that it becomes amenable to further processing in the main tactic language. Goals that are intended to be rewritten with `[conv](Tactic-Proofs/Targeted-Rewriting-with--conv/#conv-next "Documentation for tactic")` are shown with a vertical bar instead of a turnstile.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.Conv.conv "Permalink")tactic
```
[conv](Tactic-Proofs/Targeted-Rewriting-with--conv/#conv-next "Documentation for tactic")
```

`conv => ...` allows the user to perform targeted rewriting on a goal or hypothesis, by focusing on particular subexpressions.
See <https://lean-lang.org/theorem_proving_in_lean4/conv.html> for more details.
Basic forms:
  * `conv => cs` will rewrite the goal with conv tactics `cs`.
  * `conv at h => cs` will rewrite hypothesis `h`.
  * `conv in pat => cs` will rewrite the first subexpression matching `pat` (see `pattern`).


Navigation and Rewriting with `[conv](Tactic-Proofs/Targeted-Rewriting-with--conv/#conv-next "Documentation for tactic")`
In this example, there are multiple instances of addition, and `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")` would by default rewrite the first instance that it encounters. Using `[conv](Tactic-Proofs/Targeted-Rewriting-with--conv/#conv-next "Documentation for tactic")` to navigate to the specific subterm before rewriting leaves `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")` no choice but to rewrite the correct term.
`example (x y z : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : x + (y + z) = (x + z) + y := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")z:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") z[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") z [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y   conv =>x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")z:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")| x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") z[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") z [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y     [lhs](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___lhs "Documentation for conv tactic")x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")z:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")| x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") z[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")     [arg](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___arg "Documentation for conv tactic") 2x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")z:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")| y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") z     [rw](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___convRw__ "Documentation for conv tactic") [Nat.add_comm]x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")z:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")| z [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y   [rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic") [Nat.add_assoc]All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAKE8Ce8Be8Bc8ByYALgJQ7woDUS6VGpAvEpZqVetowEaoBQ88AYwD2AOwBu8egD4+/eDAAWAZ1n8wAJwDm8AEyr46gO7wA2gUIA6MABNrAfWEQIAXVlHT5q7btglSoQLOQA"\))
Rewriting Under Binders with `[conv](Tactic-Proofs/Targeted-Rewriting-with--conv/#conv-next "Documentation for tactic")`
In this example, addition occurs under binders, so `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")` can't be used. However, after using `[conv](Tactic-Proofs/Targeted-Rewriting-with--conv/#conv-next "Documentation for tactic")` to navigate to the function body, it succeeds. The nested use of `[conv](Tactic-Proofs/Targeted-Rewriting-with--conv/#conv-next "Documentation for tactic")` causes control to return to the current position in the term after performing further conversions on one of its subterms. Because the goal is a reflexive equation after rewriting, `[conv](Tactic-Proofs/Targeted-Rewriting-with--conv/#conv-next "Documentation for tactic")` automatically closes it.
`example :     (fun (x y z : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) =>       x + (y + z))     =     (fun x y z =>       (z + x) + y)   := by⊢ (fun x y z => x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") z[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") fun x y z => z [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y   conv =>| (fun x y z => x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") z[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") fun x y z => z [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y     [lhs](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___lhs "Documentation for conv tactic")| fun x y z => x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") z[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")     [intro](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___convIntro___ "Documentation for conv tactic") x y zh.h.hx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")z:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")| x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") z[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")     conv =>       [arg](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___arg "Documentation for conv tactic") 2x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")z:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")| y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") z       [rw](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___convRw__ "Documentation for conv tactic") [Nat.add_comm]x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")z:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")| z [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y     [rw](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___convRw__ "Documentation for conv tactic") [← Nat.add_assoc]h.h.hx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")z:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")| x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") z [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y     [arg](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___arg "Documentation for conv tactic") 1h.h.hx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")z:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")| x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") z     [rw](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___convRw__ "Documentation for conv tactic") [Nat.add_comm]h.h.hx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")z:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")| z [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAuAUPN8AUAzArgO0xHgE94AvJeAOTABcBKeAXgD5V00iBqTUns+vXZomwzLgJFSFVmLQYKPEIx7EhaRE3gAjYuwDGAezwA3Zmw4wAFgGcxASzy0ATofhTyYo6fNz4YZwBzeAAmP2cAd3gAbRpaADowABMkgH0jCAgAXTFImMAEwmo6RJTUsBsbQ30cjgDggEZcqNji5LSM7KA"\))
##  14.6.1. Control Structures[🔗](find/?domain=Verso.Genre.Manual.section&name=conv-control "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.first "Permalink")conv tactic
```
[first](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___first "Documentation for conv tactic")
```

`first | conv | ...` runs each `conv` until one succeeds, or else fails.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.convTry_ "Permalink")conv tactic
```
[try](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___convTry_ "Documentation for conv tactic")
```

`try tac` runs `tac` and succeeds even if `tac` failed.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.%C2%ABconv_<;>_%C2%BB "Permalink")conv tactic
```
[<;>](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv____FLQQ_conv__LT__SEMI__GT___FLQQ_ "Documentation for conv tactic")
```

`tac <;> tac'` runs `tac` on the main goal and `tac'` on each produced goal, concatenating all goals produced by `tac'`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.convRepeat_ "Permalink")conv tactic
```
[repeat](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___convRepeat_ "Documentation for conv tactic")
```

`repeat convs` runs the sequence `convs` repeatedly until it fails to apply.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.skip "Permalink")conv tactic
```
[skip](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___skip "Documentation for conv tactic")
```

`[skip](Tactic-Proofs/Tactic-Reference/#skip "Documentation for tactic")` does nothing.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.nestedConv "Permalink")conv tactic
```
[{ ... }](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___nestedConv "Documentation for conv tactic")
```

`{ convs }` runs the list of `convs` on the current target, and any subgoals that remain are trivially closed by `[skip](Tactic-Proofs/Tactic-Reference/#skip "Documentation for tactic")`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.paren "Permalink")conv tactic
```
[( ... )](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___paren "Documentation for conv tactic")
```

`(convs)` runs the `convs` in sequence on the current list of targets. This is pure grouping with no added effects.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.convDone "Permalink")conv tactic
```
[done](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___convDone "Documentation for conv tactic")
```

`[done](Tactic-Proofs/Tactic-Reference/#done "Documentation for tactic")` succeeds iff there are no goals remaining.
##  14.6.2. Goal Selection[🔗](find/?domain=Verso.Genre.Manual.section&name=conv-goals "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.allGoals "Permalink")conv tactic
```
[all_goals](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___allGoals "Documentation for conv tactic")
```

`all_goals tac` runs `tac` on each goal, concatenating the resulting goals, if any.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.anyGoals "Permalink")conv tactic
```
[any_goals](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___anyGoals "Documentation for conv tactic")
```

`any_goals tac` applies the tactic `tac` to every goal, and succeeds if at least one application succeeds.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.case "Permalink")conv tactic
```
[case ... => ...](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___case "Documentation for conv tactic")
```

  * `case tag => tac` focuses on the goal with case name `tag` and solves it using `tac`, or else fails.
  * `case tag x₁ ... xₙ => tac` additionally renames the `n` most recent hypotheses with inaccessible names to the given names.
  * `case tag₁ | tag₂ => tac` is equivalent to `(case tag₁ => tac); (case tag₂ => tac)`.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.case' "Permalink")conv tactic
```
[case' ... => ...](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___case___ "Documentation for conv tactic")
```

`[case'](Tactic-Proofs/The-Tactic-Language/#case___ "Documentation for tactic")` is similar to the `case tag => tac` tactic, but does not ensure the goal has been solved after applying `tac`, nor admits the goal if `tac` failed. Recall that `[case](Tactic-Proofs/The-Tactic-Language/#case "Documentation for tactic")` closes the goal using `[sorry](Tactic-Proofs/Tactic-Reference/#sorry "Documentation for tactic")` when `tac` fails, and the tactic execution is not interrupted.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.%C2%ABconvNext__=>_%C2%BB "Permalink")conv tactic
```
[next ... => ...](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv____FLQQ_convNext______GT___FLQQ_ "Documentation for conv tactic")
```

`next => tac` focuses on the next goal and solves it using `tac`, or else fails. `next x₁ ... xₙ => tac` additionally renames the `n` most recent hypotheses with inaccessible names to the given names.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.focus "Permalink")conv tactic
```
[focus](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___focus "Documentation for conv tactic")
```

`focus tac` focuses on the main goal, suppressing all other goals, and runs `tac` on it. Usually `· tac`, which enforces that the goal is closed by `tac`, should be preferred.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.%C2%ABconv%C2%B7._%C2%BB "Permalink")conv tactic
```
. ...
```

`· conv` focuses on the main conv goal and tries to solve it using `s`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.%C2%ABconv%C2%B7._%C2%BB "Permalink")conv tactic
```
· ...
```

`· conv` focuses on the main conv goal and tries to solve it using `s`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.failIfSuccess "Permalink")conv tactic
```
[fail_if_success](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___failIfSuccess "Documentation for conv tactic")
```

`fail_if_success t` fails if the tactic `t` succeeds.
##  14.6.3. Navigation[🔗](find/?domain=Verso.Genre.Manual.section&name=conv-nav "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.lhs "Permalink")conv tactic
```
[lhs](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___lhs "Documentation for conv tactic")
```

Traverses into the left subterm of a binary operator.
In general, for an `n`-ary operator, it traverses into the second to last argument. It is a synonym for `arg -2`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.rhs "Permalink")conv tactic
```
[rhs](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___rhs "Documentation for conv tactic")
```

Traverses into the right subterm of a binary operator.
In general, for an `n`-ary operator, it traverses into the last argument. It is a synonym for `arg -1`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.fun "Permalink")conv tactic
```
[fun](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___fun "Documentation for conv tactic")
```

Traverses into the function of a (unary) function application. For example, `| f a b` turns into `| f a`. (Use `arg 0` to traverse into `f`.)
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.congr "Permalink")conv tactic
```
[congr](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___congr "Documentation for conv tactic")
```

Performs one step of "congruence", which takes a term and produces subgoals for all the function arguments. For example, if the target is `f x y` then `[congr](Basic-Propositions/Propositional-Equality/#congr-next "Documentation for congr")` produces two subgoals, one for `x` and one for `y`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.arg "Permalink")conv tactic
```
[arg [@]i](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___arg "Documentation for conv tactic")
```

  * `arg i` traverses into the `i`'th argument of the target. For example if the target is `f a b c d` then `arg 1` traverses to `a` and `arg 3` traverses to `c`. The index may be negative; `arg -1` traverses into the last argument, `arg -2` into the second-to-last argument, and so on.
  * `arg @i` is the same as `arg i` but it counts all arguments instead of just the explicit arguments.
  * `arg 0` traverses into the function. If the target is `f a b c d`, `arg 0` traverses into `f`.


syntaxArguments to `enter`

```
enterArg ::= ...
    | num
```

```
enterArg ::= ...
    | @num
```

```
enterArg ::= ...
    | `binderIdent` matches an `ident` or a `_`. It is used for identifiers in binding
position, where `_` means that the value should be left unnamed and inaccessible.
ident
```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.enter "Permalink")conv tactic
```
[enter](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___enter "Documentation for conv tactic")
```

`enter [arg, ...]` is a compact way to describe a path to a subterm. It is a shorthand for other conv tactics as follows:
  * `enter [i]` is equivalent to `arg i`.
  * `enter [@i]` is equivalent to `arg @i`.
  * `enter [x]` (where `x` is an identifier) is equivalent to `[ext](Tactic-Proofs/Tactic-Reference/#ext "Documentation for tactic") x`.
  * `enter [in e]` (where `e` is a term) is equivalent to `pattern e`. Occurrences can be specified with `enter [in (occs := ...) e]`. For example, given the target `f (g a (fun x => x b))`, `enter [1, 2, x, 1]` will traverse to the subterm `b`.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.pattern "Permalink")conv tactic
```
[pattern](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___pattern "Documentation for conv tactic")
```

  * `pattern pat` traverses to the first subterm of the target that matches `pat`.
  * `pattern (occs := *) pat` traverses to every subterm of the target that matches `pat` which is not contained in another match of `pat`. It generates one subgoal for each matching subterm.
  * `pattern (occs := 1 2 4) pat` matches occurrences `1, 2, 4` of `pat` and produces three subgoals. Occurrences are numbered left to right from the outside in.


Note that skipping an occurrence of `pat` will traverse inside that subexpression, which means it may find more matches and this can affect the numbering of subsequent pattern matches. For example, if we are searching for `f _` in `f (f a) = f b`:
  * `occs := 1 2` (and `occs := *`) returns `| f (f a)` and `| f b`
  * `occs := 2` returns `| f a`
  * `occs := 2 3` returns `| f a` and `| f b`
  * `occs := 1 3` is an error, because after skipping `f b` there is no third match.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.ext "Permalink")conv tactic
```
[ext](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___ext "Documentation for conv tactic")
```

`[ext](Tactic-Proofs/Tactic-Reference/#ext "Documentation for tactic") x` traverses into a binder (a `fun x => e` or `∀ x, e` expression) to target `e`, introducing name `x` in the process.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.convArgs "Permalink")conv tactic
```
[args](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___convArgs "Documentation for conv tactic")
```

`args` traverses into all arguments. Synonym for `[congr](Basic-Propositions/Propositional-Equality/#congr-next "Documentation for congr")`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.convLeft "Permalink")conv tactic
```
[left](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___convLeft "Documentation for conv tactic")
```

`[left](Tactic-Proofs/Tactic-Reference/#left "Documentation for tactic")` traverses into the left argument. Synonym for `lhs`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.convRight "Permalink")conv tactic
```
[right](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___convRight "Documentation for conv tactic")
```

`[right](Tactic-Proofs/Tactic-Reference/#right "Documentation for tactic")` traverses into the right argument. Synonym for `rhs`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.convIntro___ "Permalink")conv tactic
```
[intro](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___convIntro___ "Documentation for conv tactic")
```

`[intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic")` traverses into binders. Synonym for `[ext](Tactic-Proofs/Tactic-Reference/#ext "Documentation for tactic")`.
##  14.6.4. Changing the Goal[🔗](find/?domain=Verso.Genre.Manual.section&name=conv-change "Permalink")
###  14.6.4.1. Reduction[🔗](find/?domain=Verso.Genre.Manual.section&name=conv-reduction "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.cbv "Permalink")conv tactic
```
[cbv](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___cbv "Documentation for conv tactic")
```

`cbv` performs simplification that closely mimics call-by-value evaluation. It reduces the target term by unfolding definitions using their defining equations and applying matcher equations. The unfolding is propositional, so `cbv` also works with functions defined via well-founded recursion or partial fixpoints.
The proofs produced by `cbv` only use the three standard axioms. In particular, they do not require trust in the correctness of the code generator.
This tactic is experimental and its behavior is likely to change in upcoming releases of Lean.
The `cbv` Tactic
The `[cbv](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___cbv "Documentation for conv tactic")` tactic can be used to reduce functions, including ones that are defined via [well-founded recursion](Definitions/Recursive-Definitions/#well-founded-recursion), which are otherwise irreducible. Ordinarily, `[f](Tactic-Proofs/Targeted-Rewriting-with--conv/#f-_LPAR_in-The--cbv--Tactic_RPAR_ "Definition of example")` is only propositionally equal to its unfolding, so `[rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")` can't prove the equality `[f](Tactic-Proofs/Targeted-Rewriting-with--conv/#f-_LPAR_in-The--cbv--Tactic_RPAR_ "Definition of example") 5 = 5`:
`def f (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") n [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | 0 => 0   | n + 1 => [f](Tactic-Proofs/Targeted-Rewriting-with--conv/#f-_LPAR_in-The--cbv--Tactic_RPAR_ "Definition of example") n + 1 termination_by (n,0) ``example : [f](Tactic-Proofs/Targeted-Rewriting-with--conv/#f-_LPAR_in-The--cbv--Tactic_RPAR_ "Definition of example") 5 = 5 := by⊢ [f](Tactic-Proofs/Targeted-Rewriting-with--conv/#f-_LPAR_in-The--cbv--Tactic_RPAR_ "Definition of example") 5 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 5 `Tactic `rfl` failed: The left-hand side   [f](Tactic-Proofs/Targeted-Rewriting-with--conv/#f-_LPAR_in-The--cbv--Tactic_RPAR_ "Definition of example") 5 is not definitionally equal to the right-hand side   5  ⊢ [f](Tactic-Proofs/Targeted-Rewriting-with--conv/#f-_LPAR_in-The--cbv--Tactic_RPAR_ "Definition of example") 5 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 5`[rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")⊢ [f](Tactic-Proofs/Targeted-Rewriting-with--conv/#f-_LPAR_in-The--cbv--Tactic_RPAR_ "Definition of example") 5 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 5 `
```
Tactic `rfl` failed: The left-hand side
  [f](Tactic-Proofs/Targeted-Rewriting-with--conv/#f-_LPAR_in-The--cbv--Tactic_RPAR_ "Definition of example") 5
is not definitionally equal to the right-hand side
  5

⊢ [f](Tactic-Proofs/Targeted-Rewriting-with--conv/#f-_LPAR_in-The--cbv--Tactic_RPAR_ "Definition of example") 5 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 5
```

Using `[cbv](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___cbv "Documentation for conv tactic")` on the left-hand side of the equality, the statement can be made true:
`example : [f](Tactic-Proofs/Targeted-Rewriting-with--conv/#f-_LPAR_in-The--cbv--Tactic_RPAR_ "Definition of example") 5 = 5 := by⊢ [f](Tactic-Proofs/Targeted-Rewriting-with--conv/#f-_LPAR_in-The--cbv--Tactic_RPAR_ "Definition of example") 5 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 5   conv =>| [f](Tactic-Proofs/Targeted-Rewriting-with--conv/#f-_LPAR_in-The--cbv--Tactic_RPAR_ "Definition of example") 5 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 5     [lhs](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___lhs "Documentation for conv tactic")| [f](Tactic-Proofs/Targeted-Rewriting-with--conv/#f-_LPAR_in-The--cbv--Tactic_RPAR_ "Definition of example") 5     [cbv](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___cbv "Documentation for conv tactic")| 5 `
[Live ↪](javascript:openLiveLink\("CYUwZgBJAUB2EC4IDkCGAXAlIgvAKAggFsMBjACwngHcBLdcgiAHwgAYIcA+dp1+ANQQAjJx6RBIvOhAAnIrVgZaAe1gB9AEYBPCHAA0bTHjwBaUxAAq5EBAAGpTQDc7EdKlLpapCLQDOEAAOsiB+ILDoADa6IAAegXK0ROHukfoQqLDAGRDUqLKwigDmvgH+fgCuINnUNvD0pRAVYcAAdGYW1v4QKoFeahDA/qiakaFuNrn5hbBFCHhh6Oq9/fCOTq15BcVQqJFhJnGoRIFjiFAQAKycV7gQOkykak5iTISR5H5vEOtAA"\))
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.whnf "Permalink")conv tactic
```
[whnf](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___whnf "Documentation for conv tactic")
```

Reduces the target to Weak Head Normal Form. This reduces definitions in "head position" until a constructor is exposed. For example, `[List.map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map") f [a, b, c]` weak head normalizes to `f a :: [List.map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map") f [b, c]`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.reduce "Permalink")conv tactic
```
[reduce](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___reduce "Documentation for conv tactic")
```

Puts term in normal form, this tactic is meant for debugging purposes only.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.zeta "Permalink")conv tactic
```
[zeta](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___zeta "Documentation for conv tactic")
```

Expands let-declarations and let-variables.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.delta "Permalink")conv tactic
```
[delta](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___delta "Documentation for conv tactic")
```

`delta id1 id2 ...` unfolds all occurrences of `id1`, `id2`, ... in the target. Like the `[delta](Tactic-Proofs/Tactic-Reference/#delta "Documentation for tactic")` tactic, this ignores any definitional equations and uses primitive delta-reduction instead, which may result in leaking implementation details. Users should prefer `[unfold](Tactic-Proofs/Tactic-Reference/#unfold "Documentation for tactic")` for unfolding definitions.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.unfold "Permalink")conv tactic
```
[unfold](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___unfold "Documentation for conv tactic")
```

  * `[unfold](Tactic-Proofs/Tactic-Reference/#unfold "Documentation for tactic") id` unfolds all occurrences of definition `id` in the target.
  * `unfold id1 id2 ...` is equivalent to `unfold id1; unfold id2; ...`.


Definitions can be either global or local definitions.
For non-recursive global definitions, this tactic is identical to `[delta](Tactic-Proofs/Tactic-Reference/#delta "Documentation for tactic")`. For recursive global definitions, it uses the "unfolding lemma" `id.eq_def`, which is generated for each recursive definition, to unfold according to the recursive definition given by the user. Only one level of unfolding is performed, in contrast to `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") only [id]`, which unfolds definition `id` recursively.
This is the `conv` version of the `[unfold](Tactic-Proofs/Tactic-Reference/#unfold "Documentation for tactic")` tactic.
###  14.6.4.2. Simplification[🔗](find/?domain=Verso.Genre.Manual.section&name=conv-simp "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.simp "Permalink")conv tactic
```
[simp](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___simp "Documentation for conv tactic")
```

`[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [thm]` performs simplification using `thm` and marked `@[simp]` lemmas. See the `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` tactic for more information.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.dsimp "Permalink")conv tactic
```
[dsimp](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___dsimp "Documentation for conv tactic")
```

`[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")` is the definitional simplifier in `conv`-mode. It differs from `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` in that it only applies theorems that hold by reflexivity.
Examples:
`example (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")): (0 + 0) = a - a := bya:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") a   conv =>a:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")| 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") a     [lhs](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___lhs "Documentation for conv tactic")a:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")| 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0     [dsimp](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___dsimp "Documentation for conv tactic")a:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")| 0     [rw](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___convRw__ "Documentation for conv tactic") [← Nat.sub_self a]a:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")| a [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") a `
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.simpMatch "Permalink")conv tactic
```
[simp_match](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___simpMatch "Documentation for conv tactic")
```

`simp_match` simplifies match expressions. For example,
`[match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") [a, b] [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") | [] => 0 | hd :: tl => hd`
simplifies to `a`.
###  14.6.4.3. Rewriting[🔗](find/?domain=Verso.Genre.Manual.section&name=conv-rw "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.change "Permalink")conv tactic
```
[change](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___change "Documentation for conv tactic")
```

`[change](Tactic-Proofs/Tactic-Reference/#change "Documentation for tactic") t'` replaces the target `t` with `t'`, assuming `t` and `t'` are definitionally equal.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.rewrite "Permalink")conv tactic
```
[rewrite](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___rewrite "Documentation for conv tactic")
```

`[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic") [thm]` rewrites the target using `thm`. See the `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")` tactic for more information.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.convRw__ "Permalink")conv tactic
```
[rw](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___convRw__ "Documentation for conv tactic")
```

`[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic") [rules]` applies the given list of rewrite rules to the target. See the `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")` tactic for more information.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.convErw__ "Permalink")conv tactic
```
[erw](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___convErw__ "Documentation for conv tactic")
```

`[erw](Tactic-Proofs/Tactic-Reference/#erw "Documentation for tactic") [rules]` is a shorthand for `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic") (transparency := .default) [rules]`. This does rewriting up to unfolding of regular definitions (by comparison to regular `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")` which only unfolds `@[reducible]` definitions).
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.convApply_ "Permalink")conv tactic
```
[apply](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___convApply_ "Documentation for conv tactic")
```

The `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") thm` conv tactic is the same as `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") thm` the tactic. There are no restrictions on `thm`, but strange results may occur if `thm` cannot be reasonably interpreted as proving one equality from a list of others.
##  14.6.5. Nested Tactics[🔗](find/?domain=Verso.Genre.Manual.section&name=conv-nested "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.Conv.convTactic "Permalink")tactic
```
conv'
```

Executes the given conv block without converting regular goal into a `conv` goal.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.nestedTactic "Permalink")conv tactic
```
[tactic](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___nestedTactic "Documentation for conv tactic")
```

Focuses, converts the `conv` goal `⊢ lhs` into a regular goal `⊢ lhs = rhs`, and then executes the given tactic block.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.nestedTacticCore "Permalink")conv tactic
```
[tactic'](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___nestedTacticCore "Documentation for conv tactic")
```

Executes the given tactic block without converting `conv` goal into a regular goal.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.Conv.convTactic "Permalink")tactic
```
conv'
```

Executes the given conv block without converting regular goal into a `conv` goal.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.convConvSeq "Permalink")conv tactic
```
[conv => ...](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___convConvSeq "Documentation for conv tactic")
```

`conv => cs` runs `cs` in sequence on the target `t`, resulting in `t'`, which becomes the new target subgoal.
##  14.6.6. Debugging Utilities[🔗](find/?domain=Verso.Genre.Manual.section&name=conv-debug "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.convTrace_state "Permalink")conv tactic
```
[trace_state](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___convTrace_state "Documentation for conv tactic")
```

`[trace_state](Tactic-Proofs/Tactic-Reference/#trace_state "Documentation for tactic")` prints the current goal state.
##  14.6.7. Other[🔗](find/?domain=Verso.Genre.Manual.section&name=conv-other "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.convRfl "Permalink")conv tactic
```
[rfl](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___convRfl "Documentation for conv tactic")
```

`[rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")` closes one conv goal "trivially", by using reflexivity (that is, no rewriting).
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic.conv&name=Lean.Parser.Tactic.Conv.normCast "Permalink")conv tactic
```
[norm_cast](Tactic-Proofs/Targeted-Rewriting-with--conv/#Lean___Parser___Tactic___Conv___normCast "Documentation for conv tactic")
```

`[norm_cast](Tactic-Proofs/Tactic-Reference/#norm_cast "Documentation for tactic")` tactic in `conv` mode.
[←14.5. Tactic Reference](Tactic-Proofs/Tactic-Reference/#tactic-ref "14.5. Tactic Reference")[14.7. Naming Bound Variables→](Tactic-Proofs/Naming-Bound-Variables/#bound-variable-name-hints "14.7. Naming Bound Variables")

[←14.4. Options](Tactic-Proofs/Options/#tactic-language-options "14.4. Options")[14.6. Targeted Rewriting with conv→](Tactic-Proofs/Targeted-Rewriting-with--conv/#conv "14.6. Targeted Rewriting with conv")
#  14.5. Tactic Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref "Permalink")
##  14.5.1. Classical Logic[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-classical "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.classical "Permalink")tactic
```
[classical](Tactic-Proofs/Tactic-Reference/#classical "Documentation for tactic")
```

`classical tacs` runs `tacs` in a scope where `Classical.propDecidable` is a low priority local instance.
Note that `[classical](Tactic-Proofs/Tactic-Reference/#classical "Documentation for tactic")` is a scoping tactic: it adds the instance only within the scope of the tactic.
##  14.5.2. Assumptions[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-assumptions "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.assumption "Permalink")tactic
```
[assumption](Tactic-Proofs/Tactic-Reference/#assumption "Documentation for tactic")
```

`[assumption](Tactic-Proofs/Tactic-Reference/#assumption "Documentation for tactic")` tries to solve the main goal using a hypothesis of compatible type, or else fails. Note also the `‹t›` term notation, which is a shorthand for `show t by [assumption](Tactic-Proofs/Tactic-Reference/#assumption "Documentation for tactic")`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.applyAssumption "Permalink")tactic
```
[apply_assumption](Tactic-Proofs/Tactic-Reference/#apply_assumption "Documentation for tactic")
```

`[apply_assumption](Tactic-Proofs/Tactic-Reference/#apply_assumption "Documentation for tactic")` looks for an assumption of the form `... → ∀ _, ... → head` where `head` matches the current goal.
You can specify additional rules to apply using `apply_assumption [...]`. By default `[apply_assumption](Tactic-Proofs/Tactic-Reference/#apply_assumption "Documentation for tactic")` will also try `[rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`, `trivial`, `[congrFun](Basic-Propositions/Propositional-Equality/#congrFun "Documentation for congrFun")`, and `[congrArg](Basic-Propositions/Propositional-Equality/#congrArg "Documentation for congrArg")`. If you don't want these, or don't want to use all hypotheses, use `apply_assumption only [...]`. You can use `[apply_assumption](Tactic-Proofs/Tactic-Reference/#apply_assumption "Documentation for tactic") [-h]` to omit a local hypothesis. You can use `apply_assumption using [a₁, ...]` to use all lemmas which have been labelled with the attributes `aᵢ` (these attributes must be created using `register_label_attr`).
`[apply_assumption](Tactic-Proofs/Tactic-Reference/#apply_assumption "Documentation for tactic")` will use consequences of local hypotheses obtained via `[symm](Tactic-Proofs/Tactic-Reference/#symm "Documentation for tactic")`.
If `[apply_assumption](Tactic-Proofs/Tactic-Reference/#apply_assumption "Documentation for tactic")` fails, it will call `[exfalso](Tactic-Proofs/Tactic-Reference/#exfalso "Documentation for tactic")` and try again. Thus if there is an assumption of the form `P → ¬ Q`, the new tactic state will have two goals, `P` and `Q`.
You can pass a further configuration via the syntax `apply_rules (config := {...}) lemmas`. The options supported are the same as for `[solve_by_elim](Tactic-Proofs/Tactic-Reference/#solve_by_elim "Documentation for tactic")` (and include all the options for `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic")`).
##  14.5.3. Quantifiers[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-quantifiers "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.%C2%ABtacticExists_,,%C2%BB "Permalink")tactic
```
[exists](Tactic-Proofs/Tactic-Reference/#exists "Documentation for tactic")
```

`exists e₁, e₂, ...` is shorthand for `refine ⟨e₁, e₂, ...⟩; try trivial`. It is useful for existential goals.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.intro "Permalink")tactic
```
[intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic")
```

Introduces one or more hypotheses, optionally naming and/or pattern-matching them. For each hypothesis to be introduced, the remaining main goal's target type must be a `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` or function type.
  * `intro` by itself introduces one anonymous hypothesis, which can be accessed by e.g. `[assumption](Tactic-Proofs/Tactic-Reference/#assumption "Documentation for tactic")`. It is equivalent to `[intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") _`.
  * `[intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") x y` introduces two hypotheses and names them. Individual hypotheses can be anonymized via `_`, given a type ascription, or matched against a pattern:
`intro (a, b) -- ..., a : α, b : β ⊢ ...`
  * `[intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") rfl` is short for `intro h; subst h`, if `h` is an equality where the left-hand or right-hand side is a variable.
  * Alternatively, `intro` can be combined with pattern matching much like `fun`:

```
intro
| n + 1, 0 => tac
| ...

```



[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.intros "Permalink")tactic
```
[intros](Tactic-Proofs/Tactic-Reference/#intros "Documentation for tactic")
```

`[intros](Tactic-Proofs/Tactic-Reference/#intros "Documentation for tactic")` repeatedly applies `[intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic")` to introduce zero or more hypotheses until the goal is no longer a _binding expression_ (i.e., a universal quantifier, function type, implication, or `have`/`[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")`), without performing any definitional reductions (no unfolding, beta, eta, etc.). The introduced hypotheses receive inaccessible (hygienic) names.
`[intros](Tactic-Proofs/Tactic-Reference/#intros "Documentation for tactic") x y z` is equivalent to `[intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") x y z` and exists only for historical reasons. The `[intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic")` tactic should be preferred in this case.
**Properties and relations**
  * `[intros](Tactic-Proofs/Tactic-Reference/#intros "Documentation for tactic")` succeeds even when it introduces no hypotheses.
  * `[repeat](Tactic-Proofs/The-Tactic-Language/#repeat "Documentation for tactic") [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic")` is like `[intros](Tactic-Proofs/Tactic-Reference/#intros "Documentation for tactic")`, but it performs definitional reductions to expose binders, and as such it may introduce more hypotheses than `[intros](Tactic-Proofs/Tactic-Reference/#intros "Documentation for tactic")`.
  * `[intros](Tactic-Proofs/Tactic-Reference/#intros "Documentation for tactic")` is equivalent to `intro _ _ … _`, with the fewest trailing `_` placeholders needed so that the goal is no longer a binding expression. The trailing introductions do not perform any definitional reductions.


**Examples**
Implications:
`example (p q : Prop) : p → q → p := byp:Propq:Prop⊢ p → q → p   [intros](Tactic-Proofs/Tactic-Reference/#intros "Documentation for tactic")p:Propq:Propa✝¹:pa✝:q⊢ p   /- Tactic state      a✝¹ : p      a✝ : q      ⊢ p      -/   [assumption](Tactic-Proofs/Tactic-Reference/#assumption "Documentation for tactic")All goals completed! 🐙 `
Let-bindings:
`example : let n := 1; let k := 2; n + k = 3 := by⊢ let n := 1; let k := 2; n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 3   [intros](Tactic-Proofs/Tactic-Reference/#intros "Documentation for tactic")n✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 1k✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 2⊢ n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k✝ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 3   /- n✝ : Nat := 1      k✝ : Nat := 2      ⊢ n✝ + k✝ = 3 -/   [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 `
Does not unfold definitions:
`def AllEven (f : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) := ∀ n, f n % 2 = 0  `declaration uses `sorry``example : ∀ (f : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), AllEven f → AllEven (fun k => f (k + 1)) := by⊢ ∀ (f : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), AllEven f → AllEven fun k => f [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [intros](Tactic-Proofs/Tactic-Reference/#intros "Documentation for tactic")f✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:AllEven f✝⊢ AllEven fun k => f✝ [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") /- Tactic state f✝ : Nat → Nat a✝ : AllEven f✝ ⊢ AllEven fun k => f✝ (k + 1) -/ [sorry](Tactic-Proofs/Tactic-Reference/#sorry "Documentation for tactic")All goals completed! 🐙 `
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.rintro "Permalink")tactic
```
[rintro](Tactic-Proofs/Tactic-Reference/#rintro "Documentation for tactic")
```

The `[rintro](Tactic-Proofs/Tactic-Reference/#rintro "Documentation for tactic")` tactic is a combination of the `[intros](Tactic-Proofs/Tactic-Reference/#intros "Documentation for tactic")` tactic with `[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic")` to allow for destructuring patterns while introducing variables. See `[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic")` for a description of supported patterns. For example, `[rintro](Tactic-Proofs/Tactic-Reference/#rintro "Documentation for tactic") (a | ⟨b, c⟩) ⟨d, e⟩` will introduce two variables, and then do case splits on both of them producing two subgoals, one with variables `a d e` and the other with `b c d e`.
`[rintro](Tactic-Proofs/Tactic-Reference/#rintro "Documentation for tactic")`, unlike `[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic")`, also supports the form `(x y : ty)` for introducing and type-ascripting multiple variables at once, similar to binders.
##  14.5.4. Relations[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-relations "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticRfl "Permalink")tactic
```
[rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")
```

This tactic applies to a goal whose target has the form `x ~ x`, where `~` is equality, heterogeneous equality or any relation that has a reflexivity lemma tagged with the attribute @[refl].
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticRfl' "Permalink")tactic
```
[rfl'](Tactic-Proofs/Tactic-Reference/#rfl___ "Documentation for tactic")
```

`[rfl'](Tactic-Proofs/Tactic-Reference/#rfl___ "Documentation for tactic")` is similar to `[rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`, but disables smart unfolding and unfolds all kinds of definitions, theorems included (relevant for declarations defined by well-founded recursion).
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.applyRfl "Permalink")tactic
```
[apply_rfl](Tactic-Proofs/Tactic-Reference/#apply_rfl "Documentation for tactic")
```

The same as `[rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`, but without trying `[eq_refl](Tactic-Proofs/Tactic-Reference/#eq_refl "Documentation for tactic")` at the end.
attributeReflexive Relations
The `refl` attribute marks a lemma as a proof of reflexivity for some relation. These lemmas are used by the `[rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")`, `[rfl'](Tactic-Proofs/Tactic-Reference/#rfl___ "Documentation for tactic")`, and `[apply_rfl](Tactic-Proofs/Tactic-Reference/#apply_rfl "Documentation for tactic")` tactics.

```
attr ::= ...
    | refl
```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.symm "Permalink")tactic
```
[symm](Tactic-Proofs/Tactic-Reference/#symm "Documentation for tactic")
```

  * `[symm](Tactic-Proofs/Tactic-Reference/#symm "Documentation for tactic")` applies to a goal whose target has the form `t ~ u` where `~` is a symmetric relation, that is, a relation which has a symmetry lemma tagged with the attribute [symm]. It replaces the target with `u ~ t`.
  * `[symm](Tactic-Proofs/Tactic-Reference/#symm "Documentation for tactic") at h` will rewrite a hypothesis `h : t ~ u` to `h : u ~ t`.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.symmSaturate "Permalink")tactic
```
[symm_saturate](Tactic-Proofs/Tactic-Reference/#symm_saturate "Documentation for tactic")
```

For every hypothesis `h : a ~ b` where a `@[symm]` lemma is available, add a hypothesis `h_symm : b ~ a`.
attributeSymmetric Relations
The `symm` attribute marks a lemma as a proof that a relation is symmetric. These lemmas are used by the `[symm](Tactic-Proofs/Tactic-Reference/#symm "Documentation for tactic")` and `[symm_saturate](Tactic-Proofs/Tactic-Reference/#symm_saturate "Documentation for tactic")` tactics.

```
attr ::= ...
    | symm
```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.calcTactic "Permalink")tactic
```
[calc](Tactic-Proofs/Tactic-Reference/#calc "Documentation for tactic")
```

Step-wise reasoning over transitive relations.

```
calc
  a = b := pab
  b = c := pbc
  ...
  y = z := pyz

```

proves `a = z` from the given step-wise proofs. `=` can be replaced with any relation implementing the typeclass `[Trans](Tactic-Proofs/Tactic-Reference/#Trans___mk "Documentation for Trans")`. Instead of repeating the right- hand sides, subsequent left-hand sides can be replaced with `_`.

```
calc
  a = b := pab
  _ = c := pbc
  ...
  _ = z := pyz

```

It is also possible to write the _first_ relation as `<lhs>\n  _ = <rhs> := <proof>`. This is useful for aligning relation symbols, especially on longer identifiers:

```
calc abc
  _ = bce := pabce
  _ = cef := pbcef
  ...
  _ = xyz := pwxyz

```

`[calc](Tactic-Proofs/Tactic-Reference/#calc "Documentation for tactic")` works as a term, as a tactic or as a `conv` tactic.
See [Theorem Proving in Lean 4](https://lean-lang.org/theorem_proving_in_lean4/quantifiers_and_equality.html#calculational-proofs) for more information.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Trans.mk "Permalink")type class
```


Trans.{u, v, w, u_1, u_2, u_3} {α : Sort u_1} {β : Sort u_2}
  {γ : Sort u_3} (r : α → β → Sort u) (s : β → γ → Sort v)
  (t : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (α → γ → Sort w)) :
  Sort (max (max (max (max (max (max 1 u) u_1) u_2) u_3) v) w)


Trans.{u, v, w, u_1, u_2, u_3}
  {α : Sort u_1} {β : Sort u_2}
  {γ : Sort u_3} (r : α → β → Sort u)
  (s : β → γ → Sort v)
  (t : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (α → γ → Sort w)) :
  Sort
    (max
        (max
            (max
                (max (max (max 1 u) u_1)
                    u_2)
                u_3)
            v)
        w)


```

Transitive chaining of proofs, used e.g. by `[calc](Tactic-Proofs/Tactic-Reference/#calc "Documentation for tactic")`.
It takes two relations `r` and `s` as "input", and produces an "output" relation `t`, with the property that `r a b` and `s b c` implies `t a c`. The `[calc](Tactic-Proofs/Tactic-Reference/#calc "Documentation for tactic")` tactic uses this so that when it sees a chain with `a ≤ b` and `b < c` it knows that this should be a proof of `a < c` because there is an instance `Trans (·≤·) (·<·) (·<·)`.
#  Instance Constructor

```
[Trans.mk](Tactic-Proofs/Tactic-Reference/#Trans___mk "Documentation for Trans.mk").{u, v, w, u_1, u_2, u_3}
```

#  Methods

```
trans : {a : α} → {b : β} → {c : γ} → r a b → s b c → t a c
```

Compose two proofs by transitivity, generalized over the relations involved.
###  14.5.4.1. Equality[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-equality "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.subst "Permalink")tactic
```
[subst](Tactic-Proofs/Tactic-Reference/#subst "Documentation for tactic")
```

`subst x...` substitutes each hypothesis `x` with a definition found in the local context, then eliminates the hypothesis.
  * If `x` is a local definition, then its definition is used.
  * Otherwise, if there is a hypothesis of the form `x = e` or `e = x`, then `e` is used for the definition of `x`.


If `h : a = b`, then `[subst](Tactic-Proofs/Tactic-Reference/#subst "Documentation for tactic") h` may be used if either `a` or `b` unfolds to a local hypothesis. This is similar to the `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") h` tactic.
See also: `[subst_vars](Tactic-Proofs/Tactic-Reference/#subst_vars "Documentation for tactic")` for substituting all local hypotheses that have a defining equation.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.substEqs "Permalink")tactic
```
[subst_eqs](Tactic-Proofs/Tactic-Reference/#subst_eqs "Documentation for tactic")
```

`subst_eq` repeatedly substitutes according to the equality proof hypotheses in the context, replacing the left side of the equality with the right, until no more progress can be made.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.substVars "Permalink")tactic
```
[subst_vars](Tactic-Proofs/Tactic-Reference/#subst_vars "Documentation for tactic")
```

Applies `[subst](Tactic-Proofs/Tactic-Reference/#subst "Documentation for tactic")` to all hypotheses of the form `h : x = t` or `h : t = x`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.congr "Permalink")tactic
```
[congr](Tactic-Proofs/Tactic-Reference/#congr "Documentation for tactic")
```

Apply congruence (recursively) to goals of the form `⊢ f as = f bs` and `⊢ f as ≍ f bs`. The optional parameter is the depth of the recursive applications. This is useful when `[congr](Basic-Propositions/Propositional-Equality/#congr-next "Documentation for congr")` is too aggressive in breaking down the goal. For example, given `⊢ f (g (x + y)) = f (g (y + x))`, `[congr](Basic-Propositions/Propositional-Equality/#congr-next "Documentation for congr")` produces the goals `⊢ x = y` and `⊢ y = x`, while `[congr](Tactic-Proofs/Tactic-Reference/#congr "Documentation for tactic") 2` produces the intended `⊢ x + y = y + x`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.eqRefl "Permalink")tactic
```
[eq_refl](Tactic-Proofs/Tactic-Reference/#eq_refl "Documentation for tactic")
```

`[eq_refl](Tactic-Proofs/Tactic-Reference/#eq_refl "Documentation for tactic")` is equivalent to `[exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic") rfl`, but has a few optimizations.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.acRfl "Permalink")tactic
```
[ac_rfl](Tactic-Proofs/Tactic-Reference/#ac_rfl "Documentation for tactic")
```

`[ac_rfl](Tactic-Proofs/Tactic-Reference/#ac_rfl "Documentation for tactic")` proves equalities up to application of an associative and commutative operator.
`instance : Std.Associative (α := [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (.+.) := ⟨Nat.add_assoc⟩ instance : Std.Commutative (α := [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (.+.) := ⟨Nat.add_comm⟩  example (a b c d : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : a + b + c + d = d + (b + c) + a := bya:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")b:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")c:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")d:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a [ac_rfl](Tactic-Proofs/Tactic-Reference/#ac_rfl "Documentation for tactic")All goals completed! 🐙 `
##  14.5.5. Associativity and Commutativity[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-associativity-commutativity "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticAc_nf_ "Permalink")tactic
```
[ac_nf](Tactic-Proofs/Tactic-Reference/#ac_nf "Documentation for tactic")
```

`[ac_nf](Tactic-Proofs/Tactic-Reference/#ac_nf "Documentation for tactic")` normalizes equalities up to application of an associative and commutative operator.
  * `[ac_nf](Tactic-Proofs/Tactic-Reference/#ac_nf "Documentation for tactic")` normalizes all hypotheses and the goal target of the goal.
  * `[ac_nf](Tactic-Proofs/Tactic-Reference/#ac_nf "Documentation for tactic") at l` normalizes at location(s) `l`, where `l` is either `*` or a list of hypotheses in the local context. In the latter case, a turnstile `⊢` or `|-` can also be used, to signify the target of the goal.

`instance : Std.Associative (α := [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (.+.) := ⟨Nat.add_assoc⟩ instance : Std.Commutative (α := [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (.+.) := ⟨Nat.add_comm⟩  example (a b c d : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : a + b + c + d = d + (b + c) + a := bya:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")b:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")c:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")d:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") d [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") d [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a  [ac_nf](Tactic-Proofs/Tactic-Reference/#ac_nf "Documentation for tactic")All goals completed! 🐙  -- goal: a + (b + (c + d)) = a + (b + (c + d)) `
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.acNf0 "Permalink")tactic
```
[ac_nf0](Tactic-Proofs/Tactic-Reference/#ac_nf0 "Documentation for tactic")
```

Implementation of `[ac_nf](Tactic-Proofs/Tactic-Reference/#ac_nf "Documentation for tactic")` (the full `[ac_nf](Tactic-Proofs/Tactic-Reference/#ac_nf "Documentation for tactic")` calls `trivial` afterwards).
##  14.5.6. Lemmas[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-lemmas "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.exact "Permalink")tactic
```
[exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic")
```

`[exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic") e` closes the main goal if its target type matches that of `e`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.apply "Permalink")tactic
```
[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic")
```

`[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") e` tries to match the current goal against the conclusion of `e`'s type. If it succeeds, then the tactic returns as many subgoals as the number of premises that have not been fixed by type inference or type class resolution. Non-dependent premises are added before dependent ones.
The `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic")` tactic uses higher-order pattern matching, type class resolution, and first-order unification with dependent types.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.refine "Permalink")tactic
```
[refine](Tactic-Proofs/Tactic-Reference/#refine "Documentation for tactic")
```

`[refine](Tactic-Proofs/Tactic-Reference/#refine "Documentation for tactic") e` behaves like `[exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic") e`, except that named (`?x`) or unnamed (`?_`) holes in `e` that are not solved by unification with the main goal's target type are converted into new goals, using the hole's name, if any, as the goal case name.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.refine' "Permalink")tactic
```
[refine'](Tactic-Proofs/Tactic-Reference/#refine___ "Documentation for tactic")
```

`[refine'](Tactic-Proofs/Tactic-Reference/#refine___ "Documentation for tactic") e` behaves like `[refine](Tactic-Proofs/Tactic-Reference/#refine "Documentation for tactic") e`, except that unsolved placeholders (`_`) and implicit parameters are also converted into new goals.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.solveByElim "Permalink")tactic
```
[solve_by_elim](Tactic-Proofs/Tactic-Reference/#solve_by_elim "Documentation for tactic")
```

`[solve_by_elim](Tactic-Proofs/Tactic-Reference/#solve_by_elim "Documentation for tactic")` calls `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic")` on the main goal to find an assumption whose head matches and then repeatedly calls `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic")` on the generated subgoals until no subgoals remain, performing at most `maxDepth` (defaults to 6) recursive steps.
`[solve_by_elim](Tactic-Proofs/Tactic-Reference/#solve_by_elim "Documentation for tactic")` discharges the current goal or fails.
`[solve_by_elim](Tactic-Proofs/Tactic-Reference/#solve_by_elim "Documentation for tactic")` performs backtracking if subgoals can not be solved.
By default, the assumptions passed to `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic")` are the local context, `[rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`, `trivial`, `[congrFun](Basic-Propositions/Propositional-Equality/#congrFun "Documentation for congrFun")` and `[congrArg](Basic-Propositions/Propositional-Equality/#congrArg "Documentation for congrArg")`.
The assumptions can be modified with similar syntax as for `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`:
  * `solve_by_elim [h₁, h₂, ..., hᵣ]` also applies the given expressions.
  * `solve_by_elim only [h₁, h₂, ..., hᵣ]` does not include the local context, `[rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`, `trivial`, `[congrFun](Basic-Propositions/Propositional-Equality/#congrFun "Documentation for congrFun")`, or `[congrArg](Basic-Propositions/Propositional-Equality/#congrArg "Documentation for congrArg")` unless they are explicitly included.
  * `solve_by_elim [-h₁, ... -hₙ]` removes the given local hypotheses.
  * `solve_by_elim using [a₁, ...]` uses all lemmas which have been labelled with the attributes `aᵢ` (these attributes must be created using `register_label_attr`).


`[solve_by_elim](Tactic-Proofs/Tactic-Reference/#solve_by_elim "Documentation for tactic")*` tries to solve all goals together, using backtracking if a solution for one goal makes other goals impossible. (Adding or removing local hypotheses may not be well-behaved when starting with multiple goals.)
Optional arguments passed via a configuration argument as `solve_by_elim (config := { ... })`
  * `maxDepth`: number of attempts at discharging generated subgoals
  * `[symm](Tactic-Proofs/Tactic-Reference/#symm "Documentation for tactic")`: adds all hypotheses derived by `[symm](Tactic-Proofs/Tactic-Reference/#symm "Documentation for tactic")` (defaults to `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`).
  * `[exfalso](Tactic-Proofs/Tactic-Reference/#exfalso "Documentation for tactic")`: allow calling `[exfalso](Tactic-Proofs/Tactic-Reference/#exfalso "Documentation for tactic")` and trying again if `[solve_by_elim](Tactic-Proofs/Tactic-Reference/#solve_by_elim "Documentation for tactic")` fails (defaults to `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`).
  * `transparency`: change the transparency mode when calling `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic")`. Defaults to `.default`, but it is often useful to change to `.reducible`, so semireducible definitions will not be unfolded when trying to apply a lemma.


See also the doc-comment for `Lean.Meta.Tactic.Backtrack.BacktrackConfig` for the options `proc`, `suspend`, and `discharge` which allow further customization of `[solve_by_elim](Tactic-Proofs/Tactic-Reference/#solve_by_elim "Documentation for tactic")`. Both `[apply_assumption](Tactic-Proofs/Tactic-Reference/#apply_assumption "Documentation for tactic")` and `[apply_rules](Tactic-Proofs/Tactic-Reference/#apply_rules "Documentation for tactic")` are implemented via these hooks.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.applyRules "Permalink")tactic
```
[apply_rules](Tactic-Proofs/Tactic-Reference/#apply_rules "Documentation for tactic")
```

`apply_rules [l₁, l₂, ...]` tries to solve the main goal by iteratively applying the list of lemmas `[l₁, l₂, ...]` or by applying a local hypothesis. If `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic")` generates new goals, `[apply_rules](Tactic-Proofs/Tactic-Reference/#apply_rules "Documentation for tactic")` iteratively tries to solve those goals. You can use `[apply_rules](Tactic-Proofs/Tactic-Reference/#apply_rules "Documentation for tactic") [-h]` to omit a local hypothesis.
`[apply_rules](Tactic-Proofs/Tactic-Reference/#apply_rules "Documentation for tactic")` will also use `[rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`, `trivial`, `[congrFun](Basic-Propositions/Propositional-Equality/#congrFun "Documentation for congrFun")` and `[congrArg](Basic-Propositions/Propositional-Equality/#congrArg "Documentation for congrArg")`. These can be disabled, as can local hypotheses, by using `apply_rules only [...]`.
You can use `apply_rules using [a₁, ...]` to use all lemmas which have been labelled with the attributes `aᵢ` (these attributes must be created using `register_label_attr`).
You can pass a further configuration via the syntax `apply_rules (config := {...})`. The options supported are the same as for `[solve_by_elim](Tactic-Proofs/Tactic-Reference/#solve_by_elim "Documentation for tactic")` (and include all the options for `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic")`).
`[apply_rules](Tactic-Proofs/Tactic-Reference/#apply_rules "Documentation for tactic")` will try calling `[symm](Tactic-Proofs/Tactic-Reference/#symm "Documentation for tactic")` on hypotheses and `[exfalso](Tactic-Proofs/Tactic-Reference/#exfalso "Documentation for tactic")` on the goal as needed. This can be disabled with `[apply_rules](Tactic-Proofs/Tactic-Reference/#apply_rules "Documentation for tactic") (config := {symm := false, exfalso := false})`.
You can bound the iteration depth using the syntax `[apply_rules](Tactic-Proofs/Tactic-Reference/#apply_rules "Documentation for tactic") (config := {maxDepth := n})`.
Unlike `[solve_by_elim](Tactic-Proofs/Tactic-Reference/#solve_by_elim "Documentation for tactic")`, `[apply_rules](Tactic-Proofs/Tactic-Reference/#apply_rules "Documentation for tactic")` does not perform backtracking, and greedily applies a lemma from the list until it gets stuck.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.as_aux_lemma "Permalink")tactic
```
[as_aux_lemma](Tactic-Proofs/Tactic-Reference/#as_aux_lemma "Documentation for tactic")
```

`as_aux_lemma => tac` does the same as `tac`, except that it wraps the resulting expression into an auxiliary lemma. In some cases, this significantly reduces the size of expressions because the proof term is not duplicated.
##  14.5.7. Falsehood[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-false "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticExfalso "Permalink")tactic
```
[exfalso](Tactic-Proofs/Tactic-Reference/#exfalso "Documentation for tactic")
```

`[exfalso](Tactic-Proofs/Tactic-Reference/#exfalso "Documentation for tactic")` converts a goal `⊢ tgt` into `⊢ False` by applying `[False.elim](Basic-Propositions/Truth/#False___elim "Documentation for False.elim")`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.contradiction "Permalink")tactic
```
[contradiction](Tactic-Proofs/Tactic-Reference/#contradiction "Documentation for tactic")
```

`[contradiction](Tactic-Proofs/Tactic-Reference/#contradiction "Documentation for tactic")` closes the main goal if its hypotheses are "trivially contradictory".
  * Inductive type/family with no applicable constructors
`example (h : [False](Basic-Propositions/Truth/#False "Documentation for False")) : p := byp:Sort ?u.9h:[False](Basic-Propositions/Truth/#False "Documentation for False")⊢ p [contradiction](Tactic-Proofs/Tactic-Reference/#contradiction "Documentation for tactic")All goals completed! 🐙 `
  * Injectivity of constructors
`example (h : [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : p := byp:Sort ?u.73h:[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")⊢ p [contradiction](Tactic-Proofs/Tactic-Reference/#contradiction "Documentation for tactic")All goals completed! 🐙  -- `
  * Decidable false proposition
`example (h : 2 + 2 = 3) : p := byp:Sort ?u.279h:2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 3⊢ p [contradiction](Tactic-Proofs/Tactic-Reference/#contradiction "Documentation for tactic")All goals completed! 🐙 `
  * Contradictory hypotheses
`example (h : p) (h' : ¬ p) : q := byp:Propq:Sort ?u.17h:ph':[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")p⊢ q [contradiction](Tactic-Proofs/Tactic-Reference/#contradiction "Documentation for tactic")All goals completed! 🐙 `
  * Other simple contradictions such as
`example (x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (h : x ≠ x) : p := byp:Sort ?u.17x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:x ≠ x⊢ p [contradiction](Tactic-Proofs/Tactic-Reference/#contradiction "Documentation for tactic")All goals completed! 🐙 `


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.falseOrByContra "Permalink")tactic
```
[false_or_by_contra](Tactic-Proofs/Tactic-Reference/#false_or_by_contra "Documentation for tactic")
```

Changes the goal to `[False](Basic-Propositions/Truth/#False "Documentation for False")`, retaining as much information as possible:
  * If the goal is `[False](Basic-Propositions/Truth/#False "Documentation for False")`, do nothing.
  * If the goal is an implication or a function type, introduce the argument and restart. (In particular, if the goal is `x ≠ y`, introduce `x = y`.)
  * Otherwise, for a propositional goal `P`, replace it with `¬ ¬ P` (attempting to find a `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` instance, but otherwise falling back to working classically) and introduce `¬ P`.
  * For a non-propositional goal use `[False.elim](Basic-Propositions/Truth/#False___elim "Documentation for False.elim")`.


##  14.5.8. Goal Management[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-goals "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticSuffices_ "Permalink")tactic
```
[suffices](Tactic-Proofs/Tactic-Reference/#suffices "Documentation for tactic")
```

Given a main goal `ctx ⊢ t`, `[suffices](Tactic-Proofs/Tactic-Reference/#suffices "Documentation for tactic") h : t' from e` replaces the main goal with `ctx ⊢ t'`, `e` must have type `t` in the context `ctx, h : t'`.
The variant `suffices h : t' by tac` is a shorthand for `suffices h : t' from by tac`. If `h :` is omitted, the name `this` is used.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.change "Permalink")tactic
```
[change](Tactic-Proofs/Tactic-Reference/#change "Documentation for tactic")
```

  * `[change](Tactic-Proofs/Tactic-Reference/#change "Documentation for tactic") tgt'` will change the goal from `tgt` to `tgt'`, assuming these are definitionally equal.
  * `[change](Tactic-Proofs/Tactic-Reference/#change "Documentation for tactic") t' at h` will change hypothesis `h : t` to have type `t'`, assuming assuming `t` and `t'` are definitionally equal.
  * `change a with b` will change occurrences of `a` to `b` in the goal, assuming `a` and `b` are definitionally equal.
  * `change a with b at h` similarly changes `a` to `b` in the type of hypothesis `h`.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.generalize "Permalink")tactic
```
[generalize](Tactic-Proofs/Tactic-Reference/#generalize "Documentation for tactic")
```

  * `generalize ([h :] e = x),+` replaces all occurrences `e`s in the main goal with a fresh hypothesis `x`s. If `h` is given, `h : e = x` is introduced as well.
  * `[generalize](Tactic-Proofs/Tactic-Reference/#generalize "Documentation for tactic") e = x at h₁ ... hₙ` also generalizes occurrences of `e` inside `h₁`, ..., `hₙ`.
  * `[generalize](Tactic-Proofs/Tactic-Reference/#generalize "Documentation for tactic") e = x at *` will generalize occurrences of `e` everywhere.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.specialize "Permalink")tactic
```
[specialize](Tactic-Proofs/Tactic-Reference/#specialize "Documentation for tactic")
```

The tactic `[specialize](Tactic-Proofs/Tactic-Reference/#specialize "Documentation for tactic") h a₁ ... aₙ` works on local hypothesis `h`. The premises of this hypothesis, either universal quantifications or non-dependent implications, are instantiated by concrete terms coming from arguments `a₁` ... `aₙ`. The tactic adds a new hypothesis with the same name `h := h a₁ ... aₙ` and tries to clear the previous one.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.obtain "Permalink")tactic
```
[obtain](Tactic-Proofs/Tactic-Reference/#obtain "Documentation for tactic")
```

The `[obtain](Tactic-Proofs/Tactic-Reference/#obtain "Documentation for tactic")` tactic is a combination of `have` and `[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic")`. See `[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic")` for a description of supported patterns.

```
obtain ⟨patt⟩ : type := proof

```

is equivalent to

```
have h : type := proof
rcases h with ⟨patt⟩

```

If `⟨patt⟩` is omitted, `[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic")` will try to infer the pattern.
If `type` is omitted, `:= proof` is required.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.show "Permalink")tactic
```
[show](Tactic-Proofs/Tactic-Reference/#show "Documentation for tactic")
```

`[show](Tactic-Proofs/Tactic-Reference/#show "Documentation for tactic") t` finds the first goal whose target unifies with `t`. It makes that the main goal, performs the unification, and replaces the target with the unified version of `t`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.showTerm "Permalink")tactic
```
[show_term](Tactic-Proofs/Tactic-Reference/#show_term "Documentation for tactic")
```

`show_term tac` runs `tac`, then prints the generated term in the form "exact X Y Z" or "refine X ?_ Z" (prefixed by `[expose_names](Tactic-Proofs/Tactic-Reference/#expose_names "Documentation for tactic")` if necessary) if there are remaining subgoals.
(For some tactics, the printed term will not be human readable.)
##  14.5.9. Cast Management[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-casts "Permalink")
The tactics in this section make it easier avoid getting stuck on _casts_ , which are functions that coerce data from one type to another, such as converting a natural number to the corresponding integer. They are described in more detail by Lewis and Madelaine (2020)Robert Y. Lewis and Paul-Nicolas Madelaine, 2020. [“Simplifying Casts and Coercions”](https://arxiv.org/abs/2001.10594). arXiv:2001.10594.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticNorm_cast__ "Permalink")tactic
```
[norm_cast](Tactic-Proofs/Tactic-Reference/#norm_cast "Documentation for tactic")
```

The `[norm_cast](Tactic-Proofs/Tactic-Reference/#norm_cast "Documentation for tactic")` family of tactics is used to normalize certain coercions (_casts_) in expressions.
  * `[norm_cast](Tactic-Proofs/Tactic-Reference/#norm_cast "Documentation for tactic")` normalizes casts in the target.
  * `[norm_cast](Tactic-Proofs/Tactic-Reference/#norm_cast "Documentation for tactic") at h` normalizes casts in hypothesis `h`.


The tactic is basically a version of `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` with a specific set of lemmas to move casts upwards in the expression. Therefore even in situations where non-terminal `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` calls are discouraged (because of fragility), `[norm_cast](Tactic-Proofs/Tactic-Reference/#norm_cast "Documentation for tactic")` is considered to be safe. It also has special handling of numerals.
For instance, given an assumption

```
a b : ℤ
h : ↑a + ↑b < (10 : ℚ)

```

writing `[norm_cast](Tactic-Proofs/Tactic-Reference/#norm_cast "Documentation for tactic") at h` will turn `h` into

```
h : a + b < 10

```

There are also variants of basic tactics that use `[norm_cast](Tactic-Proofs/Tactic-Reference/#norm_cast "Documentation for tactic")` to normalize expressions during their operation, to make them more flexible about the expressions they accept (we say that it is a tactic _modulo_ the effects of `[norm_cast](Tactic-Proofs/Tactic-Reference/#norm_cast "Documentation for tactic")`):
  * `[exact_mod_cast](Tactic-Proofs/Tactic-Reference/#exact_mod_cast "Documentation for tactic")` for `[exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic")` and `[apply_mod_cast](Tactic-Proofs/Tactic-Reference/#apply_mod_cast "Documentation for tactic")` for `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic")`. Writing `[exact_mod_cast](Tactic-Proofs/Tactic-Reference/#exact_mod_cast "Documentation for tactic") h` and `[apply_mod_cast](Tactic-Proofs/Tactic-Reference/#apply_mod_cast "Documentation for tactic") h` will normalize casts in the goal and `h` before using `[exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic") h` or `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") h`.
  * `[rw_mod_cast](Tactic-Proofs/Tactic-Reference/#rw_mod_cast "Documentation for tactic")` for `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")`. It applies `[norm_cast](Tactic-Proofs/Tactic-Reference/#norm_cast "Documentation for tactic")` between rewrites.
  * `[assumption_mod_cast](Tactic-Proofs/Tactic-Reference/#assumption_mod_cast "Documentation for tactic")` for `[assumption](Tactic-Proofs/Tactic-Reference/#assumption "Documentation for tactic")`. This is effectively `norm_cast at *; assumption`, but more efficient. It normalizes casts in the goal and, for every hypothesis `h` in the context, it will try to normalize casts in `h` and use `[exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic") h`.


See also `[push_cast](Tactic-Proofs/Tactic-Reference/#push_cast "Documentation for tactic")`, which moves casts inwards rather than lifting them outwards.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.pushCast "Permalink")tactic
```
[push_cast](Tactic-Proofs/Tactic-Reference/#push_cast "Documentation for tactic")
```

`[push_cast](Tactic-Proofs/Tactic-Reference/#push_cast "Documentation for tactic")` rewrites the goal to move certain coercions (_casts_) inward, toward the leaf nodes. This uses `[norm_cast](Tactic-Proofs/Tactic-Reference/#norm_cast "Documentation for tactic")` lemmas in the forward direction. For example, `↑(a + b)` will be written to `↑a + ↑b`.
  * `[push_cast](Tactic-Proofs/Tactic-Reference/#push_cast "Documentation for tactic")` moves casts inward in the goal.
  * `[push_cast](Tactic-Proofs/Tactic-Reference/#push_cast "Documentation for tactic") at h` moves casts inward in the hypothesis `h`. It can be used with extra simp lemmas with, for example, `[push_cast](Tactic-Proofs/Tactic-Reference/#push_cast "Documentation for tactic") [Int.add_zero]`.


Example:
`example (a b : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))     (h1 : ((a + b : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 10)     (h2 : ((a + b + 0 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 10) :     ((a + b : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) = 10 := bya:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")b:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:↑[(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 10h2:↑[(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 10⊢ ↑[(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 10   /-   h1 : ↑(a + b) = 10   h2 : ↑(a + b + 0) = 10   ⊢ ↑(a + b) = 10   -/   [push_cast](Tactic-Proofs/Tactic-Reference/#push_cast "Documentation for tactic")a:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")b:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:↑[(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 10h2:↑[(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 10⊢ ↑a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") ↑b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 10   /- Now   ⊢ ↑a + ↑b = 10   -/   [push_cast](Tactic-Proofs/Tactic-Reference/#push_cast "Documentation for tactic") at h1a:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")b:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:↑a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") ↑b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 10h2:↑[(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 10⊢ ↑a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") ↑b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 10   [push_cast](Tactic-Proofs/Tactic-Reference/#push_cast "Documentation for tactic") [Int.add_zero] at h2a:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")b:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:↑a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") ↑b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 10h2:↑a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") ↑b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 10⊢ ↑a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") ↑b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 10   /- Now   h1 h2 : ↑a + ↑b = 10   -/   [exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic") h1All goals completed! 🐙 `
See also `[norm_cast](Tactic-Proofs/Tactic-Reference/#norm_cast "Documentation for tactic")`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticExact_mod_cast_ "Permalink")tactic
```
[exact_mod_cast](Tactic-Proofs/Tactic-Reference/#exact_mod_cast "Documentation for tactic")
```

Normalize casts in the goal and the given expression, then close the goal with `[exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic")`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticApply_mod_cast_ "Permalink")tactic
```
[apply_mod_cast](Tactic-Proofs/Tactic-Reference/#apply_mod_cast "Documentation for tactic")
```

Normalize casts in the goal and the given expression, then `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic")` the expression to the goal.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticRw_mod_cast___ "Permalink")tactic
```
[rw_mod_cast](Tactic-Proofs/Tactic-Reference/#rw_mod_cast "Documentation for tactic")
```

Rewrites with the given rules, normalizing casts prior to each step.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticAssumption_mod_cast_ "Permalink")tactic
```
[assumption_mod_cast](Tactic-Proofs/Tactic-Reference/#assumption_mod_cast "Documentation for tactic")
```

`[assumption_mod_cast](Tactic-Proofs/Tactic-Reference/#assumption_mod_cast "Documentation for tactic")` is a variant of `[assumption](Tactic-Proofs/Tactic-Reference/#assumption "Documentation for tactic")` that solves the goal using a hypothesis. Unlike `[assumption](Tactic-Proofs/Tactic-Reference/#assumption "Documentation for tactic")`, it first pre-processes the goal and each hypothesis to move casts as far outwards as possible, so it can be used in more situations.
Concretely, it runs `[norm_cast](Tactic-Proofs/Tactic-Reference/#norm_cast "Documentation for tactic")` on the goal. For each local hypothesis `h`, it also normalizes `h` with `[norm_cast](Tactic-Proofs/Tactic-Reference/#norm_cast "Documentation for tactic")` and tries to use that to close the goal.
##  14.5.10. Managing `let` Expressions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Tactic-Proofs--Tactic-Reference--Managing--let--Expressions "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.extractLets "Permalink")tactic
```
[extract_lets](Tactic-Proofs/Tactic-Reference/#extract_lets "Documentation for tactic")
```

Extracts `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` and `have` expressions from within the target or a local hypothesis, introducing new local definitions.
  * `[extract_lets](Tactic-Proofs/Tactic-Reference/#extract_lets "Documentation for tactic")` extracts all the lets from the target.
  * `[extract_lets](Tactic-Proofs/Tactic-Reference/#extract_lets "Documentation for tactic") x y z` extracts all the lets from the target and uses `x`, `y`, and `z` for the first names. Using `_` for a name leaves it unnamed.
  * `[extract_lets](Tactic-Proofs/Tactic-Reference/#extract_lets "Documentation for tactic") x y z at h` operates on the local hypothesis `h` instead of the target.


For example, given a local hypotheses if the form `h : let x := v; b x`, then `[extract_lets](Tactic-Proofs/Tactic-Reference/#extract_lets "Documentation for tactic") z at h` introduces a new local definition `z := v` and changes `h` to be `h : b z`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.liftLets "Permalink")tactic
```
[lift_lets](Tactic-Proofs/Tactic-Reference/#lift_lets "Documentation for tactic")
```

Lifts `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` and `have` expressions within a term as far out as possible. It is like `[extract_lets](Tactic-Proofs/Tactic-Reference/#extract_lets "Documentation for tactic") +lift`, but the top-level lets at the end of the procedure are not extracted as local hypotheses.
  * `[lift_lets](Tactic-Proofs/Tactic-Reference/#lift_lets "Documentation for tactic")` lifts let expressions in the target.
  * `[lift_lets](Tactic-Proofs/Tactic-Reference/#lift_lets "Documentation for tactic") at h` lifts let expressions at the given local hypothesis.


For example,

```
example : (let x := 1; x) = 1 := by
  lift_lets
  -- ⊢ let x := 1; x = 1
  ...

```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.letToHave "Permalink")tactic
```
[let_to_have](Tactic-Proofs/Tactic-Reference/#let_to_have "Documentation for tactic")
```

Transforms `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` expressions into `have` expressions when possible.
  * `[let_to_have](Tactic-Proofs/Tactic-Reference/#let_to_have "Documentation for tactic")` transforms `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")`s in the target.
  * `[let_to_have](Tactic-Proofs/Tactic-Reference/#let_to_have "Documentation for tactic") at h` transforms `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")`s in the given local hypothesis.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.clearValue "Permalink")tactic
```
[clear_value](Tactic-Proofs/Tactic-Reference/#clear_value "Documentation for tactic")
```

  * `clear_value x...` clears the values of the given local definitions. A local definition `x : α := v` becomes a hypothesis `x : α`.
  * `[clear_value](Tactic-Proofs/Tactic-Reference/#clear_value "Documentation for tactic") (h : x = _)` adds a hypothesis `h : x = v` before clearing the value of `x`. This is short for `have h : x = v := rfl; clear_value x`. Any value definitionally equal to `v` can be used in place of `_`.
  * `[clear_value](Tactic-Proofs/Tactic-Reference/#clear_value "Documentation for tactic") *` clears values of all hypotheses that can be cleared. Fails if none can be cleared.


These syntaxes can be combined. For example, `[clear_value](Tactic-Proofs/Tactic-Reference/#clear_value "Documentation for tactic") x y *` ensures that `x` and `y` are cleared while trying to clear all other local definitions, and `clear_value (hx : x = _) y * with hx` does the same while first adding the `hx : x = v` hypothesis.
##  14.5.11. Extensionality[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-ext "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Elab.Tactic.Ext.ext "Permalink")tactic
```
[ext](Tactic-Proofs/Tactic-Reference/#ext "Documentation for tactic")
```

Applies extensionality lemmas that are registered with the `@[ext]` attribute.
  * `ext pat*` applies extensionality theorems as much as possible, using the patterns `pat*` to introduce the variables in extensionality theorems using `[rintro](Tactic-Proofs/Tactic-Reference/#rintro "Documentation for tactic")`. For example, the patterns are used to name the variables introduced by lemmas such as `[funext](The-Type-System/Functions/#funext "Documentation for funext")`.
  * Without patterns,`[ext](Tactic-Proofs/Tactic-Reference/#ext "Documentation for tactic")` applies extensionality lemmas as much as possible but introduces anonymous hypotheses whenever needed.
  * `ext pat* : n` applies ext theorems only up to depth `n`.


The `ext1 pat*` tactic is like `ext pat*` except that it only applies a single extensionality theorem.
Unused patterns will generate warning. Patterns that don't match the variables will typically result in the introduction of anonymous hypotheses.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Elab.Tactic.Ext.tacticExt1___ "Permalink")tactic
```
[ext1](Tactic-Proofs/Tactic-Reference/#ext1 "Documentation for tactic")
```

`ext1 pat*` is like `ext pat*` except that it only applies a single extensionality theorem rather than recursively applying as many extensionality theorems as possible.
The `pat*` patterns are processed using the `[rintro](Tactic-Proofs/Tactic-Reference/#rintro "Documentation for tactic")` tactic. If no patterns are supplied, then variables are introduced anonymously using the `[intros](Tactic-Proofs/Tactic-Reference/#intros "Documentation for tactic")` tactic.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Elab.Tactic.Ext.applyExtTheorem "Permalink")tactic
```
[apply_ext_theorem](Tactic-Proofs/Tactic-Reference/#apply_ext_theorem "Documentation for tactic")
```

Apply a single extensionality theorem to the current goal.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=tacticFunext___ "Permalink")tactic
```
[funext](Tactic-Proofs/Tactic-Reference/#funext-next "Documentation for tactic")
```

Apply function extensionality and introduce new hypotheses. The tactic `[funext](Tactic-Proofs/Tactic-Reference/#funext-next "Documentation for tactic")` will keep applying the `[funext](The-Type-System/Functions/#funext "Documentation for funext")` lemma until the goal target is not reducible to

```
  |-  ((fun x => ...) = (fun x => ...))

```

The variant `[funext](Tactic-Proofs/Tactic-Reference/#funext-next "Documentation for tactic") h₁ ... hₙ` applies `[funext](The-Type-System/Functions/#funext "Documentation for funext")` `n` times, and uses the given identifiers to name the new hypotheses. Patterns can be used like in the `[intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic")` tactic. Example, given a goal

```
  |-  ((fun x : Nat × Bool => ...) = (fun x => ...))

```

`[funext](Tactic-Proofs/Tactic-Reference/#funext-next "Documentation for tactic") (a, b)` applies `[funext](The-Type-System/Functions/#funext "Documentation for funext")` once and performs pattern matching on the newly introduced pair.
##  14.5.12. SMT-Inspired Automation[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Tactic-Proofs--Tactic-Reference--SMT-Inspired-Automation "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.grind "Permalink")tactic
```
[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")
```

`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` is a tactic inspired by modern SMT solvers. **Picture a virtual whiteboard** : every time grind discovers a new equality, inequality, or logical fact, it writes it on the board, groups together terms known to be equal, and lets each reasoning engine read from and contribute to the shared workspace. These engines work together to handle equality reasoning, apply known theorems, propagate new facts, perform case analysis, and run specialized solvers for domains like linear arithmetic and commutative rings.
See [the reference manual's chapter on ``](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=grind-tactic)`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` for more information.
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` is _not_ designed for goals whose search space explodes combinatorially, think large pigeonhole instances, graph‑coloring reductions, high‑order N‑queens boards, or a 200‑variable Sudoku encoded as Boolean constraints. Such encodings require thousands (or millions) of case‑splits that overwhelm `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")`’s branching search.
For **bit‑level or combinatorial problems** , consider using **`bv_decide`**.`bv_decide` calls a state‑of‑the‑art SAT solver (CaDiCaL) and then returns a _compact, machine‑checkable certificate_.
**Equality reasoning**
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` uses **congruence closure** to track equalities between terms. When two terms are known to be equal, congruence closure automatically deduces equalities between more complex expressions built from them. For example, if `a = b`, then congruence closure will also conclude that `f a` = `f b` for any function `f`. This forms the foundation for efficient equality reasoning in `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")`. Here is an example:
`example (f : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (h : a = b) : f (f b) = f (f a) := bya:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")b:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")f:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b⊢ f (f b) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f (f a)   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
**Applying theorems using E-matching**
To apply existing theorems, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` uses a technique called **E-matching** , which finds matches for known theorem patterns while taking equalities into account. Combined with congruence closure, E-matching helps `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` discover non-obvious consequences of theorems and equalities automatically.
Consider the following functions and theorems:
`def [f](releases/v4.27.0/#f "Definition of example") (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") :=   a + 1  def g (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") :=   a - 1  @[grind =] theorem gf (x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : g ([f](releases/v4.27.0/#f "Definition of example") x) = x := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ g ([f](releases/v4.27.0/#f "Definition of example") x) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x   [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [[f](releases/v4.27.0/#f "Definition of example"), g]All goals completed! 🐙 `
The theorem `gf` asserts that `g (f x) = x` for all natural numbers `x`. The attribute `[grind =]` instructs `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to use the left-hand side of the equation, `g (f x)`, as a pattern for E-matching. Suppose we now have a goal involving:

```
example {a b} (h : f b = a) : g a = b := by
  grind

```

Although `g a` is not an instance of the pattern `g (f x)`, it becomes one modulo the equation `f b = a`. By substituting `a` with `f b` in `g a`, we obtain the term `g (f b)`, which matches the pattern `g (f x)` with the assignment `x := b`. Thus, the theorem `gf` is instantiated with `x := b`, and the new equality `g (f b) = b` is asserted. `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` then uses congruence closure to derive the implied equality `g a = g (f b)` and completes the proof.
The pattern used to instantiate theorems affects the effectiveness of `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")`. For example, the pattern `g (f x)` is too restrictive in the following case: the theorem `gf` will not be instantiated because the goal does not even contain the function symbol `g`.

```
example (h₁ : f b = a) (h₂ : f c = a) : b = c := by
  grind

```

You can use the command `grind_pattern` to manually select a pattern for a given theorem. In the following example, we instruct `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to use `f x` as the pattern, allowing it to solve the goal automatically:

```
grind_pattern gf => f x

example {a b c} (h₁ : f b = a) (h₂ : f c = a) : b = c := by
  grind

```

You can enable the option `[trace.grind.ematch.instance](The--grind--tactic/E___matching/#trace___grind___ematch___instance "Documentation for option trace.grind.ematch.instance")` to make `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` print a trace message for each theorem instance it generates.
You can also specify a **multi-pattern** to control when `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` should apply a theorem. A multi-pattern requires that all specified patterns are matched in the current context before the theorem is applied. This is useful for theorems such as transitivity rules, where multiple premises must be simultaneously present for the rule to apply. The following example demonstrates this feature using a transitivity axiom for a binary relation `R`:
`opaque [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → Prop [axiom](Axioms/#Lean___Parser___Command___axiom-next "Documentation for syntax") Rtrans {x y z : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")} : [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") x y → [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") y z → [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") x z  grind_pattern Rtrans => [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") x y, [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") y z  example {a b c d} : [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") a b → [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") b c → [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") c d → [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") a d := bya:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")b:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")c:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")d:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") a b → [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") b c → [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") c d → [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") a d   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
By specifying the multi-pattern `R x y, R y z`, we instruct `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to instantiate `Rtrans` only when both `R x y` and `R y z` are available in the context. In the example, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` applies `Rtrans` to derive `R a c` from `R a b` and `R b c`, and can then repeat the same reasoning to deduce `R a d` from `R a c` and `R c d`.
Instead of using `grind_pattern` to explicitly specify a pattern, you can use the `@[grind]` attribute or one of its variants, which will use a heuristic to generate a (multi-)pattern. The complete list is available in the reference manual. The main ones are:
  * `@[grind →]` will select a multi-pattern from the hypotheses of the theorem (i.e. it will use the theorem for forwards reasoning). In more detail, it will traverse the hypotheses of the theorem from left-to-right, and each time it encounters a minimal indexable (i.e. has a constant as its head) subexpression which "covers" (i.e. fixes the value of) an argument which was not previously covered, it will add that subexpression as a pattern, until all arguments have been covered.
  * `@[grind ←]` will select a multi-pattern from the conclusion of theorem (i.e. it will use the theorem for backwards reasoning). This may fail if not all the arguments to the theorem appear in the conclusion.
  * `@[grind]` will traverse the conclusion and then the hypotheses left-to-right, adding patterns as they increase the coverage, stopping when all arguments are covered.
  * `@[grind =]` checks that the conclusion of the theorem is an equality, and then uses the left-hand-side of the equality as a pattern. This may fail if not all of the arguments appear in the left-hand-side.


Here is the previous example again but using the attribute `[grind →]`
`opaque [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → Prop @[grind →] [axiom](Axioms/#Lean___Parser___Command___axiom-next "Documentation for syntax") Rtrans {x y z : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")} : [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") x y → [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") y z → [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") x z  example {a b c d} : [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") a b → [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") b c → [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") c d → [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") a d := bya:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")b:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")c:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")d:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") a b → [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") b c → [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") c d → [R](The--grind--tactic/Bigger-Examples/#R "Definition of example") a d   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
To control theorem instantiation and avoid generating an unbounded number of instances, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` uses a generation counter. Terms in the original goal are assigned generation zero. When `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` applies a theorem using terms of generation `≤ n`, any new terms it creates are assigned generation `n + 1`. This limits how far the tactic explores when applying theorems and helps prevent an excessive number of instantiations.
**Key options:**
  * `grind (ematch := <num>)` controls the number of E-matching rounds.
  * `grind [<name>, ...]` instructs `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to use the declaration `name` during E-matching.
  * `grind only [<name>, ...]` is like `grind [<name>, ...]` but does not use theorems tagged with `@[grind]`.
  * `grind (gen := <num>)` sets the maximum generation.


**Linear integer arithmetic (`[lia](Tactic-Proofs/Tactic-Reference/#lia "Documentation for tactic")`)**
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` can solve goals that reduce to **linear integer arithmetic (LIA)** using an integrated decision procedure called **`[lia](Tactic-Proofs/Tactic-Reference/#lia "Documentation for tactic")`**. It understands
  * equalities `p = 0`
  * inequalities `p ≤ 0`
  * disequalities `p ≠ 0`
  * divisibility `d ∣ p`


The solver incrementally assigns integer values to variables; when a partial assignment violates a constraint it adds a new, implied constraint and retries. This _model-based_ search is **complete for LIA**.
**Key options:**
  * `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") -lia` disable the solver (useful for debugging)
  * `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") +qlia` accept rational models (shrinks the search space but is incomplete for ℤ)


**Examples:**
`example {x y : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")} : 2 * x + 4 * y ≠ 5 := byx:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")y:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 4 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y ≠ 5   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  -- Mixing equalities and inequalities. example {x y : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")} :     2 * x + 3 * y = 0 → 1 ≤ x → y < 1 := byx:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")y:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 3 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") x → y [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 1   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  -- Reasoning with divisibility. example (a b : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) :     2 ∣ a + 1 → 2 ∣ b + a → ¬ 2 ∣ b + 2 * a := bya:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")b:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ 2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 → 2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a → [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  example (x y : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) :     27 ≤ 11*x + 13*y →     11*x + 13*y ≤ 45 →     -10 ≤ 7*x - 9*y →     7*x - 9*y ≤ 4 → [False](Basic-Propositions/Truth/#False "Documentation for False") := byx:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")y:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ 27 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 11 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 13 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y → 11 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 13 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 45 → -10 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 7 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 9 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y → 7 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 9 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 4 → [False](Basic-Propositions/Truth/#False "Documentation for False")   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  -- Types that implement the `ToInt` type-class. example (a b c : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64"))     : a ≤ 2 → b ≤ 3 → c - a - b = 0 → c ≤ 5 := bya:[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")b:[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")c:[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")⊢ a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 2 → b [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 3 → c [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") a [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → c [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 5   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
**Algebraic solver (`ring`)**
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` ships with an algebraic solver nick-named **`ring`**for goals that can be phrased as polynomial equations (or disequations) over commutative rings, semirings, or fields.
_Works out of the box_ All core numeric types and relevant Mathlib types already provide the required type-class instances, so the solver is ready to use in most developments.
What it can decide:
  * equalities of the form `p = q`
  * disequalities `p ≠ q`
  * basic reasoning under field inverses (`a / b := a * b⁻¹`)
  * goals that mix ring facts with other `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` engines


**Key options:**
  * `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") -ring` turn the solver off (useful when debugging)
  * `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") (ringSteps := n)` cap the number of steps performed by this procedure.


**Examples**
`[open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Lean Grind  example [[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α] (x : α) : (x + 1) * (x - 1) = x^2 - 1 := byα:Type u_1inst✝:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") αx:α⊢ [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 1[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 1   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  -- Characteristic 256 means 16 * 16 = 0. example [[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α] [[IsCharP](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___IsCharP___mk "Documentation for Lean.Grind.IsCharP") α 256] (x : α) :     (x + 16) * (x - 16) = x^2 := byα:Type u_1inst✝¹:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") αinst✝:[IsCharP](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___IsCharP___mk "Documentation for Lean.Grind.IsCharP") α 256x:α⊢ [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 16[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 16[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  -- Works on built-in rings such as `UInt8`. example (x : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : (x + 16) * (x - 16) = x^2 := byx:[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")⊢ [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 16[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 16[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  example [[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") α] (a b c : α) :     a + b + c = 3 →     a^2 + b^2 + c^2 = 5 →     a^3 + b^3 + c^3 = 7 →     a^4 + b^4 = 9 - c^4 := byα:Type u_1inst✝:[CommRing](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommRing___mk "Documentation for Lean.Grind.CommRing") αa:αb:αc:α⊢ a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 3 → a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 5 → a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 3 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 3 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") c [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 3 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 7 → a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 9 [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") c [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 4   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  example [[Field](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Field___mk "Documentation for Lean.Grind.Field") α] [[NoNatZeroDivisors](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___NoNatZeroDivisors___mk "Documentation for Lean.Grind.NoNatZeroDivisors") α] (a : α) :     1 / a + 1 / (2 * a) = 3 / (2 * a) := byα:Type u_1inst✝¹:[Field](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___Field___mk "Documentation for Lean.Grind.Field") αinst✝:[NoNatZeroDivisors](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___NoNatZeroDivisors___mk "Documentation for Lean.Grind.NoNatZeroDivisors") αa:α⊢ 1 [/](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv.hDiv") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [/](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv.hDiv") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 3 [/](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv.hDiv") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
**Other options**
  * `grind (splits := <num>)` caps the _depth_ of the search tree. Once a branch performs `num` splits `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` stops splitting further in that branch.
  * `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") -splitIte` disables case splitting on if-then-else expressions.
  * `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") -splitMatch` disables case splitting on `[match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic")` expressions.
  * `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") +splitImp` instructs `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to split on any hypothesis `A → B` whose antecedent `A` is **propositional**.
  * `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") -linarith` disables the linear arithmetic solver for (ordered) modules and rings.


**Additional Examples**
`example {a b} {as bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α} : (as ++ bs ++ [b]).[getLastD](Basic-Types/Linked-Lists/#List___getLastD "Documentation for List.getLastD") a = b := byα:Type u_1a:αb:αas:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") αbs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α⊢ [(](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend")as [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") bs [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")b[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[)](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend").[getLastD](Basic-Types/Linked-Lists/#List___getLastD "Documentation for List.getLastD") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  example (x : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") (w+1)) : ([BitVec.cons](Basic-Types/Bitvectors/#BitVec___cons "Documentation for BitVec.cons") x.[msb](Basic-Types/Bitvectors/#BitVec___msb "Documentation for BitVec.msb") (x.[setWidth](Basic-Types/Bitvectors/#BitVec___setWidth "Documentation for BitVec.setWidth") w)) = x := byw:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")x:[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")w [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")⊢ [BitVec.cons](Basic-Types/Bitvectors/#BitVec___cons "Documentation for BitVec.cons") x.[msb](Basic-Types/Bitvectors/#BitVec___msb "Documentation for BitVec.msb") ([BitVec.setWidth](Basic-Types/Bitvectors/#BitVec___setWidth "Documentation for BitVec.setWidth") w x) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  example (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (lo hi i j : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :     lo ≤ i → i < j → j ≤ hi → j < as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") → [min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min.min") lo (as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") - 1) ≤ i := byα:Type u_1as:[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") αlo:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")hi:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")i:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")j:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ lo [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") i → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") j → j [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") hi → j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") → [min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min.min") lo [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 1[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") i   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.grindTrace "Permalink")tactic
```
[grind?](Tactic-Proofs/Tactic-Reference/#grind___ "Documentation for tactic")
```

`[grind?](Tactic-Proofs/Tactic-Reference/#grind___ "Documentation for tactic")` takes the same arguments as `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")`, but reports an equivalent call to `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") only` that would be sufficient to close the goal. This is useful for reducing the size of the `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` theorems in a local invocation.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.lia "Permalink")tactic
```
[lia](Tactic-Proofs/Tactic-Reference/#lia "Documentation for tactic")
```

`[lia](Tactic-Proofs/Tactic-Reference/#lia "Documentation for tactic")` solves linear integer arithmetic goals.
It is a implemented as a thin wrapper around the `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` tactic, enabling only the `[lia](Tactic-Proofs/Tactic-Reference/#lia "Documentation for tactic")` solver. Please use `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` instead if you need additional capabilities.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.grobner "Permalink")tactic
```
[grobner](Tactic-Proofs/Tactic-Reference/#grobner "Documentation for tactic")
```

`[grobner](Tactic-Proofs/Tactic-Reference/#grobner "Documentation for tactic")` solves goals that can be phrased as polynomial equations (with further polynomial equations as hypotheses) over commutative (semi)rings, using the Grobner basis algorithm.
It is a implemented as a thin wrapper around the `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` tactic, enabling only the `[grobner](Tactic-Proofs/Tactic-Reference/#grobner "Documentation for tactic")` solver. Please use `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` instead if you need additional capabilities.
##  14.5.13. Simplification[🔗](find/?domain=Verso.Genre.Manual.section&name=simp-tactics "Permalink")
The simplifier is described in greater detail in [its dedicated chapter](The-Simplifier/#the-simplifier).
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.simp "Permalink")tactic
```
[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")
```

The `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` tactic uses lemmas and hypotheses to simplify the main goal target or non-dependent hypotheses. It has many variants:
  * `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` simplifies the main goal target using lemmas tagged with the attribute `[simp]`.
  * `simp [h₁, h₂, ..., hₙ]` simplifies the main goal target using the lemmas tagged with the attribute `[simp]` and the given `hᵢ`'s, where the `hᵢ`'s are expressions.-
  * If an `hᵢ` is a defined constant `f`, then `f` is unfolded. If `f` has equational lemmas associated with it (and is not a projection or a `reducible` definition), these are used to rewrite with `f`.
  * `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [*]` simplifies the main goal target using the lemmas tagged with the attribute `[simp]` and all hypotheses.
  * `simp only [h₁, h₂, ..., hₙ]` is like `simp [h₁, h₂, ..., hₙ]` but does not use `[simp]` lemmas.
  * `simp [-id₁, ..., -idₙ]` simplifies the main goal target using the lemmas tagged with the attribute `[simp]`, but removes the ones named `idᵢ`.
  * `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") at h₁ h₂ ... hₙ` simplifies the hypotheses `h₁ : T₁` ... `hₙ : Tₙ`. If the target or another hypothesis depends on `hᵢ`, a new simplified hypothesis `hᵢ` is introduced, but the old one remains in the local context.
  * `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") at *` simplifies all the hypotheses and the target.
  * `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [*] at *` simplifies target and all (propositional) hypotheses using the other hypotheses.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.simpAutoUnfold "Permalink")tactic
```
[simp!](Tactic-Proofs/Tactic-Reference/#simp___ "Documentation for tactic")
```

`[simp!](Tactic-Proofs/Tactic-Reference/#simp___ "Documentation for tactic")` is shorthand for `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` with `autoUnfold := true`. This will unfold applications of functions defined by pattern matching, when one of the patterns applies. This can be used to partially evaluate many definitions.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.simpTrace "Permalink")tactic
```
[simp?](Tactic-Proofs/Tactic-Reference/#simp___-next "Documentation for tactic")
```

`[simp?](Tactic-Proofs/Tactic-Reference/#simp___-next "Documentation for tactic")` takes the same arguments as `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`, but reports an equivalent call to `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") only` that would be sufficient to close the goal. This is useful for reducing the size of the simp set in a local invocation to speed up processing.
`example (x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : ([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [True](Basic-Propositions/Truth/#True___intro "Documentation for True") [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x + 2 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 3) = x + 2 := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ (if [True](Basic-Propositions/Truth/#True___intro "Documentation for True") then x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 else 3) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2   `Try this:   [apply] simp only [↓reduceIte, Nat.add_left_cancel_iff]`[simp?](Tactic-Proofs/Tactic-Reference/#simp___-next "Documentation for tactic")All goals completed! 🐙 -- prints "Try this: simp only [ite_true]" `
This command can also be used in `[simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic")` and `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticSimp?!_ "Permalink")tactic
```
[simp?!](Tactic-Proofs/Tactic-Reference/#simp______ "Documentation for tactic")
```

`[simp?](Tactic-Proofs/Tactic-Reference/#simp___-next "Documentation for tactic")` takes the same arguments as `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`, but reports an equivalent call to `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") only` that would be sufficient to close the goal. This is useful for reducing the size of the simp set in a local invocation to speed up processing.
`example (x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : ([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [True](Basic-Propositions/Truth/#True___intro "Documentation for True") [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x + 2 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 3) = x + 2 := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ (if [True](Basic-Propositions/Truth/#True___intro "Documentation for True") then x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 else 3) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2   `Try this:   [apply] simp only [↓reduceIte, Nat.add_left_cancel_iff]`[simp?](Tactic-Proofs/Tactic-Reference/#simp___-next "Documentation for tactic")All goals completed! 🐙 -- prints "Try this: simp only [ite_true]" `
This command can also be used in `[simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic")` and `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.simpArith "Permalink")tactic
```
[simp_arith](Tactic-Proofs/Tactic-Reference/#simp_arith "Documentation for tactic")
```

`[simp_arith](Tactic-Proofs/Tactic-Reference/#simp_arith "Documentation for tactic")` has been deprecated. It was a shorthand for `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") +arith +decide`. Note that `+decide` is not needed for reducing arithmetic terms since simprocs have been added to Lean.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.simpArithBang "Permalink")tactic
```
[simp_arith!](Tactic-Proofs/Tactic-Reference/#simp_arith___ "Documentation for tactic")
```

`[simp_arith!](Tactic-Proofs/Tactic-Reference/#simp_arith___ "Documentation for tactic")` has been deprecated. It was a shorthand for `[simp!](Tactic-Proofs/Tactic-Reference/#simp___ "Documentation for tactic") +arith +decide`. Note that `+decide` is not needed for reducing arithmetic terms since simprocs have been added to Lean.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.dsimp "Permalink")tactic
```
[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")
```

The `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")` tactic is the definitional simplifier. It is similar to `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` but only applies theorems that hold by reflexivity. Thus, the result is guaranteed to be definitionally equal to the input.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.dsimpAutoUnfold "Permalink")tactic
```
[dsimp!](Tactic-Proofs/Tactic-Reference/#dsimp___ "Documentation for tactic")
```

`[dsimp!](Tactic-Proofs/Tactic-Reference/#dsimp___ "Documentation for tactic")` is shorthand for `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")` with `autoUnfold := true`. This will unfold applications of functions defined by pattern matching, when one of the patterns applies. This can be used to partially evaluate many definitions.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.dsimpTrace "Permalink")tactic
```
[dsimp?](Tactic-Proofs/Tactic-Reference/#dsimp___-next "Documentation for tactic")
```

`[simp?](Tactic-Proofs/Tactic-Reference/#simp___-next "Documentation for tactic")` takes the same arguments as `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`, but reports an equivalent call to `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") only` that would be sufficient to close the goal. This is useful for reducing the size of the simp set in a local invocation to speed up processing.
`example (x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : ([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [True](Basic-Propositions/Truth/#True___intro "Documentation for True") [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x + 2 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 3) = x + 2 := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ (if [True](Basic-Propositions/Truth/#True___intro "Documentation for True") then x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 else 3) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2   `Try this:   [apply] simp only [↓reduceIte, Nat.add_left_cancel_iff]`[simp?](Tactic-Proofs/Tactic-Reference/#simp___-next "Documentation for tactic")All goals completed! 🐙 -- prints "Try this: simp only [ite_true]" `
This command can also be used in `[simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic")` and `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticDsimp?!_ "Permalink")tactic
```
[dsimp?!](Tactic-Proofs/Tactic-Reference/#dsimp______ "Documentation for tactic")
```

`[simp?](Tactic-Proofs/Tactic-Reference/#simp___-next "Documentation for tactic")` takes the same arguments as `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`, but reports an equivalent call to `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") only` that would be sufficient to close the goal. This is useful for reducing the size of the simp set in a local invocation to speed up processing.
`example (x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : ([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [True](Basic-Propositions/Truth/#True___intro "Documentation for True") [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x + 2 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 3) = x + 2 := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ (if [True](Basic-Propositions/Truth/#True___intro "Documentation for True") then x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 else 3) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2   `Try this:   [apply] simp only [↓reduceIte, Nat.add_left_cancel_iff]`[simp?](Tactic-Proofs/Tactic-Reference/#simp___-next "Documentation for tactic")All goals completed! 🐙 -- prints "Try this: simp only [ite_true]" `
This command can also be used in `[simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic")` and `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.simpAll "Permalink")tactic
```
[simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic")
```

`[simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic")` is a stronger version of `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [*] at *` where the hypotheses and target are simplified multiple times until no simplification is applicable. Only non-dependent propositional hypotheses are considered.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.simpAllAutoUnfold "Permalink")tactic
```
[simp_all!](Tactic-Proofs/Tactic-Reference/#simp_all___ "Documentation for tactic")
```

`[simp_all!](Tactic-Proofs/Tactic-Reference/#simp_all___ "Documentation for tactic")` is shorthand for `[simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic")` with `autoUnfold := true`. This will unfold applications of functions defined by pattern matching, when one of the patterns applies. This can be used to partially evaluate many definitions.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.simpAllTrace "Permalink")tactic
```
[simp_all?](Tactic-Proofs/Tactic-Reference/#simp_all___-next "Documentation for tactic")
```

`[simp?](Tactic-Proofs/Tactic-Reference/#simp___-next "Documentation for tactic")` takes the same arguments as `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`, but reports an equivalent call to `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") only` that would be sufficient to close the goal. This is useful for reducing the size of the simp set in a local invocation to speed up processing.
`example (x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : ([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [True](Basic-Propositions/Truth/#True___intro "Documentation for True") [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x + 2 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 3) = x + 2 := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ (if [True](Basic-Propositions/Truth/#True___intro "Documentation for True") then x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 else 3) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2   `Try this:   [apply] simp only [↓reduceIte, Nat.add_left_cancel_iff]`[simp?](Tactic-Proofs/Tactic-Reference/#simp___-next "Documentation for tactic")All goals completed! 🐙 -- prints "Try this: simp only [ite_true]" `
This command can also be used in `[simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic")` and `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticSimp_all?!_ "Permalink")tactic
```
[simp_all?!](Tactic-Proofs/Tactic-Reference/#simp_all______ "Documentation for tactic")
```

`[simp?](Tactic-Proofs/Tactic-Reference/#simp___-next "Documentation for tactic")` takes the same arguments as `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`, but reports an equivalent call to `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") only` that would be sufficient to close the goal. This is useful for reducing the size of the simp set in a local invocation to speed up processing.
`example (x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : ([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [True](Basic-Propositions/Truth/#True___intro "Documentation for True") [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x + 2 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 3) = x + 2 := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ (if [True](Basic-Propositions/Truth/#True___intro "Documentation for True") then x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 else 3) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2   `Try this:   [apply] simp only [↓reduceIte, Nat.add_left_cancel_iff]`[simp?](Tactic-Proofs/Tactic-Reference/#simp___-next "Documentation for tactic")All goals completed! 🐙 -- prints "Try this: simp only [ite_true]" `
This command can also be used in `[simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic")` and `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.simpAllArith "Permalink")tactic
```
[simp_all_arith](Tactic-Proofs/Tactic-Reference/#simp_all_arith "Documentation for tactic")
```

`[simp_all_arith](Tactic-Proofs/Tactic-Reference/#simp_all_arith "Documentation for tactic")` has been deprecated. It was a shorthand for `[simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic") +arith +decide`. Note that `+decide` is not needed for reducing arithmetic terms since simprocs have been added to Lean.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.simpAllArithBang "Permalink")tactic
```
[simp_all_arith!](Tactic-Proofs/Tactic-Reference/#simp_all_arith___ "Documentation for tactic")
```

`[simp_all_arith!](Tactic-Proofs/Tactic-Reference/#simp_all_arith___ "Documentation for tactic")` has been deprecated. It was a shorthand for `[simp_all!](Tactic-Proofs/Tactic-Reference/#simp_all___ "Documentation for tactic") +arith +decide`. Note that `+decide` is not needed for reducing arithmetic terms since simprocs have been added to Lean.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.simpa "Permalink")tactic
```
[simpa](Tactic-Proofs/Tactic-Reference/#simpa "Documentation for tactic")
```

This is a "finishing" tactic modification of `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`. It has two forms.
  * `[simpa](Tactic-Proofs/Tactic-Reference/#simpa "Documentation for tactic") [rules, ⋯] using e` will simplify the goal and the type of `e` using `rules`, then try to close the goal using `e`.


Simplifying the type of `e` makes it more likely to match the goal (which has also been simplified). This construction also tends to be more robust under changes to the simp lemma set.
  * `[simpa](Tactic-Proofs/Tactic-Reference/#simpa "Documentation for tactic") [rules, ⋯]` will simplify the goal and the type of a hypothesis `this` if present in the context, then try to close the goal using the `[assumption](Tactic-Proofs/Tactic-Reference/#assumption "Documentation for tactic")` tactic.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticSimpa!_ "Permalink")tactic
```
[simpa!](Tactic-Proofs/Tactic-Reference/#simpa___ "Documentation for tactic")
```

This is a "finishing" tactic modification of `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`. It has two forms.
  * `[simpa](Tactic-Proofs/Tactic-Reference/#simpa "Documentation for tactic") [rules, ⋯] using e` will simplify the goal and the type of `e` using `rules`, then try to close the goal using `e`.


Simplifying the type of `e` makes it more likely to match the goal (which has also been simplified). This construction also tends to be more robust under changes to the simp lemma set.
  * `[simpa](Tactic-Proofs/Tactic-Reference/#simpa "Documentation for tactic") [rules, ⋯]` will simplify the goal and the type of a hypothesis `this` if present in the context, then try to close the goal using the `[assumption](Tactic-Proofs/Tactic-Reference/#assumption "Documentation for tactic")` tactic.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticSimpa?_ "Permalink")tactic
```
[simpa?](Tactic-Proofs/Tactic-Reference/#simpa___-next "Documentation for tactic")
```

This is a "finishing" tactic modification of `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`. It has two forms.
  * `[simpa](Tactic-Proofs/Tactic-Reference/#simpa "Documentation for tactic") [rules, ⋯] using e` will simplify the goal and the type of `e` using `rules`, then try to close the goal using `e`.


Simplifying the type of `e` makes it more likely to match the goal (which has also been simplified). This construction also tends to be more robust under changes to the simp lemma set.
  * `[simpa](Tactic-Proofs/Tactic-Reference/#simpa "Documentation for tactic") [rules, ⋯]` will simplify the goal and the type of a hypothesis `this` if present in the context, then try to close the goal using the `[assumption](Tactic-Proofs/Tactic-Reference/#assumption "Documentation for tactic")` tactic.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticSimpa?!_ "Permalink")tactic
```
[simpa?!](Tactic-Proofs/Tactic-Reference/#simpa______ "Documentation for tactic")
```

This is a "finishing" tactic modification of `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`. It has two forms.
  * `[simpa](Tactic-Proofs/Tactic-Reference/#simpa "Documentation for tactic") [rules, ⋯] using e` will simplify the goal and the type of `e` using `rules`, then try to close the goal using `e`.


Simplifying the type of `e` makes it more likely to match the goal (which has also been simplified). This construction also tends to be more robust under changes to the simp lemma set.
  * `[simpa](Tactic-Proofs/Tactic-Reference/#simpa "Documentation for tactic") [rules, ⋯]` will simplify the goal and the type of a hypothesis `this` if present in the context, then try to close the goal using the `[assumption](Tactic-Proofs/Tactic-Reference/#assumption "Documentation for tactic")` tactic.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=tacticSimp_wf "Permalink")tactic
```
[simp_wf](Tactic-Proofs/Tactic-Reference/#simp_wf "Documentation for tactic")
```

Unfold definitions commonly used in well founded relation definitions.
Since Lean 4.12, Lean unfolds these definitions automatically before presenting the goal to the user, and this tactic should no longer be necessary. Calls to `[simp_wf](Tactic-Proofs/Tactic-Reference/#simp_wf "Documentation for tactic")` can be removed or replaced by plain calls to `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`.
##  14.5.14. Rewriting[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-rw "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.rwSeq "Permalink")tactic
```
[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")
```

`[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")` is like `[rewrite](Tactic-Proofs/Tactic-Reference/#rewrite "Documentation for tactic")`, but also tries to close the goal by "cheap" (reducible) `[rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")` afterwards.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.rewriteSeq "Permalink")tactic
```
[rewrite](Tactic-Proofs/Tactic-Reference/#rewrite "Documentation for tactic")
```

`[rewrite](Tactic-Proofs/Tactic-Reference/#rewrite "Documentation for tactic") [e]` applies identity `e` as a rewrite rule to the target of the main goal. If `e` is preceded by left arrow (`←` or `<-`), the rewrite is applied in the reverse direction. If `e` is a defined constant, then the equational theorems associated with `e` are used. This provides a convenient way to unfold `e`.
  * `rewrite [e₁, ..., eₙ]` applies the given rules sequentially.
  * `[rewrite](Tactic-Proofs/Tactic-Reference/#rewrite "Documentation for tactic") [e] at l` rewrites `e` at location(s) `l`, where `l` is either `*` or a list of hypotheses in the local context. In the latter case, a turnstile `⊢` or `|-` can also be used, to signify the target of the goal.


Using `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic") (occs := .pos L) [e]`, where `L : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, you can control which "occurrences" are rewritten. (This option applies to each rule, so usually this will only be used with a single rule.) Occurrences count from `1`. At each allowed occurrence, arguments of the rewrite rule `e` may be instantiated, restricting which later rewrites can be found. (Disallowed occurrences do not result in instantiation.) `(occs := .neg L)` allows skipping specified occurrences.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticErw___ "Permalink")tactic
```
[erw](Tactic-Proofs/Tactic-Reference/#erw "Documentation for tactic")
```

`[erw](Tactic-Proofs/Tactic-Reference/#erw "Documentation for tactic") [rules]` is a shorthand for `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic") (transparency := .default) [rules]`. This does rewriting up to unfolding of regular definitions (by comparison to regular `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")` which only unfolds `@[reducible]` definitions).
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticRwa__ "Permalink")tactic
```
[rwa](Tactic-Proofs/Tactic-Reference/#rwa "Documentation for tactic")
```

`[rwa](Tactic-Proofs/Tactic-Reference/#rwa "Documentation for tactic")` is short-hand for `rw; assumption`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Meta.Rewrite.Config "Permalink")structure
```


Lean.Meta.Rewrite.Config : Type


Lean.Meta.Rewrite.Config : Type


```

Configures the behavior of the `[rewrite](Tactic-Proofs/Tactic-Reference/#rewrite "Documentation for tactic")` and `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")` tactics.
#  Constructor

```
[Lean.Meta.Rewrite.Config.mk](Tactic-Proofs/Tactic-Reference/#Lean___Meta___Rewrite___Config___mk "Documentation for Lean.Meta.Rewrite.Config.mk")
```

#  Fields

```
transparency : [Lean.Meta.TransparencyMode](Tactic-Proofs/Tactic-Reference/#Lean___Meta___TransparencyMode___all "Documentation for Lean.Meta.TransparencyMode")
```

The transparency mode to use for unfolding

```
offsetCnstrs : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

Whether to support offset constraints such as `?x + 1 =?= e`

```
occs : [Lean.Meta.Occurrences](Tactic-Proofs/Tactic-Reference/#Lean___Meta___Occurrences___all "Documentation for Lean.Meta.Occurrences")
```

Which occurrences to rewrite

```
newGoals : [Lean.Meta.Rewrite.NewGoals](Tactic-Proofs/Tactic-Reference/#Lean___Meta___Rewrite___NewGoals "Documentation for Lean.Meta.Rewrite.NewGoals")
```

How to convert the resulting metavariables into new goals
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Meta.Occurrences "Permalink")inductive type
```


Lean.Meta.Occurrences : Type


Lean.Meta.Occurrences : Type


```

Configuration for which occurrences that match an expression should be rewritten.
#  Constructors

```
all : [Lean.Meta.Occurrences](Tactic-Proofs/Tactic-Reference/#Lean___Meta___Occurrences___all "Documentation for Lean.Meta.Occurrences")
```

All occurrences should be rewritten.

```
pos (idxs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Lean.Meta.Occurrences](Tactic-Proofs/Tactic-Reference/#Lean___Meta___Occurrences___all "Documentation for Lean.Meta.Occurrences")
```

A list of indices for which occurrences should be rewritten.

```
neg (idxs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Lean.Meta.Occurrences](Tactic-Proofs/Tactic-Reference/#Lean___Meta___Occurrences___all "Documentation for Lean.Meta.Occurrences")
```

A list of indices for which occurrences should not be rewritten.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Meta.TransparencyMode "Permalink")inductive type
```


Lean.Meta.TransparencyMode : Type


Lean.Meta.TransparencyMode : Type


```

Controls which constants `isDefEq` (definitional equality) and `whnf` (weak head normal form) are allowed to unfold.
**Background: "try-hard" vs "speculative" modes**
During **type checking of user input** , we assume the input is most likely correct, and we want Lean to try hard before reporting a failure. Here, it is fine to unfold `[semireducible]` definitions (the `.default` setting).
During **proof automation** (`[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`, `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")`, type class resolution), we perform many speculative `isDefEq` calls — most of which _fail_. In this setting, we do _not_ want to try hard: unfolding too many definitions is a performance footgun. This is why `.reducible` exists.
**The transparency hierarchy**
The levels form a linear order: `none < reducible < instances < default < all`. Each level unfolds everything the previous level does, plus more:
  * **`reducible`**: Only unfolds`[reducible]` definitions. Used for speculative `isDefEq` checks (e.g., discrimination tree lookups in `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`, type class resolution). Think of `[reducible]` as `[inline]` for type checking and indexing.
  * **`instances`**: Also unfolds`[implicit_reducible]` definitions. Instance diamonds are common: for example, `[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` can come from a direct instance or via `Semiring`. These instances are all definitionally equal but structurally different, so `isDefEq` must unfold them to confirm equality. This level also handles definitions used in types that appear in implicit arguments (e.g., `[Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add")`, `[Array.size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")`). However, these definitions must not be _eagerly_ reduced (instances become huge terms), and discrimination trees do not index them. This makes `.instances` safe for speculative checks involving implicit arguments without the performance cost of `.default`.
  * **`[default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default")`**: Also unfolds`[semireducible]` definitions (anything not `[irreducible]`). Used for type checking user input where we want to try hard.
  * **`all`**: Also unfolds`[irreducible]` definitions. Rarely used.


**Implicit arguments and transparency**
When proof automation (e.g., `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`, `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")`) applies a lemma, explicit arguments are checked at the caller's transparency (typically `.reducible`). But implicit arguments are often "invisible" to the user — if a lemma fails to apply because of an implicit argument mismatch, the user is confused. Historically, Lean bumped transparency to `.default` for implicit arguments, but this eventually became a performance bottleneck in Mathlib. The option `backward.isDefEq.respectTransparency` (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`) disables this bump. Instead, instance-implicit arguments (`[..]`) are checked at `.instances`, and other implicit arguments are checked at the caller's transparency.
See also: `ReducibilityStatus`, `backward.isDefEq.respectTransparency`, `backward.whnf.reducibleClassField`.
#  Constructors

```
all : [Lean.Meta.TransparencyMode](Tactic-Proofs/Tactic-Reference/#Lean___Meta___TransparencyMode___all "Documentation for Lean.Meta.TransparencyMode")
```

Unfolds all constants, even those tagged as `@[irreducible]`.

```
default : [Lean.Meta.TransparencyMode](Tactic-Proofs/Tactic-Reference/#Lean___Meta___TransparencyMode___all "Documentation for Lean.Meta.TransparencyMode")
```

Unfolds all constants except those tagged as `@[irreducible]`. Used for type checking user-written terms where we expect the input to be correct and want to try hard.

```
reducible : [Lean.Meta.TransparencyMode](Tactic-Proofs/Tactic-Reference/#Lean___Meta___TransparencyMode___all "Documentation for Lean.Meta.TransparencyMode")
```

Unfolds only constants tagged with the `@[reducible]` attribute. Used for speculative `isDefEq` in proof automation (`simp`, `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")`, type class resolution) where most checks fail and we must not try too hard.

```
instances : [Lean.Meta.TransparencyMode](Tactic-Proofs/Tactic-Reference/#Lean___Meta___TransparencyMode___all "Documentation for Lean.Meta.TransparencyMode")
```

Unfolds reducible constants and constants tagged with `@[implicit_reducible]`. Used for checking implicit arguments during proof automation, and for unfolding class projections applied to instances. Instance diamonds (e.g., `[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` from a direct instance vs from `Semiring`) are definitionally equal but structurally different, so `isDefEq` must unfold them. Also handles definitions used in types of implicit arguments (e.g., `[Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add")`, `[Array.size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")`).

```
none : [Lean.Meta.TransparencyMode](Tactic-Proofs/Tactic-Reference/#Lean___Meta___TransparencyMode___all "Documentation for Lean.Meta.TransparencyMode")
```

Do not unfold anything.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Meta.Rewrite.NewGoals "Permalink")def
```


Lean.Meta.Rewrite.NewGoals : Type


Lean.Meta.Rewrite.NewGoals : Type


```

Controls which new mvars are turned in to goals by the `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic")` tactic.
  * `nonDependentFirst` mvars that don't depend on other goals appear first in the goal list.
  * `nonDependentOnly` only mvars that don't depend on other goals are added to goal list.
  * `all` all unassigned mvars are added to the goal list.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.unfold "Permalink")tactic
```
[unfold](Tactic-Proofs/Tactic-Reference/#unfold "Documentation for tactic")
```

  * `[unfold](Tactic-Proofs/Tactic-Reference/#unfold "Documentation for tactic") id` unfolds all occurrences of definition `id` in the target.
  * `unfold id1 id2 ...` is equivalent to `unfold id1; unfold id2; ...`.
  * `[unfold](Tactic-Proofs/Tactic-Reference/#unfold "Documentation for tactic") id at h` unfolds at the hypothesis `h`.


Definitions can be either global or local definitions.
For non-recursive global definitions, this tactic is identical to `[delta](Tactic-Proofs/Tactic-Reference/#delta "Documentation for tactic")`. For recursive global definitions, it uses the "unfolding lemma" `id.eq_def`, which is generated for each recursive definition, to unfold according to the recursive definition given by the user. Only one level of unfolding is performed, in contrast to `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") only [id]`, which unfolds definition `id` recursively.
Implemented by `Lean.Elab.Tactic.evalUnfold`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.replace "Permalink")tactic
```
[replace](Tactic-Proofs/Tactic-Reference/#replace "Documentation for tactic")
```

Acts like `have`, but removes a hypothesis with the same name as this one if possible. For example, if the state is:

```
f : α → β
h : α
⊢ goal

```

Then after `[replace](Tactic-Proofs/Tactic-Reference/#replace "Documentation for tactic") h := f h` the state will be:

```
f : α → β
h : β
⊢ goal

```

whereas `have h := f h` would result in:

```
f : α → β
h† : α
h : β
⊢ goal

```

This can be used to simulate the `specialize` and `apply at` tactics of Coq.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.delta "Permalink")tactic
```
[delta](Tactic-Proofs/Tactic-Reference/#delta "Documentation for tactic")
```

`delta id1 id2 ...` delta-expands the definitions `id1`, `id2`, .... This is a low-level tactic, it will expose how recursive definitions have been compiled by Lean.
##  14.5.15. Inductive Types[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-inductive "Permalink")
###  14.5.15.1. Introduction[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-inductive-intro "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.constructor "Permalink")tactic
```
[constructor](Tactic-Proofs/Tactic-Reference/#constructor "Documentation for tactic")
```

If the main goal's target type is an inductive type, `[constructor](Tactic-Proofs/Tactic-Reference/#constructor "Documentation for tactic")` solves it with the first matching constructor, or else fails.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.injection "Permalink")tactic
```
[injection](Tactic-Proofs/Tactic-Reference/#injection "Documentation for tactic")
```

The `[injection](Tactic-Proofs/Tactic-Reference/#injection "Documentation for tactic")` tactic is based on the fact that constructors of inductive data types are injections. That means that if `c` is a constructor of an inductive datatype, and if `(c t₁)` and `(c t₂)` are two terms that are equal then `t₁` and `t₂` are equal too. If `q` is a proof of a statement of conclusion `t₁ = t₂`, then injection applies injectivity to derive the equality of all arguments of `t₁` and `t₂` placed in the same positions. For example, from `(a::b) = (c::d)` we derive `a=c` and `b=d`. To use this tactic `t₁` and `t₂` should be constructor applications of the same constructor. Given `h : a::b = c::d`, the tactic `[injection](Tactic-Proofs/Tactic-Reference/#injection "Documentation for tactic") h` adds two new hypothesis with types `a = c` and `b = d` to the main goal. The tactic `[injection](Tactic-Proofs/Tactic-Reference/#injection "Documentation for tactic") h with h₁ h₂` uses the names `h₁` and `h₂` to name the new hypotheses.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.injections "Permalink")tactic
```
[injections](Tactic-Proofs/Tactic-Reference/#injections "Documentation for tactic")
```

`[injections](Tactic-Proofs/Tactic-Reference/#injections "Documentation for tactic")` applies `[injection](Tactic-Proofs/Tactic-Reference/#injection "Documentation for tactic")` to all hypotheses recursively (since `[injection](Tactic-Proofs/Tactic-Reference/#injection "Documentation for tactic")` can produce new hypotheses). Useful for destructing nested constructor equalities like `(a::b::c) = (d::e::f)`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.left "Permalink")tactic
```
[left](Tactic-Proofs/Tactic-Reference/#left "Documentation for tactic")
```

Applies the first constructor when the goal is an inductive type with exactly two constructors, or fails otherwise.
`example : [True](Basic-Propositions/Truth/#True___intro "Documentation for True") ∨ [False](Basic-Propositions/Truth/#False "Documentation for False") := by⊢ [True](Basic-Propositions/Truth/#True___intro "Documentation for True") [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") [False](Basic-Propositions/Truth/#False "Documentation for False")   [left](Tactic-Proofs/Tactic-Reference/#left "Documentation for tactic")h⊢ [True](Basic-Propositions/Truth/#True___intro "Documentation for True")   [trivial](Tactic-Proofs/Tactic-Reference/#trivial "Documentation for tactic")All goals completed! 🐙 `
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.right "Permalink")tactic
```
[right](Tactic-Proofs/Tactic-Reference/#right "Documentation for tactic")
```

Applies the second constructor when the goal is an inductive type with exactly two constructors, or fails otherwise.
`example {p q : Prop} (h : q) : p ∨ q := byp:Propq:Proph:q⊢ p [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") q   [right](Tactic-Proofs/Tactic-Reference/#right "Documentation for tactic")hp:Propq:Proph:q⊢ q   [exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic") hAll goals completed! 🐙 `
###  14.5.15.2. Elimination[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-inductive-elim "Permalink")
Elimination tactics use [recursors](The-Type-System/Inductive-Types/#recursors) and the automatically-derived [`casesOn` helper](The-Type-System/Inductive-Types/#recursor-elaboration-helpers) to implement induction and case splitting. The [subgoals](Tactic-Proofs/#--tech-term-subgoals) that result from these tactics are determined by the types of the minor premises of the eliminators, and using different eliminators with the `using` option results in different subgoals.
Choosing Eliminators
When attempting to prove that `∀(i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n + 1)), 0 + i = i`, after introducing the hypotheses the tactic `[induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic") imkn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")val✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")isLt✝:val✝ [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [⟨](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.mk")val✝[,](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.mk") isLt✝[⟩](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.mk") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [⟨](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.mk")val✝[,](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.mk") isLt✝[⟩](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.mk")` results in:
mkn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")val✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")isLt✝:val✝ [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [⟨](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.mk")val✝[,](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.mk") isLt✝[⟩](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.mk") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [⟨](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.mk")val✝[,](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.mk") isLt✝[⟩](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.mk")
This is because `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` is a [structure](The-Type-System/Inductive-Types/#--tech-term-Structures) with a single non-recursive constructor. Its recursor has a single minor premise for this constructor:
`Fin.rec.{u} {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} {motive : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → Sort u}   (mk : (val : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) →     (isLt : val < n) →     motive ⟨val, isLt⟩)   (t : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) : motive t`
Using the tactic `[induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic") i using [Fin.induction](Basic-Types/Finite-Natural-Numbers/#Fin___induction "Documentation for Fin.induction")zeron:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0succn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")i✝:[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") na✝:0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") i✝.[castSucc](Basic-Types/Finite-Natural-Numbers/#Fin___castSucc "Documentation for Fin.castSucc") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") i✝.[castSucc](Basic-Types/Finite-Natural-Numbers/#Fin___castSucc "Documentation for Fin.castSucc")⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") i✝.[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") i✝.[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ")` instead results in:
zeron:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0succn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")i✝:[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") na✝:0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") i✝.[castSucc](Basic-Types/Finite-Natural-Numbers/#Fin___castSucc "Documentation for Fin.castSucc") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") i✝.[castSucc](Basic-Types/Finite-Natural-Numbers/#Fin___castSucc "Documentation for Fin.castSucc")⊢ 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") i✝.[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") i✝.[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ")
`[Fin.induction](Basic-Types/Finite-Natural-Numbers/#Fin___induction "Documentation for Fin.induction")` is an alternative eliminator that implements induction on the underlying `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`:
`[Fin.induction](Basic-Types/Finite-Natural-Numbers/#Fin___induction "Documentation for Fin.induction").{u} {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}   {motive : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n + 1) → Sort u}   (zero : motive 0)   (succ : (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n) →     motive i.[castSucc](Basic-Types/Finite-Natural-Numbers/#Fin___castSucc "Documentation for Fin.castSucc") →     motive i.[succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ"))   (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n + 1)) : motive i`
Custom eliminators can be registered using the `induction_eliminator` and `cases_eliminator` attributes. The eliminator is registered for its explicit targets (i.e. those that are explicit, rather than implicit, parameters to the eliminator function) and will be applied when `[induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic")` or `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")` is used on targets of those types. When present, custom eliminators take precedence over recursors. Setting `[tactic.customEliminators](Tactic-Proofs/Options/#tactic___customEliminators "Documentation for option tactic.customEliminators")` to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` disables the use of custom eliminators.
attributeCustom Eliminators
The `induction_eliminator` attribute registers an eliminator for use by the `[induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic")` tactic.

```
attr ::= ...
    | induction_eliminator
```

The `cases_eliminator` attribute registers an eliminator for use by the `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")` tactic.

```
attr ::= ...
    | cases_eliminator
```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.cases "Permalink")tactic
```
[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")
```

Assuming `x` is a variable in the local context with an inductive type, `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") x` splits the main goal, producing one goal for each constructor of the inductive type, in which the target is replaced by a general instance of that constructor. If the type of an element in the local context depends on `x`, that element is reverted and reintroduced afterward, so that the case split affects that hypothesis as well. `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")` detects unreachable cases and closes them automatically.
For example, given `n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` and a goal with a hypothesis `h : P n` and target `Q n`, `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") n` produces one goal with hypothesis `h : P 0` and target `Q 0`, and one goal with hypothesis `h : P (Nat.succ a)` and target `Q (Nat.succ a)`. Here the name `a` is chosen automatically and is not accessible. You can use `with` to provide the variables names for each constructor.
  * `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") e`, where `e` is an expression instead of a variable, generalizes `e` in the goal, and then cases on the resulting variable.
  * Given `as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α`, `cases as with | nil => tac₁ | cons a as' => tac₂`, uses tactic `tac₁` for the `nil` case, and `tac₂` for the `cons` case, and `a` and `as'` are used as names for the new variables introduced.
  * `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") h : e`, where `e` is a variable or an expression, performs cases on `e` as above, but also adds a hypothesis `h : e = ...` to each goal, where `...` is the constructor instance for that particular case.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.rcases "Permalink")tactic
```
[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic")
```

`[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic")` is a tactic that will perform `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")` recursively, according to a pattern. It is used to destructure hypotheses or expressions composed of inductive types like `h1 : a ∧ b ∧ c ∨ d` or `h2 : ∃ x y, trans_rel R x y`. Usual usage might be `[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic") h1 with ⟨ha, hb, hc⟩ | hd` or `[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic") h2 with ⟨x, y, _ | ⟨z, hxz, hzy⟩⟩` for these examples.
Each element of an `[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic")` pattern is matched against a particular local hypothesis (most of which are generated during the execution of `[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic")` and represent individual elements destructured from the input expression). An `[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic")` pattern has the following grammar:
  * A name like `x`, which names the active hypothesis as `x`.
  * A blank `_`, which does nothing (letting the automatic naming system used by `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")` name the hypothesis).
  * A hyphen `-`, which clears the active hypothesis and any dependents.
  * The keyword `[rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`, which expects the hypothesis to be `h : a = b`, and calls `[subst](Tactic-Proofs/Tactic-Reference/#subst "Documentation for tactic")` on the hypothesis (which has the effect of replacing `b` with `a` everywhere or vice versa).
  * A type ascription `p : ty`, which sets the type of the hypothesis to `ty` and then matches it against `p`. (Of course, `ty` must unify with the actual type of `h` for this to work.)
  * A tuple pattern `⟨p1, p2, p3⟩`, which matches a constructor with many arguments, or a series of nested conjunctions or existentials. For example if the active hypothesis is `a ∧ b ∧ c`, then the conjunction will be destructured, and `p1` will be matched against `a`, `p2` against `b` and so on.
  * A `@` before a tuple pattern as in `@⟨p1, p2, p3⟩` will bind all arguments in the constructor, while leaving the `@` off will only use the patterns on the explicit arguments.
  * An alternation pattern `p1 | p2 | p3`, which matches an inductive type with multiple constructors, or a nested disjunction like `a ∨ b ∨ c`.


A pattern like `⟨a, b, c⟩ | ⟨d, e⟩` will do a split over the inductive datatype, naming the first three parameters of the first constructor as `a,b,c` and the first two of the second constructor `d,e`. If the list is not as long as the number of arguments to the constructor or the number of constructors, the remaining variables will be automatically named. If there are nested brackets such as `⟨⟨a⟩, b | c⟩ | d` then these will cause more case splits as necessary. If there are too many arguments, such as `⟨a, b, c⟩` for splitting on `∃ x, ∃ y, p x`, then it will be treated as `⟨a, ⟨b, c⟩⟩`, splitting the last parameter as necessary.
`[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic")` also has special support for quotient types: quotient induction into Prop works like matching on the constructor `quot.mk`.
`[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic") h : e with PAT` will do the same as `[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic") e with PAT` with the exception that an assumption `h : e = PAT` will be added to the context.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.funCases "Permalink")tactic
```
[fun_cases](Tactic-Proofs/Tactic-Reference/#fun_cases "Documentation for tactic")
```

The `fun_cases` tactic is a convenience wrapper of the `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")` tactic when using a functional cases principle.
The tactic invocation

```
fun_cases f x ... y ...`

```

is equivalent to

```
cases y, ... using f.fun_cases_unfolding x ...

```

where the arguments of `f` are used as arguments to `f.fun_cases_unfolding` or targets of the case analysis, as appropriate.
The form
`fun_cases f`
(with no arguments to `f`) searches the goal for a unique eligible application of `f`, and uses these arguments. An application of `f` is eligible if it is saturated and the arguments that will become targets are free variables.
The form `fun_cases f x y with | case1 => tac₁ | case2 x' ih => tac₂` works like with `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")`.
Under `set_option tactic.fun_induction.unfolding true` (the default), `[fun_induction](Tactic-Proofs/Tactic-Reference/#fun_induction "Documentation for tactic")` uses the `f.fun_cases_unfolding` theorem, which will try to automatically unfold the call to `f` in the goal. With `set_option tactic.fun_induction.unfolding false`, it uses `f.fun_cases` instead.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.induction "Permalink")tactic
```
[induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic")
```

Assuming `x` is a variable in the local context with an inductive type, `[induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic") x` applies induction on `x` to the main goal, producing one goal for each constructor of the inductive type, in which the target is replaced by a general instance of that constructor and an inductive hypothesis is added for each recursive argument to the constructor. If the type of an element in the local context depends on `x`, that element is reverted and reintroduced afterward, so that the inductive hypothesis incorporates that hypothesis as well.
For example, given `n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` and a goal with a hypothesis `h : P n` and target `Q n`, `[induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic") n` produces one goal with hypothesis `h : P 0` and target `Q 0`, and one goal with hypotheses `h : P (Nat.succ a)` and `ih₁ : P a → Q a` and target `Q (Nat.succ a)`. Here the names `a` and `ih₁` are chosen automatically and are not accessible. You can use `with` to provide the variables names for each constructor.
  * `[induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic") e`, where `e` is an expression instead of a variable, generalizes `e` in the goal, and then performs induction on the resulting variable.
  * `[induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic") e using r` allows the user to specify the principle of induction that should be used. Here `r` should be a term whose result type must be of the form `C t`, where `C` is a bound variable and `t` is a (possibly empty) sequence of bound variables
  * `[induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic") e generalizing z₁ ... zₙ`, where `z₁ ... zₙ` are variables in the local context, generalizes over `z₁ ... zₙ` before applying the induction but then introduces them in each goal. In other words, the net effect is that each inductive hypothesis is generalized.
  * Given `x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, `induction x with | zero => tac₁ | succ x' ih => tac₂` uses tactic `tac₁` for the `zero` case, and `tac₂` for the `succ` case.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.funInduction "Permalink")tactic
```
[fun_induction](Tactic-Proofs/Tactic-Reference/#fun_induction "Documentation for tactic")
```

The `[fun_induction](Tactic-Proofs/Tactic-Reference/#fun_induction "Documentation for tactic")` tactic is a convenience wrapper around the `[induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic")` tactic to use the functional induction principle.
The tactic invocation
`fun_induction f x₁ ... xₙ y₁ ... yₘ`
where `f` is a function defined by non-mutual structural or well-founded recursion, is equivalent to

```
induction y₁, ... yₘ using f.induct_unfolding x₁ ... xₙ

```

where the arguments of `f` are used as arguments to `f.induct_unfolding` or targets of the induction, as appropriate.
The form
`fun_induction f`
(with no arguments to `f`) searches the goal for a unique eligible application of `f`, and uses these arguments. An application of `f` is eligible if it is saturated and the arguments that will become targets are free variables.
The forms `[fun_induction](Tactic-Proofs/Tactic-Reference/#fun_induction "Documentation for tactic") f x y generalizing z₁ ... zₙ` and `fun_induction f x y with | case1 => tac₁ | case2 x' ih => tac₂` work like with `[induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic").`
Under `set_option tactic.fun_induction.unfolding true` (the default), `[fun_induction](Tactic-Proofs/Tactic-Reference/#fun_induction "Documentation for tactic")` uses the `f.induct_unfolding` induction principle, which will try to automatically unfold the call to `f` in the goal. With `set_option tactic.fun_induction.unfolding false`, it uses `f.induct` instead.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticNofun "Permalink")tactic
```
[nofun](Tactic-Proofs/Tactic-Reference/#nofun "Documentation for tactic")
```

The tactic `[nofun](Tactic-Proofs/Tactic-Reference/#nofun "Documentation for tactic")` is shorthand for `[exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic") [nofun](Terms/Pattern-Matching/#Lean___Parser___Term___nofun "Documentation for syntax")`: it introduces the assumptions, then performs an empty pattern match, closing the goal if the introduced pattern is impossible.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.%C2%ABtacticNomatch_,,%C2%BB "Permalink")tactic
```
[nomatch](Tactic-Proofs/Tactic-Reference/#nomatch "Documentation for tactic")
```

The tactic `[nomatch](Tactic-Proofs/Tactic-Reference/#nomatch "Documentation for tactic") h` is shorthand for `[exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic") [nomatch](Terms/Pattern-Matching/#Lean___Parser___Term___nomatch "Documentation for syntax") h`.
##  14.5.16. Library Search[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-search "Permalink")
The library search tactics are intended for interactive use. When run, they search the Lean library for lemmas or rewrite rules that could be applicable in the current situation, and suggests a new tactic. These tactics should not be left in a proof; rather, their suggestions should be incorporated.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.exact? "Permalink")tactic
```
[exact?](Tactic-Proofs/Tactic-Reference/#exact___ "Documentation for tactic")
```

Searches environment for definitions or theorems that can solve the goal using `[exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic")` with conditions resolved by `[solve_by_elim](Tactic-Proofs/Tactic-Reference/#solve_by_elim "Documentation for tactic")`.
The optional `using` clause provides identifiers in the local context that must be used by `[exact?](Tactic-Proofs/Tactic-Reference/#exact___ "Documentation for tactic")` when closing the goal. This is most useful if there are multiple ways to resolve the goal, and one wants to guide which lemma is used.
Use `+grind` to enable `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` as a fallback discharger for subgoals. Use `+try?` to enable `try?` as a fallback discharger for subgoals. Use `-star` to disable fallback to star-indexed lemmas (like `[Empty.elim](Basic-Types/The-Empty-Type/#Empty___elim "Documentation for Empty.elim")`, `[And.left](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And.left")`). Use `+all` to collect all successful lemmas instead of stopping at the first.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.apply? "Permalink")tactic
```
[apply?](Tactic-Proofs/Tactic-Reference/#apply___ "Documentation for tactic")
```

Searches environment for definitions or theorems that can refine the goal using `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic")` with conditions resolved when possible with `[solve_by_elim](Tactic-Proofs/Tactic-Reference/#solve_by_elim "Documentation for tactic")`.
The optional `using` clause provides identifiers in the local context that must be used when closing the goal.
Use `+grind` to enable `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` as a fallback discharger for subgoals. Use `+try?` to enable `try?` as a fallback discharger for subgoals. Use `-star` to disable fallback to star-indexed lemmas. Use `+all` to collect all successful lemmas instead of stopping at the first.
In this proof state:
i:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")j:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") jh2:j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k⊢ i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k
invoking ``Try this:   [apply] exact Nat.lt_trans h1 h2`[apply?](Tactic-Proofs/Tactic-Reference/#apply___ "Documentation for tactic")All goals completed! 🐙` suggests:

```
Try this:
  [apply] exact Nat.lt_trans h1 h2

```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.rewrites? "Permalink")tactic
```
[rw?](Tactic-Proofs/Tactic-Reference/#rw___ "Documentation for tactic")
```

`[rw?](Tactic-Proofs/Tactic-Reference/#rw___ "Documentation for tactic")` tries to find a lemma which can rewrite the goal.
`[rw?](Tactic-Proofs/Tactic-Reference/#rw___ "Documentation for tactic")` should not be left in proofs; it is a search tool, like `[apply?](Tactic-Proofs/Tactic-Reference/#apply___ "Documentation for tactic")`.
Suggestions are printed as `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic") [h]` or `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic") [← h]`.
You can use `[rw?](Tactic-Proofs/Tactic-Reference/#rw___ "Documentation for tactic") [-my_lemma, -my_theorem]` to prevent `[rw?](Tactic-Proofs/Tactic-Reference/#rw___ "Documentation for tactic")` using the named lemmas.
##  14.5.17. Case Analysis[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-cases "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.split "Permalink")tactic
```
[split](Tactic-Proofs/Tactic-Reference/#split "Documentation for tactic")
```

The `[split](Tactic-Proofs/Tactic-Reference/#split "Documentation for tactic")` tactic is useful for breaking nested if-then-else and `[match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic")` expressions into separate cases. For a `[match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic")` expression with `n` cases, the `[split](Tactic-Proofs/Tactic-Reference/#split "Documentation for tactic")` tactic generates at most `n` subgoals.
For example, given `n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, and a target `[if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n = 0 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") Q [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") R`, `[split](Tactic-Proofs/Tactic-Reference/#split "Documentation for tactic")` will generate one goal with hypothesis `n = 0` and target `Q`, and a second goal with hypothesis `¬n = 0` and target `R`. Note that the introduced hypothesis is unnamed, and is commonly renamed using the `[case](Tactic-Proofs/The-Tactic-Language/#case "Documentation for tactic")` or `[next](Tactic-Proofs/The-Tactic-Language/#next "Documentation for tactic")` tactics.
  * `[split](Tactic-Proofs/Tactic-Reference/#split "Documentation for tactic")` will split the goal (target).
  * `[split](Tactic-Proofs/Tactic-Reference/#split "Documentation for tactic") at h` will split the hypothesis `h`.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=%C2%ABtacticBy_cases_:_%C2%BB "Permalink")tactic
```
[by_cases](Tactic-Proofs/Tactic-Reference/#by_cases "Documentation for tactic")
```

`by_cases (h :)? p` splits the main goal into two cases, assuming `h : p` in the first branch, and `h : ¬ p` in the second branch.
##  14.5.18. Decision Procedures[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-decision "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.decide "Permalink")tactic
```
[decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")
```

`[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide")` attempts to prove the main goal (with target type `p`) by synthesizing an instance of `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") p` and then reducing that instance to evaluate the truth value of `p`. If it reduces to `[isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") h`, then `h` is a proof of `p` that closes the goal.
The target is not allowed to contain local variables or metavariables. If there are local variables, you can first try using the `[revert](Tactic-Proofs/The-Tactic-Language/#revert "Documentation for tactic")` tactic with these local variables to move them into the target, or you can use the `+revert` option, described below.
Options:
  * `[decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic") +revert` begins by reverting local variables that the target depends on, after cleaning up the local context of irrelevant variables. A variable is _relevant_ if it appears in the target, if it appears in a relevant variable, or if it is a proposition that refers to a relevant variable.
  * `[decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic") +kernel` uses kernel for reduction instead of the elaborator. It has two key properties: (1) since it uses the kernel, it ignores transparency and can unfold everything, and (2) it reduces the `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` instance only once instead of twice.
  * `[decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic") +native` uses the native code compiler (`#eval`) to evaluate the `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` instance, admitting the result via an axiom. This can be significantly more efficient than using reduction, but it is at the cost of increasing the size This can be significantly more efficient than using reduction, but it is at the cost of increasing the size of the trusted code base. Namely, it depends on the correctness of the Lean compiler and all definitions with an `@[implemented_by]` attribute. Like with `+kernel`, the `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` instance is evaluated only once.


Limitation: In the default mode or `+kernel` mode, since `[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide")` uses reduction to evaluate the term, `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` instances defined by well-founded recursion might not work because evaluating them requires reducing proofs. Reduction can also get stuck on `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` instances with `Eq.rec` terms. These can appear in instances defined using tactics (such as `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")` and `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`). To avoid this, create such instances using definitions such as `decidable_of_iff` instead.
**Examples**
Proving inequalities:
`example : 2 + 2 ≠ 5 := by⊢ 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 ≠ 5 [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")All goals completed! 🐙 `
Trying to prove a false proposition:

```
example : 1 ≠ 1 := by decide
/-
tactic 'decide' proved that the proposition
  1 ≠ 1
is false
-/

```

Trying to prove a proposition whose `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` instance fails to reduce

```
opaque unknownProp : Prop

open scoped Classical in
example : unknownProp := by decide
/-
tactic 'decide' failed for proposition
  unknownProp
since its 'Decidable' instance reduced to
  Classical.choice ⋯
rather than to the 'isTrue' constructor.
-/

```

**Properties and relations**
For equality goals for types with decidable equality, usually `[rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")` can be used in place of `[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide")`.
`example : 1 + 1 = 2 := by⊢ 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 2 [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")All goals completed! 🐙 example : 1 + 1 = 2 := by⊢ 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 2 [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 `
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.nativeDecide "Permalink")tactic
```
[native_decide](Tactic-Proofs/Tactic-Reference/#native_decide "Documentation for tactic")
```

`[native_decide](Tactic-Proofs/Tactic-Reference/#native_decide "Documentation for tactic")` is a synonym for `[decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic") +native`. It will attempt to prove a goal of type `p` by synthesizing an instance of `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") p` and then evaluating it to `[isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") ..`. Unlike `[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide")`, this uses `#eval` to evaluate the decidability instance.
This should be used with care because it adds the entire lean compiler to the trusted part, and a new axiom will show up in `#print axioms` for theorems using this method or anything that transitively depends on them. Nevertheless, because it is compiled, this can be significantly more efficient than using `[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide")`, and for very large computations this is one way to run external programs and trust the result.
`example : ([List.range](Basic-Types/Linked-Lists/#List___range "Documentation for List.range") 1000).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") = 1000 := by⊢ ([List.range](Basic-Types/Linked-Lists/#List___range "Documentation for List.range") 1000).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1000 [native_decide](Tactic-Proofs/Tactic-Reference/#native_decide "Documentation for tactic")All goals completed! 🐙 `
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.omega "Permalink")tactic
```
[omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic")
```

The `[omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic")` tactic, for resolving integer and natural linear arithmetic problems.
It is not yet a full decision procedure (no "dark" or "grey" shadows), but should be effective on many problems.
We handle hypotheses of the form `x = y`, `x < y`, `x ≤ y`, and `k ∣ x` for `x y` in `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` or `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` (and `k` a literal), along with negations of these statements.
We decompose the sides of the inequalities as linear combinations of atoms.
If we encounter `x / k` or `x % k` for literal integers `k` we introduce new auxiliary variables and the relevant inequalities.
On the first pass, we do not perform case splits on natural subtraction. If `[omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic")` fails, we recursively perform a case split on a natural subtraction appearing in a hypothesis, and try again.
The options

```
omega +splitDisjunctions +splitNatSub +splitNatAbs +splitMinMax

```

can be used to:
  * `splitDisjunctions`: split any disjunctions found in the context, if the problem is not otherwise solvable.
  * `splitNatSub`: for each appearance of `((a - b : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int"))`, split on `a ≤ b` if necessary.
  * `splitNatAbs`: for each appearance of `[Int.natAbs](Basic-Types/Integers/#Int___natAbs "Documentation for Int.natAbs") a`, split on `0 ≤ a` if necessary.
  * `splitMinMax`: for each occurrence of `[min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min.min") a b`, split on `[min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min.min") a b = a ∨ [min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min.min") a b = b` Currently, all of these are on by default.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticBv_omega "Permalink")tactic
```
[bv_omega](Tactic-Proofs/Tactic-Reference/#bv_omega "Documentation for tactic")
```

`[bv_omega](Tactic-Proofs/Tactic-Reference/#bv_omega "Documentation for tactic")` is `[omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic")` with an additional preprocessor that turns statements about `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec")` into statements about `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`. Currently the preprocessor is implemented as `[try](Tactic-Proofs/The-Tactic-Language/#try "Documentation for tactic") [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") only [bitvec_to_nat] at *`. `bitvec_to_nat` is a `@[simp]` attribute that you can (cautiously) add to more theorems.
###  14.5.18.1. SAT Solver Integration[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-sat "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.bvDecideMacro "Permalink")tactic
```
[bv_decide](Tactic-Proofs/Tactic-Reference/#bv_decide "Documentation for tactic")
```

Close fixed-width `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec")` and `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` goals by obtaining a proof from an external SAT solver and verifying it inside Lean. The solvable goals are currently limited to
  * the Lean equivalent of [`QF_BV`](https://smt-lib.org/logics-all.shtml#QF_BV)
  * automatically splitting up `structure`s that contain information about `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec")` or `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`

`example : ∀ (a b : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 64), (a &&& b) + (a ^^^ b) = a ||| b := by⊢ ∀ (a b : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 64), [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")a [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") b[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HXor___mk "Documentation for HXor.hXor")a [^^^](Type-Classes/Basic-Classes/#HXor___mk "Documentation for HXor.hXor") b[)](Type-Classes/Basic-Classes/#HXor___mk "Documentation for HXor.hXor") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [|||](Type-Classes/Basic-Classes/#HOr___mk "Documentation for HOr.hOr") b   [intros](Tactic-Proofs/Tactic-Reference/#intros "Documentation for tactic")a✝:[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 64b✝:[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 64⊢ [(](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd")a✝ [&&&](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") b✝[)](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.hAnd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HXor___mk "Documentation for HXor.hXor")a✝ [^^^](Type-Classes/Basic-Classes/#HXor___mk "Documentation for HXor.hXor") b✝[)](Type-Classes/Basic-Classes/#HXor___mk "Documentation for HXor.hXor") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a✝ [|||](Type-Classes/Basic-Classes/#HOr___mk "Documentation for HOr.hOr") b✝   bv_decideAll goals completed! 🐙 `
If `bv_decide` encounters an unknown definition it will be treated like an unconstrained `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec")` variable. Sometimes this enables solving goals despite not understanding the definition because the precise properties of the definition do not matter in the specific proof.
If `bv_decide` fails to close a goal it provides a counter-example, containing assignments for all terms that were considered as variables.
In order to avoid calling a SAT solver every time, the proof can be cached with `bv_decide?`.
If solving your problem relies inherently on using associativity or commutativity, consider enabling the `bv.ac_nf` option.
Note: `bv_decide` trusts the correctness of the code generator and adds a axioms asserting its result.
Note: include `import Std.Tactic.BVDecide`
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.bvNormalizeMacro "Permalink")tactic
```
[bv_normalize](Tactic-Proofs/Tactic-Reference/#bv_normalize "Documentation for tactic")
```

Run the normalization procedure of `bv_decide` only. Sometimes this is enough to solve basic `[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec")` goals already.
Note: include `import Std.Tactic.BVDecide`
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.bvCheck "Permalink")tactic
```
[bv_check](Tactic-Proofs/Tactic-Reference/#bv_check "Documentation for tactic")
```

This tactic works just like `bv_decide` but skips calling a SAT solver by using a proof that is already stored on disk. It is called with the name of an LRAT file in the same directory as the current Lean file:
`bv_check "proof.lrat"`
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.bvTraceMacro "Permalink")tactic
```
[bv_decide?](Tactic-Proofs/Tactic-Reference/#bv_decide___ "Documentation for tactic")
```

Suggest a proof script for a `bv_decide` tactic call. Useful for caching LRAT proofs.
Note: include `import Std.Tactic.BVDecide`
##  14.5.19. Controlling Reduction[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-reducibility "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.withReducible "Permalink")tactic
```
with_reducible
```

`with_reducible tacs` executes `tacs` using the reducible transparency setting. In this setting only definitions tagged as `[reducible]` are unfolded.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.withReducibleAndInstances "Permalink")tactic
```
with_reducible_and_instances
```

`with_reducible_and_instances tacs` executes `tacs` using the `.instances` transparency setting. In this setting only definitions tagged as `[reducible]` or type class instances are unfolded.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.withUnfoldingAll "Permalink")tactic
```
with_unfolding_all
```

`with_unfolding_all tacs` executes `tacs` using the `.all` transparency setting. In this setting all definitions that are not opaque are unfolded.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.withUnfoldingNone "Permalink")tactic
```
[with_unfolding_none](Tactic-Proofs/Tactic-Reference/#with_unfolding_none "Documentation for tactic")
```

`with_unfolding_none tacs` executes `tacs` using the `.none` transparency setting. In this setting no definitions are unfolded.
##  14.5.20. Control Flow[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-control "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.skip "Permalink")tactic
```
[skip](Tactic-Proofs/Tactic-Reference/#skip "Documentation for tactic")
```

`[skip](Tactic-Proofs/Tactic-Reference/#skip "Documentation for tactic")` does nothing.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.guardHyp "Permalink")tactic
```
[guard_hyp](Tactic-Proofs/Tactic-Reference/#guard_hyp "Documentation for tactic")
```

Tactic to check that a named hypothesis has a given type and/or value.
  * `[guard_hyp](Tactic-Proofs/Tactic-Reference/#guard_hyp "Documentation for tactic") h : t` checks the type up to reducible defeq,
  * `[guard_hyp](Tactic-Proofs/Tactic-Reference/#guard_hyp "Documentation for tactic") h :~ t` checks the type up to default defeq,
  * `[guard_hyp](Tactic-Proofs/Tactic-Reference/#guard_hyp "Documentation for tactic") h :ₛ t` checks the type up to syntactic equality,
  * `[guard_hyp](Tactic-Proofs/Tactic-Reference/#guard_hyp "Documentation for tactic") h :ₐ t` checks the type up to alpha equality.
  * `[guard_hyp](Tactic-Proofs/Tactic-Reference/#guard_hyp "Documentation for tactic") h := v` checks value up to reducible defeq,
  * `[guard_hyp](Tactic-Proofs/Tactic-Reference/#guard_hyp "Documentation for tactic") h :=~ v` checks value up to default defeq,
  * `[guard_hyp](Tactic-Proofs/Tactic-Reference/#guard_hyp "Documentation for tactic") h :=ₛ v` checks value up to syntactic equality,
  * `[guard_hyp](Tactic-Proofs/Tactic-Reference/#guard_hyp "Documentation for tactic") h :=ₐ v` checks the value up to alpha equality.


The value `v` is elaborated using the type of `h` as the expected type.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.guardTarget "Permalink")tactic
```
[guard_target](Tactic-Proofs/Tactic-Reference/#guard_target "Documentation for tactic")
```

Tactic to check that the target agrees with a given expression.
  * `[guard_target](Tactic-Proofs/Tactic-Reference/#guard_target "Documentation for tactic") = e` checks that the target is defeq at reducible transparency to `e`.
  * `[guard_target](Tactic-Proofs/Tactic-Reference/#guard_target "Documentation for tactic") =~ e` checks that the target is defeq at default transparency to `e`.
  * `[guard_target](Tactic-Proofs/Tactic-Reference/#guard_target "Documentation for tactic") =ₛ e` checks that the target is syntactically equal to `e`.
  * `[guard_target](Tactic-Proofs/Tactic-Reference/#guard_target "Documentation for tactic") =ₐ e` checks that the target is alpha-equivalent to `e`.


The term `e` is elaborated with the type of the goal as the expected type, which is mostly useful within `conv` mode.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.guardExpr "Permalink")tactic
```
[guard_expr](Tactic-Proofs/Tactic-Reference/#guard_expr "Documentation for tactic")
```

Tactic to check equality of two expressions.
  * `[guard_expr](Tactic-Proofs/Tactic-Reference/#guard_expr "Documentation for tactic") e = e'` checks that `e` and `e'` are defeq at reducible transparency.
  * `[guard_expr](Tactic-Proofs/Tactic-Reference/#guard_expr "Documentation for tactic") e =~ e'` checks that `e` and `e'` are defeq at default transparency.
  * `[guard_expr](Tactic-Proofs/Tactic-Reference/#guard_expr "Documentation for tactic") e =ₛ e'` checks that `e` and `e'` are syntactically equal.
  * `[guard_expr](Tactic-Proofs/Tactic-Reference/#guard_expr "Documentation for tactic") e =ₐ e'` checks that `e` and `e'` are alpha-equivalent.


Both `e` and `e'` are elaborated then have their metavariables instantiated before the equality check. Their types are unified (using `isDefEqGuarded`) before synthetic metavariables are processed, which helps with default instance handling.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.done "Permalink")tactic
```
[done](Tactic-Proofs/Tactic-Reference/#done "Documentation for tactic")
```

`[done](Tactic-Proofs/Tactic-Reference/#done "Documentation for tactic")` succeeds iff there are no remaining goals.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.sleep "Permalink")tactic
```
[sleep](Tactic-Proofs/Tactic-Reference/#sleep "Documentation for tactic")
```

The tactic `sleep ms` sleeps for `ms` milliseconds and does nothing. It is used for debugging purposes only.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticStop_ "Permalink")tactic
```
[stop](Tactic-Proofs/Tactic-Reference/#stop "Documentation for tactic")
```

`[stop](Tactic-Proofs/Tactic-Reference/#stop "Documentation for tactic")` is a helper tactic for "discarding" the rest of a proof: it is defined as `[repeat](Tactic-Proofs/The-Tactic-Language/#repeat "Documentation for tactic") [sorry](Tactic-Proofs/Tactic-Reference/#sorry "Documentation for tactic")`. It is useful when working on the middle of a complex proofs, and less messy than commenting the remainder of the proof.
##  14.5.21. Term Elaboration Backends[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-term-helpers "Permalink")
These tactics are used during elaboration of terms to satisfy obligations that arise.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=tacticDecreasing_with_ "Permalink")tactic
```
[decreasing_with](Tactic-Proofs/Tactic-Reference/#decreasing_with "Documentation for tactic")
```

Constructs a proof of decreasing along a well founded relation, by simplifying, then applying lexicographic order lemmas and finally using `ts` to solve the base case. If it fails, it prints a message to help the user diagnose an ill-founded recursive definition.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=tacticGet_elem_tactic "Permalink")tactic
```
[get_elem_tactic](Tactic-Proofs/Tactic-Reference/#get_elem_tactic "Documentation for tactic")
```

`[get_elem_tactic](Tactic-Proofs/Tactic-Reference/#get_elem_tactic "Documentation for tactic")` is the tactic automatically called by the notation `arr[i]` to prove any side conditions that arise when constructing the term (e.g. the index is in bounds of the array). It just delegates to `get_elem_tactic_extensible` and gives a diagnostic error message otherwise; users are encouraged to extend `get_elem_tactic_extensible` instead of this tactic.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=tacticGet_elem_tactic_trivial "Permalink")tactic
```
[get_elem_tactic_trivial](Tactic-Proofs/Tactic-Reference/#get_elem_tactic_trivial "Documentation for tactic")
```

`[get_elem_tactic_trivial](Tactic-Proofs/Tactic-Reference/#get_elem_tactic_trivial "Documentation for tactic")` has been deprecated in favour of `get_elem_tactic_extensible`.
##  14.5.22. Debugging Utilities[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-debug "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticSorry "Permalink")tactic
```
[sorry](Tactic-Proofs/Tactic-Reference/#sorry "Documentation for tactic")
```

The `[sorry](Tactic-Proofs/Tactic-Reference/#sorry "Documentation for tactic")` tactic is a temporary placeholder for an incomplete tactic proof, closing the main goal using `[exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic") sorry`.
This is intended for stubbing-out incomplete parts of a proof while still having a syntactically correct proof skeleton. Lean will give a warning whenever a proof uses `[sorry](Tactic-Proofs/Tactic-Reference/#sorry "Documentation for tactic")`, so you aren't likely to miss it, but you can double check if a theorem depends on `[sorry](Tactic-Proofs/Tactic-Reference/#sorry "Documentation for tactic")` by looking for `sorryAx` in the output of the `#print axioms my_thm` command, the axiom used by the implementation of `[sorry](Tactic-Proofs/Tactic-Reference/#sorry "Documentation for tactic")`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticAdmit "Permalink")tactic
```
[admit](Tactic-Proofs/Tactic-Reference/#admit "Documentation for tactic")
```

`[admit](Tactic-Proofs/Tactic-Reference/#admit "Documentation for tactic")` is a synonym for `[sorry](Tactic-Proofs/Tactic-Reference/#sorry "Documentation for tactic")`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.dbgTrace "Permalink")tactic
```
[dbg_trace](Tactic-Proofs/Tactic-Reference/#dbg_trace "Documentation for tactic")
```

`[dbg_trace](Tactic-Proofs/Tactic-Reference/#dbg_trace "Documentation for tactic") "foo"` prints `foo` when elaborated. Useful for debugging tactic control flow:
`example : [False](Basic-Propositions/Truth/#False "Documentation for False") ∨ [True](Basic-Propositions/Truth/#True___intro "Documentation for True") := by⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") [True](Basic-Propositions/Truth/#True___intro "Documentation for True")   [first](Tactic-Proofs/The-Tactic-Language/#first "Documentation for tactic")   | [apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") [Or.inl](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or.inl")h⊢ [False](Basic-Propositions/Truth/#False "Documentation for False"); [trivial](Tactic-Proofs/Tactic-Reference/#trivial "Documentation for tactic")h⊢ [False](Basic-Propositions/Truth/#False "Documentation for False"); [dbg_trace](Tactic-Proofs/Tactic-Reference/#dbg_trace "Documentation for tactic") "left"   | [apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") [Or.inr](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or.inr")h⊢ [True](Basic-Propositions/Truth/#True___intro "Documentation for True"); [trivial](Tactic-Proofs/Tactic-Reference/#trivial "Documentation for tactic")All goals completed! 🐙; [dbg_trace](Tactic-Proofs/Tactic-Reference/#dbg_trace "Documentation for tactic") "right" `
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.traceState "Permalink")tactic
```
[trace_state](Tactic-Proofs/Tactic-Reference/#trace_state "Documentation for tactic")
```

`[trace_state](Tactic-Proofs/Tactic-Reference/#trace_state "Documentation for tactic")` displays the current state in the info view.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.traceMessage "Permalink")tactic
```
[trace](Tactic-Proofs/Tactic-Reference/#trace "Documentation for tactic")
```

`trace msg` displays `msg` in the info view.
##  14.5.23. Suggestions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Tactic-Proofs--Tactic-Reference--Suggestions "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=%C2%ABtactic%E2%88%8E%C2%BB "Permalink")tactic
```
[∎](Tactic-Proofs/Tactic-Reference/#___-next "Documentation for tactic")
```

`∎` (typed as `\qed`) is a macro that expands to `try?` in tactic mode.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.suggestions "Permalink")tactic
```
[suggestions](Tactic-Proofs/Tactic-Reference/#suggestions "Documentation for tactic")
```

`#suggestions` will suggest relevant theorems from the library for the current goal, using the currently registered library suggestion engine.
The suggestions are printed in the order of their confidence, from highest to lowest.
##  14.5.24. Other[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-other "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticTrivial "Permalink")tactic
```
[trivial](Tactic-Proofs/Tactic-Reference/#trivial "Documentation for tactic")
```

`trivial` tries different simple tactics (e.g., `[rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")`, `[contradiction](Tactic-Proofs/Tactic-Reference/#contradiction "Documentation for tactic")`, ...) to close the current goal. You can use the command `macro_rules` to extend the set of tactics used. Example:
`[macro_rules](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules "Documentation for syntax") | `(tactic| [trivial](Tactic-Proofs/Tactic-Reference/#trivial "Documentation for tactic")) => `(tactic| [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")) `
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.solveTactic "Permalink")tactic
```
[solve](Tactic-Proofs/Tactic-Reference/#solve "Documentation for tactic")
```

Similar to `[first](Tactic-Proofs/The-Tactic-Language/#first "Documentation for tactic")`, but succeeds only if one the given tactics solves the current goal.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticAnd_intros "Permalink")tactic
```
[and_intros](Tactic-Proofs/Tactic-Reference/#and_intros "Documentation for tactic")
```

`[and_intros](Tactic-Proofs/Tactic-Reference/#and_intros "Documentation for tactic")` applies `[And.intro](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And.intro")` until it does not make progress.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticInfer_instance "Permalink")tactic
```
[infer_instance](Tactic-Proofs/Tactic-Reference/#infer_instance "Documentation for tactic")
```

`[infer_instance](Tactic-Proofs/Tactic-Reference/#infer_instance "Documentation for tactic")` is an abbreviation for `[exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic") inferInstance`. It synthesizes a value of any target type by typeclass inference.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.exposeNames "Permalink")tactic
```
[expose_names](Tactic-Proofs/Tactic-Reference/#expose_names "Documentation for tactic")
```

`[expose_names](Tactic-Proofs/Tactic-Reference/#expose_names "Documentation for tactic")` renames all inaccessible variables with accessible names, making them available for reference in generated tactics. However, this renaming introduces machine-generated names that are not fully under user control. `[expose_names](Tactic-Proofs/Tactic-Reference/#expose_names "Documentation for tactic")` is primarily intended as a preamble for auto-generated end-game tactic scripts. It is also useful as an alternative to `set_option tactic.hygienic false`. If explicit control over renaming is needed in the middle of a tactic script, consider using structured tactic scripts with `match .. with`, `induction .. with`, or `[intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic")` with explicit user-defined names, as well as tactics such as `[next](Tactic-Proofs/The-Tactic-Language/#next "Documentation for tactic")`, `[case](Tactic-Proofs/The-Tactic-Language/#case "Documentation for tactic")`, and `[rename_i](Tactic-Proofs/The-Tactic-Language/#rename_i "Documentation for tactic")`.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.tacticUnhygienic_ "Permalink")tactic
```
[unhygienic](Tactic-Proofs/Tactic-Reference/#unhygienic "Documentation for tactic")
```

`unhygienic tacs` runs `tacs` with name hygiene disabled. This means that tactics that would normally create inaccessible names will instead make regular variables. **Warning** : Tactics may change their variable naming strategies at any time, so code that depends on autogenerated names is brittle. Users should try not to use `unhygienic` if possible.
`example : ∀ x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"), x = x := by⊢ ∀ (x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [unhygienic](Tactic-Proofs/Tactic-Reference/#unhygienic "Documentation for tactic")   [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic")x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x            -- x would normally be intro'd as inaccessible   [exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic") [Eq.refl](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq.refl") xAll goals completed! 🐙  -- refer to x `
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.runTac "Permalink")tactic
```
[run_tac](Tactic-Proofs/Tactic-Reference/#run_tac "Documentation for tactic")
```

The `[run_tac](Tactic-Proofs/Tactic-Reference/#run_tac "Documentation for tactic") doSeq` tactic executes code in `TacticM Unit`.
##  14.5.25. Verification Condition Generation[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-mvcgen "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mvcgenMacro "Permalink")tactic
```
[mvcgen](Tactic-Proofs/Tactic-Reference/#mvcgen "Documentation for tactic")
```

`mvcgen` will break down a Hoare triple proof goal like `⦃P⦄ prog ⦃Q⦄` into verification conditions, provided that all functions used in `prog` have specifications registered with `@[[spec](The--mvcgen--tactic/Predicate-Transformers/#Lean___Parser___Attr___spec "Documentation for syntax")]`.
**Verification Conditions and specifications**
A verification condition is an entailment in the stateful logic of `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` in which the original program `prog` no longer occurs. Verification conditions are introduced by the `mspec` tactic; see the `mspec` tactic for what they look like. When there's no applicable `mspec` spec, `mvcgen` will try and rewrite an application `prog = f a b c` with the simp set registered via `@[[spec](The--mvcgen--tactic/Predicate-Transformers/#Lean___Parser___Attr___spec "Documentation for syntax")]`.
**Features**
When used like `mvcgen +noLetElim [foo_spec, bar_def, instBEqFloat]`, `mvcgen` will additionally
  * add a Hoare triple specification `foo_spec : ... → ⦃P⦄ foo ... ⦃Q⦄` to `[spec](The--mvcgen--tactic/Predicate-Transformers/#Lean___Parser___Attr___spec "Documentation for syntax")` set for a function `foo` occurring in `prog`,
  * unfold a definition `def bar_def ... := ...` in `prog`,
  * unfold any method of the `instBEqFloat : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` instance in `prog`.
  * it will no longer substitute away `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")`-expressions that occur at most once in `P`, `Q` or `prog`.


**Config options**
`+noLetElim` is just one config option of many. Check out `Lean.Elab.Tactic.Do.VCGen.Config` for all options. Of particular note is `stepLimit = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 42`, which is useful for bisecting bugs in `mvcgen` and tracing its execution.
**Extended syntax**
Often, `mvcgen` will be used like this:

```
mvcgen [...]
case inv1 => by exact I1
case inv2 => by exact I2
all_goals (mleave; try grind)

```

There is special syntax for this:

```
mvcgen [...] invariants
· I1
· I2
with grind

```

When `I1` and `I2` need to refer to inaccessibles (`mvcgen` will introduce a lot of them for program variables), you can use case label syntax:

```
mvcgen [...] invariants
| inv1 _ acc _ => I1 acc
| _ => I2
with grind

```

This is more convenient than the equivalent `· by rename_i _ acc _; exact I1 acc`.
**Invariant suggestions**
`mvcgen` will suggest invariants for you if you use the `invariants?` keyword.

```
mvcgen [...] invariants?

```

This is useful if you do not recall the exact syntax to construct invariants. Furthermore, it will suggest a concrete invariant encoding "this holds at the start of the loop and this must hold at the end of the loop" by looking at the corresponding VCs. Although the suggested invariant is a good starting point, it is too strong and requires users to interpolate it such that the inductive step can be proved. Example:

```
def mySum (l : List Nat) : Nat := Id.run do
  let mut acc := 0
  for x in l do
    acc := acc + x
  return acc

/--
info: Try this:
  invariants
    · ⇓⟨xs, letMuts⟩ => ⌜xs.prefix = [] ∧ letMuts = 0 ∨ xs.suffix = [] ∧ letMuts = l.sum⌝
-/
#guard_msgs (info) in
theorem mySum_suggest_invariant (l : List Nat) : mySum l = l.sum := by
  generalize h : mySum l = r
  apply Id.of_wp_run_eq h
  mvcgen invariants?
  all_goals admit

```

###  14.5.25.1. Tactics for Stateful Goals in `Std.Do.SPred`[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-ref-spred "Permalink")
####  14.5.25.1.1. Starting and Stopping the Proof Mode[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Tactic-Proofs--Tactic-Reference--Verification-Condition-Generation--Tactics-for-Stateful-Goals-in--Std___Do___SPred--Starting-and-Stopping-the-Proof-Mode "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mstartMacro "Permalink")tactic
```
[mstart](Tactic-Proofs/Tactic-Reference/#mstart "Documentation for tactic")
```

Start the stateful proof mode of `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`. This will transform a stateful goal of the form `H ⊢ₛ T` into `⊢ₛ H → T` upon which `mintro` can be used to re-introduce `H` and give it a name. It is often more convenient to use `mintro` directly, which will try `mstart` automatically if necessary.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mstopMacro "Permalink")tactic
```
[mstop](Tactic-Proofs/Tactic-Reference/#mstop "Documentation for tactic")
```

Stops the stateful proof mode of `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`. This will simply forget all the names given to stateful hypotheses and pretty-print a bit differently.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mleaveMacro "Permalink")tactic
```
[mleave](Tactic-Proofs/Tactic-Reference/#mleave "Documentation for tactic")
```

Leaves the stateful proof mode of `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")`, tries to eta-expand through all definitions related to the logic of the `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` and gently simplifies the resulting pure Lean proposition. This is often the right thing to do after `mvcgen` in order for automation to prove the goal.
####  14.5.25.1.2. Proving a Stateful Goal[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Tactic-Proofs--Tactic-Reference--Verification-Condition-Generation--Tactics-for-Stateful-Goals-in--Std___Do___SPred--Proving-a-Stateful-Goal "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mspecMacro "Permalink")tactic
```
[mspec](Tactic-Proofs/Tactic-Reference/#mspec "Documentation for tactic")
```

`mspec` is an `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic")`-like tactic that applies a Hoare triple specification to the target of the stateful goal.
Given a stateful goal `H ⊢ₛ wp⟦prog⟧ Q'`, `mspec foo_spec` will instantiate `foo_spec : ... → ⦃P⦄ foo ⦃Q⦄`, match `foo` against `prog` and produce subgoals for the verification conditions `?pre : H ⊢ₛ P` and `?post : Q ⊢ₚ Q'`.
  * If `prog = x >>= f`, then `mspec Specs.bind` is tried first so that `foo` is matched against `x` instead. Tactic `mspec_no_bind` does not attempt to do this decomposition.
  * If `?pre` or `?post` follow by `.[rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")`, then they are discharged automatically.
  * `?post` is automatically simplified into constituent `⊢ₛ` entailments on success and failure continuations.
  * `?pre` and `?post.*` goals introduce their stateful hypothesis under an inaccessible name. You can give it a name with the `mrename_i` tactic.
  * Any uninstantiated MVar arising from instantiation of `foo_spec` becomes a new subgoal.
  * If the target of the stateful goal looks like `fun s => _` then `mspec` will first `mintro ∀s`.
  * If `P` has schematic variables that can be instantiated by doing `mintro ∀s`, for example `foo_spec : ∀(n:Nat), ⦃fun s => ⌜n = s⌝⦄ foo ⦃Q⦄`, then `mspec` will do `mintro ∀s` first to instantiate `n = s`.
  * Right before applying the spec, the `mframe` tactic is used, which has the following effect: Any hypothesis `Hᵢ` in the goal `h₁:H₁, h₂:H₂, ..., hₙ:Hₙ ⊢ₛ T` that is pure (i.e., equivalent to some `⌜φᵢ⌝`) will be moved into the pure context as `hᵢ:φᵢ`.


Additionally, `mspec` can be used without arguments or with a term argument:
  * `mspec` without argument will try and look up a spec for `x` registered with `@[[spec](The--mvcgen--tactic/Predicate-Transformers/#Lean___Parser___Attr___spec "Documentation for syntax")]`.
  * `mspec (foo_spec blah ?bleh)` will elaborate its argument as a term with expected type `⦃?P⦄ x ⦃?Q⦄` and introduce `?bleh` as a subgoal. This is useful to pass an invariant to e.g., `Specs.forIn_list` and leave the inductive step as a hole.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mintroMacro "Permalink")tactic
```
[mintro](Tactic-Proofs/Tactic-Reference/#mintro "Documentation for tactic")
```

Like `[intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic")`, but introducing stateful hypotheses into the stateful context of the `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` proof mode. That is, given a stateful goal `(hᵢ : Hᵢ)* ⊢ₛ P → T`, `mintro h` transforms into `(hᵢ : Hᵢ)*, (h : P) ⊢ₛ T`.
Furthermore, `mintro ∀s` is like `[intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") s`, but preserves the stateful goal. That is, `mintro ∀s` brings the topmost state variable `s:σ` in scope and transforms `(hᵢ : Hᵢ)* ⊢ₛ T` (where the entailment is in `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") (σ::σs)`) into `(hᵢ : Hᵢ s)* ⊢ₛ T s` (where the entailment is in `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred") σs`).
Beyond that, `mintro` supports the full syntax of `mcases` patterns (`mintro pat = (mintro h; mcases h with pat`), and can perform multiple introductions in sequence.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mexactMacro "Permalink")tactic
```
[mexact](Tactic-Proofs/Tactic-Reference/#mexact "Documentation for tactic")
```

`mexact` is like `[exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic")`, but operating on a stateful `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` goal.

```
example (Q : SPred σs) : Q ⊢ₛ Q := by
  mstart
  mintro HQ
  mexact HQ

```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.massumptionMacro "Permalink")tactic
```
[massumption](Tactic-Proofs/Tactic-Reference/#massumption "Documentation for tactic")
```

`massumption` is like `[assumption](Tactic-Proofs/Tactic-Reference/#assumption "Documentation for tactic")`, but operating on a stateful `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` goal.

```
example (P Q : SPred σs) : Q ⊢ₛ P → Q := by
  mintro _ _
  massumption

```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mrefineMacro "Permalink")tactic
```
[mrefine](Tactic-Proofs/Tactic-Reference/#mrefine "Documentation for tactic")
```

Like `[refine](Tactic-Proofs/Tactic-Reference/#refine "Documentation for tactic")`, but operating on stateful `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` goals.

```
example (P Q R : SPred σs) : (P ∧ Q ∧ R) ⊢ₛ P ∧ R := by
  mintro ⟨HP, HQ, HR⟩
  mrefine ⟨HP, HR⟩

example (ψ : Nat → SPred σs) : ψ 42 ⊢ₛ ∃ x, ψ x := by
  mintro H
  mrefine ⟨⌜42⌝, H⟩

```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mconstructorMacro "Permalink")tactic
```
[mconstructor](Tactic-Proofs/Tactic-Reference/#mconstructor "Documentation for tactic")
```

`mconstructor` is like `[constructor](Tactic-Proofs/Tactic-Reference/#constructor "Documentation for tactic")`, but operating on a stateful `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` goal.

```
example (Q : SPred σs) : Q ⊢ₛ Q ∧ Q := by
  mintro HQ
  mconstructor <;> mexact HQ

```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mleftMacro "Permalink")tactic
```
[mleft](Tactic-Proofs/Tactic-Reference/#mleft "Documentation for tactic")
```

`mleft` is like `[left](Tactic-Proofs/Tactic-Reference/#left "Documentation for tactic")`, but operating on a stateful `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` goal.

```
example (P Q : SPred σs) : P ⊢ₛ P ∨ Q := by
  mintro HP
  mleft
  mexact HP

```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mrightMacro "Permalink")tactic
```
[mright](Tactic-Proofs/Tactic-Reference/#mright "Documentation for tactic")
```

`mright` is like `[right](Tactic-Proofs/Tactic-Reference/#right "Documentation for tactic")`, but operating on a stateful `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` goal.

```
example (P Q : SPred σs) : P ⊢ₛ Q ∨ P := by
  mintro HP
  mright
  mexact HP

```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mexistsMacro "Permalink")tactic
```
[mexists](Tactic-Proofs/Tactic-Reference/#mexists "Documentation for tactic")
```

`mexists` is like `[exists](Tactic-Proofs/Tactic-Reference/#exists "Documentation for tactic")`, but operating on a stateful `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` goal.

```
example (ψ : Nat → SPred σs) : ψ 42 ⊢ₛ ∃ x, ψ x := by
  mintro H
  mexists 42

```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mpureIntroMacro "Permalink")tactic
```
[mpure_intro](Tactic-Proofs/Tactic-Reference/#mpure_intro "Documentation for tactic")
```

`mpure_intro` operates on a stateful `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` goal of the form `P ⊢ₛ ⌜φ⌝`. It leaves the stateful proof mode (thereby discarding `P`), leaving the regular goal `φ`.

```
theorem simple : ⊢ₛ (⌜True⌝ : SPred σs) := by
  mpure_intro
  exact True.intro

```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mexfalsoMacro "Permalink")tactic
```
[mexfalso](Tactic-Proofs/Tactic-Reference/#mexfalso "Documentation for tactic")
```

`mexfalso` is like `[exfalso](Tactic-Proofs/Tactic-Reference/#exfalso "Documentation for tactic")`, but operating on a stateful `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` goal.

```
example (P : SPred σs) : ⌜False⌝ ⊢ₛ P := by
  mintro HP
  mexfalso
  mexact HP

```

####  14.5.25.1.3. Manipulating Stateful Hypotheses[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Tactic-Proofs--Tactic-Reference--Verification-Condition-Generation--Tactics-for-Stateful-Goals-in--Std___Do___SPred--Manipulating-Stateful-Hypotheses "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mclearMacro "Permalink")tactic
```
[mclear](Tactic-Proofs/Tactic-Reference/#mclear "Documentation for tactic")
```

`mclear` is like `[clear](Tactic-Proofs/The-Tactic-Language/#clear "Documentation for tactic")`, but operating on a stateful `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` goal.

```
example (P Q : SPred σs) : P ⊢ₛ Q → Q := by
  mintro HP
  mintro HQ
  mclear HP
  mexact HQ

```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mdup "Permalink")tactic
```
[mdup](Tactic-Proofs/Tactic-Reference/#mdup "Documentation for tactic")
```

Duplicate a stateful `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` hypothesis.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mhaveMacro "Permalink")tactic
```
[mhave](Tactic-Proofs/Tactic-Reference/#mhave "Documentation for tactic")
```

`mhave` is like `have`, but operating on a stateful `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` goal.

```
example (P Q : SPred σs) : P ⊢ₛ (P → Q) → Q := by
  mintro HP HPQ
  mhave HQ : Q := by mspecialize HPQ HP; mexact HPQ
  mexact HQ

```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mreplaceMacro "Permalink")tactic
```
[mreplace](Tactic-Proofs/Tactic-Reference/#mreplace "Documentation for tactic")
```

`mreplace` is like `[replace](Tactic-Proofs/Tactic-Reference/#replace "Documentation for tactic")`, but operating on a stateful `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` goal.

```
example (P Q : SPred σs) : P ⊢ₛ (P → Q) → Q := by
  mintro HP HPQ
  mreplace HPQ : Q := by mspecialize HPQ HP; mexact HPQ
  mexact HPQ

```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mspecializeMacro "Permalink")tactic
```
[mspecialize](Tactic-Proofs/Tactic-Reference/#mspecialize "Documentation for tactic")
```

`mspecialize` is like `specialize`, but operating on a stateful `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` goal. It specializes a hypothesis from the stateful context with hypotheses from either the pure or stateful context or pure terms.

```
example (P Q : SPred σs) : P ⊢ₛ (P → Q) → Q := by
  mintro HP HPQ
  mspecialize HPQ HP
  mexact HPQ

example (y : Nat) (P Q : SPred σs) (Ψ : Nat → SPred σs) (hP : ⊢ₛ P) : ⊢ₛ Q → (∀ x, P → Q → Ψ x) → Ψ (y + 1) := by
  mintro HQ HΨ
  mspecialize HΨ (y + 1) hP HQ
  mexact HΨ

```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mspecializePureMacro "Permalink")tactic
```
[mspecialize_pure](Tactic-Proofs/Tactic-Reference/#mspecialize_pure "Documentation for tactic")
```

`mspecialize_pure` is like `mspecialize`, but it specializes a hypothesis from the _pure_ context with hypotheses from either the pure or stateful context or pure terms.

```
example (y : Nat) (P Q : SPred σs) (Ψ : Nat → SPred σs) (hP : ⊢ₛ P) (hΨ : ∀ x, ⊢ₛ P → Q → Ψ x) : ⊢ₛ Q → Ψ (y + 1) := by
  mintro HQ
  mspecialize_pure (hΨ (y + 1)) hP HQ => HΨ
  mexact HΨ

```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mcasesMacro "Permalink")tactic
```
[mcases](Tactic-Proofs/Tactic-Reference/#mcases "Documentation for tactic")
```

Like `[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic")`, but operating on stateful `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` goals. Example: Given a goal `h : (P ∧ (Q ∨ R) ∧ (Q → R)) ⊢ₛ R`, `mcases h with ⟨-, ⟨hq | hr⟩, hqr⟩` will yield two goals: `(hq : Q, hqr : Q → R) ⊢ₛ R` and `(hr : R) ⊢ₛ R`.
That is, `mcases h with pat` has the following semantics, based on `pat`:
  * `pat=□h'` renames `h` to `h'` in the stateful context, regardless of whether `h` is pure
  * `pat=⌜h'⌝` introduces `h' : φ` to the pure local context if `h : ⌜φ⌝` (c.f. `Lean.Elab.Tactic.Do.ProofMode.IsPure`)
  * `pat=h'` is like `pat=⌜h'⌝` if `h` is pure (c.f. `Lean.Elab.Tactic.Do.ProofMode.IsPure`), otherwise it is like `pat=□h'`.
  * `pat=_` renames `h` to an inaccessible name
  * `pat=-` discards `h`
  * `⟨pat₁, pat₂⟩` matches on conjunctions and existential quantifiers and recurses via `pat₁` and `pat₂`.
  * `⟨pat₁ | pat₂⟩` matches on disjunctions, matching the left alternative via `pat₁` and the right alternative via `pat₂`.


[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mrenameIMacro "Permalink")tactic
```
[mrename_i](Tactic-Proofs/Tactic-Reference/#mrename_i "Documentation for tactic")
```

`mrename_i` is like `[rename_i](Tactic-Proofs/The-Tactic-Language/#rename_i "Documentation for tactic")`, but names inaccessible stateful hypotheses in a `[Std.Do.SPred](The--mvcgen--tactic/Predicate-Transformers/#Std___Do___SPred "Documentation for Std.Do.SPred")` goal.
[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mpureMacro "Permalink")tactic
```
[mpure](Tactic-Proofs/Tactic-Reference/#mpure "Documentation for tactic")
```

`mpure` moves a pure hypothesis from the stateful context into the pure context.

```
example (Q : SPred σs) (ψ : φ → ⊢ₛ Q): ⌜φ⌝ ⊢ₛ Q := by
  mintro Hφ
  mpure Hφ
  mexact (ψ Hφ)

```

[🔗](find/?domain=Verso.Genre.Manual.doc.tactic&name=Lean.Parser.Tactic.mframeMacro "Permalink")tactic
```
[mframe](Tactic-Proofs/Tactic-Reference/#mframe "Documentation for tactic")
```

`mframe` infers which hypotheses from the stateful context can be moved into the pure context. This is useful because pure hypotheses "survive" the next application of modus ponens (`Std.Do.SPred.mp`) and transitivity (`Std.Do.SPred.entails.trans`).
It is used as part of the `mspec` tactic.

```
example (P Q : SPred σs) : ⊢ₛ ⌜p⌝ ∧ Q ∧ ⌜q⌝ ∧ ⌜r⌝ ∧ P ∧ ⌜s⌝ ∧ ⌜t⌝ → Q := by
  mintro _
  mframe
  /- `h : p ∧ q ∧ r ∧ s ∧ t` in the pure context -/
  mcases h with hP
  mexact h

```

[←14.4. Options](Tactic-Proofs/Options/#tactic-language-options "14.4. Options")[14.6. Targeted Rewriting with conv→](Tactic-Proofs/Targeted-Rewriting-with--conv/#conv "14.6. Targeted Rewriting with conv")

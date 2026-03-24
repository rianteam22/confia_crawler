[←14.6. Targeted Rewriting with conv](Tactic-Proofs/Targeted-Rewriting-with--conv/#conv "14.6. Targeted Rewriting with conv")[14.8. Custom Tactics→](Tactic-Proofs/Custom-Tactics/#custom-tactics "14.8. Custom Tactics")
#  14.7. Naming Bound Variables[🔗](find/?domain=Verso.Genre.Manual.section&name=bound-variable-name-hints "Permalink")
When the [simplifier](The-Simplifier/#the-simplifier) or the `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")` tactic introduce new binding forms such as function parameters, they select a name for the bound variable based on the one in the statement of the rewrite rule being applied. This name is made unique if necessary. In some situations, such as [preprocessing definitions for termination proofs that use well-founded recursion](Definitions/Recursive-Definitions/#well-founded-preprocessing), the names that appear in termination proof obligations should be the corresponding names written in the original function definition.
The `[binderNameHint](Tactic-Proofs/Naming-Bound-Variables/#binderNameHint "Documentation for binderNameHint")` [gadget](Type-Classes/Class-Declarations/#--tech-term-gadgets) can be used to indicate that a bound variable should be named according to the variables bound in some other term. By convention, the term `()` is used to indicate that a name should _not_ be taken from the original definition.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=binderNameHint "Permalink")def
```


binderNameHint.{u, v, w} {α : Sort u} {β : Sort v} {γ : Sort w} (v : α)
  (binder : β) (e : γ) : γ


binderNameHint.{u, v, w} {α : Sort u}
  {β : Sort v} {γ : Sort w} (v : α)
  (binder : β) (e : γ) : γ


```

The expression `[binderNameHint](Tactic-Proofs/Naming-Bound-Variables/#binderNameHint "Documentation for binderNameHint") v binder e` defined to be `e`.
If it is used on the right-hand side of an equation that is used for rewriting by `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")` or `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`, and `v` is a local variable, and `binder` is an expression that (after beta-reduction) is a binder (`fun w => …` or `∀ w, …`), then it will rename `v` to the name used in that binder, and remove the `[binderNameHint](Tactic-Proofs/Naming-Bound-Variables/#binderNameHint "Documentation for binderNameHint")`.
A typical use of this gadget would be as follows; the gadget ensures that after rewriting, the local variable is still `name`, and not `x`:

```
theorem all_eq_not_any_not (l : List α) (p : α → Bool) :
    l.all p = !l.any fun x => binderNameHint x p (!p x) := sorry

example (names : List String) : names.all (fun name => "Waldo".isPrefixOf name) = true := by
  rw [all_eq_not_any_not]
  -- ⊢ (!names.any fun name => !"Waldo".isPrefixOf name) = true

```

If `binder` is not a binder, then the name of `v` attains a macro scope. This only matters when the resulting term is used in a non-hygienic way, e.g. in termination proofs for well-founded recursion.
This gadget is supported by
  * `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`, `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")` and `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")` in the right-hand-side of an equation
  * `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` in the assumptions of congruence rules


It is ineffective in other positions (hypotheses of rewrite rules) or when used by other tactics (e.g. `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic")`).
[←14.6. Targeted Rewriting with conv](Tactic-Proofs/Targeted-Rewriting-with--conv/#conv "14.6. Targeted Rewriting with conv")[14.8. Custom Tactics→](Tactic-Proofs/Custom-Tactics/#custom-tactics "14.8. Custom Tactics")

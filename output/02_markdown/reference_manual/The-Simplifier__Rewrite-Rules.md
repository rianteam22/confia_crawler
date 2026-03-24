[←15.1. Invoking the Simplifier](The-Simplifier/Invoking-the-Simplifier/#simp-tactic-naming "15.1. Invoking the Simplifier")[15.3. Simp sets→](The-Simplifier/Simp-sets/#simp-sets "15.3. Simp sets")
#  15.2. Rewrite Rules[🔗](find/?domain=Verso.Genre.Manual.section&name=simp-rewrites "Permalink")
The simplifier has three kinds of rewrite rules: 

Declarations to unfold
    
The simplifier will only unfold [reducible](Definitions/Recursive-Definitions/#--tech-term-Reducible) definitions by default. However, a rewrite rule can be added for any [semireducible](Definitions/Recursive-Definitions/#--tech-term-Semireducible) or [irreducible](Definitions/Recursive-Definitions/#--tech-term-Irreducible) definition that causes the simplifier to unfold it as well. When the simplifier is running in definitional mode (`[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")` and its variants), definition unfolding only replaces the defined name with its value; otherwise, it also uses the equational lemmas produced by the equation compiler. 

Equational lemmas
    
The simplifier can treat equality proofs as rewrite rules, in which case the left side of the equality will be replaced with the right. These equational lemmas may have any number of parameters. The simplifier instantiates parameters to make the left side of the equality match the goal, and it performs a proof search to instantiate any additional parameters. 

Simplification procedures
    
The simplifier supports simplification procedures, known as _simprocs_ , that use Lean metaprogramming to perform rewrites that can't be efficiently specified using equations. Lean includes simprocs for the most important operations on built-in types.
Due to [propositional extensionality](The-Type-System/Propositions/#--tech-term-Extensionality), equational lemmas can rewrite propositions to simpler, logically equivalent propositions. When the simplifier rewrites a proof goal to `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")`, it automatically closes it. As a special case of equational lemmas, propositions other than equality can be tagged as rewrite rules They are preprocessed into rules that rewrite the proposition to `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")`.
Rewriting Propositions
When asked to simplify an equality of pairs:
α:Typeβ:Typew:αy:αx:βz:β⊢ [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")w[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") x[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")y[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") z[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")
`[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")α:Typeβ:Typew:αy:αx:βz:β⊢ w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") z` yields a conjunction of equalities:
α:Typeβ:Typew:αy:αx:βz:β⊢ w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") z
The default simp set contains `Prod.mk.injEq`, which shows the equivalence of the two statements:
`Prod.mk.injEq.{u, v} {α : Type u} {β : Type v} (fst : α) (snd : β) :   ∀ (fst_1 : α) (snd_1 : β),     ((fst, snd) = (fst_1, snd_1)) = (fst = fst_1 ∧ snd = snd_1)`
In addition to rewrite rules, `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` has a number of built-in reduction rules, [controlled by the `config` parameter](The-Simplifier/Configuring-Simplification/#simp-config). Even when the simp set is empty, `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` can replace `let`-bound variables with their values, reduce ``Lean.Parser.Term.match : term`
Pattern matching. `match e, ... with | p, ... => f | ...` matches each given term `e` against each pattern `p` of a match alternative. When all patterns of an alternative match, the `match` term evaluates to the value of the corresponding right-hand side `f` with the pattern variables bound to the respective matched values. If used as `match h : e, ... with | p, ... => f | ...`, `h : e = p` is available within `f`.
When not constructing a proof, `match` does not automatically substitute variables matched on in dependent variables' types. Use `match (generalizing := true) ...` to enforce this.
Syntax quotations can also be used in a pattern match. This matches a `Syntax` value against quotations, pattern variables, or `_`.
Quoted identifiers only match identical identifiers - custom matching such as by the preresolved names only should be done explicitly.
`Syntax.atom`s are ignored during matching by default except when part of a built-in literal. For users introducing new atoms, we recommend wrapping them in dedicated syntax kinds if they should participate in matching. For example, in

```
syntax "c" ("foo" <|> "bar") ...

```

`foo` and `bar` are indistinguishable during matching, but in

```
syntax foo := "foo"
syntax "c" (foo <|> "bar") ...

```

they are not.
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match) expressions whose [discriminants](Terms/Pattern-Matching/#--tech-term-match-discriminants) are constructor applications, reduce structure projections applied to constructors, or apply lambdas to their arguments.
[←15.1. Invoking the Simplifier](The-Simplifier/Invoking-the-Simplifier/#simp-tactic-naming "15.1. Invoking the Simplifier")[15.3. Simp sets→](The-Simplifier/Simp-sets/#simp-sets "15.3. Simp sets")

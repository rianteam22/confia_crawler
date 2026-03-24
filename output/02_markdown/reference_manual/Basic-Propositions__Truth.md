[←19. Basic Propositions](Basic-Propositions/#basic-props "19. Basic Propositions")[19.2. Logical Connectives→](Basic-Propositions/Logical-Connectives/#The-Lean-Language-Reference--Basic-Propositions--Logical-Connectives "19.2. Logical Connectives")
#  19.1. Truth[🔗](find/?domain=Verso.Genre.Manual.section&name=true-false "Permalink")
Fundamentally, there are only two propositions in Lean: `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")` and `[False](Basic-Propositions/Truth/#False "Documentation for False")`. The axiom of propositional extensionality (`[propext](The-Type-System/Propositions/#propext "Documentation for propext")`) allows propositions to be considered equal when they are logically equivalent, and every true proposition is logically equivalent to `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")`. Similarly, every false proposition is logically equivalent to `[False](Basic-Propositions/Truth/#False "Documentation for False")`.
`[True](Basic-Propositions/Truth/#True___intro "Documentation for True")` is an inductively defined proposition with a single constructor that takes no parameters. It is always possible to prove `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")`. `[False](Basic-Propositions/Truth/#False "Documentation for False")`, on the other hand, is an inductively defined proposition with no constructors. Proving it requires finding an inconsistency in the current context.
Both `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")` and `[False](Basic-Propositions/Truth/#False "Documentation for False")` are [subsingletons](The-Type-System/Inductive-Types/#subsingleton-elimination); this means that they can be used to compute inhabitants of non-propositional types. For `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")`, this amounts to ignoring the proof, which is not informative. For `[False](Basic-Propositions/Truth/#False "Documentation for False")`, this amounts to a demonstration that the current code is unreachable and does not need to be completed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=True.intro "Permalink")inductive proposition
```


True : Prop


True : Prop


```

`[True](Basic-Propositions/Truth/#True___intro "Documentation for True")` is a proposition and has only an introduction rule, `[True.intro](Basic-Propositions/Truth/#True___intro "Documentation for True.intro") : [True](Basic-Propositions/Truth/#True___intro "Documentation for True")`. In other words, `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")` is simply true, and has a canonical proof, `[True.intro](Basic-Propositions/Truth/#True___intro "Documentation for True.intro")` For more information: [Propositional Logic](https://lean-lang.org/theorem_proving_in_lean4/propositions_and_proofs.html#propositional-logic)
#  Constructors

```
intro : [True](Basic-Propositions/Truth/#True___intro "Documentation for True")
```

`[True](Basic-Propositions/Truth/#True___intro "Documentation for True")` is true, and `[True.intro](Basic-Propositions/Truth/#True___intro "Documentation for True.intro")` (or more commonly, `trivial`) is the proof.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=False "Permalink")inductive proposition
```


False : Prop


False : Prop


```

`[False](Basic-Propositions/Truth/#False "Documentation for False")` is the empty proposition. Thus, it has no introduction rules. It represents a contradiction. `[False](Basic-Propositions/Truth/#False "Documentation for False")` elimination rule, `False.rec`, expresses the fact that anything follows from a contradiction. This rule is sometimes called ex falso (short for ex falso sequitur quodlibet), or the principle of explosion. For more information: [Propositional Logic](https://lean-lang.org/theorem_proving_in_lean4/propositions_and_proofs.html#propositional-logic)
#  Constructors
[🔗](find/?domain=Verso.Genre.Manual.doc&name=False.elim "Permalink")def
```


False.elim.{u} {C : Sort u} (h : [False](Basic-Propositions/Truth/#False "Documentation for False")) : C


False.elim.{u} {C : Sort u} (h : [False](Basic-Propositions/Truth/#False "Documentation for False")) :
  C


```

`[False.elim](Basic-Propositions/Truth/#False___elim "Documentation for False.elim") : [False](Basic-Propositions/Truth/#False "Documentation for False") → C` says that from `[False](Basic-Propositions/Truth/#False "Documentation for False")`, any desired proposition `C` holds. Also known as ex falso quodlibet (EFQ) or the principle of explosion.
The target type is actually `C : Sort u` which means it works for both propositions and types. When executed, this acts like an "unreachable" instruction: it is **undefined behavior** to run, but it will probably print "unreachable code". (You would need to construct a proof of false to run it anyway, which you can only do using `[sorry](Tactic-Proofs/Tactic-Reference/#sorry "Documentation for tactic")` or unsound axioms.)
Dead Code and Subsingleton Elimination
The fourth branch in the definition of `[f](Basic-Propositions/Truth/#f-_LPAR_in-Dead-Code-and-Subsingleton-Elimination_RPAR_ "Definition of example")` is unreachable, so no concrete `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` value needs to be provided:
`def f (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=   [if](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") h1 : n < 11 [then](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax")     "Small"   [else](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") [if](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") h2 : n > 13 [then](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax")     "Large"   [else](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") [if](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") h3 : n % 2 = 1 [then](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax")     "Odd"   [else](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") [if](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") h4 : n ≠ 12 [then](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax")     [False.elim](Basic-Propositions/Truth/#False___elim "Documentation for False.elim") (byn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h1:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 11h2:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")n > 13h3:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")n [%](Type-Classes/Basic-Classes/#HMod___mk "Documentation for HMod.hMod") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1h4:n ≠ 12⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic")All goals completed! 🐙)   [else](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") "Twelve" `
In this example, `[False.elim](Basic-Propositions/Truth/#False___elim "Documentation for False.elim")` indicates to Lean that the current local context is logically inconsistent: proving `[False](Basic-Propositions/Truth/#False "Documentation for False")` suffices to abandon the branch.
Similarly, the definition of `[g](Basic-Propositions/Truth/#g-_LPAR_in-Dead-Code-and-Subsingleton-Elimination_RPAR_ "Definition of example")` appears to have the potential to be non-terminating. However, the recursive call occurs on an unreachable path through the program. The proof automation used for producing termination proofs can detect that the local assumptions are inconsistent.
`def g (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=   [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n < 11 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax")     "Small"   [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n > 13 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax")     "Large"   [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n % 2 = 1 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax")     "Odd"   [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n ≠ 12 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax")     [g](Basic-Propositions/Truth/#g-_LPAR_in-Dead-Code-and-Subsingleton-Elimination_RPAR_ "Definition of example") (n + 1)   [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "Twelve" termination_by n `
[Live ↪](javascript:openLiveLink\("CYUwZgBJAUB2EC4IDkCGAXAlIiBldATgJawDmiAvAFAQRGQAWAjDvADwRMvoMiw20IAIlwBbVABsJQgSAkBnEHUYAmVhAB8nAMwQefAbSEAZVAVIgZtOYuUQGupPACkENRU57e/QcIDywMBWEDZK9PYALOqABkScavo+ggBikooAdHJEohDQAEYAnhAA9qIgpKiYsgpKQgAqAO5yAG6WVFSgkORwOGhYOPjEZJQC4eyc3N6GwmKS0lW2o5o6Xga+JmYWwaF2Lm4QHhOrgkIBQfNhkPCxTPGTvl3wANScldbVwg3NreggBKIkGCIRVgAH0ChBYEA"\))
[←19. Basic Propositions](Basic-Propositions/#basic-props "19. Basic Propositions")[19.2. Logical Connectives→](Basic-Propositions/Logical-Connectives/#The-Lean-Language-Reference--Basic-Propositions--Logical-Connectives "19.2. Logical Connectives")

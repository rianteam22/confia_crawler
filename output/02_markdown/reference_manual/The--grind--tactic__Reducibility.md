[←16.10. Annotating Libraries for grind](The--grind--tactic/Annotating-Libraries-for--grind/#grind-annotation "16.10. Annotating Libraries for grind")[16.12. Bigger Examples→](The--grind--tactic/Bigger-Examples/#grind-bigger-examples "16.12. Bigger Examples")
#  16.11. Reducibility[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--grind--tactic--Reducibility "Permalink")
[Reducible](Definitions/Recursive-Definitions/#--tech-term-Reducible) definitions in terms are eagerly unfolded by `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")`. This enables more efficient definitional equality comparisons and indexing.
Reducibility and Congruence Closure
The definition of `[one](The--grind--tactic/Reducibility/#one-_LPAR_in-Reducibility-and-Congruence-Closure_RPAR_ "Definition of example")` is not [reducible](Definitions/Recursive-Definitions/#--tech-term-Reducible):
`def one := 1 `
This means that `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` does not unfold it:
`example : [one](The--grind--tactic/Reducibility/#one-_LPAR_in-Reducibility-and-Congruence-Closure_RPAR_ "Definition of example") = 1 := by⊢ [one](The--grind--tactic/Reducibility/#one-_LPAR_in-Reducibility-and-Congruence-Closure_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1 ``grind` failed grindh:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[one](The--grind--tactic/Reducibility/#one-_LPAR_in-Reducibility-and-Congruence-Closure_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[one](The--grind--tactic/Reducibility/#one-_LPAR_in-Reducibility-and-Congruence-Closure_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1
 
  * [eqc] False propositions
    * [prop] [one](The--grind--tactic/Reducibility/#one-_LPAR_in-Reducibility-and-Congruence-Closure_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1
 
  * [cutsat] Assignment satisfying linear constraints
    * [assign] [one](The--grind--tactic/Reducibility/#one-_LPAR_in-Reducibility-and-Congruence-Closure_RPAR_ "Definition of example") := 2
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
```
`grind` failed
grindh:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[one](The--grind--tactic/Reducibility/#one-_LPAR_in-Reducibility-and-Congruence-Closure_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[one](The--grind--tactic/Reducibility/#one-_LPAR_in-Reducibility-and-Congruence-Closure_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1


  * [eqc] False propositions
    * [prop] [one](The--grind--tactic/Reducibility/#one-_LPAR_in-Reducibility-and-Congruence-Closure_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1


  * [cutsat] Assignment satisfying linear constraints
    * [assign] [one](The--grind--tactic/Reducibility/#one-_LPAR_in-Reducibility-and-Congruence-Closure_RPAR_ "Definition of example") := 2



```

`[two](The--grind--tactic/Reducibility/#two-_LPAR_in-Reducibility-and-Congruence-Closure_RPAR_ "Definition of example")`, on the other hand, is an abbreviation and thus reducible:
`abbrev two := 2 `
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` unfolds `[two](The--grind--tactic/Reducibility/#two-_LPAR_in-Reducibility-and-Congruence-Closure_RPAR_ "Definition of example")` before adding it to the “whiteboard”, allowing the proof to be completed immediately:
`example : [two](The--grind--tactic/Reducibility/#two-_LPAR_in-Reducibility-and-Congruence-Closure_RPAR_ "Definition of example") = 2 := by⊢ [two](The--grind--tactic/Reducibility/#two-_LPAR_in-Reducibility-and-Congruence-Closure_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 2 [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("CYUwZgBA9gdiEC4C8ECMAodBDARjgTiAG4QAuA7lIigEyYgAeWAtgA4A28CZlEt1EHAE8IAc3wBLGMCA"\))
E-matching patterns also unfold reducible definitions. The patterns generated for theorems about abbreviations are expressed in terms of the unfolded abbreviations. Abbreviations should not generally be recursive; in particular, when using `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")`, recursive abbreviations can result in poor indexing performance and unpredictable patterns.
E-matching and Unfolding Abbreviations
When adding `grind` annotations to theorems, E-matching patterns are generated based on the theorem statement. These patterns determine when the theorem is instantiated. The theorem `[one_eq_1](The--grind--tactic/Reducibility/#one_eq_1-_LPAR_in-E-matching-and-Unfolding-Abbreviations_RPAR_ "Definition of example")` mentions the [semireducible](Definitions/Recursive-Definitions/#--tech-term-Semireducible) definition `[one](The--grind--tactic/Reducibility/#one-_LPAR_in-E-matching-and-Unfolding-Abbreviations_RPAR_ "Definition of example")`, and the resulting pattern is also `[one](The--grind--tactic/Reducibility/#one-_LPAR_in-E-matching-and-Unfolding-Abbreviations_RPAR_ "Definition of example")`:
`def one := 1  @[`[one_eq_1](The--grind--tactic/Reducibility/#one_eq_1-_LPAR_in-E-matching-and-Unfolding-Abbreviations_RPAR_ "Definition of example"): [[one](The--grind--tactic/Reducibility/#one-_LPAR_in-E-matching-and-Unfolding-Abbreviations_RPAR_ "Definition of example")]`[grind?](The--grind--tactic/E___matching/#Lean___Parser___Attr___grind___-next "Documentation for syntax") =] theorem one_eq_1 : [one](The--grind--tactic/Reducibility/#one-_LPAR_in-E-matching-and-Unfolding-Abbreviations_RPAR_ "Definition of example") = 1 := by⊢ [one](The--grind--tactic/Reducibility/#one-_LPAR_in-E-matching-and-Unfolding-Abbreviations_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1 [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 `
```
[one_eq_1](The--grind--tactic/Reducibility/#one_eq_1-_LPAR_in-E-matching-and-Unfolding-Abbreviations_RPAR_ "Definition of example"): [[one](The--grind--tactic/Reducibility/#one-_LPAR_in-E-matching-and-Unfolding-Abbreviations_RPAR_ "Definition of example")]
```

Applying the same annotation to a theorem about the [`reducible`](Definitions/Recursive-Definitions/#--tech-term-Reducible) abbreviation `[two](The--grind--tactic/Reducibility/#two-_LPAR_in-E-matching-and-Unfolding-Abbreviations_RPAR_ "Definition of example")` results in a pattern in which `[two](The--grind--tactic/Reducibility/#two-_LPAR_in-E-matching-and-Unfolding-Abbreviations_RPAR_ "Definition of example")` is unfolded:
`abbrev two := 2  @[`[two_eq_2](The--grind--tactic/Reducibility/#two_eq_2-_LPAR_in-E-matching-and-Unfolding-Abbreviations_RPAR_ "Definition of example"): [[@](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat")[OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[2] `[instOfNatNat 2]]`[grind?](The--grind--tactic/E___matching/#Lean___Parser___Attr___grind___-next "Documentation for syntax") =] theorem two_eq_2: [two](The--grind--tactic/Reducibility/#two-_LPAR_in-E-matching-and-Unfolding-Abbreviations_RPAR_ "Definition of example") = 2 := by⊢ [two](The--grind--tactic/Reducibility/#two-_LPAR_in-E-matching-and-Unfolding-Abbreviations_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 2 [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
```
[two_eq_2](The--grind--tactic/Reducibility/#two_eq_2-_LPAR_in-E-matching-and-Unfolding-Abbreviations_RPAR_ "Definition of example"): [[@](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat")[OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[2] `[instOfNatNat 2]]
```

[Live ↪](javascript:openLiveLink\("CYUwZgBA9gdiEC4C8ECMAodABA2gcwCcBLGYAfgiQF10AXACxCgJAFto4B9EAR09UQd4KAcggAjAJ4QCYADaYAhuPEsAbhFoB3KIhQAmTLkIlylGgyYt22qNz76EmnZQj69E6SdJA"\))
Recursive Abbreviations and `grind`
Using the `grind` attribute to add E-matching patterns for a recursive abbreviation's [equational lemmas](Elaboration-and-Compilation/#--tech-term-equational-lemmas) does not result in useful patterns for recursive abbreviations. The `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind?[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")` attribute on this definition of the Fibonacci function results in three patterns, each corresponding to one of the three possibilities:
`@[`fib.eq_3: [fib (#0 + 2)]``fib.eq_1: [fib `[0]]``fib.eq_2: [fib `[1]]`[grind?](The--grind--tactic/E___matching/#Lean___Parser___Attr___grind___-next "Documentation for syntax")] def fib : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") | 0 => 0 | 1 => 1 | n + 2 => fib n + fib (n + 1) `
```
fib.eq_1: [fib `[0]]
```

```
fib.eq_2: [fib `[1]]
```

```
fib.eq_3: [fib (#0 + 2)]
```

Replacing the definition with an abbreviation results in patterns in which occurrences of the function are unfolded. These patterns are not particularly useful:
`@[`fib.eq_3: [[@](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")[HAdd.hAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHAdd] (fib #0) (fib (#0 + 1))]``fib.eq_1: [[@](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat")[OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[0] `[instOfNatNat 0]]``fib.eq_2: [[@](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat")[OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[1] `[instOfNatNat 1]]`[grind?](The--grind--tactic/E___matching/#Lean___Parser___Attr___grind___-next "Documentation for syntax")] abbrev fib : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") | 0 => 0 | 1 => 1 | n + 2 => fib n + fib (n + 1) `
```
fib.eq_1: [[@](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat")[OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[0] `[instOfNatNat 0]]
```

```
fib.eq_2: [[@](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat")[OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[1] `[instOfNatNat 1]]
```

```
fib.eq_3: [[@](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")[HAdd.hAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHAdd] (fib #0) (fib (#0 + 1))]
```

[←16.10. Annotating Libraries for grind](The--grind--tactic/Annotating-Libraries-for--grind/#grind-annotation "16.10. Annotating Libraries for grind")[16.12. Bigger Examples→](The--grind--tactic/Bigger-Examples/#grind-bigger-examples "16.12. Bigger Examples")

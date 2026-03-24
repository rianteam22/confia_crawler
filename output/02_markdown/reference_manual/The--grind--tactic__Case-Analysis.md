[←16.4. Constraint Propagation](The--grind--tactic/Constraint-Propagation/#grind-propagation "16.4. Constraint Propagation")[16.6. E‑matching→](The--grind--tactic/E___matching/#e-matching "16.6. E‑matching")
#  16.5. Case Analysis[🔗](find/?domain=Verso.Genre.Manual.section&name=grind-split "Permalink")
In addition to congruence closure and constraint propagation, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` performs case analysis. During case analysis, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` considers each possible way that a term could have been built, or each possible value of a particular term, in a manner similar to the `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")` and `[split](Tactic-Proofs/Tactic-Reference/#split "Documentation for tactic")` tactics. This case analysis is not exhaustive: `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` only recursively splits cases up to a configured depth limit, and configuration options and annotations control which terms are candidates for splitting.
##  16.5.1. Selection Heuristics[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--grind--tactic--Case-Analysis--Selection-Heuristics "Permalink")
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` decides which sub‑term to split on by combining three sources of signal: 

Structural flags
    
These configuration flags determine whether `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` performs certain case splits: 

`splitIte` (default `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`)
    
Every ``Lean.Parser.Term.ite```if`-term should be split, as if by the `[split](Tactic-Proofs/Tactic-Reference/#split "Documentation for tactic")` tactic. 

`splitMatch` (default `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`)
    
Every ``Lean.Parser.Term.match : term`
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
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match)-term should be split, as if by the `[split](Tactic-Proofs/Tactic-Reference/#split "Documentation for tactic")` tactic. 

`splitImp` (default `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`)
    
Hypotheses of the form `A → B` whose antecedent `A` is **propositional** are split by considering all possibilities for `A`. Arithmetic antecedents are special‑cased: if `A` is an arithmetic literal (that is, a proposition formed by operators such as `≤`, `=`, `¬`, `[Dvd](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd")`, …) then `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` will split _even when`splitImp := false`_ so the integer solver can propagate facts. 

Global limits
    
The `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` option `splits := n` caps the depth of the search tree. Once a branch performs `n` splits `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` stops splitting further in that branch; if the branch cannot be closed it reports that the split threshold has been reached. 

Manual annotations
    
Inductive predicates or structures may be tagged with the `grind cases` attribute. `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` treats every instance of that predicate as a candidate for splitting.
attributeCase Analysis

```
attr ::= ...
    | 


Marks a theorem or definition for use by the grind tactic.


An optional modifier (e.g. =, →, ←, cases, intro, ext, inj, etc.)
controls how grind uses the declaration:




  * whether it is applied forwards, backwards, or both,


  * whether equalities are used on the left, right, or both sides,


  * whether case-splits, constructors, extensionality, or injectivity are applied,


  * or whether custom instantiation patterns are used.




See the individual modifier docstrings for details.


grind 


The cases modifier marks inductively-defined predicates as suitable for case splitting.


cases
```

The `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")` modifier marks inductively-defined predicates as suitable for case splitting.
attributeEager Case Analysis

```
attr ::= ...
    | 


Marks a theorem or definition for use by the grind tactic.


An optional modifier (e.g. =, →, ←, cases, intro, ext, inj, etc.)
controls how grind uses the declaration:




  * whether it is applied forwards, backwards, or both,


  * whether equalities are used on the left, right, or both sides,


  * whether case-splits, constructors, extensionality, or injectivity are applied,


  * or whether custom instantiation patterns are used.




See the individual modifier docstrings for details.


grind 


The cases eager modifier marks inductively-defined predicates as suitable for case splitting,
and instructs grind to perform it eagerly while preprocessing hypotheses.


cases eager
```

The `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") eager` modifier marks inductively-defined predicates as suitable for case splitting, and instructs `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to perform it eagerly while preprocessing hypotheses.
Splitting Conditional Expressions
In this example, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` proves the theorem by considering both cases for the conditional:
`example (c : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))     (h : ([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") c [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") y) = 0) :     x = 0 ∨ y = 0 := byc:[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:(if c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") then x else y) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
Disabling `splitIte` causes the proof to fail:
`example (c : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))     (h : ([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") c [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") y) = 0) :     x = 0 ∨ y = 0 := byc:[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:(if c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") then x else y) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0   ``grind` failed grindc:[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")x y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:(if c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") then x else y) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0left:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0right:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] (if c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") then x else y) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
 
  * [eqc] False propositions 
    * [prop] x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
    * [prop] y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
 
  * [eqc] Equivalence classes
    * [eqc] others
      * [eqc] {0, if c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") then x else y}
 
  * [cutsat] Assignment satisfying linear constraints 
    * [assign] x := 1
 
    * [assign] y := 2
 
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") -splitIteAll goals completed! 🐙 `
In particular, it cannot make progress after discovering that the conditional expression is equal to `0`:

```
`grind` failed
grindc:[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")x y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:(if c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") then x else y) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0left:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0right:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts

    * [prop] (if c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") then x else y) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0




  * [eqc] False propositions

    * [prop] x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


    * [prop] y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0




  * [eqc] Equivalence classes
    * [eqc] others
      * [eqc] {0, if c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") then x else y}


  * [cutsat] Assignment satisfying linear constraints

    * [assign] x := 1


    * [assign] y := 2





```

Forbidding all case splitting causes the proof to fail for the same reason:
`example (c : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))     (h : ([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") c [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") y) = 0) :     x = 0 ∨ y = 0 := byc:[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:(if c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") then x else y) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0   ``grind` failed grindc:[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")x y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:(if c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") then x else y) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0left:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0right:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] (if c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") then x else y) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
 
  * [eqc] False propositions 
    * [prop] x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
    * [prop] y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
 
  * [eqc] Equivalence classes
    * [eqc] others
      * [eqc] {0, if c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") then x else y}
 
  * [cutsat] Assignment satisfying linear constraints 
    * [assign] x := 1
 
    * [assign] y := 2
 
 
  * [limits] Thresholds reached
    * [limit] maximum number of case-splits has been reached, threshold: `(splits := 0)`
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") (splits := 0)All goals completed! 🐙 `
```
`grind` failed
grindc:[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")x y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:(if c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") then x else y) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0left:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0right:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts

    * [prop] (if c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") then x else y) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0




  * [eqc] False propositions

    * [prop] x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


    * [prop] y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0




  * [eqc] Equivalence classes
    * [eqc] others
      * [eqc] {0, if c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") then x else y}


  * [cutsat] Assignment satisfying linear constraints

    * [assign] x := 1


    * [assign] y := 2




  * [limits] Thresholds reached
    * [limit] maximum number of case-splits has been reached, threshold: `(splits := 0)`



```

Allowing just one split is sufficient:
`example (c : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))     (h : ([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") c [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") y) = 0) :     x = 0 ∨ y = 0 := byc:[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:(if c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") then x else y) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") (splits := 1)All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAKAxvAXPAQge2zAlEiPAJ7rwByYALvgFDyNIAW5iAlgGbyrXPAA7eMWAwAzghKEAvPAAMhNAybFZc+IAoiUvDXpZAIxLKA5gCd2AgCZ06oSLAQpyOPIUTEyGKrWWNErDA5uXn4hEXFJGXlFX2EdeU1tXTQDI0YzC0skMVh2ajE9eABGfCA"\))
Splitting Pattern Matching
Disabling case splitting on pattern matches causes `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to fail in this example:
`example (h : y = [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") x [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") | 0 => 1 | _ => 2) :     y > 0 := byy:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")   match x with   | 0 => 1   | x => 2⊢ y > 0   ``grind` failed grindy x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")   match x with   | 0 => 1   | x => 2h_1:y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")       match x with       | 0 => 1       | x => 2
 
    * [prop] y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
    * [prop] (x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → [False](Basic-Propositions/Truth/#False "Documentation for False")) →       (match x with         | 0 => 1         | x => 2) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")         2
 
 
  * [eqc] True propositions
    * [prop] (x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → [False](Basic-Propositions/Truth/#False "Documentation for False")) →       (match x with         | 0 => 1         | x => 2) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")         2
 
  * [eqc] Equivalence classes 
    * [eqc] {y, 0}
      * [eqc] {match x with     | 0 => 1     | x => 2}
 
    * [eqc] {x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → [False](Basic-Propositions/Truth/#False "Documentation for False"), (fun x_0 => x_0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → [False](Basic-Propositions/Truth/#False "Documentation for False")) x, x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → [False](Basic-Propositions/Truth/#False "Documentation for False")}
 
 
  * [ematch] E-matching patterns 
    * [thm] _example.match_1.congr_eq_1: [_example.match_1 #4 (@Lean.Grind.genPattern `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] #0 #3 `[0]) #2 #1]
 
    * [thm] _example.match_1.congr_eq_2: [_example.match_1 #6 (@Lean.Grind.genPattern `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] #1 #5 #2) #4 #3]
 
 
  * [cutsat] Assignment satisfying linear constraints 
    * [assign] y := 0
 
    * [assign] x := 1
 
    * [assign] match x with     | 0 => 1     | x => 2 := 0
 
 
 [grind] Diagnostics
  * [thm] E-Matching instances
    * [thm] _example.match_1.congr_eq_2 ↦ 1

`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") -splitMatchAll goals completed! 🐙 `
```
`grind` failed
grindy x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
  match x with
  | 0 => 1
  | x => 2h_1:y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts

    * [prop] y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
      match x with
      | 0 => 1
      | x => 2


    * [prop] y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


    * [prop] (x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → [False](Basic-Propositions/Truth/#False "Documentation for False")) →
      (match x with
        | 0 => 1
        | x => 2) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
        2




  * [eqc] True propositions
    * [prop] (x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → [False](Basic-Propositions/Truth/#False "Documentation for False")) →
      (match x with
        | 0 => 1
        | x => 2) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
        2


  * [eqc] Equivalence classes

    * [eqc] {y, 0}
      * [eqc] {match x with
    | 0 => 1
    | x => 2}


    * [eqc] {x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → [False](Basic-Propositions/Truth/#False "Documentation for False"), (fun x_0 => x_0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → [False](Basic-Propositions/Truth/#False "Documentation for False")) x, x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → [False](Basic-Propositions/Truth/#False "Documentation for False")}




  * [ematch] E-matching patterns

    * [thm] _example.match_1.congr_eq_1: [_example.match_1 #4 (@Lean.Grind.genPattern `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] #0 #3 `[0]) #2 #1]


    * [thm] _example.match_1.congr_eq_2: [_example.match_1 #6 (@Lean.Grind.genPattern `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] #1 #5 #2) #4 #3]




  * [cutsat] Assignment satisfying linear constraints

    * [assign] y := 0


    * [assign] x := 1


    * [assign] match x with
    | 0 => 1
    | x => 2 := 0





[grind] Diagnostics
  * [thm] E-Matching instances
    * [thm] _example.match_1.congr_eq_2 ↦ 1


```

Enabling the option causes the proof to succeed:
`example (h : y = [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") x [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") | 0 => 1 | _ => 2) :     y > 0 := byy:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")   match x with   | 0 => 1   | x => 2⊢ y > 0   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAKAFvAXPAnvAvPCYALgMaojwDuAloagD7wAMuAfPAIzwMD6r8ATAEp0AKHjis8NszR4ARpjHwA5gCcqAOwAmQA"\))
Splitting Predicates
`[Not30](The--grind--tactic/Case-Analysis/#Not30-_LPAR_in-Splitting-Predicates_RPAR_ "Definition of example")` is a somewhat verbose way to state that a number is not `30`:
`inductive Not30 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Prop where   | gt : x > 30 → [Not30](The--grind--tactic/Case-Analysis/#Not30-_LPAR_in-Splitting-Predicates_RPAR_ "Definition of example") x   | lt : x < 30 → [Not30](The--grind--tactic/Case-Analysis/#Not30-_LPAR_in-Splitting-Predicates_RPAR_ "Definition of example") x `
By default, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` cannot show that `[Not30](The--grind--tactic/Case-Analysis/#Not30-_LPAR_in-Splitting-Predicates_RPAR_ "Definition of example")` implies that a number is, in fact, not `30`:
`example : [Not30](The--grind--tactic/Case-Analysis/#Not30-_LPAR_in-Splitting-Predicates_RPAR_ "Definition of example") n → n ≠ 30 := byn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [Not30](The--grind--tactic/Case-Analysis/#Not30-_LPAR_in-Splitting-Predicates_RPAR_ "Definition of example") n → n ≠ 30 ``grind` failed grindn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:[Not30](The--grind--tactic/Case-Analysis/#Not30-_LPAR_in-Splitting-Predicates_RPAR_ "Definition of example") nh_1:n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 30⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] [Not30](The--grind--tactic/Case-Analysis/#Not30-_LPAR_in-Splitting-Predicates_RPAR_ "Definition of example") n
 
    * [prop] n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 30
 
 
  * [eqc] True propositions
    * [prop] [Not30](The--grind--tactic/Case-Analysis/#Not30-_LPAR_in-Splitting-Predicates_RPAR_ "Definition of example") n
 
  * [eqc] Equivalence classes
    * [eqc] {n, 30}
 
  * [cutsat] Assignment satisfying linear constraints
    * [assign] n := 30
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
This is because `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` does not consider both cases for `[Not30](The--grind--tactic/Case-Analysis/#Not30-_LPAR_in-Splitting-Predicates_RPAR_ "Definition of example")`

```
`grind` failed
grindn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:[Not30](The--grind--tactic/Case-Analysis/#Not30-_LPAR_in-Splitting-Predicates_RPAR_ "Definition of example") nh_1:n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 30⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts

    * [prop] [Not30](The--grind--tactic/Case-Analysis/#Not30-_LPAR_in-Splitting-Predicates_RPAR_ "Definition of example") n


    * [prop] n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 30




  * [eqc] True propositions
    * [prop] [Not30](The--grind--tactic/Case-Analysis/#Not30-_LPAR_in-Splitting-Predicates_RPAR_ "Definition of example") n


  * [eqc] Equivalence classes
    * [eqc] {n, 30}


  * [cutsat] Assignment satisfying linear constraints
    * [assign] n := 30



```

Adding the `grind cases` attribute to `[Not30](The--grind--tactic/Case-Analysis/#Not30-_LPAR_in-Splitting-Predicates_RPAR_ "Definition of example")` allows the proof to succeed:
`[attribute](Attributes/#Lean___Parser___Command___attribute "Documentation for syntax") [grind cases] [Not30](The--grind--tactic/Case-Analysis/#Not30-_LPAR_in-Splitting-Predicates_RPAR_ "Definition of example")  example : [Not30](The--grind--tactic/Case-Analysis/#Not30-_LPAR_in-Splitting-Predicates_RPAR_ "Definition of example") n → n ≠ 30 := byn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [Not30](The--grind--tactic/Case-Analysis/#Not30-_LPAR_in-Splitting-Predicates_RPAR_ "Definition of example") n → n ≠ 30 [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
Similarly, the `grind cases` attribute on `[Even](Introduction/#Even___zero-next "Documentation for Even")` allows `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to perform case splits:
`@[grind cases] inductive Even : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Prop   | zero : [Even](Introduction/#Even___zero-next "Documentation for Even") 0   | step : [Even](Introduction/#Even___zero-next "Documentation for Even") n → [Even](Introduction/#Even___zero-next "Documentation for Even") (n + 2)  [attribute](Attributes/#Lean___Parser___Command___attribute "Documentation for syntax") [grind cases] [Even](Introduction/#Even___zero-next "Documentation for Even")  example (h : [Even](Introduction/#Even___zero-next "Documentation for Even") 5) : [False](Basic-Propositions/Truth/#False "Documentation for False") := byh:[Even](Introduction/#Even___zero-next "Documentation for Even") 5⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  set_option [trace.grind.split](The--grind--tactic/Case-Analysis/#trace___grind___split "Documentation for option trace.grind.split") true [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") example (h : [Even](Introduction/#Even___zero-next "Documentation for Even") (n + 2)) : [Even](Introduction/#Even___zero-next "Documentation for Even") n := byn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:[Even](Introduction/#Even___zero-next "Documentation for Even") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")⊢ [Even](Introduction/#Even___zero-next "Documentation for Even") n   `[grind.split] [Even](Introduction/#Even___zero-next "Documentation for Even") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd"), generation: 0`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABAOQPYwMwAZkC40BDGZQJMJkAFAJ3QAdkB3AC0WsQChlkAfZAc1KEAHsgB8yXOTSYpwrr2QAbIclEAeSXgoZseeRxIxqwAEYQYKANr8T4ZFCIBnRE4C6MvRw6JhRALZ0SiiEulIg0hGABkRaBAC8yKYAngJ2YN4AAjZpDs6ubhygkLAIKACiSBGhJNI09Ap8AF5s6ATIFYgROA3ITpYMhB0RERRDyAAUEQDUyABMAJTeRibmlsjZRbku7u2V3r4BQSjjzG1jAKzzbQBiREou8YlJCrZF3i4wAPr0cOgRxkQoIgAHSvcDApxBYCkYwQFCgHx+QLBCanQaVCbTObzK7ozrIKoJZIvNJAA"\))
##  16.5.2. Performance[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--grind--tactic--Case-Analysis--Performance "Permalink")
Case analysis is powerful, but computationally expensive: each level of case splitting multiplies the search space. It's important to be judicious and not perform unnecessary splits. In particular:
  * Increase `splits` **only** when the goal genuinely needs deeper branching; each extra level multiplies the search space.
  * Disable `splitMatch` when large pattern‑matching definitions explode the tree; this can be observed by setting the `[trace.grind.split](The--grind--tactic/Case-Analysis/#trace___grind___split "Documentation for option trace.grind.split")`.
  * Flags can be combined, e.g. `by grind -splitMatch (splits := 10) +splitImp`.
  * The `grind cases` attribute is [_scoped_](Attributes/#scoped-attributes). The modifiers ``Lean.Parser.Term.attrKind`
`attrKind` matches `("scoped" <|> "local")?`, used before an attribute like `@[local simp]`. 
``local` and ``Lean.Parser.Term.attrKind`
`attrKind` matches `("scoped" <|> "local")?`, used before an attribute like `@[local simp]`. 
``scoped` restrict extra splitting to a section or namespace.


[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=trace.grind.split "Permalink")option
```
trace.grind.split
```

Default value: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
enable/disable tracing for the given module and submodules
[←16.4. Constraint Propagation](The--grind--tactic/Constraint-Propagation/#grind-propagation "16.4. Constraint Propagation")[16.6. E‑matching→](The--grind--tactic/E___matching/#e-matching "16.6. E‑matching")

[←16.6. E‑matching](The--grind--tactic/E___matching/#e-matching "16.6. E‑matching")[16.8. Algebraic Solver (Commutative Rings, Fields)→](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#grind-ring "16.8. Algebraic Solver \(Commutative Rings, Fields\)")
#  16.7. Linear Integer Arithmetic[🔗](find/?domain=Verso.Genre.Manual.section&name=cutsat "Permalink")
The linear integer arithmetic solver implements a model-based decision procedure for linear integer arithmetic. The solver can process four categories of linear polynomial constraints (where `p` is a [linear polynomial](https://en.wikipedia.org/wiki/Degree_of_a_polynomial)): 

Equality
    
`p = 0` 

Divisibility
    
`d ∣ p` 

Inequality
    
`p ≤ 0` 

Disequality
    
`p ≠ 0`
It is complete for linear integer arithmetic, and natural numbers are supported by converting them to integers with `[Int.ofNat](Basic-Types/Integers/#Int___ofNat "Documentation for Int.ofNat")`. Support for additional types that can be embedded into `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` can be added via instances of `[Lean.Grind.ToInt](The--grind--tactic/Linear-Integer-Arithmetic/#Lean___Grind___ToInt___mk "Documentation for Lean.Grind.ToInt")`. Nonlinear terms (e.g. `x * x`) are allowed, and are represented as variables. The solver is additionally capable of propagating information back to the metaphorical `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` whiteboard, which can trigger further progress from the other subsystems. By default, it is enabled; it can be disabled using the flag `-lia`
Examples of Linear Integer Arithmetic
All of these statements can be proved using the linear integer arithmetic solver. In the first example, the left-hand side must be a multiple of 2, and thus cannot be 5:
`example {x y : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")} : 2 * x + 4 * y ≠ 5 := byx:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")y:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 4 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y ≠ 5   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
The solver supports mixing equalities and inequalities:
`example {x y : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")} :     2 * x + 3 * y = 0 →     1 ≤ x →     y < 1 := byx:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")y:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 3 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") x → y [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 1   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
It also supports linear divisibility constraints:
`example (a b : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) :     2 ∣ a + 1 →     2 ∣ b + a →     ¬ 2 ∣ b + 2 * a := bya:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")b:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ 2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 → 2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a → [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
Without `lia`, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` cannot prove the statement:
`example (a b : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) :     2 ∣ a + 1 →     2 ∣ b + a →     ¬ 2 ∣ b + 2 * a := bya:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")b:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ 2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 → 2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a → [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a   ``grind` failed grinda b:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")h:2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1h_1:2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") bh_2:2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] 2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1
 
    * [prop] 2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b
 
    * [prop] 2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b
 
 
  * [eqc] True propositions 
    * [prop] 2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b
 
    * [prop] 2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1
 
    * [prop] 2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b
 
 
  * [ematch] E-matching patterns 
    * [thm] Nat.dvd_mul_left_of_dvd: [[@](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd")[Dvd.dvd](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[Nat.instDvd] #3 #2, [@](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")[HMul.hMul](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHMul] #0 #2]
 
    * [thm] Nat.dvd_mul_right_of_dvd: [[@](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd")[Dvd.dvd](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[Nat.instDvd] #3 #2, [@](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")[HMul.hMul](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHMul] #2 #0]
 
 
  * [linarith] Linarith assignment for `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` 
    * [assign] a := 0
 
    * [assign] b := 0
 
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") -liaAll goals completed! 🐙 `
```
`grind` failed
grinda b:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")h:2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1h_1:2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") bh_2:2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts

    * [prop] 2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1


    * [prop] 2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b


    * [prop] 2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b




  * [eqc] True propositions

    * [prop] 2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b


    * [prop] 2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1


    * [prop] 2 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b




  * [ematch] E-matching patterns

    * [thm] Nat.dvd_mul_left_of_dvd: [[@](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd")[Dvd.dvd](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[Nat.instDvd] #3 #2, [@](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")[HMul.hMul](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHMul] #0 #2]


    * [thm] Nat.dvd_mul_right_of_dvd: [[@](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd")[Dvd.dvd](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[Nat.instDvd] #3 #2, [@](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")[HMul.hMul](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHMul] #2 #0]




  * [linarith] Linarith assignment for `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`

    * [assign] a := 0


    * [assign] b := 0





```

[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEBvE8Ce8Bc8CSA7ALgL6bwBM8AVPCgNTwAsla8gBkTwCsmAvPAEaoAoePADmAJwCWuACYCBoSLATJmWPEUxDhZJrXgBmJuh4AGeICTCLcICM8QCZE1C1eYAeeLYw9+W8VNnzwaDh4AAowPhJ1AEpNbR1AYiJ4cLpbSzjyRN54OnC07QAahIi6cipwzz5BYV8ZIA"\))
##  16.7.1. Rational Solutions[🔗](find/?domain=Verso.Genre.Manual.section&name=cutsat-qlia "Permalink")
The solver is complete for linear integer arithmetic. However, the search can become vast with very few constraints, but the solver was not designed to perform massive case-analysis. The `qlia` option to `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` reduces the search space by instructing the solver to accept rational solutions. With this option, the solver is likely to be faster, but it is incomplete.
Rational Solutions
The following example has a rational solution, but does not have integer solutions:
`example {x y : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")} :     27 ≤ 13 * x + 11 * y →     13 * x + 11 * y ≤ 30 →     -10 ≤ 9 * x - 7 * y →     9 * x - 7 * y > 4 := byx:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")y:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ 27 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 13 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 11 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y → 13 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 11 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 30 → -10 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 9 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 7 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y → 9 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 7 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y > 4   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
Because it uses the rational solution, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` fails to refute the negation of the goal when `+qlia` is specified:
`example {x y : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")} :     27 ≤ 13 * x + 11 * y →     13 * x + 11 * y ≤ 30 →     -10 ≤ 9 * x - 7 * y →     9 * x - 7 * y > 4 := byx:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")y:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ 27 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 13 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 11 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y → 13 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 11 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 30 → -10 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 9 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 7 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y → 9 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 7 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y > 4   ``grind` failed grindx y:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")h:-13 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -11 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 27 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0h_1:13 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 11 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -30 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0h_2:-9 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 7 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -10 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0h_3:9 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -7 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -4 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] -13 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -11 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 27 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
    * [prop] 13 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 11 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -30 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
    * [prop] -9 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 7 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -10 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
    * [prop] 9 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -7 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -4 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
 
  * [eqc] True propositions 
    * [prop] -9 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 7 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -10 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
    * [prop] -13 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -11 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 27 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
    * [prop] 9 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -7 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -4 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
    * [prop] 13 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 11 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -30 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
 
  * [cutsat] Assignment satisfying linear constraints 
    * [assign] x := 62/117
 
    * [assign] y := 2
 
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") +qliaAll goals completed! 🐙 `
```
`grind` failed
grindx y:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")h:-13 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -11 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 27 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0h_1:13 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 11 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -30 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0h_2:-9 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 7 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -10 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0h_3:9 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -7 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -4 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts

    * [prop] -13 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -11 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 27 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0


    * [prop] 13 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 11 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -30 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0


    * [prop] -9 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 7 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -10 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0


    * [prop] 9 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -7 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -4 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0




  * [eqc] True propositions

    * [prop] -9 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 7 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -10 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0


    * [prop] -13 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -11 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 27 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0


    * [prop] 9 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -7 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -4 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0


    * [prop] 13 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 11 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -30 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0




  * [cutsat] Assignment satisfying linear constraints

    * [assign] x := 62/117


    * [assign] y := 2





```

The rational model constructed by the solver is in the section `Assignment satisfying linear constraints` in the goal diagnostics.
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEBvE8Ce8Bc8CSA7ALgL6YBQ858ATAOzyAmRPAIwDM8AVPCgNROPtrxASYRkKLft1790DZgAYhI8gFpG8hgE5x8JfFod0wivE0cUOvQIB88ACyYAvPABGqEQHMATgEtcAEyA"\))
##  16.7.2. Nonlinear Constraints[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--grind--tactic--Linear-Integer-Arithmetic--Nonlinear-Constraints "Permalink")
The solver currently does support nonlinear constraints, and treats nonlinear terms such as `x * x` as variables.
Nonlinear Terms
The linear integer arithmetic solver fails to prove this theorem:
`example (x : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : x * x ≥ 0 := byx:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x ≥ 0   ``grind` failed grindx:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")h:x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts
    * [prop] x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
  * [eqc] True propositions
    * [prop] x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
  * [ematch] E-matching patterns 
    * [thm] Nat.pow_pos: [[@](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")[HPow.hPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHPow] #2 #1]
 
    * [thm] Nat.div_pow_of_pos: [[@](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")[HPow.hPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHPow] #2 #1]
 
 
  * [cutsat] Assignment satisfying linear constraints 
    * [assign] x := 0
 
    * [assign] 「x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2」 := -1
 
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
```
`grind` failed
grindx:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")h:x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts
    * [prop] x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0


  * [eqc] True propositions
    * [prop] x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0


  * [ematch] E-matching patterns

    * [thm] Nat.pow_pos: [[@](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")[HPow.hPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHPow] #2 #1]


    * [thm] Nat.div_pow_of_pos: [[@](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")[HPow.hPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHPow] #2 #1]




  * [cutsat] Assignment satisfying linear constraints

    * [assign] x := 0


    * [assign] 「x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2」 := -1





```

From the perspective of the linear integer arithmetic solver, it is equivalent to:
`example {y : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")} (x : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : y ≥ 0 := byy:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")x:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ y ≥ 0   ``grind` failed grindy x:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")h:y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts
    * [prop] y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
  * [eqc] True propositions
    * [prop] y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
  * [cutsat] Assignment satisfying linear constraints 
    * [assign] y := -1
 
    * [assign] x := 2
 
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
```
`grind` failed
grindx:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")h:x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts
    * [prop] x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0


  * [eqc] True propositions
    * [prop] x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0


  * [ematch] E-matching patterns

    * [thm] Nat.pow_pos: [[@](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")[HPow.hPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHPow] #2 #1]


    * [thm] Nat.div_pow_of_pos: [[@](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")[HPow.hPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHPow] #2 #1]




  * [cutsat] Assignment satisfying linear constraints

    * [assign] x := 0


    * [assign] 「x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2」 := -1





```

This can be seen by setting the option `trace.grind.lia.assert` to `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, which traces all constraints processed by the solver.
`example (x : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : x*x ≥ 0 := byx:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x ≥ 0   [set_option](Tactic-Proofs/The-Tactic-Language/#set_option "Documentation for tactic") trace.grind.lia.assert [true](Tactic-Proofs/The-Tactic-Language/#set_option "Documentation for tactic") [in](Tactic-Proofs/The-Tactic-Language/#set_option "Documentation for tactic")   `[grind.lia.assert] -1*「x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1」 + 「x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2」 + 1 = 0[grind.lia.assert] 「x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2」 + 1 ≤ 0```grind` failed grindx:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")h:x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts
    * [prop] x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
  * [eqc] True propositions
    * [prop] x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
  * [ematch] E-matching patterns 
    * [thm] Nat.pow_pos: [[@](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")[HPow.hPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHPow] #2 #1]
 
    * [thm] Nat.div_pow_of_pos: [[@](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow")[HPow.hPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[instHPow] #2 #1]
 
 
  * [cutsat] Assignment satisfying linear constraints 
    * [assign] x := 0
 
    * [assign] 「x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2」 := -1
 
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
```
[grind.lia.assert] -1*「x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1」 + 「x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2」 + 1 = 0[grind.lia.assert] 「x [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2」 + 1 ≤ 0
```

The term `x ^ 2` is “quoted” in `「x ^ 2」 + 1 ≤ 0` to indicate that `x ^ 2` is treated as a variable.
##  16.7.3. Division and Modulus[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--grind--tactic--Linear-Integer-Arithmetic--Division-and-Modulus "Permalink")
The solver supports linear division and modulo operations.
Linear Division and Modulo
`example (x y : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) :     x = y / 2 →     y % 2 = 0 →     y - 2 * x = 0 := byx:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")y:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y [/](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv.hDiv") 2 → y [%](Type-Classes/Basic-Classes/#HMod___mk "Documentation for HMod.hMod") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → y [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 2 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAKE8Ce8Bc8CSA7ALgJSYBQ858KAvGvAPTwBM8gSYRkXoCkT8NADK3bl0AWh4AqSr3gCMNAEap2AcwBOAS1wATIA"\))
##  16.7.4. Algebraic Processing[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--grind--tactic--Linear-Integer-Arithmetic--Algebraic-Processing "Permalink")
The solver normalizes commutative (semi)ring expressions.
Commutative (Semi)ring Normalization
Commutative ring normalization allows this goal to be solved:
`example (a b : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))     (h₁ : a + 1 ≠ a * b * a)     (h₂ : a * a * b ≤ a + 1) :     b * a ^ 2 < a + 1 := bya:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")b:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h₁:a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 ≠ a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") ah₂:a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") b [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1⊢ b [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") a [^](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.hPow") 2 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAKM8BG8Bc8ByYAuAlAFDylIAWggQSbwoDU8AjPIAZEt8AVGp7cWRYCCCGii4jugEyJ2DRgUwky6UfAB68AEzwAPFKaYAvGgCe8gOYAnAJYA7ACZA"\))
##  16.7.5. Propagating Information[🔗](find/?domain=Verso.Genre.Manual.section&name=cutsat-mbtc "Permalink")
The solver also implements _model-based theory combination_ , which is a mechanism for propagating equalities back to the metaphorical shared whiteboard. These additional equalities may in turn trigger new congruences. Model-based theory combination increases the size of the search space; it can be disabled using the option `grind -mbtc`.
Propagating Equalities
In the example above, the linear inequalities and disequalities imply `y = 0`:
`example (f : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) (x y : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) :     f x = 0 →     0 ≤ y → y ≤ 1 → y ≠ 1 →     f (x + y) = 0 := byf:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")x:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")y:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ f x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → 0 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") y → y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 1 → y ≠ 1 → f [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
Consequently `x = x + y`, so `f x = f (x + y)` by [congruence](The--grind--tactic/Congruence-Closure/#--tech-term-Congruence-closure). Without model-based theory combination, the proof gets stuck:
`example (f : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) (x y : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) :     f x = 0 →     0 ≤ y → y ≤ 1 → y ≠ 1 →     f (x + y) = 0 := byf:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")x:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")y:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ f x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → 0 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") y → y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 1 → y ≠ 1 → f [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0   ``grind` failed grindf:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")x y:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")h:f x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0h_1:-1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0h_2:y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0h_3:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1h_4:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")f [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] f x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
    * [prop] -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
    * [prop] y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1
 
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")f [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
 
  * [eqc] True propositions 
    * [prop] y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
    * [prop] -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
 
  * [eqc] False propositions 
    * [prop] y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1
 
    * [prop] f [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
 
  * [eqc] Equivalence classes
    * [eqc] {f x, 0}
 
  * [cutsat] Assignment satisfying linear constraints 
    * [assign] x := 0
 
    * [assign] y := 0
 
    * [assign] f x := 0
 
    * [assign] f [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") := 4
 
 
  * [ring] Ring `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`
    * [diseqs] Disequalities
      * [_] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") -mbtcAll goals completed! 🐙 `
```
`grind` failed
grindf:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")x y:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")h:f x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0h_1:-1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0h_2:y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0h_3:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1h_4:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")f [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts

    * [prop] f x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


    * [prop] -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0


    * [prop] y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0


    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1


    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")f [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0




  * [eqc] True propositions

    * [prop] y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0


    * [prop] -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0




  * [eqc] False propositions

    * [prop] y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 1


    * [prop] f [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0




  * [eqc] Equivalence classes
    * [eqc] {f x, 0}


  * [cutsat] Assignment satisfying linear constraints

    * [assign] x := 0


    * [assign] y := 0


    * [assign] f x := 0


    * [assign] f [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") := 4




  * [ring] Ring `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`
    * [diseqs] Disequalities
      * [_] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0



```

[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAKAZvAXPAkgOwC70CTCLPASiRHgE91jcy0AoeZ+VCgXngAZCmWfAJkRVCwoQEYR1QAZE8CQT7NUiCgGoqZTjzScARpT4BzAE4BLbABMgA"\))
##  16.7.6. Other Types[🔗](find/?domain=Verso.Genre.Manual.section&name=cutsat-ToInt "Permalink")
The LIA solver can also process linear constraints that contain natural numbers. It converts them into integer constraints using `Int.ofNat`.
Natural Numbers as Linear Integer Arithmetic
`example (x y z : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :     x < y + z →     y + 1 < z →     z + x < 3 * z := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")z:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") z → y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") z → z [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 3 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") z   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAKE8Ce8Be8Bc8ByYALgJQ4BQ8l8KAPGvANSbyBJhBVekwIzx1ZtVmTWvADM8AFTNsAXngAjVOwDmAJwCWAOwAmQA"\))
There is an extensible mechanism via the `[Lean.Grind.ToInt](The--grind--tactic/Linear-Integer-Arithmetic/#Lean___Grind___ToInt___mk "Documentation for Lean.Grind.ToInt")` type class to tell the solver that a type embeds in the integers. Using this, we can solve goals such as:
`example (a b c : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 11) : a ≤ 2 → b ≤ 3 → c = a + b → c ≤ 5 := bya:[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 11b:[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 11c:[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 11⊢ a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 2 → b [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 3 → c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b → c [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 5   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  example (a : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 2) : a ≠ 0 → a ≠ 1 → [False](Basic-Propositions/Truth/#False "Documentation for False") := bya:[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 2⊢ a ≠ 0 → a ≠ 1 → [False](Basic-Propositions/Truth/#False "Documentation for False")   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  example (a b c : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : a ≤ 2 → b ≤ 3 → c - a - b = 0 → c ≤ 5 := bya:[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")b:[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")c:[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")⊢ a [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 2 → b [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 3 → c [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") a [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 → c [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 5   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Grind.ToInt.toInt_inj "Permalink")type class
```


Lean.Grind.ToInt.{u} (α : Type u)
  (range : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") [Lean.Grind.IntInterval](The--grind--tactic/Linear-Integer-Arithmetic/#Lean___Grind___IntInterval___co "Documentation for Lean.Grind.IntInterval")) : Type u


Lean.Grind.ToInt.{u} (α : Type u)
  (range :
    [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") [Lean.Grind.IntInterval](The--grind--tactic/Linear-Integer-Arithmetic/#Lean___Grind___IntInterval___co "Documentation for Lean.Grind.IntInterval")) :
  Type u


```

`ToInt α I` asserts that `α` can be embedded faithfully into an interval `I` in the integers.
#  Instance Constructor

```
[Lean.Grind.ToInt.mk](The--grind--tactic/Linear-Integer-Arithmetic/#Lean___Grind___ToInt___mk "Documentation for Lean.Grind.ToInt.mk").{u}
```

#  Methods

```
toInt : α → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")
```

The embedding function.

```
toInt_inj : ∀ (x y : α), [↑](The--grind--tactic/Linear-Integer-Arithmetic/#Lean___Grind___ToInt___mk "Documentation for Lean.Grind.ToInt.toInt")x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [↑](The--grind--tactic/Linear-Integer-Arithmetic/#Lean___Grind___ToInt___mk "Documentation for Lean.Grind.ToInt.toInt")y → x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y
```

The embedding function is injective.

```
toInt_mem : ∀ (x : α), [↑](The--grind--tactic/Linear-Integer-Arithmetic/#Lean___Grind___ToInt___mk "Documentation for Lean.Grind.ToInt.toInt")x ∈ range
```

The embedding function lands in the interval.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Grind.IntInterval.co "Permalink")inductive type
```


Lean.Grind.IntInterval : Type


Lean.Grind.IntInterval : Type


```

An interval in the integers (either finite, half-infinite, or infinite).
#  Constructors

```
co (lo hi : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Lean.Grind.IntInterval](The--grind--tactic/Linear-Integer-Arithmetic/#Lean___Grind___IntInterval___co "Documentation for Lean.Grind.IntInterval")
```

The finite interval `[lo, hi)`.

```
ci (lo : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Lean.Grind.IntInterval](The--grind--tactic/Linear-Integer-Arithmetic/#Lean___Grind___IntInterval___co "Documentation for Lean.Grind.IntInterval")
```

The half-infinite interval `[lo, ∞)`.

```
io (hi : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Lean.Grind.IntInterval](The--grind--tactic/Linear-Integer-Arithmetic/#Lean___Grind___IntInterval___co "Documentation for Lean.Grind.IntInterval")
```

The half-infinite interval `(-∞, hi)`.

```
ii : [Lean.Grind.IntInterval](The--grind--tactic/Linear-Integer-Arithmetic/#Lean___Grind___IntInterval___co "Documentation for Lean.Grind.IntInterval")
```

The infinite interval `(-∞, ∞)`.
##  16.7.7. Implementation Notes[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--grind--tactic--Linear-Integer-Arithmetic--Implementation-Notes "Permalink")
The implementation of the linear integer arithmetic solver is inspired by Section 4 of Jovanović and de Moura (2023)Dejan Jovanović and Leonardo de Moura, 2023. [“Cutting to the Chase: Solving Linear Integer Arithmetic”](https://link.springer.com/chapter/10.1007/978-3-642-22438-6_26). In  _Automated Deduction: CADE '23._ (LNCS 6803). Compared to the paper, it includes several enhancements and modifications such as:
  * extended constraint support (equality and disequality),
  * an optimized encoding of the `Cooper-Left` rule using a “big”-disjunction instead of fresh variables, and
  * decision variable tracking for case splits (disequalities, `Cooper-Left`, `Cooper-Right`).


The solver procedure builds a model (that is, an assignment of the variables in the term) incrementally, resolving conflicts through constraint generation. For example, given a partial model `{x := 1}` and constraint `3 ∣ 3 * y + x + 1`:
  * The solver cannot extend the model to `y` because `3 ∣ 3 * y + 2` is unsatisfiable.
  * Thus, it resolves the conflict by generating the implied constraint `3 ∣ x + 1`.
  * The new constraint forces the solver to find a new assignment for `x`.


When assigning a variable `y`, the solver considers:
  * The best upper and lower bounds (inequalities).
  * A divisibility constraint.
  * All disequality constraints where `y` is the maximal variable.


The `Cooper-Left` and `Cooper-Right` rules handle the combination of inequalities and divisibility. For unsatisfiable disequalities `p ≠ 0`, the solver generates the case split: `p + 1 ≤ 0 ∨ -p + 1 ≤ 0`.
[←16.6. E‑matching](The--grind--tactic/E___matching/#e-matching "16.6. E‑matching")[16.8. Algebraic Solver (Commutative Rings, Fields)→](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#grind-ring "16.8. Algebraic Solver \(Commutative Rings, Fields\)")

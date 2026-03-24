[←16.3. Congruence Closure](The--grind--tactic/Congruence-Closure/#congruence-closure "16.3. Congruence Closure")[16.5. Case Analysis→](The--grind--tactic/Case-Analysis/#grind-split "16.5. Case Analysis")
#  16.4. Constraint Propagation[🔗](find/?domain=Verso.Genre.Manual.section&name=grind-propagation "Permalink")
Constraint propagation works on the `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")` and `[False](Basic-Propositions/Truth/#False "Documentation for False")` buckets of the whiteboard. Whenever a term is added to one of those buckets, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` fires dozens of small _forward rules_ that derive further information from its logical consequences: 

Boolean connectives
    
The truth tables of the Boolean connectives can be used to derive further true and false facts. For example:
  * If `A` is `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")`, then `A ∨ B` becomes `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")`.
  * If `A ∧ B` is `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")`, then both `A` and `B` become `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")`.
  * If `A ∧ B` is `[False](Basic-Propositions/Truth/#False "Documentation for False")`, at least one of `A`, `B` becomes `[False](Basic-Propositions/Truth/#False "Documentation for False")`.



Inductive Types
    
If terms formed by applications of two different constructors of the same [inductive type](The-Type-System/Inductive-Types/#--tech-term-Inductive-types) (e.g. `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` and `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")`) are placed in the same equivalence class, a contradiction is derived. If two terms formed by applications of the same constructor are placed in the same equivalence class, then their arguments are also made equal. 

Projections
    
From `h : (x, y) = (x', y')` we derive `x = x'` and `y = y'`. 

Casts
    
Any term `[cast](Basic-Propositions/Propositional-Equality/#cast "Documentation for cast") h a : β` is equated with `a : α` immediately (using [heterogeneous equality](Basic-Propositions/Propositional-Equality/#--tech-term-Heterogeneous-equality)). 

Reduction
    
Definitional reduction is propagated, so `(a, b).1` is equated with `a`.
Below is a _representative slice_ of the propagators that demonstrates their overall style. Each follows the same skeleton.
  1. It inspect the truth value of sub‑expressions.
  2. If further facts can be derived, it either equates terms (connecting them on the metaphorical whiteboard) using (`pushEq`), or it indicates truth values using (`pushEqTrue` / `pushEqFalse`). These steps produce proof terms using internal helper lemmas such as `Grind.and_eq_of_eq_true_left`.
  3. If a contradiction arises, the goal is closed using (`closeGoal`).


_Upward propagation_ derives facts about a term from facts about sub-terms, while _downward propagation_ derives facts about sub-terms from facts about a term.
`/-- Propagate equalities *upwards* for conjunctions. -/ builtin_grind_propagator propagateAndUp ↑And := fun e => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let_expr [And](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") a b := e | return ()   if (← isEqTrue a) then     -- a = True  ⇒  (a ∧ b) = b     pushEq e b <|       mkApp3 (mkConst ``Grind.and_eq_of_eq_true_left)         a b (← mkEqTrueProof a)   else if (← isEqTrue b) then     -- b = True  ⇒  (a ∧ b) = a     pushEq e a <|       mkApp3 (mkConst ``Grind.and_eq_of_eq_true_right)         a b (← mkEqTrueProof b)   else if (← isEqFalse a) then     -- a = False  ⇒  (a ∧ b) = False     pushEqFalse e <|       mkApp3 (mkConst ``Grind.and_eq_of_eq_false_left)         a b (← mkEqFalseProof a)   else if (← isEqFalse b) then     -- b = False  ⇒  (a ∧ b) = False     pushEqFalse e <|       mkApp3 (mkConst ``Grind.and_eq_of_eq_false_right)         a b (← mkEqFalseProof b)  /-- Truth flows *down* when the whole `And` is proven `True`. -/ builtin_grind_propagator propagateAndDown ↓And :=   fun e => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   if (← isEqTrue e) then     let_expr [And](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") a b := e | return ()     let h ← mkEqTrueProof e     -- (a ∧ b) = True  ⇒  a = True     pushEqTrue a <| mkApp3       (mkConst ``Grind.eq_true_of_and_eq_true_left) a b h     -- (a ∧ b) = True  ⇒  B = True     pushEqTrue b <| mkApp3       (mkConst ``Grind.eq_true_of_and_eq_true_right) a b h `
Other frequently‑triggered propagators follow the same pattern:  
|  Propagator  |  Handles  |  Notes   |  
| --- | --- | --- |  
|  `propagateOrUp` / `propagateOrDown`  |  `A ∨ B`  |  Uses the truth table for disjunction to derive further truth values   |  
|  `propagateNotUp` / `propagateNotDown`  |  `¬ A`  |  Ensures that `¬ A` and `A` have opposite truth values   |  
|  `propagateEqUp` / `propagateEqDown`  |  `a = b`  |  Bridges Booleans, detects constructor clash   |  
|  `propagateIte` / `propagateDIte`  |  `ite` / `dite`  |  Equates the term with the chosen branch once the condition's truth value is known   |  
|  `propagateEtaStruct`  |  Values of structures tagged `[grind ext]`  |  Generates η‑expansion `a = ⟨a.1, …⟩`  |  
Many specialized variants for `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` mirror these rules exactly (e.g. `propagateBoolAndUp`).
##  16.4.1. Propagation‑Only Examples[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--grind--tactic--Constraint-Propagation--Propagation___Only-Examples "Permalink")
These goals are closed **purely** by constraint propagation—no case splits, no theory solvers:
`example (a : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : (a && !a) = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") := bya:[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")⊢ [(](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")a [&&](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [!](Basic-Types/Booleans/#Bool___not "Documentation for Bool.not")a[)](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  -- Conditional (ite): -- once the condition is true, ite picks the 'then' branch. example (c : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (t e : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (h : c = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) :     ([if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") c [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") t [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") e) = t := byc:[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")t:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")e:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")⊢ (if c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") then t else e) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  -- Negation propagates truth downwards. example (a : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (h : (!a) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : a = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") := bya:[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")h:[(](Basic-Types/Booleans/#Bool___not "Documentation for Bool.not")[!](Basic-Types/Booleans/#Bool___not "Documentation for Bool.not")a[)](Basic-Types/Booleans/#Bool___not "Documentation for Bool.not") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")⊢ a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
These snippets run instantly because the relevant propagators (`propagateBoolAndUp`, `propagateIte`, `propagateBoolNotDown`) fire as soon as the hypotheses are internalized. Setting the option `trace.grind.eqc` to `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` causes `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to print a line every time two equivalence classes merge, which is handy for seeing propagation in action.
The set of propagation rules is expanded and refined over time, so the InfoView will show increasingly rich `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")` and `[False](Basic-Propositions/Truth/#False "Documentation for False")` buckets. The full equivalence classes are displayed automatically _only when`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` fails_, and only for the first subgoal that it could not close—use this output to inspect missing facts and understand why the subgoal remains open.
Identifying Missing Facts
In this example, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` fails:
`example :     x = y ∧ y = z →     w = x ∨ w = v →     w = z := byα✝:Sort u_1x:α✝y:α✝z:α✝w:α✝v:α✝⊢ x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") z → w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") v → w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") z   ``grind` failed grindα:Sort u_1x y z w v:αleft:x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") yright:y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") zh_1:w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") vh_2:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") z⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y
 
    * [prop] y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") z
 
    * [prop] w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") v
 
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") z
 
 
  * [eqc] True propositions 
    * [prop] w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") v
 
    * [prop] w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") v
 
 
  * [eqc] False propositions 
    * [prop] w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x
 
    * [prop] w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") z
 
 
  * [eqc] Equivalence classes 
    * [eqc] {x, y, z}
 
    * [eqc] {w, v}
 
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
The resulting error message includes the identified equivalence classes along with the true and false propositions:

```
`grind` failed
grindα:Sort u_1x y z w v:αleft:x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") yright:y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") zh_1:w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") vh_2:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") z⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts

    * [prop] x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y


    * [prop] y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") z


    * [prop] w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") v


    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") z




  * [eqc] True propositions

    * [prop] w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") v


    * [prop] w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") v




  * [eqc] False propositions

    * [prop] w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x


    * [prop] w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") z




  * [eqc] Equivalence classes

    * [eqc] {x, y, z}


    * [eqc] {w, v}





```

Both `x = y` and `y = z` were discovered by constraint propagation from the `x = y ∧ y = z` premise. In this proof, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` performed a case split on `w = x ∨ w = v`. In the second branch, it could not place `w` and `z` in the same equivalence class.
[←16.3. Congruence Closure](The--grind--tactic/Congruence-Closure/#congruence-closure "16.3. Congruence Closure")[16.5. Case Analysis→](The--grind--tactic/Case-Analysis/#grind-split "16.5. Case Analysis")

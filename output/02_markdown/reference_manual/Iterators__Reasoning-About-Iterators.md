[←22.4. Iterator Combinators](Iterators/Iterator-Combinators/#The-Lean-Language-Reference--Iterators--Iterator-Combinators "22.4. Iterator Combinators")[23. Notations and Macros→](Notations-and-Macros/#language-extension "23. Notations and Macros")
#  22.5. Reasoning About Iterators[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Iterators--Reasoning-About-Iterators "Permalink")
##  22.5.1. Reasoning About Consumers[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Iterators--Reasoning-About-Iterators--Reasoning-About-Consumers "Permalink")
The iterator library provides a large number of useful lemmas. Most theorems about finite iterators can be proven by rewriting the statement to one about lists, using the fact that the correspondence between iterator combinators and corresponding list operations has already been proved. In practice, many of these theorems are already registered as `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` lemmas.
The lemmas have a very predictable naming system, and many are in the [default simp set](The-Simplifier/Simp-sets/#--tech-term-default-simp-set). Some of the most important include:
  * Consumer lemmas such as `Iter.all_toList`, `Iter.any_toList`, and `Iter.foldl_toList` that introduce lists as a model.
  * Simplification lemmas such as `Iter.toList_map` that `Iter.toList_filter` push the list model “inwards” in the goal.
  * Producer lemmas such as `List.toList_iter` and `Array.toList_iter` that replace a producer with a list model, removing iterators from the goal entirely.


The latter two categories are typically automatic with `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`.
Reasoning via Lists
Every element returned by an iterator that multiplies the numbers consumed some other iterator by two is even. To prove this statement, `Iter.all_toList`, `Iter.toList_map`, and `Array.toList_iter` are used to replace the statement about iterators with one about lists, after which `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` discharges the goal:
`example (l : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :     (l.[iter](Basic-Types/Arrays/#Array___iter "Documentation for Array.iter").[map](Iterators/Iterator-Combinators/#Std___Iter___map "Documentation for Std.Iter.map") (· * 2)).[all](Iterators/Consuming-Iterators/#Std___Iter___all "Documentation for Std.Iter.all") (· % 2 = 0) := byl:[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [Iter.all](Iterators/Consuming-Iterators/#Std___Iter___all "Documentation for Std.Iter.all") (fun x => [decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")x [%](Type-Classes/Basic-Classes/#HMod___mk "Documentation for HMod.hMod") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")) ([Iter.map](Iterators/Iterator-Combinators/#Std___Iter___map "Documentation for Std.Iter.map") (fun x => x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") 2) l.[iter](Basic-Types/Arrays/#Array___iter "Documentation for Array.iter")) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")   [rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic") [← Iter.all_toList]l:[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ (([Iter.map](Iterators/Iterator-Combinators/#Std___Iter___map "Documentation for Std.Iter.map") (fun x => x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") 2) l.[iter](Basic-Types/Arrays/#Array___iter "Documentation for Array.iter")).[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList").[all](Basic-Types/Linked-Lists/#List___all "Documentation for List.all") fun x => [decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")x [%](Type-Classes/Basic-Classes/#HMod___mk "Documentation for HMod.hMod") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")   [rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic") [Iter.toList_map]l:[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ (([List.map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map") (fun x => x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") 2) l.[iter](Basic-Types/Arrays/#Array___iter "Documentation for Array.iter").[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList")).[all](Basic-Types/Linked-Lists/#List___all "Documentation for List.all") fun x => [decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")x [%](Type-Classes/Basic-Classes/#HMod___mk "Documentation for HMod.hMod") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")   [rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic") [Array.toList_iter]l:[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ (([List.map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map") (fun x => x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") 2) l.toList).[all](Basic-Types/Linked-Lists/#List___all "Documentation for List.all") fun x => [decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")x [%](Type-Classes/Basic-Classes/#HMod___mk "Documentation for HMod.hMod") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")   [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")All goals completed! 🐙 `
In fact, because most of the needed lemmas are in the [default simp set](The-Simplifier/Simp-sets/#--tech-term-default-simp-set), the proof can be quite short:
`example (l : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :     (l.[iter](Basic-Types/Arrays/#Array___iter "Documentation for Array.iter").[map](Iterators/Iterator-Combinators/#Std___Iter___map "Documentation for Std.Iter.map") (· * 2)).[all](Iterators/Consuming-Iterators/#Std___Iter___all "Documentation for Std.Iter.all") (· % 2 = 0) := byl:[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [Iter.all](Iterators/Consuming-Iterators/#Std___Iter___all "Documentation for Std.Iter.all") (fun x => [decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")x [%](Type-Classes/Basic-Classes/#HMod___mk "Documentation for HMod.hMod") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")) ([Iter.map](Iterators/Iterator-Combinators/#Std___Iter___map "Documentation for Std.Iter.map") (fun x => x [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") 2) l.[iter](Basic-Types/Arrays/#Array___iter "Documentation for Array.iter")) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")   [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [← Iter.all_toList]All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAZRgEwHQBECGNOoJIwCmU20AzgFAURiEB2iKVhAHpuADaFwAUHcALjgBBKCQCecAHLYAlIIpwlvDqmBEoqEJjC8A7XABUcAEyzZqTB348DAUlNwAvHAAM8gS4BG4xXCgA7nAA2oAJhHAExJbWAPowEAAywGQwALp+gSGRmvFJKTHaYOlKmcGiEqi5yTAx6sTFcGSgYMxsnNx8giJimJIyMB5+SnxqGlo6+kam5tE29o4u7oLevkpN4CHh2bNxidWpQA"\))
##  22.5.2. Stepwise Reasoning[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Iterators--Reasoning-About-Iterators--Stepwise-Reasoning "Permalink")
When there are not enough lemmas to prove a property by rewriting to a list model, it can be necessary to prove things about iterators by reasoning directly about their step functions. The induction principles in this section are useful for stepwise reasoning.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.inductSkips "Permalink")def
```


Std.Iter.inductSkips.{x, u_1} {α β : Type u_1} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (motive : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β → Sort x)
  (step :
    (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) →
      ({it' : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β} →
          it.IsPlausibleStep ([IterStep.skip](Iterators/Iterator-Definitions/#Std___IterStep___yield "Documentation for Std.IterStep.skip") it') → motive it') →
        motive it)
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : motive it


Std.Iter.inductSkips.{x, u_1}
  {α β : Type u_1} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  (motive : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β → Sort x)
  (step :
    (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) →
      ({it' : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β} →
          it.IsPlausibleStep
              ([IterStep.skip](Iterators/Iterator-Definitions/#Std___IterStep___yield "Documentation for Std.IterStep.skip") it') →
            motive it') →
        motive it)
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : motive it


```

Induction principle for productive iterators: One can define a function `f` that maps every iterator `it` to an element of `motive it` by defining `f it` in terms of the values of `f` on the plausible skip successors of `it'.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.inductSkips "Permalink")def
```


Std.IterM.inductSkips.{x, u_1, u_2} {α : Type u_1}
  {m : Type u_1 → Type u_2} {β : Type u_1} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive") α m] (motive : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β → Sort x)
  (step :
    (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) →
      ({it' : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β} →
          it.IsPlausibleStep ([IterStep.skip](Iterators/Iterator-Definitions/#Std___IterStep___yield "Documentation for Std.IterStep.skip") it') → motive it') →
        motive it)
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : motive it


Std.IterM.inductSkips.{x, u_1, u_2}
  {α : Type u_1} {m : Type u_1 → Type u_2}
  {β : Type u_1} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive") α m]
  (motive : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β → Sort x)
  (step :
    (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) →
      ({it' : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β} →
          it.IsPlausibleStep
              ([IterStep.skip](Iterators/Iterator-Definitions/#Std___IterStep___yield "Documentation for Std.IterStep.skip") it') →
            motive it') →
        motive it)
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : motive it


```

Induction principle for productive monadic iterators: One can define a function `f` that maps every iterator `it` to an element of `motive it` by defining `f it` in terms of the values of `f` on the plausible skip successors of `it'.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.inductSteps "Permalink")def
```


Std.Iter.inductSteps.{x, u_1} {α β : Type u_1} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (motive : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β → Sort x)
  (step :
    (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) →
      ({it' : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β} →
          {out : β} →
            it.IsPlausibleStep ([IterStep.yield](Iterators/Iterator-Definitions/#Std___IterStep___yield "Documentation for Std.IterStep.yield") it' out) → motive it') →
        ({it' : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β} →
            it.IsPlausibleStep ([IterStep.skip](Iterators/Iterator-Definitions/#Std___IterStep___yield "Documentation for Std.IterStep.skip") it') → motive it') →
          motive it)
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : motive it


Std.Iter.inductSteps.{x, u_1}
  {α β : Type u_1} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (motive : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β → Sort x)
  (step :
    (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) →
      ({it' : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β} →
          {out : β} →
            it.IsPlausibleStep
                ([IterStep.yield](Iterators/Iterator-Definitions/#Std___IterStep___yield "Documentation for Std.IterStep.yield") it' out) →
              motive it') →
        ({it' : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β} →
            it.IsPlausibleStep
                ([IterStep.skip](Iterators/Iterator-Definitions/#Std___IterStep___yield "Documentation for Std.IterStep.skip") it') →
              motive it') →
          motive it)
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : motive it


```

Induction principle for finite iterators: One can define a function `f` that maps every iterator `it` to an element of `motive it` by defining `f it` in terms of the values of `f` on the plausible successors of `it'.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.inductSteps "Permalink")def
```


Std.IterM.inductSteps.{x, u_1, u_2} {α : Type u_1}
  {m : Type u_1 → Type u_2} {β : Type u_1} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite") α m]
  (motive : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β → Sort x)
  (step :
    (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) →
      ({it' : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β} →
          {out : β} →
            it.IsPlausibleStep ([IterStep.yield](Iterators/Iterator-Definitions/#Std___IterStep___yield "Documentation for Std.IterStep.yield") it' out) → motive it') →
        ({it' : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β} →
            it.IsPlausibleStep ([IterStep.skip](Iterators/Iterator-Definitions/#Std___IterStep___yield "Documentation for Std.IterStep.skip") it') → motive it') →
          motive it)
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : motive it


Std.IterM.inductSteps.{x, u_1, u_2}
  {α : Type u_1} {m : Type u_1 → Type u_2}
  {β : Type u_1} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite") α m]
  (motive : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β → Sort x)
  (step :
    (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) →
      ({it' : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β} →
          {out : β} →
            it.IsPlausibleStep
                ([IterStep.yield](Iterators/Iterator-Definitions/#Std___IterStep___yield "Documentation for Std.IterStep.yield") it' out) →
              motive it') →
        ({it' : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β} →
            it.IsPlausibleStep
                ([IterStep.skip](Iterators/Iterator-Definitions/#Std___IterStep___yield "Documentation for Std.IterStep.skip") it') →
              motive it') →
          motive it)
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : motive it


```

Induction principle for finite monadic iterators: One can define a function `f` that maps every iterator `it` to an element of `motive it` by defining `f it` in terms of the values of `f` on the plausible successors of `it'.
The standard library also includes lemmas for the stepwise behavior of all the producers and combinators. Examples include `List.step_iter_nil`, `List.step_iter_cons`, `IterM.step_map`.
##  22.5.3. Monads for Reasoning[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Iterators--Reasoning-About-Iterators--Monads-for-Reasoning "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iterators.PostconditionT.operation "Permalink")structure
```


Std.Iterators.PostconditionT.{w, w'} (m : Type w → Type w')
  (α : Type w) : Type (max w w')


Std.Iterators.PostconditionT.{w, w'}
  (m : Type w → Type w') (α : Type w) :
  Type (max w w')


```

`[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m α` represents an operation in the monad `m` together with a intrinsic proof that some postcondition holds for the `α` valued monadic result. It consists of a predicate `P` about `α` and an element of `m ({ a // P a })` and is a helpful tool for intrinsic verification, notably termination proofs, in the context of iterators.
`[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m` is a monad if `m` is. However, note that `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m α` is a structure, so that the compiler will generate inefficient code from recursive functions returning `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m α`. Optimizations for `[ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT")`, `[StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT")` etc. aren't applicable for structures.
Moreover, `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m α` is not a well-behaved monad transformer because `[PostconditionT.lift](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___lift "Documentation for Std.Iterators.PostconditionT.lift")` neither commutes with `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` nor with `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")`.
#  Constructor

```
[Std.Iterators.PostconditionT.mk](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT.mk").{w, w'}
```

#  Fields

```
Property : α → Prop
```

A predicate that holds for the return value(s) of the `m`-monadic operation.

```
operation : m ([Subtype](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") self.[Property](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT.Property"))
```

The actual monadic operation. Its return value is bundled together with a proof that it satisfies `Property`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iterators.PostconditionT.run "Permalink")def
```


Std.Iterators.PostconditionT.run.{w, w'} {m : Type w → Type w'}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type w} (x : [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m α) : m α


Std.Iterators.PostconditionT.run.{w, w'}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type w} (x : [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m α) :
  m α


```

Converts an operation from `PostConditionT m` to `m`, discarding the postcondition.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iterators.PostconditionT.lift "Permalink")def
```


Std.Iterators.PostconditionT.lift.{w, w'} {α : Type w}
  {m : Type w → Type w'} [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] (x : m α) : [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m α


Std.Iterators.PostconditionT.lift.{w, w'}
  {α : Type w} {m : Type w → Type w'}
  [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m] (x : m α) :
  [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m α


```

Lifts an operation from `m` to `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m` without asserting any nontrivial postcondition.
Caution: `lift` is not a lawful lift function. For example, `pure a : PostconditionT m α` is not the same as `[PostconditionT.lift](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___lift "Documentation for Std.Iterators.PostconditionT.lift") ([pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") a : m α)`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iterators.PostconditionT.liftWithProperty "Permalink")def
```


Std.Iterators.PostconditionT.liftWithProperty.{w, w'} {α : Type w}
  {m : Type w → Type w'} {P : α → Prop} (x : m [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") α [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") P α [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")) :
  [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m α


Std.Iterators.PostconditionT.liftWithProperty.{w,
    w'}
  {α : Type w} {m : Type w → Type w'}
  {P : α → Prop} (x : m [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") α [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") P α [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")) :
  [PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m α


```

Lifts a monadic value from `m { a : α // P a }` to a value `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT") m α`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.IsPlausibleIndirectOutput "Permalink")inductive predicate
```


Std.Iter.IsPlausibleIndirectOutput.{w} {α β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β → β → Prop


Std.Iter.IsPlausibleIndirectOutput.{w}
  {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] :
  [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β → β → Prop


```

Asserts that a certain iterator `it` could plausibly yield the value `out` after an arbitrary number of steps.
#  Constructors

```
direct.{w} {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] {it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β}
  {out : β} :
  it.IsPlausibleOutput out →
    it.[IsPlausibleIndirectOutput](Iterators/Reasoning-About-Iterators/#Std___Iter___IsPlausibleIndirectOutput___direct "Documentation for Std.Iter.IsPlausibleIndirectOutput") out
```

The output value could plausibly be emitted in the next step.

```
indirect.{w} {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  {it it' : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β} {out : β} :
  it'.IsPlausibleSuccessorOf it →
    it'.[IsPlausibleIndirectOutput](Iterators/Reasoning-About-Iterators/#Std___Iter___IsPlausibleIndirectOutput___direct "Documentation for Std.Iter.IsPlausibleIndirectOutput") out →
      it.[IsPlausibleIndirectOutput](Iterators/Reasoning-About-Iterators/#Std___Iter___IsPlausibleIndirectOutput___direct "Documentation for Std.Iter.IsPlausibleIndirectOutput") out
```

The output value could plausibly be emitted in a step after the next step.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iterators.HetT.Property "Permalink")structure
```


Std.Iterators.HetT.{w, w', v} (m : Type w → Type w') (α : Type v) :
  Type (max v w')


Std.Iterators.HetT.{w, w', v}
  (m : Type w → Type w') (α : Type v) :
  Type (max v w')


```

If `m` is a monad, then `[HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m` is a monad that has two features:
  * It generalizes `m` to arbitrary universes.
  * It tracks a postcondition property that holds for the monadic return value, similarly to `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT")`.


This monad is noncomputable and is merely a vehicle for more convenient proofs, especially proofs about the equivalence of iterators, because it avoids universe issues and spares users the work to handle the postconditions manually.
Caution: Just like `[PostconditionT](Iterators/Reasoning-About-Iterators/#Std___Iterators___PostconditionT___mk "Documentation for Std.Iterators.PostconditionT")`, this is not a lawful monad transformer. To lift from `m` to `[HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m`, use `[HetT.lift](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___lift "Documentation for Std.Iterators.HetT.lift")`.
Because this monad is fundamentally universe-polymorphic, it is recommended for consistency to always use the methods `[HetT.pure](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___pure "Documentation for Std.Iterators.HetT.pure")`, `[HetT.map](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___map "Documentation for Std.Iterators.HetT.map")` and `[HetT.bind](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___bind "Documentation for Std.Iterators.HetT.bind")` instead of the homogeneous versions `[Pure.pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")`, `[Functor.map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map")` and `[Bind.bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")`.
#  Constructor

```
[Std.Iterators.HetT.mk](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT.mk").{w, w', v}
```

#  Fields

```
Property : α → Prop
```

A predicate that holds for the return value(s) of the `m`-monadic operation.

```
small : Std.Internal.Small ([Subtype](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") self.[Property](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT.Property"))
```

A proof that the possible return values are equivalent to a `w`-small type.

```
operation : m (Std.Internal.USquash ([Subtype](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") self.[Property](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT.Property")))
```

The actual monadic operation. Its return value is bundled together with a proof that it satisfies `Property` and squashed so that it fits into the monad `m`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.stepAsHetT "Permalink")def
```


Std.IterM.stepAsHetT.{u_1, u_2} {α : Type u_1} {m : Type u_1 → Type u_2}
  {β : Type u_1} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) :
  [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m ([IterStep](Iterators/Iterator-Definitions/#Std___IterStep___yield "Documentation for Std.IterStep") ([IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) β)


Std.IterM.stepAsHetT.{u_1, u_2}
  {α : Type u_1} {m : Type u_1 → Type u_2}
  {β : Type u_1} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) :
  [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m ([IterStep](Iterators/Iterator-Definitions/#Std___IterStep___yield "Documentation for Std.IterStep") ([IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) β)


```

A noncomputable variant of `[IterM.step](Iterators/Consuming-Iterators/#Std___IterM___step "Documentation for Std.IterM.step")` using the `[HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT")` monad. It is used in the definition of the equivalence relations on iterators, namely `[IterM.Equiv](Iterators/Reasoning-About-Iterators/#Std___IterM___Equiv "Documentation for Std.IterM.Equiv")` and `[Iter.Equiv](Iterators/Reasoning-About-Iterators/#Std___Iter___Equiv "Documentation for Std.Iter.Equiv")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iterators.HetT.lift "Permalink")def
```


Std.Iterators.HetT.lift.{w, w'} {α : Type w} {m : Type w → Type w'}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (x : m α) : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m α


Std.Iterators.HetT.lift.{w, w'}
  {α : Type w} {m : Type w → Type w'}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (x : m α) : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m α


```

Lifts `x : m α` into `[HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m α` with the trivial postcondition.
Caution: This is not a lawful monad lifting function
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iterators.HetT.prun "Permalink")def
```


Std.Iterators.HetT.prun.{u_1, u_2, u_3} {m : Type u_1 → Type u_2}
  {α : Type u_3} {β : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (x : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m α)
  (f : (a : α) → x.[Property](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT.Property") a → m β) : m β


Std.Iterators.HetT.prun.{u_1, u_2, u_3}
  {m : Type u_1 → Type u_2} {α : Type u_3}
  {β : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (x : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m α)
  (f : (a : α) → x.[Property](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT.Property") a → m β) : m β


```

Applies the given function to the result of the contained `m`-monadic operation with a proof that the postcondition property holds, returning another operation in `m`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iterators.HetT.pure "Permalink")def
```


Std.Iterators.HetT.pure.{w, w', v} {m : Type w → Type w'} [[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") m]
  {α : Type v} (a : α) : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m α


Std.Iterators.HetT.pure.{w, w', v}
  {m : Type w → Type w'} [[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") m]
  {α : Type v} (a : α) : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m α


```

A universe-heterogeneous version of `[Pure.pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")`. Given `a : α`, it returns an element of `[HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m α` with the postcondition `(a = ·)`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iterators.HetT.map "Permalink")def
```


Std.Iterators.HetT.map.{w, w', u, v} {m : Type w → Type w'} [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m]
  {α : Type u} {β : Type v} (f : α → β) (x : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m α) : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m β


Std.Iterators.HetT.map.{w, w', u, v}
  {m : Type w → Type w'} [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m]
  {α : Type u} {β : Type v} (f : α → β)
  (x : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m α) : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m β


```

A universe-heterogeneous version of `[Functor.map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iterators.HetT.pmap "Permalink")def
```


Std.Iterators.HetT.pmap.{w, w', u, v} {m : Type w → Type w'} [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m]
  {α : Type u} {β : Type v} (x : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m α)
  (f : (a : α) → x.[Property](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT.Property") a → β) : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m β


Std.Iterators.HetT.pmap.{w, w', u, v}
  {m : Type w → Type w'} [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m]
  {α : Type u} {β : Type v} (x : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m α)
  (f : (a : α) → x.[Property](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT.Property") a → β) :
  [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m β


```

A generalization of `[HetT.map](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___map "Documentation for Std.Iterators.HetT.map")` that provides the postcondition property to the mapping function.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iterators.HetT.bind "Permalink")def
```


Std.Iterators.HetT.bind.{w, w', u, v} {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type u} {β : Type v} (x : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m α) (f : α → [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m β) : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m β


Std.Iterators.HetT.bind.{w, w', u, v}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type u} {β : Type v} (x : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m α)
  (f : α → [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m β) : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m β


```

A universe-heterogeneous version of `[Bind.bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iterators.HetT.pbind "Permalink")def
```


Std.Iterators.HetT.pbind.{w, w', u, v} {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type u} {β : Type v} (x : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m α)
  (f : (a : α) → x.[Property](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT.Property") a → [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m β) : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m β


Std.Iterators.HetT.pbind.{w, w', u, v}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type u} {β : Type v} (x : [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m α)
  (f :
    (a : α) → x.[Property](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT.Property") a → [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m β) :
  [HetT](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___mk "Documentation for Std.Iterators.HetT") m β


```

A generalization of `[HetT.bind](Iterators/Reasoning-About-Iterators/#Std___Iterators___HetT___bind "Documentation for Std.Iterators.HetT.bind")` that provides the postcondition property to the mapping function.
##  22.5.4. Equivalence[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Iterators--Reasoning-About-Iterators--Equivalence "Permalink")
Iterator equivalence is defined in terms of the observable behavior of iterators, rather than their implementations. In particular, the internal state is ignored.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.Equiv "Permalink")def
```


Std.Iter.Equiv.{u_1} {α₁ α₂ β : Type u_1} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₁ [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (ita : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) (itb : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : Prop


Std.Iter.Equiv.{u_1} {α₁ α₂ β : Type u_1}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₁ [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  (ita : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) (itb : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : Prop


```

Equivalence relation on iterators. Equivalent iterators behave the same as long as the internal state of them is not directly inspected.
Two iterators (possibly of different types) are equivalent if they have the same `[Iterator.IsPlausibleStep](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator.IsPlausibleStep")` relation and their step functions are the same _up to equivalence of the successor iterators_. This coinductive definition captures the idea that the only relevant feature of an iterator is its step function. Other information retrievable from the iterator -- for example, whether it is a list iterator or an array iterator -- is totally irrelevant for the equivalence judgement.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.Equiv "Permalink")def
```


Std.IterM.Equiv.{w, w'} {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") m]
  {β α₁ α₂ : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₁ m β] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ m β]
  (ita : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) (itb : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : Prop


Std.IterM.Equiv.{w, w'}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad") m] {β α₁ α₂ : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₁ m β] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α₂ m β]
  (ita : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) (itb : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) :
  Prop


```

Equivalence relation on monadic iterators. Equivalent iterators behave the same as long as the internal state of them is not directly inspected.
Two iterators (possibly of different types) are equivalent if they have the same `[Iterator.IsPlausibleStep](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator.IsPlausibleStep")` relation and their step functions are the same _up to equivalence of the successor iterators_. This coinductive definition captures the idea that the only relevant feature of an iterator is its step function. Other information retrievable from the iterator -- for example, whether it is a list iterator or an array iterator -- is totally irrelevant for the equivalence judgement.
[←22.4. Iterator Combinators](Iterators/Iterator-Combinators/#The-Lean-Language-Reference--Iterators--Iterator-Combinators "22.4. Iterator Combinators")[23. Notations and Macros→](Notations-and-Macros/#language-extension "23. Notations and Macros")

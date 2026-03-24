[←19.1. Truth](Basic-Propositions/Truth/#true-false "19.1. Truth")[19.3. Quantifiers→](Basic-Propositions/Quantifiers/#The-Lean-Language-Reference--Basic-Propositions--Quantifiers "19.3. Quantifiers")
#  19.2. Logical Connectives[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Propositions--Logical-Connectives "Permalink")
Conjunction is implemented as the inductively defined proposition `[And](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And")`. The constructor `[And.intro](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And.intro")` represents the introduction rule for conjunction: to prove a conjunction, it suffices to prove both conjuncts. Similarly, `[And.elim](Basic-Propositions/Logical-Connectives/#And___elim "Documentation for And.elim")` represents the elimination rule: given a proof of a conjunction and a proof of some other statement that assumes both conjuncts, the other statement can be proven. Because `[And](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And")` is a [subsingleton](The-Type-System/Inductive-Types/#--tech-term-subsingleton), `[And.elim](Basic-Propositions/Logical-Connectives/#And___elim "Documentation for And.elim")` can also be used as part of computing data. However, it should not be confused with `[PProd](Basic-Types/Tuples/#PProd___mk "Documentation for PProd")`: using non-computable reasoning principles such as the Axiom of Choice to define data (including `[Prod](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")`) causes Lean to be unable to compile and run the resulting program, while using them in a proof of a proposition causes no such issue.
In a [tactic](Tactic-Proofs/#tactics) proof, conjunctions can be proved using `[And.intro](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And.intro")` explicitly via `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic")`, but `[constructor](Tactic-Proofs/Tactic-Reference/#constructor "Documentation for tactic")` is more common. When multiple conjunctions are nested in a proof goal, `[and_intros](Tactic-Proofs/Tactic-Reference/#and_intros "Documentation for tactic")` can be used to apply `[And.intro](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And.intro")` in each relevant location. Assumptions of conjunctions in the context can be simplified using `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")`, pattern matching with `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` or `[match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic")`, or `[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=And "Permalink")structure
```


And (a b : Prop) : Prop


And (a b : Prop) : Prop


```

`[And](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") a b`, or `a ∧ b`, is the conjunction of propositions. It can be constructed and destructed like a pair: if `ha : a` and `hb : b` then `⟨ha, hb⟩ : a ∧ b`, and if `h : a ∧ b` then `h.[left](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And.left") : a` and `h.[right](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And.right") : b`.
Conventions for notations in identifiers:
  * The recommended spelling of `∧` in identifiers is `[and](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")`.
  * The recommended spelling of `/\` in identifiers is `[and](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")` (prefer `∧` over `/\`).


#  Constructor

```
[And.intro](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And.intro")
```

`[And.intro](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And.intro") : a → b → a ∧ b` is the constructor for the And operation.
#  Fields

```
left : a
```

Extract the left conjunct from a conjunction. `h : a ∧ b` then `h.[left](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And.left")`, also notated as `h.1`, is a proof of `a`.

```
right : b
```

Extract the right conjunct from a conjunction. `h : a ∧ b` then `h.[right](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And.right")`, also notated as `h.2`, is a proof of `b`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=And.elim "Permalink")def
```


And.elim.{u_1} {a b : Prop} {α : Sort u_1} (f : a → b → α) (h : a [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") b) :
  α


And.elim.{u_1} {a b : Prop} {α : Sort u_1}
  (f : a → b → α) (h : a [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") b) : α


```

Non-dependent eliminator for `[And](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And")`.
Disjunction implemented as the inductively defined proposition `[Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or")`. It has two constructors, one for each introduction rule: a proof of either disjunct is sufficient to prove the disjunction. While the definition of `[Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or")` is similar to that of `[Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")`, it is quite different in practice. Because `[Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")` is a type, it is possible to check _which_ constructor was used to create any given value. `[Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or")`, on the other hand, forms propositions: terms that prove a disjunction cannot be interrogated to check which disjunct was true. In other words, because `[Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or")` is not a [subsingleton](The-Type-System/Inductive-Types/#--tech-term-subsingleton), its proofs cannot be used as part of a computation.
In a [tactic](Tactic-Proofs/#tactics) proof, disjunctions can be proved using either constructor (`[Or.inl](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or.inl")` or `[Or.inr](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or.inr")`) explicitly via `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic")`. Assumptions of disjunctions in the context can be simplified using `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")`, pattern matching with `[match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic")`, or `[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Or.inl "Permalink")inductive predicate
```


Or (a b : Prop) : Prop


Or (a b : Prop) : Prop


```

`[Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") a b`, or `a ∨ b`, is the disjunction of propositions. There are two constructors for `[Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or")`, called `[Or.inl](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or.inl") : a → a ∨ b` and `[Or.inr](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or.inr") : b → a ∨ b`, and you can use `[match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic")` or `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")` to destruct an `[Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or")` assumption into the two cases.
Conventions for notations in identifiers:
  * The recommended spelling of `∨` in identifiers is `[or](Basic-Types/Booleans/#Bool___or "Documentation for Bool.or")`.
  * The recommended spelling of `\/` in identifiers is `[or](Basic-Types/Booleans/#Bool___or "Documentation for Bool.or")` (prefer `∨` over `\/`).


#  Constructors

```
inl {a b : Prop} (h : a) : a [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") b
```

`[Or.inl](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or.inl")` is "left injection" into an `[Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or")`. If `h : a` then `[Or.inl](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or.inl") h : a ∨ b`.

```
inr {a b : Prop} (h : b) : a [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") b
```

`[Or.inr](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or.inr")` is "right injection" into an `[Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or")`. If `h : b` then `[Or.inr](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or.inr") h : a ∨ b`.
When either disjunct is [decidable](Type-Classes/Basic-Classes/#--tech-term-decidable), it becomes possible to use `[Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or")` to compute data. This is because the decision procedure's result provides a suitable branch condition.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Or.by_cases "Permalink")def
```


Or.by_cases.{u} {p q : Prop} [[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") p] {α : Sort u} (h : p [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") q)
  (h₁ : p → α) (h₂ : q → α) : α


Or.by_cases.{u} {p q : Prop} [[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") p]
  {α : Sort u} (h : p [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") q) (h₁ : p → α)
  (h₂ : q → α) : α


```

Construct a non-Prop by cases on an `[Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or")`, when the left conjunct is decidable.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Or.by_cases' "Permalink")def
```


Or.by_cases'.{u} {q p : Prop} [[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") q] {α : Sort u} (h : p [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") q)
  (h₁ : p → α) (h₂ : q → α) : α


Or.by_cases'.{u} {q p : Prop}
  [[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") q] {α : Sort u} (h : p [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") q)
  (h₁ : p → α) (h₂ : q → α) : α


```

Construct a non-Prop by cases on an `[Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or")`, when the right conjunct is decidable.
Rather than encoding negation as an inductive type, `¬P` is defined to mean `P → [False](Basic-Propositions/Truth/#False "Documentation for False")`. In other words, to prove a negation, it suffices to assume the negated statement and derive a contradiction. This also means that `[False](Basic-Propositions/Truth/#False "Documentation for False")` can be derived immediately from a proof of a proposition and its negation, and then used to prove any proposition or inhabit any type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Not "Permalink")def
```


Not (a : Prop) : Prop


Not (a : Prop) : Prop


```

`[Not](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not") p`, or `¬p`, is the negation of `p`. It is defined to be `p → [False](Basic-Propositions/Truth/#False "Documentation for False")`, so if your goal is `¬p` you can use `[intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") h` to turn the goal into `h : p ⊢ False`, and if you have `hn : ¬p` and `h : p` then `hn h : [False](Basic-Propositions/Truth/#False "Documentation for False")` and `(hn h).[elim](Basic-Propositions/Truth/#False___elim "Documentation for False.elim")` will prove anything. For more information: [Propositional Logic](https://lean-lang.org/theorem_proving_in_lean4/propositions_and_proofs.html#propositional-logic)
Conventions for notations in identifiers:
  * The recommended spelling of `¬` in identifiers is `[not](Basic-Types/Booleans/#Bool___not "Documentation for Bool.not")`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=absurd "Permalink")def
```


absurd.{v} {a : Prop} {b : Sort v} (h₁ : a) (h₂ : [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")a) : b


absurd.{v} {a : Prop} {b : Sort v}
  (h₁ : a) (h₂ : [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")a) : b


```

Anything follows from two contradictory hypotheses. Example:
`example (hp : p) (hnp : ¬p) : q := [absurd](Basic-Propositions/Logical-Connectives/#absurd "Documentation for absurd") hp hnp `
For more information: [Propositional Logic](https://lean-lang.org/theorem_proving_in_lean4/propositions_and_proofs.html#propositional-logic)
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Not.elim "Permalink")def
```


Not.elim.{u_1} {a : Prop} {α : Sort u_1} (H1 : [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")a) (H2 : a) : α


Not.elim.{u_1} {a : Prop} {α : Sort u_1}
  (H1 : [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")a) (H2 : a) : α


```

_Ex falso_ for negation: from `¬a` and `a` anything follows. This is the same as `[absurd](Basic-Propositions/Logical-Connectives/#absurd "Documentation for absurd")` with the arguments flipped, but it is in the `[Not](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")` namespace so that projection notation can be used.
Implication is represented using [function types](Terms/Function-Types/#function-types) in the [universe](The-Type-System/Universes/#--tech-term-universes) of [propositions](The-Type-System/Propositions/#--tech-term-Propositions). To prove `A → B`, it is enough to prove `B` after assuming `A`. This corresponds to the typing rule for ``Lean.Parser.Term.fun : term```fun`. Similarly, the typing rule for function application corresponds to _modus ponens_ : given a proof of `A → B` and a proof of `A`, `B` can be proved.
Truth-Functional Implication
The representation of implication as functions in the universe of propositions is equivalent to the traditional definition in which `A → B` is defined as `(¬A) ∨ B`. This can be proved using [propositional extensionality](The-Type-System/Propositions/#--tech-term-Extensionality) and the law of the excluded middle:
`theorem truth_functional_imp {A B : Prop} :     ((¬ A) ∨ B) = (A → B) := byA:PropB:Prop⊢ [(](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or")[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")A [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") B[)](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") (A → B)   [apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") [propext](The-Type-System/Propositions/#propext "Documentation for propext")aA:PropB:Prop⊢ [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")A [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") B [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") A → B   [constructor](Tactic-Proofs/Tactic-Reference/#constructor "Documentation for tactic")a.mpA:PropB:Prop⊢ [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")A [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") B → A → Ba.mprA:PropB:Prop⊢ (A → B) → [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")A [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") B   .a.mpA:PropB:Prop⊢ [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")A [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") B → A → B [rintro](Tactic-Proofs/Tactic-Reference/#rintro "Documentation for tactic") (h | h) aa.mp.inlA:PropB:Proph:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")Aa:A⊢ Ba.mp.inrA:PropB:Proph:Ba:A⊢ B <;>a.mp.inlA:PropB:Proph:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")Aa:A⊢ Ba.mp.inrA:PropB:Proph:Ba:A⊢ B [trivial](Tactic-Proofs/Tactic-Reference/#trivial "Documentation for tactic")All goals completed! 🐙   .a.mprA:PropB:Prop⊢ (A → B) → [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")A [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") B [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") ha.mprA:PropB:Proph:A → B⊢ [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")A [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") B     [by_cases](Tactic-Proofs/Tactic-Reference/#by_cases "Documentation for tactic") AposA:PropB:Proph:A → Bh✝:A⊢ [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")A [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") BnegA:PropB:Proph:A → Bh✝:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")A⊢ [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")A [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") B     .posA:PropB:Proph:A → Bh✝:A⊢ [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")A [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") B [apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") [Or.inr](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or.inr")pos.hA:PropB:Proph:A → Bh✝:A⊢ B; [solve_by_elim](Tactic-Proofs/Tactic-Reference/#solve_by_elim "Documentation for tactic")All goals completed! 🐙     .negA:PropB:Proph:A → Bh✝:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")A⊢ [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")A [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") B [apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") [Or.inl](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or.inl")neg.hA:PropB:Proph:A → Bh✝:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")A⊢ [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")A; [trivial](Tactic-Proofs/Tactic-Reference/#trivial "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("C4Cwpg9gTmC2AEwoFdQH0BmyB2BjYAlhNgIYA2aBsADvAN4CC8AQvAFzwAKUE1AvuwBQ8EfAAUYgDXwGASniAKIhbyAvOKaAkwmXs1AIwCew+CWrUy++NR7UwAD2BHcxAM5Jk+aEYB08KAWxIEOIg8AA+8CDyJPAAPADcAHyIfgBuBOTe8P6BEUYiBmi4JM5gzjJ58D4mZhYA8lBe/lBx8M4QZClgaAVgZFQVVabm8PWN2GQtSARp5EA"\))
Logical equivalence, or “if and only if”, is represented using a structure that is equivalent to the conjunction of both directions of the implication.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Iff.intro "Permalink")structure
```


Iff (a b : Prop) : Prop


Iff (a b : Prop) : Prop


```

If and only if, or logical bi-implication. `a ↔ b` means that `a` implies `b` and vice versa. By `[propext](The-Type-System/Propositions/#propext "Documentation for propext")`, this implies that `a` and `b` are equal and hence any expression involving `a` is equivalent to the corresponding expression with `b` instead.
Conventions for notations in identifiers:
  * The recommended spelling of `↔` in identifiers is `iff`.
  * The recommended spelling of `<->` in identifiers is `iff` (prefer `↔` over `<->`).


#  Constructor

```
[Iff.intro](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff.intro")
```

If `a → b` and `b → a` then `a` and `b` are equivalent.
#  Fields

```
mp : a → b
```

Modus ponens for if and only if. If `a ↔ b` and `a`, then `b`.

```
mpr : b → a
```

Modus ponens for if and only if, reversed. If `a ↔ b` and `b`, then `a`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Iff.elim "Permalink")def
```


Iff.elim.{u_1} {a b : Prop} {α : Sort u_1} (f : (a → b) → (b → a) → α)
  (h : a [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") b) : α


Iff.elim.{u_1} {a b : Prop} {α : Sort u_1}
  (f : (a → b) → (b → a) → α)
  (h : a [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") b) : α


```

Non-dependent eliminator for `[Iff](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff")`.
syntaxPropositional Connectives
The logical connectives other than implication are typically referred to using dedicated syntax, rather than via their defined names:

```
term ::= ...
    | 


And a b, or a ∧ b, is the conjunction of propositions. It can be
constructed and destructed like a pair: if ha : a and hb : b then
⟨ha, hb⟩ : a ∧ b, and if h : a ∧ b then h.left : a and h.right : b.


Conventions for notations in identifiers:




  * The recommended spelling of ∧ in identifiers is and.




term ∧ term
```

```
term ::= ...
    | 


Or a b, or a ∨ b, is the disjunction of propositions. There are two
constructors for Or, called Or.inl : a → a ∨ b and Or.inr : b → a ∨ b,
and you can use match or cases to destruct an Or assumption into the
two cases.


Conventions for notations in identifiers:




  * The recommended spelling of ∨ in identifiers is or.




term ∨ term
```

```
term ::= ...
    | 


Not p, or ¬p, is the negation of p. It is defined to be p → False,
so if your goal is ¬p you can use intro h to turn the goal into
h : p ⊢ False, and if you have hn : ¬p and h : p then hn h : False
and (hn h).elim will prove anything.
For more information: Propositional Logic[](https://lean-lang.org/theorem_proving_in_lean4/propositions_and_proofs.html#propositional-logic)


Conventions for notations in identifiers:




  * The recommended spelling of ¬ in identifiers is not.




¬ term
```

```
term ::= ...
    | 


If and only if, or logical bi-implication. a ↔ b means that a implies b and vice versa.
By propext, this implies that a and b are equal and hence any expression involving a
is equivalent to the corresponding expression with b instead.


Conventions for notations in identifiers:




  * The recommended spelling of ↔ in identifiers is iff.




term ↔ term
```

[←19.1. Truth](Basic-Propositions/Truth/#true-false "19.1. Truth")[19.3. Quantifiers→](Basic-Propositions/Quantifiers/#The-Lean-Language-Reference--Basic-Propositions--Quantifiers "19.3. Quantifiers")

[←About: projNonPropFromProp](Error-Explanations/About___--projNonPropFromProp/#The-Lean-Language-Reference--Error-Explanations--About___--projNonPropFromProp "About: projNonPropFromProp")[About: redundantMatchAlt→](Error-Explanations/About___--redundantMatchAlt/#The-Lean-Language-Reference--Error-Explanations--About___--redundantMatchAlt "About: redundantMatchAlt")
#  About: `propRecLargeElim`[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--propRecLargeElim "Permalink")
Error code: `lean.propRecLargeElim`
_Attempted to eliminate a proof into a higher type universe._
**Severity:** Error**Since:** 4.23.0
This error occurs when attempting to eliminate a proof of a proposition into a higher type universe. Because Lean's type theory does not allow large elimination from `Prop`, it is invalid to pattern-match on such values—e.g., by using ``Lean.Parser.Term.let : term`
`let` is used to declare a local definition. Example:

```
let x := 1
let y := x + 1
x + y

```

Since functions are first class citizens in Lean, you can use `let` to declare local functions too.

```
let double := fun x => 2*x
double (double 3)

```

For recursive definitions, you should use `let rec`. You can also perform pattern matching using `let`. For example, assume `p` has type `Nat × Nat`, then you can write

```
let (x, y) := p
x + y

```

The _anaphoric let_ `let := v` defines a variable called `this`.
``let` or ``Lean.Parser.Term.match : term`
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
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match)—to produce a piece of data in a non-propositional universe (i.e., `Type u`). More precisely, the motive of a propositional recursor must be a proposition. (See the manual section on [Subsingleton Elimination](The-Type-System/Inductive-Types/#subsingleton-elimination) for exceptions to this rule.)
Note that this error will arise in any expression that eliminates from a proof into a non-propositional universe, even if that expression occurs within another expression of propositional type (e.g., in a ``Lean.Parser.Term.let : term`
`let` is used to declare a local definition. Example:

```
let x := 1
let y := x + 1
x + y

```

Since functions are first class citizens in Lean, you can use `let` to declare local functions too.

```
let double := fun x => 2*x
double (double 3)

```

For recursive definitions, you should use `let rec`. You can also perform pattern matching using `let`. For example, assume `p` has type `Nat × Nat`, then you can write

```
let (x, y) := p
x + y

```

The _anaphoric let_ `let := v` defines a variable called `this`.
``let` binding in a proof). The “Defining an intermediate data value within a proof” example below demonstrates such an occurrence. Errors of this kind can usually be resolved by moving the recursor application “outward,” so that its motive is the proposition being proved rather than the type of data-valued term.
##  Examples[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--propRecLargeElim--Examples "Permalink")
Defining an Intermediate Data Value Within a Proof
OriginalFixed
`example {α : Type} [inst : [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") α] (p : α → Prop) :     ∃ x, p x ∨ ¬ p x :=   let val :=     `Tactic `cases` failed with a nested error: Tactic `induction` failed: recursor `Nonempty.casesOn` can only eliminate into `Prop`  α:Typemotive:[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") α → Sort ?u.48h_1:(x : α) → motive ⋯inst✝:[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") α⊢ motive inst✝ after processing   _ the dependent pattern matcher can solve the following kinds of equations - <var> = <term> and <term> = <var> - <term> = <term> where the terms are definitionally equal - <constructor> = <constructor>, examples: List.cons x xs = List.cons y ys, and List.cons x xs = List.nil`[match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") inst [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") | [.intro](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty.intro") x => x ⟨val, Classical.em (p val)⟩ `
```
Tactic `cases` failed with a nested error:
Tactic `induction` failed: recursor `Nonempty.casesOn` can only eliminate into `Prop`

α:Typemotive:[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") α → Sort ?u.48h_1:(x : α) → motive ⋯inst✝:[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") α⊢ motive inst✝ after processing
  _
the dependent pattern matcher can solve the following kinds of equations
- <var> = <term> and <term> = <var>
- <term> = <term> where the terms are definitionally equal
- <constructor> = <constructor>, examples: List.cons x xs = List.cons y ys, and List.cons x xs = List.nil
```

`example {α : Type} [inst : [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") α] (p : α → Prop) :     ∃ x, p x ∨ ¬ p x :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") inst [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | [.intro](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty.intro") x => ⟨x, Classical.em (p x)⟩ `
Even though the ``Lean.Parser.Command.example```example` being defined has a propositional type, the body of `val` does not; it has type `α : Type`. Thus, pattern-matching on the proof of `Nonempty α` (a proposition) to produce `val` requires eliminating that proof into a non-propositional type and is disallowed. Instead, the ``Lean.Parser.Term.match : term`
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
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match) expression must be moved to the top level of the `example`, where the result is a `Prop`-valued proof of the existential claim stated in the example's header. This restructuring could also be done using a pattern-matching ``Lean.Parser.Term.let : term`
`let` is used to declare a local definition. Example:

```
let x := 1
let y := x + 1
x + y

```

Since functions are first class citizens in Lean, you can use `let` to declare local functions too.

```
let double := fun x => 2*x
double (double 3)

```

For recursive definitions, you should use `let rec`. You can also perform pattern matching using `let`. For example, assume `p` has type `Nat × Nat`, then you can write

```
let (x, y) := p
x + y

```

The _anaphoric let_ `let := v` defines a variable called `this`.
``let` binding.
Extracting the Witness from an Existential Proof
OriginalFixed (in Prop)Fixed (in Type)
`def getWitness {α : Type u} {p : α → Prop} (h : ∃ x, p x) : α :=   `Tactic `cases` failed with a nested error: Tactic `induction` failed: recursor `Exists.casesOn` can only eliminate into `Prop`  α:Type up:α → Propmotive:[(](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists")[∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") x[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") p x[)](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") → Sort ?u.52h_1:(x : α) → (h : p x) → motive ⋯h✝:[∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") x[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") p x⊢ motive h✝ after processing   _ the dependent pattern matcher can solve the following kinds of equations - <var> = <term> and <term> = <var> - <term> = <term> where the terms are definitionally equal - <constructor> = <constructor>, examples: List.cons x xs = List.cons y ys, and List.cons x xs = List.nil`[match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") h [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") | [.intro](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists.intro") x _ => x `
```
Tactic `cases` failed with a nested error:
Tactic `induction` failed: recursor `Exists.casesOn` can only eliminate into `Prop`

α:Type up:α → Propmotive:[(](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists")[∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") x[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") p x[)](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") → Sort ?u.52h_1:(x : α) → (h : p x) → motive ⋯h✝:[∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") x[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") p x⊢ motive h✝ after processing
  _
the dependent pattern matcher can solve the following kinds of equations
- <var> = <term> and <term> = <var>
- <term> = <term> where the terms are definitionally equal
- <constructor> = <constructor>, examples: List.cons x xs = List.cons y ys, and List.cons x xs = List.nil
```

`theorem useWitness {α : Type u} {p : α → Prop} {q : Prop}     (h : ∃ x, p x) (hq : (x : α) → p x → q) : q :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") h [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | [.intro](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists.intro") x hx => hq x hx `
`def getWitness {α : Type u} {p : α → Prop}     (h : (x : α) ×' p x) : α :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") h [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | [.mk](Basic-Types/Tuples/#PSigma___mk "Documentation for PSigma.mk") x _ => x `
In this example, simply relocating the pattern-match is insufficient; the attempted definition `getWitness` is fundamentally unsound. (Consider the case where `p` is `fun (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) => n > 0`: if `h` and `h'` are proofs of `∃ x, x > 0`, with `h` using witness `1` and `h'` witness `2`, then since `h = h'` by proof irrelevance, it follows that `getWitness h = getWitness h'`—i.e., `1 = 2`.)
Instead, `getWitness` must be rewritten: either the resulting type of the function must be a proposition (the first fixed example above), or `h` must not be a proposition (the second).
In the first corrected example, the resulting type of `useWitness` is now a proposition `q`. This allows us to pattern-match on `h`—since we are eliminating into a propositional type—and pass the unpacked values to `hq`. From a programmatic perspective, one can view `useWitness` as rewriting `getWitness` in continuation-passing style, restricting subsequent computations to use its result only to construct values in `Prop`, as required by the prohibition on propositional large elimination. Note that `useWitness` is the existential elimination principle `Exists.elim`.
The second corrected example changes the type of `h` from an existential proposition to a `Type`-valued dependent pair (corresponding to the `[PSigma](Basic-Types/Tuples/#PSigma___mk "Documentation for PSigma")` type constructor). Since this type is not propositional, eliminating into `α : Type u` is no longer invalid, and the previously attempted pattern match now type-checks.
[←About: projNonPropFromProp](Error-Explanations/About___--projNonPropFromProp/#The-Lean-Language-Reference--Error-Explanations--About___--projNonPropFromProp "About: projNonPropFromProp")[About: redundantMatchAlt→](Error-Explanations/About___--redundantMatchAlt/#The-Lean-Language-Reference--Error-Explanations--About___--redundantMatchAlt "About: redundantMatchAlt")

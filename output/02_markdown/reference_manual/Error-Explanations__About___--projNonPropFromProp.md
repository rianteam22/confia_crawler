[←About: invalidField](Error-Explanations/About___--invalidField/#The-Lean-Language-Reference--Error-Explanations--About___--invalidField "About: invalidField")[About: propRecLargeElim→](Error-Explanations/About___--propRecLargeElim/#The-Lean-Language-Reference--Error-Explanations--About___--propRecLargeElim "About: propRecLargeElim")
#  About: `projNonPropFromProp`[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--projNonPropFromProp "Permalink")
Error code: `lean.projNonPropFromProp`
_Tried to project data from a proof._
**Severity:** Error**Since:** 4.23.0
This error occurs when attempting to project a piece of data from a proof of a proposition using an index projection. For example, if `h` is a proof of an existential proposition, attempting to extract the witness `h.1` is an example of this error. Such projections are disallowed because they may violate Lean's prohibition of large elimination from `Prop` (refer to the [Propositions](The-Type-System/Propositions/#propositions) manual section for further details).
Instead of an index projection, consider using a pattern-matching ``Lean.Parser.Term.let : term`
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
``let`, ``Lean.Parser.Term.match : term`
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
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match) expression, or a destructuring tactic like `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")` to eliminate from one propositional type to another. Note that such elimination is only valid if the resulting value is also in `Prop`; if it is not, the error [`lean.propRecLargeElim`](Error-Explanations/About___--propRecLargeElim/#lean___propRecLargeElim) will be raised.
##  Examples[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--projNonPropFromProp--Examples "Permalink")
Attempting to Use Index Projection on Existential Proof
OriginalFixed (let)Fixed (cases)
`example (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (h : ∃ x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"), x > a + 1) : ∃ x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"), x > 0 :=   ⟨`Invalid projection: Cannot project a value of non-propositional type   [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") from the expression   h which has propositional type   [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") x[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") x > a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1`h.1, Nat.lt_of_succ_lt h.2⟩ `
```
Invalid projection: Cannot project a value of non-propositional type
  [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
from the expression
  h
which has propositional type
  [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") x[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") x > a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1
```

`example (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (h : ∃ x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"), x > a + 1) : ∃ x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"), x > a :=   let ⟨w, hw⟩ := h   ⟨w, Nat.lt_of_succ_lt hw⟩ `
`example (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (h : ∃ x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"), x > a + 1) : ∃ x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"), x > a := by   [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") h with   | [intro](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists.intro") w hw =>     [exists](Tactic-Proofs/Tactic-Reference/#exists "Documentation for tactic") w     [omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic") `
The witness associated with a proof of an existential proposition cannot be extracted using an index projection. Instead, it is necessary to use a pattern match: either a term like a ``Lean.Parser.Term.let : term`
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
``let` binding or a tactic like `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")`.
[←About: invalidField](Error-Explanations/About___--invalidField/#The-Lean-Language-Reference--Error-Explanations--About___--invalidField "About: invalidField")[About: propRecLargeElim→](Error-Explanations/About___--propRecLargeElim/#The-Lean-Language-Reference--Error-Explanations--About___--propRecLargeElim "About: propRecLargeElim")

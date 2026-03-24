[←16.5. Case Analysis](The--grind--tactic/Case-Analysis/#grind-split "16.5. Case Analysis")[16.7. Linear Integer Arithmetic→](The--grind--tactic/Linear-Integer-Arithmetic/#cutsat "16.7. Linear Integer Arithmetic")
#  16.6. E‑matching[🔗](find/?domain=Verso.Genre.Manual.section&name=e-matching "Permalink")
_E-matching_ is a procedure for efficiently instantiating quantified theorem statements with ground terms. It is widely employed in SMT solvers, and `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` uses it to instantiate theorems efficiently. It is especially effective when combined with [congruence closure](The--grind--tactic/Congruence-Closure/#--tech-term-Congruence-closure), enabling `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to discover non-obvious consequences of equalities and annotated theorems automatically.
E-matching adds new facts to the metaphorical whiteboard, based on an index of theorems. When the whiteboard contains terms that match the index, the E-matching engine instantiates the corresponding theorems, and the resulting terms can feed further rounds of [congruence closure](The--grind--tactic/Congruence-Closure/#--tech-term-Congruence-closure), [constraint propagation](The--grind--tactic/Constraint-Propagation/#--tech-term-Constraint-propagation), and theory-specific solvers. Each fact added to the whiteboard by E-matching is referred to as an _instance_. Annotating theorems for E-matching, thus adding them to the index, is essential for enabling `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to make effective use of a library.
In addition to user-specified theorems, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` uses automatically generated equations for ``Lean.Parser.Term.match : term``Pattern matching. `match e, ... with | p, ... => f | ...` matches each given term `e` against each pattern `p` of a match alternative. When all patterns of an alternative match, the `match` term evaluates to the value of the corresponding right-hand side `f` with the pattern variables bound to the respective matched values. If used as `match h : e, ... with | p, ... => f | ...`, `h : e = p` is available within `f`.  When not constructing a proof, `match` does not automatically substitute variables matched on in dependent variables' types. Use `match (generalizing := true) ...` to enforce this.  Syntax quotations can also be used in a pattern match. This matches a `Syntax` value against quotations, pattern variables, or `_`.  Quoted identifiers only match identical identifiers - custom matching such as by the preresolved names only should be done explicitly.  `Syntax.atom`s are ignored during matching by default except when part of a built-in literal. For users introducing new atoms, we recommend wrapping them in dedicated syntax kinds if they should participate in matching. For example, in ```lean syntax "c" ("foo" <|> "bar") ... ``` `foo` and `bar` are indistinguishable during matching, but in ```lean syntax foo := "foo" syntax "c" (foo <|> "bar") ... ``` they are not. ``[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match)-expressions as E-matching theorems. Behind the scenes, the [elaborator](Terms/#--tech-term-elaborator) generates auxiliary functions that implement pattern matches, along with equational theorems that specify their behavior. Using these equations with E-matching enables `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to reduce these instances of pattern matching.
##  16.6.1. Patterns[🔗](find/?domain=Verso.Genre.Manual.section&name=e-matching-patterns "Permalink")
The E-matching index is a table of _patterns_. When a term matches one of the patterns in the table, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` attempts to instantiate and apply the corresponding theorem, giving rise to further facts and equalities. Selecting appropriate patterns is an important part of using `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` effectively: if the patterns are too restrictive, then useful theorems may not be applied; if they are too general, performance may suffer.
E-matching Patterns
Consider the following functions and theorems:
`def f (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") :=   a + 1  def g (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") :=   a - 1  @[grind =] theorem gf (x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [g](The--grind--tactic/E___matching/#g-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") ([f](The--grind--tactic/E___matching/#f-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") x) = x := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [g](The--grind--tactic/E___matching/#g-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") ([f](The--grind--tactic/E___matching/#f-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") x) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x   [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [[f](The--grind--tactic/E___matching/#f-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example"), [g](The--grind--tactic/E___matching/#g-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example")]All goals completed! 🐙 `
The theorem `[gf](The--grind--tactic/E___matching/#gf-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example")` asserts that `[g](The--grind--tactic/E___matching/#g-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") ([f](The--grind--tactic/E___matching/#f-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") x) = x` for all natural numbers `x`. The attribute `grind =` instructs `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to use the left-hand side of the equation, `[g](The--grind--tactic/E___matching/#g-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") ([f](The--grind--tactic/E___matching/#f-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") x)`, as a pattern for heuristic instantiation via E-matching.
This proof goal does not include an instance of `[g](The--grind--tactic/E___matching/#g-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") ([f](The--grind--tactic/E___matching/#f-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") x)`, but `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` is nonetheless able to solve it:
`example {a b} (h : [f](The--grind--tactic/E___matching/#f-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") b = a) : [g](The--grind--tactic/E___matching/#g-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") a = b := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")b✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")b:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:[f](The--grind--tactic/E___matching/#f-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a⊢ [g](The--grind--tactic/E___matching/#g-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
Although `[g](The--grind--tactic/E___matching/#g-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") a` is not an instance of the pattern `[g](The--grind--tactic/E___matching/#g-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") ([f](The--grind--tactic/E___matching/#f-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") x)`, it becomes one modulo the equation `[f](The--grind--tactic/E___matching/#f-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") b = a`. By substituting `a` with `[f](The--grind--tactic/E___matching/#f-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") b` in `[g](The--grind--tactic/E___matching/#g-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") a`, we obtain the term `[g](The--grind--tactic/E___matching/#g-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") ([f](The--grind--tactic/E___matching/#f-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") b)`, which matches the pattern `[g](The--grind--tactic/E___matching/#g-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") ([f](The--grind--tactic/E___matching/#f-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") x)` with the assignment `x := b`. Thus, the theorem `[gf](The--grind--tactic/E___matching/#gf-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example")` is instantiated with `x := b`, and the new equality `[g](The--grind--tactic/E___matching/#g-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") ([f](The--grind--tactic/E___matching/#f-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") b) = b` is asserted. `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` then uses congruence closure to derive the implied equality `[g](The--grind--tactic/E___matching/#g-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") a = [g](The--grind--tactic/E___matching/#g-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") ([f](The--grind--tactic/E___matching/#f-_LPAR_in-E-matching-Patterns_RPAR_ "Definition of example") b)` and completes the proof.
[Live ↪](javascript:openLiveLink\("CYUwZgBJAUCGEC4IDlYBcCUiXsQXgCgIJ4BqCARgINEgHMI5tVNncFDj4BaS6gAQDadAE4BLAHbAIeALoE0ACxAB7ESAC2EOjAAebVkgbRIurHgj6OEAEYBPIhADOYjQAcIgsABpt8ggBusOKwNgA2IBAA3vrwNgYAvtQgurDuEdFxCYyK2JDxFrBYRiQytvi2DsSiksBAA"\))
The ``Lean.Parser.Command.grind_pattern```grind_pattern` command can be used to manually select an E-matching pattern for a theorem. Enabling the option `[trace.grind.ematch.instance](The--grind--tactic/E___matching/#trace___grind___ematch___instance "Documentation for option trace.grind.ematch.instance")` causes `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` print a trace message for each theorem instance it generates, which can be helpful when determining E-matching patterns.
syntaxE-matching Pattern Selection

```
command ::= ...
    | The `grind_pattern` command can be used to manually select a pattern for theorem instantiation.
Enabling the option `trace.grind.ematch.instance` causes `grind` to print a trace message for each
theorem instance it generates, which can be helpful when determining patterns.

When multiple patterns are specified together, all of them must match in the current context before
`grind` attempts to instantiate the theorem. This is referred to as a *multi-pattern*.
This is useful for theorems such as transitivity rules, where multiple premises must be simultaneously
present for the rule to apply.

In the following example, `R` is a transitive binary relation over `Int`.
```
opaque R : Int → Int → Prop
axiom Rtrans {x y z : Int} : R x y → R y z → R x z
```
To use the fact that `R` is transitive, `grind` must already be able to satisfy both premises.
This is represented using a multi-pattern:
```
grind_pattern Rtrans => R x y, R y z

example {a b c d} : R a b → R b c → R c d → R a d := by
  grind
```
The multi-pattern `R x y`, `R y z` instructs `grind` to instantiate `Rtrans` only when both `R x y`
and `R y z` are available in the context. In the example, `grind` applies `Rtrans` to derive `R a c`
from `R a b` and `R b c`, and can then repeat the same reasoning to deduce `R a d` from `R a c` and
`R c d`.

You can add constraints to restrict theorem instantiation. For example:
```
grind_pattern extract_extract => (as.extract i j).extract k l where
  as =/= #[]
```
The constraint instructs `grind` to instantiate the theorem only if `as` is **not** definitionally equal
to `#[]`.

## Constraints

- `x =/= term`: The term bound to `x` (one of the theorem parameters) is **not** definitionally equal to `term`.
  The term may contain holes (i.e., `_`).

- `x =?= term`: The term bound to `x` is definitionally equal to `term`.
  The term may contain holes (i.e., `_`).

- `size x < n`: The term bound to `x` has size less than `n`. Implicit arguments
and binder types are ignored when computing the size.

- `depth x < n`: The term bound to `x` has depth less than `n`.

- `is_ground x`: The term bound to `x` does not contain local variables or meta-variables.

- `is_value x`: The term bound to `x` is a value. That is, it is a constructor fully applied to value arguments,
a literal (`Nat`, `Int`, `String`, etc.), or a lambda `fun x => t`.

- `is_strict_value x`: Similar to `is_value`, but without lambdas.

- `not_value x`: The term bound to `x` is a **not** value (see `is_value`).

- `not_strict_value x`: Similar to `not_value`, but without lambdas.

- `gen < n`: The theorem instance has generation less than `n`. Recall that each term is assigned a
generation, and terms produced by theorem instantiation have a generation that is one greater than
the maximal generation of all the terms used to instantiate the theorem. This constraint complements
the `gen` option available in `grind`.

- `max_insts < n`: A new instance is generated only if less than `n` instances have been generated so far.

- `guard e`: The instantiation is delayed until `grind` learns that `e` is `true` in this state.

- `check e`: Similar to `guard e`, but `grind` checks whether `e` is implied by its current state by
assuming `¬ e` and trying to deduce an inconsistency.

## Example

Consider the following example where `f` is a monotonic function
```
opaque f : Nat → Nat
axiom fMono : x ≤ y → f x ≤ f y
```
and you want to instruct `grind` to instantiate `fMono` for every pair of terms `f x` and `f y` when
`x ≤ y` and `x` is **not** definitionally equal to `y`. You can use
```
grind_pattern fMono => f x, f y where
  guard x ≤ y
  x =/= y
```
Then, in the following example, only three instances are generated.
```
/--
trace: [grind.ematch.instance] fMono: a ≤ f a → f a ≤ f (f a)
[grind.ematch.instance] fMono: f a ≤ f (f a) → f (f a) ≤ f (f (f a))
[grind.ematch.instance] fMono: a ≤ f (f a) → f a ≤ f (f (f a))
-/
#guard_msgs in
example : f b = f c → a ≤ f a → f (f a) ≤ f (f (f a)) := by
  set_option trace.grind.ematch.instance true in
  grind
```
`attrKind` matches `("scoped" <|> "local")?`, used before an attribute like `@[local simp]`. grind_pattern ident => term,*
```

Associates a theorem with one or more patterns. When multiple patterns are provided in a single ``Lean.Parser.Command.grind_pattern```grind_pattern` command, _all_ of them must match a term before `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` will attempt to instantiate the theorem.

```
command ::= ...
    | The `grind_pattern` command can be used to manually select a pattern for theorem instantiation.
Enabling the option `trace.grind.ematch.instance` causes `grind` to print a trace message for each
theorem instance it generates, which can be helpful when determining patterns.

When multiple patterns are specified together, all of them must match in the current context before
`grind` attempts to instantiate the theorem. This is referred to as a *multi-pattern*.
This is useful for theorems such as transitivity rules, where multiple premises must be simultaneously
present for the rule to apply.

In the following example, `R` is a transitive binary relation over `Int`.
```
opaque R : Int → Int → Prop
axiom Rtrans {x y z : Int} : R x y → R y z → R x z
```
To use the fact that `R` is transitive, `grind` must already be able to satisfy both premises.
This is represented using a multi-pattern:
```
grind_pattern Rtrans => R x y, R y z

example {a b c d} : R a b → R b c → R c d → R a d := by
  grind
```
The multi-pattern `R x y`, `R y z` instructs `grind` to instantiate `Rtrans` only when both `R x y`
and `R y z` are available in the context. In the example, `grind` applies `Rtrans` to derive `R a c`
from `R a b` and `R b c`, and can then repeat the same reasoning to deduce `R a d` from `R a c` and
`R c d`.

You can add constraints to restrict theorem instantiation. For example:
```
grind_pattern extract_extract => (as.extract i j).extract k l where
  as =/= #[]
```
The constraint instructs `grind` to instantiate the theorem only if `as` is **not** definitionally equal
to `#[]`.

## Constraints

- `x =/= term`: The term bound to `x` (one of the theorem parameters) is **not** definitionally equal to `term`.
  The term may contain holes (i.e., `_`).

- `x =?= term`: The term bound to `x` is definitionally equal to `term`.
  The term may contain holes (i.e., `_`).

- `size x < n`: The term bound to `x` has size less than `n`. Implicit arguments
and binder types are ignored when computing the size.

- `depth x < n`: The term bound to `x` has depth less than `n`.

- `is_ground x`: The term bound to `x` does not contain local variables or meta-variables.

- `is_value x`: The term bound to `x` is a value. That is, it is a constructor fully applied to value arguments,
a literal (`Nat`, `Int`, `String`, etc.), or a lambda `fun x => t`.

- `is_strict_value x`: Similar to `is_value`, but without lambdas.

- `not_value x`: The term bound to `x` is a **not** value (see `is_value`).

- `not_strict_value x`: Similar to `not_value`, but without lambdas.

- `gen < n`: The theorem instance has generation less than `n`. Recall that each term is assigned a
generation, and terms produced by theorem instantiation have a generation that is one greater than
the maximal generation of all the terms used to instantiate the theorem. This constraint complements
the `gen` option available in `grind`.

- `max_insts < n`: A new instance is generated only if less than `n` instances have been generated so far.

- `guard e`: The instantiation is delayed until `grind` learns that `e` is `true` in this state.

- `check e`: Similar to `guard e`, but `grind` checks whether `e` is implied by its current state by
assuming `¬ e` and trying to deduce an inconsistency.

## Example

Consider the following example where `f` is a monotonic function
```
opaque f : Nat → Nat
axiom fMono : x ≤ y → f x ≤ f y
```
and you want to instruct `grind` to instantiate `fMono` for every pair of terms `f x` and `f y` when
`x ≤ y` and `x` is **not** definitionally equal to `y`. You can use
```
grind_pattern fMono => f x, f y where
  guard x ≤ y
  x =/= y
```
Then, in the following example, only three instances are generated.
```
/--
trace: [grind.ematch.instance] fMono: a ≤ f a → f a ≤ f (f a)
[grind.ematch.instance] fMono: f a ≤ f (f a) → f (f a) ≤ f (f (f a))
[grind.ematch.instance] fMono: a ≤ f (f a) → f a ≤ f (f (f a))
-/
#guard_msgs in
example : f b = f c → a ≤ f a → f (f a) ≤ f (f (f a)) := by
  set_option trace.grind.ematch.instance true in
  grind
```
`attrKind` matches `("scoped" <|> "local")?`, used before an attribute like `@[local simp]`. grind_pattern ident => term,* where (isValue
       | isStrictValue
       | notValue
       | notStrictValue
       | isGround
       | sizeLt
       | depthLt
       | genLt
       | maxInsts
       | guard
       | check
       | notDefEq
       | defEq)
```

The optional ``Lean.Parser.Command.grind_pattern```where` clause specifies constraints that must be satisfied before `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` attempts to instantiate the theorem. Each constraint has the form `variable =/= value`, preventing instantiation when the pattern variable would be assigned the specified value. This is useful to avoid unbounded or excessive instantiations with problematic terms.
Selecting Patterns
The `grind =` attribute uses the left side of the equality as the E-matching pattern for `[gf](The--grind--tactic/E___matching/#gf-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example")`:
`def f (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") :=   a + 1  def g (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") :=   a - 1  @[grind =] theorem gf (x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [g](The--grind--tactic/E___matching/#g-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") ([f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") x) = x := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [g](The--grind--tactic/E___matching/#g-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") ([f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") x) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x   [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [[f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example"), [g](The--grind--tactic/E___matching/#g-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example")]All goals completed! 🐙 `
For example, the pattern `g (f x)` is too restrictive in the following case: the theorem `gf` will not be instantiated because the goal does not even contain the function symbol `g`.
In this example, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` fails because the pattern is too restrictive: the goal does not contain the function symbol `[g](The--grind--tactic/E___matching/#g-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example")`.
`example (h₁ : [f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") b = a) (h₂ : [f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") c = a) : b = c := byb:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")c:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h₁:[f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ah₂:[f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a⊢ b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") c   ``grind` failed grindb a c:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h₁:[f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ah₂:[f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ah:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") c⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] [f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
 
    * [prop] [f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a
 
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") c
 
 
  * [eqc] False propositions
    * [prop] b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") c
 
  * [eqc] Equivalence classes
    * [eqc] {a, [f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") b, [f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") c}
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
```
`grind` failed
grindb a c:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h₁:[f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ah₂:[f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ah:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") c⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts

    * [prop] [f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a


    * [prop] [f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a


    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") c




  * [eqc] False propositions
    * [prop] b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") c


  * [eqc] Equivalence classes
    * [eqc] {a, [f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") b, [f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") c}



```

Using just `f x` as the pattern allows `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to solve the goal automatically:
`grind_pattern [gf](The--grind--tactic/E___matching/#gf-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") => [f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") x  example {a b c} (h₁ : [f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") b = a) (h₂ : [f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") c = a) : b = c := bya:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")b:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")c:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h₁:[f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ah₂:[f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a⊢ b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") c   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
Enabling `[trace.grind.ematch.instance](The--grind--tactic/E___matching/#trace___grind___ematch___instance "Documentation for option trace.grind.ematch.instance")` makes it possible to see the equalities found by E-matching:
`example (h₁ : [f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") b = a) (h₂ : [f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") c = a) : b = c := byb:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")c:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h₁:[f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ah₂:[f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") c [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a⊢ b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") c   [set_option](Tactic-Proofs/The-Tactic-Language/#set_option "Documentation for tactic") [trace.grind.ematch.instance](The--grind--tactic/E___matching/#trace___grind___ematch___instance "Documentation for option trace.grind.ematch.instance") [true](Tactic-Proofs/The-Tactic-Language/#set_option "Documentation for tactic") [in](Tactic-Proofs/The-Tactic-Language/#set_option "Documentation for tactic")   `[grind.ematch.instance] [gf](The--grind--tactic/E___matching/#gf-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example"): [g](The--grind--tactic/E___matching/#g-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") ([f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") c) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") c[grind.ematch.instance] [gf](The--grind--tactic/E___matching/#gf-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example"): [g](The--grind--tactic/E___matching/#g-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") ([f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") b) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
```
[grind.ematch.instance] [gf](The--grind--tactic/E___matching/#gf-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example"): [g](The--grind--tactic/E___matching/#g-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") ([f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") c) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") c[grind.ematch.instance] [gf](The--grind--tactic/E___matching/#gf-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example"): [g](The--grind--tactic/E___matching/#g-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") ([f](The--grind--tactic/E___matching/#f-_LPAR_in-Selecting-Patterns_RPAR_ "Definition of example") b) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b
```

After E-matching, the proof succeeds because congruence closure equates `g (f c)` with `g (f b)`, because both `f b` and `f c` are equal to `a`. Thus, `b` and `c` must be in the same equivalence class.
[Live ↪](javascript:openLiveLink\("CYUwZgBJAUCGEC4IDlYBcCUiXsQXgCgIJ4BqCARgINEgHMI5tVNncFDj4BaS6gAQDadAE4BLAHbAIeALoE0ACxAB7ESAC2EOjAAebVkgbRIurHgj6OEAEYBPIhADOYjQAcIgsABpt8gqKSwAD6buhoICIS2pB4AHxQltQgurDuADYgEADe8DYQAMYAvoyKgIEE2JD5FrBY0IqAQQSVhTIkWEjVLdb2joFSyakZWfUVSFWttaVNYy017batBfi2DsROIGjBKm5oYirRaCKwBSAAdH3Ap5roBYqnkk5osBInEIcArlmSveJSQA"\))
When multiple patterns are specified together, all of them must match in the current context before `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` attempts to instantiate the theorem. This is referred to as a _multi-pattern_. This is useful for lemmas such as transitivity rules, where multiple premises must be simultaneously present for the rule to apply. A single theorem may be associated with multiple separate patterns by using multiple invocations of ``Lean.Parser.Command.grind_pattern```grind_pattern` or the `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind _=_[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")` attribute. If _any_ of these separate patterns match, the theorem will be instantiated.
Multi-Patterns
`[R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example")` is a transitive binary relation over `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`:
`opaque R : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → Prop [axiom](Axioms/#Lean___Parser___Command___axiom-next "Documentation for syntax") Rtrans {x y z : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")} : [R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") x y → [R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") y z → [R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") x z `
To use the fact that `[R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example")` is transitive, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` must already be able to satisfy both premises. This is represented using a [multi-pattern](The--grind--tactic/E___matching/#--tech-term-multi-pattern):
`grind_pattern [Rtrans](The--grind--tactic/E___matching/#Rtrans-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") => [R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") x y, [R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") y z  example {a b c d} : [R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") a b → [R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") b c → [R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") c d → [R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") a d := bya:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")b:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")c:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")d:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ [R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") a b → [R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") b c → [R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") c d → [R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") a d   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
The multi-pattern `R x y, R y z` instructs `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to instantiate `[Rtrans](The--grind--tactic/E___matching/#Rtrans-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example")` only when both `[R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") x y` and `[R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") y z` are available in the context. In the example, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` applies `[Rtrans](The--grind--tactic/E___matching/#Rtrans-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example")` to derive `[R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") a c` from `[R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") a b` and `[R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") b c`, and can then repeat the same reasoning to deduce `[R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") a d` from `[R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") a c` and `[R](The--grind--tactic/E___matching/#R-_LPAR_in-Multi-Patterns_RPAR_ "Definition of example") c d`.
[Live ↪](javascript:openLiveLink\("PYBwhgjgrgpgBAJTgLjgSQHYBc6CTCd2ecACgE6gBQYAHgJbAC2iWpYGAznAN7VwCecAF4oCWAL4ikvAfiQDhsuL0EUKAc1K0MAEwD64LFhikMzVhzgBeAHyIl/ADR35qmNTAMQAG3hcwcACM4AGM4bQlUJH8gxSDQxVDtIiiwlEtAvgo4OA0tbVUANzBNMACfbmkhOGiQ1NRMcSA"\))
Pattern Constraints
Certain combinations of theorems can lead to unbounded instantiation, where E-matching repeatedly generates longer and longer terms. Consider theorems about `[List.flatMap](Basic-Types/Linked-Lists/#List___flatMap "Documentation for List.flatMap")` and `[List.reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse")`. If `List.flatMap_def`, `List.flatMap_reverse`, and `List.reverse_flatMap` are all annotated with `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind =[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")`, then as soon as `List.flatMap_reverse` is instantiated, the following chain of instantiations occurs, creating progressively longer function compositions with `[List.reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse")`. This can be observed using the `#grind_lint` command:

```
attribute [local grind =] List.reverse_flatMap

set_option trace.grind.ematch.instance true in
#grind_lint inspect List.flatMap_reverse

```

The trace output shows the unbounded instantiation:

```
[grind.ematch.instance] List.flatMap_def: List.flatMap (List.reverse ∘ f) l = (List.map (List.reverse ∘ f) l).flatten
[grind.ematch.instance] List.flatMap_def: List.flatMap f l.reverse = (List.map f l.reverse).flatten
[grind.ematch.instance] List.flatMap_reverse: List.flatMap f l.reverse = (List.flatMap (List.reverse ∘ f) l).reverse
[grind.ematch.instance] List.reverse_flatMap: (List.flatMap (List.reverse ∘ f) l).reverse =
  List.flatMap (List.reverse ∘ List.reverse ∘ f) l.reverse
[grind.ematch.instance] List.flatMap_def: List.flatMap (List.reverse ∘ List.reverse ∘ f) l.reverse =
  (List.map (List.reverse ∘ List.reverse ∘ f) l.reverse).flatten

```

This pattern continues indefinitely, with each iteration adding another `[List.reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse")` to the composition. The ``Lean.Parser.Command.grind_pattern```where` clause prevents this by excluding problematic instantiations:

```
grind_pattern reverse_flatMap => (l.flatMap f).reverse where
  f =/= List.reverse ∘ _

```

This instructs `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to use the pattern `(l.flatMap f).reverse`, but only when `f` is not a composition with `[List.reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse")`, preventing the unbounded chain of instantiations.
You can use `#grind_lint check` to look for problematic patterns, or `#grind_lint check in List` or `#grind_lint check in module Std.Data` to look in specific namespaces or modules.
The `grind` attribute automatically generates an E-matching pattern or multi-pattern using a heuristic, instead of using ``Lean.Parser.Command.grindPattern : command``The `grind_pattern` command can be used to manually select a pattern for theorem instantiation. Enabling the option `trace.grind.ematch.instance` causes `grind` to print a trace message for each theorem instance it generates, which can be helpful when determining patterns.  When multiple patterns are specified together, all of them must match in the current context before `grind` attempts to instantiate the theorem. This is referred to as a *multi-pattern*. This is useful for theorems such as transitivity rules, where multiple premises must be simultaneously present for the rule to apply.  In the following example, `R` is a transitive binary relation over `Int`. ``` opaque R : Int → Int → Prop axiom Rtrans {x y z : Int} : R x y → R y z → R x z ``` To use the fact that `R` is transitive, `grind` must already be able to satisfy both premises. This is represented using a multi-pattern: ``` grind_pattern Rtrans => R x y, R y z  example {a b c d} : R a b → R b c → R c d → R a d := by   grind ``` The multi-pattern `R x y`, `R y z` instructs `grind` to instantiate `Rtrans` only when both `R x y` and `R y z` are available in the context. In the example, `grind` applies `Rtrans` to derive `R a c` from `R a b` and `R b c`, and can then repeat the same reasoning to deduce `R a d` from `R a c` and `R c d`.  You can add constraints to restrict theorem instantiation. For example: ``` grind_pattern extract_extract => (as.extract i j).extract k l where   as =/= #[] ``` The constraint instructs `grind` to instantiate the theorem only if `as` is **not** definitionally equal to `#[]`.  ## Constraints  - `x =/= term`: The term bound to `x` (one of the theorem parameters) is **not** definitionally equal to `term`.   The term may contain holes (i.e., `_`).  - `x =?= term`: The term bound to `x` is definitionally equal to `term`.   The term may contain holes (i.e., `_`).  - `size x < n`: The term bound to `x` has size less than `n`. Implicit arguments and binder types are ignored when computing the size.  - `depth x < n`: The term bound to `x` has depth less than `n`.  - `is_ground x`: The term bound to `x` does not contain local variables or meta-variables.  - `is_value x`: The term bound to `x` is a value. That is, it is a constructor fully applied to value arguments, a literal (`Nat`, `Int`, `String`, etc.), or a lambda `fun x => t`.  - `is_strict_value x`: Similar to `is_value`, but without lambdas.  - `not_value x`: The term bound to `x` is a **not** value (see `is_value`).  - `not_strict_value x`: Similar to `not_value`, but without lambdas.  - `gen < n`: The theorem instance has generation less than `n`. Recall that each term is assigned a generation, and terms produced by theorem instantiation have a generation that is one greater than the maximal generation of all the terms used to instantiate the theorem. This constraint complements the `gen` option available in `grind`.  - `max_insts < n`: A new instance is generated only if less than `n` instances have been generated so far.  - `guard e`: The instantiation is delayed until `grind` learns that `e` is `true` in this state.  - `check e`: Similar to `guard e`, but `grind` checks whether `e` is implied by its current state by assuming `¬ e` and trying to deduce an inconsistency.  ## Example  Consider the following example where `f` is a monotonic function ``` opaque f : Nat → Nat axiom fMono : x ≤ y → f x ≤ f y ``` and you want to instruct `grind` to instantiate `fMono` for every pair of terms `f x` and `f y` when `x ≤ y` and `x` is **not** definitionally equal to `y`. You can use ``` grind_pattern fMono => f x, f y where   guard x ≤ y   x =/= y ``` Then, in the following example, only three instances are generated. ``` /-- trace: [grind.ematch.instance] fMono: a ≤ f a → f a ≤ f (f a) [grind.ematch.instance] fMono: f a ≤ f (f a) → f (f a) ≤ f (f (f a)) [grind.ematch.instance] fMono: a ≤ f (f a) → f a ≤ f (f (f a)) -/ #guard_msgs in example : f b = f c → a ≤ f a → f (f a) ≤ f (f (f a)) := by   set_option trace.grind.ematch.instance true in   grind ``` ```grind_pattern` to explicitly specify a pattern. It includes a number of variants that select different heuristics. The `grind?` attribute displays an info message showing the pattern which was selected—this is very helpful for debugging!
Patterns are subexpressions of theorem statements. A subexpression is _indexable_ if it has an indexable constant as its head, and it is said to _cover_ one of the theorem's arguments if it fixes the argument's value. Indexable constants are all constants other than `[Eq](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")`, `[HEq](Basic-Propositions/Propositional-Equality/#HEq___refl "Documentation for HEq")`, `[Iff](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff")`, `[And](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And")`, `[Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or")`, and `[Not](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")`. The set of arguments that are covered by a pattern or multi-pattern is referred to as its _coverage_. Some constants are lower priority than others; in particular, the arithmetic operators `[HAdd.hAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")`, `[HSub.hSub](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")`, `[HMul.hMul](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")`, `[Dvd.dvd](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd")`, `[HDiv.hDiv](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv.hDiv")`, and `[HMod.hMod](Type-Classes/Basic-Classes/#HMod___mk "Documentation for HMod.hMod")` have low priority. An indexable subexpression is _minimal_ if there is no smaller indexable subexpression whose head constant has at least as high priority.
attributeGrind Patterns
When the `grind` attribute is added to a definition, it causes `grind` to unfold that definition to its body whenever it is encountered. When using the module system, if the body of the definition is not visible (e.g. via `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")expose[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")`), then the `grind` attribute is ignored.

```
attr ::= ...
    | Marks a theorem or definition for use by the `grind` tactic.

An optional modifier (e.g. `=`, `→`, `←`, `cases`, `intro`, `ext`, `inj`, etc.)
controls how `grind` uses the declaration:
* whether it is applied forwards, backwards, or both,
* whether equalities are used on the left, right, or both sides,
* whether case-splits, constructors, extensionality, or injectivity are applied,
* or whether custom instantiation patterns are used.

See the individual modifier docstrings for details.
grind grindMod?
```

The `grind` attribute automatically generates an E-matching pattern for a theorem, using a strategy determined by the provided modifier. If no modifier is provided, then `grind` suggests suitable modifiers, displaying the resulting patterns.

```
attr ::= ...
    | Like `@[grind]`, but enforces the **minimal indexable subexpression condition**:
when several subterms cover the same free variables, `grind!` chooses the smallest one.

This influences E-matching pattern selection.

### Example
```lean
theorem fg_eq (h : x > 0) : f (g x) = x

@[grind <-] theorem fg_eq (h : x > 0) : f (g x) = x
-- Pattern selected: `f (g x)`

-- With minimal subexpression:
@[grind! <-] theorem fg_eq (h : x > 0) : f (g x) = x
-- Pattern selected: `g x`
```
grind! grindMod?
```

The `grind!` attribute automatically generates an E-matching pattern for a theorem, using a strategy determined by the provided modifier. It additionally enforces the condition that the selected pattern(s) should be minimal indexable subexpressions.

```
attr ::= ...
    | Like `@[grind]`, but also prints the pattern(s) selected by `grind`
as info messages. Useful for debugging annotations and modifiers.
grind? grindMod?
```

The `grind?` displays the pattern that was generated.

```
attr ::= ...
    | Like `@[grind!]`, but also prints the pattern(s) selected by `grind`
as info messages. Combines minimal subexpression selection with debugging output.
grind!? grindMod?
```

The `grind!?` attribute is equivalent to `grind!`, except it displays the resulting pattern for inspection.
Without any modifier, `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")` traverses the conclusion and then the hypotheses from left to right, adding patterns as they increase the coverage, stopping when all arguments are covered. This default strategy can be explicitly requested using the ``Lean.Parser.Attr.grindDef``The `.` modifier instructs `grind` to select a multi-pattern by traversing the conclusion of the theorem, and then the hypotheses from left to right. We say this is the default modifier. Each time it encounters a subexpression which covers an argument which was not previously covered, it adds that subexpression as a pattern, until all arguments have been covered. If `grind!` is used, then only minimal indexable subexpressions are considered. ```.` modifier. In addition to using the default strategy, the attribute checks which other strategies could be applied, and displays all of the resulting patterns.
syntaxDefault Pattern

```
grindMod ::= ...
    | The `.` modifier instructs `grind` to select a multi-pattern by traversing the conclusion of the
theorem, and then the hypotheses from left to right. We say this is the default modifier.
Each time it encounters a subexpression which covers an argument which was not
previously covered, it adds that subexpression as a pattern, until all arguments have been covered.
If `grind!` is used, then only minimal indexable subexpressions are considered.
.
```

```
grindMod ::= ...
    | The `.` modifier instructs `grind` to select a multi-pattern by traversing the conclusion of the
theorem, and then the hypotheses from left to right. We say this is the default modifier.
Each time it encounters a subexpression which covers an argument which was not
previously covered, it adds that subexpression as a pattern, until all arguments have been covered.
If `grind!` is used, then only minimal indexable subexpressions are considered.
·
```

The `[.](Tactic-Proofs/The-Tactic-Language/#___ "Documentation for tactic")` modifier instructs `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to select a multi-pattern by traversing the conclusion of the theorem, and then the hypotheses from left to right. We say this is the default modifier. Each time it encounters a subexpression which covers an argument which was not previously covered, it adds that subexpression as a pattern, until all arguments have been covered. If `[grind!](The--grind--tactic/E___matching/#Lean___Parser___Attr___grind___ "Documentation for syntax")` is used, then only minimal indexable subexpressions are considered.
syntaxEquality Rewrites

```
grindMod ::= ...
    | The `=` modifier instructs `grind` to check that the conclusion of the theorem is an equality,
and then uses the left-hand side of the equality as a pattern. This may fail if not all of the arguments appear
in the left-hand side.
=
```

The `=` modifier instructs `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to check that the conclusion of the theorem is an equality, and then uses the left-hand side of the equality as a pattern. This may fail if not all of the arguments appear in the left-hand side.
syntaxBackward Equality Rewrites

```
grindMod ::= ...
    | The `=_` modifier instructs `grind` to check that the conclusion of the theorem is an equality,
and then uses the right-hand side of the equality as a pattern. This may fail if not all of the arguments appear
in the right-hand side.
=_
```

The `=_` modifier instructs `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to check that the conclusion of the theorem is an equality, and then uses the right-hand side of the equality as a pattern. This may fail if not all of the arguments appear in the right-hand side.
syntaxBidirectional Equality Rewrites

```
grindMod ::= ...
    | The `_=_` modifier acts like a macro which expands to `=` and `=_`.  It adds two patterns,
allowing the equality theorem to trigger in either direction.
_=_
```

The `_=_` modifier acts like a macro which expands to `=` and `=_`. It adds two patterns, allowing the equality theorem to trigger in either direction.
syntaxForward Reasoning

```
grindMod ::= ...
    | The `→` modifier instructs `grind` to select a multi-pattern from the hypotheses of the theorem.
In other words, `grind` will use the theorem for forwards reasoning.
To generate a pattern, it traverses the hypotheses of the theorem from left to right.
Each time it encounters a subexpression which covers an argument which was not
previously covered, it adds that subexpression as a pattern, until all arguments have been covered.
If `grind!` is used, then only minimal indexable subexpressions are considered.
→
```

The `→` modifier instructs `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to select a multi-pattern from the hypotheses of the theorem. In other words, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` will use the theorem for forwards reasoning. To generate a pattern, it traverses the hypotheses of the theorem from left to right. Each time it encounters a subexpression which covers an argument which was not previously covered, it adds that subexpression as a pattern, until all arguments have been covered. If `[grind!](The--grind--tactic/E___matching/#Lean___Parser___Attr___grind___ "Documentation for syntax")` is used, then only minimal indexable subexpressions are considered.
syntaxBackward Reasoning

```
grindMod ::= ...
    | The `←` modifier instructs `grind` to select a multi-pattern from the conclusion of theorem.
In other words, `grind` will use the theorem for backwards reasoning.
This may fail if not all of the arguments to the theorem appear in the conclusion.
Each time it encounters a subexpression which covers an argument which was not
previously covered, it adds that subexpression as a pattern, until all arguments have been covered.
If `grind!` is used, then only minimal indexable subexpressions are considered.
←
```

The `←` modifier instructs `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to select a multi-pattern from the conclusion of theorem. In other words, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` will use the theorem for backwards reasoning. This may fail if not all of the arguments to the theorem appear in the conclusion. Each time it encounters a subexpression which covers an argument which was not previously covered, it adds that subexpression as a pattern, until all arguments have been covered. If `[grind!](The--grind--tactic/E___matching/#Lean___Parser___Attr___grind___ "Documentation for syntax")` is used, then only minimal indexable subexpressions are considered.
It is important to inspect the patterns generated by the `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")` attribute to ensure that they match the correct parts of the lemma. If the pattern is too strict, the lemma will not be applied in situations where it would be relevant, leading to less automation. If it is too general, then performance will suffer as the lemma is tried in many situations where it is not helpful.
There are also three less commonly used modifiers for lemmas:
syntaxLeft-to-Right Traversal

```
grindMod ::= ...
    | The `⇒` modifier instructs `grind` to select a multi-pattern by traversing all the hypotheses from
left to right, followed by the conclusion.
Each time it encounters a subexpression which covers an argument which was not
previously covered, it adds that subexpression as a pattern, until all arguments have been covered.
If `grind!` is used, then only minimal indexable subexpressions are considered.
=>
```

```
grindMod ::= ...
    | The `⇒` modifier instructs `grind` to select a multi-pattern by traversing all the hypotheses from
left to right, followed by the conclusion.
Each time it encounters a subexpression which covers an argument which was not
previously covered, it adds that subexpression as a pattern, until all arguments have been covered.
If `grind!` is used, then only minimal indexable subexpressions are considered.
⇒
```

The `⇒` modifier instructs `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to select a multi-pattern by traversing all the hypotheses from left to right, followed by the conclusion. Each time it encounters a subexpression which covers an argument which was not previously covered, it adds that subexpression as a pattern, until all arguments have been covered. If `[grind!](The--grind--tactic/E___matching/#Lean___Parser___Attr___grind___ "Documentation for syntax")` is used, then only minimal indexable subexpressions are considered.
syntaxRight-to-Left Traversal

```
grindMod ::= ...
    | The `⇐` modifier instructs `grind` to select a multi-pattern by traversing the conclusion, and then
all the hypotheses from right to left.
Each time it encounters a subexpression which covers an argument which was not
previously covered, it adds that subexpression as a pattern, until all arguments have been covered.
If `grind!` is used, then only minimal indexable subexpressions are considered.
<=
```

```
grindMod ::= ...
    | The `⇐` modifier instructs `grind` to select a multi-pattern by traversing the conclusion, and then
all the hypotheses from right to left.
Each time it encounters a subexpression which covers an argument which was not
previously covered, it adds that subexpression as a pattern, until all arguments have been covered.
If `grind!` is used, then only minimal indexable subexpressions are considered.
⇐
```

The `⇐` modifier instructs `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to select a multi-pattern by traversing the conclusion, and then all the hypotheses from right to left. Each time it encounters a subexpression which covers an argument which was not previously covered, it adds that subexpression as a pattern, until all arguments have been covered. If `[grind!](The--grind--tactic/E___matching/#Lean___Parser___Attr___grind___ "Documentation for syntax")` is used, then only minimal indexable subexpressions are considered.
syntaxBackward Reasoning on Equality

```
grindMod ::= ...
    | The `←=` modifier is unlike the other `grind` modifiers, and it used specifically for
backwards reasoning on equality. When a theorem's conclusion is an equality proposition and it
is annotated with `@[grind ←=]`, grind `will` instantiate it whenever the corresponding disequality
is assumed—this is a consequence of the fact that grind performs all proofs by contradiction.
Ordinarily, the grind attribute does not consider the `=` symbol when generating patterns.
←=
```

The `←=` modifier is unlike the other `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` modifiers, and it used specifically for backwards reasoning on equality. When a theorem's conclusion is an equality proposition and it is annotated with `@[grind ←=]`, grind `will` instantiate it whenever the corresponding disequality is assumed—this is a consequence of the fact that grind performs all proofs by contradiction. Ordinarily, the grind attribute does not consider the `=` symbol when generating patterns.
The `@[grind ←=]` Attribute
When attempting to prove that `a⁻¹ = b`, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` uses `[inv_eq](The--grind--tactic/E___matching/#inv_eq-_LPAR_in-The--____LSQ_grind-_______RSQ_--Attribute_RPAR_ "Definition of example")` due to the `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind ←=[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")` annotation.
`@[grind ←=] theorem `declaration uses `sorry``inv_eq [One α] [[Mul](Type-Classes/Basic-Classes/#Mul___mk "Documentation for Mul") α] [Inv α] {a b : α} (w : a * b = 1) : a⁻¹ = b := sorry `
[Live ↪](javascript:openLiveLink\("G4QwTgliBGA2CmACA3oRuAC+KSOogXIhogNoCSAdsIQLoBQtAAsQOaTkAmigCYQC8dALgAt4AezDwAtogiUA+vACOJAPLkkqaiQCyAV1g0SFKhqw58hdLUTXEACgDu57ACozPRAEYAlE8DeBAE7Ed1w8HitEAGcxMABPIA"\))
syntaxFunction-Valued Congruence Closure

```
grindMod ::= ...
    | The `funCC` modifier marks global functions that support **function-valued congruence closure**.
Given an application `f a₁ a₂ … aₙ`, when `funCC := true`,
`grind` generates and tracks equalities for all partial applications:
- `f a₁`
- `f a₁ a₂`
- `…`
- `f a₁ a₂ … aₙ`
funCC
```

The `funCC` modifier marks global functions that support **function-valued congruence closure**. Given an application `f a₁ a₂ … aₙ`, when `funCC := true`, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` generates and tracks equalities for all partial applications:
  * `f a₁`
  * `f a₁ a₂`
  * `…`
  * `f a₁ a₂ … aₙ`


Some additional modifiers can be used to add other kinds of lemmas to the index. This includes extensionality theorems, injectivity theorems for functions, and a shortcut to add all constructors of an inductively defined predicate to the index.
syntaxExtensionality

```
grindMod ::= ...
    | The `ext` modifier marks extensionality theorems for use by `grind`.
For example, the standard library marks `funext` with this attribute.

Whenever `grind` encounters a disequality `a ≠ b`, it attempts to apply any
available extensionality theorems whose matches the type of `a` and `b`.
ext
```

The `[ext](Tactic-Proofs/Tactic-Reference/#ext "Documentation for tactic")` modifier marks extensionality theorems for use by `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")`. For example, the standard library marks `[funext](The-Type-System/Functions/#funext "Documentation for funext")` with this attribute.
Whenever `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` encounters a disequality `a ≠ b`, it attempts to apply any available extensionality theorems whose matches the type of `a` and `b`.
In addition, adding `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind ext[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")` to a structure registers a its extensionality theorem.
The `@[grind ext]` Attribute
`[Point](The--grind--tactic/E___matching/#Point-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")` is a structure with two fields:
`structure Point where   x : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")   y : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") `
By default, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` can solve goals like this one, because definitional equality includes [η-equivalence](The-Type-System/#--tech-term-___-equivalence) for product types:
`example (p : [Point](The--grind--tactic/E___matching/#Point-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")) : p = ⟨p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")⟩ := byp:[Point](The--grind--tactic/E___matching/#Point-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")⊢ p [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") } [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
However, it can't solve goals like this one that require an appeal to propositional equalities:
`example (p : [Point](The--grind--tactic/E___matching/#Point-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")) (a : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : a = p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") → p = ⟨a, p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")⟩ := byp:[Point](The--grind--tactic/E___matching/#Point-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")a:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") → p [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := a, [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") } ``grind` failed grindp:[Point](The--grind--tactic/E___matching/#Point-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")a:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")h:a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")h_1:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")p [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := a, [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")
 
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")p [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := a, [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }
 
 
  * [eqc] False propositions
    * [prop] p [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := a, [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }
 
  * [eqc] Equivalence classes
    * [eqc] {a, p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")}
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
```
`grind` failed
grindp:[Point](The--grind--tactic/E___matching/#Point-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")a:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")h:a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")h_1:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")p [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := a, [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts

    * [prop] a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")


    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")p [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := a, [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }




  * [eqc] False propositions
    * [prop] p [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := a, [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }


  * [eqc] Equivalence classes
    * [eqc] {a, p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")}



```

This kind of goal may come up when proving theorems like the fact that swapping the fields of a point twice is the identity:
`def Point.swap (p : [Point](The--grind--tactic/E___matching/#Point-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")) : [Point](The--grind--tactic/E___matching/#Point-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := ⟨p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")⟩ ``theorem swap_swap_eq_id : [Point.swap](The--grind--tactic/E___matching/#Point___swap-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") ∘ [Point.swap](The--grind--tactic/E___matching/#Point___swap-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") = id := by⊢ [Point.swap](The--grind--tactic/E___matching/#Point___swap-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") [∘](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [Point.swap](The--grind--tactic/E___matching/#Point___swap-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id   [unfold](Tactic-Proofs/Tactic-Reference/#unfold "Documentation for tactic") [Point.swap](The--grind--tactic/E___matching/#Point___swap-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")⊢ [(](The-Type-System/Functions/#Function___comp "Documentation for Function.comp")(fun p => { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }) [∘](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") fun p => { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }[)](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id   ``grind` failed grindh:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[(](The-Type-System/Functions/#Function___comp "Documentation for Function.comp")(fun p => { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }) [∘](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") fun p => { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }[)](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") idw:[Point](The--grind--tactic/E___matching/#Point-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")h_1:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not"){ [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := w.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := w.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") } [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id w⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[(](The-Type-System/Functions/#Function___comp "Documentation for Function.comp")(fun p => { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }) [∘](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") fun p => { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }[)](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id
 
    * [prop] [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") x[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not"){ [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := x.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := x.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") } [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id x
 
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not"){ [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := w.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := w.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") } [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id w
 
    * [prop] id w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") w
 
 
  * [eqc] True propositions
    * [prop] [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") x[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not"){ [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := x.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := x.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") } [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id x
 
  * [eqc] False propositions 
    * [prop] [(](The-Type-System/Functions/#Function___comp "Documentation for Function.comp")(fun p => { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }) [∘](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") fun p => { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }[)](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id
 
    * [prop] { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := w.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := w.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") } [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id w
 
 
  * [eqc] Equivalence classes
    * [eqc] {w, id w}
 
  * [cases] Case analyses
    * [cases] [1/1]: [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") x[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not"){ [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := x.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := x.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") } [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id x
      * [cases] source: Extensionality `funext`
 
  * [ematch] E-matching patterns
    * [thm] id.eq_1: [@id #1 #0]
 
 [grind] Diagnostics
  * [thm] E-Matching instances
    * [thm] id.eq_1 ↦ 1

`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
```
`grind` failed
grindh:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[(](The-Type-System/Functions/#Function___comp "Documentation for Function.comp")(fun p => { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }) [∘](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") fun p => { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }[)](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") idw:[Point](The--grind--tactic/E___matching/#Point-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")h_1:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not"){ [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := w.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := w.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") } [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id w⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts

    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[(](The-Type-System/Functions/#Function___comp "Documentation for Function.comp")(fun p => { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }) [∘](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") fun p => { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }[)](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id


    * [prop] [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") x[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not"){ [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := x.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := x.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") } [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id x


    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not"){ [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := w.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := w.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") } [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id w


    * [prop] id w [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") w




  * [eqc] True propositions
    * [prop] [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") x[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not"){ [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := x.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := x.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") } [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id x


  * [eqc] False propositions

    * [prop] [(](The-Type-System/Functions/#Function___comp "Documentation for Function.comp")(fun p => { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }) [∘](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") fun p => { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }[)](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id


    * [prop] { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := w.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := w.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") } [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id w




  * [eqc] Equivalence classes
    * [eqc] {w, id w}


  * [cases] Case analyses
    * [cases] [1/1]: [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") x[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not"){ [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := x.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := x.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") } [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id x
      * [cases] source: Extensionality `funext`


  * [ematch] E-matching patterns
    * [thm] id.eq_1: [@id #1 #0]



[grind] Diagnostics
  * [thm] E-Matching instances
    * [thm] id.eq_1 ↦ 1


```

Adding the `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind ext[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")` attribute to `[Point](The--grind--tactic/E___matching/#Point-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")` enables `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to solve both the original example and prove this theorem:
`[attribute](Attributes/#Lean___Parser___Command___attribute "Documentation for syntax") [grind ext] [Point](The--grind--tactic/E___matching/#Point-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")  example (p : [Point](The--grind--tactic/E___matching/#Point-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")) (a : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : a = p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") → p = ⟨a, p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")⟩ := byp:[Point](The--grind--tactic/E___matching/#Point-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")a:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") → p [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := a, [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  theorem swap_swap_eq_id' : [Point.swap](The--grind--tactic/E___matching/#Point___swap-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") ∘ [Point.swap](The--grind--tactic/E___matching/#Point___swap-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") = id := by⊢ [Point.swap](The--grind--tactic/E___matching/#Point___swap-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") [∘](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [Point.swap](The--grind--tactic/E___matching/#Point___swap-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id   [unfold](Tactic-Proofs/Tactic-Reference/#unfold "Documentation for tactic") [Point.swap](The--grind--tactic/E___matching/#Point___swap-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example")⊢ [(](The-Type-System/Functions/#Function___comp "Documentation for Function.comp")(fun p => { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }) [∘](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") fun p => { [x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example"), [y](The--grind--tactic/E___matching/#Point___y-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") := p.[x](The--grind--tactic/E___matching/#Point___x-_LPAR_in-The--____LSQ_grind-ext_RSQ_--Attribute_RPAR_ "Definition of example") }[)](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") id   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgAoHsCWA7EiDuALeBAKEUQA9EAuRASW1MQE9q6Hj5yBDAWwAcANkgAUfVmiwgAlKzEBeRIAvyPgDpyAGkSqmgS/JqCgEYsA5mCwATYsXPwAZigzYVwXFzGjxj6Z8n6l2zVVyHSsuEHB0AwgQJABtUwtEThAAXQdJK05eQRExGglsGWEuVnpvGhKFIMRAJMItRAVFLkCVXT8jRgTMS2IQQlQEHkQXNwB9Eb5R+ABHUfRzAHIfJwnEQAwidJXXeUR59qZGCExbVAFzTZBnbc6zbqA"\))
syntaxInjectivity

```
grindMod ::= ...
    | The `inj` modifier marks injectivity theorems for use by `grind`.
The conclusion of the theorem must be of the form `Function.Injective f`
where the term `f` contains at least one constant symbol.
inj
```

The `inj` modifier marks injectivity theorems for use by `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")`. The conclusion of the theorem must be of the form `[Function.Injective](The-Type-System/Functions/#Function___Injective "Documentation for Function.Injective") f` where the term `f` contains at least one constant symbol.
Injectivity Patterns
This function `[double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example")` doubles its argument:
`def double (x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := x + x `
By default, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` cannot prove the following theorem:
`theorem A {n k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} :     [double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example") (n + 5) = [double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example") (k - 3) →     n + 8 = k := byn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 5[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 3[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") → n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 8 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k   ``grind` failed grind.1n k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:[double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 5[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 3[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")h_1:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 8 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") kh_2:-1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 3 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] [double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 5[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 3[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")
 
    * [prop] [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 3[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") if -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 3 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0 then [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -3 else 0
 
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 8 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k
 
    * [prop] -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 3 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
 
  * [eqc] True propositions
    * [prop] -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 3 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
  * [eqc] False propositions
    * [prop] n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 8 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k
 
  * [eqc] Equivalence classes 
    * [eqc] {[double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 5[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd"), [double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 3[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")}
 
    * [eqc] others
      * [eqc] {[↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 3[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub"), if -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 3 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0 then [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -3 else 0, [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -3}
 
 
  * [cases] Case analyses
    * [cases] [1/2]: if -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 3 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0 then [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -3 else 0
      * [cases] source: Initial goal
 
  * [cutsat] Assignment satisfying linear constraints 
    * [assign] n := 0
 
    * [assign] k := 3
 
    * [assign] [double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 5[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") := 1
 
    * [assign] [double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 3[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") := 1
 
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
However, `[double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example")` is injective, and this fact can be registered for `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` using the `grind inj` attribute:
`@[grind inj] theorem double_inj : [Function.Injective](The-Type-System/Functions/#Function___Injective "Documentation for Function.Injective") [double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example") := by⊢ [Function.Injective](The-Type-System/Functions/#Function___Injective "Documentation for Function.Injective") [double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example")   [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") only [[double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example"), [Function.Injective](The-Type-System/Functions/#Function___Injective "Documentation for Function.Injective")]⊢ ∀ ⦃a₁ a₂ : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⦄, a₁ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a₁ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a₂ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a₂ → a₁ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a₂   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
This injectivity lemma suffices to prove the theorem:
`theorem B {n k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} :     [double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example") (n + 5) = [double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example") (k - 3) →     n + 8 = k := byn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 5[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [double](The--grind--tactic/E___matching/#double-_LPAR_in-Injectivity-Patterns_RPAR_ "Definition of example") [(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 3[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") → n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 8 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("CYUwZgBMD2CuBGAbEEAUAPCAuCA5AhgC4CU2eR2AvBJgNQ0BQDAAgNoDmATgJYB2wEPgCsAug0IALENE4gAtlDhIQAfWFkAYrF4BjQt2i8AdAEleQkHu4A3FDATIqEeAE8GECAGducgA4RDRBcIVntlABoILV19Q1NzS31bMQ8uPmAmSWlZBQAhCABvXggAazICQgBfbHcPRQcUVGL6AFZSajDHVDKAWggAZlJAJMJaj2aIAA4IajKsaldatP4gA"\))
syntaxConstructor Patterns

```
grindMod ::= ...
    | The `intro` modifier instructs `grind` to use the constructors (introduction rules)
of an inductive predicate as E-matching theorems.Example:
```
inductive Even : Nat → Prop where
| zero : Even 0
| add2 : Even x → Even (x + 2)

attribute [grind intro] Even
example (h : Even x) : Even (x + 6) := by grind
example : Even 0 := by grind
```
Here `attribute [grind intro] Even` acts like a macro that expands to
`attribute [grind] Even.zero` and `attribute [grind] Even.add2`.
This is especially convenient for inductive predicates with many constructors.
intro
```

The `[intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic")` modifier instructs `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to use the constructors (introduction rules) of an inductive predicate as E-matching theorems.Example:
`inductive [Even](Introduction/#Even___zero-next "Documentation for Even") : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Prop where | [zero](Introduction/#Even___zero-next "Documentation for Even.zero") : [Even](Introduction/#Even___zero-next "Documentation for Even") 0 | add2 : [Even](Introduction/#Even___zero-next "Documentation for Even") x → [Even](Introduction/#Even___zero-next "Documentation for Even") (x + 2)  [attribute](Attributes/#Lean___Parser___Command___attribute "Documentation for syntax") [grind intro] [Even](Introduction/#Even___zero-next "Documentation for Even") example (h : [Even](Introduction/#Even___zero-next "Documentation for Even") x) : [Even](Introduction/#Even___zero-next "Documentation for Even") (x + 6) := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:[Even](Introduction/#Even___zero-next "Documentation for Even") x⊢ [Even](Introduction/#Even___zero-next "Documentation for Even") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 6[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 example : [Even](Introduction/#Even___zero-next "Documentation for Even") 0 := by⊢ [Even](Introduction/#Even___zero-next "Documentation for Even") 0 [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
Here `attribute [grind intro] Even` acts like a macro that expands to `attribute [grind] Even.zero` and `attribute [grind] Even.add2`. This is especially convenient for inductive predicates with many constructors.
Patterns for Constructors
The predicate `[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example")` states that each of the values in a list of integers is less than the one before, and the function `[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example")` checks this property, returning a `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`.
`inductive Decreasing : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → Prop   | nil : [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") []   | singleton : [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [x]   | cons : [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") (x :: xs) → y > x → [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") (y :: x :: xs)  def decreasing : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")   | [] | [_] => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")   | y :: x :: xs => y > x && [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") (x :: xs) `
The function is correct if it returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` exactly when `[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example")` holds for its argument. Attempting to prove this fact using a combination of `[fun_induction](Tactic-Proofs/Tactic-Reference/#fun_induction "Documentation for tactic")` and `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` fails immediately, with none of the three cases proven:
`def decreasingCorrect : [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") xs = [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") xs := byxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") xs [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") xs   [fun_induction](Tactic-Proofs/Tactic-Reference/#fun_induction "Documentation for tactic") decreasingcase1⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")case2head✝:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")head✝[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")case3y✝:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")x✝:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")xs✝:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")ih1✝:[(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[(](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") (y✝ > x✝) [&&](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[)](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") <;>case1⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")case2head✝:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")head✝[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")case3y✝:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")x✝:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")xs✝:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")ih1✝:[(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[(](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") (y✝ > x✝) [&&](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[)](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") ``grind` failed grind.1y x:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")ih1:[(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")h:[(](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And")-1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0 [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")left:-1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0left_1:[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")right_1:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
 
    * [prop] [(](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And")-1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0 [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
 
    * [prop] -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
    * [prop] [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")
 
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
 
 
  * [eqc] True propositions 
    * [prop] [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
 
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
 
    * [prop] -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0 [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")
 
    * [prop] [(](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And")-1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0 [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
 
    * [prop] [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
 
    * [prop] [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")
 
    * [prop] -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0
 
 
  * [eqc] False propositions
    * [prop] [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
 
  * [eqc] Equivalence classes
    * [eqc] {[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true"), [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")}
 
  * [cases] Case analyses
    * [cases] [1/2]: [(](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And")-1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0 [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
      * [cases] source: Initial goal
 
  * [cutsat] Assignment satisfying linear constraints 
    * [assign] y := 1
 
    * [assign] x := 0
 
 
```grind` failed grindh:[True](Basic-Propositions/Truth/#True___intro "Documentation for True") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts
    * [prop] [True](Basic-Propositions/Truth/#True___intro "Documentation for True") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")
 
  * [eqc] True propositions 
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")
 
    * [prop] [True](Basic-Propositions/Truth/#True___intro "Documentation for True") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")
 
 
  * [eqc] False propositions
    * [prop] [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")
 
```grind` failed grindhead:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")h:[True](Basic-Propositions/Truth/#True___intro "Documentation for True") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")head[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts
    * [prop] [True](Basic-Propositions/Truth/#True___intro "Documentation for True") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")head[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
 
  * [eqc] True propositions 
    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")head[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
 
    * [prop] [True](Basic-Propositions/Truth/#True___intro "Documentation for True") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")head[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
 
 
  * [eqc] False propositions
    * [prop] [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")head[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
```
`grind` failed
grindh:[True](Basic-Propositions/Truth/#True___intro "Documentation for True") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts
    * [prop] [True](Basic-Propositions/Truth/#True___intro "Documentation for True") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")


  * [eqc] True propositions

    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")


    * [prop] [True](Basic-Propositions/Truth/#True___intro "Documentation for True") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")




  * [eqc] False propositions
    * [prop] [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")



```

```
`grind` failed
grindhead:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")h:[True](Basic-Propositions/Truth/#True___intro "Documentation for True") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")head[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts
    * [prop] [True](Basic-Propositions/Truth/#True___intro "Documentation for True") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")head[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")


  * [eqc] True propositions

    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")head[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")


    * [prop] [True](Basic-Propositions/Truth/#True___intro "Documentation for True") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")head[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")




  * [eqc] False propositions
    * [prop] [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")head[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")



```

```
`grind` failed
grind.1y x:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")ih1:[(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")h:[(](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And")-1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0 [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")left:-1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0left_1:[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")right_1:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts

    * [prop] [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")


    * [prop] [(](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And")-1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0 [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")


    * [prop] -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0


    * [prop] [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")


    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")




  * [eqc] True propositions

    * [prop] [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")


    * [prop] [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")


    * [prop] -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0 [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")


    * [prop] [(](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And")-1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0 [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")


    * [prop] [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")


    * [prop] [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")


    * [prop] -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0




  * [eqc] False propositions
    * [prop] [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")


  * [eqc] Equivalence classes
    * [eqc] {[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true"), [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")}


  * [cases] Case analyses
    * [cases] [1/2]: [(](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And")-1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 0 [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
      * [cases] source: Initial goal


  * [cutsat] Assignment satisfying linear constraints

    * [assign] y := 1


    * [assign] x := 0





```

Adding the `grind intro` attribute to `[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example")` results in E-matching patterns being added for each of the three constructors, after which `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` can prove the first two goals, and requires only a case analysis of a hypothesis to prove the final goal:
`[attribute](Attributes/#Lean___Parser___Command___attribute "Documentation for syntax") [grind intro] [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example")  def decreasingCorrect' : [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") xs = [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") xs := byxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") xs [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") xs   [fun_induction](Tactic-Proofs/Tactic-Reference/#fun_induction "Documentation for tactic") decreasingcase1⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")case2head✝:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")head✝[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")case3y✝:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")x✝:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")xs✝:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")ih1✝:[(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[(](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") (y✝ > x✝) [&&](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[)](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") <;>case1⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")case2head✝:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")head✝[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")case3y✝:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")x✝:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")xs✝:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")ih1✝:[(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[(](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") (y✝ > x✝) [&&](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[)](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [try](Tactic-Proofs/The-Tactic-Language/#try "Documentation for tactic") [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙   [case](Tactic-Proofs/The-Tactic-Language/#case "Documentation for tactic") case3 y x xs ih =>y:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")x:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")ih:[(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[(](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") (y✝ > x✝) [&&](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[)](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")     [apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") [propext](The-Type-System/Propositions/#propext "Documentation for propext")ay:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")x:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")ih:[(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")⊢ [(](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") (y > x) [&&](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[)](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")     [constructor](Tactic-Proofs/Tactic-Reference/#constructor "Documentation for tactic")a.mpy:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")x:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")ih:[(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")⊢ [(](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") (y > x) [&&](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[)](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")a.mpry:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")x:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")ih:[(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")⊢ [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") → [(](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") (y > x) [&&](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[)](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")     .a.mpy:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")x:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")ih:[(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")⊢ [(](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") (y > x) [&&](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[)](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙     .a.mpry:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")x:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")ih:[(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")⊢ [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") → [(](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") (y > x) [&&](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[)](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") intro       | [.cons](The--grind--tactic/E___matching/#Decreasing___cons-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") hDec hLt =>y:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")x:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")ih:[(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝:[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")hDec:[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")hLt:y > x⊢ [(](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") (y > x) [&&](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[)](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")         [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
Adding `grind cases` to `[Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example")` enables this case analysis automatically, resulting in a fully automatic proof:
`[attribute](Attributes/#Lean___Parser___Command___attribute "Documentation for syntax") [grind cases] [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example")  def decreasingCorrect'' : [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") xs = [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") xs := byxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") xs [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") xs   [fun_induction](Tactic-Proofs/Tactic-Reference/#fun_induction "Documentation for tactic") decreasingcase1⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")case2head✝:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")head✝[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")case3y✝:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")x✝:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")xs✝:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")ih1✝:[(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[(](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") (y✝ > x✝) [&&](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[)](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") <;>case1⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")case2head✝:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")head✝[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")case3y✝:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")x✝:[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")xs✝:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")ih1✝:[(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")⊢ [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")[(](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") (y✝ > x✝) [&&](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [decreasing](The--grind--tactic/E___matching/#decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[)](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Decreasing](The--grind--tactic/E___matching/#Decreasing-_LPAR_in-Patterns-for-Constructors_RPAR_ "Definition of example") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABAEUVAToghgZ1AHNkAuZAGWDxmQEkQbAkwmQAVMB7ABwChlkAfZCGAAbUmgzZ8RZAG0AurwHICIQiMQx2Iceiy5VxWQA9FfQVG15dkgzIAUx0mWN4AlMmYBPZAD5kTsx6UobI9j4kLs4B7tzcYIgAZsgJ+tJq4pTUdAyeyABC7OwiSoIKyrIA+vLIALz+MJgQiKXIEVGRMXX+Pv5OAGT9KbbpxI7Rrm5xODCNwABGEDAosoSYoGDIoI3sNcF2anEJyakhRADC7JjYsADk4qcHxK51EmmhLyS1yPNeSokQECVDbQODaYbvGQAHgA3A1MD41hslFB8ChUXhEABmNoBLrAAAW3SUfBwnE4Ih8nA4nEQxhgJOQlhA1CasCujIAdMgkeAuVsGBxGeZkJzmdYCXpkATyDR6sK+Dz1nzuDM5otlnJeZsMYg8HsRoYjkkIWc1JdrhgYLd7mRHqMut99g7Pt9fv9AcDwKDgOD7aFYf5tUA"\))
syntaxUnfolding During Preprocessing

```
grindMod ::= ...
    | The `unfold` modifier instructs `grind` to unfold the given definition during the preprocessing step.
Example:
```
@[grind unfold] def h (x : Nat) := 2 * x
example : 6 ∣ 3*h x := by grind
```
unfold
```

The `[unfold](Tactic-Proofs/Tactic-Reference/#unfold "Documentation for tactic")` modifier instructs `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to unfold the given definition during the preprocessing step. Example:
`@[grind unfold] def [h](releases/v4.28.0/#h "Definition of example") (x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) := 2 * x example : 6 ∣ 3*[h](releases/v4.28.0/#h "Definition of example") x := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ 6 [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") 3 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [h](releases/v4.28.0/#h "Definition of example") x [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
syntaxNormalization Rules

```
grindMod ::= ...
    | The `norm` modifier instructs `grind` to use a theorem as a normalization rule. That is,
the theorem is applied during the preprocessing step.
This feature is meant for advanced users who understand how the preprocessor and `grind`'s search
procedure interact with each other.
New users can still benefit from this feature by restricting its use to theorems that completely
eliminate a symbol from the goal. Example:
```
theorem max_def : max n m = if n ≤ m then m else n
```
For a negative example, consider:
```
opaque f : Int → Int → Int → Int
theorem fax1 : f x 0 1 = 1 := sorry
theorem fax2 : f 1 x 1 = 1 := sorry
attribute [grind norm] fax1
attribute [grind =] fax2

example (h : c = 1) : f c 0 c = 1 := by
  grind -- fails
```
In this example, `fax1` is a normalization rule, but it is not applicable to the input goal since
`f c 0 c` is not an instance of `f x 0 1`. However, `f c 0 c` matches the pattern `f 1 x 1` modulo
the equality `c = 1`. Thus, `grind` instantiates `fax2` with `x := 0`, producing the equality
`f 1 0 1 = 1`, which the normalizer simplifies to `True`. As a result, nothing useful is learned.
In the future, we plan to include linters to automatically detect issues like these.
Example:
```
opaque f : Nat → Nat
opaque g : Nat → Nat

@[grind norm] axiom fax : f x = x + 2
@[grind norm ←] axiom fg : f x = g x

example : f x ≥ 2 := by grind
example : f x ≥ g x := by grind
example : f x + g x ≥ 4 := by grind
```
norm
```

The `norm` modifier instructs `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to use a theorem as a normalization rule. That is, the theorem is applied during the preprocessing step. This feature is meant for advanced users who understand how the preprocessor and `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")`'s search procedure interact with each other. New users can still benefit from this feature by restricting its use to theorems that completely eliminate a symbol from the goal. Example:

```
theorem max_def : max n m = if n ≤ m then m else n

```

For a negative example, consider:

```
opaque f : Int → Int → Int → Int
theorem fax1 : f x 0 1 = 1 := sorry
theorem fax2 : f 1 x 1 = 1 := sorry
attribute [grind norm] fax1
attribute [grind =] fax2

example (h : c = 1) : f c 0 c = 1 := by
  grind -- fails

```

In this example, `fax1` is a normalization rule, but it is not applicable to the input goal since `f c 0 c` is not an instance of `f x 0 1`. However, `f c 0 c` matches the pattern `f 1 x 1` modulo the equality `c = 1`. Thus, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` instantiates `fax2` with `x := 0`, producing the equality `f 1 0 1 = 1`, which the normalizer simplifies to `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")`. As a result, nothing useful is learned. In the future, we plan to include linters to automatically detect issues like these. Example:
`opaque [f](releases/v4.27.0/#f "Definition of example") : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") opaque g : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")  @[grind norm] [axiom](Axioms/#Lean___Parser___Command___axiom-next "Documentation for syntax") fax : [f](releases/v4.27.0/#f "Definition of example") x = x + 2 @[grind norm ←] [axiom](Axioms/#Lean___Parser___Command___axiom-next "Documentation for syntax") fg : [f](releases/v4.27.0/#f "Definition of example") x = g x  example : [f](releases/v4.27.0/#f "Definition of example") x ≥ 2 := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [f](releases/v4.27.0/#f "Definition of example") x ≥ 2 [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 example : [f](releases/v4.27.0/#f "Definition of example") x ≥ g x := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [f](releases/v4.27.0/#f "Definition of example") x ≥ g x [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 example : [f](releases/v4.27.0/#f "Definition of example") x + g x ≥ 4 := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [f](releases/v4.27.0/#f "Definition of example") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") g x ≥ 4 [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
##  16.6.2. Inspecting Patterns[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--grind--tactic--E___matching--Inspecting-Patterns "Permalink")
The `grind?` attribute is a version of the `grind` attribute that additionally displays the generated pattern or [multi-pattern](The--grind--tactic/E___matching/#--tech-term-multi-pattern). Patterns and multi-patterns are displayed as lists of subexpressions, each of which is a pattern; ordinary patterns are displayed as singleton lists. In these displayed patterns, the names of defined constants are printed as-is. When the theorem's parameters occur in the pattern, they are displayed using numbers rather than names. In particular, they are numbered from right to left, starting at 0; this representation is referred to as _de Bruijn indices_.
Inspecting Patterns
In order to use this proof that divisibility is transitive with `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")`, it requires E-matching patterns:
`theorem div_trans {n k j : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : n ∣ k → k ∣ j → n ∣ j := byn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")j:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ n [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") k → k [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") j → n [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") j   [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") ⟨d₁, p₁⟩ ⟨d₂, p₂⟩n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")j:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")d₁:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")p₁:k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d₁d₂:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")p₂:j [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d₂⊢ n [∣](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") j   [exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic") ⟨d₁ * d₂, byn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")j:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")d₁:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")p₁:k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d₁d₂:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")p₂:j [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d₂⊢ j [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [(](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul")d₁ [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") d₂[)](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic") [p₂, p₁, Nat.mul_assoc]All goals completed! 🐙⟩ `
The right attribute to use is `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind →[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")`, because there should be a pattern for each premise. Using `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind? →[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")`, it is possible to see which patterns are generated:
`[attribute](Attributes/#Lean___Parser___Command___attribute "Documentation for syntax") [`[div_trans](The--grind--tactic/E___matching/#div_trans-_LPAR_in-Inspecting-Patterns_RPAR_ "Definition of example"): [[@](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd")[Dvd.dvd](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[Nat.instDvd] #4 #3, [@](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd")[Dvd.dvd](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[Nat.instDvd] #3 #2]`[grind?](The--grind--tactic/E___matching/#Lean___Parser___Attr___grind___-next "Documentation for syntax") →] [div_trans](The--grind--tactic/E___matching/#div_trans-_LPAR_in-Inspecting-Patterns_RPAR_ "Definition of example") `
There are two:

```
[div_trans](The--grind--tactic/E___matching/#div_trans-_LPAR_in-Inspecting-Patterns_RPAR_ "Definition of example"): [[@](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd")[Dvd.dvd](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[Nat.instDvd] #4 #3, [@](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd")[Dvd.dvd](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.dvd") `[[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] `[Nat.instDvd] #3 #2]
```

Arguments are numbered from right to left, so `#0` is the assumption that `k ∣ j`, while `#4` is `n`. Thus, these two patterns correspond to the terms `n ∣ k` and `k ∣ j`.
[Live ↪](javascript:openLiveLink\("C4Cwpg9gTmC2AEATAlgNwPrCgQwHYGd4BvXeAa3gCt4AueAOW2AF9b5TBiInPkCTCbr6n05VaAXngAjAJ4AoePGS4sEeIAvyRIECCADTwADhsCX5GsSAggh26TBufDAAPbAGNgxjfABUSM5KnwoAd3gAbQtzbQYmADpYAFcAG3RsfHwIBwBdKxkmLGQJaOAwIIBzKEVEAH5eVKQ0TBwCIA"\))
The rules for selecting patterns from subexpressions of the hypotheses and conclusion are subtle.
Forward Pattern Generation
`[axiom](Axioms/#Lean___Parser___Command___axiom-next "Documentation for syntax") p : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [axiom](Axioms/#Lean___Parser___Command___axiom-next "Documentation for syntax") q : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ``@[`[h₁](The--grind--tactic/E___matching/#h___-_LPAR_in-Forward-Pattern-Generation_RPAR_ "Definition of example"): [[q](The--grind--tactic/E___matching/#q-_LPAR_in-Forward-Pattern-Generation_RPAR_ "Definition of example") #1]`[grind!?](The--grind--tactic/E___matching/#Lean___Parser___Attr___grind______ "Documentation for syntax") →] theorem `declaration uses `sorry``h₁ (w : 7 = [p](The--grind--tactic/E___matching/#p-_LPAR_in-Forward-Pattern-Generation_RPAR_ "Definition of example") ([q](The--grind--tactic/E___matching/#q-_LPAR_in-Forward-Pattern-Generation_RPAR_ "Definition of example") x)) : [p](The--grind--tactic/E___matching/#p-_LPAR_in-Forward-Pattern-Generation_RPAR_ "Definition of example") (x + 1) = [q](The--grind--tactic/E___matching/#q-_LPAR_in-Forward-Pattern-Generation_RPAR_ "Definition of example") x := sorry `
```
[h₁](The--grind--tactic/E___matching/#h___-_LPAR_in-Forward-Pattern-Generation_RPAR_ "Definition of example"): [[q](The--grind--tactic/E___matching/#q-_LPAR_in-Forward-Pattern-Generation_RPAR_ "Definition of example") #1]
```

The pattern is `q x`. Counting from the right, parameter `#0` is the premise `w` and parameter `#1` is the implicit parameter `x`.
Why did `@[grind →]`? select `q #1`? The attribute `@[grind →]` finds patterns by traversing the hypotheses (that is, parameters whose types are propositions) from left to right. In this case, there's only a single hypothesis: `7 = p (q x)`. The heuristic described above says that `grind` will search for a minimal [indexable](The--grind--tactic/E___matching/#--tech-term-indexable) subexpression which [covers](The--grind--tactic/E___matching/#--tech-term-cover) a previously uncovered parameter. There's just one uncovered parameter, namely `x`. The whole hypothesis `p (q x) = 7` can't be used because `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` will not index on equality. The right-hand side `7` is not helpful, because it doesn't determine the value of `x`. `p (q x)` is not suitable because it is not minimal: it has `q x` inside of it, which is indexable (its head is the constant `q`), and it determines the value of `x`. The expression `q x` itself is minimal, because `x` is not indexable. Thus, `q x` is selected as the pattern.
[Live ↪](javascript:openLiveLink\("IYDwlg9gtgBADjAXDAcsALjQSYSowKFElgEcldMc1088ABAbQHMAnMAOwBMBCAfmwF0Y6ABYBTCM1GxhgQIIYACgDuZAOwwAvPAWkQASl1kE8kDADUMAIwHNOpJoDOE5gE8gA"\))
Backward Pattern Generation
In this example, the ``Lean.Parser.Attr.grindMod```←` modifier indicates that the pattern should be found in the conclusion:
`set_option trace.grind.debug.ematch.pattern true [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") @[`[grind.debug.ematch.pattern] place: p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") q x[grind.debug.ematch.pattern] collect: p (x + 1) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") q x[grind.debug.ematch.pattern] arg: [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"), support: true[grind.debug.ematch.pattern] arg: p (x + 1), support: false[grind.debug.ematch.pattern] collect: p (x + 1)[grind.debug.ematch.pattern] candidate: p (x + 1)[grind.debug.ematch.pattern] found pattern: p (#1 + 1)[grind.debug.ematch.pattern] found full coverage[grind.debug.ematch.pattern] arg: q x, support: false``[h₂](The--grind--tactic/E___matching/#h___-_LPAR_in-Backward-Pattern-Generation_RPAR_ "Definition of example"): [p (#1 + 1)]`[grind?](The--grind--tactic/E___matching/#Lean___Parser___Attr___grind___-next "Documentation for syntax") ←] theorem `declaration uses `sorry``h₂ (w : 7 = p (q x)) : p (x + 1) = q x := sorry `
The left side of the equality is used because `[Eq](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")` is not indexable and `[HAdd.hAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")` has lower priority than `p`.

```
[h₂](The--grind--tactic/E___matching/#h___-_LPAR_in-Backward-Pattern-Generation_RPAR_ "Definition of example"): [p (#1 + 1)]
```

[Live ↪](javascript:openLiveLink\("IYDwlg9gtgBADjAXDAcsALjQSYSowKFElgEcldMc1088BnAU3QH0I51IA7GdAJ2AGN6AOgDmPMBwAmQyfQBGAVxFD6UDPwAWQuBnT0eXXgvowJeAAIBtMRMkB+GIATCALrcN9CD1UwNgIIIYABQA7mQA7DAAvPCBpCAAlHFkCAEgMADUMACMiVGxSFG0njwAnkA"\))
Bidirectional Equality Pattern Generation
In this example, two separate E-matching patterns are generated from the equality conclusion. One matches the left-hand side, and the other matches the right-hand side.
`@[`[h₃](The--grind--tactic/E___matching/#h___-_LPAR_in-Bidirectional-Equality-Pattern-Generation_RPAR_ "Definition of example"): [q #1]``[h₃](The--grind--tactic/E___matching/#h___-_LPAR_in-Bidirectional-Equality-Pattern-Generation_RPAR_ "Definition of example"): [p (#1 + 1)]`[grind?](The--grind--tactic/E___matching/#Lean___Parser___Attr___grind___-next "Documentation for syntax") _=_] theorem `declaration uses `sorry``h₃ (w : 7 = p (q x)) : p (x + 1) = q x := sorry `
```
[h₃](The--grind--tactic/E___matching/#h___-_LPAR_in-Bidirectional-Equality-Pattern-Generation_RPAR_ "Definition of example"): [q #1]
```

The entire left side of the equality is used instead of just `x + 1` because `[HAdd.hAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")` has lower priority than `p`.

```
[h₃](The--grind--tactic/E___matching/#h___-_LPAR_in-Bidirectional-Equality-Pattern-Generation_RPAR_ "Definition of example"): [p (#1 + 1)]
```

[Live ↪](javascript:openLiveLink\("IYDwlg9gtgBADjAXDAcsALjQSYSowKFElgEcldMc1088ABAbQHMAnMAOwBMB+GAfQF5eAXRjoAFgFMIzCbDGBgghgAKAO5kA7DH7xlpEAEp9ZBEpAwA1DACMR7XqTaAztOYBPIA"\))
Patterns from Conclusion and Hypotheses
Without any modifiers, `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")` produces a multipattern by first checking the conclusion and then the premises:
`@[`[h₄](The--grind--tactic/E___matching/#h___-_LPAR_in-Patterns-from-Conclusion-and-Hypotheses_RPAR_ "Definition of example"): [p (#2 + 2), q #1]`[grind?](The--grind--tactic/E___matching/#Lean___Parser___Attr___grind___-next "Documentation for syntax") .] theorem `declaration uses `sorry``h₄ (w : p x = q y) : p (x + 2) = 7 := sorry `
Here, argument `x` is `#2`, `y` is `#1`, and `w` is `#0`. The resulting multipattern contains the left-hand side of the equality, which is the only [minimal](The--grind--tactic/E___matching/#--tech-term-minimal) [indexable](The--grind--tactic/E___matching/#--tech-term-indexable) subexpression of the conclusion that covers an argument (namely `x`). It also contains `q y`, which is the only minimal indexable subexpression of the hypothesis `w` that covers an additional argument (namely `y`).

```
[h₄](The--grind--tactic/E___matching/#h___-_LPAR_in-Patterns-from-Conclusion-and-Hypotheses_RPAR_ "Definition of example"): [p (#2 + 2), q #1]
```

[Live ↪](javascript:openLiveLink\("IYDwlg9gtgBADjAXDAcsALjQSYSowKFElgEcldMc1088ABAbQHMAnMAOwBMB+GAOgF0Y6ABYBTCM1GxhgEIIYACgDuZBCBgBeGKQCeAShUK1AahgAmfZoDsSTQGcJzbUA"\))
Failing Backward Pattern Generation
In this example, pattern generation fails because the theorem's conclusion doesn't mention the argument `y`.
`@[``@[grind ←] theorem [h₅](The--grind--tactic/E___matching/#h___-_LPAR_in-Failing-Backward-Pattern-Generation_RPAR_ "Definition of example")` failed to find patterns in the theorem's conclusion, consider using different options or the `grind_pattern` command`[grind?](The--grind--tactic/E___matching/#Lean___Parser___Attr___grind___-next "Documentation for syntax") ←] theorem `declaration uses `sorry``h₅ (w : p x = q y) : p (x + 2) = 7 := sorry `
```
`@[grind ←] theorem [h₅](The--grind--tactic/E___matching/#h___-_LPAR_in-Failing-Backward-Pattern-Generation_RPAR_ "Definition of example")` failed to find patterns in the theorem's conclusion, consider using different options or the `grind_pattern` command
```

[Live ↪](javascript:openLiveLink\("IYDwlg9gtgBADjAXDAcsALjQSYSowKFElgEcldMc10g"\))
Left-to-Right Generation
In this example, the pattern is generated by traversing the premises from left to right, followed by the conclusion:
`@[`[h₆](The--grind--tactic/E___matching/#h___-_LPAR_in-Left-to-Right-Generation_RPAR_ "Definition of example"): [q (#3 + 2), p (#2 + 2)]`[grind?](The--grind--tactic/E___matching/#Lean___Parser___Attr___grind___-next "Documentation for syntax") =>] theorem `declaration uses `sorry``h₆ (_ : q (y + 2) = q y) (_ : q (y + 1) = q y) : p (x + 2) = 7 := sorry `
In the patterns, `y` is argument `#3` and `x` is argument `#2`, because [automatic implicit parameters](Definitions/Headers-and-Signatures/#--tech-term-automatic-implicit-parameters) are inserted from left to right and `y` occurs before `x` in the theorem statement. The premises are arguments `#1` and `#0`. In the resulting multipattern, `y` is covered by a subexpression of the first premise, and `z` is covered by a subexpression of the conclusion:

```
[h₆](The--grind--tactic/E___matching/#h___-_LPAR_in-Left-to-Right-Generation_RPAR_ "Definition of example"): [q (#3 + 2), p (#2 + 2)]
```

[Live ↪](javascript:openLiveLink\("IYDwlg9gtgBADjAXDAcsALjQSYSowKFElgEcldMc1088ABAbQHMAnMAOwBMB+GAXgD4AujHQALAKYRm42KMBhBHhhKYACgD6ZUioCeMANQwATAEo+MUtuOLl6zat0GAjKd7mYlpNaUIVIfUZcYAHYkXmsAZylmbSA"\))
##  16.6.3. Resource Limits[🔗](find/?domain=Verso.Genre.Manual.section&name=grind-limits "Permalink")
E-matching can generate an unbounded number of theorem [instances](The--grind--tactic/E___matching/#--tech-term-instance). For the sake of both efficiency and termination, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` limits the number of times that E-matching can run using two mechanisms: 

Generations
    
Each term is assigned a _generation_ , and terms produced by E-matching have a generation that is one greater than the maximal generation of all the terms used to instantiate the theorem. E-matching only considers terms whose generation is beneath a configurable threshold. The `gen` option to `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` controls the generation threshold. 

Round Limits
    
Each invocation of the E-matching engine is referred to as a _round_. Only a limited number of rounds of E-matching are performed. The `ematch` option to `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` controls the round limit. Too Many Instances
E-matching can generate too many theorem [instances](The--grind--tactic/E___matching/#--tech-term-instance). Some patterns may even generate an unbounded number of instances.
In this example, `[s_eq](The--grind--tactic/E___matching/#s_eq-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example")` is added to the index with the pattern `s x`:
`def s (x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) := 0  @[`[s_eq](The--grind--tactic/E___matching/#s_eq-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example"): [[s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") #0]`[grind?](The--grind--tactic/E___matching/#Lean___Parser___Attr___grind___-next "Documentation for syntax") =] theorem s_eq (x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") x = [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") (x + 1) := [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
```
[s_eq](The--grind--tactic/E___matching/#s_eq-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example"): [[s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") #0]
```

Attempting to use this theorem results in many facts about `[s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example")` applied to concrete values being generated. In particular, `[s_eq](The--grind--tactic/E___matching/#s_eq-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example")` is instantiated with a new `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` in each of the five rounds. First, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` instantiates `[s_eq](The--grind--tactic/E___matching/#s_eq-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example")` with `x := 0`, which generates the term `[s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 1`. This matches the pattern `s x`, and is thus used to instantiate `[s_eq](The--grind--tactic/E___matching/#s_eq-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example")` with `x := 1`, which generates the term `[s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 2`, and so on until the round limit is reached.
`example : [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 > 0 := by⊢ [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 > 0   ``grind` failed grindh:[s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 1
 
    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 2
 
    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 3
 
    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 3 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 4
 
    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 4 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 5
 
 
  * [eqc] Equivalence classes
    * [eqc] {[s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0, 0, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 1, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 2, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 3, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 4, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 5}
 
  * [ematch] E-matching patterns
    * [thm] [s_eq](The--grind--tactic/E___matching/#s_eq-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example"): [[s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") #0]
 
  * [cutsat] Assignment satisfying linear constraints 
    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 := 0
 
    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 1 := 0
 
    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 2 := 0
 
    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 3 := 0
 
    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 4 := 0
 
    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 5 := 0
 
 
  * [limits] Thresholds reached
    * [limit] maximum number of E-matching rounds has been reached, threshold: `(ematch := 5)`
 
 [grind] Diagnostics
  * [thm] E-Matching instances
    * [thm] [s_eq](The--grind--tactic/E___matching/#s_eq-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") ↦ 5

`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
```
`grind` failed
grindh:[s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts

    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 1


    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 2


    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 3


    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 3 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 4


    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 4 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 5




  * [eqc] Equivalence classes
    * [eqc] {[s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0, 0, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 1, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 2, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 3, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 4, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 5}


  * [ematch] E-matching patterns
    * [thm] [s_eq](The--grind--tactic/E___matching/#s_eq-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example"): [[s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") #0]


  * [cutsat] Assignment satisfying linear constraints

    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 := 0


    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 1 := 0


    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 2 := 0


    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 3 := 0


    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 4 := 0


    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 5 := 0




  * [limits] Thresholds reached
    * [limit] maximum number of E-matching rounds has been reached, threshold: `(ematch := 5)`



[grind] Diagnostics
  * [thm] E-Matching instances
    * [thm] [s_eq](The--grind--tactic/E___matching/#s_eq-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") ↦ 5


```

Increasing the round limit to 20 causes E-matching to terminate due to the default generation limit of 8:
`example : [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 > 0 := by⊢ [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 > 0   ``grind` failed grindh:[s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 1
 
    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 2
 
    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 3
 
    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 3 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 4
 
    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 4 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 5
 
    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 5 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 6
 
    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 6 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 7
 
    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 7 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 8
 
 
  * [eqc] Equivalence classes
    * [eqc] {[s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0, 0, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 1, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 2, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 3, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 4, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 5, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 6, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 7, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 8}
 
  * [ematch] E-matching patterns
    * [thm] [s_eq](The--grind--tactic/E___matching/#s_eq-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example"): [[s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") #0]
 
  * [cutsat] Assignment satisfying linear constraints 
    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 := 0
 
    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 1 := 0
 
    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 2 := 0
 
    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 3 := 0
 
    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 4 := 0
 
    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 5 := 0
 
    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 6 := 0
 
    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 7 := 0
 
    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 8 := 0
 
 
  * [limits] Thresholds reached
    * [limit] maximum term generation has been reached, threshold: `(gen := 8)`
 
 [grind] Diagnostics
  * [thm] E-Matching instances
    * [thm] [s_eq](The--grind--tactic/E___matching/#s_eq-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") ↦ 8

`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") (ematch := 20)All goals completed! 🐙 `
```
`grind` failed
grindh:[s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts

    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 1


    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 2


    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 3


    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 3 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 4


    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 4 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 5


    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 5 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 6


    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 6 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 7


    * [prop] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 7 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 8




  * [eqc] Equivalence classes
    * [eqc] {[s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0, 0, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 1, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 2, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 3, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 4, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 5, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 6, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 7, [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 8}


  * [ematch] E-matching patterns
    * [thm] [s_eq](The--grind--tactic/E___matching/#s_eq-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example"): [[s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") #0]


  * [cutsat] Assignment satisfying linear constraints

    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 0 := 0


    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 1 := 0


    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 2 := 0


    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 3 := 0


    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 4 := 0


    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 5 := 0


    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 6 := 0


    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 7 := 0


    * [assign] [s](The--grind--tactic/E___matching/#s-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") 8 := 0




  * [limits] Thresholds reached
    * [limit] maximum term generation has been reached, threshold: `(gen := 8)`



[grind] Diagnostics
  * [thm] E-Matching instances
    * [thm] [s_eq](The--grind--tactic/E___matching/#s_eq-_LPAR_in-Too-Many-Instances_RPAR_ "Definition of example") ↦ 8


```

[Live ↪](javascript:openLiveLink\("CYUwZgBAzhAUAeEBcEByBDALgSmQXggAYAoYgAQG0BzAJwEsA7YAfgjwF0JMALEAexogAttAD6IAI5xEKDDmTQIiAjAQQA1BACMuJHmIQINMABsgA"\))
Increasing E-matching Limits
`[iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example")` returns the list of all numbers strictly less than its argument, and the theorem `[iota_succ](The--grind--tactic/E___matching/#iota_succ-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example")` describes its behavior on `[Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")`:
`def iota : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   | 0 => []   | n + 1 => n :: [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") n  @[grind =] theorem iota_succ : [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") (n + 1) = n :: [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") n :=   [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
The fact that `([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") > 10` can be proven by repeatedly instantiating `[iota_succ](The--grind--tactic/E___matching/#iota_succ-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example")` and `List.length_cons`. However, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` does not succeed:
`example : ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") > 10 := by⊢ ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") > 10   ``grind` failed grindh:([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 10⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 10
 
    * [prop] [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 19 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19
 
    * [prop] [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 18 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18
 
    * [prop] [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")19 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1
 
    * [prop] [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 17 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17
 
    * [prop] [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")18 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1
 
    * [prop] [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 16 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16
 
    * [prop] [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")17 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1
 
    * [prop] [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 15 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 15
 
    * [prop] [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")16 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1
 
 
  * [eqc] True propositions
    * [prop] ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 10
 
  * [eqc] Equivalence classes 
    * [eqc] {[iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20, 19 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19}
 
    * [eqc] {([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")19 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1}
 
    * [eqc] {[iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19, 18 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18}
 
    * [eqc] {[iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18, 17 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17}
 
    * [eqc] {([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")18 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1}
 
    * [eqc] {[iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17, 16 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16}
 
    * [eqc] {([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")17 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1}
 
    * [eqc] {[iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16, 15 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 15}
 
    * [eqc] {([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")16 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1}
 
    * [eqc] others 
      * [eqc] {[↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")[(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")}
 
      * [eqc] {[↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")[(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")}
 
      * [eqc] {[↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")[(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")}
 
      * [eqc] {[↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")[(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")}
 
 
 
  * [ematch] E-matching patterns 
    * [thm] List.eq_nil_of_length_eq_zero: [[@](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")[List.length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") #2 #1]
 
    * [thm] [iota_succ](The--grind--tactic/E___matching/#iota_succ-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example"): [[iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") (#0 + 1)]
 
    * [thm] List.length_cons: [[@](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")[List.length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") #2 ([@](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[List.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") _ #1 #0)]
 
 
  * [cutsat] Assignment satisfying linear constraints 
    * [assign] ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := 4
 
    * [assign] ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := 3
 
    * [assign] [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")19 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := 4
 
    * [assign] ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := 2
 
    * [assign] [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")18 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := 3
 
    * [assign] ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := 1
 
    * [assign] [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")17 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := 2
 
    * [assign] ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := 0
 
    * [assign] [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")16 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := 1
 
 
  * [ring] Ring `Lean.Grind.Ring.OfSemiring.Q [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`
    * [basis] Basis 
      * [_] ↑([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") ↑([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
      * [_] ↑([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") ↑([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
      * [_] ↑([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") ↑([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
 
  * [limits] Thresholds reached
    * [limit] maximum number of E-matching rounds has been reached, threshold: `(ematch := 5)`
 
 [grind] Diagnostics
  * [thm] E-Matching instances 
    * [thm] [iota_succ](The--grind--tactic/E___matching/#iota_succ-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") ↦ 5
 
    * [thm] List.length_cons ↦ 4
 

`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
```
`grind` failed
grindh:([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 10⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts

    * [prop] ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 10


    * [prop] [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 19 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19


    * [prop] [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 18 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18


    * [prop] [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")19 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1


    * [prop] [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 17 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17


    * [prop] [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")18 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1


    * [prop] [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 16 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16


    * [prop] [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")17 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1


    * [prop] [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 15 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 15


    * [prop] [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")16 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1




  * [eqc] True propositions
    * [prop] ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") 10


  * [eqc] Equivalence classes

    * [eqc] {[iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20, 19 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19}


    * [eqc] {([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")19 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1}


    * [eqc] {[iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19, 18 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18}


    * [eqc] {[iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18, 17 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17}


    * [eqc] {([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")18 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1}


    * [eqc] {[iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17, 16 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16}


    * [eqc] {([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")17 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1}


    * [eqc] {[iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16, 15 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 15}


    * [eqc] {([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")16 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1}


    * [eqc] others

      * [eqc] {[↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")[(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")}


      * [eqc] {[↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")[(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")}


      * [eqc] {[↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")[(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")}


      * [eqc] {[↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")[(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")}






  * [ematch] E-matching patterns

    * [thm] List.eq_nil_of_length_eq_zero: [[@](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")[List.length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") #2 #1]


    * [thm] [iota_succ](The--grind--tactic/E___matching/#iota_succ-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example"): [[iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") (#0 + 1)]


    * [thm] List.length_cons: [[@](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")[List.length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") #2 ([@](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")[List.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") _ #1 #0)]




  * [cutsat] Assignment satisfying linear constraints

    * [assign] ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := 4


    * [assign] ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := 3


    * [assign] [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")19 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := 4


    * [assign] ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := 2


    * [assign] [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")18 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := 3


    * [assign] ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := 1


    * [assign] [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")17 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := 2


    * [assign] ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := 0


    * [assign] [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")16 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") := 1




  * [ring] Ring `Lean.Grind.Ring.OfSemiring.Q [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`
    * [basis] Basis

      * [_] ↑([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 19).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") ↑([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


      * [_] ↑([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 18).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") ↑([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


      * [_] ↑([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 17).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") ↑([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 16).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0




  * [limits] Thresholds reached
    * [limit] maximum number of E-matching rounds has been reached, threshold: `(ematch := 5)`



[grind] Diagnostics
  * [thm] E-Matching instances

    * [thm] [iota_succ](The--grind--tactic/E___matching/#iota_succ-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") ↦ 5


    * [thm] List.length_cons ↦ 4




```

Due to the limited number of E-matching rounds, the chain of instantiations is not completed. Increasing these limits allows `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to succeed:
`example : ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") > 10 := by⊢ ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") > 10   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") (gen := 20) (ematch := 20)All goals completed! 🐙 `
When the option `diagnostics` is set to `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` displays the number of instances that it generates for each theorem. This is useful to detect theorems that contain patterns that are triggering too many instances. In this case, the diagnostics show that `[iota_succ](The--grind--tactic/E___matching/#iota_succ-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example")` is instantiated 12 times:
`set_option diagnostics true [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") set_option diagnostics.threshold 10 [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") `[diag] Diagnostics
 
  * [reduction] unfolded reducible declarations (max: 52, num: 1):
    * [reduction] [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") ↦ 52
 
  * [type_class] used instances (max: 38, num: 4): 
    * [type_class] instOfNat ↦ 38
 
    * [type_class] Lean.Grind.CommRing.OfCommSemiring.ofCommSemiring ↦ 13
 
    * [type_class] Lean.Grind.instCommSemiringNat ↦ 12
 
    * [type_class] Lean.Grind.CommRing.OfCommSemiring.instOfNatQ ↦ 12
 
 
  * [kernel] unfolded declarations (max: 387, num: 73): 
    * [kernel] Int.Linear.Poly.rec ↦ 387
 
    * [kernel] Bool.rec ↦ 324
 
    * [kernel] Int.Linear.Expr.rec ↦ 197
 
    * [kernel] Int.rec ↦ 192
 
    * [kernel] Nat.rec ↦ 128
 
    * [kernel] Lean.RArray.rec ↦ 118
 
    * [kernel] Int.casesOn ↦ 116
 
    * [kernel] [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") ↦ 110
 
    * [kernel] Int.Linear.Expr.casesOn ↦ 104
 
    * [kernel] Bool.and' ↦ 94
 
    * [kernel] List.rec ↦ 85
 
    * [kernel] Int.Linear.Poly.casesOn ↦ 85
 
    * [kernel] Int.Linear.Poly.denote.match_1 ↦ 81
 
    * [kernel] [NatCast.natCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast") ↦ 77
 
    * [kernel] [Add.add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add.add") ↦ 73
 
    * [kernel] [HAdd.hAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") ↦ 73
 
    * [kernel] Bool.casesOn ↦ 68
 
    * [kernel] Nat.casesOn ↦ 64
 
    * [kernel] Int.Linear.Expr.toPoly'.go.match_1 ↦ 58
 
    * [kernel] Int.Linear.Poly.brecOn ↦ 51
 
    * [kernel] List.casesOn ↦ 50
 
    * [kernel] [cond](Basic-Types/Booleans/#cond "Documentation for cond") ↦ 49
 
    * [kernel] cond.match_1 ↦ 49
 
    * [kernel] Int.add.match_1 ↦ 48
 
    * [kernel] Int.Linear.Expr.denote.match_1 ↦ 46
 
    * [kernel] Int.beq' ↦ 44
 
    * [kernel] Int.Linear.Poly.brecOn.go ↦ 41
 
    * [kernel] Int.negOfNat.match_1 ↦ 40
 
    * [kernel] Int.Linear.Var ↦ 37
 
    * [kernel] Int.Linear.Expr.brecOn ↦ 36
 
    * [kernel] Int.Linear.Expr.brecOn.go ↦ 35
 
    * [kernel] [Int.negOfNat](Basic-Types/Integers/#Int___negOfNat "Documentation for Int.negOfNat") ↦ 33
 
    * [kernel] Lean.RArray.get ↦ 27
 
    * [kernel] [Int.mul](Basic-Types/Integers/#Int___mul "Documentation for Int.mul") ↦ 26
 
    * [kernel] Int.Linear.Poly.beq' ↦ 26
 
    * [kernel] instOfNatNat ↦ 25
 
    * [kernel] [HMul.hMul](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") ↦ 25
 
    * [kernel] [Mul.mul](Type-Classes/Basic-Classes/#Mul___mk "Documentation for Mul.mul") ↦ 25
 
    * [kernel] Int.Linear.Var.denote ↦ 25
 
    * [kernel] [Function.comp](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") ↦ 24
 
    * [kernel] Int.Linear.Expr.denote ↦ 24
 
    * [kernel] Int.Linear.Poly.insert ↦ 23
 
    * [kernel] Nat.Linear.Expr.rec ↦ 23
 
    * [kernel] instDecidableEqList.match_1 ↦ 22
 
    * [kernel] iota.match_1 ↦ 21
 
    * [kernel] [Int.add](Basic-Types/Integers/#Int___add "Documentation for Int.add") ↦ 20
 
    * [kernel] Int.neg.match_1 ↦ 20
 
    * [kernel] [Int.neg](Basic-Types/Integers/#Int___neg "Documentation for Int.neg") ↦ 19
 
    * [kernel] [Neg.neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg") ↦ 19
 
    * [kernel] [BEq.beq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") ↦ 17
 
    * [kernel] 23 more entries... 
      * [kernel] [Nat.blt](Basic-Types/Natural-Numbers/#Nat___blt "Documentation for Nat.blt") ↦ 16
 
      * [kernel] Decidable.casesOn ↦ 15
 
      * [kernel] Decidable.rec ↦ 15
 
      * [kernel] instOfNat ↦ 14
 
      * [kernel] [decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") ↦ 13
 
      * [kernel] Prod.casesOn ↦ 13
 
      * [kernel] Prod.rec ↦ 13
 
      * [kernel] Int.Linear.Poly.combine_mul_k ↦ 13
 
      * [kernel] Int.Linear.Poly.combine_mul_k' ↦ 13
 
      * [kernel] [LE.le](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") ↦ 12
 
      * [kernel] List.brecOn ↦ 12
 
      * [kernel] Int.Linear.norm_eq_cert ↦ 12
 
      * [kernel] Int.Linear.Expr.norm ↦ 12
 
      * [kernel] Int.Linear.Expr.toPoly' ↦ 12
 
      * [kernel] Int.Linear.Poly.addConst ↦ 12
 
      * [kernel] Int.Linear.Poly.norm ↦ 12
 
      * [kernel] Nat.Linear.Expr.casesOn ↦ 12
 
      * [kernel] Int.Linear.Expr.toPoly'.go ↦ 12
 
      * [kernel] instDecidableEqNat ↦ 11
 
      * [kernel] [Nat.decEq](Basic-Types/Natural-Numbers/#Nat___decEq "Documentation for Nat.decEq") ↦ 11
 
      * [kernel] Int.Linear.eq_eq_subst'_cert ↦ 11
 
      * [kernel] List.brecOn.go ↦ 11
 
      * [kernel] Nat.decEq.match_1 ↦ 11
 
 
 
  * use `set_option diagnostics.threshold <num>` to control threshold for reporting counters
 
`example : ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") > 10 := by⊢ ([iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") 20).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") > 10 `[grind] Diagnostics
 
  * [thm] E-Matching instances 
    * [thm] [iota_succ](The--grind--tactic/E___matching/#iota_succ-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") ↦ 12
 
    * [thm] List.length_cons ↦ 11
 
 
  * [app] Applications 
    * [app] [NatCast.natCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast") ↦ 37
 
    * [app] [List.length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") ↦ 23
 
    * [app] [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") ↦ 13
 
    * [app] [List.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") ↦ 12
 
    * [app] [Eq](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ↦ 11
 
    * [app] [HAdd.hAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") ↦ 11
 
    * [app] Lean.Grind.Ring.OfSemiring.toQ ↦ 11
 
    * [app] instHAdd ↦ 1
 
    * [app] [LE.le](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") ↦ 1
 
    * [app] [Lean.Grind.CommSemiring.toSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring.toSemiring") ↦ 1
 
 
  * [grind] Simplifier 
    * [simp] used theorems (max: 15, num: 2): 
      * [simp] Lean.Meta.Grind.Arith.normNatOfNatInst ↦ 15
 
      * [simp] Nat.reduceAdd ↦ 12
 
 
    * [simp] tried theorems (max: 46, num: 1):
      * [simp] eq_self ↦ 46 ❌️
 
    * use `set_option diagnostics.threshold <num>` to control threshold for reporting counters
 
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") (gen := 20) (ematch := 20)All goals completed! 🐙 `
```
[grind] Diagnostics


  * [thm] E-Matching instances

    * [thm] [iota_succ](The--grind--tactic/E___matching/#iota_succ-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") ↦ 12


    * [thm] List.length_cons ↦ 11




  * [app] Applications

    * [app] [NatCast.natCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast") ↦ 37


    * [app] [List.length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") ↦ 23


    * [app] [iota](The--grind--tactic/E___matching/#iota-_LPAR_in-Increasing-E-matching-Limits_RPAR_ "Definition of example") ↦ 13


    * [app] [List.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") ↦ 12


    * [app] [Eq](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ↦ 11


    * [app] [HAdd.hAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") ↦ 11


    * [app] Lean.Grind.Ring.OfSemiring.toQ ↦ 11


    * [app] instHAdd ↦ 1


    * [app] [LE.le](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") ↦ 1


    * [app] [Lean.Grind.CommSemiring.toSemiring](The--grind--tactic/Algebraic-Solver-_LPAR_Commutative-Rings___-Fields_RPAR_/#Lean___Grind___CommSemiring___mk "Documentation for Lean.Grind.CommSemiring.toSemiring") ↦ 1




  * [grind] Simplifier

    * [simp] used theorems (max: 15, num: 2):

      * [simp] Lean.Meta.Grind.Arith.normNatOfNatInst ↦ 15


      * [simp] Nat.reduceAdd ↦ 12




    * [simp] tried theorems (max: 46, num: 1):
      * [simp] eq_self ↦ 46 ❌️


    * use `set_option diagnostics.threshold <num>` to control threshold for reporting counters





```

[Live ↪](javascript:openLiveLink\("CYUwZgBAlg9gLgQwgLggOQXCgkwggGSgGcsM4AoCCAHwgAYIBeAPggG0BdC6iAOwgGoIARkYs+yVLES8yZAAKsA5gCcoPYI3YQ4ACxAxlIALbR4CAPqEArgGMbKU9IAUfQUICUjXiklnvyBi5lMAAbWRAADwQjAAcQkAcnKSQAJlp3ADp4nkVdCBYhegCIACMATy4VNQ0nRRBxBgg0zydjTBsdFEbm2UIQOHMYGLhYPmAoBEUeGGIoG0JtZSsEtTI+gaGRmDGJqZmR+YzdQ0IdGBCNQugeMkjouITUJL9mrPrczoKixvLK1XUILV6l0mulAW04B0Qc0gA"\))
By default, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` uses automatically generated equations for ``Lean.Parser.Term.match : term``Pattern matching. `match e, ... with | p, ... => f | ...` matches each given term `e` against each pattern `p` of a match alternative. When all patterns of an alternative match, the `match` term evaluates to the value of the corresponding right-hand side `f` with the pattern variables bound to the respective matched values. If used as `match h : e, ... with | p, ... => f | ...`, `h : e = p` is available within `f`.  When not constructing a proof, `match` does not automatically substitute variables matched on in dependent variables' types. Use `match (generalizing := true) ...` to enforce this.  Syntax quotations can also be used in a pattern match. This matches a `Syntax` value against quotations, pattern variables, or `_`.  Quoted identifiers only match identical identifiers - custom matching such as by the preresolved names only should be done explicitly.  `Syntax.atom`s are ignored during matching by default except when part of a built-in literal. For users introducing new atoms, we recommend wrapping them in dedicated syntax kinds if they should participate in matching. For example, in ```lean syntax "c" ("foo" <|> "bar") ... ``` `foo` and `bar` are indistinguishable during matching, but in ```lean syntax foo := "foo" syntax "c" (foo <|> "bar") ... ``` they are not. ``[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match)-expressions as E-matching theorems. This can be disabled by setting the `matchEqs` flag to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
E-matching and Pattern Matching
Enabling diagnostics shows that `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` uses one of the equations of the auxiliary matching function during E-matching:
`theorem gt1 (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :     x = y + 1 →     0 < [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") x [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")         | 0 => 0         | _ + 1 => 1 := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 →   0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")     match x with     | 0 => 0     | n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") => 1   `[diag] Diagnostics
 
  * [reduction] unfolded reducible declarations (max: 34, num: 1):
    * [reduction] Nat.casesOn ↦ 34
 
  * [kernel] unfolded declarations (max: 40, num: 6): 
    * [kernel] List.rec ↦ 40
 
    * [kernel] Bool.rec ↦ 28
 
    * [kernel] [OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") ↦ 26
 
    * [kernel] List.casesOn ↦ 25
 
    * [kernel] Nat.Linear.Expr.rec ↦ 23
 
    * [kernel] Bool.casesOn ↦ 22
 
 
  * use `set_option diagnostics.threshold <num>` to control threshold for reporting counters
 
`[set_option](Tactic-Proofs/The-Tactic-Language/#set_option "Documentation for tactic") diagnostics [true](Tactic-Proofs/The-Tactic-Language/#set_option "Documentation for tactic") [in](Tactic-Proofs/The-Tactic-Language/#set_option "Documentation for tactic") `[grind] Diagnostics
 
  * [thm] E-Matching instances
    * [thm] gt1.match_1.congr_eq_2 ↦ 1
 
  * [app] Applications 
    * [app] [NatCast.natCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast") ↦ 4
 
    * [app] instHAdd ↦ 1
 
    * [app] [HAdd.hAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") ↦ 1
 
    * [app] gt1.match_1 ↦ 1
 
 
`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
```
[grind] Diagnostics


  * [thm] E-Matching instances
    * [thm] gt1.match_1.congr_eq_2 ↦ 1


  * [app] Applications

    * [app] [NatCast.natCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast") ↦ 4


    * [app] instHAdd ↦ 1


    * [app] [HAdd.hAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") ↦ 1


    * [app] gt1.match_1 ↦ 1





```

The theorem has this type:
``gt1.match_1.congr_eq_2.{u_1} (motive : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u_1) (x✝ : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (h_1 : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → motive 0)   (h_2 : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → motive n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")) (n✝ : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (heq_1 : x✝ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n✝.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")) :   (match x✝ with     | 0 => h_1 [(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")     | n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") => h_2 n) [≍](Basic-Propositions/Propositional-Equality/#HEq___refl "Documentation for HEq")     h_2 n✝`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") gt1.match_1.congr_eq_2 `
```
gt1.match_1.congr_eq_2.{u_1} (motive : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Sort u_1) (x✝ : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (h_1 : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → motive 0)
  (h_2 : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → motive n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")) (n✝ : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (heq_1 : x✝ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n✝.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")) :
  (match x✝ with
    | 0 => h_1 [(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")
    | n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") => h_2 n) [≍](Basic-Propositions/Propositional-Equality/#HEq___refl "Documentation for HEq")
    h_2 n✝
```

Disabling the use of matcher function equations causes the proof to fail:
`example (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))     : x = y + 1 →       0 < [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") x [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")           | 0 => 0           | _+1 => 1 := byx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 →   0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")     match x with     | 0 => 0     | n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") => 1   ``grind` failed grind.2x y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1h_1:(match x with   | 0 => 0   | n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") => 1) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")   0n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h_2:x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [grind] Goal diagnostics
 
  * [facts] Asserted facts 
    * [prop] x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1
 
    * [prop] (match x with       | 0 => 0       | n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") => 1) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")       0
 
    * [prop] x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1
 
 
  * [eqc] Equivalence classes 
    * [eqc] {x, y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1, n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1}
 
    * [eqc] {y, n}
 
    * [eqc] others 
      * [eqc] {↑y, ↑n}
 
      * [eqc] {[↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")y, [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")n}
 
      * [eqc] {[↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")[(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd"), [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")[(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")}
 
      * [eqc] {0,     match x with     | 0 => 0     | n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") => 1}
 
 
 
  * [cases] Case analyses
    * [cases] [2/2]: match x with     | 0 => 0     | n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") => 1
      * [cases] source: Initial goal
 
  * [cutsat] Assignment satisfying linear constraints 
    * [assign] x := 1
 
    * [assign] y := 0
 
    * [assign] match x with     | 0 => 0     | n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") => 1 := 0
 
    * [assign] n := 0
 
 
  * [ring] Rings 
    * [ring] Ring `Lean.Grind.Ring.OfSemiring.Q [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`
      * [basis] Basis
        * [_] ↑n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") ↑y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
    * [ring] Ring `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`
      * [basis] Basis
        * [_] [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0
 
 
 [grind] Diagnostics
  * [cases] Cases instances
    * [cases] [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit") ↦ 1

`[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") -matchEqsAll goals completed! 🐙 `
```
`grind` failed
grind.2x y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1h_1:(match x with
  | 0 => 0
  | n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") => 1) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
  0n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h_2:x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")
[grind] Goal diagnostics


  * [facts] Asserted facts

    * [prop] x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1


    * [prop] (match x with
      | 0 => 0
      | n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") => 1) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
      0


    * [prop] x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1




  * [eqc] Equivalence classes

    * [eqc] {x, y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1, n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1}


    * [eqc] {y, n}


    * [eqc] others

      * [eqc] {↑y, ↑n}


      * [eqc] {[↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")y, [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")n}


      * [eqc] {[↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")[(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd"), [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")[(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")}


      * [eqc] {0,
    match x with
    | 0 => 0
    | n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") => 1}






  * [cases] Case analyses
    * [cases] [2/2]: match x with
    | 0 => 0
    | n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") => 1
      * [cases] source: Initial goal


  * [cutsat] Assignment satisfying linear constraints

    * [assign] x := 1


    * [assign] y := 0


    * [assign] match x with
    | 0 => 0
    | n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") => 1 := 0


    * [assign] n := 0




  * [ring] Rings

    * [ring] Ring `Lean.Grind.Ring.OfSemiring.Q [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`
      * [basis] Basis
        * [_] ↑n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") ↑y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0


    * [ring] Ring `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`
      * [basis] Basis
        * [_] [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") -1 [*](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.hMul") [↑](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.natCast")n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0





[grind] Diagnostics
  * [cases] Cases instances
    * [cases] [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit") ↦ 1


```

[Live ↪](javascript:openLiveLink\("C4Cwpg9gTmC2AEBzYBGeAKAHvAnvAXPAHICGwAlAQFDy3zYC8u8A1PGoEmENdADPADzxYZAMYh68AO4BLUNzp0APvD4MAfCvkL4ygPqt28dYfxMARjm4BnMMF0QADsGkQAdvAAm0kolcQrziJW8MBQAK5g8NKu3IhQ0R5UVADEYmAiANZIqAB0wsBiuig5Im5xumAAjroATEA"\))
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=trace.grind.ematch.instance "Permalink")option
```
trace.grind.ematch.instance
```

Default value: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
enable/disable tracing for the given module and submodules
[←16.5. Case Analysis](The--grind--tactic/Case-Analysis/#grind-split "16.5. Case Analysis")[16.7. Linear Integer Arithmetic→](The--grind--tactic/Linear-Integer-Arithmetic/#cutsat "16.7. Linear Integer Arithmetic")

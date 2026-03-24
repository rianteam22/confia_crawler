[←About: propRecLargeElim](Error-Explanations/About___--propRecLargeElim/#The-Lean-Language-Reference--Error-Explanations--About___--propRecLargeElim "About: propRecLargeElim")[About: synthInstanceFailed→](Error-Explanations/About___--synthInstanceFailed/#The-Lean-Language-Reference--Error-Explanations--About___--synthInstanceFailed "About: synthInstanceFailed")
#  About: `redundantMatchAlt`[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--redundantMatchAlt "Permalink")
Error code: `lean.redundantMatchAlt`
_Match alternative will never be reached._
**Severity:** Error**Since:** 4.22.0
This error occurs when an alternative in a pattern match can never be reached: any values that would match the provided patterns would also match some preceding alternative. Refer to the [Pattern Matching](Terms/Pattern-Matching/#pattern-matching) manual section for additional details about pattern matching.
This error may appear in any pattern matching expression, including ``Lean.Parser.Term.match : term`
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
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match) expressions, equational function definitions, `if let` bindings, and monadic ``Lean.Parser.Term.let : term`
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
``let` bindings with fallback clauses.
In pattern-matches with multiple arms, this error may occur if a less-specific pattern precedes a more-specific one that it subsumes. Bear in mind that expressions are matched against patterns from top to bottom, so specific patterns should precede generic ones.
In ``termIfLet : term`
`if let pat := d then t else e` is a shorthand syntax for:

```
match d with
| pat => t
| _ => e

```

It matches `d` against the pattern `pat` and the bindings are available in `t`. If the pattern does not match, it returns `e` instead.
`[`if let`](Terms/Conditionals/#termIfLet) bindings and monadic ``Lean.Parser.Term.let : term`
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
``let` bindings with fallback clauses, in which only one pattern is specified, this error indicates that the specified pattern will always be matched. In this case, the binding in question can be replaced with a standard pattern-matching ``Lean.Parser.Term.let : term`
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
``let`.
One common cause of this error is that a pattern that was intended to match a constructor was instead interpreted as a variable binding. This occurs, for instance, if a constructor name (e.g., `cons`) is written without its prefix (`[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List")`) outside of that type's namespace. The constructor-name-as-variable linter, enabled by default, will display a warning on any variable patterns that resemble constructor names.
This error nearly always indicates an issue with the code where it appears. If needed, however, `set_option match.ignoreUnusedAlts true` will disable the check for this error and allow pattern matches with redundant alternatives to be compiled by discarding the unused arms.
##  Examples[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--redundantMatchAlt--Examples "Permalink")
Incorrect Ordering of Pattern Matches
OriginalFixed
`def seconds : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α   | [] => []   | _ :: xss => seconds xss   | `Redundant alternative: Any expression matching   [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")head✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") tail✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xss will match one of the preceding alternatives`(_ :: x :: _) :: xss => x :: seconds xss `
```
Redundant alternative: Any expression matching
  [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")head✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") tail✝[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xss
will match one of the preceding alternatives
```

`def seconds : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α   | [] => []   | (_ :: x :: _) :: xss => x :: seconds xss   | _ :: xss => seconds xss `
Since any expression matching `(_ :: x :: _) :: xss` will also match `_ :: xss`, the last alternative in the broken implementation is never reached. We resolve this by moving the more specific alternative before the more general one.
Unnecessary Fallback Clause
OriginalFixed
`example (p : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") × [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   `Redundant alternative: Any expression matching   x✝ will match one of the preceding alternatives`let (m, n) := p | return 0 return m + n `
```
Redundant alternative: Any expression matching
  x✝
will match one of the preceding alternatives
```

`example (p : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") × [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let (m, n) := p   return m + n `
Here, the fallback clause serves as a catch-all for all values of `p` that do not match `(m, n)`. However, no such values exist, so the fallback clause is unnecessary and can be removed. A similar error arises when using `if let pat := e` when `e` will always match `pat`.
Pattern Treated as Variable, Not Constructor
OriginalFixed
`example (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") xs [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | nil => [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")   | `Redundant alternative: Any expression matching   x✝ will match one of the preceding alternatives`_ => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") `
```
Redundant alternative: Any expression matching
  x✝
will match one of the preceding alternatives
```

`example (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") xs [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | [.nil](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil") => [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")   | _ => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") `
In the original example, `nil` is treated as a variable, not as a constructor name, since this definition is not within the `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List")` namespace. Thus, all values of `xs` will match the first pattern, rendering the second unused. Notice that the constructor-name-as-variable linter displays a warning at `nil`, indicating its similarity to a valid constructor name. Using dot-prefix notation, as shown in the fixed example, or specifying the full constructor name `[List.nil](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")` achieves the intended behavior.
[←About: propRecLargeElim](Error-Explanations/About___--propRecLargeElim/#The-Lean-Language-Reference--Error-Explanations--About___--propRecLargeElim "About: propRecLargeElim")[About: synthInstanceFailed→](Error-Explanations/About___--synthInstanceFailed/#The-Lean-Language-Reference--Error-Explanations--About___--synthInstanceFailed "About: synthInstanceFailed")

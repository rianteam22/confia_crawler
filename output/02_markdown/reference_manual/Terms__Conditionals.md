[←13.6. Structures and Constructors](Terms/Structures-and-Constructors/#The-Lean-Language-Reference--Terms--Structures-and-Constructors "13.6. Structures and Constructors")[13.8. Pattern Matching→](Terms/Pattern-Matching/#pattern-matching "13.8. Pattern Matching")
#  13.7. Conditionals[🔗](find/?domain=Verso.Genre.Manual.section&name=if-then-else "Permalink")
The conditional expression is used to check whether a proposition is true or false.Despite their syntactic similarity, the ``Lean.Parser.Tactic.tacIfThenElse : tactic`
In tactic mode, `if t then tac1 else tac2` is alternative syntax for:

```
by_cases t
· tac1
· tac2

```

It performs case distinction on `h† : t` or `h† : ¬t`, where `h†` is an anonymous hypothesis, and `tac1` and `tac2` are the subproofs. (It doesn't actually use nondependent `if`, since this wouldn't add anything to the context and hence would be useless for proving theorems. To actually insert an `ite` application use `refine if t then ?_ else ?_`.)
The assumptions in each subgoal can be named. `if h : t then tac1 else tac2` can be used as alternative syntax for:

```
by_cases h : t
· tac1
· tac2

```

It performs case distinction on `h : t` or `h : ¬t`.
You can use `?_` or `_` for either subproof to delay the goal to after the tactic, but if a tactic sequence is provided for `tac1` or `tac2` then it will require the goal to be closed by the end of the block.
`[`if`](Tactic-Proofs/The-Tactic-Language/#if) used [in the tactic language](Tactic-Proofs/The-Tactic-Language/#tactic-language-branching) and the ``Lean.Parser.Term.doIf : doElem```if` used [in `do`-notation](Tactic-Proofs/The-Tactic-Language/#tactic-language-branching) are separate syntactic forms, documented in their own sections. This requires that the proposition has a `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` instance, because it's not possible to check whether _arbitrary_ propositions are true or false. There is also a [coercion](Coercions/#--tech-term-coercion) from `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` to `Prop` that results in a decidable proposition (namely, that the `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` in question is equal to `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), described in the [section on decidability](Type-Classes/Basic-Classes/#decidable-propositions).
There are two versions of the conditional expression: one simply performs a case distinction, while the other additionally adds an assumption about the proposition's truth or falsity to the local context. This allows run-time checks to generate compile-time evidence that can be used to statically rule out errors.
syntaxConditionals
Without a name annotation, the conditional expression expresses only control flow.

```
term ::= ...
    | 


if c then t else e is notation for ite c t e, "if-then-else", which decides to
return t or e depending on whether c is true or false. The explicit argument
c : Prop does not have any actual computational content, but there is an additional
[Decidable c] argument synthesized by typeclass inference which actually
determines how to evaluate c to true or false. Write if h : c then t else e
instead for a "dependent if-then-else" dite, which allows t/e to use the fact
that c is true/false.


if term then
        term
      else
        term
```

With the name annotation, the branches of the ``termDepIfThenElse : term`
"Dependent" if-then-else, normally written via the notation `if h : c then t(h) else e(h)`, is sugar for `dite c (fun h => t(h)) (fun h => e(h))`, and it is the same as `if c then t else e` except that `t` is allowed to depend on a proof `h : c`, and `e` can depend on `h : ¬c`. (Both branches use the same name for the hypothesis, even though it has different types in the two cases.)
We use this to be able to communicate the if-then-else condition to the branches. For example, `Array.get arr i h` expects a proof `h : i < arr.size` in order to avoid a bounds check, so you can write `if h : i < arr.size then arr.get i h else ...` to avoid the bounds check inside the if branch. (Of course in this case we have only lifted the check into an explicit `if`, but we could also use this proof multiple times or derive `i < arr.size` from some other proposition that we are checking in the `if`.)
`[`if`](Terms/Conditionals/#termDepIfThenElse) have access to a local assumption that the proposition is respectively true or false.

```
term ::= ...
    | 


"Dependent" if-then-else, normally written via the notation if h : c then t(h) else e(h),
is sugar for dite c (fun h => t(h)) (fun h => e(h)), and it is the same as
if c then t else e except that t is allowed to depend on a proof h : c,
and e can depend on h : ¬c. (Both branches use the same name for the hypothesis,
even though it has different types in the two cases.)


We use this to be able to communicate the if-then-else condition to the branches.
For example, Array.get arr i h expects a proof h : i < arr.size in order to
avoid a bounds check, so you can write if h : i < arr.size then arr.get i h else ...
to avoid the bounds check inside the if branch. (Of course in this case we have only
lifted the check into an explicit if, but we could also use this proof multiple times
or derive i < arr.size from some other proposition that we are checking in the if.)


if 


binderIdent matches an ident or a _. It is used for identifiers in binding
position, where _ means that the value should be left unnamed and inaccessible.


binderIdent : term then
        term
      else
        term
```

Checking Array Bounds
Array indexing requires evidence that the index in question is within the bounds of the array, so `getThird` does not elaborate.
`def getThird (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : α := `failed to prove index is valid, possible solutions:   - Use `have`-expressions to prove the index is valid   - Use `a[i]!` notation instead, runtime check is performed, and 'Panic' error message is produced if index is not valid   - Use `a[i]?` notation instead, result is an `Option` type   - Use `a[i]'h` notation instead, where `h` is a proof that index is valid α:Type ?u.7xs:[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α⊢ 2 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")`xs[2] `
```
failed to prove index is valid, possible solutions:
  - Use `have`-expressions to prove the index is valid
  - Use `a[i]!` notation instead, runtime check is performed, and 'Panic' error message is produced if index is not valid
  - Use `a[i]?` notation instead, result is an `Option` type
  - Use `a[i]'h` notation instead, where `h` is a proof that index is valid
α:Type ?u.7xs:[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α⊢ 2 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")
```

Relaxing the return type to `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` and adding a bounds check results in the same error. This is because the proof that the index is in bounds was not added to the local context.
`def getThird (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α :=   [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") ≤ 2 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")   [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") `failed to prove index is valid, possible solutions:   - Use `have`-expressions to prove the index is valid   - Use `a[i]!` notation instead, runtime check is performed, and 'Panic' error message is produced if index is not valid   - Use `a[i]?` notation instead, result is an `Option` type   - Use `a[i]'h` notation instead, where `h` is a proof that index is valid α:Type ?u.7xs:[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α⊢ 2 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")`xs[2] `
```
failed to prove index is valid, possible solutions:
  - Use `have`-expressions to prove the index is valid
  - Use `a[i]!` notation instead, runtime check is performed, and 'Panic' error message is produced if index is not valid
  - Use `a[i]?` notation instead, result is an `Option` type
  - Use `a[i]'h` notation instead, where `h` is a proof that index is valid
α:Type ?u.7xs:[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α⊢ 2 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")
```

Naming the proof `h` is sufficient to enable the tactics that perform bounds checking to succeed, even though it does not occur explicitly in the text of the program.
`def getThird (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α :=   [if](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") h : xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") ≤ 2 [then](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")   [else](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") xs[2] `
[Live ↪](javascript:openLiveLink\("CYUwZgBA5iAuAqALAlgJ2BAFADwM4QC4IBBVVAQwE8JBG4AEpCIB5AB1mQHsA7WwgXgBQECMkiJGeAHS5kALxARAJkQQATBFiIQPLtxBCIIADa4FeANoqAukA"\))
There is also a pattern-matching version of ``termIfLet : term`
`if let pat := d then t else e` is a shorthand syntax for:

```
match d with
| pat => t
| _ => e

```

It matches `d` against the pattern `pat` and the bindings are available in `t`. If the pattern does not match, it returns `e` instead.
`[`if`](Terms/Conditionals/#termIfLet). If the pattern matches, then it takes the first branch, binding the pattern variables. If the pattern does not match, then it takes the second branch.
syntaxPattern-Matching Conditionals

```
term ::= ...
    | 


if let pat := d then t else e is a shorthand syntax for:


```
match d with
| pat => t
| _ => e

```

It matches `d` against the pattern `pat` and the bindings are available in `t`. If the pattern does not match, it returns `e` instead.
`if let term := term then term else term
```

If a `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`-only conditional statement is ever needed, the ``boolIfThenElse : term`
The conditional function.
`cond c x y` is the same as `if c then x else y`, but optimized for a Boolean condition rather than a decidable proposition. It can also be written using the notation `bif c then x else y`.
Just like `ite`, `cond` is declared `@[macro_inline]`, which causes applications of `cond` to be unfolded. As a result, `x` and `y` are not evaluated at runtime until one of them is selected, and only the selected branch is evaluated.
`[`bif`](Terms/Conditionals/#boolIfThenElse) variant can be used.
syntaxBoolean-Only Conditional

```
term ::= ...
    | 


The conditional function.


cond c x y is the same as if c then x else y, but optimized for a Boolean condition rather than
a decidable proposition. It can also be written using the notation bif c then x else y.


Just like ite, cond is declared @[macro_inline], which causes applications of cond to be
unfolded. As a result, x and y are not evaluated at runtime until one of them is selected, and
only the selected branch is evaluated.


bif term then
        term
      else
        term
```

[←13.6. Structures and Constructors](Terms/Structures-and-Constructors/#The-Lean-Language-Reference--Terms--Structures-and-Constructors "13.6. Structures and Constructors")[13.8. Pattern Matching→](Terms/Pattern-Matching/#pattern-matching "13.8. Pattern Matching")

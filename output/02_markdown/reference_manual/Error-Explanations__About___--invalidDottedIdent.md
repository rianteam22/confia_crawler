[←About: inferDefTypeFailed](Error-Explanations/About___--inferDefTypeFailed/#The-Lean-Language-Reference--Error-Explanations--About___--inferDefTypeFailed "About: inferDefTypeFailed")[About: invalidField→](Error-Explanations/About___--invalidField/#The-Lean-Language-Reference--Error-Explanations--About___--invalidField "About: invalidField")
#  About: `invalidDottedIdent`[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--invalidDottedIdent "Permalink")
Error code: `lean.invalidDottedIdent`
_Dotted identifier notation used with invalid or non-inferrable expected type._
**Severity:** Error**Since:** 4.22.0
This error indicates that dotted identifier notation was used in an invalid or unsupported context. Dotted identifier notation allows an identifier's namespace to be omitted, provided that it can be inferred by Lean based on type information. Details about this notation can be found in the manual section on [identifiers](Terms/Identifiers/#identifiers-and-resolution).
This notation can only be used in a term whose type Lean is able to infer. If there is insufficient type information for Lean to do so, this error will be raised. The inferred type must not be a type universe (e.g., `Prop` or `Type`), as dotted-identifier notation is not supported on these types.
##  Examples[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--invalidDottedIdent--Examples "Permalink")
Insufficient Type Information
OriginalFixed
`def reverseDuplicate (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :=   `Invalid dotted identifier notation: The expected type of `.reverse` could not be determined  Hint: Using one of these would be unambiguous:   [apply] `[Array.reverse](Basic-Types/Arrays/#Array___reverse "Documentation for Array.reverse")`   [apply] `[BitVec.reverse](Basic-Types/Bitvectors/#BitVec___reverse "Documentation for BitVec.reverse")`   [apply] `[List.reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse")`   [apply] `Vector.reverse`   [apply] `List.IsInfix.reverse`   [apply] `List.IsPrefix.reverse`   [apply] `List.IsSuffix.reverse`   [apply] `List.Sublist.reverse`   [apply] `Lean.Grind.AC.Seq.reverse`   [apply] `Std.DTreeMap.Internal.Impl.reverse`   [apply] `Std.Tactic.BVDecide.BVUnOp.reverse`   [apply] `Std.DTreeMap.Internal.Impl.Ordered.reverse``.reverse (xs ++ xs) `
```
Invalid dotted identifier notation: The expected type of `.reverse` could not be determined

Hint: Using one of these would be unambiguous:
  [apply] `[Array.reverse](Basic-Types/Arrays/#Array___reverse "Documentation for Array.reverse")`
  [apply] `[BitVec.reverse](Basic-Types/Bitvectors/#BitVec___reverse "Documentation for BitVec.reverse")`
  [apply] `[List.reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse")`
  [apply] `Vector.reverse`
  [apply] `List.IsInfix.reverse`
  [apply] `List.IsPrefix.reverse`
  [apply] `List.IsSuffix.reverse`
  [apply] `List.Sublist.reverse`
  [apply] `Lean.Grind.AC.Seq.reverse`
  [apply] `Std.DTreeMap.Internal.Impl.reverse`
  [apply] `Std.Tactic.BVDecide.BVUnOp.reverse`
  [apply] `Std.DTreeMap.Internal.Impl.Ordered.reverse`
```

`def reverseDuplicate (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α :=   [.reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse") (xs ++ xs) `
Because the return type of `reverseDuplicate` is not specified, the expected type of `.reverse` cannot be determined. Lean will not use the type of the argument `xs ++ xs` to infer the omitted namespace. Adding the return type `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` allows Lean to infer the type of `.reverse` and thus the appropriate namespace (`[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List")`) in which to resolve this identifier.
Note that this means that changing the return type of `reverseDuplicate` changes how `.reverse` resolves: if the return type is `T`, then Lean will (attempt to) resolve `.reverse` to a function `T.reverse` whose return type is `T`—even if `T.reverse` does not take an argument of type `List α`.
Dotted Identifier Where Type Universe Expected
OriginalFixed
`example (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") n > 42 [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | `Invalid dotted identifier notation: Not supported on type universe   Prop`.true => n - 1 | .false => n + 1 `
```
Invalid dotted identifier notation: Not supported on type universe
  Prop
```

`example (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") [decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") (n > 42) [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | [.true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")  => n - 1   | [.false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") => n + 1 `
The proposition `n > 42` has type `Prop`, which, being a type universe, does not support dotted-identifier notation. As this example demonstrates, attempting to use this notation in such a context is almost always an error. The intent in this example was for `.true` and `.false` to be Booleans, not propositions; however, ``Lean.Parser.Term.match : term`
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
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match) expressions do not automatically perform this coercion for decidable propositions. Explicitly adding `[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide")` makes the discriminant a `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` and allows the dotted-identifier resolution to succeed.
[←About: inferDefTypeFailed](Error-Explanations/About___--inferDefTypeFailed/#The-Lean-Language-Reference--Error-Explanations--About___--inferDefTypeFailed "About: inferDefTypeFailed")[About: invalidField→](Error-Explanations/About___--invalidField/#The-Lean-Language-Reference--Error-Explanations--About___--invalidField "About: invalidField")

[←16.9. Linear Arithmetic Solver](The--grind--tactic/Linear-Arithmetic-Solver/#grind-linarith "16.9. Linear Arithmetic Solver")[16.11. Reducibility→](The--grind--tactic/Reducibility/#The-Lean-Language-Reference--The--grind--tactic--Reducibility "16.11. Reducibility")
#  16.10. Annotating Libraries for `grind`[🔗](find/?domain=Verso.Genre.Manual.section&name=grind-annotation "Permalink")
To use `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` effectively with a library, it must be annotated by applying the `grind` attribute to suitable lemmas or declaring ``Lean.Parser.Command.grindPattern : command`
The `grind_pattern` command can be used to manually select a pattern for theorem instantiation. Enabling the option `trace.grind.ematch.instance` causes `grind` to print a trace message for each theorem instance it generates, which can be helpful when determining patterns.
When multiple patterns are specified together, all of them must match in the current context before `grind` attempts to instantiate the theorem. This is referred to as a _multi-pattern_. This is useful for theorems such as transitivity rules, where multiple premises must be simultaneously present for the rule to apply.
In the following example, `R` is a transitive binary relation over `Int`.

```
opaque R : Int → Int → Prop
axiom Rtrans {x y z : Int} : R x y → R y z → R x z

```

To use the fact that `R` is transitive, `grind` must already be able to satisfy both premises. This is represented using a multi-pattern:

```
grind_pattern Rtrans => R x y, R y z

example {a b c d} : R a b → R b c → R c d → R a d := by
  grind

```

The multi-pattern `R x y`, `R y z` instructs `grind` to instantiate `Rtrans` only when both `R x y` and `R y z` are available in the context. In the example, `grind` applies `Rtrans` to derive `R a c` from `R a b` and `R b c`, and can then repeat the same reasoning to deduce `R a d` from `R a c` and `R c d`.
You can add constraints to restrict theorem instantiation. For example:

```
grind_pattern extract_extract => (as.extract i j).extract k l where
  as =/= #[]

```

The constraint instructs `grind` to instantiate the theorem only if `as` is **not** definitionally equal to `#[]`.
## Constraints
  * `x =/= term`: The term bound to `x` (one of the theorem parameters) is **not** definitionally equal to `term`. The term may contain holes (i.e., `_`).
  * `x =?= term`: The term bound to `x` is definitionally equal to `term`. The term may contain holes (i.e., `_`).
  * `size x < n`: The term bound to `x` has size less than `n`. Implicit arguments and binder types are ignored when computing the size.
  * `depth x < n`: The term bound to `x` has depth less than `n`.
  * `is_ground x`: The term bound to `x` does not contain local variables or meta-variables.
  * `is_value x`: The term bound to `x` is a value. That is, it is a constructor fully applied to value arguments, a literal (`Nat`, `Int`, `String`, etc.), or a lambda `fun x => t`.
  * `is_strict_value x`: Similar to `is_value`, but without lambdas.
  * `not_value x`: The term bound to `x` is a **not** value (see `is_value`).
  * `not_strict_value x`: Similar to `not_value`, but without lambdas.
  * `gen < n`: The theorem instance has generation less than `n`. Recall that each term is assigned a generation, and terms produced by theorem instantiation have a generation that is one greater than the maximal generation of all the terms used to instantiate the theorem. This constraint complements the `gen` option available in `grind`.
  * `max_insts < n`: A new instance is generated only if less than `n` instances have been generated so far.
  * `guard e`: The instantiation is delayed until `grind` learns that `e` is `true` in this state.
  * `check e`: Similar to `guard e`, but `grind` checks whether `e` is implied by its current state by assuming `¬ e` and trying to deduce an inconsistency.


## Example
Consider the following example where `f` is a monotonic function

```
opaque f : Nat → Nat
axiom fMono : x ≤ y → f x ≤ f y

```

and you want to instruct `grind` to instantiate `fMono` for every pair of terms `f x` and `f y` when `x ≤ y` and `x` is **not** definitionally equal to `y`. You can use

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

``grind_pattern`s. These annotations direct `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")`'s selection of theorems, which lead to further facts on the metaphorical whiteboard. With too few annotations, `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` will fail to use the lemmas; with too many, it may become slow or it fail due to exhausting resource limitations. Annotations should generally be conservative: only add an annotation if you expect that `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` should _always_ instantiate the theorem once the patterns are matched.
##  16.10.1. Simp Lemmas[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--grind--tactic--Annotating-Libraries-for--grind--Simp-Lemmas "Permalink")
Typically, many theorems that are annotated with `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")simp[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")` should also be annotated with `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind =[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")`. One significant exception is that typically we avoid having `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")simp[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")` theorems that introduce an ``Lean.Parser.Term.if```if` on the right hand side, instead preferring a pair of theorems with the positive and negative conditions as hypotheses. Because `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` is designed to perform case splitting, it is generally better to instead annotate the single theorem introducing the ``Lean.Parser.Term.if```if` with `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind =[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")`.
Besides using `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind =[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")` to encourage `[grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")` to perform rewriting from left to right, you can also use `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind _=_[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")` to “saturate”, allowing bidirectional rewriting whenever either side is encountered.
##  16.10.2. Backwards and Forwards Reasoning[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The--grind--tactic--Annotating-Libraries-for--grind--Backwards-and-Forwards-Reasoning "Permalink")
Use `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind ←[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")` (which generates patterns from the conclusion of the theorem) for backwards reasoning theorems, i.e. theorems that should be tried when their conclusion matches a goal. Some examples of theorems in the standard library that are annotated with `grind ←` are:
  * `Array.not_mem_empty (a : α) : ¬ a ∈ #[]`
  * `Array.getElem_filter   {xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α} {p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")} {i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}   (h : i < (xs.[filter](Basic-Types/Arrays/#Array___filter "Documentation for Array.filter") p).[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) :   p (xs.[filter](Basic-Types/Arrays/#Array___filter "Documentation for Array.filter") p)[i]`
  * `List.Pairwise.tail   {l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α} (h : [Pairwise](Basic-Types/Linked-Lists/#List___Pairwise___nil "Documentation for List.Pairwise") R l) :   [Pairwise](Basic-Types/Linked-Lists/#List___Pairwise___nil "Documentation for List.Pairwise") R l.[tail](Basic-Types/Linked-Lists/#List___tail "Documentation for List.tail")`


In each case, the lemma is relevant when its conclusion matches a proof goal.
Use `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind →[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")` (which generates patterns from the hypotheses) for forwards reasoning theorems, i.e. where facts should be propagated from existing facts on the whiteboard. Some examples of theorems in the standard library that are annotated with `grind →` are:
  * `List.getElem_of_getElem? {l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α} :   l[i]? = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a →   ∃ h : i < l.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"), l[i] = a`
  * `Array.mem_of_mem_erase [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] {a b : α} {xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α}   (h : a ∈ xs.[erase](Basic-Types/Arrays/#Array___erase "Documentation for Array.erase") b) :   a ∈ xs`
  * `List.forall_none_of_filterMap_eq_nil   (h : [filterMap](Basic-Types/Linked-Lists/#List___filterMap "Documentation for List.filterMap") f xs = []) :   ∀ x ∈ xs, f x = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


In these cases, the theorems' assumptions determine when they are relevant.
There are many uses for custom patterns created with the ``Lean.Parser.Command.grindPattern : command`
The `grind_pattern` command can be used to manually select a pattern for theorem instantiation. Enabling the option `trace.grind.ematch.instance` causes `grind` to print a trace message for each theorem instance it generates, which can be helpful when determining patterns.
When multiple patterns are specified together, all of them must match in the current context before `grind` attempts to instantiate the theorem. This is referred to as a _multi-pattern_. This is useful for theorems such as transitivity rules, where multiple premises must be simultaneously present for the rule to apply.
In the following example, `R` is a transitive binary relation over `Int`.

```
opaque R : Int → Int → Prop
axiom Rtrans {x y z : Int} : R x y → R y z → R x z

```

To use the fact that `R` is transitive, `grind` must already be able to satisfy both premises. This is represented using a multi-pattern:

```
grind_pattern Rtrans => R x y, R y z

example {a b c d} : R a b → R b c → R c d → R a d := by
  grind

```

The multi-pattern `R x y`, `R y z` instructs `grind` to instantiate `Rtrans` only when both `R x y` and `R y z` are available in the context. In the example, `grind` applies `Rtrans` to derive `R a c` from `R a b` and `R b c`, and can then repeat the same reasoning to deduce `R a d` from `R a c` and `R c d`.
You can add constraints to restrict theorem instantiation. For example:

```
grind_pattern extract_extract => (as.extract i j).extract k l where
  as =/= #[]

```

The constraint instructs `grind` to instantiate the theorem only if `as` is **not** definitionally equal to `#[]`.
## Constraints
  * `x =/= term`: The term bound to `x` (one of the theorem parameters) is **not** definitionally equal to `term`. The term may contain holes (i.e., `_`).
  * `x =?= term`: The term bound to `x` is definitionally equal to `term`. The term may contain holes (i.e., `_`).
  * `size x < n`: The term bound to `x` has size less than `n`. Implicit arguments and binder types are ignored when computing the size.
  * `depth x < n`: The term bound to `x` has depth less than `n`.
  * `is_ground x`: The term bound to `x` does not contain local variables or meta-variables.
  * `is_value x`: The term bound to `x` is a value. That is, it is a constructor fully applied to value arguments, a literal (`Nat`, `Int`, `String`, etc.), or a lambda `fun x => t`.
  * `is_strict_value x`: Similar to `is_value`, but without lambdas.
  * `not_value x`: The term bound to `x` is a **not** value (see `is_value`).
  * `not_strict_value x`: Similar to `not_value`, but without lambdas.
  * `gen < n`: The theorem instance has generation less than `n`. Recall that each term is assigned a generation, and terms produced by theorem instantiation have a generation that is one greater than the maximal generation of all the terms used to instantiate the theorem. This constraint complements the `gen` option available in `grind`.
  * `max_insts < n`: A new instance is generated only if less than `n` instances have been generated so far.
  * `guard e`: The instantiation is delayed until `grind` learns that `e` is `true` in this state.
  * `check e`: Similar to `guard e`, but `grind` checks whether `e` is implied by its current state by assuming `¬ e` and trying to deduce an inconsistency.


## Example
Consider the following example where `f` is a monotonic function

```
opaque f : Nat → Nat
axiom fMono : x ≤ y → f x ≤ f y

```

and you want to instruct `grind` to instantiate `fMono` for every pair of terms `f x` and `f y` when `x ≤ y` and `x` is **not** definitionally equal to `y`. You can use

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

``grind_pattern` command. One common use is to introduce inequalities about terms, or membership propositions.
We might have
`[variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax") [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]  theorem count_le_size {a : α} {xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α} : count a xs ≤ xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") :=   ...  grind_pattern [count_le_size](The--grind--tactic/Annotating-Libraries-for--grind/#count_le_size "Definition of example") => count a xs `
which will register this inequality as soon as a `count a xs` term is encountered (even if the problem has not previously involved inequalities).
We can also use multi-patterns to be more restrictive, e.g. only introducing an inequality about sizes if the whiteboard already contains facts about sizes:
`theorem `declaration uses `sorry``size_pos_of_mem {xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α} (h : a ∈ xs) : 0 < xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") := sorry grind_pattern [size_pos_of_mem](The--grind--tactic/Annotating-Libraries-for--grind/#size_pos_of_mem "Definition of example") => a ∈ xs, xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") `
Unlike a `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind →[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")` attribute, which would cause this theorem to be instantiated whenever `a ∈ xs` is encountered, this pattern will only be used when `xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")` is already on the whiteboard. (Note that this grind pattern could also be produced using the `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind <=[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")` attribute, which looks at the conclusion first, then backwards through the hypotheses to select patterns. On the other hand, `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")grind →[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")` would select only `a ∈ xs`.)
In Mathlib we might want to enable polynomial reasoning about the sine and cosine functions, and so add a custom grind pattern
`theorem sin_sq_add_cos_sq : [sin](The--grind--tactic/Bigger-Examples/#sin "Definition of example") x ^ 2 + [cos](The--grind--tactic/Bigger-Examples/#cos "Definition of example") x ^ 2 = 1 := ...  grind_pattern [sin_sq_add_cos_sq](The--grind--tactic/Annotating-Libraries-for--grind/#sin_sq_add_cos_sq "Definition of example") => [sin](The--grind--tactic/Bigger-Examples/#sin "Definition of example") x, [cos](The--grind--tactic/Bigger-Examples/#cos "Definition of example") x `
which will instantiate the theorem as soon as **both** `[sin](The--grind--tactic/Bigger-Examples/#sin "Definition of example") x` and `[cos](The--grind--tactic/Bigger-Examples/#cos "Definition of example") x` (with the same `x`) are encountered. This theorem will then automatically enter the Gröbner basis module, and be used to reason about polynomial expressions involving both `[sin](The--grind--tactic/Bigger-Examples/#sin "Definition of example") x` and `[cos](The--grind--tactic/Bigger-Examples/#cos "Definition of example") x`. One both alternatively, more aggressively, write two separate grind patterns so that this theorem instantiated when either `[sin](The--grind--tactic/Bigger-Examples/#sin "Definition of example") x` or `[cos](The--grind--tactic/Bigger-Examples/#cos "Definition of example") x` is encountered.
[←16.9. Linear Arithmetic Solver](The--grind--tactic/Linear-Arithmetic-Solver/#grind-linarith "16.9. Linear Arithmetic Solver")[16.11. Reducibility→](The--grind--tactic/Reducibility/#The-Lean-Language-Reference--The--grind--tactic--Reducibility "16.11. Reducibility")

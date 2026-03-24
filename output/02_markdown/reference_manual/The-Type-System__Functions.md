[←4. The Type System](The-Type-System/#type-system "4. The Type System")[4.2. Propositions→](The-Type-System/Propositions/#propositions "4.2. Propositions")
#  4.1. Functions[🔗](find/?domain=Verso.Genre.Manual.section&name=functions "Permalink")
Function types are a built-in feature of Lean. Functions map the values of one type (the _domain_) into those of another type (the _codomain_), and _function types_ specify the domain and codomain of functions.
There are two kinds of function type: 

Dependent 
    
Dependent function types explicitly name the parameter, and the function's codomain may refer explicitly to this name. Because types can be computed from values, a dependent function may return values from any number of different types, depending on its argument.Dependent functions are sometimes referred to as _dependent products_ , because they correspond to an indexed product of sets. 

Non-Dependent 
    
Non-dependent function types do not include a name for the parameter, and the codomain does not vary based on the specific argument provided. Dependent Function Types
The function `[two](The-Type-System/Functions/#two-_LPAR_in-Dependent-Function-Types_RPAR_ "Definition of example")` returns values in different types, depending on which argument it is called with:
`def two : (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) → [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") b [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") × [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=   fun b =>     [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") b [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")     | [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") => ((), ())     | [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") => "two" `
The body of the function cannot be written with `if...then...else...` because it does not refine types the same way that ``Lean.Parser.Term.match : term`
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match) does.
[Live ↪](javascript:openLiveLink\("CYUwZgBALg7g9hAXBAFAIyRAQnOAbASgkCTCCAS0gygAsQA7CAVTrKggHWmW2Q8BnEBADKUAE5k6AcyQBeAFAQIYAK4MMMgHwLFEALYBDKAGNqEDDFbVtigD7RRywZtQoCAGlQEC1iHbD7+Jw0IACJYOBCgA"\))
In Lean's core language, all function types are dependent: non-dependent function types are dependent function types in which the parameter name does not occur in the [codomain](The-Type-System/Functions/#--tech-term-codomain). Additionally, two dependent function types that have different parameter names may be definitionally equal if renaming the parameter makes them equal. However, the Lean elaborator does not introduce a local binding for non-dependent functions' parameters.
Definitional Equality of Dependent and Non-Dependent Functions
The types `(x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` and `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` are definitionally equal:
`example : ((x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) = ([Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :=   [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
Similarly, the types `(n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → n + 1 = 1 + n` and `(k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → k + 1 = 1 + k` are definitionally equal:
`example : ((n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → n + 1 = 1 + n) = ((k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → k + 1 = 1 + k) :=   [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAueAKFInwHJgC4Ep5AkwngGVcAnASwDsBzQgXlR12LMtoaUYCh54FAGYxevUJFgJkaGplaEScgNTwAjPGYbVNJqhQBreXkXwjqjVviqDhRHwHCYQA"\))
Non-Dependent Functions Don't Bind Variables
A dependent function is required in the following statement that all elements of an array are non-zero:
`def AllNonZero (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : Prop :=   (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → (lt : i < xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) → xs[i] ≠ 0 `
This is because the elaborator for array access requires a proof that the index is in bounds. The non-dependent version of the statement does not introduce this assumption:
`def AllNonZero (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : Prop :=   (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → (i < xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) → `failed to prove index is valid, possible solutions:   - Use `have`-expressions to prove the index is valid   - Use `a[i]!` notation instead, runtime check is performed, and 'Panic' error message is produced if index is not valid   - Use `a[i]?` notation instead, result is an `Option` type   - Use `a[i]'h` notation instead, where `h` is a proof that index is valid xs:[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")i:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")`xs[i] ≠ 0 `
```
failed to prove index is valid, possible solutions:
  - Use `have`-expressions to prove the index is valid
  - Use `a[i]!` notation instead, runtime check is performed, and 'Panic' error message is produced if index is not valid
  - Use `a[i]?` notation instead, result is an `Option` type
  - Use `a[i]'h` notation instead, where `h` is a proof that index is valid
xs:[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")i:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")
```

While the core type theory does not feature [implicit](Terms/Functions/#--tech-term-implicit) parameters, function types do include an indication of whether the parameter is implicit. This information is used by the Lean elaborator, but it does not affect type checking or definitional equality in the core theory and can be ignored when thinking only about the core type theory.
Definitional Equality of Implicit and Explicit Function Types
The types `{α : Type} → (x : α) → α` and `(α : Type) → (x : α) → α` are definitionally equal, even though the first parameter is implicit in one and explicit in the other.
`example :     ({α : Type} → (x : α) → α)     =     ((α : Type) → (x : α) → α)   := [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAuAUPN8AUBvQjcBPgCoCeUwAvvIEmEmI+OAlFfA6ugLytoYZ6KEnBG1DLT4MmLNIjbwATgDMYQA"\))
##  4.1.1. Function Abstractions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The-Type-System--Functions--Function-Abstractions "Permalink")
In Lean's type theory, functions are created using _function abstractions_ that bind a variable. In various communities, function abstractions are also known as _lambdas_ , due to Alonzo Church's notation for them, or _anonymous functions_ because they don't need to be defined with a name in the global environment. When the function is applied, the result is found by [β-reduction](The-Type-System/#--tech-term-___): substituting the argument for the bound variable. In compiled code, this happens strictly: the argument must already be a value. When type checking, there are no such restrictions; the equational theory of definitional equality allows β-reduction with any term.
In Lean's [term language](Terms/Functions/#function-terms), function abstractions may take multiple parameters or use pattern matching. These features are translated to simpler operations in the core language, where all functions abstractions take exactly one parameter. Not all functions originate from abstractions: [type constructors](The-Type-System/Inductive-Types/#--tech-term-type-constructors), [constructors](The-Type-System/Inductive-Types/#--tech-term-constructors), and [recursors](The-Type-System/Inductive-Types/#--tech-term-recursor) may have function types, but they cannot be defined using function abstractions alone.
##  4.1.2. Currying[🔗](find/?domain=Verso.Genre.Manual.section&name=currying "Permalink")
In Lean's core type theory, every function maps each element of the [domain](The-Type-System/Functions/#--tech-term-domain) to a single element of the [codomain](The-Type-System/Functions/#--tech-term-codomain). In other words, every function expects exactly one parameter. Multiple-parameter functions are implemented by defining higher-order functions that, when supplied with the first parameter, return a new function that expects the remaining parameters. This encoding is called _currying_ , popularized by and named after Haskell B. Curry. Lean's syntax for defining functions, specifying their types, and applying them creates the illusion of multiple-parameter functions, but the result of elaboration contains only single-parameter functions.
##  4.1.3. Extensionality[🔗](find/?domain=Verso.Genre.Manual.section&name=function-extensionality "Permalink")
Definitional equality of functions in Lean is _intensional_. This means that definitional equality is defined _syntactically_ , modulo renaming of bound variables and [reduction](The-Type-System/#--tech-term-reduction). To a first approximation, this means that two functions are definitionally equal if they implement the same algorithm, rather than the usual mathematical notion of equality that states that two functions are equal if they map equal elements of the [domain](The-Type-System/Functions/#--tech-term-domain) to equal elements of the [codomain](The-Type-System/Functions/#--tech-term-codomain).
Definitional equality is used by the type checker, so it's important that it be predictable. The syntactic character of intensional equality means that the algorithm to check it can be feasibly specified. Checking extensional equality involves proving essentially arbitrary theorems about equality of functions, and there is no clear specification for an algorithm to check it. This makes extensional equality a poor choice for a type checker. Function extensionality is instead made available as a reasoning principle that can be invoked when proving the [proposition](The-Type-System/Propositions/#--tech-term-Propositions) that two functions are equal.
In addition to reduction and renaming of bound variables, definitional equality does support one limited form of extensionality, called [_η-equivalence_](The-Type-System/#--tech-term-___-equivalence), in which functions are equal to abstractions whose bodies apply them to the argument. Given `[f](releases/v4.27.0/#f "Definition of example")` with type `(x : α) → β x`, `[f](releases/v4.27.0/#f "Definition of example")` is definitionally equal to `fun x => [f](releases/v4.27.0/#f "Definition of example") x`.
When reasoning about functions, the theorem `[funext](The-Type-System/Functions/#funext "Documentation for funext")`Unlike some intensional type theories, `[funext](The-Type-System/Functions/#funext "Documentation for funext")` is a theorem in Lean. It can be proved [using quotient types](The-Type-System/Quotients/#quotient-funext). or the corresponding tactics `[funext](Tactic-Proofs/Tactic-Reference/#funext-next "Documentation for tactic")` or `[ext](Tactic-Proofs/Tactic-Reference/#ext "Documentation for tactic")` can be used to prove that two functions are equal if they map equal inputs to equal outputs.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=funext "Permalink")theorem
```


funext.{u, v} {α : Sort u} {β : α → Sort v} {f g : (x : α) → β x}
  (h : ∀ (x : α), f x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g x) : f [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g


funext.{u, v} {α : Sort u}
  {β : α → Sort v} {f g : (x : α) → β x}
  (h : ∀ (x : α), f x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g x) : f [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g


```

**Function extensionality.** If two functions return equal results for all possible arguments, then they are equal.
It is called “extensionality” because it provides a way to prove two objects equal based on the properties of the underlying mathematical functions, rather than based on the syntax used to denote them. Function extensionality is a theorem that can be [proved using quotient types](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=quotient-funext).
##  4.1.4. Totality and Termination[🔗](find/?domain=Verso.Genre.Manual.section&name=totality "Permalink")
Functions can be defined recursively using ``Lean.Parser.Command.declaration : command```def`. From the perspective of Lean's logic, all functions are _total_ , meaning that they map each element of the [domain](The-Type-System/Functions/#--tech-term-domain) to an element of the [codomain](The-Type-System/Functions/#--tech-term-codomain) in finite time.Some programming language communities use the term _total_ in a different sense, where functions are considered total if they do not crash due to unhandled cases but non-termination is ignored. The values of total functions are defined for all type-correct arguments, and they cannot fail to terminate or crash due to a missing case in a pattern match.
While the logical model of Lean considers all functions to be total, Lean is also a practical programming language that provides certain “escape hatches”. Functions that have not been proven to terminate can still be used in Lean's logic as long as their [codomain](The-Type-System/Functions/#--tech-term-codomain) is proven nonempty. These functions are treated as uninterpreted functions by Lean's logic, and their computational behavior is ignored. In compiled code, these functions are treated just like any others. Other functions may be marked unsafe; these functions are not available to Lean's logic at all. The section on [partial and unsafe function definitions](Definitions/Recursive-Definitions/#partial-unsafe) contains more detail on programming with recursive functions.
Similarly, operations that should fail at runtime in compiled code, such as out-of-bounds access to an array, can only be used when the resulting type is known to be inhabited. These operations result in an arbitrarily chosen inhabitant of the type in Lean's logic (specifically, the one specified in the type's `[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited")` instance).
Panic
The function `[thirdChar](The-Type-System/Functions/#thirdChar-_LPAR_in-Panic_RPAR_ "Definition of example")` extracts the third element of an array, or panics if the array has two or fewer elements:
`def thirdChar (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") := xs[2]! `
The (nonexistent) third elements of `#['!']` and `#['-', 'x']` are equal, because they result in the same arbitrarily-chosen character:
`example : [thirdChar](The-Type-System/Functions/#thirdChar-_LPAR_in-Panic_RPAR_ "Definition of example") #['!'] = [thirdChar](The-Type-System/Functions/#thirdChar-_LPAR_in-Panic_RPAR_ "Definition of example") #['-', 'x'] := [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
Indeed, both are equal to `'A'`, which happens to be the default fallback for `[Char](Basic-Types/Characters/#Char___mk "Documentation for Char")`:
`example : [thirdChar](The-Type-System/Functions/#thirdChar-_LPAR_in-Panic_RPAR_ "Definition of example") #['!'] = 'A' := [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") example : [thirdChar](The-Type-System/Functions/#thirdChar-_LPAR_in-Panic_RPAR_ "Definition of example") #['-', 'x'] = 'A' := [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
[Live ↪](javascript:openLiveLink\("CYUwZgBALgFglgJ2AYRgQwRAFADwM4QBcEAgggmgJ4SoYCURN6mhAvBPgNoBMAugIQAoQSBxoAtgAcANiEaxEKZhADEnAOT91vCOwVJamNeoC06gDQR1ObUXYIw04aIky5xfUoyqNWne3USdTsIBycXKVl5eANlYzNLa1sAoJCwoA"\))
##  4.1.5. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=function-api "Permalink")
The `Function` namespace contains general-purpose helpers for working with functions.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Function.comp "Permalink")def
```


Function.comp.{u, v, w} {α : Sort u} {β : Sort v} {δ : Sort w}
  (f : β → δ) (g : α → β) : α → δ


Function.comp.{u, v, w} {α : Sort u}
  {β : Sort v} {δ : Sort w} (f : β → δ)
  (g : α → β) : α → δ


```

Function composition, usually written with the infix operator `∘`. A new function is created from two existing functions, where one function's output is used as input to the other.
Examples:
  * `[Function.comp](The-Type-System/Functions/#Function___comp "Documentation for Function.comp") [List.reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse") ([List.drop](Basic-Types/Linked-Lists/#List___drop "Documentation for List.drop") 2) [3, 2, 4, 1] = [1, 4]`
  * `([List.reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse") ∘ [List.drop](Basic-Types/Linked-Lists/#List___drop "Documentation for List.drop") 2) [3, 2, 4, 1] = [1, 4]`


Conventions for notations in identifiers:
  * The recommended spelling of `∘` in identifiers is `comp`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Function.const "Permalink")def
```


Function.const.{u, v} {α : Sort u} (β : Sort v) (a : α) : β → α


Function.const.{u, v} {α : Sort u}
  (β : Sort v) (a : α) : β → α


```

The constant function that ignores its argument.
If `a : α`, then `[Function.const](The-Type-System/Functions/#Function___const "Documentation for Function.const") β a : β → α` is the “constant function with value `a`”. For all arguments `b : β`, `[Function.const](The-Type-System/Functions/#Function___const "Documentation for Function.const") β a b = a`.
Examples:
  * `[Function.const](The-Type-System/Functions/#Function___const "Documentation for Function.const") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") 10 [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") = 10`
  * `[Function.const](The-Type-System/Functions/#Function___const "Documentation for Function.const") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") 10 [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") = 10`
  * `[Function.const](The-Type-System/Functions/#Function___const "Documentation for Function.const") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") 10 "any string" = 10`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Function.curry "Permalink")def
```


Function.curry.{u_1, u_2, u_3} {α : Type u_1} {β : Type u_2}
  {φ : Sort u_3} : (α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β → φ) → α → β → φ


Function.curry.{u_1, u_2, u_3}
  {α : Type u_1} {β : Type u_2}
  {φ : Sort u_3} : (α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β → φ) → α → β → φ


```

Transforms a function from pairs into an equivalent two-parameter function.
Examples:
  * `[Function.curry](The-Type-System/Functions/#Function___curry "Documentation for Function.curry") (fun (x, y) => x + y) 3 5 = 8`
  * `[Function.curry](The-Type-System/Functions/#Function___curry "Documentation for Function.curry") [Prod.swap](Basic-Types/Tuples/#Prod___swap "Documentation for Prod.swap") 3 "five" = ("five", 3)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Function.uncurry "Permalink")def
```


Function.uncurry.{u_1, u_2, u_3} {α : Type u_1} {β : Type u_2}
  {φ : Sort u_3} : (α → β → φ) → α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β → φ


Function.uncurry.{u_1, u_2, u_3}
  {α : Type u_1} {β : Type u_2}
  {φ : Sort u_3} : (α → β → φ) → α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β → φ


```

Transforms a two-parameter function into an equivalent function from pairs.
Examples:
  * `[Function.uncurry](The-Type-System/Functions/#Function___uncurry "Documentation for Function.uncurry") [List.drop](Basic-Types/Linked-Lists/#List___drop "Documentation for List.drop") (1, ["a", "b", "c"]) = ["b", "c"]`
  * `[("orange", 2), ("android", 3) ].[map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map") ([Function.uncurry](The-Type-System/Functions/#Function___uncurry "Documentation for Function.uncurry") [String.take](Basic-Types/Strings/#String___take "Documentation for String.take")) = ["or", "and"]`


###  4.1.5.1. Properties[🔗](find/?domain=Verso.Genre.Manual.section&name=function-api-properties "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Function.Injective "Permalink")def
```


Function.Injective.{u_1, u_2} {α : Sort u_1} {β : Sort u_2}
  (f : α → β) : Prop


Function.Injective.{u_1, u_2}
  {α : Sort u_1} {β : Sort u_2}
  (f : α → β) : Prop


```

A function `f : α → β` is called injective if `f x = f y` implies `x = y`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Function.Surjective "Permalink")def
```


Function.Surjective.{u_1, u_2} {α : Sort u_1} {β : Sort u_2}
  (f : α → β) : Prop


Function.Surjective.{u_1, u_2}
  {α : Sort u_1} {β : Sort u_2}
  (f : α → β) : Prop


```

A function `f : α → β` is called surjective if every `b : β` is equal to `f a` for some `a : α`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Function.LeftInverse "Permalink")def
```


Function.LeftInverse.{u_1, u_2} {α : Sort u_1} {β : Sort u_2}
  (g : β → α) (f : α → β) : Prop


Function.LeftInverse.{u_1, u_2}
  {α : Sort u_1} {β : Sort u_2}
  (g : β → α) (f : α → β) : Prop


```

`LeftInverse g f` means that `g` is a left inverse to `f`. That is, `g ∘ f = id`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Function.HasLeftInverse "Permalink")def
```


Function.HasLeftInverse.{u_1, u_2} {α : Sort u_1} {β : Sort u_2}
  (f : α → β) : Prop


Function.HasLeftInverse.{u_1, u_2}
  {α : Sort u_1} {β : Sort u_2}
  (f : α → β) : Prop


```

`HasLeftInverse f` means that `f` has an unspecified left inverse.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Function.RightInverse "Permalink")def
```


Function.RightInverse.{u_1, u_2} {α : Sort u_1} {β : Sort u_2}
  (g : β → α) (f : α → β) : Prop


Function.RightInverse.{u_1, u_2}
  {α : Sort u_1} {β : Sort u_2}
  (g : β → α) (f : α → β) : Prop


```

`RightInverse g f` means that `g` is a right inverse to `f`. That is, `f ∘ g = id`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Function.HasRightInverse "Permalink")def
```


Function.HasRightInverse.{u_1, u_2} {α : Sort u_1} {β : Sort u_2}
  (f : α → β) : Prop


Function.HasRightInverse.{u_1, u_2}
  {α : Sort u_1} {β : Sort u_2}
  (f : α → β) : Prop


```

`HasRightInverse f` means that `f` has an unspecified right inverse.
[←4. The Type System](The-Type-System/#type-system "4. The Type System")[4.2. Propositions→](The-Type-System/Propositions/#propositions "4.2. Propositions")

[←20.13. Tuples](Basic-Types/Tuples/#tuples "20.13. Tuples")[20.15. Linked Lists→](Basic-Types/Linked-Lists/#List "20.15. Linked Lists")
#  20.14. Sum Types[🔗](find/?domain=Verso.Genre.Manual.section&name=sum-types "Permalink")
_Sum types_ represent a choice between two types: an element of the sum is an element of one of the other types, paired with an indication of which type it came from. Sums are also known as disjoint unions, discriminated unions, or tagged unions. The constructors of a sum are also called _injections_ ; mathematically, they can be considered as injective functions from each summand to the sum.
There are two varieties of the sum type:
  * `[Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")` is [polymorphic](The-Type-System/Universes/#--tech-term-universe-polymorphism) over all `Type` [universes](The-Type-System/Universes/#--tech-term-universes), and is never a [proposition](The-Type-System/Propositions/#--tech-term-Propositions).
  * `[PSum](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum")` is allows the summands to be propositions or types. Unlike `[Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or")`, the `[PSum](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum")` of two propositions is still a type, and non-propositional code can check which injection was used to construct a given value.


Manually-written Lean code almost always uses only `[Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")`, while `[PSum](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum")` is used as part of the implementation of proof automation. This is because it imposes problematic constraints that universe level unification cannot solve. In particular, this type is in the universe `Sort (max 1 u v)`, which can cause problems for universe level unification because the equation `max 1 u v = ?u + 1` has no solution in level arithmetic. `PSum` is usually only used in automation that constructs sums of arbitrary types.
[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=Either%E2%86%AASum "Permalink")inductive type
```


Sum.{u, v} (α : Type u) (β : Type v) : Type (max u v)


Sum.{u, v} (α : Type u) (β : Type v) :
  Type (max u v)


```

The disjoint union of types `α` and `β`, ordinarily written `α ⊕ β`.
An element of `α ⊕ β` is either an `a : α` wrapped in `[Sum.inl](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inl")` or a `b : β` wrapped in `[Sum.inr](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inr")`. `α ⊕ β` is not equivalent to the set-theoretic union of `α` and `β` because its values include an indication of which of the two types was chosen. The union of a singleton set with itself contains one element, while `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") ⊕ [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")` contains distinct values `inl ()` and `inr ()`.
#  Constructors

```
inl.{u, v} {α : Type u} {β : Type v} (val : α) : α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β
```

Left injection into the sum type `α ⊕ β`.

```
inr.{u, v} {α : Type u} {β : Type v} (val : β) : α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β
```

Right injection into the sum type `α ⊕ β`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=PSum.inl "Permalink")inductive type
```


PSum.{u, v} (α : Sort u) (β : Sort v) : Sort (max (max 1 u) v)


PSum.{u, v} (α : Sort u) (β : Sort v) :
  Sort (max (max 1 u) v)


```

The disjoint union of arbitrary sorts `α` `β`, or `α ⊕' β`.
It differs from `α ⊕ β` in that it allows `α` and `β` to have arbitrary sorts `Sort u` and `Sort v`, instead of restricting them to `Type u` and `Type v`. This means that it can be used in situations where one side is a proposition, like `[True](Basic-Propositions/Truth/#True___intro "Documentation for True") ⊕' [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`. However, the resulting universe level constraints are often more difficult to solve than those that result from `[Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")`.
#  Constructors

```
inl.{u, v} {α : Sort u} {β : Sort v} (val : α) : α [⊕'](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum") β
```

Left injection into the sum type `α ⊕' β`.

```
inr.{u, v} {α : Sort u} {β : Sort v} (val : β) : α [⊕'](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum") β
```

Right injection into the sum type `α ⊕' β`.
##  20.14.1. Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=sum-syntax "Permalink")
The names `[Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")` and `[PSum](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum")` are rarely written explicitly. Most code uses the corresponding infix operators.
syntaxSum Types

```
term ::= ...
    | 


The disjoint union of types α and β, ordinarily written α ⊕ β.


An element of α ⊕ β is either an a : α wrapped in Sum.inl or a b : β wrapped in Sum.inr.
α ⊕ β is not equivalent to the set-theoretic union of α and β because its values include an
indication of which of the two types was chosen. The union of a singleton set with itself contains
one element, while Unit ⊕ Unit contains distinct values inl () and inr ().


term ⊕ term
```

`α ⊕ β` is notation for `[Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") α β`.
syntaxPotentially-Propositional Sum Types

```
term ::= ...
    | 


The disjoint union of arbitrary sorts α β, or α ⊕' β.


It differs from α ⊕ β in that it allows α and β to have arbitrary sorts Sort u and Sort v,
instead of restricting them to Type u and Type v. This means that it can be used in situations
where one side is a proposition, like True ⊕' Nat. However, the resulting universe level
constraints are often more difficult to solve than those that result from Sum.


term ⊕' term
```

`α ⊕' β` is notation for `[PSum](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum") α β`.
##  20.14.2. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=sum-api "Permalink")
Sum types are primarily used with [pattern matching](Terms/Pattern-Matching/#--tech-term-Pattern-matching) rather than explicit function calls from an API. As such, their primary API is the constructors `[inl](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inl")` and `[inr](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inr")`.
###  20.14.2.1. Case Distinction[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Sum-Types--API-Reference--Case-Distinction "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Sum.isLeft "Permalink")def
```


Sum.isLeft.{u_1, u_2} {α : Type u_1} {β : Type u_2} : α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Sum.isLeft.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} : α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a sum is the left injection `inl`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Sum.isRight "Permalink")def
```


Sum.isRight.{u_1, u_2} {α : Type u_1} {β : Type u_2} : α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Sum.isRight.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} : α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a sum is the right injection `inr`.
###  20.14.2.2. Extracting Values[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Sum-Types--API-Reference--Extracting-Values "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Sum.elim "Permalink")def
```


Sum.elim.{u_1, u_2, u_3} {α : Type u_1} {β : Type u_2} {γ : Sort u_3}
  (f : α → γ) (g : β → γ) : α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β → γ


Sum.elim.{u_1, u_2, u_3} {α : Type u_1}
  {β : Type u_2} {γ : Sort u_3}
  (f : α → γ) (g : β → γ) : α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β → γ


```

Case analysis for sums that applies the appropriate function `f` or `g` after checking which constructor is present.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Sum.getLeft "Permalink")def
```


Sum.getLeft.{u_1, u_2} {α : Type u_1} {β : Type u_2} (ab : α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β) :
  ab.[isLeft](Basic-Types/Sum-Types/#Sum___isLeft "Documentation for Sum.isLeft") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → α


Sum.getLeft.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} (ab : α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β) :
  ab.[isLeft](Basic-Types/Sum-Types/#Sum___isLeft "Documentation for Sum.isLeft") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → α


```

Retrieves the contents from a sum known to be `inl`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Sum.getLeft? "Permalink")def
```


Sum.getLeft?.{u_1, u_2} {α : Type u_1} {β : Type u_2} : α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Sum.getLeft?.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} : α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Checks whether a sum is the left injection `inl` and, if so, retrieves its contents.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Sum.getRight "Permalink")def
```


Sum.getRight.{u_1, u_2} {α : Type u_1} {β : Type u_2} (ab : α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β) :
  ab.[isRight](Basic-Types/Sum-Types/#Sum___isRight "Documentation for Sum.isRight") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → β


Sum.getRight.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} (ab : α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β) :
  ab.[isRight](Basic-Types/Sum-Types/#Sum___isRight "Documentation for Sum.isRight") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → β


```

Retrieves the contents from a sum known to be `inr`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Sum.getRight? "Permalink")def
```


Sum.getRight?.{u_1, u_2} {α : Type u_1} {β : Type u_2} :
  α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


Sum.getRight?.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} : α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


```

Checks whether a sum is the right injection `inr` and, if so, retrieves its contents.
###  20.14.2.3. Transformations[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Sum-Types--API-Reference--Transformations "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Sum.map "Permalink")def
```


Sum.map.{u_1, u_2, u_3, u_4} {α : Type u_1} {α' : Type u_2}
  {β : Type u_3} {β' : Type u_4} (f : α → α') (g : β → β') :
  α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β → α' [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β'


Sum.map.{u_1, u_2, u_3, u_4}
  {α : Type u_1} {α' : Type u_2}
  {β : Type u_3} {β' : Type u_4}
  (f : α → α') (g : β → β') :
  α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β → α' [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β'


```

Transforms a sum according to functions on each type.
This function maps `α ⊕ β` to `α' ⊕ β'`, sending `α` to `α'` and `β` to `β'`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Sum.swap "Permalink")def
```


Sum.swap.{u_1, u_2} {α : Type u_1} {β : Type u_2} : α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β → β [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") α


Sum.swap.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} : α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β → β [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") α


```

Swaps the factors of a sum type.
The constructor `[Sum.inl](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inl")` is replaced with `[Sum.inr](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inr")`, and vice versa.
###  20.14.2.4. Inhabited[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Sum-Types--API-Reference--Inhabited "Permalink")
The `[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited")` definitions for `[Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")` and `[PSum](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum")` are not registered as instances. This is because there are two separate ways to construct a default value (via `[inl](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inl")` or `[inr](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inr")`), and instance synthesis might result in either choice. The result could be situations where two identically-written terms elaborate differently and are not [definitionally equal](The-Type-System/#--tech-term-definitional-equality).
Both types have `[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty")` instances, for which [proof irrelevance](The-Type-System/#--tech-term-proof-irrelevance) makes the choice of `[inl](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inl")` or `[inr](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inr")` not matter. This is enough to enable `partial` functions. For situations that require an `[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited")` instance, such as programs that use `panic!`, the instance can be explicitly used by adding it to the local context with ``Lean.Parser.Term.have : term`
`have` is used to declare local hypotheses and opaque local definitions.
It has the same syntax as `let`, and it is equivalent to `let +nondep`, creating a _nondependent_ let expression.
``have` or ``Lean.Parser.Term.let : term`
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
Inhabited Sum Types
In Lean's logic, ``Lean.Parser.Term.panic : term`
``panic!` is equivalent to the default value specified in its type's `[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited")` instance. This means that the type must have such an instance—a `[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty")` instance combined with the axiom of choice would render the program non-computable.
Products have the right instance:
`example : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") × [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := panic! "Can't find it" `
Sums do not, by default:
`example : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ⊕ [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := `failed to synthesize instance of type class   [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")[)](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`panic! "Can't find it" `
```
failed to synthesize instance of type class
  [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")[)](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```

The desired instance can be made available to instance synthesis using ``Lean.Parser.Term.have : term`
``have`:
`example : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ⊕ [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=   have : [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") ([Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ⊕ [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) := [Sum.inhabitedLeft](Basic-Types/Sum-Types/#Sum___inhabitedLeft "Documentation for Sum.inhabitedLeft")   panic! "Can't find it" `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAueA5MAXeB1+BldATgJYB2A5kgLzxRglEDGAhPAEQDCdA5JgGakATeEXSsAUGNCRYCZGkyBUojyFSFRJTHx4ACzAA3WfACSJXQCMRwIQAp58JfmLkAlFTwBXCADpS5ywIAZYF50TRo6RhYObj5BYVEgA"\))
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Sum.inhabitedLeft "Permalink")def
```


Sum.inhabitedLeft.{u, v} {α : Type u} {β : Type v} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] :
  [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β[)](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")


Sum.inhabitedLeft.{u, v} {α : Type u}
  {β : Type v} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] :
  [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β[)](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")


```

If the left type in a sum is inhabited then the sum is inhabited.
This is not an instance to avoid non-canonical instances when both the left and right types are inhabited.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Sum.inhabitedRight "Permalink")def
```


Sum.inhabitedRight.{u, v} {α : Type u} {β : Type v} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") β] :
  [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β[)](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")


Sum.inhabitedRight.{u, v} {α : Type u}
  {β : Type v} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") β] :
  [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β[)](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")


```

If the right type in a sum is inhabited then the sum is inhabited.
This is not an instance to avoid non-canonical instances when both the left and right types are inhabited.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=PSum.inhabitedLeft "Permalink")def
```


PSum.inhabitedLeft.{u_1, u_2} {α : Sort u_1} {β : Sort u_2}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] : [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum")α [⊕'](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum") β[)](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum")


PSum.inhabitedLeft.{u_1, u_2}
  {α : Sort u_1} {β : Sort u_2}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] : [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum")α [⊕'](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum") β[)](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum")


```

If the left type in a sum is inhabited then the sum is inhabited.
This is not an instance to avoid non-canonical instances when both the left and right types are inhabited.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=PSum.inhabitedRight "Permalink")def
```


PSum.inhabitedRight.{u_1, u_2} {α : Sort u_1} {β : Sort u_2}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") β] : [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum")α [⊕'](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum") β[)](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum")


PSum.inhabitedRight.{u_1, u_2}
  {α : Sort u_1} {β : Sort u_2}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") β] : [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum")α [⊕'](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum") β[)](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum")


```

If the right type in a sum is inhabited then the sum is inhabited.
This is not an instance to avoid non-canonical instances when both the left and right types are inhabited.
[←20.13. Tuples](Basic-Types/Tuples/#tuples "20.13. Tuples")[20.15. Linked Lists→](Basic-Types/Linked-Lists/#List "20.15. Linked Lists")

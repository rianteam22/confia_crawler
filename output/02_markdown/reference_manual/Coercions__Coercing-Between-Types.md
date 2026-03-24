[←11.1. Coercion Insertion](Coercions/Coercion-Insertion/#coercion-insertion "11.1. Coercion Insertion")[11.3. Coercing to Sorts→](Coercions/Coercing-to-Sorts/#sort-coercion "11.3. Coercing to Sorts")
#  11.2. Coercing Between Types[🔗](find/?domain=Verso.Genre.Manual.section&name=ordinary-coercion "Permalink")
Coercions between types are inserted when the Lean elaborator successfully constructs a term, inferring its type, in a context where a term of some other type was expected. Before signaling an error, the elaborator attempts to insert a coercion from the inferred type to the expected type by synthesizing an instance of `[CoeT](Coercions/Coercing-Between-Types/#CoeT___mk "Documentation for CoeT")`. There are two ways that this might succeed:
  1. There could be a chain of coercions from the inferred type to the expected type through a number of intermediate types. These chained coercions are selected based on the inferred type and the expected type, but not the term being coerced.
  2. There could be a single dependent coercion from the inferred type to the expected type. Dependent coercions take the term being coerced into account as well as the inferred and expected types, but they cannot be chained.


The simplest way to define a non-dependent coercion is by implementing a `[Coe](Coercions/#Coe___mk "Documentation for Coe")` instance, which is enough to synthesize a `[CoeT](Coercions/Coercing-Between-Types/#CoeT___mk "Documentation for CoeT")` instance. This instance participates in chaining, and may be applied any number of times. The expected type of the expression is used to drive synthesis of `[Coe](Coercions/#Coe___mk "Documentation for Coe")` instances, rather than the inferred type. For instances that can be used at most once, or instances in which the inferred type should drive synthesis, one of the other coercion classes may be needed.
Defining Coercions
The type `[Even](Introduction/#Even___zero-next "Documentation for Even")` represents the even natural numbers.
`structure Even where   number : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   isEven : number % 2 = 0 `
A coercion allows even numbers to be used where natural numbers are expected. The `coe` attribute marks the projection as a coercion so that it can be shown accordingly in proof states and error messages, as described in the [section on implementing coercions](Coercions/Coercing-Between-Types/#coercion-impl).
`[attribute](Attributes/#Lean___Parser___Command___attribute "Documentation for syntax") [[coe](Coercions/Coercing-Between-Types/#Lean___Attr___coe "Documentation for syntax")] [Even.number](Coercions/Coercing-Between-Types/#Even___number-_LPAR_in-Defining-Coercions_RPAR_ "Definition of example")  instance : [Coe](Coercions/#Coe___mk "Documentation for Coe") [Even](Introduction/#Even___zero-next "Documentation for Even") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") where   [coe](Coercions/#Coe___mk "Documentation for Coe.coe") := [Even.number](Coercions/Coercing-Between-Types/#Even___number-_LPAR_in-Defining-Coercions_RPAR_ "Definition of example") `
With this coercion in place, even numbers can be used where natural numbers are expected.
`def four : [Even](Introduction/#Even___zero-next "Documentation for Even") := ⟨4, by⊢ 4 [%](Type-Classes/Basic-Classes/#HMod___mk "Documentation for HMod.hMod") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 [omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic")All goals completed! 🐙⟩  `5`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ([four](Coercions/Coercing-Between-Types/#four-_LPAR_in-Defining-Coercions_RPAR_ "Definition of example") : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) + 1 `
```
5
```

Due to coercion chaining, there is also a coercion from `[Even](Introduction/#Even___zero-next "Documentation for Even")` to `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` formed by chaining the `[Coe](Coercions/#Coe___mk "Documentation for Coe") [Even](Introduction/#Even___zero-next "Documentation for Even") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` instance with the existing coercion from `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` to `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`:
``-1`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ([four](Coercions/Coercing-Between-Types/#four-_LPAR_in-Defining-Coercions_RPAR_ "Definition of example") : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) - 5 `
```
-1
```

[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgKIDd4DtEHcAW8EAoRRDCAWwCMDEAuRAOQEMRjEBLYNTO0i6sIgCkiAEyIAvIgAMhQi3DtKEEEgDaUAPbwAuinQYAdGSoE57DKCYYoSegGFt+nsxA58RElrtTuRkwJyACbwAGaIoZpwvH50UoAX5AAsADSIlACeiJrk8ADmTICX5HIAxPCoTAA2iAAUkdH0rgCUiADUiACMJWWVNXWC9ACSGCDNALSIAKxAA"\))
Dependent coercions are needed when the specific term being coerced is required in order to determine whether or how to coerce the term: for example, only decidable propositions can be coerced to `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`, so the proposition in question must occur as part of the instance's type so that it can require the `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` instance. Non-dependent coercions are used whenever all values of the inferred type can be coerced to the target type.
Defining Dependent Coercions
The string `"four"` can be coerced into the natural number `4` with this instance declaration:
`instance : [CoeDep](Coercions/Coercing-Between-Types/#CoeDep___mk "Documentation for CoeDep") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") "four" [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") where   [coe](Coercions/Coercing-Between-Types/#CoeDep___mk "Documentation for CoeDep.coe") := 4  `4`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ("four" : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) `
```
4
```

Ordinary type errors are produced for other strings:
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") `Type mismatch   "three" has type   [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") but is expected to have type   [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`("three" : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) `
```
Type mismatch
  "three"
has type
  [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
but is expected to have type
  [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

[Live ↪](javascript:openLiveLink\("JYOwzgLghiDGCmACAXIgwge3gEXgB0QGUIAnUAc0QCIAzDAVxKsQDkoJEB3AC3hPgBQiRLCwoAvIgAsAgQGJ4ANygAbRAApaDJilbsAlEA"\))
Non-dependent coercions may be chained: if there is a coercion from `α` to `β` and from `β` to `γ`, then there is also a coercion from `α` to `γ`.  The chain should be in the form `[CoeHead](Coercions/Coercing-Between-Types/#CoeHead___mk "Documentation for CoeHead")``???``[CoeOut](Coercions/Coercing-Between-Types/#CoeOut___mk "Documentation for CoeOut")``∗*∗``[Coe](Coercions/#Coe___mk "Documentation for Coe")``∗*∗``[CoeTail](Coercions/Coercing-Between-Types/#CoeTail___mk "Documentation for CoeTail")``???`, which is to say it may consist of:
  * An optional instance of `[CoeHead](Coercions/Coercing-Between-Types/#CoeHead___mk "Documentation for CoeHead") α α'`, followed by
  * Zero or more instances of `[CoeOut](Coercions/Coercing-Between-Types/#CoeOut___mk "Documentation for CoeOut") α' …`, …, `[CoeOut](Coercions/Coercing-Between-Types/#CoeOut___mk "Documentation for CoeOut") … α''`, followed by
  * Zero or more instances of `[Coe](Coercions/#Coe___mk "Documentation for Coe") α'' …`, …, `[Coe](Coercions/#Coe___mk "Documentation for Coe") … β'`, followed by
  * An optional instance of `[CoeTail](Coercions/Coercing-Between-Types/#CoeTail___mk "Documentation for CoeTail") β' γ`


Most coercions can be implemented as instances of `[Coe](Coercions/#Coe___mk "Documentation for Coe")`. `[CoeHead](Coercions/Coercing-Between-Types/#CoeHead___mk "Documentation for CoeHead")`, `[CoeOut](Coercions/Coercing-Between-Types/#CoeOut___mk "Documentation for CoeOut")`, and `[CoeTail](Coercions/Coercing-Between-Types/#CoeTail___mk "Documentation for CoeTail")` are needed in certain special situations.
`[CoeHead](Coercions/Coercing-Between-Types/#CoeHead___mk "Documentation for CoeHead")` and `[CoeOut](Coercions/Coercing-Between-Types/#CoeOut___mk "Documentation for CoeOut")` instances are chained from the inferred type towards the expected type. In other words, information in the type found for the term is used to resolve a chain of instances. `[Coe](Coercions/#Coe___mk "Documentation for Coe")` and `[CoeTail](Coercions/Coercing-Between-Types/#CoeTail___mk "Documentation for CoeTail")` instances are chained from the expected type towards the inferred type, so information in the expected type is used to resolve a chain of instances. If these chains meet in the middle, a coercion has been found. This is reflected in their type signatures: `[CoeHead](Coercions/Coercing-Between-Types/#CoeHead___mk "Documentation for CoeHead")` and `[CoeOut](Coercions/Coercing-Between-Types/#CoeOut___mk "Documentation for CoeOut")` use [semi-output parameters](Type-Classes/Instance-Synthesis/#--tech-term-Semi-output-parameters) for the coercion's target, while `[Coe](Coercions/#Coe___mk "Documentation for Coe")` and `[CoeTail](Coercions/Coercing-Between-Types/#CoeTail___mk "Documentation for CoeTail")` use [semi-output parameters](Type-Classes/Instance-Synthesis/#--tech-term-Semi-output-parameters) for the coercions' source.
When an instance provides a value for a [semi-output parameter](Type-Classes/Instance-Synthesis/#--tech-term-Semi-output-parameters), the value is used during instance synthesis. However, if no value is provided, then a value may be assigned by the synthesis algorithm. Consequently, every semi-output parameter should be assigned a type when an instance is selected. This means that `[CoeOut](Coercions/Coercing-Between-Types/#CoeOut___mk "Documentation for CoeOut")` should be used when the variables that occur in the coercion's output are a subset of those in its input, and `[Coe](Coercions/#Coe___mk "Documentation for Coe")` should be used when the variables in the input are a subset of those in the output.
`CoeOut` vs `Coe` instances
A `[Truthy](Coercions/Coercing-Between-Types/#Truthy-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example")` value is a value paired with an indication of whether it should be considered to be true or false. A `[Decision](Coercions/Coercing-Between-Types/#Decision-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example")` is either `[yes](Coercions/Coercing-Between-Types/#Decision___yes-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example")`, `[no](Coercions/Coercing-Between-Types/#Decision___no-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example")`, or `[maybe](Coercions/Coercing-Between-Types/#Decision___maybe-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example")`, with the latter containing further data for consideration.
`structure Truthy (α : Type) where   val : α   isTrue : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")  inductive Decision (α : Type) where   | yes   | maybe (val : α)   | no `
“Truthy” values can be converted to `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`s by forgetting the contained value. `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`s can be converted to `[Decision](Coercions/Coercing-Between-Types/#Decision-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example")`s by discounting the `[maybe](Coercions/Coercing-Between-Types/#Decision___maybe-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example")` case.
`@[[coe](Coercions/Coercing-Between-Types/#Lean___Attr___coe "Documentation for syntax")] def Truthy.toBool : [Truthy](Coercions/Coercing-Between-Types/#Truthy-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example") α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") :=   [Truthy.isTrue](Coercions/Coercing-Between-Types/#Truthy___isTrue-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example")  @[[coe](Coercions/Coercing-Between-Types/#Lean___Attr___coe "Documentation for syntax")] def Decision.ofBool : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") → [Decision](Coercions/Coercing-Between-Types/#Decision-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example") α   | [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") => .yes   | [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") => .no `
`[Truthy.toBool](Coercions/Coercing-Between-Types/#Truthy___toBool-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example")` must be a `[CoeOut](Coercions/Coercing-Between-Types/#CoeOut___mk "Documentation for CoeOut")` instance, because the target of the coercion contains fewer unknown type variables than the source, while `[Decision.ofBool](Coercions/Coercing-Between-Types/#Decision___ofBool-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example")` must be a `[Coe](Coercions/#Coe___mk "Documentation for Coe")` instance, because the source of the coercion contains fewer variables than the target:
`instance : [CoeOut](Coercions/Coercing-Between-Types/#CoeOut___mk "Documentation for CoeOut") ([Truthy](Coercions/Coercing-Between-Types/#Truthy-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example") α) [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := ⟨[Truthy.isTrue](Coercions/Coercing-Between-Types/#Truthy___isTrue-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example")⟩  instance : [Coe](Coercions/#Coe___mk "Documentation for Coe") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") ([Decision](Coercions/Coercing-Between-Types/#Decision-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example") α) := ⟨[Decision.ofBool](Coercions/Coercing-Between-Types/#Decision___ofBool-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example")⟩ `
With these instances, coercion chaining works:
``Decision.yes`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ({ [val](Coercions/Coercing-Between-Types/#Truthy___val-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example") := 1, [isTrue](Coercions/Coercing-Between-Types/#Truthy___isTrue-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example") := [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") : [Truthy](Coercions/Coercing-Between-Types/#Truthy-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") } : [Decision](Coercions/Coercing-Between-Types/#Decision-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) `
```
Decision.yes
```

Attempting to use the wrong class leads to an error:
``instance does not provide concrete values for (semi-)out-params   [Coe](Coercions/#Coe___mk "Documentation for Coe") ([Truthy](Coercions/Coercing-Between-Types/#Truthy-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example") ?α) [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`instance : [Coe](Coercions/#Coe___mk "Documentation for Coe") ([Truthy](Coercions/Coercing-Between-Types/#Truthy-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example") α) [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := ⟨[Truthy.isTrue](Coercions/Coercing-Between-Types/#Truthy___isTrue-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example")⟩ `
```
instance does not provide concrete values for (semi-)out-params
  [Coe](Coercions/#Coe___mk "Documentation for Coe") ([Truthy](Coercions/Coercing-Between-Types/#Truthy-_LPAR_in-CoeOut--vs--Coe--instances_RPAR_ "Definition of example") ?α) [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgCqRACwJ6IBSEbgRALhUwAd4BKRAd3XgQChFEA3AQwBsjE8nEBLYKghJiAIQD2Ejgwb8AdgBNoIfiyQAReFEH8J83AWLIylGnUbMAPokzxgfGwFs2mAEZIc7LsTwVHiPISsgACANpQEvAAugyK8ABmKGhYAHQgEpLS3MIY2ASASYSIWT4AvHy5aYLC8KERUbHxSVo6wHryqRIJJdw9RS26+jwB4CKIpQB8iKl2DtaICZzASJPTQbIKoGzyUKKIAMJRAPIQILiV+VQ9hKWIgBfkF6nVkPCAl+Qb8ls7e4dIPTgDNpDPxEW53QHtTrdKQcd4MADE8G8uAA3qxOKDEABGAA0AiEL0xoz2F0QADk2GcAL7cCFDADK4AUAHMKEA"\))
[🔗](find/?domain=Verso.Genre.Manual.doc&name=CoeHead.mk "Permalink")type class
```


CoeHead.{u, v} (α : Sort u) (β : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Sort v)) :
  Sort (max (max 1 u) v)


CoeHead.{u, v} (α : Sort u)
  (β : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Sort v)) :
  Sort (max (max 1 u) v)


```

`[CoeHead](Coercions/Coercing-Between-Types/#CoeHead___mk "Documentation for CoeHead") α β` is for coercions that are applied from left-to-right at most once at beginning of the coercion chain.
#  Instance Constructor

```
[CoeHead.mk](Coercions/Coercing-Between-Types/#CoeHead___mk "Documentation for CoeHead.mk").{u, v}
```

#  Methods

```
coe : α → β
```

Coerces a value of type `α` to type `β`. Accessible by the notation `↑x`, or by double type ascription `((x : α) : β)`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=CoeOut "Permalink")type class
```


CoeOut.{u, v} (α : Sort u) (β : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Sort v)) :
  Sort (max (max 1 u) v)


CoeOut.{u, v} (α : Sort u)
  (β : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Sort v)) :
  Sort (max (max 1 u) v)


```

`[CoeOut](Coercions/Coercing-Between-Types/#CoeOut___mk "Documentation for CoeOut") α β` is for coercions that are applied from left-to-right.
#  Instance Constructor

```
[CoeOut.mk](Coercions/Coercing-Between-Types/#CoeOut___mk "Documentation for CoeOut.mk").{u, v}
```

#  Methods

```
coe : α → β
```

Coerces a value of type `α` to type `β`. Accessible by the notation `↑x`, or by double type ascription `((x : α) : β)`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=CoeTail "Permalink")type class
```


CoeTail.{u, v} (α : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Sort u)) (β : Sort v) :
  Sort (max (max 1 u) v)


CoeTail.{u, v} (α : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Sort u))
  (β : Sort v) : Sort (max (max 1 u) v)


```

`[CoeTail](Coercions/Coercing-Between-Types/#CoeTail___mk "Documentation for CoeTail") α β` is for coercions that can only appear at the end of a sequence of coercions. That is, `α` can be further coerced via `[Coe](Coercions/#Coe___mk "Documentation for Coe") σ α` and `[CoeHead](Coercions/Coercing-Between-Types/#CoeHead___mk "Documentation for CoeHead") τ σ` instances but `β` will only be the expected type of the expression.
#  Instance Constructor

```
[CoeTail.mk](Coercions/Coercing-Between-Types/#CoeTail___mk "Documentation for CoeTail.mk").{u, v}
```

#  Methods

```
coe : α → β
```

Coerces a value of type `α` to type `β`. Accessible by the notation `↑x`, or by double type ascription `((x : α) : β)`.
Instances of `[CoeT](Coercions/Coercing-Between-Types/#CoeT___mk "Documentation for CoeT")` can be synthesized when an appropriate chain of instances exists, or when there is a single applicable `[CoeDep](Coercions/Coercing-Between-Types/#CoeDep___mk "Documentation for CoeDep")` instance.When coercing from `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` to another type, a `[NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast")` instances also suffices. If both exist, then the `[CoeDep](Coercions/Coercing-Between-Types/#CoeDep___mk "Documentation for CoeDep")` instance takes priority.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=CoeT "Permalink")type class
```


CoeT.{u, v} (α : Sort u) : α → (β : Sort v) → Sort (max 1 v)


CoeT.{u, v} (α : Sort u) :
  α → (β : Sort v) → Sort (max 1 v)


```

`[CoeT](Coercions/Coercing-Between-Types/#CoeT___mk "Documentation for CoeT")` is the core typeclass which is invoked by Lean to resolve a type error. It can also be triggered explicitly with the notation `↑x` or by double type ascription `((x : α) : β)`.
A `[CoeT](Coercions/Coercing-Between-Types/#CoeT___mk "Documentation for CoeT")` chain has the grammar `CoeHead? CoeOut* Coe* CoeTail? | CoeDep`.
#  Instance Constructor

```
[CoeT.mk](Coercions/Coercing-Between-Types/#CoeT___mk "Documentation for CoeT.mk").{u, v}
```

#  Methods

```
coe : β
```

The resulting value of type `β`. The input `x : α` is a parameter to the type class, so the value of type `β` may possibly depend on additional typeclasses on `x`.
Dependent coercions may not be chained. As an alternative to a chain of coercions, a term `e` of type `α` can be coerced to `β` using an instance of `[CoeDep](Coercions/Coercing-Between-Types/#CoeDep___mk "Documentation for CoeDep") α e β`. Dependent coercions are useful in situations where only some of the values can be coerced; this mechanism is used to coerce only decidable propositions to `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`. They are also useful when the value itself occurs in the coercion's target type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=CoeDep "Permalink")type class
```


CoeDep.{u, v} (α : Sort u) : α → (β : Sort v) → Sort (max 1 v)


CoeDep.{u, v} (α : Sort u) :
  α → (β : Sort v) → Sort (max 1 v)


```

`[CoeDep](Coercions/Coercing-Between-Types/#CoeDep___mk "Documentation for CoeDep") α (x : α) β` is a typeclass for dependent coercions, that is, the type `β` can depend on `x` (or rather, the value of `x` is available to typeclass search so an instance that relates `β` to `x` is allowed).
Dependent coercions do not participate in the transitive chaining process of regular coercions: they must exactly match the type mismatch on both sides.
#  Instance Constructor

```
[CoeDep.mk](Coercions/Coercing-Between-Types/#CoeDep___mk "Documentation for CoeDep.mk").{u, v}
```

#  Methods

```
coe : β
```

The resulting value of type `β`. The input `x : α` is a parameter to the type class, so the value of type `β` may possibly depend on additional typeclasses on `x`.
Dependent Coercion
A type of non-empty lists can be defined as a pair of a list and a proof that it is not empty. This type can be coerced to ordinary lists by applying the projection:
`structure NonEmptyList (α : Type u) : Type u where   contents : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α   non_empty : contents ≠ []  instance : [Coe](Coercions/#Coe___mk "Documentation for Coe") ([NonEmptyList](Coercions/Coercing-Between-Types/#NonEmptyList-_LPAR_in-Dependent-Coercion_RPAR_ "Definition of example") α) ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) where   [coe](Coercions/#Coe___mk "Documentation for Coe.coe") xs := xs.[contents](Coercions/Coercing-Between-Types/#NonEmptyList___contents-_LPAR_in-Dependent-Coercion_RPAR_ "Definition of example") `
The coercion works as expected:
`def oneTwoThree : [NonEmptyList](Coercions/Coercing-Between-Types/#NonEmptyList-_LPAR_in-Dependent-Coercion_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := ⟨[1, 2, 3], by⊢ [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") ≠ [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil") [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")All goals completed! 🐙⟩  `[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 4[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ([oneTwoThree](Coercions/Coercing-Between-Types/#oneTwoThree-_LPAR_in-Dependent-Coercion_RPAR_ "Definition of example") : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) ++ [4] `
Arbitrary lists cannot, however, be coerced to non-empty lists, because some arbitrarily-chosen lists may indeed be empty:
`instance : [Coe](Coercions/#Coe___mk "Documentation for Coe") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) ([NonEmptyList](Coercions/Coercing-Between-Types/#NonEmptyList-_LPAR_in-Dependent-Coercion_RPAR_ "Definition of example") α) where   [coe](Coercions/#Coe___mk "Documentation for Coe.coe") xs := ⟨xs, `don't know how to synthesize placeholder for argument `non_empty` context: α:Type u_1xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α⊢ xs ≠ [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")`_⟩ `
```
don't know how to synthesize placeholder for argument `non_empty`
context:
α:Type u_1xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α⊢ xs ≠ [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")
```

A dependent coercion can restrict the domain of the coercion to only lists that are not empty:
`instance : [CoeDep](Coercions/Coercing-Between-Types/#CoeDep___mk "Documentation for CoeDep") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (x :: xs) ([NonEmptyList](Coercions/Coercing-Between-Types/#NonEmptyList-_LPAR_in-Dependent-Coercion_RPAR_ "Definition of example") α) where   [coe](Coercions/Coercing-Between-Types/#CoeDep___mk "Documentation for CoeDep.coe") := ⟨x :: xs, byα:Type ?u.31x:αxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α⊢ x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") xs ≠ [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil") [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")All goals completed! 🐙⟩  `{ contents := [1, 2, 3], non_empty := _ }`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ([1, 2, 3] : [NonEmptyList](Coercions/Coercing-Between-Types/#NonEmptyList-_LPAR_in-Dependent-Coercion_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) `
```
{ contents := [1, 2, 3], non_empty := _ }
```

Dependent coercion insertion requires that the term to be coerced syntactically matches the term in the instance header. Lists that are known to be non-empty, but which are not syntactically instances of `(· :: ·)`, cannot be coerced with this instance.
``fun xs =>   let ys := xs [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")4[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons");   sorry : (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → ?m.14 xs`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") fun (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) => let ys : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := xs ++ [4] `Type mismatch   ys has type   [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") but is expected to have type   [NonEmptyList](Coercions/Coercing-Between-Types/#NonEmptyList-_LPAR_in-Dependent-Coercion_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`(ys : [NonEmptyList](Coercions/Coercing-Between-Types/#NonEmptyList-_LPAR_in-Dependent-Coercion_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) `
When coercion insertion fails, the original type error is reported:

```
Type mismatch
  ys
has type
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
but is expected to have type
  [NonEmptyList](Coercions/Coercing-Between-Types/#NonEmptyList-_LPAR_in-Dependent-Coercion_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

[Live ↪](javascript:openLiveLink\("K4OwlgbgpgTgzlABMAUCuAXGwDGHgxIByA9iAKIC2ADhgJ4AyYmiAFII3AiAXIgCp3UkwAJTc+AoYgDuAC1hQUiRDjIYoIDHDFMW7RYhBkA+lBr0xKjes2JABkSIA2gF00YEJgCGIHEh4BhEiRWUgozRmYMRHZRVh1I6Ok5Qn0VJAAPLS4AXkQMgDpLNQ04NAATKAAzRDIoXikSXhlCX0QQqlpwliIPSOzEQAvyBwBGABpEACYxgGYnMYAjOkQ4MBpAS/I0AGIoCA8AGzYauoamqBa41p7RAGorxwAWFxQ3T28WgKgAEShqNnOE1jS3B4GRibTCf1EsnkKUC3By/UBXGBcHmi2Wa022z2bGGY0miBmYjBHXO3QwwiAA"\))
syntaxCoercions

```
term ::= ...
    | 


↑x represents a coercion, which converts x of type α to type β, using
typeclasses to resolve a suitable conversion function. You can often leave the
↑ off entirely, since coercion is triggered implicitly whenever there is a
type error, but in ambiguous cases it can be useful to use ↑ to disambiguate
between e.g. ↑x + ↑y and ↑(x + y).


↑term
```

Coercions can be explicitly placed using the prefix operator ``coeNotation : term`
`↑x` represents a coercion, which converts `x` of type `α` to type `β`, using typeclasses to resolve a suitable conversion function. You can often leave the `↑` off entirely, since coercion is triggered implicitly whenever there is a type error, but in ambiguous cases it can be useful to use `↑` to disambiguate between e.g. `↑x + ↑y` and `↑(x + y)`.
`[`↑`](Coercions/Coercing-Between-Types/#coeNotation).
Unlike using nested [type ascriptions](Terms/Type-Ascription/#--tech-term-Type-ascriptions), the ``coeNotation : term`
`↑x` represents a coercion, which converts `x` of type `α` to type `β`, using typeclasses to resolve a suitable conversion function. You can often leave the `↑` off entirely, since coercion is triggered implicitly whenever there is a type error, but in ambiguous cases it can be useful to use `↑` to disambiguate between e.g. `↑x + ↑y` and `↑(x + y)`.
`[`↑`](Coercions/Coercing-Between-Types/#coeNotation) syntax for placing coercions does not require the involved types to be written explicitly.
Controlling Coercion Insertion
Instance synthesis and coercion insertion interact with one another. Synthesizing an instance may make type information known that later triggers coercion insertion. The specific placement of coercions may matter.
In this definition of `[sub](Coercions/Coercing-Between-Types/#sub-_LPAR_in-Controlling-Coercion-Insertion_RPAR_ "Definition of example")`, the `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` instance is synthesized based on the function's return type. This instance requires that the two parameters also be `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`s, but they are `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`s. Coercions are inserted around each argument to the subtraction operator. This can be seen in the output of ``Lean.Parser.Command.print : command```#print`.
`def sub (n k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") := n - k  `def sub : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") := fun n k => ↑n [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") ↑k`#print [sub](Coercions/Coercing-Between-Types/#sub-_LPAR_in-Controlling-Coercion-Insertion_RPAR_ "Definition of example") `
```
def sub : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") :=
fun n k => ↑n [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") ↑k
```

Placing the coercion operator outside the subtraction causes the elaborator to attempt to infer a type for the subtraction and then insert a coercion. Because the arguments are both `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`s, the `[Sub](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` instance is selected, leading to the difference being a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`. The difference is then coerced to an `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`.
`def sub' (n k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") := ↑ (n - k)  `def sub' : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") := fun n k => ↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")n [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") k[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")`#print [sub'](Coercions/Coercing-Between-Types/#sub___-_LPAR_in-Controlling-Coercion-Insertion_RPAR_ "Definition of example") `
These two functions are not equivalent because subtraction of natural numbers truncates at zero:
``-4`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [sub](Coercions/Coercing-Between-Types/#sub-_LPAR_in-Controlling-Coercion-Insertion_RPAR_ "Definition of example") 4 8 `
```
-4
```
``0`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [sub'](Coercions/Coercing-Between-Types/#sub___-_LPAR_in-Controlling-Coercion-Insertion_RPAR_ "Definition of example") 4 8 `
```
0
```

[Live ↪](javascript:openLiveLink\("CYUwZgBAzgrgRhAFAOwgawgLggOQIYAuAlFhAJLIFYC8EqAtOgFBMDEADgE4CWl08LUJFhwA5ElQZs+YqQpVMtQImEEiIzREWHHnxGitIAG54ANvwQAWCAA4Dxs3ohXrQA"\))
##  11.2.1. Implementing Coercions[🔗](find/?domain=Verso.Genre.Manual.section&name=coercion-impl "Permalink")
The appropriate `[CoeHead](Coercions/Coercing-Between-Types/#CoeHead___mk "Documentation for CoeHead")`, `[CoeOut](Coercions/Coercing-Between-Types/#CoeOut___mk "Documentation for CoeOut")`, `[Coe](Coercions/#Coe___mk "Documentation for Coe")`, or `[CoeTail](Coercions/Coercing-Between-Types/#CoeTail___mk "Documentation for CoeTail")` instance is sufficient to cause a desired coercion to be inserted. However, the implementation of the coercion should be registered as a coercion using the `coe` attribute. This causes Lean to display uses of the coercion with the ``coeNotation : term`
`↑x` represents a coercion, which converts `x` of type `α` to type `β`, using typeclasses to resolve a suitable conversion function. You can often leave the `↑` off entirely, since coercion is triggered implicitly whenever there is a type error, but in ambiguous cases it can be useful to use `↑` to disambiguate between e.g. `↑x + ↑y` and `↑(x + y)`.
`[`↑`](Coercions/Coercing-Between-Types/#coeNotation) operator. It also causes the `[norm_cast](Tactic-Proofs/Tactic-Reference/#norm_cast "Documentation for tactic")` tactic to treat the coercion as a cast, rather than as an ordinary function.
attributeCoercion Declarations

```
attr ::= ...
    | 


The @[coe] attribute on a function (which should also appear in a
instance : Coe A B := ⟨myFn⟩ declaration) allows the delaborator to show
applications of this function as ↑ when printing expressions.


coe
```

The `@[coe]` attribute on a function (which should also appear in a `instance : Coe A B := ⟨myFn⟩` declaration) allows the delaborator to show applications of this function as `↑` when printing expressions.
Implementing Coercions
The [enum inductive](The-Type-System/Inductive-Types/#--tech-term-enum-inductive) type `[Weekday](Coercions/Coercing-Between-Types/#Weekday-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example")` represents the days of the week:
`inductive Weekday where   | mo | tu | we | th | fr | sa | su `
As a seven-element type, it contains the same information as `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 7`. There is a bijection:
`def Weekday.toFin : [Weekday](Coercions/Coercing-Between-Types/#Weekday-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") → [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 7   | [mo](Coercions/Coercing-Between-Types/#Weekday___mo-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") => 0   | [tu](Coercions/Coercing-Between-Types/#Weekday___tu-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") => 1   | [we](Coercions/Coercing-Between-Types/#Weekday___we-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") => 2   | [th](Coercions/Coercing-Between-Types/#Weekday___th-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") => 3   | [fr](Coercions/Coercing-Between-Types/#Weekday___fr-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") => 4   | [sa](Coercions/Coercing-Between-Types/#Weekday___sa-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") => 5   | [su](Coercions/Coercing-Between-Types/#Weekday___su-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") => 6  def Weekday.fromFin : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 7 → [Weekday](Coercions/Coercing-Between-Types/#Weekday-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example")   | 0 => [mo](Coercions/Coercing-Between-Types/#Weekday___mo-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example")   | 1 => [tu](Coercions/Coercing-Between-Types/#Weekday___tu-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example")   | 2 => [we](Coercions/Coercing-Between-Types/#Weekday___we-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example")   | 3 => [th](Coercions/Coercing-Between-Types/#Weekday___th-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example")   | 4 => [fr](Coercions/Coercing-Between-Types/#Weekday___fr-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example")   | 5 => [sa](Coercions/Coercing-Between-Types/#Weekday___sa-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example")   | 6 => [su](Coercions/Coercing-Between-Types/#Weekday___su-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") `
Each type can be coerced to the other:
`instance : [Coe](Coercions/#Coe___mk "Documentation for Coe") [Weekday](Coercions/Coercing-Between-Types/#Weekday-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 7) where   [coe](Coercions/#Coe___mk "Documentation for Coe.coe") := [Weekday.toFin](Coercions/Coercing-Between-Types/#Weekday___toFin-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example")  instance : [Coe](Coercions/#Coe___mk "Documentation for Coe") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 7) [Weekday](Coercions/Coercing-Between-Types/#Weekday-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") where   [coe](Coercions/#Coe___mk "Documentation for Coe.coe") := [Weekday.fromFin](Coercions/Coercing-Between-Types/#Weekday___fromFin-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") `
While this works, instances of the coercions that occur in Lean's output are not presented using the coercion operator, which is what Lean users expect. Instead, the name `[Weekday.fromFin](Coercions/Coercing-Between-Types/#Weekday___fromFin-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example")` is used explicitly:
`def wednesday : [Weekday](Coercions/Coercing-Between-Types/#Weekday-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") := (2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 7)  `def wednesday : [Weekday](Coercions/Coercing-Between-Types/#Weekday-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") := [Weekday.fromFin](Coercions/Coercing-Between-Types/#Weekday___fromFin-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") 2`#print [wednesday](Coercions/Coercing-Between-Types/#wednesday-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") `
```
def wednesday : [Weekday](Coercions/Coercing-Between-Types/#Weekday-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") :=
[Weekday.fromFin](Coercions/Coercing-Between-Types/#Weekday___fromFin-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") 2
```

Adding the `coe` attribute to the definition of a coercion causes it to be displayed using the coercion operator:
`[attribute](Attributes/#Lean___Parser___Command___attribute "Documentation for syntax") [[coe](Coercions/Coercing-Between-Types/#Lean___Attr___coe "Documentation for syntax")] [Weekday.fromFin](Coercions/Coercing-Between-Types/#Weekday___fromFin-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") [attribute](Attributes/#Lean___Parser___Command___attribute "Documentation for syntax") [[coe](Coercions/Coercing-Between-Types/#Lean___Attr___coe "Documentation for syntax")] [Weekday.toFin](Coercions/Coercing-Between-Types/#Weekday___toFin-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example")  def friday : [Weekday](Coercions/Coercing-Between-Types/#Weekday-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") := (5 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 7)  `def friday : [Weekday](Coercions/Coercing-Between-Types/#Weekday-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") := ↑5`#print [friday](Coercions/Coercing-Between-Types/#friday-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") `
```
def friday : [Weekday](Coercions/Coercing-Between-Types/#Weekday-_LPAR_in-Implementing-Coercions_RPAR_ "Definition of example") :=
↑5
```

[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABAdUYg1mAhgT2QHcALRAJ0QChlkAfZAWwHs7kYJXCV6ZjWAzMqwDOOEREqUwifmgzZ8AOhhMAYqGQAuOVlwFASYTJ1IZAHZqrZsgC8APmQAGCzw53kARmdEUbgExfeG3sAZi9BIOQAFi9RCIBWGNd7ADZJaVl0XSVBJgZjLSMNU2RDTIU8LwcI5i93CPYvXwiuL2D64i9IiMEvOIjRL2T+iUpeRCYKBh1y5TVQAH0cvIXgMAKyvVn8gAoN7LJc/JAAShtkE01rZAAjCpoKAAdEHBhkbagcYURhZEBOAh35sgANQeY6ALgJkBBhKAAOaFECKD5fYQAbmQSJQAC9yCw3GR+AAbY4WHAPB4EgjGRSIAnABgONGfYQQBgPOBMECSMYTRBTPZ4RRLYzzFTC1breSbIUaXaSpSijSEU5XQhaK63CwYn6qgA8KPs+IJklAwhgOBAUBQ2gAwkwUPy3vlTKcSOQqDQoHa1dNNgrOZQTWaLVbkLaUNsnacHa6KJqvZcfftDqA0jJvGAQN89BKsgQE9smtpI5IAMQPMigV5cDNZ/CSF4wCvXCAwFAAbU9iAAuomBdLOQ2my3252e/ytimpGnBKt8Dnyt7tn0i0ViZQyxWQK8Z3ogA"\))
##  11.2.2. Coercions from Natural Numbers and Integers[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-api-cast "Permalink")
The type classes `[NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast")` and `[IntCast](Coercions/Coercing-Between-Types/#IntCast___mk "Documentation for IntCast")` are special cases of `[Coe](Coercions/#Coe___mk "Documentation for Coe")` that are used to define a coercion from `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` or `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` to some other type that is in some sense canonical. They exist to enable better integration with large libraries of mathematics, such as [Mathlib](https://github.com/leanprover-community/mathlib4), that make heavy use of coercions to map from the natural numbers or integers to other structures (typically rings). Ideally, the coercion of a natural number or integer into these structures is a [simp normal form](The-Simplifier/Simp-Normal-Forms/#--tech-term-simp-normal-form), because it is a convenient way to denote them.
When the coercion application is expected to be the [simp normal form](The-Simplifier/Simp-Normal-Forms/#--tech-term-simp-normal-form) for a type, it is important that _all_ such coercions are [definitionally equal](The-Type-System/#--tech-term-definitional-equality) in practice. Otherwise, the [simp normal form](The-Simplifier/Simp-Normal-Forms/#--tech-term-simp-normal-form) would need to choose a single chained coercion path, but lemmas could accidentally be stated using a different path. Because `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`'s internal index is based on the underlying structure of the term, rather than its presentation in the surface syntax, these differences would cause the lemmas to not be applied where expected. `[NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast")` and `[IntCast](Coercions/Coercing-Between-Types/#IntCast___mk "Documentation for IntCast")` instances, on the other hand, should be defined such that they are always [definitionally equal](The-Type-System/#--tech-term-definitional-equality), avoiding the problem. The Lean standard library's instances are arranged such that `[NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast")` or `[IntCast](Coercions/Coercing-Between-Types/#IntCast___mk "Documentation for IntCast")` instances are chosen preferentially over chains of coercion instances during coercion insertion. They can also be used as `[CoeOut](Coercions/Coercing-Between-Types/#CoeOut___mk "Documentation for CoeOut")` instances, allowing a graceful fallback to coercion chaining when needed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=NatCast "Permalink")type class
```


NatCast.{u} (R : Type u) : Type u


NatCast.{u} (R : Type u) : Type u


```

The canonical homomorphism `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → R`. In most use cases, the target type will have a (semi)ring structure, and this homomorphism should be a (semi)ring homomorphism.
`[NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast")` and `[IntCast](Coercions/Coercing-Between-Types/#IntCast___mk "Documentation for IntCast")` exist to allow different libraries with their own types that can be notated as natural numbers to have consistent `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` normal forms without needing to create coercion simplification sets that are aware of all combinations. Libraries should make it easy to work with `[NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast")` where possible. For instance, in Mathlib there will be such a homomorphism (and thus a `[NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast") R` instance) whenever `R` is an additive monoid with a `1`.
The prototypical example is `[Int.ofNat](Basic-Types/Integers/#Int___ofNat "Documentation for Int.ofNat")`.
#  Instance Constructor

```
[NatCast.mk](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast.mk").{u}
```

#  Methods

```
natCast : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → R
```

The canonical map `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → R`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nat.cast "Permalink")def
```


Nat.cast.{u} {R : Type u} [[NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast") R] : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → R


Nat.cast.{u} {R : Type u} [[NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast") R] :
  [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → R


```

The canonical homomorphism `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → R`. In most use cases, the target type will have a (semi)ring structure, and this homomorphism should be a (semi)ring homomorphism.
`[NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast")` and `[IntCast](Coercions/Coercing-Between-Types/#IntCast___mk "Documentation for IntCast")` exist to allow different libraries with their own types that can be notated as natural numbers to have consistent `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` normal forms without needing to create coercion simplification sets that are aware of all combinations. Libraries should make it easy to work with `[NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast")` where possible. For instance, in Mathlib there will be such a homomorphism (and thus a `[NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast") R` instance) whenever `R` is an additive monoid with a `1`.
The prototypical example is `[Int.ofNat](Basic-Types/Integers/#Int___ofNat "Documentation for Int.ofNat")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IntCast.intCast "Permalink")type class
```


IntCast.{u} (R : Type u) : Type u


IntCast.{u} (R : Type u) : Type u


```

The canonical homomorphism `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → R`. In most use cases, the target type will have a ring structure, and this homomorphism should be a ring homomorphism.
`[IntCast](Coercions/Coercing-Between-Types/#IntCast___mk "Documentation for IntCast")` and `[NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast")` exist to allow different libraries with their own types that can be notated as natural numbers to have consistent `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` normal forms without needing to create coercion simplification sets that are aware of all combinations. Libraries should make it easy to work with `[IntCast](Coercions/Coercing-Between-Types/#IntCast___mk "Documentation for IntCast")` where possible. For instance, in Mathlib there will be such a homomorphism (and thus an `[IntCast](Coercions/Coercing-Between-Types/#IntCast___mk "Documentation for IntCast") R` instance) whenever `R` is an additive group with a `1`.
#  Instance Constructor

```
[IntCast.mk](Coercions/Coercing-Between-Types/#IntCast___mk "Documentation for IntCast.mk").{u}
```

#  Methods

```
intCast : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → R
```

The canonical map `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → R`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Int.cast "Permalink")def
```


Int.cast.{u} {R : Type u} [[IntCast](Coercions/Coercing-Between-Types/#IntCast___mk "Documentation for IntCast") R] : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → R


Int.cast.{u} {R : Type u} [[IntCast](Coercions/Coercing-Between-Types/#IntCast___mk "Documentation for IntCast") R] :
  [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → R


```

The canonical homomorphism `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → R`. In most use cases, the target type will have a ring structure, and this homomorphism should be a ring homomorphism.
`[IntCast](Coercions/Coercing-Between-Types/#IntCast___mk "Documentation for IntCast")` and `[NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast")` exist to allow different libraries with their own types that can be notated as natural numbers to have consistent `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` normal forms without needing to create coercion simplification sets that are aware of all combinations. Libraries should make it easy to work with `[IntCast](Coercions/Coercing-Between-Types/#IntCast___mk "Documentation for IntCast")` where possible. For instance, in Mathlib there will be such a homomorphism (and thus an `[IntCast](Coercions/Coercing-Between-Types/#IntCast___mk "Documentation for IntCast") R` instance) whenever `R` is an additive group with a `1`.
[←11.1. Coercion Insertion](Coercions/Coercion-Insertion/#coercion-insertion "11.1. Coercion Insertion")[11.3. Coercing to Sorts→](Coercions/Coercing-to-Sorts/#sort-coercion "11.3. Coercing to Sorts")

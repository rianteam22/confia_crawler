[←11.4. Coercing to Function Types](Coercions/Coercing-to-Function-Types/#fun-coercion "11.4. Coercing to Function Types")[12. Run-Time Code→](Run-Time-Code/#runtime "12. Run-Time Code")
#  11.5. Implementation Details[🔗](find/?domain=Verso.Genre.Manual.section&name=coercion-impl-details "Permalink")
Only ordinary coercion insertion uses chaining. Inserting coercions to a [sort](Coercions/Coercing-to-Sorts/#sort-coercion) or a [function](Coercions/Coercing-to-Function-Types/#fun-coercion) uses ordinary instance synthesis. Similarly, [dependent coercions](Coercions/Coercing-Between-Types/#--tech-term-Dependent-coercions) are not chained.
##  11.5.1. Unfolding Coercions[🔗](find/?domain=Verso.Genre.Manual.section&name=coercion-unfold-impl "Permalink")
The coercion insertion mechanism unfolds applications of coercions, which allows them to control the specific shape of the resulting term. This is important both to ensure readable proof goals and to control evaluation of the coerced term in compiled code. Unfolding coercions is controlled by the `coe_decl` attribute, which is applied to each coercion method (e.g. `[Coe.coe](Coercions/#Coe___mk "Documentation for Coe.coe")`). This attribute should be considered part of the internals of the coercion mechanism, rather than part of the public coercion API.
##  11.5.2. Coercion Chaining[🔗](find/?domain=Verso.Genre.Manual.section&name=coercion-chain-impl "Permalink")
Coercion chaining is implemented through a collection of auxiliary type classes. Users should not write instances of these classes directly, but knowledge of their structure can be useful when diagnosing the reason why a coercion was not inserted as expected. The specific rules governing the ordering of instances in the chain (namely, that it should match `[CoeHead](Coercions/Coercing-Between-Types/#CoeHead___mk "Documentation for CoeHead")`﻿`?``[CoeOut](Coercions/Coercing-Between-Types/#CoeOut___mk "Documentation for CoeOut")`﻿`*``[Coe](Coercions/#Coe___mk "Documentation for Coe")`﻿`*``[CoeTail](Coercions/Coercing-Between-Types/#CoeTail___mk "Documentation for CoeTail")`﻿`?`) are implemented by the following type classes:
  * `[CoeTC](Coercions/Implementation-Details/#CoeTC___mk "Documentation for CoeTC")` is the transitive closure of `[Coe](Coercions/#Coe___mk "Documentation for Coe")` instances.
  * `[CoeOTC](Coercions/Implementation-Details/#CoeOTC___mk "Documentation for CoeOTC")` is the middle of the chain, consisting of the transitive closure of `[CoeOut](Coercions/Coercing-Between-Types/#CoeOut___mk "Documentation for CoeOut")` instances followed by `[CoeTC](Coercions/Implementation-Details/#CoeTC___mk "Documentation for CoeTC")`.
  * `[CoeHTC](Coercions/Implementation-Details/#CoeHTC___mk "Documentation for CoeHTC")` is the start of the chain, consisting of at most one `[CoeHead](Coercions/Coercing-Between-Types/#CoeHead___mk "Documentation for CoeHead")` instance followed by `[CoeOTC](Coercions/Implementation-Details/#CoeOTC___mk "Documentation for CoeOTC")`.
  * `[CoeHTCT](Coercions/Implementation-Details/#CoeHTCT___mk "Documentation for CoeHTCT")` is the whole chain, consisting of `CoeHTC` followed by at most one `[CoeTail](Coercions/Coercing-Between-Types/#CoeTail___mk "Documentation for CoeTail")` instance. Alternatively, it might be a `[NatCast](Coercions/Coercing-Between-Types/#NatCast___mk "Documentation for NatCast")` instance.
  * `[CoeT](Coercions/Coercing-Between-Types/#CoeT___mk "Documentation for CoeT")` represents the entire chain: it is either a `[CoeHTCT](Coercions/Implementation-Details/#CoeHTCT___mk "Documentation for CoeHTCT")` chain or a single `[CoeDep](Coercions/Coercing-Between-Types/#CoeDep___mk "Documentation for CoeDep")` instance.


Auxiliary Classes for Coercions
[🔗](find/?domain=Verso.Genre.Manual.doc&name=CoeHTCT.mk "Permalink")type class
```


CoeHTCT.{u, v} (α : Sort u) (β : Sort v) : Sort (max (max 1 u) v)


CoeHTCT.{u, v} (α : Sort u) (β : Sort v) :
  Sort (max (max 1 u) v)


```

Auxiliary class implementing `[CoeHead](Coercions/Coercing-Between-Types/#CoeHead___mk "Documentation for CoeHead")* [Coe](Coercions/#Coe___mk "Documentation for Coe")* CoeTail?`. Users should generally not implement this directly.
#  Instance Constructor

```
[CoeHTCT.mk](Coercions/Implementation-Details/#CoeHTCT___mk "Documentation for CoeHTCT.mk").{u, v}
```

#  Methods

```
coe : α → β
```

Coerces a value of type `α` to type `β`. Accessible by the notation `↑x`, or by double type ascription `((x : α) : β)`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=CoeHTC.coe "Permalink")type class
```


CoeHTC.{u, v} (α : Sort u) (β : Sort v) : Sort (max (max 1 u) v)


CoeHTC.{u, v} (α : Sort u) (β : Sort v) :
  Sort (max (max 1 u) v)


```

Auxiliary class implementing `CoeHead CoeOut* Coe*`. Users should generally not implement this directly.
#  Instance Constructor

```
[CoeHTC.mk](Coercions/Implementation-Details/#CoeHTC___mk "Documentation for CoeHTC.mk").{u, v}
```

#  Methods

```
coe : α → β
```

Coerces a value of type `α` to type `β`. Accessible by the notation `↑x`, or by double type ascription `((x : α) : β)`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=CoeOTC.coe "Permalink")type class
```


CoeOTC.{u, v} (α : Sort u) (β : Sort v) : Sort (max (max 1 u) v)


CoeOTC.{u, v} (α : Sort u) (β : Sort v) :
  Sort (max (max 1 u) v)


```

Auxiliary class implementing `CoeOut* Coe*`. Users should generally not implement this directly.
#  Instance Constructor

```
[CoeOTC.mk](Coercions/Implementation-Details/#CoeOTC___mk "Documentation for CoeOTC.mk").{u, v}
```

#  Methods

```
coe : α → β
```

Coerces a value of type `α` to type `β`. Accessible by the notation `↑x`, or by double type ascription `((x : α) : β)`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=CoeTC.coe "Permalink")type class
```


CoeTC.{u, v} (α : Sort u) (β : Sort v) : Sort (max (max 1 u) v)


CoeTC.{u, v} (α : Sort u) (β : Sort v) :
  Sort (max (max 1 u) v)


```

Auxiliary class implementing `Coe*`. Users should generally not implement this directly.
#  Instance Constructor

```
[CoeTC.mk](Coercions/Implementation-Details/#CoeTC___mk "Documentation for CoeTC.mk").{u, v}
```

#  Methods

```
coe : α → β
```

Coerces a value of type `α` to type `β`. Accessible by the notation `↑x`, or by double type ascription `((x : α) : β)`.
[←11.4. Coercing to Function Types](Coercions/Coercing-to-Function-Types/#fun-coercion "11.4. Coercing to Function Types")[12. Run-Time Code→](Run-Time-Code/#runtime "12. Run-Time Code")

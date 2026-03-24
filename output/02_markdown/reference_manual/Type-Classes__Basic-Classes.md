[←10.4. Deriving Instances](Type-Classes/Deriving-Instances/#deriving-instances "10.4. Deriving Instances")[11. Coercions→](Coercions/#coercions "11. Coercions")
#  10.5. Basic Classes[🔗](find/?domain=Verso.Genre.Manual.section&name=basic-classes "Permalink")
Many Lean type classes exist in order to allow built-in notations such as addition or array indexing to be overloaded.
##  10.5.1. Boolean Equality Tests[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Type-Classes--Basic-Classes--Boolean-Equality-Tests "Permalink")
The Boolean equality operator `==` is overloaded by defining instances of `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")`. The companion class `[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable")` specifies a hashing procedure for a type. When a type has both `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` and `[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable")` instances, then the hashes computed should respect the `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` instance: two values equated by `[BEq.beq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")` should always have the same hash.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BEq.beq "Permalink")type class
```


BEq.{u} (α : Type u) : Type u


BEq.{u} (α : Type u) : Type u


```

`[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α` is a typeclass for supplying a boolean-valued equality relation on `α`, notated as `a == b`. Unlike `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") α` (which uses `a = b`), this is `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` valued instead of `Prop` valued, and it also does not have any axioms like being reflexive or agreeing with `=`. It is mainly intended for programming applications. See `[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq")` for a version that requires that `==` and `=` coincide.
Typically we prefer to put the "more variable" term on the left, and the "more constant" term on the right.
#  Instance Constructor

```
[BEq.mk](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.mk").{u}
```

#  Methods

```
beq : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

Boolean equality, notated as `a == b`.
Conventions for notations in identifiers:
  * The recommended spelling of `==` in identifiers is `beq`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Hashable "Permalink")type class
```


Hashable.{u} (α : Sort u) : Sort (max 1 u)


Hashable.{u} (α : Sort u) : Sort (max 1 u)


```

Types that can be hashed into a `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`.
#  Instance Constructor

```
[Hashable.mk](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable.mk").{u}
```

#  Methods

```
hash : α → [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")
```

Hashes a value into a `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=mixHash "Permalink")opaque
```


mixHash (u₁ u₂ : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


mixHash (u₁ u₂ : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

An opaque hash mixing operation, used to implement hashing for products.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=LawfulBEq.toReflBEq "Permalink")type class
```


LawfulBEq.{u} (α : Type u) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] : Prop


LawfulBEq.{u} (α : Type u) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] : Prop


```

A Boolean equality test coincides with propositional equality.
In other words:
  * `a == b` implies `a = b`.
  * `a == a` is true.


#  Instance Constructor

```
[LawfulBEq.mk](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq.mk").{u}
```

#  Extends
  * `[ReflBEq](Type-Classes/Basic-Classes/#ReflBEq___mk "Documentation for ReflBEq") α`


#  Methods

```
rfl : ∀ {a : α}, [(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")a [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") a[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")
```

Inherited from 
  1. `[ReflBEq](Type-Classes/Basic-Classes/#ReflBEq___mk "Documentation for ReflBEq") α`



```
eq_of_beq : ∀ {a b : α}, [(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")a [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") b[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b
```

If `a == b` evaluates to `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, then `a` and `b` are equal in the logic.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ReflBEq "Permalink")type class
```


ReflBEq.{u_1} (α : Type u_1) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] : Prop


ReflBEq.{u_1} (α : Type u_1) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] :
  Prop


```

`[ReflBEq](Type-Classes/Basic-Classes/#ReflBEq___mk "Documentation for ReflBEq") α` says that the `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` implementation is reflexive.
#  Instance Constructor

```
[ReflBEq.mk](Type-Classes/Basic-Classes/#ReflBEq___mk "Documentation for ReflBEq.mk").{u_1}
```

#  Methods

```
rfl : ∀ {a : α}, [(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")a [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") a[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")
```

`==` is reflexive, that is, `(a == a) = true`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EquivBEq.mk "Permalink")type class
```


EquivBEq.{u_1} (α : Type u_1) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] : Prop


EquivBEq.{u_1} (α : Type u_1) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] :
  Prop


```

`[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq")` says that the `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` implementation is an equivalence relation.
#  Instance Constructor

```
[EquivBEq.mk](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq.mk").{u_1}
```

#  Extends
  * `PartialEquivBEq α`
  * `[ReflBEq](Type-Classes/Basic-Classes/#ReflBEq___mk "Documentation for ReflBEq") α`


#  Methods

```
symm : ∀ {a b : α}, [(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")a [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") b[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → [(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")b [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") a[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")
```

Inherited from 
  1. `PartialEquivBEq α`
  2. `[ReflBEq](Type-Classes/Basic-Classes/#ReflBEq___mk "Documentation for ReflBEq") α`



```
trans : ∀ {a b c : α}, [(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")a [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") b[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → [(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")b [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") c[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → [(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")a [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") c[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")
```

Inherited from 
  1. `PartialEquivBEq α`
  2. `[ReflBEq](Type-Classes/Basic-Classes/#ReflBEq___mk "Documentation for ReflBEq") α`



```
rfl : ∀ {a : α}, [(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")a [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") a[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")
```

Inherited from 
  1. `PartialEquivBEq α`
  2. `[ReflBEq](Type-Classes/Basic-Classes/#ReflBEq___mk "Documentation for ReflBEq") α`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=LawfulHashable.mk "Permalink")type class
```


LawfulHashable.{u} (α : Type u) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] : Prop


LawfulHashable.{u} (α : Type u) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] : Prop


```

The `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α` and `[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α` instances on `α` are compatible. This means that `a == b` implies `hash a = hash b`.
This is automatic if the `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` instance is lawful.
#  Instance Constructor

```
[LawfulHashable.mk](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable.mk").{u}
```

#  Methods

```
hash_eq : ∀ (a b : α), [(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")a [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") b[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → [hash](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable.hash") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [hash](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable.hash") b
```

If `a == b`, then `hash a = hash b`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=hash_eq "Permalink")theorem
```


hash_eq.{u_1} {α : Type u_1} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  {a b : α} : [(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")a [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") b[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → [hash](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable.hash") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [hash](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable.hash") b


hash_eq.{u_1} {α : Type u_1} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  {a b : α} :
  [(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")a [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") b[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → [hash](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable.hash") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [hash](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable.hash") b


```

A lawful hash function respects its Boolean equality test.
##  10.5.2. Ordering[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Type-Classes--Basic-Classes--Ordering "Permalink")
There are two primary ways to order the values of a type:
  * The `[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord")` type class provides a three-way comparison operator, `[compare](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord.compare")`, which can indicate that one value is less than, equal to, or greater than another. It returns an `[Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")`.
  * The `[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT")` and `[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE")` classes provide canonical `Prop`-valued ordering relations for a type that do not need to be decidable. These relations are used to overload the `<` and `≤` operators.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Ord.mk "Permalink")type class
```


Ord.{u} (α : Type u) : Type u


Ord.{u} (α : Type u) : Type u


```

`[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α` provides a computable total order on `α`, in terms of the `compare : α → α → Ordering` function.
Typically instances will be transitive, reflexive, and antisymmetric, but this is not enforced by the typeclass.
There is a derive handler, so appending `deriving Ord` to an inductive type or structure will attempt to create an `[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord")` instance.
#  Instance Constructor

```
[Ord.mk](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord.mk").{u}
```

#  Methods

```
compare : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")
```

Compare two elements in `α` using the comparator contained in an `[[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α]` instance.
The `[compare](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord.compare")` method is exported, so no explicit `Ord` namespace is required to use it.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=compareOn "Permalink")def
```


compareOn.{u_1, u_2} {β : Type u_1} {α : Sort u_2} [ord : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") β]
  (f : α → β) (x y : α) : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")


compareOn.{u_1, u_2} {β : Type u_1}
  {α : Sort u_2} [ord : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") β] (f : α → β)
  (x y : α) : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")


```

Compares two values by comparing the results of applying a function.
In particular, `x` is compared to `y` by comparing `f x` and `f y`.
Examples:
  * `[compareOn](Type-Classes/Basic-Classes/#compareOn "Documentation for compareOn") (·.[length](Basic-Types/Strings/#String___length "Documentation for String.length")) "apple" "banana" = [.lt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.lt")`
  * `[compareOn](Type-Classes/Basic-Classes/#compareOn "Documentation for compareOn") (· % 3) 5 6 = [.gt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.gt")`
  * `[compareOn](Type-Classes/Basic-Classes/#compareOn "Documentation for compareOn") (·.[foldl](Basic-Types/Linked-Lists/#List___foldl "Documentation for List.foldl") [max](Type-Classes/Basic-Classes/#Max___mk "Documentation for Max.max") 0) [1, 2, 3] [3, 2, 1] = [.eq](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.eq")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Ord.opposite "Permalink")def
```


Ord.opposite.{u_1} {α : Type u_1} (ord : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α) : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α


Ord.opposite.{u_1} {α : Type u_1}
  (ord : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α) : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α


```

Inverts the order of an `[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord")` instance.
The result is an `[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α` instance that returns `[Ordering.lt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.lt")` when `ord` would return `[Ordering.gt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.gt")` and that returns `[Ordering.gt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.gt")` when `ord` would return `[Ordering.lt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.lt")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Ordering.eq "Permalink")inductive type
```


Ordering : Type


Ordering : Type


```

The result of a comparison according to a total order.
The relationship between the compared items may be:
  * `[Ordering.lt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.lt")`: less than
  * `[Ordering.eq](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.eq")`: equal
  * `[Ordering.gt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.gt")`: greater than


#  Constructors

```
lt : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")
```

Less than.

```
eq : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")
```

Equal.

```
gt : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")
```

Greater than.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Ordering.swap "Permalink")def
```


Ordering.swap : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")


Ordering.swap : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")


```

Swaps less-than and greater-than ordering results.
Examples:
  * `[Ordering.lt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.lt").[swap](Type-Classes/Basic-Classes/#Ordering___swap "Documentation for Ordering.swap") = [Ordering.gt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.gt")`
  * `[Ordering.eq](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.eq").[swap](Type-Classes/Basic-Classes/#Ordering___swap "Documentation for Ordering.swap") = [Ordering.eq](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.eq")`
  * `[Ordering.gt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.gt").[swap](Type-Classes/Basic-Classes/#Ordering___swap "Documentation for Ordering.swap") = [Ordering.lt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.lt")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Ordering.then "Permalink")def
```


Ordering.then (a b : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")) : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")


Ordering.then (a b : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")) : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")


```

If `a` and `b` are `[Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")`, then `a.[then](Type-Classes/Basic-Classes/#Ordering___then "Documentation for Ordering.then") b` returns `a` unless it is `.eq`, in which case it returns `b`. Additionally, it has “short-circuiting” behavior similar to boolean `&&`: if `a` is not `.eq` then the expression for `b` is not evaluated.
This is a useful primitive for constructing lexicographic comparator functions. The `deriving Ord` syntax on a structure uses the `[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord")` instance to compare each field in order, combining the results equivalently to `[Ordering.then](Type-Classes/Basic-Classes/#Ordering___then "Documentation for Ordering.then")`.
Use `[compareLex](Type-Classes/Basic-Classes/#compareLex "Documentation for compareLex")` to lexicographically combine two comparison functions.
Examples:
`structure Person where   name : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")   age : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")  -- Sort people first by name (in ascending order), and people with the same name by age (in -- descending order) instance : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") Person where   [compare](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord.compare") a b := ([compare](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord.compare") a.name b.name).[then](Type-Classes/Basic-Classes/#Ordering___then "Documentation for Ordering.then") ([compare](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord.compare") b.age a.age) `
```
#eval Ord.compare (⟨"Gert", 33⟩ : Person) ⟨"Dana", 50⟩

```
`[Ordering.gt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.gt")`
```
#eval Ord.compare (⟨"Gert", 33⟩ : Person) ⟨"Gert", 50⟩

```
`[Ordering.gt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.gt")`
```
#eval Ord.compare (⟨"Gert", 33⟩ : Person) ⟨"Gert", 20⟩

```
`[Ordering.lt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.lt")`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Ordering.isLT "Permalink")def
```


Ordering.isLT : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Ordering.isLT : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the ordering is `lt`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Ordering.isLE "Permalink")def
```


Ordering.isLE : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Ordering.isLE : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the ordering is `lt` or `eq`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Ordering.isEq "Permalink")def
```


Ordering.isEq : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Ordering.isEq : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the ordering is `eq`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Ordering.isNe "Permalink")def
```


Ordering.isNe : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Ordering.isNe : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the ordering is not `eq`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Ordering.isGE "Permalink")def
```


Ordering.isGE : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Ordering.isGE : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the ordering is `gt` or `eq`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Ordering.isGT "Permalink")def
```


Ordering.isGT : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Ordering.isGT : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the ordering is `gt`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=compareOfLessAndEq "Permalink")def
```


compareOfLessAndEq.{u_1} {α : Type u_1} (x y : α) [[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") α]
  [[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") y[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")] [[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") α] : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")


compareOfLessAndEq.{u_1} {α : Type u_1}
  (x y : α) [[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") α] [[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") y[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")]
  [[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") α] : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")


```

Uses decidable less-than and equality relations to find an `[Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")`.
In particular, if `x < y` then the result is `[Ordering.lt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.lt")`. If `x = y` then the result is `[Ordering.eq](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.eq")`. Otherwise, it is `[Ordering.gt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.gt")`.
`[compareOfLessAndBEq](Type-Classes/Basic-Classes/#compareOfLessAndBEq "Documentation for compareOfLessAndBEq")` uses `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` instead of `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=compareOfLessAndBEq "Permalink")def
```


compareOfLessAndBEq.{u_1} {α : Type u_1} (x y : α) [[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") α]
  [[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") y[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")] [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")


compareOfLessAndBEq.{u_1} {α : Type u_1}
  (x y : α) [[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") α] [[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")x [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") y[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")]
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")


```

Uses a decidable less-than relation and Boolean equality to find an `[Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")`.
In particular, if `x < y` then the result is `[Ordering.lt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.lt")`. If `x == y` then the result is `[Ordering.eq](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.eq")`. Otherwise, it is `[Ordering.gt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.gt")`.
`[compareOfLessAndEq](Type-Classes/Basic-Classes/#compareOfLessAndEq "Documentation for compareOfLessAndEq")` uses `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq")` instead of `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=compareLex "Permalink")def
```


compareLex.{u_1, u_2} {α : Sort u_1} {β : Sort u_2}
  (cmp₁ cmp₂ : α → β → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")) (a : α) (b : β) : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")


compareLex.{u_1, u_2} {α : Sort u_1}
  {β : Sort u_2}
  (cmp₁ cmp₂ : α → β → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")) (a : α)
  (b : β) : [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")


```

Compares `a` and `b` lexicographically by `cmp₁` and `cmp₂`.
`a` and `b` are first compared by `cmp₁`. If this returns `[Ordering.eq](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.eq")`, `a` and `b` are compared by `cmp₂` to break the tie.
To lexicographically combine two `[Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")`s, use `[Ordering.then](Type-Classes/Basic-Classes/#Ordering___then "Documentation for Ordering.then")`.
syntaxOrdering Operators
The less-than operator is overloaded in the `[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT")` class:

```
term ::= ...
    | 


The less-than relation: x < y 


Conventions for notations in identifiers:




  * The recommended spelling of < in identifiers is lt.




term < term
```

The less-than-or-equal-to operator is overloaded in the `[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE")` class:

```
term ::= ...
    | 


The less-equal relation: x ≤ y 


Conventions for notations in identifiers:




  * The recommended spelling of ≤ in identifiers is le.




term ≤ term
```

The greater-than and greater-than-or-equal-to operators are the reverse of the less-than and less-than-or-equal-to operators, and cannot be independently overloaded:

```
term ::= ...
    | 


a > b is an abbreviation for b < a. 


Conventions for notations in identifiers:




  * The recommended spelling of > in identifiers is gt.




term > term
```

```
term ::= ...
    | 


a ≥ b is an abbreviation for b ≤ a. 


Conventions for notations in identifiers:




  * The recommended spelling of ≥ in identifiers is ge.




term ≥ term
```

[🔗](find/?domain=Verso.Genre.Manual.doc&name=LT.mk "Permalink")type class
```


LT.{u} (α : Type u) : Type u


LT.{u} (α : Type u) : Type u


```

`[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") α` is the typeclass which supports the notation `x < y` where `x y : α`.
#  Instance Constructor

```
[LT.mk](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.mk").{u}
```

#  Methods

```
lt : α → α → Prop
```

The less-than relation: `x < y`
Conventions for notations in identifiers:
  * The recommended spelling of `<` in identifiers is `lt`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=LE.mk "Permalink")type class
```


LE.{u} (α : Type u) : Type u


LE.{u} (α : Type u) : Type u


```

`[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") α` is the typeclass which supports the notation `x ≤ y` where `x y : α`.
#  Instance Constructor

```
[LE.mk](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.mk").{u}
```

#  Methods

```
le : α → α → Prop
```

The less-equal relation: `x ≤ y`
Conventions for notations in identifiers:
  * The recommended spelling of `≤` in identifiers is `le`.
  * The recommended spelling of `<=` in identifiers is `le` (prefer `≤` over `<=`).


An `[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord")` can be used to construct `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")`, `[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT")`, and `[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE")` instances with the following helpers. They are not automatically instances because many types are better served by custom relations.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ltOfOrd "Permalink")def
```


ltOfOrd.{u_1} {α : Type u_1} [[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α] : [LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") α


ltOfOrd.{u_1} {α : Type u_1} [[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α] :
  [LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") α


```

Constructs an `[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT")` instance from an `[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord")` instance that asserts that the result of `[compare](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord.compare")` is `[Ordering.lt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.lt")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=leOfOrd "Permalink")def
```


leOfOrd.{u_1} {α : Type u_1} [[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α] : [LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") α


leOfOrd.{u_1} {α : Type u_1} [[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α] :
  [LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") α


```

Constructs an `[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE")` instance from an `[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord")` instance that asserts that the result of `[compare](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord.compare")` satisfies `[Ordering.isLE](Type-Classes/Basic-Classes/#Ordering___isLE "Documentation for Ordering.isLE")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Ord.toBEq "Permalink")def
```


Ord.toBEq.{u_1} {α : Type u_1} (ord : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α) : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α


Ord.toBEq.{u_1} {α : Type u_1}
  (ord : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α) : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α


```

Constructs a `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` instance from an `[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord")` instance.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Ord.toLE "Permalink")def
```


Ord.toLE.{u_1} {α : Type u_1} (ord : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α) : [LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") α


Ord.toLE.{u_1} {α : Type u_1}
  (ord : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α) : [LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") α


```

Constructs an `[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE")` instance from an `[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord")` instance.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Ord.toLT "Permalink")def
```


Ord.toLT.{u_1} {α : Type u_1} (ord : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α) : [LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") α


Ord.toLT.{u_1} {α : Type u_1}
  (ord : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α) : [LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") α


```

Constructs an `[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT")` instance from an `[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord")` instance.
Using `Ord` Instances for `LT` and `LE` Instances
Lean can automatically derive an `[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord")` instance. In this case, the `[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") [Vegetable](Type-Classes/Basic-Classes/#Vegetable-_LPAR_in-Using--Ord--Instances-for--LT--and--LE--Instances_RPAR_ "Definition of example")` instance compares vegetables lexicographically:
`structure Vegetable where   color : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")   size : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 5 deriving [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") ``def broccoli : [Vegetable](Type-Classes/Basic-Classes/#Vegetable-_LPAR_in-Using--Ord--Instances-for--LT--and--LE--Instances_RPAR_ "Definition of example") where   [color](Type-Classes/Basic-Classes/#Vegetable___color-_LPAR_in-Using--Ord--Instances-for--LT--and--LE--Instances_RPAR_ "Definition of example") := "green"   [size](Type-Classes/Basic-Classes/#Vegetable___size-_LPAR_in-Using--Ord--Instances-for--LT--and--LE--Instances_RPAR_ "Definition of example") := 2  def sweetPotato : [Vegetable](Type-Classes/Basic-Classes/#Vegetable-_LPAR_in-Using--Ord--Instances-for--LT--and--LE--Instances_RPAR_ "Definition of example") where   [color](Type-Classes/Basic-Classes/#Vegetable___color-_LPAR_in-Using--Ord--Instances-for--LT--and--LE--Instances_RPAR_ "Definition of example") := "orange"   [size](Type-Classes/Basic-Classes/#Vegetable___size-_LPAR_in-Using--Ord--Instances-for--LT--and--LE--Instances_RPAR_ "Definition of example") := 3 `
Using the helpers `[ltOfOrd](Type-Classes/Basic-Classes/#ltOfOrd "Documentation for ltOfOrd")` and `[leOfOrd](Type-Classes/Basic-Classes/#leOfOrd "Documentation for leOfOrd")`, `[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") [Vegetable](Type-Classes/Basic-Classes/#Vegetable-_LPAR_in-Using--Ord--Instances-for--LT--and--LE--Instances_RPAR_ "Definition of example")` and `[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") [Vegetable](Type-Classes/Basic-Classes/#Vegetable-_LPAR_in-Using--Ord--Instances-for--LT--and--LE--Instances_RPAR_ "Definition of example")` instances can be defined. These instances compare the vegetables using `[compare](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord.compare")` and logically assert that the result is as expected.
`instance : [LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") [Vegetable](Type-Classes/Basic-Classes/#Vegetable-_LPAR_in-Using--Ord--Instances-for--LT--and--LE--Instances_RPAR_ "Definition of example") := [ltOfOrd](Type-Classes/Basic-Classes/#ltOfOrd "Documentation for ltOfOrd") instance : [LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") [Vegetable](Type-Classes/Basic-Classes/#Vegetable-_LPAR_in-Using--Ord--Instances-for--LT--and--LE--Instances_RPAR_ "Definition of example") := [leOfOrd](Type-Classes/Basic-Classes/#leOfOrd "Documentation for leOfOrd") `
The resulting relations are decidable because equality is decidable for `[Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")`:
``[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [broccoli](Type-Classes/Basic-Classes/#broccoli-_LPAR_in-Using--Ord--Instances-for--LT--and--LE--Instances_RPAR_ "Definition of example") < [sweetPotato](Type-Classes/Basic-Classes/#sweetPotato-_LPAR_in-Using--Ord--Instances-for--LT--and--LE--Instances_RPAR_ "Definition of example") `
```
[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")
```
``[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [broccoli](Type-Classes/Basic-Classes/#broccoli-_LPAR_in-Using--Ord--Instances-for--LT--and--LE--Instances_RPAR_ "Definition of example") ≤ [sweetPotato](Type-Classes/Basic-Classes/#sweetPotato-_LPAR_in-Using--Ord--Instances-for--LT--and--LE--Instances_RPAR_ "Definition of example") `
```
[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")
```
``[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [broccoli](Type-Classes/Basic-Classes/#broccoli-_LPAR_in-Using--Ord--Instances-for--LT--and--LE--Instances_RPAR_ "Definition of example") < [broccoli](Type-Classes/Basic-Classes/#broccoli-_LPAR_in-Using--Ord--Instances-for--LT--and--LE--Instances_RPAR_ "Definition of example") `
```
[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")
```
``[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [broccoli](Type-Classes/Basic-Classes/#broccoli-_LPAR_in-Using--Ord--Instances-for--LT--and--LE--Instances_RPAR_ "Definition of example") ≤ [broccoli](Type-Classes/Basic-Classes/#broccoli-_LPAR_in-Using--Ord--Instances-for--LT--and--LE--Instances_RPAR_ "Definition of example") `
```
[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")
```

[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgGrwObxAQwEYBskB3AC3gQChFEoB7PGsRALkQGVwBLAOzUsWA4AvJCwBi3RAFZyAEzIcAbtzSIA8mBnlZ8AGaIcYGlFp4OzFOky4CiEmXh8TDZgF5EAIjQJ4Xd3wHCrogATFpyesCE8JgACjTYIDTmqBjY+ESkFFROjExu7gxYPPB+VAEibgDMWtygRVAiiAAyACoWqdYViHggqjrqmrXYXA3mTQCi7VbpQQR9A1oAxPAKWHj6hsZ0ZgA8/FGx8ViJSytrG0YmZoAmRPvRIHEJNKer6waX24h771umL+c/K6IW6A7ZAA"\))
###  10.5.2.1. Instance Construction[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Type-Classes--Basic-Classes--Ordering--Instance-Construction "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Ord.lex "Permalink")def
```


Ord.lex.{u_1, u_2} {α : Type u_1} {β : Type u_2} :
  [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α → [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") β → [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


Ord.lex.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} :
  [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α → [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") β → [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Constructs the lexicographic order on products `α × β` from orders for `α` and `β`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Ord.lex' "Permalink")def
```


Ord.lex'.{u_1} {α : Type u_1} (ord₁ ord₂ : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α) : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α


Ord.lex'.{u_1} {α : Type u_1}
  (ord₁ ord₂ : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α) : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α


```

Constructs an `[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord")` instance from two existing instances by combining them lexicographically.
The resulting instance compares elements first by `ord₁` and then, if this returns `[Ordering.eq](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.eq")`, by `ord₂`.
The function `[compareLex](Type-Classes/Basic-Classes/#compareLex "Documentation for compareLex")` can be used to perform this comparison without constructing an intermediate `[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord")` instance. `[Ordering.then](Type-Classes/Basic-Classes/#Ordering___then "Documentation for Ordering.then")` can be used to lexicographically combine the results of comparisons.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Ord.on "Permalink")def
```


Ord.on.{u_1, u_2} {β : Type u_1} {α : Type u_2} :
  [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") β → (f : α → β) → [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α


Ord.on.{u_1, u_2} {β : Type u_1}
  {α : Type u_2} :
  [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") β → (f : α → β) → [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α


```

Constructs an `[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord")` instance that compares values according to the results of `f`.
In particular, `ord.on f` compares `x` and `y` by comparing `f x` and `f y` according to `ord`.
The function `[compareOn](Type-Classes/Basic-Classes/#compareOn "Documentation for compareOn")` can be used to perform this comparison without constructing an intermediate `[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord")` instance.
##  10.5.3. Minimum and Maximum Values[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Type-Classes--Basic-Classes--Minimum-and-Maximum-Values "Permalink")
The classes `Max` and `Min` provide overloaded operators for choosing the greater or lesser of two values. These should be in agreement with `Ord`, `LT`, and `LE` instances, if they exist, but there is no mechanism to enforce this.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Min.mk "Permalink")type class
```


Min.{u} (α : Type u) : Type u


Min.{u} (α : Type u) : Type u


```

An overloaded operation to find the lesser of two values of type `α`.
#  Instance Constructor

```
[Min.mk](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min.mk").{u}
```

#  Methods

```
min : α → α → α
```

Returns the lesser of its two arguments.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Max "Permalink")type class
```


Max.{u} (α : Type u) : Type u


Max.{u} (α : Type u) : Type u


```

An overloaded operation to find the greater of two values of type `α`.
#  Instance Constructor

```
[Max.mk](Type-Classes/Basic-Classes/#Max___mk "Documentation for Max.mk").{u}
```

#  Methods

```
max : α → α → α
```

Returns the greater of its two arguments.
Given an `[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") α` instance for which `[LE.le](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")` is decidable, the helpers `[minOfLe](Type-Classes/Basic-Classes/#minOfLe "Documentation for minOfLe")` and `[maxOfLe](Type-Classes/Basic-Classes/#maxOfLe "Documentation for maxOfLe")` can be used to create suitable `[Min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min") α` and `[Max](Type-Classes/Basic-Classes/#Max___mk "Documentation for Max") α` instances. They can be used as the right-hand side of an ``Lean.Parser.Command.declaration : command```instance` declaration.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=minOfLe "Permalink")def
```


minOfLe.{u_1} {α : Type u_1} [[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") α] [[DecidableRel](Type-Classes/Basic-Classes/#DecidableRel "Documentation for DecidableRel") [LE.le](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")] : [Min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min") α


minOfLe.{u_1} {α : Type u_1} [[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") α]
  [[DecidableRel](Type-Classes/Basic-Classes/#DecidableRel "Documentation for DecidableRel") [LE.le](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")] : [Min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min") α


```

Constructs a `[Min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min")` instance from a decidable `≤` operation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=maxOfLe "Permalink")def
```


maxOfLe.{u_1} {α : Type u_1} [[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") α] [[DecidableRel](Type-Classes/Basic-Classes/#DecidableRel "Documentation for DecidableRel") [LE.le](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")] : [Max](Type-Classes/Basic-Classes/#Max___mk "Documentation for Max") α


maxOfLe.{u_1} {α : Type u_1} [[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") α]
  [[DecidableRel](Type-Classes/Basic-Classes/#DecidableRel "Documentation for DecidableRel") [LE.le](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")] : [Max](Type-Classes/Basic-Classes/#Max___mk "Documentation for Max") α


```

Constructs a `[Max](Type-Classes/Basic-Classes/#Max___mk "Documentation for Max")` instance from a decidable `≤` operation.
##  10.5.4. Decidability[🔗](find/?domain=Verso.Genre.Manual.section&name=decidable-propositions "Permalink")
A proposition is _decidable_ if it can be checked algorithmically. The Law of the Excluded Middle means that every proposition is true or false, but it provides no way to check which of the two cases holds, which can often be useful. By default, only algorithmic `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` instances for which code can be generated are in scope; opening the `Classical` namespace makes every proposition decidable.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Decidable.isTrue "Permalink")inductive type
```


Decidable (p : Prop) : Type


Decidable (p : Prop) : Type


```

Either a proof that `p` is true or a proof that `p` is false. This is equivalent to a `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` paired with a proof that the `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if and only if `p` is true.
`[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` instances are primarily used via `[if](Tactic-Proofs/The-Tactic-Language/#if "Documentation for tactic")`-expressions and the tactic `[decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")`. In conditional expressions, the `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` instance for the proposition is used to select a branch. At run time, this case distinction code is identical to that which would be generated for a `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`-based conditional. In proofs, the tactic `[decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")` synthesizes an instance of `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") p`, attempts to reduce it to `[isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") h`, and then succeeds with the proof `h` if it can.
Because `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` carries data, when writing `@[simp]` lemmas which include a `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` instance on the LHS, it is best to use `{_ : Decidable p}` rather than `[[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") p]` so that non-canonical instances can be found via unification rather than instance synthesis.
#  Constructors

```
isFalse {p : Prop} (h : [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")p) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") p
```

Proves that `p` is decidable by supplying a proof of `¬p`

```
isTrue {p : Prop} (h : p) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") p
```

Proves that `p` is decidable by supplying a proof of `p`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=DecidablePred "Permalink")def
```


DecidablePred.{u} {α : Sort u} (r : α → Prop) : Sort (max 1 u)


DecidablePred.{u} {α : Sort u}
  (r : α → Prop) : Sort (max 1 u)


```

A decidable predicate.
A predicate is decidable if the corresponding proposition is `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` for each possible argument.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=DecidableRel "Permalink")def
```


DecidableRel.{u, v} {α : Sort u} {β : Sort v} (r : α → β → Prop) :
  Sort (max (max 1 u) v)


DecidableRel.{u, v} {α : Sort u}
  {β : Sort v} (r : α → β → Prop) :
  Sort (max (max 1 u) v)


```

A decidable relation.
A relation is decidable if the corresponding proposition is `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` for all possible arguments.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=DecidableEq "Permalink")def
```


DecidableEq.{u} (α : Sort u) : Sort (max 1 u)


DecidableEq.{u} (α : Sort u) :
  Sort (max 1 u)


```

Propositional equality is `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` for all elements of a type.
In other words, an instance of `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") α` is a means of deciding the proposition `a = b` is for all `a b : α`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=DecidableLT "Permalink")def
```


DecidableLT.{u} (α : Type u) [[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") α] : Type u


DecidableLT.{u} (α : Type u) [[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") α] :
  Type u


```

Abbreviation for `[DecidableRel](Type-Classes/Basic-Classes/#DecidableRel "Documentation for DecidableRel") (· < · : α → α → Prop)`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=DecidableLE "Permalink")def
```


DecidableLE.{u} (α : Type u) [[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") α] : Type u


DecidableLE.{u} (α : Type u) [[LE](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE") α] :
  Type u


```

Abbreviation for `[DecidableRel](Type-Classes/Basic-Classes/#DecidableRel "Documentation for DecidableRel") (· ≤ · : α → α → Prop)`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Decidable.decide "Permalink")def
```


Decidable.decide (p : Prop) [h : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") p] : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Decidable.decide (p : Prop)
  [h : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") p] : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Converts a decidable proposition into a `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`.
If `p : Prop` is decidable, then `[decide](Type-Classes/Basic-Classes/#Decidable___decide "Documentation for Decidable.decide") p : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` is the Boolean value that is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if `p` is true and `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` if `p` is false.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Decidable.byCases "Permalink")def
```


Decidable.byCases.{u} {p : Prop} {q : Sort u} [dec : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") p]
  (h1 : p → q) (h2 : [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")p → q) : q


Decidable.byCases.{u} {p : Prop}
  {q : Sort u} [dec : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") p]
  (h1 : p → q) (h2 : [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")p → q) : q


```

Construct a `q` if some proposition `p` is decidable, and both the truth and falsity of `p` are sufficient to construct a `q`.
This is a synonym for `dite`, the dependent if-then-else operator.
Excluded Middle and `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")`
The equality of functions from `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` to `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` is not decidable:
`example (f g : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") (f = g) := `failed to synthesize instance of type class   [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")f [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`[inferInstance](Type-Classes/Instance-Synthesis/#inferInstance "Documentation for inferInstance") `
```
failed to synthesize instance of type class
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")f [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```

Opening `Classical` makes every proposition decidable; however, declarations and examples that use this fact must be marked ``Lean.Parser.Command.declaration : command```noncomputable` to indicate that code should not be generated for them.
`[open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Classical noncomputable example (f g : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") (f = g) :=   [inferInstance](Type-Classes/Instance-Synthesis/#inferInstance "Documentation for inferInstance") `
[Live ↪](javascript:openLiveLink\("PYBwpgdgBAwgNgQwM5IJYGMFwFAWBdYAWxAFcAXBAIzjCjAA8ETaoAKAMygHMoAuKADkE5KICTCISICU/KABEw6VABNqrTlAC8PGX03YoUVBA5gATgEkISSgTBA"\))
##  10.5.5. Inhabited Types[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Type-Classes--Basic-Classes--Inhabited-Types "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Inhabited "Permalink")type class
```


Inhabited.{u} (α : Sort u) : Sort (max 1 u)


Inhabited.{u} (α : Sort u) :
  Sort (max 1 u)


```

`[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α` is a typeclass that says that `α` has a designated element, called `([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : α)`. This is sometimes referred to as a "pointed type".
This class is used by functions that need to return a value of the type when called "out of domain". For example, `Array.get! arr i : α` returns a value of type `α` when `arr : Array α`, but if `i` is not in range of the array, it reports a panic message, but this does not halt the program, so it must still return a value of type `α` (and in fact this is required for logical consistency), so in this case it returns `[default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default")`.
#  Instance Constructor

```
[Inhabited.mk](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.mk").{u}
```

#  Methods

```
default : α
```

`[default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default")` is a function that produces a "default" element of any `[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited")` type. This element does not have any particular specified properties, but it is often an all-zeroes value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Nonempty "Permalink")inductive predicate
```


Nonempty.{u} (α : Sort u) : Prop


Nonempty.{u} (α : Sort u) : Prop


```

`[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") α` is a typeclass that says that `α` is not an empty type, that is, there exists an element in the type. It differs from `[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α` in that `[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") α` is a `Prop`, which means that it does not actually carry an element of `α`, only a proof that _there exists_ such an element. Given `[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") α`, you can construct an element of `α` _nonconstructively_ using `Classical.choice`.
#  Constructors

```
intro.{u} {α : Sort u} (val : α) : [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") α
```

If `val : α`, then `α` is nonempty.
##  10.5.6. Subsingleton Types[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Type-Classes--Basic-Classes--Subsingleton-Types "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subsingleton.intro "Permalink")type class
```


Subsingleton.{u} (α : Sort u) : Prop


Subsingleton.{u} (α : Sort u) : Prop


```

A _subsingleton_ is a type with at most one element. It is either empty or has a unique element.
All propositions are subsingletons because of proof irrelevance: false propositions are empty, and all proofs of a true proposition are equal to one another. Some non-propositional types are also subsingletons.
#  Instance Constructor

```
[Subsingleton.intro](Type-Classes/Basic-Classes/#Subsingleton___intro "Documentation for Subsingleton.intro").{u}
```

Prove that `α` is a subsingleton by showing that any two elements are equal.
#  Methods

```
allEq : ∀ (a b : α), a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b
```

Any two elements of a subsingleton are equal.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subsingleton.elim "Permalink")theorem
```


Subsingleton.elim.{u} {α : Sort u} [h : [Subsingleton](Type-Classes/Basic-Classes/#Subsingleton___intro "Documentation for Subsingleton") α] (a b : α) :
  a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b


Subsingleton.elim.{u} {α : Sort u}
  [h : [Subsingleton](Type-Classes/Basic-Classes/#Subsingleton___intro "Documentation for Subsingleton") α] (a b : α) : a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b


```

If a type is a subsingleton, then all of its elements are equal.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subsingleton.helim "Permalink")theorem
```


Subsingleton.helim.{u} {α β : Sort u} [h₁ : [Subsingleton](Type-Classes/Basic-Classes/#Subsingleton___intro "Documentation for Subsingleton") α] (h₂ : α [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") β)
  (a : α) (b : β) : a [≍](Basic-Propositions/Propositional-Equality/#HEq___refl "Documentation for HEq") b


Subsingleton.helim.{u} {α β : Sort u}
  [h₁ : [Subsingleton](Type-Classes/Basic-Classes/#Subsingleton___intro "Documentation for Subsingleton") α] (h₂ : α [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") β)
  (a : α) (b : β) : a [≍](Basic-Propositions/Propositional-Equality/#HEq___refl "Documentation for HEq") b


```

If two types are equal and one of them is a subsingleton, then all of their elements are [heterogeneously equal](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=HEq).
##  10.5.7. Arithmetic and Bitwise Operators[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Type-Classes--Basic-Classes--Arithmetic-and-Bitwise-Operators "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Zero.mk "Permalink")type class
```


Zero.{u} (α : Type u) : Type u


Zero.{u} (α : Type u) : Type u


```

A type with a zero element.
#  Instance Constructor

```
[Zero.mk](Type-Classes/Basic-Classes/#Zero___mk "Documentation for Zero.mk").{u}
```

#  Methods

```
zero : α
```

The zero element of the type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=NeZero "Permalink")type class
```


NeZero.{u_1} {R : Type u_1} [[Zero](Type-Classes/Basic-Classes/#Zero___mk "Documentation for Zero") R] (n : R) : Prop


NeZero.{u_1} {R : Type u_1} [[Zero](Type-Classes/Basic-Classes/#Zero___mk "Documentation for Zero") R]
  (n : R) : Prop


```

A type-class version of `n ≠ 0`.
#  Instance Constructor

```
[NeZero.mk](Type-Classes/Basic-Classes/#NeZero___mk "Documentation for NeZero.mk").{u_1}
```

#  Methods

```
out : n ≠ 0
```

The proposition that `n` is not zero.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=HAdd.mk "Permalink")type class
```


HAdd.{u, v, w} (α : Type u) (β : Type v) (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


HAdd.{u, v, w} (α : Type u) (β : Type v)
  (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


```

The notation typeclass for heterogeneous addition. This enables the notation `a + b : γ` where `a : α`, `b : β`.
#  Instance Constructor

```
[HAdd.mk](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.mk").{u, v, w}
```

#  Methods

```
hAdd : α → β → γ
```

`a + b` computes the sum of `a` and `b`. The meaning of this notation is type-dependent.
Conventions for notations in identifiers:
  * The recommended spelling of `+` in identifiers is `add`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Add.mk "Permalink")type class
```


Add.{u} (α : Type u) : Type u


Add.{u} (α : Type u) : Type u


```

The homogeneous version of `[HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd")`: `a + b : α` where `a b : α`.
#  Instance Constructor

```
[Add.mk](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add.mk").{u}
```

#  Methods

```
add : α → α → α
```

`a + b` computes the sum of `a` and `b`. See `[HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=HSub.hSub "Permalink")type class
```


HSub.{u, v, w} (α : Type u) (β : Type v) (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


HSub.{u, v, w} (α : Type u) (β : Type v)
  (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


```

The notation typeclass for heterogeneous subtraction. This enables the notation `a - b : γ` where `a : α`, `b : β`.
#  Instance Constructor

```
[HSub.mk](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.mk").{u, v, w}
```

#  Methods

```
hSub : α → β → γ
```

`a - b` computes the difference of `a` and `b`. The meaning of this notation is type-dependent.
  * For natural numbers, this operator saturates at 0: `a - b = 0` when `a ≤ b`.


Conventions for notations in identifiers:
  * The recommended spelling of `-` in identifiers is `sub` (when used as a binary operator).


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Sub.sub "Permalink")type class
```


Sub.{u} (α : Type u) : Type u


Sub.{u} (α : Type u) : Type u


```

The homogeneous version of `[HSub](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub")`: `a - b : α` where `a b : α`.
#  Instance Constructor

```
[Sub.mk](Type-Classes/Basic-Classes/#Sub___mk "Documentation for Sub.mk").{u}
```

#  Methods

```
sub : α → α → α
```

`a - b` computes the difference of `a` and `b`. See `[HSub](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=HMul.mk "Permalink")type class
```


HMul.{u, v, w} (α : Type u) (β : Type v) (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


HMul.{u, v, w} (α : Type u) (β : Type v)
  (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


```

The notation typeclass for heterogeneous multiplication. This enables the notation `a * b : γ` where `a : α`, `b : β`.
#  Instance Constructor

```
[HMul.mk](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul.mk").{u, v, w}
```

#  Methods

```
hMul : α → β → γ
```

`a * b` computes the product of `a` and `b`. The meaning of this notation is type-dependent.
Conventions for notations in identifiers:
  * The recommended spelling of `*` in identifiers is `mul`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=SMul.mk "Permalink")type class
```


SMul.{u, v} (M : Type u) (α : Type v) : Type (max u v)


SMul.{u, v} (M : Type u) (α : Type v) :
  Type (max u v)


```

Typeclass for types with a scalar multiplication operation, denoted `•` (`\bu`)
#  Instance Constructor

```
[SMul.mk](Type-Classes/Basic-Classes/#SMul___mk "Documentation for SMul.mk").{u, v}
```

#  Methods

```
smul : M → α → α
```

`m • a : α` denotes the product of `m : M` and `a : α`. The meaning of this notation is type-dependent, but it is intended to be used for left actions.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Mul "Permalink")type class
```


Mul.{u} (α : Type u) : Type u


Mul.{u} (α : Type u) : Type u


```

The homogeneous version of `[HMul](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul")`: `a * b : α` where `a b : α`.
#  Instance Constructor

```
[Mul.mk](Type-Classes/Basic-Classes/#Mul___mk "Documentation for Mul.mk").{u}
```

#  Methods

```
mul : α → α → α
```

`a * b` computes the product of `a` and `b`. See `[HMul](Type-Classes/Basic-Classes/#HMul___mk "Documentation for HMul")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=HDiv.hDiv "Permalink")type class
```


HDiv.{u, v, w} (α : Type u) (β : Type v) (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


HDiv.{u, v, w} (α : Type u) (β : Type v)
  (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


```

The notation typeclass for heterogeneous division. This enables the notation `a / b : γ` where `a : α`, `b : β`.
#  Instance Constructor

```
[HDiv.mk](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv.mk").{u, v, w}
```

#  Methods

```
hDiv : α → β → γ
```

`a / b` computes the result of dividing `a` by `b`. The meaning of this notation is type-dependent.
  * For most types like `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`, `Rat`, `Real`, `a / 0` is defined to be `0`.
  * For `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, `a / b` rounds downwards.
  * For `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`, `a / b` rounds downwards if `b` is positive or upwards if `b` is negative. It is implemented as `[Int.ediv](Basic-Types/Integers/#Int___ediv "Documentation for Int.ediv")`, the unique function satisfying `a % b + b * (a / b) = a` and `0 ≤ a % b < natAbs b` for `b ≠ 0`. Other rounding conventions are available using the functions `[Int.fdiv](Basic-Types/Integers/#Int___fdiv "Documentation for Int.fdiv")` (floor rounding) and `[Int.tdiv](Basic-Types/Integers/#Int___tdiv "Documentation for Int.tdiv")` (truncation rounding).
  * For `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")`, `a / 0` follows the IEEE 754 semantics for division, usually resulting in `inf` or `nan`.


Conventions for notations in identifiers:
  * The recommended spelling of `/` in identifiers is `div`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Div.mk "Permalink")type class
```


Div.{u} (α : Type u) : Type u


Div.{u} (α : Type u) : Type u


```

The homogeneous version of `[HDiv](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv")`: `a / b : α` where `a b : α`.
#  Instance Constructor

```
[Div.mk](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div.mk").{u}
```

#  Methods

```
div : α → α → α
```

`a / b` computes the result of dividing `a` by `b`. See `[HDiv](Type-Classes/Basic-Classes/#HDiv___mk "Documentation for HDiv")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Dvd.mk "Permalink")type class
```


Dvd.{u_1} (α : Type u_1) : Type u_1


Dvd.{u_1} (α : Type u_1) : Type u_1


```

Notation typeclass for the `∣` operation (typed as `\|`), which represents divisibility.
#  Instance Constructor

```
[Dvd.mk](Type-Classes/Basic-Classes/#Dvd___mk "Documentation for Dvd.mk").{u_1}
```

#  Methods

```
dvd : α → α → Prop
```

Divisibility. `a ∣ b` (typed as `\|`) means that there is some `c` such that `b = a * c`.
Conventions for notations in identifiers:
  * The recommended spelling of `∣` in identifiers is `dvd`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=HMod "Permalink")type class
```


HMod.{u, v, w} (α : Type u) (β : Type v) (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


HMod.{u, v, w} (α : Type u) (β : Type v)
  (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


```

The notation typeclass for heterogeneous modulo / remainder. This enables the notation `a % b : γ` where `a : α`, `b : β`.
#  Instance Constructor

```
[HMod.mk](Type-Classes/Basic-Classes/#HMod___mk "Documentation for HMod.mk").{u, v, w}
```

#  Methods

```
hMod : α → β → γ
```

`a % b` computes the remainder upon dividing `a` by `b`. The meaning of this notation is type-dependent.
  * For `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` and `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` it satisfies `a % b + b * (a / b) = a`, and `a % 0` is defined to be `a`.


Conventions for notations in identifiers:
  * The recommended spelling of `%` in identifiers is `mod`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Mod.mk "Permalink")type class
```


Mod.{u} (α : Type u) : Type u


Mod.{u} (α : Type u) : Type u


```

The homogeneous version of `[HMod](Type-Classes/Basic-Classes/#HMod___mk "Documentation for HMod")`: `a % b : α` where `a b : α`.
#  Instance Constructor

```
[Mod.mk](Type-Classes/Basic-Classes/#Mod___mk "Documentation for Mod.mk").{u}
```

#  Methods

```
mod : α → α → α
```

`a % b` computes the remainder upon dividing `a` by `b`. See `[HMod](Type-Classes/Basic-Classes/#HMod___mk "Documentation for HMod")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=HPow "Permalink")type class
```


HPow.{u, v, w} (α : Type u) (β : Type v) (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


HPow.{u, v, w} (α : Type u) (β : Type v)
  (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


```

The notation typeclass for heterogeneous exponentiation. This enables the notation `a ^ b : γ` where `a : α`, `b : β`.
#  Instance Constructor

```
[HPow.mk](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow.mk").{u, v, w}
```

#  Methods

```
hPow : α → β → γ
```

`a ^ b` computes `a` to the power of `b`. The meaning of this notation is type-dependent.
Conventions for notations in identifiers:
  * The recommended spelling of `^` in identifiers is `pow`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Pow.mk "Permalink")type class
```


Pow.{u, v} (α : Type u) (β : Type v) : Type (max u v)


Pow.{u, v} (α : Type u) (β : Type v) :
  Type (max u v)


```

The homogeneous version of `[HPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow")`: `a ^ b : α` where `a : α`, `b : β`. (The right argument is not the same as the left since we often want this even in the homogeneous case.)
Types can choose to subscribe to particular defaulting behavior by providing an instance to either `[NatPow](Type-Classes/Basic-Classes/#NatPow___mk "Documentation for NatPow")` or `[HomogeneousPow](Type-Classes/Basic-Classes/#HomogeneousPow___mk "Documentation for HomogeneousPow")`:
  * `[NatPow](Type-Classes/Basic-Classes/#NatPow___mk "Documentation for NatPow")` is for types whose exponents is preferentially a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`.
  * `[HomogeneousPow](Type-Classes/Basic-Classes/#HomogeneousPow___mk "Documentation for HomogeneousPow")` is for types whose base and exponent are preferentially the same.


#  Instance Constructor

```
[Pow.mk](Type-Classes/Basic-Classes/#Pow___mk "Documentation for Pow.mk").{u, v}
```

#  Methods

```
pow : α → β → α
```

`a ^ b` computes `a` to the power of `b`. See `[HPow](Type-Classes/Basic-Classes/#HPow___mk "Documentation for HPow")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=NatPow.mk "Permalink")type class
```


NatPow.{u} (α : Type u) : Type u


NatPow.{u} (α : Type u) : Type u


```

The homogeneous version of `[Pow](Type-Classes/Basic-Classes/#Pow___mk "Documentation for Pow")` where the exponent is a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`. The purpose of this class is that it provides a default `[Pow](Type-Classes/Basic-Classes/#Pow___mk "Documentation for Pow")` instance, which can be used to specialize the exponent to `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` during elaboration.
For example, if `x ^ 2` should preferentially elaborate with `2 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` then `x`'s type should provide an instance for this class.
#  Instance Constructor

```
[NatPow.mk](Type-Classes/Basic-Classes/#NatPow___mk "Documentation for NatPow.mk").{u}
```

#  Methods

```
pow : α → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → α
```

`a ^ n` computes `a` to the power of `n` where `n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`. See `[Pow](Type-Classes/Basic-Classes/#Pow___mk "Documentation for Pow")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=HomogeneousPow "Permalink")type class
```


HomogeneousPow.{u} (α : Type u) : Type u


HomogeneousPow.{u} (α : Type u) : Type u


```

The completely homogeneous version of `[Pow](Type-Classes/Basic-Classes/#Pow___mk "Documentation for Pow")` where the exponent has the same type as the base. The purpose of this class is that it provides a default `[Pow](Type-Classes/Basic-Classes/#Pow___mk "Documentation for Pow")` instance, which can be used to specialize the exponent to have the same type as the base's type during elaboration. This is to say, a type should provide an instance for this class in case `x ^ y` should be elaborated with both `x` and `y` having the same type.
For example, the `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` type provides an instance of this class, which causes expressions such as `(2.2 ^ 2.2 : [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float"))` to elaborate.
#  Instance Constructor

```
[HomogeneousPow.mk](Type-Classes/Basic-Classes/#HomogeneousPow___mk "Documentation for HomogeneousPow.mk").{u}
```

#  Methods

```
pow : α → α → α
```

`a ^ b` computes `a` to the power of `b` where `a` and `b` both have the same type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=HShiftLeft.mk "Permalink")type class
```


HShiftLeft.{u, v, w} (α : Type u) (β : Type v) (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


HShiftLeft.{u, v, w} (α : Type u)
  (β : Type v) (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


```

The typeclass behind the notation `a <<< b : γ` where `a : α`, `b : β`.
#  Instance Constructor

```
[HShiftLeft.mk](Type-Classes/Basic-Classes/#HShiftLeft___mk "Documentation for HShiftLeft.mk").{u, v, w}
```

#  Methods

```
hShiftLeft : α → β → γ
```

`a <<< b` computes `a` shifted to the left by `b` places. The meaning of this notation is type-dependent.
  * On `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, this is equivalent to `a * 2 ^ b`.
  * On `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")` and other fixed width unsigned types, this is the same but truncated to the bit width.


Conventions for notations in identifiers:
  * The recommended spelling of `<<<` in identifiers is `shiftLeft`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=ShiftLeft "Permalink")type class
```


ShiftLeft.{u} (α : Type u) : Type u


ShiftLeft.{u} (α : Type u) : Type u


```

The homogeneous version of `[HShiftLeft](Type-Classes/Basic-Classes/#HShiftLeft___mk "Documentation for HShiftLeft")`: `a <<< b : α` where `a b : α`.
#  Instance Constructor

```
[ShiftLeft.mk](Type-Classes/Basic-Classes/#ShiftLeft___mk "Documentation for ShiftLeft.mk").{u}
```

#  Methods

```
shiftLeft : α → α → α
```

The implementation of `a <<< b : α`. See `[HShiftLeft](Type-Classes/Basic-Classes/#HShiftLeft___mk "Documentation for HShiftLeft")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=HShiftRight.mk "Permalink")type class
```


HShiftRight.{u, v, w} (α : Type u) (β : Type v)
  (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) : Type (max (max u v) w)


HShiftRight.{u, v, w} (α : Type u)
  (β : Type v) (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


```

The typeclass behind the notation `a >>> b : γ` where `a : α`, `b : β`.
#  Instance Constructor

```
[HShiftRight.mk](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight.mk").{u, v, w}
```

#  Methods

```
hShiftRight : α → β → γ
```

`a >>> b` computes `a` shifted to the right by `b` places. The meaning of this notation is type-dependent.
  * On `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` and fixed width unsigned types like `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")`, this is equivalent to `a / 2 ^ b`.


Conventions for notations in identifiers:
  * The recommended spelling of `>>>` in identifiers is `shiftRight`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=ShiftRight.mk "Permalink")type class
```


ShiftRight.{u} (α : Type u) : Type u


ShiftRight.{u} (α : Type u) : Type u


```

The homogeneous version of `[HShiftRight](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight")`: `a >>> b : α` where `a b : α`.
#  Instance Constructor

```
[ShiftRight.mk](Type-Classes/Basic-Classes/#ShiftRight___mk "Documentation for ShiftRight.mk").{u}
```

#  Methods

```
shiftRight : α → α → α
```

The implementation of `a >>> b : α`. See `[HShiftRight](Type-Classes/Basic-Classes/#HShiftRight___mk "Documentation for HShiftRight")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Neg.neg "Permalink")type class
```


Neg.{u} (α : Type u) : Type u


Neg.{u} (α : Type u) : Type u


```

The notation typeclass for negation. This enables the notation `-a : α` where `a : α`.
#  Instance Constructor

```
[Neg.mk](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.mk").{u}
```

#  Methods

```
neg : α → α
```

`-a` computes the negative or opposite of `a`. The meaning of this notation is type-dependent.
Conventions for notations in identifiers:
  * The recommended spelling of `-` in identifiers is `neg` (when used as a unary operator).


[🔗](find/?domain=Verso.Genre.Manual.doc&name=HAnd.hAnd "Permalink")type class
```


HAnd.{u, v, w} (α : Type u) (β : Type v) (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


HAnd.{u, v, w} (α : Type u) (β : Type v)
  (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


```

The typeclass behind the notation `a &&& b : γ` where `a : α`, `b : β`.
#  Instance Constructor

```
[HAnd.mk](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd.mk").{u, v, w}
```

#  Methods

```
hAnd : α → β → γ
```

`a &&& b` computes the bitwise AND of `a` and `b`. The meaning of this notation is type-dependent.
Conventions for notations in identifiers:
  * The recommended spelling of `&&&` in identifiers is `[and](Basic-Types/Booleans/#Bool___and "Documentation for Bool.and")`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=AndOp.and "Permalink")type class
```


AndOp.{u} (α : Type u) : Type u


AndOp.{u} (α : Type u) : Type u


```

The homogeneous version of `[HAnd](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd")`: `a &&& b : α` where `a b : α`. (It is called `[AndOp](Type-Classes/Basic-Classes/#AndOp___mk "Documentation for AndOp")` because `[And](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And")` is taken for the propositional connective.)
#  Instance Constructor

```
[AndOp.mk](Type-Classes/Basic-Classes/#AndOp___mk "Documentation for AndOp.mk").{u}
```

#  Methods

```
and : α → α → α
```

The implementation of `a &&& b : α`. See `[HAnd](Type-Classes/Basic-Classes/#HAnd___mk "Documentation for HAnd")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=HOr.hOr "Permalink")type class
```


HOr.{u, v, w} (α : Type u) (β : Type v) (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


HOr.{u, v, w} (α : Type u) (β : Type v)
  (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


```

The typeclass behind the notation `a ||| b : γ` where `a : α`, `b : β`.
#  Instance Constructor

```
[HOr.mk](Type-Classes/Basic-Classes/#HOr___mk "Documentation for HOr.mk").{u, v, w}
```

#  Methods

```
hOr : α → β → γ
```

`a ||| b` computes the bitwise OR of `a` and `b`. The meaning of this notation is type-dependent.
Conventions for notations in identifiers:
  * The recommended spelling of `|||` in identifiers is `[or](Basic-Types/Booleans/#Bool___or "Documentation for Bool.or")`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=OrOp.mk "Permalink")type class
```


OrOp.{u} (α : Type u) : Type u


OrOp.{u} (α : Type u) : Type u


```

The homogeneous version of `[HOr](Type-Classes/Basic-Classes/#HOr___mk "Documentation for HOr")`: `a ||| b : α` where `a b : α`. (It is called `[OrOp](Type-Classes/Basic-Classes/#OrOp___mk "Documentation for OrOp")` because `[Or](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or")` is taken for the propositional connective.)
#  Instance Constructor

```
[OrOp.mk](Type-Classes/Basic-Classes/#OrOp___mk "Documentation for OrOp.mk").{u}
```

#  Methods

```
or : α → α → α
```

The implementation of `a ||| b : α`. See `[HOr](Type-Classes/Basic-Classes/#HOr___mk "Documentation for HOr")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=HXor.mk "Permalink")type class
```


HXor.{u, v, w} (α : Type u) (β : Type v) (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


HXor.{u, v, w} (α : Type u) (β : Type v)
  (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


```

The typeclass behind the notation `a ^^^ b : γ` where `a : α`, `b : β`.
#  Instance Constructor

```
[HXor.mk](Type-Classes/Basic-Classes/#HXor___mk "Documentation for HXor.mk").{u, v, w}
```

#  Methods

```
hXor : α → β → γ
```

`a ^^^ b` computes the bitwise XOR of `a` and `b`. The meaning of this notation is type-dependent.
Conventions for notations in identifiers:
  * The recommended spelling of `^^^` in identifiers is `[xor](Basic-Types/Booleans/#Bool___xor "Documentation for Bool.xor")`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=XorOp.mk "Permalink")type class
```


XorOp.{u} (α : Type u) : Type u


XorOp.{u} (α : Type u) : Type u


```

The homogeneous version of `[HXor](Type-Classes/Basic-Classes/#HXor___mk "Documentation for HXor")`: `a ^^^ b : α` where `a b : α`.
#  Instance Constructor

```
[XorOp.mk](Type-Classes/Basic-Classes/#XorOp___mk "Documentation for XorOp.mk").{u}
```

#  Methods

```
xor : α → α → α
```

The implementation of `a ^^^ b : α`. See `[HXor](Type-Classes/Basic-Classes/#HXor___mk "Documentation for HXor")`.
##  10.5.8. Append[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Type-Classes--Basic-Classes--Append "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=HAppend "Permalink")type class
```


HAppend.{u, v, w} (α : Type u) (β : Type v) (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


HAppend.{u, v, w} (α : Type u)
  (β : Type v) (γ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) :
  Type (max (max u v) w)


```

The notation typeclass for heterogeneous append. This enables the notation `a ++ b : γ` where `a : α`, `b : β`.
#  Instance Constructor

```
[HAppend.mk](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.mk").{u, v, w}
```

#  Methods

```
hAppend : α → β → γ
```

`a ++ b` is the result of concatenation of `a` and `b`, usually read "append". The meaning of this notation is type-dependent.
Conventions for notations in identifiers:
  * The recommended spelling of `++` in identifiers is `append`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Append.mk "Permalink")type class
```


Append.{u} (α : Type u) : Type u


Append.{u} (α : Type u) : Type u


```

The homogeneous version of `[HAppend](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend")`: `a ++ b : α` where `a b : α`.
#  Instance Constructor

```
[Append.mk](Type-Classes/Basic-Classes/#Append___mk "Documentation for Append.mk").{u}
```

#  Methods

```
append : α → α → α
```

`a ++ b` is the result of concatenation of `a` and `b`. See `[HAppend](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend")`.
##  10.5.9. Data Lookups[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Type-Classes--Basic-Classes--Data-Lookups "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=GetElem "Permalink")type class
```


GetElem.{u, v, w} (coll : Type u) (idx : Type v)
  (elem : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) (valid : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (coll → idx → Prop)) :
  Type (max (max u v) w)


GetElem.{u, v, w} (coll : Type u)
  (idx : Type v)
  (elem : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w))
  (valid : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (coll → idx → Prop)) :
  Type (max (max u v) w)


```

The classes `[GetElem](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem")` and `[GetElem?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?")` implement lookup notation, specifically `xs[i]`, `xs[i]?`, `xs[i]!`, and `xs[i]'p`.
Both classes are indexed by types `coll`, `idx`, and `elem` which are the collection, the index, and the element types. A single collection may support lookups with multiple index types. The relation `valid` determines when the index is guaranteed to be valid; lookups of valid indices are guaranteed not to fail.
For example, an instance for arrays looks like `[GetElem](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") α (fun xs i => i < xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size"))`. In other words, given an array `xs` and a natural number `i`, `xs[i]` will return an `α` when `valid xs i` holds, which is true when `i` is less than the size of the array. `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")` additionally supports indexing with `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")` instead of `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`. In either case, because the bounds are checked at compile time, no runtime check is required.
Given `xs[i]` with `xs : coll` and `i : idx`, Lean looks for an instance of `[GetElem](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem") coll idx elem valid` and uses this to infer the type of the return value `elem` and side condition `valid` required to ensure `xs[i]` yields a valid value of type `elem`. The tactic `[get_elem_tactic](Tactic-Proofs/Tactic-Reference/#get_elem_tactic "Documentation for tactic")` is invoked to prove validity automatically. The `xs[i]'p` notation uses the proof `p` to satisfy the validity condition. If the proof `p` is long, it is often easier to place the proof in the context using `have`, because `[get_elem_tactic](Tactic-Proofs/Tactic-Reference/#get_elem_tactic "Documentation for tactic")` tries `[assumption](Tactic-Proofs/Tactic-Reference/#assumption "Documentation for tactic")`.
The proof side-condition `valid xs i` is automatically dispatched by the `[get_elem_tactic](Tactic-Proofs/Tactic-Reference/#get_elem_tactic "Documentation for tactic")` tactic; this tactic can be extended by adding more clauses to `get_elem_tactic_extensible` using `macro_rules`.
`xs[i]?` and `xs[i]!` do not impose a proof obligation; the former returns an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") elem`, with `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` signalling that the value isn't present, and the latter returns `elem` but panics if the value isn't there, returning `default : elem` based on the `[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") elem` instance. These are provided by the `[GetElem?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?")` class, for which there is a default instance generated from a `[GetElem](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem")` class as long as `valid xs i` is always decidable.
Important instances include:
  * `arr[i] : α` where `arr : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α` and `i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` or `i : USize`: does array indexing with no runtime bounds check and a proof side goal `i < arr.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")`.
  * `l[i] : α` where `l : List α` and `i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`: index into a list, with proof side goal `i < l.length`.


#  Instance Constructor

```
[GetElem.mk](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem.mk").{u, v, w}
```

#  Methods

```
getElem : (xs : coll) → (i : idx) → valid xs i → elem
```

The syntax `arr[i]` gets the `i`'th element of the collection `arr`. If there are proof side conditions to the application, they will be automatically inferred by the `[get_elem_tactic](Tactic-Proofs/Tactic-Reference/#get_elem_tactic "Documentation for tactic")` tactic.
Conventions for notations in identifiers:
  * The recommended spelling of `xs[i]` in identifiers is `[getElem](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem.getElem")`.
  * The recommended spelling of `xs[i]'h` in identifiers is `[getElem](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem.getElem")`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=GetElem?.toGetElem "Permalink")type class
```


GetElem?.{u, v, w} (coll : Type u) (idx : Type v)
  (elem : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) (valid : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (coll → idx → Prop)) :
  Type (max (max u v) w)


GetElem?.{u, v, w} (coll : Type u)
  (idx : Type v)
  (elem : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w))
  (valid : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (coll → idx → Prop)) :
  Type (max (max u v) w)


```

The classes `[GetElem](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem")` and `[GetElem?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?")` implement lookup notation, specifically `xs[i]`, `xs[i]?`, `xs[i]!`, and `xs[i]'p`.
Both classes are indexed by types `coll`, `idx`, and `elem` which are the collection, the index, and the element types. A single collection may support lookups with multiple index types. The relation `valid` determines when the index is guaranteed to be valid; lookups of valid indices are guaranteed not to fail.
For example, an instance for arrays looks like `[GetElem](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") α (fun xs i => i < xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size"))`. In other words, given an array `xs` and a natural number `i`, `xs[i]` will return an `α` when `valid xs i` holds, which is true when `i` is less than the size of the array. `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")` additionally supports indexing with `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")` instead of `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`. In either case, because the bounds are checked at compile time, no runtime check is required.
Given `xs[i]` with `xs : coll` and `i : idx`, Lean looks for an instance of `[GetElem](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem") coll idx elem valid` and uses this to infer the type of the return value `elem` and side condition `valid` required to ensure `xs[i]` yields a valid value of type `elem`. The tactic `[get_elem_tactic](Tactic-Proofs/Tactic-Reference/#get_elem_tactic "Documentation for tactic")` is invoked to prove validity automatically. The `xs[i]'p` notation uses the proof `p` to satisfy the validity condition. If the proof `p` is long, it is often easier to place the proof in the context using `have`, because `[get_elem_tactic](Tactic-Proofs/Tactic-Reference/#get_elem_tactic "Documentation for tactic")` tries `[assumption](Tactic-Proofs/Tactic-Reference/#assumption "Documentation for tactic")`.
The proof side-condition `valid xs i` is automatically dispatched by the `[get_elem_tactic](Tactic-Proofs/Tactic-Reference/#get_elem_tactic "Documentation for tactic")` tactic; this tactic can be extended by adding more clauses to `get_elem_tactic_extensible` using `macro_rules`.
`xs[i]?` and `xs[i]!` do not impose a proof obligation; the former returns an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") elem`, with `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` signalling that the value isn't present, and the latter returns `elem` but panics if the value isn't there, returning `default : elem` based on the `[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") elem` instance. These are provided by the `[GetElem?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?")` class, for which there is a default instance generated from a `[GetElem](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem")` class as long as `valid xs i` is always decidable.
Important instances include:
  * `arr[i] : α` where `arr : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α` and `i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` or `i : USize`: does array indexing with no runtime bounds check and a proof side goal `i < arr.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")`.
  * `l[i] : α` where `l : List α` and `i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`: index into a list, with proof side goal `i < l.length`.


#  Instance Constructor

```
[GetElem?.mk](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.mk").{u, v, w}
```

#  Extends
  * `[GetElem](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem") coll idx elem valid`


#  Methods

```
getElem : (xs : coll) → (i : idx) → valid xs i → elem
```

Inherited from 
  1. `[GetElem](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem") coll idx elem valid`



```
getElem? : coll → idx → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") elem
```

The syntax `arr[i]?` gets the `i`'th element of the collection `arr`, if it is present (and wraps it in `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")`), and otherwise returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
Conventions for notations in identifiers:
  * The recommended spelling of `xs[i]?` in identifiers is `[getElem?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")`.



```
getElem! : [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") elem] → coll → idx → elem
```

The syntax `arr[i]!` gets the `i`'th element of the collection `arr`, if it is present, and otherwise panics at runtime and returns the `[default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default")` term from `[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") elem`.
Conventions for notations in identifiers:
  * The recommended spelling of `xs[i]!` in identifiers is `getElem!`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=LawfulGetElem "Permalink")type class
```


LawfulGetElem.{u, v, w} (cont : Type u) (idx : Type v)
  (elem : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w)) (dom : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (cont → idx → Prop))
  [ge : [GetElem?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?") cont idx elem dom] : Prop


LawfulGetElem.{u, v, w} (cont : Type u)
  (idx : Type v)
  (elem : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w))
  (dom : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (cont → idx → Prop))
  [ge : [GetElem?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?") cont idx elem dom] : Prop


```

Lawful `[GetElem?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?")` instances (which extend `[GetElem](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem")`) are those for which the potentially-failing `[GetElem?.getElem?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")` and `GetElem?.getElem!` operators succeed when the validity predicate is satisfied, and fail when it is not.
#  Instance Constructor

```
[LawfulGetElem.mk](Type-Classes/Basic-Classes/#LawfulGetElem___mk "Documentation for LawfulGetElem.mk").{u, v, w}
```

#  Methods

```
getElem?_def : ∀ (c : cont) (i : idx) [inst : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") (dom c i)], c[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")i[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") if h : dom c i then [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") c[[](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem.getElem")i[]](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem.getElem") else [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")
```

`[GetElem?.getElem?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")` succeeds when the validity predicate is satisfied and fails otherwise.

```
getElem!_def : ∀ [inst : [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") elem] (c : cont) (i : idx),
  c[i]! [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
    match c[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")i[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") with
    | [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") e => e
    | [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") => [default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default")
```

`GetElem?.getElem!` succeeds and fails when `[GetElem](Type-Classes/Basic-Classes/#GetElem___mk "Documentation for GetElem").getElem?` succeeds and fails.
[←10.4. Deriving Instances](Type-Classes/Deriving-Instances/#deriving-instances "10.4. Deriving Instances")[11. Coercions→](Coercions/#coercions "11. Coercions")

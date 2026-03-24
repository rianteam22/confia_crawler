[←20.12. Optional Values](Basic-Types/Optional-Values/#option "20.12. Optional Values")[20.14. Sum Types→](Basic-Types/Sum-Types/#sum-types "20.14. Sum Types")
#  20.13. Tuples[🔗](find/?domain=Verso.Genre.Manual.section&name=tuples "Permalink")
The Lean standard library includes a variety of tuple-like types. In practice, they differ in four ways:
  * whether the first projection is a type or a proposition
  * whether the second projection is a type or a proposition
  * whether the second projection's type depends on the first projection's value
  * whether the type as a whole is a proposition or type

  
|  Type  |  First Projection  |  Second Projection  |  Dependent?  |  Universe  |  
| --- | --- | --- | --- | --- |  
|  `[Prod](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")`  |  `Type u`  |  `Type v`  |  ❌️  |  `Type (max u v)`  |  
|  `[And](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And")`  |  `Prop`  |  `Prop`  |  ❌️  |  `Prop`  |  
|  `[Sigma](Basic-Types/Tuples/#Sigma___mk "Documentation for Sigma")`  |  `Type u`  |  `Type v`  |  ✔  |  `Type (max u v)`  |  
|  `[Subtype](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")`  |  `Type u`  |  `Prop`  |  ✔  |  `Type u`  |  
|  `[Exists](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists")`  |  `Type u`  |  `Prop`  |  ✔  |  `Prop`  |  
Some potential rows in this table do not exist in the library:
  * There is no dependent pair where the first projection is a proposition, because [proof irrelevance](The-Type-System/#--tech-term-proof-irrelevance) renders this meaningless.
  * There is no non-dependent pair that combines a type with a proposition because the situation is rare in practice: grouping data with _unrelated_ proofs is uncommon.


These differences lead to very different use cases. `[Prod](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")` and its variants `[PProd](Basic-Types/Tuples/#PProd___mk "Documentation for PProd")` and `[MProd](Basic-Types/Tuples/#MProd___mk "Documentation for MProd")` simply group data together—they are products. Because its second projection is dependent, `[Sigma](Basic-Types/Tuples/#Sigma___mk "Documentation for Sigma")` has the character of a sum: for each element of the first projection's type, there may be a different type in the second projection. `[Subtype](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")` selects the values of a type that satisfy a predicate. Even though it syntactically resembles a pair, in practice it is treated as an actual subset. `[And](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And")` is a logical connective, and `[Exists](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists")` is a quantifier. This chapter documents the tuple-like pairs, namely `[Prod](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")` and `[Sigma](Basic-Types/Tuples/#Sigma___mk "Documentation for Sigma")`.
##  20.13.1. Ordered Pairs[🔗](find/?domain=Verso.Genre.Manual.section&name=pairs "Permalink")
The type `α × β`, which is a [notation](Notations-and-Macros/Notations/#--tech-term-notation) for `[Prod](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") α β`, contains ordered pairs in which the first item is an `α` and the second is a `β`. These pairs are written in parentheses, separated by commas. Larger tuples are represented as nested tuples, so `α × β × γ` is equivalent to `α × (β × γ)` and `(x, y, z)` is equivalent to `(x, (y, z))`.
syntaxProduct Types

```
term ::= ...
    | 


The product type, usually written α × β. Product types are also called pair or tuple types.
Elements of this type are pairs in which the first element is an α and the second element is a
β.


Products nest to the right, so (x, y, z) : α × β × γ is equivalent to (x, (y, z)) : α × (β × γ).


Conventions for notations in identifiers:




  * The recommended spelling of × in identifiers is Prod.




term × term
```

The product `[Prod](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") α β` is written `α × β`.
syntaxPairs

```
term ::= ...
    | 


Tuple notation; () is short for Unit.unit, (a, b, c) for Prod.mk a (Prod.mk b c), etc. 


Conventions for notations in identifiers:




  * The recommended spelling of (a, b) in identifiers is mk.




([anonymous]term, term)
```

[🔗](find/?domain=Verso.Genre.Manual.doc&name=Prod.snd "Permalink")structure
```


Prod.{u, v} (α : Type u) (β : Type v) : Type (max u v)


Prod.{u, v} (α : Type u) (β : Type v) :
  Type (max u v)


```

The product type, usually written `α × β`. Product types are also called pair or tuple types. Elements of this type are pairs in which the first element is an `α` and the second element is a `β`.
Products nest to the right, so `(x, y, z) : α × β × γ` is equivalent to `(x, (y, z)) : α × (β × γ)`.
Conventions for notations in identifiers:
  * The recommended spelling of `×` in identifiers is `[Prod](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")`.


#  Constructor

```
[Prod.mk](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").{u, v}
```

Constructs a pair. This is usually written `(x, y)` instead of `[Prod.mk](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") x y`.
Conventions for notations in identifiers:
  * The recommended spelling of `(a, b)` in identifiers is `mk`.


#  Fields

```
fst : α
```

The first element of a pair.

```
snd : β
```

The second element of a pair.
There are also the variants `α ×' β` (which is notation for `[PProd](Basic-Types/Tuples/#PProd___mk "Documentation for PProd") α β`) and `[MProd](Basic-Types/Tuples/#MProd___mk "Documentation for MProd")`, which differ with respect to [universe](The-Type-System/Universes/#--tech-term-universes) levels: like `[PSum](Basic-Types/Sum-Types/#PSum___inl "Documentation for PSum")`, `[PProd](Basic-Types/Tuples/#PProd___mk "Documentation for PProd")` allows either `α` or `β` to be a proposition, while `[MProd](Basic-Types/Tuples/#MProd___mk "Documentation for MProd")` requires that both be types at the _same_ universe level. Generally speaking, `[PProd](Basic-Types/Tuples/#PProd___mk "Documentation for PProd")` is primarily used in the implementation of proof automation and the elaborator, as it tends to give rise to universe level unification problems that can't be solved. `[MProd](Basic-Types/Tuples/#MProd___mk "Documentation for MProd")`, on the other hand, can simplify universe level issues in certain advanced use cases.
syntaxProducts of Arbitrary Sorts

```
term ::= ...
    | 


A product type in which the types may be propositions, usually written α ×' β.


This type is primarily used internally and as an implementation detail of proof automation. It is
rarely useful in hand-written code.


Conventions for notations in identifiers:




  * The recommended spelling of ×' in identifiers is PProd.




term ×' term
```

The product `[PProd](Basic-Types/Tuples/#PProd___mk "Documentation for PProd") α β`, in which both types could be propositions, is written `α × β`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=PProd.fst "Permalink")structure
```


PProd.{u, v} (α : Sort u) (β : Sort v) : Sort (max (max 1 u) v)


PProd.{u, v} (α : Sort u) (β : Sort v) :
  Sort (max (max 1 u) v)


```

A product type in which the types may be propositions, usually written `α ×' β`.
This type is primarily used internally and as an implementation detail of proof automation. It is rarely useful in hand-written code.
Conventions for notations in identifiers:
  * The recommended spelling of `×'` in identifiers is `[PProd](Basic-Types/Tuples/#PProd___mk "Documentation for PProd")`.


#  Constructor

```
[PProd.mk](Basic-Types/Tuples/#PProd___mk "Documentation for PProd.mk").{u, v}
```

#  Fields

```
fst : α
```

The first element of a pair.

```
snd : β
```

The second element of a pair.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MProd.snd "Permalink")structure
```


MProd.{u} (α β : Type u) : Type u


MProd.{u} (α β : Type u) : Type u


```

A product type in which both `α` and `β` are in the same universe.
It is called `[MProd](Basic-Types/Tuples/#MProd___mk "Documentation for MProd")` is because it is the _universe-monomorphic_ product type.
#  Constructor

```
[MProd.mk](Basic-Types/Tuples/#MProd___mk "Documentation for MProd.mk").{u}
```

#  Fields

```
fst : α
```

The first element of a pair.

```
snd : β
```

The second element of a pair.
###  20.13.1.1. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=prod-api "Permalink")
As a mere pair, the primary API for `[Prod](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")` is provided by pattern matching and by the first and second projections `[Prod.fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst")` and `[Prod.snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd")`.
####  20.13.1.1.1. Transformation[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Tuples--Ordered-Pairs--API-Reference--Transformation "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Prod.map "Permalink")def
```


Prod.map.{u₁, u₂, v₁, v₂} {α₁ : Type u₁} {α₂ : Type u₂} {β₁ : Type v₁}
  {β₂ : Type v₂} (f : α₁ → α₂) (g : β₁ → β₂) : α₁ [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β₁ → α₂ [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β₂


Prod.map.{u₁, u₂, v₁, v₂} {α₁ : Type u₁}
  {α₂ : Type u₂} {β₁ : Type v₁}
  {β₂ : Type v₂} (f : α₁ → α₂)
  (g : β₁ → β₂) : α₁ [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β₁ → α₂ [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β₂


```

Transforms a pair by applying functions to both elements.
Examples:
  * `(1, 2).[map](Basic-Types/Tuples/#Prod___map "Documentation for Prod.map") (· + 1) (· * 3) = (2, 6)`
  * `(1, 2).[map](Basic-Types/Tuples/#Prod___map "Documentation for Prod.map") toString (· * 3) = ("1", 6)`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Prod.swap "Permalink")def
```


Prod.swap.{u_1, u_2} {α : Type u_1} {β : Type u_2} : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β → β [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") α


Prod.swap.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β → β [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") α


```

Swaps the elements in a pair.
Examples:
  * `(1, 2).[swap](Basic-Types/Tuples/#Prod___swap "Documentation for Prod.swap") = (2, 1)`
  * `("orange", -87).[swap](Basic-Types/Tuples/#Prod___swap "Documentation for Prod.swap") = (-87, "orange")`


####  20.13.1.1.2. Natural Number Ranges[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Tuples--Ordered-Pairs--API-Reference--Natural-Number-Ranges "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Prod.allI "Permalink")def
```


Prod.allI (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : (j : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i.[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") j → j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") i.[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Prod.allI (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f :
    (j : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) →
      i.[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") j → j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") i.[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a predicate holds for all natural numbers in a range.
In particular, `(start, stop).[allI](Basic-Types/Tuples/#Prod___allI "Documentation for Prod.allI") f` returns true if `f` is true for all natural numbers from `start` (inclusive) to `stop` (exclusive).
Examples:
  * `(5, 8).[allI](Basic-Types/Tuples/#Prod___allI "Documentation for Prod.allI") (fun j _ _ => j < 10) = (5 < 10) && (6 < 10) && (7 < 10)`
  * `(5, 8).[allI](Basic-Types/Tuples/#Prod___allI "Documentation for Prod.allI") (fun j _ _ => j % 2 = 0) = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `(6, 7).[allI](Basic-Types/Tuples/#Prod___allI "Documentation for Prod.allI") (fun j _ _ => j % 2 = 0) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Prod.anyI "Permalink")def
```


Prod.anyI (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : (j : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i.[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") j → j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") i.[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Prod.anyI (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f :
    (j : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) →
      i.[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") j → j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") i.[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a predicate holds for any natural number in a range.
In particular, `(start, stop).[allI](Basic-Types/Tuples/#Prod___allI "Documentation for Prod.allI") f` returns true if `f` is true for any natural number from `start` (inclusive) to `stop` (exclusive).
Examples:
  * `(5, 8).[anyI](Basic-Types/Tuples/#Prod___anyI "Documentation for Prod.anyI") (fun j _ _ => j == 6) = (5 == 6) || (6 == 6) || (7 == 6)`
  * `(5, 8).[anyI](Basic-Types/Tuples/#Prod___anyI "Documentation for Prod.anyI") (fun j _ _ => j % 2 = 0) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `(6, 6).[anyI](Basic-Types/Tuples/#Prod___anyI "Documentation for Prod.anyI") (fun j _ _ => j % 2 = 0) = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Prod.foldI "Permalink")def
```


Prod.foldI.{u} {α : Type u} (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : (j : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → i.[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") j → j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") i.[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd") → α → α) (init : α) : α


Prod.foldI.{u} {α : Type u}
  (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f :
    (j : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) →
      i.[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") j → j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") i.[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd") → α → α)
  (init : α) : α


```

Combines an initial value with each natural number from a range, in increasing order.
In particular, `(start, stop).[foldI](Basic-Types/Tuples/#Prod___foldI "Documentation for Prod.foldI") f init` applies `f`on all the numbers from `start` (inclusive) to `stop` (exclusive) in increasing order:
Examples:
  * `(5, 8).[foldI](Basic-Types/Tuples/#Prod___foldI "Documentation for Prod.foldI") (fun j _ _ xs => xs.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") j) #[] = (#[] |>.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") 5 |>.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") 6 |>.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") 7)`
  * `(5, 8).[foldI](Basic-Types/Tuples/#Prod___foldI "Documentation for Prod.foldI") (fun j _ _ xs => xs.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") j) #[] = #[5, 6, 7]`
  * `(5, 8).[foldI](Basic-Types/Tuples/#Prod___foldI "Documentation for Prod.foldI") (fun j _ _ xs => toString j :: xs) [] = ["7", "6", "5"]`


####  20.13.1.1.3. Ordering[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Tuples--Ordered-Pairs--API-Reference--Ordering "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Prod.lexLt "Permalink")def
```


Prod.lexLt.{u_1, u_2} {α : Type u_1} {β : Type u_2} [[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") α] [[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") β]
  (s t : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β) : Prop


Prod.lexLt.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} [[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") α] [[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") β]
  (s t : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β) : Prop


```

Lexicographical order for products.
Two pairs are lexicographically ordered if their first elements are ordered or if their first elements are equal and their second elements are ordered.
##  20.13.2. Dependent Pairs[🔗](find/?domain=Verso.Genre.Manual.section&name=sigma-types "Permalink")
_Dependent pairs_ , also known as _dependent sums_ or _Σ-types_ , are pairs in which the second term's type may depend on the _value_ of the first term. They are closely related to the existential quantifier and `[Subtype](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")`. Unlike existentially quantified statements, dependent pairs are in the `Type` universe and are computationally relevant data. Unlike subtypes, the second term is also computationally relevant data. Like ordinary pairs, dependent pairs may be nested; this nesting is right-associative.
syntaxDependent Pair Types

```
term ::= ...
    | (


binderIdent matches an ident or a _. It is used for identifiers in binding
position, where _ means that the value should be left unnamed and inaccessible.


ident : term) × term
```

```
term ::= ...
    | Σ 


binderIdent matches an ident or a _. It is used for identifiers in binding
position, where _ means that the value should be left unnamed and inaccessible.


ident 


binderIdent matches an ident or a _. It is used for identifiers in binding
position, where _ means that the value should be left unnamed and inaccessible.


ident* (: term)?, term
```

```
term ::= ...
    | Σ (


binderIdent matches an ident or a _. It is used for identifiers in binding
position, where _ means that the value should be left unnamed and inaccessible.


ident 


binderIdent matches an ident or a _. It is used for identifiers in binding
position, where _ means that the value should be left unnamed and inaccessible.


ident* : term), term
```

Dependent pair types bind one or more variables, which are then in scope in the final term. If there is one variable, then its type is a that of the first element in the pair and the final term is the type of the second element in the pair. If there is more than one variable, the types are nested right-associatively. The identifiers may also be `_`. With parentheses, multiple bound variables may have different types, while the unparenthesized variant requires that all have the same type.
Nested Dependent Pair Types
The type
`Σ n k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"), [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n * k)`
is equivalent to
`Σ n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"), Σ k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"), [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n * k)`
and
`(n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) × (k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) × [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n * k)`
The type
`Σ (n k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n * k)) , [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") i.[val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val")`
is equivalent to
`Σ (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), Σ (k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), Σ (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n * k)) , [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") i.[val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val")`
and
`(n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) × (k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) × (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (n * k)) × [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") i.[val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val")`
The two styles of annotation cannot be mixed in a single ``«termΣ_,_» : term```Σ`-type:

```
Σ n kunexpected token '('; expected ',' (i : Fin (n * k)) , Fin i.val
```

```
<example>:1:5-1:7: unexpected token '('; expected ','
```

Dependent pairs are typically used in one of two ways:
  1. They can be used to “package” a concrete type index together with a value of the indexed family, used when the index value is not known ahead of time. The type `Σ n, [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` is a pair of a natural number and some other number that's strictly smaller. This is the most common way to use dependent pairs.
  2. The first element can be thought of as a “tag” that's used to select from among different types for the second term. This is similar to the way that selecting a constructor of a sum type determines the types of the constructor's arguments. For example, the type
`Σ (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")), [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") b [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") α`
is equivalent to `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α`, where `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` is `⟨[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true"), ()⟩` and `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x` is `⟨[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false"), x⟩`. Using dependent pairs this way is uncommon, because it's typically much easier to define a special-purpose [inductive type](The-Type-System/Inductive-Types/#--tech-term-Inductive-types) directly.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Sigma "Permalink")structure
```


Sigma.{u, v} {α : Type u} (β : α → Type v) : Type (max u v)


Sigma.{u, v} {α : Type u}
  (β : α → Type v) : Type (max u v)


```

Dependent pairs, in which the second element's type depends on the value of the first element. The type `[Sigma](Basic-Types/Tuples/#Sigma___mk "Documentation for Sigma") β` is typically written `Σ a : α, β a` or `(a : α) × β a`.
Although its values are pairs, `[Sigma](Basic-Types/Tuples/#Sigma___mk "Documentation for Sigma")` is sometimes known as the _dependent sum type_ , since it is the type level version of an indexed summation.
#  Constructor

```
[Sigma.mk](Basic-Types/Tuples/#Sigma___mk "Documentation for Sigma.mk").{u, v}
```

Constructs a dependent pair.
Using this constructor in a context in which the type is not known usually requires a type ascription to determine `β`. This is because the desired relationship between the two values can't generally be determined automatically.
#  Fields

```
fst : α
```

The first component of a dependent pair.

```
snd : β self.[fst](Basic-Types/Tuples/#Sigma___mk "Documentation for Sigma.fst")
```

The second component of a dependent pair. Its type depends on the first component.
Dependent Pairs with Data
The type `Vector`, which associates a known length with an array, can be placed in a dependent pair with the length itself. While this is logically equivalent to just using `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")`, this construction is sometimes necessary to bridge gaps in an API.
`def getNLinesRev : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [IO](IO/Logical-Model/#IO "Documentation for IO") (Vector [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") n)   | 0 => [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") #v[]   | n + 1 => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")     let xs ← [getNLinesRev](Basic-Types/Tuples/#getNLinesRev-_LPAR_in-Dependent-Pairs-with-Data_RPAR_ "Definition of example") n     return xs.push (← (← [IO.getStdin](IO/Files___-File-Handles___-and-Streams/#IO___getStdin "Documentation for IO.getStdin")).[getLine](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream.getLine"))  def getNLines (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [IO](IO/Logical-Model/#IO "Documentation for IO") (Vector [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") n) := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   return (← [getNLinesRev](Basic-Types/Tuples/#getNLinesRev-_LPAR_in-Dependent-Pairs-with-Data_RPAR_ "Definition of example") n).reverse  partial def getValues : [IO](IO/Logical-Model/#IO "Documentation for IO") (Σ n, Vector [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") n) := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let stdin ← [IO.getStdin](IO/Files___-File-Handles___-and-Streams/#IO___getStdin "Documentation for IO.getStdin")    [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "How many lines to read?"   let howMany ← stdin.[getLine](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream.getLine")    if let [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") howMany := howMany.[trimAscii](Basic-Types/Strings/#String___trimAscii "Documentation for String.trimAscii").[copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy").[toNat?](Basic-Types/Strings/#String___toNat___ "Documentation for String.toNat?") then     return ⟨howMany, (← [getNLines](Basic-Types/Tuples/#getNLines-_LPAR_in-Dependent-Pairs-with-Data_RPAR_ "Definition of example") howMany)⟩   else     [IO.eprintln](IO/Console-Output/#IO___eprintln "Documentation for IO.eprintln") "Please enter a number."     [getValues](Basic-Types/Tuples/#getValues-_LPAR_in-Dependent-Pairs-with-Data_RPAR_ "Definition of example")  def main : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let values ← [getValues](Basic-Types/Tuples/#getValues-_LPAR_in-Dependent-Pairs-with-Data_RPAR_ "Definition of example")   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Got {values.[fst](Basic-Types/Tuples/#Sigma___mk "Documentation for Sigma.fst")} values. They are:"   for x in values.[snd](Basic-Types/Tuples/#Sigma___mk "Documentation for Sigma.snd") do     [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") x.[trimAscii](Basic-Types/Strings/#String___trimAscii "Documentation for String.trimAscii") `
When calling the program with this standard input:
`stdin``4``Apples``Quince``Plums``Raspberries`
the output is:
`stdout``How many lines to read?``Got 4 values. They are:``Raspberries``Plums``Quince``Apples`
Dependent Pairs as Sums
`[Sigma](Basic-Types/Tuples/#Sigma___mk "Documentation for Sigma")` can be used to implement sum types. The `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` in the first projection of `[Sum'](Basic-Types/Tuples/#Sum___-_LPAR_in-Dependent-Pairs-as-Sums_RPAR_ "Definition of example")` indicates which type the second projection is drawn from.
`def Sum' (α : Type) (β : Type) : Type :=   Σ (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")),     [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") b [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")     | [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") => α     | [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") => β `
The injections pair a tag (a `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`) with a value of the indicated type. Annotating them with `match_pattern` allows them to be used in patterns as well as in ordinary terms.
`[variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax") {α β : Type}  @[match_pattern] def Sum'.inl (x : α) : [Sum'](Basic-Types/Tuples/#Sum___-_LPAR_in-Dependent-Pairs-as-Sums_RPAR_ "Definition of example") α β := ⟨[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true"), x⟩  @[match_pattern] def Sum'.inr (x : β) : [Sum'](Basic-Types/Tuples/#Sum___-_LPAR_in-Dependent-Pairs-as-Sums_RPAR_ "Definition of example") α β := ⟨[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false"), x⟩  def Sum'.swap : [Sum'](Basic-Types/Tuples/#Sum___-_LPAR_in-Dependent-Pairs-as-Sums_RPAR_ "Definition of example") α β → [Sum'](Basic-Types/Tuples/#Sum___-_LPAR_in-Dependent-Pairs-as-Sums_RPAR_ "Definition of example") β α   | [.inl](Basic-Types/Tuples/#Sum______inl-_LPAR_in-Dependent-Pairs-as-Sums_RPAR_ "Definition of example") x => [.inr](Basic-Types/Tuples/#Sum______inr-_LPAR_in-Dependent-Pairs-as-Sums_RPAR_ "Definition of example") x   | [.inr](Basic-Types/Tuples/#Sum______inr-_LPAR_in-Dependent-Pairs-as-Sums_RPAR_ "Definition of example") y => [.inl](Basic-Types/Tuples/#Sum______inl-_LPAR_in-Dependent-Pairs-as-Sums_RPAR_ "Definition of example") y `
[Live ↪](javascript:openLiveLink\("CYUwZgBAygrgtgcggCkI3AEBcEAqBPADiAJQqBNwJjgcRXoZgLwBQEEgxcAoBGFAQgPa8AbIgBpmLCHACGAFwDGACwhcA7gEtp8sSwA+EaQCcYICPQB8EVFoi6wkgQGdjZiKUaMAbpP2rJHAcYBvdHIsWhAAXzcAAQBtKTl5AH18GWkQfQA7AF1GUEhYRAA6VQyBFAAPClQSLAKkYIYIQAvyAyNhCHLAS/JouJkFZNT07NzwaHgEYoz9CopSGrHECxdGptsHEHautzyFiftlSXwKOqXyQCTCXeXLHQhJssrnSenysV0niFwTczuPoA"\))
Just as `[Prod](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")` has a variant `[PProd](Basic-Types/Tuples/#PProd___mk "Documentation for PProd")` that accepts propositions as well as types, `[PSigma](Basic-Types/Tuples/#PSigma___mk "Documentation for PSigma")` allows its projections to be propositions. This has the same drawbacks as `[PProd](Basic-Types/Tuples/#PProd___mk "Documentation for PProd")`: it is much more likely to lead to failures of universe level unification. However, `[PSigma](Basic-Types/Tuples/#PSigma___mk "Documentation for PSigma")` can be necessary when implementing custom proof automation or in some rare, advanced use cases.
syntaxFully-Polymorphic Dependent Pair Types

```
term ::= ...
    | Σ' 


binderIdent matches an ident or a _. It is used for identifiers in binding
position, where _ means that the value should be left unnamed and inaccessible.


ident 


binderIdent matches an ident or a _. It is used for identifiers in binding
position, where _ means that the value should be left unnamed and inaccessible.


ident* (: term)? , term
```

```
term ::= ...
    | Σ' (


binderIdent matches an ident or a _. It is used for identifiers in binding
position, where _ means that the value should be left unnamed and inaccessible.


ident 


binderIdent matches an ident or a _. It is used for identifiers in binding
position, where _ means that the value should be left unnamed and inaccessible.


ident* : term), term
```

The rules for nesting `Σ'`, as well as those that govern its binding structure, are the same as those for ``«termΣ_,_» : term```Σ`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=PSigma.snd "Permalink")structure
```


PSigma.{u, v} {α : Sort u} (β : α → Sort v) : Sort (max (max 1 u) v)


PSigma.{u, v} {α : Sort u}
  (β : α → Sort v) :
  Sort (max (max 1 u) v)


```

Fully universe-polymorphic dependent pairs, in which the second element's type depends on the value of the first element and both types are allowed to be propositions. The type `[PSigma](Basic-Types/Tuples/#PSigma___mk "Documentation for PSigma") β` is typically written `Σ' a : α, β a` or `(a : α) ×' β a`.
In practice, this generality leads to universe level constraints that are difficult to solve, so `[PSigma](Basic-Types/Tuples/#PSigma___mk "Documentation for PSigma")` is rarely used in manually-written code. It is usually only used in automation that constructs pairs of arbitrary types.
To pair a value with a proof that a predicate holds for it, use `[Subtype](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")`. To demonstrate that a value exists that satisfies a predicate, use `[Exists](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists")`. A dependent pair with a proposition as its first component is not typically useful due to proof irrelevance: there's no point in depending on a specific proof because all proofs are equal anyway.
#  Constructor

```
[PSigma.mk](Basic-Types/Tuples/#PSigma___mk "Documentation for PSigma.mk").{u, v}
```

Constructs a fully universe-polymorphic dependent pair.
#  Fields

```
fst : α
```

The first component of a dependent pair.

```
snd : β self.[fst](Basic-Types/Tuples/#PSigma___mk "Documentation for PSigma.fst")
```

The second component of a dependent pair. Its type depends on the first component.
[←20.12. Optional Values](Basic-Types/Optional-Values/#option "20.12. Optional Values")[20.14. Sum Types→](Basic-Types/Sum-Types/#sum-types "20.14. Sum Types")

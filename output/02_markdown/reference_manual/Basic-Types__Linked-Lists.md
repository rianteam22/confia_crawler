[←20.14. Sum Types](Basic-Types/Sum-Types/#sum-types "20.14. Sum Types")[20.16. Arrays→](Basic-Types/Arrays/#Array "20.16. Arrays")
#  20.15. Linked Lists[🔗](find/?domain=Verso.Genre.Manual.section&name=List "Permalink")
Linked lists, implemented as the [inductive type](The-Type-System/Inductive-Types/#--tech-term-Inductive-types) `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List")`, contain an ordered sequence of elements. Unlike [arrays](Basic-Types/Arrays/#Array), Lean compiles lists according to the ordinary rules for inductive types; however, some operations on lists are replaced by tail-recursive equivalents in compiled code using the `csimp` mechanism. Lean provides syntax for both literal lists and the constructor `[List.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List "Permalink")inductive type
```


List.{u} (α : Type u) : Type u


List.{u} (α : Type u) : Type u


```

Linked lists: ordered lists, in which each element has a reference to the next element.
Most operations on linked lists take time proportional to the length of the list, because each element must be traversed to find the next element.
`[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` is isomorphic to `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α`, but they are useful for different things:
  * `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` is easier for reasoning, and `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α` is modeled as a wrapper around `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α`.
  * `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` works well as a persistent data structure, when many copies of the tail are shared. When the value is not shared, `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α` will have better performance because it can do destructive updates.


#  Constructors

```
nil.{u} {α : Type u} : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α
```

The empty list, usually written `[]`.
Conventions for notations in identifiers:
  * The recommended spelling of `[]` in identifiers is `[nil](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")`.



```
cons.{u} {α : Type u} (head : α) (tail : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α
```

The list whose first element is `[head](Basic-Types/Linked-Lists/#List___head "Documentation for List.head")`, where `[tail](Basic-Types/Linked-Lists/#List___tail "Documentation for List.tail")` is the rest of the list. Usually written `head :: tail`.
Conventions for notations in identifiers:
  * The recommended spelling of `::` in identifiers is `[cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")`.
  * The recommended spelling of `[a]` in identifiers is `singleton`.


##  20.15.1. Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=list-syntax "Permalink")
List literals are written in square brackets, with the elements of the list separated by commas. The constructor `[List.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")` that adds an element to the front of a list is represented by the infix operator ``«term_::_» : term`
The list whose first element is `head`, where `tail` is the rest of the list. Usually written `head :: tail`.
Conventions for notations in identifiers:
  * The recommended spelling of `::` in identifiers is `cons`.


`[`::`](Basic-Types/Linked-Lists/#_FLQQ_term_________FLQQ_-next-next-next-next-next-next-next-next). The syntax for lists can be used both in ordinary terms and in patterns.
syntaxList Literals

```
term ::= ...
    | 


The syntax [a, b, c] is shorthand for a :: b :: c :: [], or
List.cons a (List.cons b (List.cons c List.nil)). It allows conveniently constructing
list literals.


For lists of length at least 64, an alternative desugaring strategy is used
which uses let bindings as intermediates as in
let left := [d, e, f]; a :: b :: c :: left to avoid creating very deep expressions.
Note that this changes the order of evaluation, although it should not be observable
unless you use side effecting operations like dbg_trace.


Conventions for notations in identifiers:




  * 

The recommended spelling of [] in identifiers is nil.




  * 

The recommended spelling of [a] in identifiers is singleton.






[term,*]
```

The syntax `[a, b, c]` is shorthand for `a :: b :: c :: []`, or `[List.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") a ([List.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") b ([List.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") c [List.nil](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")))`. It allows conveniently constructing list literals.
For lists of length at least 64, an alternative desugaring strategy is used which uses let bindings as intermediates as in `let left := [d, e, f]; a :: b :: c :: left` to avoid creating very deep expressions. Note that this changes the order of evaluation, although it should not be observable unless you use side effecting operations like `[dbg_trace](Tactic-Proofs/Tactic-Reference/#dbg_trace "Documentation for tactic")`.
Conventions for notations in identifiers:
  * The recommended spelling of `[]` in identifiers is `nil`.
  * The recommended spelling of `[a]` in identifiers is `singleton`.


syntaxList Construction

```
term ::= ...
    | 


The list whose first element is head, where tail is the rest of the list.
Usually written head :: tail.


Conventions for notations in identifiers:




  * The recommended spelling of :: in identifiers is cons.




term :: term
```

The list whose first element is `head`, where `tail` is the rest of the list. Usually written `head :: tail`.
Conventions for notations in identifiers:
  * The recommended spelling of `::` in identifiers is `cons`.


Constructing Lists
All of these examples are equivalent:
`example : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := [1, 2, 3] example : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 1 :: [2, 3] example : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 1 :: 2 :: [3] example : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 1 :: 2 :: 3 :: [] example : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 1 :: 2 :: 3 :: [.nil](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil") example : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 1 :: 2 :: [.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3 [.nil](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil") example : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := [.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 ([.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2 ([.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3 [.nil](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil"))) `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAueAZAlgZwC7wHJh0QF54BtARgBp4AmagZgF0AoUSWBZdbPApE8kmSk68Jq3DQ4SVJhz5CAobWWlxbKZ1k8F/eIMTIay+qpYaOM7vL7F9y44bHKAdADs0MCe2lc5vRXsnR2QXAGMAezcMZ3dPb00rf107cKiYwQAKNOiVbMjc0ziYAEoSoA"\))
Pattern Matching and Lists
All of these functions are equivalent:
`def split : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α × [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α   | [] => ([], [])   | [x] => ([x], [])   | x :: x' :: xs =>     let (ys, zs) := [split](Basic-Types/Linked-Lists/#split-_LPAR_in-Pattern-Matching-and-Lists_RPAR_ "Definition of example") xs     (x :: ys, x' :: zs) ``def split' : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α × [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α   | [.nil](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil") => ([.nil](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil"), [.nil](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil"))   | x :: [] => ([.singleton](Basic-Types/Linked-Lists/#List___singleton "Documentation for List.singleton") x, [.nil](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil"))   | x :: x' :: xs =>     let (ys, zs) := [split](Basic-Types/Linked-Lists/#split-_LPAR_in-Pattern-Matching-and-Lists_RPAR_ "Definition of example") xs     (x :: ys, x' :: zs) ``def split'' : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α × [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α   | [.nil](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil") => ([.nil](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil"), [.nil](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil"))   | [.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [.nil](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil") => ([.singleton](Basic-Types/Linked-Lists/#List___singleton "Documentation for List.singleton") x, [.nil](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil"))   | [.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x ([.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x' xs) =>     let (ys, zs) := [split](Basic-Types/Linked-Lists/#split-_LPAR_in-Pattern-Matching-and-Lists_RPAR_ "Definition of example") xs     ([.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x ys, [.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x' zs) `
[Live ↪](javascript:openLiveLink\("CYUwZgBAzgDgNgSwC4QFwQDIKiwjcAUCTCTbPCAdeJwlwCgIIAfCAbQF0IBeAPggAo2ANC1YBKOoxYAPdtz7NpQtmPpNJadJIDk6iJKicu4+nBApeATyhCAXlBFoO0eMl1QjfNanSWhWnbbEaUEhYRCRtdCwqfCIo0go46nEmADoAOwQ4Az50zKFcuGUJT3Q2bN4UqAQ0gHMTJAB7NN18jMLk3R0/L1cDd3q+HwgAhycw13deEogh7vQAmiDwMeRNCMpSWJJqcg2klQgC8oLWzKLUgGMm/TUj2Qqq2vqmlsO288OrtJucr5vtPT2bj9UyDKzDOyjUIuPSTFJ/TpDeHXXTaBY0AC0GIgABUQFQLnAAIYIAC2NBAkiJpPgIDQEAAAtCUI4mc5wqMAEbmcRgACuaUppFh9GqwD5FyQCBeeggfMeNRWSBSYolKAAPABuHhVGksZlCZmaIRxSrVOqmJqsRaU6m0+ls8aso0RRzc3kCoU7EUQVWS6XNWXy81KlVpcWSiBanVkmD69mG9lrE0kM1PS1pVhAA"\))
##  20.15.2. Performance Notes[🔗](find/?domain=Verso.Genre.Manual.section&name=list-performance "Permalink")
The representation of lists is not overridden or modified by the compiler: they are linked lists, with a pointer indirection for each element. Calculating the length of a list requires a full traversal, and modifying an element in a list requires a traversal and reallocation of the prefix of the list that is prior to the element being modified. Due to Lean's reference-counting-based memory management, operations such as `[List.map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map")` that traverse a list, allocating a new `[List.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")` constructor for each in the prior list, can reuse the original list's memory when there are no other references to it.
Because of the important role played by lists in specifications, most list functions are written as straightforwardly as possible using structural recursion. This makes it easier to write proofs by induction, but it also means that these operations consume stack space proportional to the length of the list. There are tail-recursive versions of many list functions that are equivalent to the non-tail-recursive versions, but are more difficult to use when reasoning. In compiled code, the tail-recursive versions are automatically used instead of the non-tail-recursive versions.
##  20.15.3. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=list-api-reference "Permalink")
###  20.15.3.1. Predicates and Relations[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Linked-Lists--API-Reference--Predicates-and-Relations "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.IsPrefix "Permalink")def
```


List.IsPrefix.{u} {α : Type u} (l₁ l₂ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : Prop


List.IsPrefix.{u} {α : Type u}
  (l₁ l₂ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : Prop


```

The first list is a prefix of the second.
`IsPrefix l₁ l₂`, written `l₁ <+: l₂`, means that there exists some `t : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` such that `l₂` has the form `l₁ ++ t`.
The function `[List.isPrefixOf](Basic-Types/Linked-Lists/#List___isPrefixOf "Documentation for List.isPrefixOf")` is a Boolean equivalent.
Conventions for notations in identifiers:
  * The recommended spelling of `<+:` in identifiers is `prefix` (not `isPrefix`).


syntaxList Prefix

```
term ::= ...
    | 


The first list is a prefix of the second.


IsPrefix l₁ l₂, written l₁ <+: l₂, means that there exists some t : List α such that l₂ has
the form l₁ ++ t.


The function List.isPrefixOf is a Boolean equivalent.


Conventions for notations in identifiers:




  * The recommended spelling of <+: in identifiers is prefix (not isPrefix).




term <+: term
```

The first list is a prefix of the second.
`IsPrefix l₁ l₂`, written `l₁ <+: l₂`, means that there exists some `t : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` such that `l₂` has the form `l₁ ++ t`.
The function `[List.isPrefixOf](Basic-Types/Linked-Lists/#List___isPrefixOf "Documentation for List.isPrefixOf")` is a Boolean equivalent.
Conventions for notations in identifiers:
  * The recommended spelling of `<+:` in identifiers is `prefix` (not `isPrefix`).


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.IsSuffix "Permalink")def
```


List.IsSuffix.{u} {α : Type u} (l₁ l₂ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : Prop


List.IsSuffix.{u} {α : Type u}
  (l₁ l₂ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : Prop


```

The first list is a suffix of the second.
`IsSuffix l₁ l₂`, written `l₁ <:+ l₂`, means that there exists some `t : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` such that `l₂` has the form `t ++ l₁`.
The function `[List.isSuffixOf](Basic-Types/Linked-Lists/#List___isSuffixOf "Documentation for List.isSuffixOf")` is a Boolean equivalent.
Conventions for notations in identifiers:
  * The recommended spelling of `<:+` in identifiers is `suffix` (not `isSuffix`).


syntaxList Suffix

```
term ::= ...
    | 


The first list is a suffix of the second.


IsSuffix l₁ l₂, written l₁ <:+ l₂, means that there exists some t : List α such that l₂ has
the form t ++ l₁.


The function List.isSuffixOf is a Boolean equivalent.


Conventions for notations in identifiers:




  * The recommended spelling of <:+ in identifiers is suffix (not isSuffix).




term <:+ term
```

The first list is a suffix of the second.
`IsSuffix l₁ l₂`, written `l₁ <:+ l₂`, means that there exists some `t : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` such that `l₂` has the form `t ++ l₁`.
The function `[List.isSuffixOf](Basic-Types/Linked-Lists/#List___isSuffixOf "Documentation for List.isSuffixOf")` is a Boolean equivalent.
Conventions for notations in identifiers:
  * The recommended spelling of `<:+` in identifiers is `suffix` (not `isSuffix`).


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.IsInfix "Permalink")def
```


List.IsInfix.{u} {α : Type u} (l₁ l₂ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : Prop


List.IsInfix.{u} {α : Type u}
  (l₁ l₂ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : Prop


```

The first list is a contiguous sub-list of the second list. Typically written with the `<:+:` operator.
In other words, `l₁ <:+: l₂` means that there exist lists `s : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` and `t : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` such that `l₂` has the form `s ++ l₁ ++ t`.
Conventions for notations in identifiers:
  * The recommended spelling of `<:+:` in identifiers is `infix` (not `isInfix`).


syntaxList Infix

```
term ::= ...
    | 


The first list is a contiguous sub-list of the second list. Typically written with the <:+:
operator.


In other words, l₁ <:+: l₂ means that there exist lists s : List α and t : List α such that
l₂ has the form s ++ l₁ ++ t.


Conventions for notations in identifiers:




  * The recommended spelling of <:+: in identifiers is infix (not isInfix).




term <:+: term
```

The first list is a contiguous sub-list of the second list. Typically written with the `<:+:` operator.
In other words, `l₁ <:+: l₂` means that there exist lists `s : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` and `t : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` such that `l₂` has the form `s ++ l₁ ++ t`.
Conventions for notations in identifiers:
  * The recommended spelling of `<:+:` in identifiers is `infix` (not `isInfix`).


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.Sublist.cons%E2%82%82 "Permalink")inductive predicate
```


List.Sublist.{u_1} {α : Type u_1} : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → Prop


List.Sublist.{u_1} {α : Type u_1} :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → Prop


```

The first list is a non-contiguous sub-list of the second list. Typically written with the `<+` operator.
In other words, `l₁ <+ l₂` means that `l₁` can be transformed into `l₂` by repeatedly inserting new elements.
#  Constructors

```
slnil.{u_1} {α : Type u_1} : [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil").[Sublist](Basic-Types/Linked-Lists/#List___Sublist___slnil "Documentation for List.Sublist") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")
```

The base case: `[]` is a sublist of `[]`

```
cons.{u_1} {α : Type u_1} {l₁ l₂ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α} (a : α) :
  l₁.[Sublist](Basic-Types/Linked-Lists/#List___Sublist___slnil "Documentation for List.Sublist") l₂ → l₁.[Sublist](Basic-Types/Linked-Lists/#List___Sublist___slnil "Documentation for List.Sublist") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")a [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") l₂[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

If `l₁` is a subsequence of `l₂`, then it is also a subsequence of `a :: l₂`.

```
cons₂.{u_1} {α : Type u_1} {l₁ l₂ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α} (a : α) :
  l₁.[Sublist](Basic-Types/Linked-Lists/#List___Sublist___slnil "Documentation for List.Sublist") l₂ → [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")a [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") l₁[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[Sublist](Basic-Types/Linked-Lists/#List___Sublist___slnil "Documentation for List.Sublist") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")a [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") l₂[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

If `l₁` is a subsequence of `l₂`, then `a :: l₁` is a subsequence of `a :: l₂`.
syntaxSublists

```
term ::= ...
    | 


The first list is a non-contiguous sub-list of the second list. Typically written with the <+
operator.


In other words, l₁ <+ l₂ means that l₁ can be transformed into l₂ by repeatedly inserting new
elements.


term <+ term
```

The first list is a non-contiguous sub-list of the second list. Typically written with the `<+` operator.
In other words, `l₁ <+ l₂` means that `l₁` can be transformed into `l₂` by repeatedly inserting new elements.
This syntax is only available when the `List` namespace is opened.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.Perm.swap "Permalink")inductive predicate
```


List.Perm.{u} {α : Type u} : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → Prop


List.Perm.{u} {α : Type u} :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → Prop


```

Two lists are permutations of each other if they contain the same elements, each occurring the same number of times but not necessarily in the same order.
One list can be proven to be a permutation of another by showing how to transform one into the other by repeatedly swapping adjacent elements.
`[List.isPerm](Basic-Types/Linked-Lists/#List___isPerm "Documentation for List.isPerm")` is a Boolean equivalent of this relation.
#  Constructors

```
nil.{u} {α : Type u} : [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil").[Perm](Basic-Types/Linked-Lists/#List___Perm___nil "Documentation for List.Perm") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")
```

The empty list is a permutation of the empty list: `[] ~ []`.

```
cons.{u} {α : Type u} (x : α) {l₁ l₂ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α} :
  l₁.[Perm](Basic-Types/Linked-Lists/#List___Perm___nil "Documentation for List.Perm") l₂ → [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") l₁[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[Perm](Basic-Types/Linked-Lists/#List___Perm___nil "Documentation for List.Perm") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") l₂[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

If one list is a permutation of the other, adding the same element as the head of each yields lists that are permutations of each other: `l₁ ~ l₂ → x::l₁ ~ x::l₂`.

```
swap.{u} {α : Type u} (x y : α) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") l[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons").[Perm](Basic-Types/Linked-Lists/#List___Perm___nil "Documentation for List.Perm") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") l[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

If two lists are identical except for having their first two elements swapped, then they are permutations of each other: `x::y::l ~ y::x::l`.

```
trans.{u} {α : Type u} {l₁ l₂ l₃ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α} :
  l₁.[Perm](Basic-Types/Linked-Lists/#List___Perm___nil "Documentation for List.Perm") l₂ → l₂.[Perm](Basic-Types/Linked-Lists/#List___Perm___nil "Documentation for List.Perm") l₃ → l₁.[Perm](Basic-Types/Linked-Lists/#List___Perm___nil "Documentation for List.Perm") l₃
```

Permutation is transitive: `l₁ ~ l₂ → l₂ ~ l₃ → l₁ ~ l₃`.
syntaxList Permutation

```
term ::= ...
    | 


Two lists are permutations of each other if they contain the same elements, each occurring the same
number of times but not necessarily in the same order.


One list can be proven to be a permutation of another by showing how to transform one into the other
by repeatedly swapping adjacent elements.


List.isPerm is a Boolean equivalent of this relation.


term ~ term
```

Two lists are permutations of each other if they contain the same elements, each occurring the same number of times but not necessarily in the same order.
One list can be proven to be a permutation of another by showing how to transform one into the other by repeatedly swapping adjacent elements.
`[List.isPerm](Basic-Types/Linked-Lists/#List___isPerm "Documentation for List.isPerm")` is a Boolean equivalent of this relation.
This syntax is only available when the `List` namespace is opened.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.Pairwise.nil "Permalink")inductive predicate
```


List.Pairwise.{u} {α : Type u} (R : α → α → Prop) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → Prop


List.Pairwise.{u} {α : Type u}
  (R : α → α → Prop) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → Prop


```

Each element of a list is related to all later elements of the list by `R`.
`Pairwise R l` means that all the elements of `l` with earlier indexes are `R`-related to all the elements with later indexes.
For example, `Pairwise (· ≠ ·) l` asserts that `l` has no duplicates, and `Pairwise (· < ·) l` asserts that `l` is (strictly) sorted.
Examples:
  * `Pairwise (· < ·) [1, 2, 3] ↔ (1 < 2 ∧ 1 < 3) ∧ 2 < 3`
  * `Pairwise (· = ·) [1, 2, 3] = [False](Basic-Propositions/Truth/#False "Documentation for False")`
  * `Pairwise (· ≠ ·) [1, 2, 3] = [True](Basic-Propositions/Truth/#True___intro "Documentation for True")`


#  Constructors

```
nil.{u} {α : Type u} {R : α → α → Prop} : [List.Pairwise](Basic-Types/Linked-Lists/#List___Pairwise___nil "Documentation for List.Pairwise") R [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")
```

All elements of the empty list are vacuously pairwise related.

```
cons.{u} {α : Type u} {R : α → α → Prop} {a : α}
  {l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α} :
  (∀ (a' : α), a' ∈ l → R a a') →
    [List.Pairwise](Basic-Types/Linked-Lists/#List___Pairwise___nil "Documentation for List.Pairwise") R l → [List.Pairwise](Basic-Types/Linked-Lists/#List___Pairwise___nil "Documentation for List.Pairwise") R [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")a [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") l[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

A nonempty list is pairwise related with `R` if the head is related to every element of the tail and the tail is itself pairwise related.
That is, `a :: l` is `[Pairwise](Basic-Types/Linked-Lists/#List___Pairwise___nil "Documentation for List.Pairwise") R` if:
  * `R` relates `a` to every element of `l`
  * `l` is `[Pairwise](Basic-Types/Linked-Lists/#List___Pairwise___nil "Documentation for List.Pairwise") R`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.Nodup "Permalink")def
```


List.Nodup.{u} {α : Type u} : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → Prop


List.Nodup.{u} {α : Type u} :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → Prop


```

The list has no duplicates: it contains every element at most once.
It is defined as `Pairwise (· ≠ ·)`: each element is unequal to all other elements.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.Lex.cons "Permalink")inductive predicate
```


List.Lex.{u} {α : Type u} (r : α → α → Prop) (as bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : Prop


List.Lex.{u} {α : Type u}
  (r : α → α → Prop) (as bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  Prop


```

Lexicographic ordering for lists with respect to an ordering of elements.
`as` is lexicographically smaller than `bs` if
  * `as` is empty and `bs` is non-empty, or
  * both `as` and `bs` are non-empty, and the head of `as` is less than the head of `bs` according to `r`, or
  * both `as` and `bs` are non-empty, their heads are equal, and the tail of `as` is less than the tail of `bs`.


#  Constructors

```
nil.{u} {α : Type u} {r : α → α → Prop} {a : α}
  {l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α} : [List.Lex](Basic-Types/Linked-Lists/#List___Lex___nil "Documentation for List.Lex") r [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")a [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") l[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

`[]` is the smallest element in the lexicographic order.

```
rel.{u} {α : Type u} {r : α → α → Prop} {a₁ : α}
  {l₁ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α} {a₂ : α} {l₂ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α} (h : r a₁ a₂) :
  [List.Lex](Basic-Types/Linked-Lists/#List___Lex___nil "Documentation for List.Lex") r [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")a₁ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") l₁[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")a₂ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") l₂[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

If the head of the first list is smaller than the head of the second, then the first list is lexicographically smaller than the second list.

```
cons.{u} {α : Type u} {r : α → α → Prop} {a : α}
  {l₁ l₂ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α} (h : [List.Lex](Basic-Types/Linked-Lists/#List___Lex___nil "Documentation for List.Lex") r l₁ l₂) :
  [List.Lex](Basic-Types/Linked-Lists/#List___Lex___nil "Documentation for List.Lex") r [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")a [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") l₁[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")a [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") l₂[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

If two lists have the same head, then their tails determine their lexicographic order. If the tail of the first list is lexicographically smaller than the tail of the second list, then the entire first list is lexicographically smaller than the entire second list.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.Mem "Permalink")inductive predicate
```


List.Mem.{u} {α : Type u} (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → Prop


List.Mem.{u} {α : Type u} (a : α) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → Prop


```

List membership, typically accessed via the `∈` operator.
`a ∈ l` means that `a` is an element of the list `l`. Elements are compared according to Lean's logical equality.
The related function `[List.elem](Basic-Types/Linked-Lists/#List___elem "Documentation for List.elem")` is a Boolean membership test that uses a `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α` instance.
Examples:
  * `a ∈ [x, y, z] ↔ a = x ∨ a = y ∨ a = z`


#  Constructors

```
head.{u} {α : Type u} {a : α} (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [List.Mem](Basic-Types/Linked-Lists/#List___Mem___head "Documentation for List.Mem") a [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")a [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") as[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

The head of a list is a member: `a ∈ a :: as`.

```
tail.{u} {α : Type u} {a : α} (b : α) {as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α} :
  [List.Mem](Basic-Types/Linked-Lists/#List___Mem___head "Documentation for List.Mem") a as → [List.Mem](Basic-Types/Linked-Lists/#List___Mem___head "Documentation for List.Mem") a [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")b [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") as[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

A member of the tail of a list is a member of the list: `a ∈ l → a ∈ b :: l`.
###  20.15.3.2. Constructing Lists[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Linked-Lists--API-Reference--Constructing-Lists "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.singleton "Permalink")def
```


List.singleton.{u} {α : Type u} (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.singleton.{u} {α : Type u} (a : α) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Constructs a single-element list.
Examples:
  * `[List.singleton](Basic-Types/Linked-Lists/#List___singleton "Documentation for List.singleton") 5 = [5]`.
  * `[List.singleton](Basic-Types/Linked-Lists/#List___singleton "Documentation for List.singleton") "green" = ["green"]`.
  * `[List.singleton](Basic-Types/Linked-Lists/#List___singleton "Documentation for List.singleton") [1, 2, 3] = [[1, 2, 3]]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.concat "Permalink")def
```


List.concat.{u} {α : Type u} : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.concat.{u} {α : Type u} :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Adds an element to the _end_ of a list.
The added element is the last element of the resulting list.
Examples:
  * `[List.concat](Basic-Types/Linked-Lists/#List___concat "Documentation for List.concat") ["red", "yellow"] "green" = ["red", "yellow", "green"]`
  * `[List.concat](Basic-Types/Linked-Lists/#List___concat "Documentation for List.concat") [1, 2, 3] 4 = [1, 2, 3, 4]`
  * `[List.concat](Basic-Types/Linked-Lists/#List___concat "Documentation for List.concat") [] () = [()]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.replicate "Permalink")def
```


List.replicate.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.replicate.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Creates a list that contains `n` copies of `a`.
  * `[List.replicate](Basic-Types/Linked-Lists/#List___replicate "Documentation for List.replicate") 5 "five" = ["five", "five", "five", "five", "five"]`
  * `[List.replicate](Basic-Types/Linked-Lists/#List___replicate "Documentation for List.replicate") 0 "zero" = []`
  * `[List.replicate](Basic-Types/Linked-Lists/#List___replicate "Documentation for List.replicate") 2 ' ' = [' ', ' ']`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.replicateTR "Permalink")def
```


List.replicateTR.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.replicateTR.{u} {α : Type u}
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Creates a list that contains `n` copies of `a`.
This is a tail-recursive version of `[List.replicate](Basic-Types/Linked-Lists/#List___replicate "Documentation for List.replicate")`.
  * `[List.replicateTR](Basic-Types/Linked-Lists/#List___replicateTR "Documentation for List.replicateTR") 5 "five" = ["five", "five", "five", "five", "five"]`
  * `[List.replicateTR](Basic-Types/Linked-Lists/#List___replicateTR "Documentation for List.replicateTR") 0 "zero" = []`
  * `[List.replicateTR](Basic-Types/Linked-Lists/#List___replicateTR "Documentation for List.replicateTR") 2 ' ' = [' ', ' ']`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.ofFn "Permalink")def
```


List.ofFn.{u_1} {α : Type u_1} {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (f : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.ofFn.{u_1} {α : Type u_1} {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (f : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Creates a list by applying `f` to each potential index in order, starting at `0`.
Examples:
  * `[List.ofFn](Basic-Types/Linked-Lists/#List___ofFn "Documentation for List.ofFn") (n := 3) toString = ["0", "1", "2"]`
  * `[List.ofFn](Basic-Types/Linked-Lists/#List___ofFn "Documentation for List.ofFn") (fun i => #["red", "green", "blue"].get i.val i.isLt) = ["red", "green", "blue"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.append "Permalink")def
```


List.append.{u_1} {α : Type u_1} (xs ys : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.append.{u_1} {α : Type u_1}
  (xs ys : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Appends two lists. Normally used via the `++` operator.
Appending lists takes time proportional to the length of the first list: `O(|xs|)`.
Examples:
  * `[1, 2, 3] ++ [4, 5] = [1, 2, 3, 4, 5]`.
  * `[] ++ [4, 5] = [4, 5]`.
  * `[1, 2, 3] ++ [] = [1, 2, 3]`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.appendTR "Permalink")def
```


List.appendTR.{u} {α : Type u} (as bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.appendTR.{u} {α : Type u}
  (as bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Appends two lists. Normally used via the `++` operator.
Appending lists takes time proportional to the length of the first list: `O(|xs|)`.
This is a tail-recursive version of `[List.append](Basic-Types/Linked-Lists/#List___append "Documentation for List.append")`.
Examples:
  * `[1, 2, 3] ++ [4, 5] = [1, 2, 3, 4, 5]`.
  * `[] ++ [4, 5] = [4, 5]`.
  * `[1, 2, 3] ++ [] = [1, 2, 3]`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.range "Permalink")def
```


List.range (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


List.range (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns a list of the numbers from `0` to `n` exclusive, in increasing order.
`O(n)`.
Examples:
  * `range 5 = [0, 1, 2, 3, 4]`
  * `range 0 = []`
  * `range 2 = [0, 1]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.range' "Permalink")def
```


List.range' (start len : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (step : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 1) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


List.range' (start len : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (step : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 1) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns a list of the numbers with the given length `len`, starting at `start` and increasing by `step` at each element.
In other words, `[List.range'](Basic-Types/Linked-Lists/#List___range___ "Documentation for List.range'") start len step` is `[start, start+step, ..., start+(len-1)*step]`.
Examples:
  * `[List.range'](Basic-Types/Linked-Lists/#List___range___ "Documentation for List.range'") 0 3 (step := 1) = [0, 1, 2]`
  * `[List.range'](Basic-Types/Linked-Lists/#List___range___ "Documentation for List.range'") 0 3 (step := 2) = [0, 2, 4]`
  * `[List.range'](Basic-Types/Linked-Lists/#List___range___ "Documentation for List.range'") 0 4 (step := 2) = [0, 2, 4, 6]`
  * `[List.range'](Basic-Types/Linked-Lists/#List___range___ "Documentation for List.range'") 3 4 (step := 2) = [3, 5, 7, 9]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.range'TR "Permalink")def
```


List.range'TR (s n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (step : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 1) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


List.range'TR (s n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (step : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 1) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns a list of the numbers with the given length `len`, starting at `start` and increasing by `step` at each element.
In other words, `[List.range'TR](Basic-Types/Linked-Lists/#List___range___TR "Documentation for List.range'TR") start len step` is `[start, start+step, ..., start+(len-1)*step]`.
This is a tail-recursive version of `[List.range'](Basic-Types/Linked-Lists/#List___range___ "Documentation for List.range'")`.
Examples:
  * `[List.range'TR](Basic-Types/Linked-Lists/#List___range___TR "Documentation for List.range'TR") 0 3 (step := 1) = [0, 1, 2]`
  * `[List.range'TR](Basic-Types/Linked-Lists/#List___range___TR "Documentation for List.range'TR") 0 3 (step := 2) = [0, 2, 4]`
  * `[List.range'TR](Basic-Types/Linked-Lists/#List___range___TR "Documentation for List.range'TR") 0 4 (step := 2) = [0, 2, 4, 6]`
  * `[List.range'TR](Basic-Types/Linked-Lists/#List___range___TR "Documentation for List.range'TR") 3 4 (step := 2) = [3, 5, 7, 9]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.finRange "Permalink")def
```


List.finRange (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n)


List.finRange (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n)


```

Lists all elements of `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` in order, starting at `0`.
Examples:
  * `[List.finRange](Basic-Types/Linked-Lists/#List___finRange "Documentation for List.finRange") 0 = ([] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 0))`
  * `[List.finRange](Basic-Types/Linked-Lists/#List___finRange "Documentation for List.finRange") 2 = ([0, 1] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 2))`


###  20.15.3.3. Length[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Linked-Lists--API-Reference--Length "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.length "Permalink")def
```


List.length.{u_1} {α : Type u_1} : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


List.length.{u_1} {α : Type u_1} :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The length of a list.
This function is overridden in the compiler to `lengthTR`, which uses constant stack space.
Examples:
  * `([] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")).[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") = 0`
  * `["green", "brown"].[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") = 2`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.lengthTR "Permalink")def
```


List.lengthTR.{u_1} {α : Type u_1} (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


List.lengthTR.{u_1} {α : Type u_1}
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The length of a list.
This is a tail-recursive version of `[List.length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")`, used to implement `[List.length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")` without running out of stack space.
Examples:
  * `([] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")).[lengthTR](Basic-Types/Linked-Lists/#List___lengthTR "Documentation for List.lengthTR") = 0`
  * `["green", "brown"].[lengthTR](Basic-Types/Linked-Lists/#List___lengthTR "Documentation for List.lengthTR") = 2`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.isEmpty "Permalink")def
```


List.isEmpty.{u} {α : Type u} : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


List.isEmpty.{u} {α : Type u} :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a list is empty.
`O(1)`.
Examples:
  * `[].[isEmpty](Basic-Types/Linked-Lists/#List___isEmpty "Documentation for List.isEmpty") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `["grape"].[isEmpty](Basic-Types/Linked-Lists/#List___isEmpty "Documentation for List.isEmpty") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `["apple", "banana"].[isEmpty](Basic-Types/Linked-Lists/#List___isEmpty "Documentation for List.isEmpty") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


###  20.15.3.4. Head and Tail[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Linked-Lists--API-Reference--Head-and-Tail "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.head "Permalink")def
```


List.head.{u} {α : Type u} (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : as ≠ [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil") → α


List.head.{u} {α : Type u} (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  as ≠ [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil") → α


```

Returns the first element of a non-empty list.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.head? "Permalink")def
```


List.head?.{u} {α : Type u} : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


List.head?.{u} {α : Type u} :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Returns the first element in the list, if there is one. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the list is empty.
Use `[List.headD](Basic-Types/Linked-Lists/#List___headD "Documentation for List.headD")` to provide a fallback value for empty lists, or `[List.head!](Basic-Types/Linked-Lists/#List___head___-next "Documentation for List.head!")` to panic on empty lists.
Examples:
  * `([] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")).[head?](Basic-Types/Linked-Lists/#List___head___ "Documentation for List.head?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `[3, 2, 1].[head?](Basic-Types/Linked-Lists/#List___head___ "Documentation for List.head?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 3`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.headD "Permalink")def
```


List.headD.{u} {α : Type u} (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (fallback : α) : α


List.headD.{u} {α : Type u} (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (fallback : α) : α


```

Returns the first element in the list if there is one, or `fallback` if the list is empty.
Use `[List.head?](Basic-Types/Linked-Lists/#List___head___ "Documentation for List.head?")` to return an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")`, and `[List.head!](Basic-Types/Linked-Lists/#List___head___-next "Documentation for List.head!")` to panic on empty lists.
Examples:
  * `[].[headD](Basic-Types/Linked-Lists/#List___headD "Documentation for List.headD") "empty" = "empty"`
  * `[].[headD](Basic-Types/Linked-Lists/#List___headD "Documentation for List.headD") 2 = 2`
  * `["head", "shoulders", "knees"].[headD](Basic-Types/Linked-Lists/#List___headD "Documentation for List.headD") "toes" = "head"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.head! "Permalink")def
```


List.head!.{u_1} {α : Type u_1} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → α


List.head!.{u_1} {α : Type u_1}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → α


```

Returns the first element in the list. If the list is empty, panics and returns `[default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default")`.
Safer alternatives include:
  * `[List.head](Basic-Types/Linked-Lists/#List___head "Documentation for List.head")`, which requires a proof that the list is non-empty,
  * `[List.head?](Basic-Types/Linked-Lists/#List___head___ "Documentation for List.head?")`, which returns an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")`, and
  * `[List.headD](Basic-Types/Linked-Lists/#List___headD "Documentation for List.headD")`, which returns an explicitly-provided fallback value on empty lists.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.tail "Permalink")def
```


List.tail.{u} {α : Type u} : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.tail.{u} {α : Type u} :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Drops the first element of a nonempty list, returning the tail. Returns `[]` when the argument is empty.
Examples:
  * `["apple", "banana", "grape"].[tail](Basic-Types/Linked-Lists/#List___tail "Documentation for List.tail") = ["banana", "grape"]`
  * `["apple"].[tail](Basic-Types/Linked-Lists/#List___tail "Documentation for List.tail") = []`
  * `([] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")).[tail](Basic-Types/Linked-Lists/#List___tail "Documentation for List.tail") = []`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.tail! "Permalink")def
```


List.tail!.{u_1} {α : Type u_1} : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.tail!.{u_1} {α : Type u_1} :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Drops the first element of a nonempty list, returning the tail. If the list is empty, this function panics when executed and returns the empty list.
Safer alternatives include
  * `tail`, which returns the empty list without panicking,
  * `tail?`, which returns an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")`, and
  * `tailD`, which returns a fallback value when passed the empty list.


Examples:
  * `["apple", "banana", "grape"].[tail!](Basic-Types/Linked-Lists/#List___tail___ "Documentation for List.tail!") = ["banana", "grape"]`
  * `["banana", "grape"].[tail!](Basic-Types/Linked-Lists/#List___tail___ "Documentation for List.tail!") = ["grape"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.tail? "Permalink")def
```


List.tail?.{u} {α : Type u} : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)


List.tail?.{u} {α : Type u} :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)


```

Drops the first element of a nonempty list, returning the tail. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` when the argument is empty.
Alternatives include `[List.tail](Basic-Types/Linked-Lists/#List___tail "Documentation for List.tail")`, which returns the empty list on failure, `[List.tailD](Basic-Types/Linked-Lists/#List___tailD "Documentation for List.tailD")`, which returns an explicit fallback value, and `[List.tail!](Basic-Types/Linked-Lists/#List___tail___ "Documentation for List.tail!")`, which panics on the empty list.
Examples:
  * `["apple", "banana", "grape"].[tail?](Basic-Types/Linked-Lists/#List___tail___-next "Documentation for List.tail?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ["banana", "grape"]`
  * `["apple"].[tail?](Basic-Types/Linked-Lists/#List___tail___-next "Documentation for List.tail?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") []`
  * `([] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")).[tail](Basic-Types/Linked-Lists/#List___tail "Documentation for List.tail") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.tailD "Permalink")def
```


List.tailD.{u} {α : Type u} (l fallback : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.tailD.{u} {α : Type u}
  (l fallback : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Drops the first element of a nonempty list, returning the tail. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` when the argument is empty.
Alternatives include `[List.tail](Basic-Types/Linked-Lists/#List___tail "Documentation for List.tail")`, which returns the empty list on failure, `[List.tail?](Basic-Types/Linked-Lists/#List___tail___-next "Documentation for List.tail?")`, which returns an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")`, and `[List.tail!](Basic-Types/Linked-Lists/#List___tail___ "Documentation for List.tail!")`, which panics on the empty list.
Examples:
  * `["apple", "banana", "grape"].[tailD](Basic-Types/Linked-Lists/#List___tailD "Documentation for List.tailD") ["orange"] = ["banana", "grape"]`
  * `["apple"].[tailD](Basic-Types/Linked-Lists/#List___tailD "Documentation for List.tailD") ["orange"] = []`
  * `[].[tailD](Basic-Types/Linked-Lists/#List___tailD "Documentation for List.tailD") ["orange"] = ["orange"]`


###  20.15.3.5. Lookups[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Linked-Lists--API-Reference--Lookups "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.get "Permalink")def
```


List.get.{u} {α : Type u} (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") as.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") → α


List.get.{u} {α : Type u} (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") as.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") → α


```

Returns the element at the provided index, counting from `0`.
In other words, for `i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") as.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")`, `as.[get](Basic-Types/Linked-Lists/#List___get "Documentation for List.get") i` returns the `i`'th element of the list `as`. Because the index is a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` bounded by the list's length, the index will never be out of bounds.
Examples:
  * `["spring", "summer", "fall", "winter"].[get](Basic-Types/Linked-Lists/#List___get "Documentation for List.get") (2 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 4) = "fall"`
  * `["spring", "summer", "fall", "winter"].[get](Basic-Types/Linked-Lists/#List___get "Documentation for List.get") (0 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 4) = "spring"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.getD "Permalink")def
```


List.getD.{u_1} {α : Type u_1} (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (fallback : α) :
  α


List.getD.{u_1} {α : Type u_1}
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (fallback : α) :
  α


```

Returns the element at the provided index, counting from `0`. Returns `fallback` if the index is out of bounds.
To return an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` depending on whether the index is in bounds, use `as[i]?`. To panic if the index is out of bounds, use `as[i]!`.
Examples:
  * `["spring", "summer", "fall", "winter"].[getD](Basic-Types/Linked-Lists/#List___getD "Documentation for List.getD") 2 "never" = "fall"`
  * `["spring", "summer", "fall", "winter"].[getD](Basic-Types/Linked-Lists/#List___getD "Documentation for List.getD") 0 "never" = "spring"`
  * `["spring", "summer", "fall", "winter"].[getD](Basic-Types/Linked-Lists/#List___getD "Documentation for List.getD") 4 "never" = "never"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.getLast "Permalink")def
```


List.getLast.{u} {α : Type u} (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : as ≠ [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil") → α


List.getLast.{u} {α : Type u}
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : as ≠ [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil") → α


```

Returns the last element of a non-empty list.
Examples:
  * `["circle", "rectangle"].[getLast](Basic-Types/Linked-Lists/#List___getLast "Documentation for List.getLast") (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")) = "rectangle"`
  * `["circle"].[getLast](Basic-Types/Linked-Lists/#List___getLast "Documentation for List.getLast") (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")) = "circle"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.getLast? "Permalink")def
```


List.getLast?.{u} {α : Type u} : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


List.getLast?.{u} {α : Type u} :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Returns the last element in the list, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the list is empty.
Alternatives include `[List.getLastD](Basic-Types/Linked-Lists/#List___getLastD "Documentation for List.getLastD")`, which takes a fallback value for empty lists, and `[List.getLast!](Basic-Types/Linked-Lists/#List___getLast___-next "Documentation for List.getLast!")`, which panics on empty lists.
Examples:
  * `["circle", "rectangle"].[getLast?](Basic-Types/Linked-Lists/#List___getLast___ "Documentation for List.getLast?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "rectangle"`
  * `["circle"].[getLast?](Basic-Types/Linked-Lists/#List___getLast___ "Documentation for List.getLast?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "circle"`
  * `([] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")).[getLast?](Basic-Types/Linked-Lists/#List___getLast___ "Documentation for List.getLast?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.getLastD "Permalink")def
```


List.getLastD.{u} {α : Type u} (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (fallback : α) : α


List.getLastD.{u} {α : Type u}
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (fallback : α) : α


```

Returns the last element in the list, or `fallback` if the list is empty.
Alternatives include `[List.getLast?](Basic-Types/Linked-Lists/#List___getLast___ "Documentation for List.getLast?")`, which returns an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")`, and `[List.getLast!](Basic-Types/Linked-Lists/#List___getLast___-next "Documentation for List.getLast!")`, which panics on empty lists.
Examples:
  * `["circle", "rectangle"].[getLastD](Basic-Types/Linked-Lists/#List___getLastD "Documentation for List.getLastD") "oval" = "rectangle"`
  * `["circle"].[getLastD](Basic-Types/Linked-Lists/#List___getLastD "Documentation for List.getLastD") "oval" = "circle"`
  * `([] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")).[getLastD](Basic-Types/Linked-Lists/#List___getLastD "Documentation for List.getLastD") "oval" = "oval"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.getLast! "Permalink")def
```


List.getLast!.{u_1} {α : Type u_1} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → α


List.getLast!.{u_1} {α : Type u_1}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → α


```

Returns the last element in the list. Panics and returns `[default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default")` if the list is empty.
Safer alternatives include:
  * `getLast?`, which returns an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")`,
  * `getLastD`, which takes a fallback value for empty lists, and
  * `getLast`, which requires a proof that the list is non-empty.


Examples:
  * `["circle", "rectangle"].[getLast!](Basic-Types/Linked-Lists/#List___getLast___-next "Documentation for List.getLast!") = "rectangle"`
  * `["circle"].[getLast!](Basic-Types/Linked-Lists/#List___getLast___-next "Documentation for List.getLast!") = "circle"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.lookup "Permalink")def
```


List.lookup.{u, v} {α : Type u} {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] :
  α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


List.lookup.{u, v} {α : Type u}
  {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] :
  α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


```

Treats the list as an association list that maps keys to values, returning the first value whose key is equal to the specified key.
`O(|l|)`.
Examples:
  * `[(1, "one"), (3, "three"), (3, "other")].[lookup](Basic-Types/Linked-Lists/#List___lookup "Documentation for List.lookup") 3 = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "three"`
  * `[(1, "one"), (3, "three"), (3, "other")].[lookup](Basic-Types/Linked-Lists/#List___lookup "Documentation for List.lookup") 2 = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.max? "Permalink")def
```


List.max?.{u} {α : Type u} [[Max](Type-Classes/Basic-Classes/#Max___mk "Documentation for Max") α] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


List.max?.{u} {α : Type u} [[Max](Type-Classes/Basic-Classes/#Max___mk "Documentation for Max") α] :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Returns the largest element of the list if it is not empty, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if it is empty.
Examples:
  * `[].max? = none`
  * `[4].[max?](Basic-Types/Linked-Lists/#List___max___ "Documentation for List.max?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 4`
  * `[1, 4, 2, 10, 6].[max?](Basic-Types/Linked-Lists/#List___max___ "Documentation for List.max?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 10`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.min? "Permalink")def
```


List.min?.{u} {α : Type u} [[Min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min") α] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


List.min?.{u} {α : Type u} [[Min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min") α] :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Returns the smallest element of the list if it is not empty, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if it is empty.
Examples:
  * `[].min? = none`
  * `[4].[min?](Basic-Types/Linked-Lists/#List___min___ "Documentation for List.min?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 4`
  * `[1, 4, 2, 10, 6].[min?](Basic-Types/Linked-Lists/#List___min___ "Documentation for List.min?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 1`


###  20.15.3.6. Queries[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Linked-Lists--API-Reference--Queries "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.count "Permalink")def
```


List.count.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


List.count.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Counts the number of times an element occurs in a list.
Examples:
  * `[1, 1, 2, 3, 5].[count](Basic-Types/Linked-Lists/#List___count "Documentation for List.count") 1 = 2`
  * `[1, 1, 2, 3, 5].[count](Basic-Types/Linked-Lists/#List___count "Documentation for List.count") 5 = 1`
  * `[1, 1, 2, 3, 5].[count](Basic-Types/Linked-Lists/#List___count "Documentation for List.count") 4 = 0`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.countP "Permalink")def
```


List.countP.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


List.countP.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Counts the number of elements in the list `l` that satisfy the Boolean predicate `p`.
Examples:
  * `[1, 2, 3, 4, 5].[countP](Basic-Types/Linked-Lists/#List___countP "Documentation for List.countP") (· % 2 == 0) = 2`
  * `[1, 2, 3, 4, 5].[countP](Basic-Types/Linked-Lists/#List___countP "Documentation for List.countP") (· < 5) = 4`
  * `[1, 2, 3, 4, 5].[countP](Basic-Types/Linked-Lists/#List___countP "Documentation for List.countP") (· > 5) = 0`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.idxOf "Permalink")def
```


List.idxOf.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


List.idxOf.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the index of the first element equal to `a`, or the length of the list if no element is equal to `a`.
Examples:
  * `["carrot", "potato", "broccoli"].[idxOf](Basic-Types/Linked-Lists/#List___idxOf "Documentation for List.idxOf") "carrot" = 0`
  * `["carrot", "potato", "broccoli"].[idxOf](Basic-Types/Linked-Lists/#List___idxOf "Documentation for List.idxOf") "broccoli" = 2`
  * `["carrot", "potato", "broccoli"].[idxOf](Basic-Types/Linked-Lists/#List___idxOf "Documentation for List.idxOf") "tomato" = 3`
  * `["carrot", "potato", "broccoli"].[idxOf](Basic-Types/Linked-Lists/#List___idxOf "Documentation for List.idxOf") "anything else" = 3`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.idxOf? "Permalink")def
```


List.idxOf?.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


List.idxOf?.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the index of the first element equal to `a`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no element is equal to `a`.
Examples:
  * `["carrot", "potato", "broccoli"].[idxOf?](Basic-Types/Linked-Lists/#List___idxOf___ "Documentation for List.idxOf?") "carrot" = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 0`
  * `["carrot", "potato", "broccoli"].[idxOf?](Basic-Types/Linked-Lists/#List___idxOf___ "Documentation for List.idxOf?") "broccoli" = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2`
  * `["carrot", "potato", "broccoli"].[idxOf?](Basic-Types/Linked-Lists/#List___idxOf___ "Documentation for List.idxOf?") "tomato" = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `["carrot", "potato", "broccoli"].[idxOf?](Basic-Types/Linked-Lists/#List___idxOf___ "Documentation for List.idxOf?") "anything else" = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.finIdxOf? "Permalink")def
```


List.finIdxOf?.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (a : α) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") l.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"))


List.finIdxOf?.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (a : α) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") l.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"))


```

Returns the index of the first element equal to `a`, or the length of the list if no element is equal to `a`. The index is returned as a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")`, which guarantees that it is in bounds.
Examples:
  * `["carrot", "potato", "broccoli"].[finIdxOf?](Basic-Types/Linked-Lists/#List___finIdxOf___ "Documentation for List.finIdxOf?") "carrot" = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 0`
  * `["carrot", "potato", "broccoli"].[finIdxOf?](Basic-Types/Linked-Lists/#List___finIdxOf___ "Documentation for List.finIdxOf?") "broccoli" = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2`
  * `["carrot", "potato", "broccoli"].[finIdxOf?](Basic-Types/Linked-Lists/#List___finIdxOf___ "Documentation for List.finIdxOf?") "tomato" = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `["carrot", "potato", "broccoli"].[finIdxOf?](Basic-Types/Linked-Lists/#List___finIdxOf___ "Documentation for List.finIdxOf?") "anything else" = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.find? "Permalink")def
```


List.find?.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


List.find?.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Returns the first element of the list for which the predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such element is found.
`O(|l|)`.
Examples:
  * `[7, 6, 5, 8, 1, 2, 6].[find?](Basic-Types/Linked-Lists/#List___find___ "Documentation for List.find?") (· < 5) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 1`
  * `[7, 6, 5, 8, 1, 2, 6].[find?](Basic-Types/Linked-Lists/#List___find___ "Documentation for List.find?") (· < 1) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.findFinIdx? "Permalink")def
```


List.findFinIdx?.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") l.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"))


List.findFinIdx?.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") l.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length"))


```

Returns the index of the first element for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if there is no such element. The index is returned as a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")`, which guarantees that it is in bounds.
Examples:
  * `[7, 6, 5, 8, 1, 2, 6].[findFinIdx?](Basic-Types/Linked-Lists/#List___findFinIdx___ "Documentation for List.findFinIdx?") (· < 5) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (4 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 7)`
  * `[7, 6, 5, 8, 1, 2, 6].[findFinIdx?](Basic-Types/Linked-Lists/#List___findFinIdx___ "Documentation for List.findFinIdx?") (· < 1) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.findIdx "Permalink")def
```


List.findIdx.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


List.findIdx.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the index of the first element for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, or the length of the list if there is no such element.
Examples:
  * `[7, 6, 5, 8, 1, 2, 6].[findIdx](Basic-Types/Linked-Lists/#List___findIdx "Documentation for List.findIdx") (· < 5) = 4`
  * `[7, 6, 5, 8, 1, 2, 6].[findIdx](Basic-Types/Linked-Lists/#List___findIdx "Documentation for List.findIdx") (· < 1) = 7`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.findIdx? "Permalink")def
```


List.findIdx?.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


List.findIdx?.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the index of the first element for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if there is no such element.
Examples:
  * `[7, 6, 5, 8, 1, 2, 6].[findIdx](Basic-Types/Linked-Lists/#List___findIdx "Documentation for List.findIdx") (· < 5) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 4`
  * `[7, 6, 5, 8, 1, 2, 6].[findIdx](Basic-Types/Linked-Lists/#List___findIdx "Documentation for List.findIdx") (· < 1) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.findM? "Permalink")def
```


List.findM?.{u} {m : Type → Type u} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type}
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)


List.findM?.{u} {m : Type → Type u}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type} (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)


```

Returns the first element of the list for which the monadic predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such element is found. Elements of the list are checked in order.
`O(|l|)`.
Example:
``some 1``Almost! 6 Almost! 5 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [7, 6, 5, 8, 1, 2, 6].[findM?](Basic-Types/Linked-Lists/#List___findM___ "Documentation for List.findM?") fun i => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") if i < 5 then return [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") if i ≤ 6 then [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Almost! {i}" return [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") ``Almost! 6 Almost! 5``[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 1`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.findSome? "Permalink")def
```


List.findSome?.{u, v} {α : Type u} {β : Type v} (f : α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


List.findSome?.{u, v} {α : Type u}
  {β : Type v} (f : α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


```

Returns the first non-`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` result of applying `f` to each element of the list in order. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if `f` returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` for all elements of the list.
`O(|l|)`.
Examples:
  * `[7, 6, 5, 8, 1, 2, 6].[findSome?](Basic-Types/Linked-Lists/#List___findSome___ "Documentation for List.findSome?") (fun x => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x < 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (10 * x) [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 10`
  * `[7, 6, 5, 8, 1, 2, 6].[findSome?](Basic-Types/Linked-Lists/#List___findSome___ "Documentation for List.findSome?") (fun x => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x < 1 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (10 * x) [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.findSomeM? "Permalink")def
```


List.findSomeM?.{u, v, w} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type w}
  {β : Type u} (f : α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


List.findSomeM?.{u, v, w}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type w} {β : Type u}
  (f : α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


```

Returns the first non-`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` result of applying the monadic function `f` to each element of the list, in order. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if `f` returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` for all elements.
`O(|l|)`.
Example:
``some 10``Almost! 6 Almost! 5 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [7, 6, 5, 8, 1, 2, 6].[findSomeM?](Basic-Types/Linked-Lists/#List___findSomeM___ "Documentation for List.findSomeM?") fun i => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") if i < 5 then return [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (i * 10) if i ≤ 6 then [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Almost! {i}" return [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") ``Almost! 6 Almost! 5``[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 10`
###  20.15.3.7. Conversions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Linked-Lists--API-Reference--Conversions "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.toArray "Permalink")def
```


List.toArray.{u_1} {α : Type u_1} (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


List.toArray.{u_1} {α : Type u_1}
  (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Converts a `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` into an `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α`.
`O(|xs|)`. At runtime, this operation is implemented by `[List.toArrayImpl](Basic-Types/Linked-Lists/#List___toArrayImpl "Documentation for List.toArrayImpl")` and takes time linear in the length of the list. `[List.toArray](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")` should be used instead of `[Array.mk](Basic-Types/Arrays/#Array___mk "Documentation for Array.mk")`.
Examples:
  * `[1, 2, 3].[toArray](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray") = #[1, 2, 3]`
  * `["monday", "wednesday", friday"].toArray = #["monday", "wednesday", friday"].`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.toArrayImpl "Permalink")def
```


List.toArrayImpl.{u_1} {α : Type u_1} (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


List.toArrayImpl.{u_1} {α : Type u_1}
  (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Converts a `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` into an `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α` by repeatedly pushing elements from the list onto an empty array. `O(|xs|)`.
Use `[List.toArray](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")` instead of calling this function directly. At runtime, this operation implements both `[List.toArray](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")` and `[Array.mk](Basic-Types/Arrays/#Array___mk "Documentation for Array.mk")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.toByteArray "Permalink")def
```


List.toByteArray (bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


List.toByteArray (bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) :
  [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


```

Converts a list of bytes into a `[ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.toFloatArray "Permalink")def
```


List.toFloatArray (ds : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) : FloatArray


List.toFloatArray (ds : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")) :
  FloatArray


```

Converts a list of floats into a `FloatArray`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.toString "Permalink")def
```


List.toString.{u_1} {α : Type u_1} [ToString α] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


List.toString.{u_1} {α : Type u_1}
  [ToString α] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Converts a list into a string, using `ToString.toString` to convert its elements.
The resulting string resembles list literal syntax, with the elements separated by `", "` and enclosed in square brackets.
The resulting string may not be valid Lean syntax, because there's no such expectation for `ToString` instances.
Examples:
  * `[1, 2, 3].[toString](Basic-Types/Linked-Lists/#List___toString "Documentation for List.toString") = "[1, 2, 3]"`
  * `["cat", "dog"].[toString](Basic-Types/Linked-Lists/#List___toString "Documentation for List.toString") = "[cat, dog]"`
  * `["cat", "dog", ""].[toString](Basic-Types/Linked-Lists/#List___toString "Documentation for List.toString") = "[cat, dog, ]"`


###  20.15.3.8. Modification[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Linked-Lists--API-Reference--Modification "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.set "Permalink")def
```


List.set.{u_1} {α : Type u_1} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.set.{u_1} {α : Type u_1} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Replaces the value at (zero-based) index `n` in `l` with `a`. If the index is out of bounds, then the list is returned unmodified.
Examples:
  * `["water", "coffee", "soda", "juice"].[set](Basic-Types/Linked-Lists/#List___set "Documentation for List.set") 1 "tea" = ["water", "tea", "soda", "juice"]`
  * `["water", "coffee", "soda", "juice"].[set](Basic-Types/Linked-Lists/#List___set "Documentation for List.set") 4 "tea" = ["water", "coffee", "soda", "juice"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.setTR "Permalink")def
```


List.setTR.{u_1} {α : Type u_1} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.setTR.{u_1} {α : Type u_1}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Replaces the value at (zero-based) index `n` in `l` with `a`. If the index is out of bounds, then the list is returned unmodified.
This is a tail-recursive version of `[List.set](Basic-Types/Linked-Lists/#List___set "Documentation for List.set")` that's used at runtime.
Examples:
  * `["water", "coffee", "soda", "juice"].[set](Basic-Types/Linked-Lists/#List___set "Documentation for List.set") 1 "tea" = ["water", "tea", "soda", "juice"]`
  * `["water", "coffee", "soda", "juice"].[set](Basic-Types/Linked-Lists/#List___set "Documentation for List.set") 4 "tea" = ["water", "coffee", "soda", "juice"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.modify "Permalink")def
```


List.modify.{u} {α : Type u} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : α → α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.modify.{u} {α : Type u} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : α → α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Replaces the element at the given index, if it exists, with the result of applying `f` to it. If the index is invalid, the list is returned unmodified.
Examples:
  * `[1, 2, 3].[modify](Basic-Types/Linked-Lists/#List___modify "Documentation for List.modify") 0 (· * 10) = [10, 2, 3]`
  * `[1, 2, 3].[modify](Basic-Types/Linked-Lists/#List___modify "Documentation for List.modify") 2 (· * 10) = [1, 2, 30]`
  * `[1, 2, 3].[modify](Basic-Types/Linked-Lists/#List___modify "Documentation for List.modify") 3 (· * 10) = [1, 2, 3]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.modifyTR "Permalink")def
```


List.modifyTR.{u_1} {α : Type u_1} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : α → α) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.modifyTR.{u_1} {α : Type u_1}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : α → α) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Replaces the element at the given index, if it exists, with the result of applying `f` to it.
This is a tail-recursive version of `[List.modify](Basic-Types/Linked-Lists/#List___modify "Documentation for List.modify")`.
Examples:
  * `[1, 2, 3].[modifyTR](Basic-Types/Linked-Lists/#List___modifyTR "Documentation for List.modifyTR") 0 (· * 10) = [10, 2, 3]`
  * `[1, 2, 3].[modifyTR](Basic-Types/Linked-Lists/#List___modifyTR "Documentation for List.modifyTR") 2 (· * 10) = [1, 2, 30]`
  * `[1, 2, 3].[modifyTR](Basic-Types/Linked-Lists/#List___modifyTR "Documentation for List.modifyTR") 3 (· * 10) = [1, 2, 3]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.modifyHead "Permalink")def
```


List.modifyHead.{u} {α : Type u} (f : α → α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.modifyHead.{u} {α : Type u}
  (f : α → α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Replace the head of the list with the result of applying `f` to it. Returns the empty list if the list is empty.
Examples:
  * `[1, 2, 3].[modifyHead](Basic-Types/Linked-Lists/#List___modifyHead "Documentation for List.modifyHead") (· * 10) = [10, 2, 3]`
  * `[].[modifyHead](Basic-Types/Linked-Lists/#List___modifyHead "Documentation for List.modifyHead") (· * 10) = []`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.modifyTailIdx "Permalink")def
```


List.modifyTailIdx.{u} {α : Type u} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.modifyTailIdx.{u} {α : Type u}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (f : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Replaces the `n`th tail of `l` with the result of applying `f` to it. Returns the input without using `f` if the index is larger than the length of the List.
Examples:
`["circle", "square", "triangle"].[modifyTailIdx](Basic-Types/Linked-Lists/#List___modifyTailIdx "Documentation for List.modifyTailIdx") 1 [List.reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse")``["circle", "triangle", "square"]``["circle", "square", "triangle"].[modifyTailIdx](Basic-Types/Linked-Lists/#List___modifyTailIdx "Documentation for List.modifyTailIdx") 1 (fun xs => xs ++ xs)``["circle", "square", "triangle", "square", "triangle"]``["circle", "square", "triangle"].[modifyTailIdx](Basic-Types/Linked-Lists/#List___modifyTailIdx "Documentation for List.modifyTailIdx") 2 (fun xs => xs ++ xs)``["circle", "square", "triangle", "triangle"]``["circle", "square", "triangle"].[modifyTailIdx](Basic-Types/Linked-Lists/#List___modifyTailIdx "Documentation for List.modifyTailIdx") 5 (fun xs => xs ++ xs)``["circle", "square", "triangle"]`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.erase "Permalink")def
```


List.erase.{u_1} {α : Type u_1} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.erase.{u_1} {α : Type u_1} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Removes the first occurrence of `a` from `l`. If `a` does not occur in `l`, the list is returned unmodified.
`O(|l|)`.
Examples:
  * `[1, 5, 3, 2, 5].[erase](Basic-Types/Linked-Lists/#List___erase "Documentation for List.erase") 5 = [1, 3, 2, 5]`
  * `[1, 5, 3, 2, 5].[erase](Basic-Types/Linked-Lists/#List___erase "Documentation for List.erase") 6 = [1, 5, 3, 2, 5]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.eraseTR "Permalink")def
```


List.eraseTR.{u_1} {α : Type u_1} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.eraseTR.{u_1} {α : Type u_1} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Removes the first occurrence of `a` from `l`. If `a` does not occur in `l`, the list is returned unmodified.
`O(|l|)`.
This is a tail-recursive version of `[List.erase](Basic-Types/Linked-Lists/#List___erase "Documentation for List.erase")`, used in runtime code.
Examples:
  * `[1, 5, 3, 2, 5].[eraseTR](Basic-Types/Linked-Lists/#List___eraseTR "Documentation for List.eraseTR") 5 = [1, 3, 2, 5]`
  * `[1, 5, 3, 2, 5].[eraseTR](Basic-Types/Linked-Lists/#List___eraseTR "Documentation for List.eraseTR") 6 = [1, 5, 3, 2, 5]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.eraseDups "Permalink")def
```


List.eraseDups.{u_1} {α : Type u_1} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.eraseDups.{u_1} {α : Type u_1}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Erases duplicated elements in the list, keeping the first occurrence of duplicated elements.
`O(|l|^2)`.
Examples:
  * `[1, 3, 2, 2, 3, 5].[eraseDups](Basic-Types/Linked-Lists/#List___eraseDups "Documentation for List.eraseDups") = [1, 3, 2, 5]`
  * `["red", "green", "green", "blue"].[eraseDups](Basic-Types/Linked-Lists/#List___eraseDups "Documentation for List.eraseDups") = ["red", "green", "blue"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.eraseIdx "Permalink")def
```


List.eraseIdx.{u} {α : Type u} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.eraseIdx.{u} {α : Type u}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Removes the element at the specified index. If the index is out of bounds, the list is returned unmodified.
`O(i)`.
Examples:
  * `[0, 1, 2, 3, 4].[eraseIdx](Basic-Types/Linked-Lists/#List___eraseIdx "Documentation for List.eraseIdx") 0 = [1, 2, 3, 4]`
  * `[0, 1, 2, 3, 4].[eraseIdx](Basic-Types/Linked-Lists/#List___eraseIdx "Documentation for List.eraseIdx") 1 = [0, 2, 3, 4]`
  * `[0, 1, 2, 3, 4].[eraseIdx](Basic-Types/Linked-Lists/#List___eraseIdx "Documentation for List.eraseIdx") 5 = [0, 1, 2, 3, 4]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.eraseIdxTR "Permalink")def
```


List.eraseIdxTR.{u_1} {α : Type u_1} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.eraseIdxTR.{u_1} {α : Type u_1}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Removes the element at the specified index. If the index is out of bounds, the list is returned unmodified.
`O(i)`.
This is a tail-recursive version of `[List.eraseIdx](Basic-Types/Linked-Lists/#List___eraseIdx "Documentation for List.eraseIdx")`, used at runtime.
Examples:
  * `[0, 1, 2, 3, 4].[eraseIdxTR](Basic-Types/Linked-Lists/#List___eraseIdxTR "Documentation for List.eraseIdxTR") 0 = [1, 2, 3, 4]`
  * `[0, 1, 2, 3, 4].[eraseIdxTR](Basic-Types/Linked-Lists/#List___eraseIdxTR "Documentation for List.eraseIdxTR") 1 = [0, 2, 3, 4]`
  * `[0, 1, 2, 3, 4].[eraseIdxTR](Basic-Types/Linked-Lists/#List___eraseIdxTR "Documentation for List.eraseIdxTR") 5 = [0, 1, 2, 3, 4]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.eraseP "Permalink")def
```


List.eraseP.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.eraseP.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Removes the first element of a list for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`. If no element satisfies `p`, then the list is returned unchanged.
Examples:
  * `[2, 1, 2, 1, 3, 4].[eraseP](Basic-Types/Linked-Lists/#List___eraseP "Documentation for List.eraseP") (· < 2) = [2, 2, 1, 3, 4]`
  * `[2, 1, 2, 1, 3, 4].[eraseP](Basic-Types/Linked-Lists/#List___eraseP "Documentation for List.eraseP") (· > 2) = [2, 1, 2, 1, 4]`
  * `[2, 1, 2, 1, 3, 4].[eraseP](Basic-Types/Linked-Lists/#List___eraseP "Documentation for List.eraseP") (· > 8) = [2, 1, 2, 1, 3, 4]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.erasePTR "Permalink")def
```


List.erasePTR.{u_1} {α : Type u_1} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.erasePTR.{u_1} {α : Type u_1}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Removes the first element of a list for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`. If no element satisfies `p`, then the list is returned unchanged.
This is a tail-recursive version of `eraseP`, used at runtime.
Examples:
  * `[2, 1, 2, 1, 3, 4].[erasePTR](Basic-Types/Linked-Lists/#List___erasePTR "Documentation for List.erasePTR") (· < 2) = [2, 2, 1, 3, 4]`
  * `[2, 1, 2, 1, 3, 4].[erasePTR](Basic-Types/Linked-Lists/#List___erasePTR "Documentation for List.erasePTR") (· > 2) = [2, 1, 2, 1, 4]`
  * `[2, 1, 2, 1, 3, 4].[erasePTR](Basic-Types/Linked-Lists/#List___erasePTR "Documentation for List.erasePTR") (· > 8) = [2, 1, 2, 1, 3, 4]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.eraseReps "Permalink")def
```


List.eraseReps.{u_1} {α : Type u_1} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.eraseReps.{u_1} {α : Type u_1}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Erases repeated elements, keeping the first element of each run.
`O(|l|)`.
Example:
  * `[1, 3, 2, 2, 2, 3, 3, 5].[eraseReps](Basic-Types/Linked-Lists/#List___eraseReps "Documentation for List.eraseReps") = [1, 3, 2, 3, 5]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.extract "Permalink")def
```


List.extract.{u} {α : Type u} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := l.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.extract.{u} {α : Type u} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := l.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Returns the slice of `l` from indices `start` (inclusive) to `stop` (exclusive).
Examples:
  * [0, 1, 2, 3, 4, 5].extract 1 2 = [1]
  * [0, 1, 2, 3, 4, 5].extract 2 2 = []
  * [0, 1, 2, 3, 4, 5].extract 2 4 = [2, 3]
  * [0, 1, 2, 3, 4, 5].extract 2 = [2, 3, 4, 5]
  * [0, 1, 2, 3, 4, 5].extract (stop := 2) = [0, 1]


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.removeAll "Permalink")def
```


List.removeAll.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (xs ys : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.removeAll.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (xs ys : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Removes all elements of `xs` that are present in `ys`.
`O(|xs| * |ys|)`.
Examples:
  * `[1, 1, 5, 1, 2, 4, 5].[removeAll](Basic-Types/Linked-Lists/#List___removeAll "Documentation for List.removeAll") [1, 2, 2] = [5, 4, 5]`
  * `[1, 2, 3, 2].[removeAll](Basic-Types/Linked-Lists/#List___removeAll "Documentation for List.removeAll") [] = [1, 2, 3, 2]`
  * `[1, 2, 3, 2].[removeAll](Basic-Types/Linked-Lists/#List___removeAll "Documentation for List.removeAll") [3] = [1, 2, 2]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.replace "Permalink")def
```


List.replace.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (a b : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.replace.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (a b : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Replaces the first element of the list `l` that is equal to `a` with `b`. If no element is equal to `a`, then the list is returned unchanged.
`O(|l|)`.
Examples:
  * `[1, 4, 2, 3, 3, 7].[replace](Basic-Types/Linked-Lists/#List___replace "Documentation for List.replace") 3 6 = [1, 4, 2, 6, 3, 7]`
  * `[1, 4, 2, 3, 3, 7].[replace](Basic-Types/Linked-Lists/#List___replace "Documentation for List.replace") 5 6 = [1, 4, 2, 3, 3, 7]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.replaceTR "Permalink")def
```


List.replaceTR.{u_1} {α : Type u_1} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (b c : α) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.replaceTR.{u_1} {α : Type u_1}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (b c : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Replaces the first element of the list `l` that is equal to `a` with `b`. If no element is equal to `a`, then the list is returned unchanged.
`O(|l|)`. This is a tail-recursive version of `[List.replace](Basic-Types/Linked-Lists/#List___replace "Documentation for List.replace")` that's used in runtime code.
Examples:
  * `[1, 4, 2, 3, 3, 7].[replaceTR](Basic-Types/Linked-Lists/#List___replaceTR "Documentation for List.replaceTR") 3 6 = [1, 4, 2, 6, 3, 7]`
  * `[1, 4, 2, 3, 3, 7].[replaceTR](Basic-Types/Linked-Lists/#List___replaceTR "Documentation for List.replaceTR") 5 6 = [1, 4, 2, 3, 3, 7]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.reverse "Permalink")def
```


List.reverse.{u} {α : Type u} (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.reverse.{u} {α : Type u}
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Reverses a list.
`O(|as|)`.
Because of the “functional but in place” optimization implemented by Lean's compiler, this function does not allocate a new list when its reference to the input list is unshared: it simply walks the linked list and reverses all the node pointers.
Examples:
  * `[1, 2, 3, 4].[reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse") = [4, 3, 2, 1]`
  * `[].[reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse") = []`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.flatten "Permalink")def
```


List.flatten.{u_1} {α : Type u_1} : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.flatten.{u_1} {α : Type u_1} :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Concatenates a list of lists into a single list, preserving the order of the elements.
`O(|flatten L|)`.
Examples:
  * `[["a"], ["b", "c"]].[flatten](Basic-Types/Linked-Lists/#List___flatten "Documentation for List.flatten") = ["a", "b", "c"]`
  * `[["a"], [], ["b", "c"], ["d", "e", "f"]].[flatten](Basic-Types/Linked-Lists/#List___flatten "Documentation for List.flatten") = ["a", "b", "c", "d", "e", "f"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.flattenTR "Permalink")def
```


List.flattenTR.{u_1} {α : Type u_1} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.flattenTR.{u_1} {α : Type u_1}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Concatenates a list of lists into a single list, preserving the order of the elements.
`O(|flatten L|)`. This is a tail-recursive version of `[List.flatten](Basic-Types/Linked-Lists/#List___flatten "Documentation for List.flatten")`, used in runtime code.
Examples:
  * `[["a"], ["b", "c"]].[flattenTR](Basic-Types/Linked-Lists/#List___flattenTR "Documentation for List.flattenTR") = ["a", "b", "c"]`
  * `[["a"], [], ["b", "c"], ["d", "e", "f"]].[flattenTR](Basic-Types/Linked-Lists/#List___flattenTR "Documentation for List.flattenTR") = ["a", "b", "c", "d", "e", "f"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.rotateLeft "Permalink")def
```


List.rotateLeft.{u} {α : Type u} (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 1) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.rotateLeft.{u} {α : Type u}
  (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 1) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Rotates the elements of `xs` to the left, moving `i % xs.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")` elements from the start of the list to the end.
`O(|xs|)`.
Examples:
  * `[1, 2, 3, 4, 5].[rotateLeft](Basic-Types/Linked-Lists/#List___rotateLeft "Documentation for List.rotateLeft") 3 = [4, 5, 1, 2, 3]`
  * `[1, 2, 3, 4, 5].[rotateLeft](Basic-Types/Linked-Lists/#List___rotateLeft "Documentation for List.rotateLeft") 5 = [1, 2, 3, 4, 5]`
  * `[1, 2, 3, 4, 5].[rotateLeft](Basic-Types/Linked-Lists/#List___rotateLeft "Documentation for List.rotateLeft") 1 = [2, 3, 4, 5, 1]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.rotateRight "Permalink")def
```


List.rotateRight.{u} {α : Type u} (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 1) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.rotateRight.{u} {α : Type u}
  (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 1) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Rotates the elements of `xs` to the right, moving `i % xs.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")` elements from the end of the list to the start.
After rotation, the element at `xs[n]` is at index `(i + n) % l.length`. `O(|xs|)`.
Examples:
  * `[1, 2, 3, 4, 5].[rotateRight](Basic-Types/Linked-Lists/#List___rotateRight "Documentation for List.rotateRight") 3 = [3, 4, 5, 1, 2]`
  * `[1, 2, 3, 4, 5].[rotateRight](Basic-Types/Linked-Lists/#List___rotateRight "Documentation for List.rotateRight") 5 = [1, 2, 3, 4, 5]`
  * `[1, 2, 3, 4, 5].[rotateRight](Basic-Types/Linked-Lists/#List___rotateRight "Documentation for List.rotateRight") 1 = [5, 1, 2, 3, 4]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.leftpad "Permalink")def
```


List.leftpad.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.leftpad.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (a : α) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Pads `l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` on the left with repeated occurrences of `a : α` until it is of length `n`. If `l` already has at least `n` elements, it is returned unmodified.
Examples:
  * `[1, 2, 3].[leftpad](Basic-Types/Linked-Lists/#List___leftpad "Documentation for List.leftpad") 5 0 = [0, 0, 1, 2, 3]`
  * `["red", "green", "blue"].[leftpad](Basic-Types/Linked-Lists/#List___leftpad "Documentation for List.leftpad") 4 "blank" = ["blank", "red", "green", "blue"]`
  * `["red", "green", "blue"].[leftpad](Basic-Types/Linked-Lists/#List___leftpad "Documentation for List.leftpad") 3 "blank" = ["red", "green", "blue"]`
  * `["red", "green", "blue"].[leftpad](Basic-Types/Linked-Lists/#List___leftpad "Documentation for List.leftpad") 1 "blank" = ["red", "green", "blue"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.leftpadTR "Permalink")def
```


List.leftpadTR.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.leftpadTR.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (a : α) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Pads `l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` on the left with repeated occurrences of `a : α` until it is of length `n`. If `l` already has at least `n` elements, it is returned unmodified.
This is a tail-recursive version of `[List.leftpad](Basic-Types/Linked-Lists/#List___leftpad "Documentation for List.leftpad")`, used at runtime.
Examples:
  * `[1, 2, 3].leftPadTR 5 0 = [0, 0, 1, 2, 3]`
  * `["red", "green", "blue"].leftPadTR 4 "blank" = ["blank", "red", "green", "blue"]`
  * `["red", "green", "blue"].leftPadTR 3 "blank" = ["red", "green", "blue"]`
  * `["red", "green", "blue"].leftPadTR 1 "blank" = ["red", "green", "blue"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.rightpad "Permalink")def
```


List.rightpad.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.rightpad.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (a : α) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Pads `l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` on the right with repeated occurrences of `a : α` until it is of length `n`. If `l` already has at least `n` elements, it is returned unmodified.
Examples:
  * `[1, 2, 3].[rightpad](Basic-Types/Linked-Lists/#List___rightpad "Documentation for List.rightpad") 5 0 = [1, 2, 3, 0, 0]`
  * `["red", "green", "blue"].[rightpad](Basic-Types/Linked-Lists/#List___rightpad "Documentation for List.rightpad") 4 "blank" = ["red", "green", "blue", "blank"]`
  * `["red", "green", "blue"].[rightpad](Basic-Types/Linked-Lists/#List___rightpad "Documentation for List.rightpad") 3 "blank" = ["red", "green", "blue"]`
  * `["red", "green", "blue"].[rightpad](Basic-Types/Linked-Lists/#List___rightpad "Documentation for List.rightpad") 1 "blank" = ["red", "green", "blue"]`


####  20.15.3.8.1. Insertion[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Linked-Lists--API-Reference--Modification--Insertion "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.insert "Permalink")def
```


List.insert.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (a : α) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.insert.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (a : α) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Inserts an element into a list without duplication.
If the element is present in the list, the list is returned unmodified. Otherwise, the new element is inserted at the head of the list.
Examples:
  * `[1, 2, 3].[insert](Basic-Types/Linked-Lists/#List___insert "Documentation for List.insert") 0 = [0, 1, 2, 3]`
  * `[1, 2, 3].[insert](Basic-Types/Linked-Lists/#List___insert "Documentation for List.insert") 4 = [4, 1, 2, 3]`
  * `[1, 2, 3].[insert](Basic-Types/Linked-Lists/#List___insert "Documentation for List.insert") 2 = [1, 2, 3]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.insertIdx "Permalink")def
```


List.insertIdx.{u} {α : Type u} (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.insertIdx.{u} {α : Type u}
  (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Inserts an element into a list at the specified index. If the index is greater than the length of the list, then the list is returned unmodified.
In other words, the new element is inserted into the list `l` after the first `i` elements of `l`.
Examples:
  * `["tues", "thur", "sat"].[insertIdx](Basic-Types/Linked-Lists/#List___insertIdx "Documentation for List.insertIdx") 1 "wed" = ["tues", "wed", "thur", "sat"]`
  * `["tues", "thur", "sat"].[insertIdx](Basic-Types/Linked-Lists/#List___insertIdx "Documentation for List.insertIdx") 2 "wed" = ["tues", "thur", "wed", "sat"]`
  * `["tues", "thur", "sat"].[insertIdx](Basic-Types/Linked-Lists/#List___insertIdx "Documentation for List.insertIdx") 3 "wed" = ["tues", "thur", "sat", "wed"]`
  * `["tues", "thur", "sat"].[insertIdx](Basic-Types/Linked-Lists/#List___insertIdx "Documentation for List.insertIdx") 4 "wed" = ["tues", "thur", "sat"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.insertIdxTR "Permalink")def
```


List.insertIdxTR.{u_1} {α : Type u_1} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.insertIdxTR.{u_1} {α : Type u_1}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Inserts an element into a list at the specified index. If the index is greater than the length of the list, then the list is returned unmodified.
In other words, the new element is inserted into the list `l` after the first `i` elements of `l`.
This is a tail-recursive version of `[List.insertIdx](Basic-Types/Linked-Lists/#List___insertIdx "Documentation for List.insertIdx")`, used at runtime.
Examples:
  * `["tues", "thur", "sat"].[insertIdxTR](Basic-Types/Linked-Lists/#List___insertIdxTR "Documentation for List.insertIdxTR") 1 "wed" = ["tues", "wed", "thur", "sat"]`
  * `["tues", "thur", "sat"].[insertIdxTR](Basic-Types/Linked-Lists/#List___insertIdxTR "Documentation for List.insertIdxTR") 2 "wed" = ["tues", "thur", "wed", "sat"]`
  * `["tues", "thur", "sat"].[insertIdxTR](Basic-Types/Linked-Lists/#List___insertIdxTR "Documentation for List.insertIdxTR") 3 "wed" = ["tues", "thur", "sat", "wed"]`
  * `["tues", "thur", "sat"].[insertIdxTR](Basic-Types/Linked-Lists/#List___insertIdxTR "Documentation for List.insertIdxTR") 4 "wed" = ["tues", "thur", "sat"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.intersperse "Permalink")def
```


List.intersperse.{u} {α : Type u} (sep : α) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.intersperse.{u} {α : Type u}
  (sep : α) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Alternates the elements of `l` with `sep`.
`O(|l|)`.
`[List.intercalate](Basic-Types/Linked-Lists/#List___intercalate "Documentation for List.intercalate")` is a similar function that alternates a separator list with elements of a list of lists.
Examples:
  * `[List.intersperse](Basic-Types/Linked-Lists/#List___intersperse "Documentation for List.intersperse") "then" [] = []`
  * `[List.intersperse](Basic-Types/Linked-Lists/#List___intersperse "Documentation for List.intersperse") "then" ["walk"] = ["walk"]`
  * `[List.intersperse](Basic-Types/Linked-Lists/#List___intersperse "Documentation for List.intersperse") "then" ["walk", "run"] = ["walk", "then", "run"]`
  * `[List.intersperse](Basic-Types/Linked-Lists/#List___intersperse "Documentation for List.intersperse") "then" ["walk", "run", "rest"] = ["walk", "then", "run", "then", "rest"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.intersperseTR "Permalink")def
```


List.intersperseTR.{u} {α : Type u} (sep : α) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.intersperseTR.{u} {α : Type u}
  (sep : α) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Alternates the elements of `l` with `sep`.
`O(|l|)`.
This is a tail-recursive version of `[List.intersperse](Basic-Types/Linked-Lists/#List___intersperse "Documentation for List.intersperse")`, used at runtime.
Examples:
  * `[List.intersperseTR](Basic-Types/Linked-Lists/#List___intersperseTR "Documentation for List.intersperseTR") "then" [] = []`
  * `[List.intersperseTR](Basic-Types/Linked-Lists/#List___intersperseTR "Documentation for List.intersperseTR") "then" ["walk"] = ["walk"]`
  * `[List.intersperseTR](Basic-Types/Linked-Lists/#List___intersperseTR "Documentation for List.intersperseTR") "then" ["walk", "run"] = ["walk", "then", "run"]`
  * `[List.intersperseTR](Basic-Types/Linked-Lists/#List___intersperseTR "Documentation for List.intersperseTR") "then" ["walk", "run", "rest"] = ["walk", "then", "run", "then", "rest"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.intercalate "Permalink")def
```


List.intercalate.{u} {α : Type u} (sep : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.intercalate.{u} {α : Type u}
  (sep : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Alternates the lists in `xs` with the separator `sep`, appending them. The resulting list is flattened.
`O(|xs|)`.
`[List.intersperse](Basic-Types/Linked-Lists/#List___intersperse "Documentation for List.intersperse")` is a similar function that alternates a separator element with the elements of a list.
Examples:
  * `[List.intercalate](Basic-Types/Linked-Lists/#List___intercalate "Documentation for List.intercalate") sep [] = []`
  * `[List.intercalate](Basic-Types/Linked-Lists/#List___intercalate "Documentation for List.intercalate") sep [a] = a`
  * `[List.intercalate](Basic-Types/Linked-Lists/#List___intercalate "Documentation for List.intercalate") sep [a, b] = a ++ sep ++ b`
  * `[List.intercalate](Basic-Types/Linked-Lists/#List___intercalate "Documentation for List.intercalate") sep [a, b, c] = a ++ sep ++ b ++ sep ++ c`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.intercalateTR "Permalink")def
```


List.intercalateTR.{u_1} {α : Type u_1} (sep : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.intercalateTR.{u_1} {α : Type u_1}
  (sep : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Alternates the lists in `xs` with the separator `sep`.
This is a tail-recursive version of `[List.intercalate](Basic-Types/Linked-Lists/#List___intercalate "Documentation for List.intercalate")` used at runtime.
Examples:
  * `[List.intercalateTR](Basic-Types/Linked-Lists/#List___intercalateTR "Documentation for List.intercalateTR") sep [] = []`
  * `[List.intercalateTR](Basic-Types/Linked-Lists/#List___intercalateTR "Documentation for List.intercalateTR") sep [a] = a`
  * `[List.intercalateTR](Basic-Types/Linked-Lists/#List___intercalateTR "Documentation for List.intercalateTR") sep [a, b] = a ++ sep ++ b`
  * `[List.intercalateTR](Basic-Types/Linked-Lists/#List___intercalateTR "Documentation for List.intercalateTR") sep [a, b, c] = a ++ sep ++ b ++ sep ++ c`


###  20.15.3.9. Sorting[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Linked-Lists--API-Reference--Sorting "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.mergeSort "Permalink")def
```


List.mergeSort.{u_1} {α : Type u_1} (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (le : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := by exact fun a b => a ≤ b) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.mergeSort.{u_1} {α : Type u_1}
  (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (le : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := by
    exact fun a b => a ≤ b) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

A stable merge sort.
This function is a simplified implementation that's designed to be easy to reason about, rather than for efficiency. In particular, it uses the non-tail-recursive `[List.merge](Basic-Types/Linked-Lists/#List___merge "Documentation for List.merge")` function and traverses lists unnecessarily.
It is replaced at runtime by an efficient implementation that has been proven to be equivalent.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.merge "Permalink")def
```


List.merge.{u_1} {α : Type u_1} (xs ys : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (le : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := by exact fun a b => a ≤ b) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.merge.{u_1} {α : Type u_1}
  (xs ys : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (le : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := by
    exact fun a b => a ≤ b) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Merges two lists, using `le` to select the first element of the resulting list if both are non-empty.
If both input lists are sorted according to `le`, then the resulting list is also sorted according to `le`. `O(|xs| + |ys|)`.
This implementation is not tail-recursive, but it is replaced at runtime by a proven-equivalent tail-recursive merge.
###  20.15.3.10. Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Linked-Lists--API-Reference--Iteration "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.iter "Permalink")def
```


List.iter.{w} {α : Type w} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") α


List.iter.{w} {α : Type w} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") α


```

Returns a finite iterator for the given list. The iterator yields the elements of the list in order and then terminates.
The monadic version of this iterator is `[List.iterM](Basic-Types/Linked-Lists/#List___iterM "Documentation for List.iterM")`.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.iterM "Permalink")def
```


List.iterM.{w, w'} {α : Type w} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (m : Type w → Type w')
  [[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") m] : [Std.IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m α


List.iterM.{w, w'} {α : Type w}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (m : Type w → Type w')
  [[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") m] : [Std.IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m α


```

Returns a finite iterator for the given list. The iterator yields the elements of the list in order and then terminates.
The non-monadic version of this iterator is `[List.iter](Basic-Types/Linked-Lists/#List___iter "Documentation for List.iter")`.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.forA "Permalink")def
```


List.forA.{u, v, w} {m : Type u → Type v} [[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m] {α : Type w}
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (f : α → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


List.forA.{u, v, w} {m : Type u → Type v}
  [[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m] {α : Type w}
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (f : α → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) :
  m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Applies the applicative action `f` to every element in the list, in order.
If `m` is also a `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")`, then using `[List.forM](Basic-Types/Linked-Lists/#List___forM "Documentation for List.forM")` can be more efficient.
`[List.mapA](Basic-Types/Linked-Lists/#List___mapA "Documentation for List.mapA")` is a variant that collects results.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.forM "Permalink")def
```


List.forM.{u, v, w} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type w}
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (f : α → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


List.forM.{u, v, w} {m : Type u → Type v}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type w} (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (f : α → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Applies the monadic action `f` to every element in the list, in order.
`[List.mapM](Basic-Types/Linked-Lists/#List___mapM "Documentation for List.mapM")` is a variant that collects results. `[List.forA](Basic-Types/Linked-Lists/#List___forA "Documentation for List.forA")` is a variant that works on any `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.firstM "Permalink")def
```


List.firstM.{u, v, w} {m : Type u → Type v} [[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative") m] {α : Type w}
  {β : Type u} (f : α → m β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → m β


List.firstM.{u, v, w}
  {m : Type u → Type v} [[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative") m]
  {α : Type w} {β : Type u}
  (f : α → m β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → m β


```

Maps `f` over the list and collects the results with `<|>`. The result for the end of the list is `failure`.
Examples:
  * `[[], [1, 2], [], [2]].[firstM](Basic-Types/Linked-Lists/#List___firstM "Documentation for List.firstM") [List.head?](Basic-Types/Linked-Lists/#List___head___ "Documentation for List.head?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 1`
  * `[[], [], []].[firstM](Basic-Types/Linked-Lists/#List___firstM "Documentation for List.firstM") [List.head?](Basic-Types/Linked-Lists/#List___head___ "Documentation for List.head?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `[].[firstM](Basic-Types/Linked-Lists/#List___firstM "Documentation for List.firstM") [List.head?](Basic-Types/Linked-Lists/#List___head___ "Documentation for List.head?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.sum "Permalink")def
```


List.sum.{u_1} {α : Type u_1} [[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") α] [[Zero](Type-Classes/Basic-Classes/#Zero___mk "Documentation for Zero") α] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → α


List.sum.{u_1} {α : Type u_1} [[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") α]
  [[Zero](Type-Classes/Basic-Classes/#Zero___mk "Documentation for Zero") α] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → α


```

Computes the sum of the elements of a list.
Examples:
  * `[a, b, c].[sum](Basic-Types/Linked-Lists/#List___sum "Documentation for List.sum") = a + (b + (c + 0))`
  * `[1, 2, 5].[sum](Basic-Types/Linked-Lists/#List___sum "Documentation for List.sum") = 8`


####  20.15.3.10.1. Folds[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Linked-Lists--API-Reference--Iteration--Folds "Permalink")
Folds are operators that combine the elements of a list using a function. They come in two varieties, named after the nesting of the function calls: 

Left folds 
    
Left folds combine the elements from the head of the list towards the end. The head of the list is combined with the initial value, and the result of this operation is then combined with the next value, and so forth. 

Right folds 
    
Right folds combine the elements from the end of the list towards the start, as if each `[cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")` constructor were replaced by a call to the combining function and `[nil](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")` were replaced by the initial value.
Monadic folds, indicated with an `-M` suffix, allow the combining function to use effects in a [monad](Functors___-Monads-and--do--Notation/#--tech-term-Monad), which may include stopping the fold early.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.foldl "Permalink")def
```


List.foldl.{u, v} {α : Type u} {β : Type v} (f : α → β → α) (init : α) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β → α


List.foldl.{u, v} {α : Type u}
  {β : Type v} (f : α → β → α)
  (init : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β → α


```

Folds a function over a list from the left, accumulating a value starting with `init`. The accumulated value is combined with the each element of the list in order, using `f`.
Examples:
  * `[a, b, c].[foldl](Basic-Types/Linked-Lists/#List___foldl "Documentation for List.foldl") f z  = f (f (f z a) b) c`
  * `[1, 2, 3].[foldl](Basic-Types/Linked-Lists/#List___foldl "Documentation for List.foldl") (· ++ toString ·) "" = "123"`
  * `[1, 2, 3].[foldl](Basic-Types/Linked-Lists/#List___foldl "Documentation for List.foldl") (s!"({·} {·})") "" = "((( 1) 2) 3)"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.foldlM "Permalink")def
```


List.foldlM.{u, v, w} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {s : Type u}
  {α : Type w} (f : s → α → m s) (init : s) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → m s


List.foldlM.{u, v, w}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {s : Type u} {α : Type w}
  (f : s → α → m s) (init : s) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → m s


```

Folds a monadic function over a list from the left, accumulating a value starting with `init`. The accumulated value is combined with the each element of the list in order, using `f`.
Example:
`example [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → β → m α) :     [List.foldlM](Basic-Types/Linked-Lists/#List___foldlM "Documentation for List.foldlM") (m := m) f x₀ [a, b, c] = ([do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")       let x₁ ← f x₀ a       let x₂ ← f x₁ b       let x₃ ← f x₂ c       [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x₃)   := bym:Type u_1 → Type u_2α:Type u_1β:Type u_3x₀:αa:βb:βc:βinst✝:[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") mf:α → β → m α⊢ [List.foldlM](Basic-Types/Linked-Lists/#List___foldlM "Documentation for List.foldlM") f x₀ [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")a[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") b[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") c[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") do   let x₁ ← f x₀ a   let x₂ ← f x₁ b   let x₃ ← f x₂ c   [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x₃ [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 `
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.foldlRecOn "Permalink")def
```


List.foldlRecOn.{u_1, u_2, u_3} {β : Type u_1} {α : Type u_2}
  {motive : β → Sort u_3} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (op : β → α → β) {b : β} :
  motive b →
    ((b : β) → motive b → (a : α) → a ∈ l → motive (op b a)) →
      motive ([List.foldl](Basic-Types/Linked-Lists/#List___foldl "Documentation for List.foldl") op b l)


List.foldlRecOn.{u_1, u_2, u_3}
  {β : Type u_1} {α : Type u_2}
  {motive : β → Sort u_3} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (op : β → α → β) {b : β} :
  motive b →
    ((b : β) →
        motive b →
          (a : α) →
            a ∈ l → motive (op b a)) →
      motive ([List.foldl](Basic-Types/Linked-Lists/#List___foldl "Documentation for List.foldl") op b l)


```

A reasoning principle for proving propositions about the result of `[List.foldl](Basic-Types/Linked-Lists/#List___foldl "Documentation for List.foldl")` by establishing an invariant that is true for the initial data and preserved by the operation being folded.
Because the motive can return a type in any sort, this function may be used to construct data as well as to prove propositions.
Example:
`example {xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : xs.[foldl](Basic-Types/Linked-Lists/#List___foldl "Documentation for List.foldl") (· + ·) 1 > 0 := byxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [List.foldl](Basic-Types/Linked-Lists/#List___foldl "Documentation for List.foldl") (fun x1 x2 => x1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x2) 1 xs > 0   [apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") [List.foldlRecOn](Basic-Types/Linked-Lists/#List___foldlRecOn "Documentation for List.foldlRecOn")xxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 1xxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ ∀ (b : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b → ∀ (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), a ∈ xs → 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a   .xxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 1 [show](Tactic-Proofs/Tactic-Reference/#show "Documentation for tactic") 0 < 1xxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 1; [trivial](Tactic-Proofs/Tactic-Reference/#trivial "Documentation for tactic")All goals completed! 🐙   .xxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ ∀ (b : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b → ∀ (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), a ∈ xs → 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a [show](Tactic-Proofs/Tactic-Reference/#show "Documentation for tactic") ∀ (b : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), 0 < b → ∀ (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), a ∈ xs → 0 < b + axxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ ∀ (b : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b → ∀ (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), a ∈ xs → 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a     [intros](Tactic-Proofs/Tactic-Reference/#intros "Documentation for tactic")xxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")b✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝²:0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b✝a✝¹:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:a✝¹ ∈ xs⊢ 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") a✝¹; [omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic")All goals completed! 🐙 `
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.foldr "Permalink")def
```


List.foldr.{u, v} {α : Type u} {β : Type v} (f : α → β → β) (init : β)
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : β


List.foldr.{u, v} {α : Type u}
  {β : Type v} (f : α → β → β) (init : β)
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : β


```

Folds a function over a list from the right, accumulating a value starting with `init`. The accumulated value is combined with the each element of the list in reverse order, using `f`.
`O(|l|)`. Replaced at runtime with `[List.foldrTR](Basic-Types/Linked-Lists/#List___foldrTR "Documentation for List.foldrTR")`.
Examples:
  * `[a, b, c].[foldr](Basic-Types/Linked-Lists/#List___foldr "Documentation for List.foldr") f init  = f a (f b (f c init))`
  * `[1, 2, 3].[foldr](Basic-Types/Linked-Lists/#List___foldr "Documentation for List.foldr") (toString · ++ ·) "" = "123"`
  * `[1, 2, 3].[foldr](Basic-Types/Linked-Lists/#List___foldr "Documentation for List.foldr") (s!"({·} {·})") "!" = "(1 (2 (3 !)))"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.foldrM "Permalink")def
```


List.foldrM.{u, v, w} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {s : Type u}
  {α : Type w} (f : α → s → m s) (init : s) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : m s


List.foldrM.{u, v, w}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {s : Type u} {α : Type w}
  (f : α → s → m s) (init : s)
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : m s


```

Folds a monadic function over a list from the right, accumulating a value starting with `init`. The accumulated value is combined with the each element of the list in reverse order, using `f`.
Example:
`example [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → β → m β) :   [List.foldrM](Basic-Types/Linked-Lists/#List___foldrM "Documentation for List.foldrM") (m := m) f x₀ [a, b, c] = ([do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")     let x₁ ← f c x₀     let x₂ ← f b x₁     let x₃ ← f a x₂     [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x₃)   := bym:Type u_1 → Type u_2α:Type u_3β:Type u_1x₀:βa:αb:αc:αinst✝:[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") mf:α → β → m β⊢ [List.foldrM](Basic-Types/Linked-Lists/#List___foldrM "Documentation for List.foldrM") f x₀ [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")a[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") b[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") c[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") do   let x₁ ← f c x₀   let x₂ ← f b x₁   let x₃ ← f a x₂   [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x₃ [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 `
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.foldrRecOn "Permalink")def
```


List.foldrRecOn.{u_1, u_2, u_3} {β : Type u_1} {α : Type u_2}
  {motive : β → Sort u_3} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (op : α → β → β) {b : β} :
  motive b →
    ((b : β) → motive b → (a : α) → a ∈ l → motive (op a b)) →
      motive ([List.foldr](Basic-Types/Linked-Lists/#List___foldr "Documentation for List.foldr") op b l)


List.foldrRecOn.{u_1, u_2, u_3}
  {β : Type u_1} {α : Type u_2}
  {motive : β → Sort u_3} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (op : α → β → β) {b : β} :
  motive b →
    ((b : β) →
        motive b →
          (a : α) →
            a ∈ l → motive (op a b)) →
      motive ([List.foldr](Basic-Types/Linked-Lists/#List___foldr "Documentation for List.foldr") op b l)


```

A reasoning principle for proving propositions about the result of `[List.foldr](Basic-Types/Linked-Lists/#List___foldr "Documentation for List.foldr")` by establishing an invariant that is true for the initial data and preserved by the operation being folded.
Because the motive can return a type in any sort, this function may be used to construct data as well as to prove propositions.
Example:
`example {xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : xs.[foldr](Basic-Types/Linked-Lists/#List___foldr "Documentation for List.foldr") (· + ·) 1 > 0 := byxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [List.foldr](Basic-Types/Linked-Lists/#List___foldr "Documentation for List.foldr") (fun x1 x2 => x1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x2) 1 xs > 0   [apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") [List.foldrRecOn](Basic-Types/Linked-Lists/#List___foldrRecOn "Documentation for List.foldrRecOn")xxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 1xxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ ∀ (b : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b → ∀ (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), a ∈ xs → 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b   .xxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 1 [show](Tactic-Proofs/Tactic-Reference/#show "Documentation for tactic") 0 < 1xxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") 1; [trivial](Tactic-Proofs/Tactic-Reference/#trivial "Documentation for tactic")All goals completed! 🐙   .xxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ ∀ (b : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b → ∀ (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), a ∈ xs → 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b [show](Tactic-Proofs/Tactic-Reference/#show "Documentation for tactic") ∀ (b : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), 0 < b → ∀ (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), a ∈ xs → 0 < a + bxxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ ∀ (b : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b → ∀ (a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")), a ∈ xs → 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") a [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b     [intros](Tactic-Proofs/Tactic-Reference/#intros "Documentation for tactic")xxs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")b✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝²:0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") b✝a✝¹:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:a✝¹ ∈ xs⊢ 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") a✝¹ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") b✝; [omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic")All goals completed! 🐙 `
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.foldrTR "Permalink")def
```


List.foldrTR.{u_1, u_2} {α : Type u_1} {β : Type u_2} (f : α → β → β)
  (init : β) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : β


List.foldrTR.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} (f : α → β → β)
  (init : β) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : β


```

Folds a function over a list from the right, accumulating a value starting with `init`. The accumulated value is combined with the each element of the list in reverse order, using `f`.
`O(|l|)`. This is the tail-recursive replacement for `[List.foldr](Basic-Types/Linked-Lists/#List___foldr "Documentation for List.foldr")` in runtime code.
Examples:
  * `[a, b, c].[foldrTR](Basic-Types/Linked-Lists/#List___foldrTR "Documentation for List.foldrTR") f init  = f a (f b (f c init))`
  * `[1, 2, 3].[foldrTR](Basic-Types/Linked-Lists/#List___foldrTR "Documentation for List.foldrTR") (toString · ++ ·) "" = "123"`
  * `[1, 2, 3].[foldrTR](Basic-Types/Linked-Lists/#List___foldrTR "Documentation for List.foldrTR") (s!"({·} {·})") "!" = "(1 (2 (3 !)))"`


###  20.15.3.11. Transformation[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Linked-Lists--API-Reference--Transformation "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.map "Permalink")def
```


List.map.{u_1, u_2} {α : Type u_1} {β : Type u_2} (f : α → β)
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


List.map.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} (f : α → β)
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


```

Applies a function to each element of the list, returning the resulting list of values.
`O(|l|)`.
Examples:
  * `[a, b, c].[map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map") f = [f a, f b, f c]`
  * `[].[map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map") [Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") = []`
  * `["one", "two", "three"].[map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map") (·.[length](Basic-Types/Strings/#String___length "Documentation for String.length")) = [3, 3, 5]`
  * `["one", "two", "three"].[map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map") (·.reverse) = ["eno", "owt", "eerht"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.mapTR "Permalink")def
```


List.mapTR.{u, v} {α : Type u} {β : Type v} (f : α → β) (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


List.mapTR.{u, v} {α : Type u}
  {β : Type v} (f : α → β) (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


```

Applies a function to each element of the list, returning the resulting list of values.
`O(|l|)`. This is the tail-recursive variant of `[List.map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map")`, used in runtime code.
Examples:
  * `[a, b, c].[mapTR](Basic-Types/Linked-Lists/#List___mapTR "Documentation for List.mapTR") f = [f a, f b, f c]`
  * `[].[mapTR](Basic-Types/Linked-Lists/#List___mapTR "Documentation for List.mapTR") [Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") = []`
  * `["one", "two", "three"].[mapTR](Basic-Types/Linked-Lists/#List___mapTR "Documentation for List.mapTR") (·.[length](Basic-Types/Strings/#String___length "Documentation for String.length")) = [3, 3, 5]`
  * `["one", "two", "three"].[mapTR](Basic-Types/Linked-Lists/#List___mapTR "Documentation for List.mapTR") (·.reverse) = ["eno", "owt", "eerht"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.mapM "Permalink")def
```


List.mapM.{u, v, w} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type w}
  {β : Type u} (f : α → m β) (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


List.mapM.{u, v, w} {m : Type u → Type v}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type w} {β : Type u}
  (f : α → m β) (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


```

Applies the monadic action `f` to every element in the list, left-to-right, and returns the list of results.
This implementation is tail recursive. `[List.mapM'](Basic-Types/Linked-Lists/#List___mapM___ "Documentation for List.mapM'")` is a non-tail-recursive variant that may be more convenient to reason about. `[List.forM](Basic-Types/Linked-Lists/#List___forM "Documentation for List.forM")` is the variant that discards the results and `[List.mapA](Basic-Types/Linked-Lists/#List___mapA "Documentation for List.mapA")` is the variant that works with `[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.mapM' "Permalink")def
```


List.mapM'.{u_1, u_2, u_3} {m : Type u_1 → Type u_2} {α : Type u_3}
  {β : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → m β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


List.mapM'.{u_1, u_2, u_3}
  {m : Type u_1 → Type u_2} {α : Type u_3}
  {β : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → m β) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


```

Applies the monadic action `f` on every element in the list, left-to-right, and returns the list of results.
This is a non-tail-recursive variant of `[List.mapM](Basic-Types/Linked-Lists/#List___mapM "Documentation for List.mapM")` that's easier to reason about. It cannot be used as the main definition and replaced by the tail-recursive version because they can only be proved equal when `m` is a `[LawfulMonad](Functors___-Monads-and--do--Notation/Laws/#LawfulMonad___mk "Documentation for LawfulMonad")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.mapA "Permalink")def
```


List.mapA.{u, v, w} {m : Type u → Type v} [[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m] {α : Type w}
  {β : Type u} (f : α → m β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


List.mapA.{u, v, w} {m : Type u → Type v}
  [[Applicative](Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative") m] {α : Type w}
  {β : Type u} (f : α → m β) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


```

Applies the applicative action `f` on every element in the list, left-to-right, and returns the list of results.
If `m` is also a `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")`, then using `mapM` can be more efficient.
See `[List.forA](Basic-Types/Linked-Lists/#List___forA "Documentation for List.forA")` for the variant that discards the results. See `[List.mapM](Basic-Types/Linked-Lists/#List___mapM "Documentation for List.mapM")` for the variant that works with `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")`.
This function is not tail-recursive, so it may fail with a stack overflow on long lists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.mapFinIdx "Permalink")def
```


List.mapFinIdx.{u_1, u_2} {α : Type u_1} {β : Type u_2} (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → α → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") as.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") → β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


List.mapFinIdx.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (f :
    (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → α → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") as.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") → β) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


```

Applies a function to each element of the list along with the index at which that element is found, returning the list of results. In addition to the index, the function is also provided with a proof that the index is valid.
`[List.mapIdx](Basic-Types/Linked-Lists/#List___mapIdx "Documentation for List.mapIdx")` is a variant that does not provide the function with evidence that the index is valid.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.mapFinIdxM "Permalink")def
```


List.mapFinIdxM.{u_1, u_2, u_3} {m : Type u_1 → Type u_2} {α : Type u_3}
  {β : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → α → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") as.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") → m β) : m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


List.mapFinIdxM.{u_1, u_2, u_3}
  {m : Type u_1 → Type u_2} {α : Type u_3}
  {β : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (f :
    (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → α → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") as.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length") → m β) :
  m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


```

Applies a monadic function to each element of the list along with the index at which that element is found, returning the list of results. In addition to the index, the function is also provided with a proof that the index is valid.
`[List.mapIdxM](Basic-Types/Linked-Lists/#List___mapIdxM "Documentation for List.mapIdxM")` is a variant that does not provide the function with evidence that the index is valid.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.mapIdx "Permalink")def
```


List.mapIdx.{u_1, u_2} {α : Type u_1} {β : Type u_2} (f : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → α → β)
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


List.mapIdx.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} (f : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → α → β)
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


```

Applies a function to each element of the list along with the index at which that element is found, returning the list of results.
`[List.mapFinIdx](Basic-Types/Linked-Lists/#List___mapFinIdx "Documentation for List.mapFinIdx")` is a variant that additionally provides the function with a proof that the index is valid.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.mapIdxM "Permalink")def
```


List.mapIdxM.{u_1, u_2, u_3} {m : Type u_1 → Type u_2} {α : Type u_3}
  {β : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → α → m β) (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


List.mapIdxM.{u_1, u_2, u_3}
  {m : Type u_1 → Type u_2} {α : Type u_3}
  {β : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → α → m β) (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


```

Applies a monadic function to each element of the list along with the index at which that element is found, returning the list of results.
`[List.mapFinIdxM](Basic-Types/Linked-Lists/#List___mapFinIdxM "Documentation for List.mapFinIdxM")` is a variant that additionally provides the function with a proof that the index is valid.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.mapMono "Permalink")def
```


List.mapMono.{u_1} {α : Type u_1} (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (f : α → α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.mapMono.{u_1} {α : Type u_1}
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (f : α → α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Applies a function to each element of a list, returning the list of results. The function is monomorphic: it is required to return a value of the same type. The internal implementation uses pointer equality, and does not allocate a new list if the result of each function call is pointer-equal to its argument.
For verification purposes, `[List.mapMono](Basic-Types/Linked-Lists/#List___mapMono "Documentation for List.mapMono") = [List.map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.mapMonoM "Permalink")def
```


List.mapMonoM.{u_1, u_2} {m : Type u_1 → Type u_2} {α : Type u_1}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (f : α → m α) : m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)


List.mapMonoM.{u_1, u_2}
  {m : Type u_1 → Type u_2} {α : Type u_1}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (f : α → m α) :
  m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)


```

Applies a monadic function to each element of a list, returning the list of results. The function is monomorphic: it is required to return a value of the same type. The internal implementation uses pointer equality, and does not allocate a new list if the result of each function call is pointer-equal to its argument.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.flatMap "Permalink")def
```


List.flatMap.{u, v} {α : Type u} {β : Type v} (b : α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


List.flatMap.{u, v} {α : Type u}
  {β : Type v} (b : α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


```

Applies a function that returns a list to each element of a list, and concatenates the resulting lists.
Examples:
  * `[2, 3, 2].[flatMap](Basic-Types/Linked-Lists/#List___flatMap "Documentation for List.flatMap") [List.range](Basic-Types/Linked-Lists/#List___range "Documentation for List.range") = [0, 1, 0, 1, 2, 0, 1]`
  * `["red", "blue"].[flatMap](Basic-Types/Linked-Lists/#List___flatMap "Documentation for List.flatMap") String.toList = ['r', 'e', 'd', 'b', 'l', 'u', 'e']`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.flatMapTR "Permalink")def
```


List.flatMapTR.{u_1, u_2} {α : Type u_1} {β : Type u_2} (f : α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


List.flatMapTR.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} (f : α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


```

Applies a function that returns a list to each element of a list, and concatenates the resulting lists.
This is the tail-recursive version of `[List.flatMap](Basic-Types/Linked-Lists/#List___flatMap "Documentation for List.flatMap")` that's used at runtime.
Examples:
  * `[2, 3, 2].[flatMapTR](Basic-Types/Linked-Lists/#List___flatMapTR "Documentation for List.flatMapTR") [List.range](Basic-Types/Linked-Lists/#List___range "Documentation for List.range") = [0, 1, 0, 1, 2, 0, 1]`
  * `["red", "blue"].[flatMapTR](Basic-Types/Linked-Lists/#List___flatMapTR "Documentation for List.flatMapTR") String.toList = ['r', 'e', 'd', 'b', 'l', 'u', 'e']`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.flatMapM "Permalink")def
```


List.flatMapM.{u, v, w} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type w}
  {β : Type u} (f : α → m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)) (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


List.flatMapM.{u, v, w}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type w} {β : Type u}
  (f : α → m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)) (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


```

Applies a monadic function that returns a list to each element of a list, from left to right, and concatenates the resulting lists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.zip "Permalink")def
```


List.zip.{u, v} {α : Type u} {β : Type v} :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


List.zip.{u, v} {α : Type u}
  {β : Type v} :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Combines two lists into a list of pairs in which the first and second components are the corresponding elements of each list. The resulting list is the length of the shorter of the input lists.
`O(min |xs| |ys|)`.
Examples:
  * `["Mon", "Tue", "Wed"].[zip](Basic-Types/Linked-Lists/#List___zip "Documentation for List.zip") [1, 2, 3] = [("Mon", 1), ("Tue", 2), ("Wed", 3)]`
  * `["Mon", "Tue", "Wed"].[zip](Basic-Types/Linked-Lists/#List___zip "Documentation for List.zip") [1, 2] = [("Mon", 1), ("Tue", 2)]`
  * `[x₁, x₂, x₃].[zip](Basic-Types/Linked-Lists/#List___zip "Documentation for List.zip") [y₁, y₂, y₃, y₄] = [(x₁, y₁), (x₂, y₂), (x₃, y₃)]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.zipIdx "Permalink")def
```


List.zipIdx.{u} {α : Type u} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


List.zipIdx.{u} {α : Type u} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Pairs each element of a list with its index, optionally starting from an index other than `0`.
`O(|l|)`.
Examples:
  * `[a, b, c].[zipIdx](Basic-Types/Linked-Lists/#List___zipIdx "Documentation for List.zipIdx") = [(a, 0), (b, 1), (c, 2)]`
  * `[a, b, c].[zipIdx](Basic-Types/Linked-Lists/#List___zipIdx "Documentation for List.zipIdx") 5 = [(a, 5), (b, 6), (c, 7)]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.zipIdxTR "Permalink")def
```


List.zipIdxTR.{u_1} {α : Type u_1} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


List.zipIdxTR.{u_1} {α : Type u_1}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Pairs each element of a list with its index, optionally starting from an index other than `0`.
`O(|l|)`. This is a tail-recursive version of `[List.zipIdx](Basic-Types/Linked-Lists/#List___zipIdx "Documentation for List.zipIdx")` that's used at runtime.
Examples:
  * `[a, b, c].[zipIdxTR](Basic-Types/Linked-Lists/#List___zipIdxTR "Documentation for List.zipIdxTR") = [(a, 0), (b, 1), (c, 2)]`
  * `[a, b, c].[zipIdxTR](Basic-Types/Linked-Lists/#List___zipIdxTR "Documentation for List.zipIdxTR") 5 = [(a, 5), (b, 6), (c, 7)]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.zipWith "Permalink")def
```


List.zipWith.{u, v, w} {α : Type u} {β : Type v} {γ : Type w}
  (f : α → β → γ) (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (ys : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") γ


List.zipWith.{u, v, w} {α : Type u}
  {β : Type v} {γ : Type w}
  (f : α → β → γ) (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (ys : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") γ


```

Applies a function to the corresponding elements of two lists, stopping at the end of the shorter list.
`O(min |xs| |ys|)`.
Examples:
  * `[1, 2].[zipWith](Basic-Types/Linked-Lists/#List___zipWith "Documentation for List.zipWith") (· + ·) [5, 6] = [6, 8]`
  * `[1, 2, 3].[zipWith](Basic-Types/Linked-Lists/#List___zipWith "Documentation for List.zipWith") (· + ·) [5, 6, 10] = [6, 8, 13]`
  * `[].[zipWith](Basic-Types/Linked-Lists/#List___zipWith "Documentation for List.zipWith") (· + ·) [5, 6] = []`
  * `[x₁, x₂, x₃].[zipWith](Basic-Types/Linked-Lists/#List___zipWith "Documentation for List.zipWith") f [y₁, y₂, y₃, y₄] = [f x₁ y₁, f x₂ y₂, f x₃ y₃]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.zipWithTR "Permalink")def
```


List.zipWithTR.{u_1, u_2, u_3} {α : Type u_1} {β : Type u_2}
  {γ : Type u_3} (f : α → β → γ) (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") γ


List.zipWithTR.{u_1, u_2, u_3}
  {α : Type u_1} {β : Type u_2}
  {γ : Type u_3} (f : α → β → γ)
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") γ


```

Applies a function to the corresponding elements of two lists, stopping at the end of the shorter list.
`O(min |xs| |ys|)`. This is a tail-recursive version of `[List.zipWith](Basic-Types/Linked-Lists/#List___zipWith "Documentation for List.zipWith")` that's used at runtime.
Examples:
  * `[1, 2].[zipWithTR](Basic-Types/Linked-Lists/#List___zipWithTR "Documentation for List.zipWithTR") (· + ·) [5, 6] = [6, 8]`
  * `[1, 2, 3].[zipWithTR](Basic-Types/Linked-Lists/#List___zipWithTR "Documentation for List.zipWithTR") (· + ·) [5, 6, 10] = [6, 8, 13]`
  * `[].[zipWithTR](Basic-Types/Linked-Lists/#List___zipWithTR "Documentation for List.zipWithTR") (· + ·) [5, 6] = []`
  * `[x₁, x₂, x₃].[zipWithTR](Basic-Types/Linked-Lists/#List___zipWithTR "Documentation for List.zipWithTR") f [y₁, y₂, y₃, y₄] = [f x₁ y₁, f x₂ y₂, f x₃ y₃]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.zipWithAll "Permalink")def
```


List.zipWithAll.{u, v, w} {α : Type u} {β : Type v} {γ : Type w}
  (f : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β → γ) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") γ


List.zipWithAll.{u, v, w} {α : Type u}
  {β : Type v} {γ : Type w}
  (f : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β → γ) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") γ


```

Applies a function to the corresponding elements of both lists, stopping when there are no more elements in either list. If one list is shorter than the other, the function is passed `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` for the missing elements.
Examples:
  * `[1, 6].[zipWithAll](Basic-Types/Linked-Lists/#List___zipWithAll "Documentation for List.zipWithAll") [min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min.min") [5, 2] = [[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 1, [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2]`
  * `[1, 2, 3].[zipWithAll](Basic-Types/Linked-Lists/#List___zipWithAll "Documentation for List.zipWithAll") [Prod.mk](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [5, 6] = [([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 1, [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5), ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2, [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 6), ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 3, [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none"))]`
  * `[x₁, x₂].[zipWithAll](Basic-Types/Linked-Lists/#List___zipWithAll "Documentation for List.zipWithAll") f [y] = [f ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x₁) ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") y), f ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x₂) [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.unzip "Permalink")def
```


List.unzip.{u, v} {α : Type u} {β : Type v} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


List.unzip.{u, v} {α : Type u}
  {β : Type v} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


```

Separates a list of pairs into two lists that contain the respective first and second components.
`O(|l|)`.
Examples:
  * `[("Monday", 1), ("Tuesday", 2)].[unzip](Basic-Types/Linked-Lists/#List___unzip "Documentation for List.unzip") = (["Monday", "Tuesday"], [1, 2])`
  * `[(x₁, y₁), (x₂, y₂), (x₃, y₃)].[unzip](Basic-Types/Linked-Lists/#List___unzip "Documentation for List.unzip") = ([x₁, x₂, x₃], [y₁, y₂, y₃])`
  * `([] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") × [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))).[unzip](Basic-Types/Linked-Lists/#List___unzip "Documentation for List.unzip") = (([], []) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") × [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.unzipTR "Permalink")def
```


List.unzipTR.{u, v} {α : Type u} {β : Type v} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


List.unzipTR.{u, v} {α : Type u}
  {β : Type v} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


```

Separates a list of pairs into two lists that contain the respective first and second components.
`O(|l|)`. This is a tail-recursive version of `[List.unzip](Basic-Types/Linked-Lists/#List___unzip "Documentation for List.unzip")` that's used at runtime.
Examples:
  * `[("Monday", 1), ("Tuesday", 2)].[unzipTR](Basic-Types/Linked-Lists/#List___unzipTR "Documentation for List.unzipTR") = (["Monday", "Tuesday"], [1, 2])`
  * `[(x₁, y₁), (x₂, y₂), (x₃, y₃)].[unzipTR](Basic-Types/Linked-Lists/#List___unzipTR "Documentation for List.unzipTR") = ([x₁, x₂, x₃], [y₁, y₂, y₃])`
  * `([] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") × [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))).[unzipTR](Basic-Types/Linked-Lists/#List___unzipTR "Documentation for List.unzipTR") = (([], []) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") × [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))`


###  20.15.3.12. Filtering[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Linked-Lists--API-Reference--Filtering "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.filter "Permalink")def
```


List.filter.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.filter.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Returns the list of elements in `l` for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
`O(|l|)`.
Examples:
  * `[1, 2, 5, 2, 7, 7].[filter](Basic-Types/Linked-Lists/#List___filter "Documentation for List.filter") (· > 2) = [5, 7, 7]`
  * `[1, 2, 5, 2, 7, 7].[filter](Basic-Types/Linked-Lists/#List___filter "Documentation for List.filter") (fun _ => [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) = []`
  * `[1, 2, 5, 2, 7, 7].[filter](Basic-Types/Linked-Lists/#List___filter "Documentation for List.filter") (fun _ => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) = [1, 2, 5, 2, 7, 7]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.filterTR "Permalink")def
```


List.filterTR.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.filterTR.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Returns the list of elements in `l` for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
`O(|l|)`. This is a tail-recursive version of `[List.filter](Basic-Types/Linked-Lists/#List___filter "Documentation for List.filter")`, used at runtime.
Examples:
  * `[1, 2, 5, 2, 7, 7].[filterTR](Basic-Types/Linked-Lists/#List___filterTR "Documentation for List.filterTR") (· > 2)  = [5, 7, 7]`
  * `[1, 2, 5, 2, 7, 7].[filterTR](Basic-Types/Linked-Lists/#List___filterTR "Documentation for List.filterTR") (fun _ => [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) = []`
  * `[1, 2, 5, 2, 7, 7].filterTR (fun _ => true) = * [1, 2, 5, 2, 7, 7]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.filterM "Permalink")def
```


List.filterM.{v} {m : Type → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type}
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)


List.filterM.{v} {m : Type → Type v}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type} (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)


```

Applies the monadic predicate `p` to every element in the list, in order from left to right, and returns the list of elements for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
`O(|l|)`.
Example:
``[1, 2, 2]``Checking 1 Checking 2 Checking 5 Checking 2 Checking 7 Checking 7 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [1, 2, 5, 2, 7, 7].[filterM](Basic-Types/Linked-Lists/#List___filterM "Documentation for List.filterM") fun x => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Checking {x}" return x < 3 ``Checking 1 Checking 2 Checking 5 Checking 2 Checking 7 Checking 7``[1, 2, 2]`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.filterRevM "Permalink")def
```


List.filterRevM.{v} {m : Type → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type}
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)


List.filterRevM.{v} {m : Type → Type v}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type} (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)


```

Applies the monadic predicate `p` on every element in the list in reverse order, from right to left, and returns those elements for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`. The elements of the returned list are in the same order as in the input list.
Example:
``[1, 2, 2]``Checking 7 Checking 7 Checking 2 Checking 5 Checking 2 Checking 1 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [1, 2, 5, 2, 7, 7].[filterRevM](Basic-Types/Linked-Lists/#List___filterRevM "Documentation for List.filterRevM") fun x => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Checking {x}" return x < 3 ``Checking 7 Checking 7 Checking 2 Checking 5 Checking 2 Checking 1``[1, 2, 2]`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.filterMap "Permalink")def
```


List.filterMap.{u, v} {α : Type u} {β : Type v} (f : α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


List.filterMap.{u, v} {α : Type u}
  {β : Type v} (f : α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


```

Applies a function that returns an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` to each element of a list, collecting the non-`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` values.
`O(|l|)`.
Example:
``[10, 14, 14]`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [1, 2, 5, 2, 7, 7].[filterMap](Basic-Types/Linked-Lists/#List___filterMap "Documentation for List.filterMap") fun x => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x > 2 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (2 * x) [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") ``[10, 14, 14]`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.filterMapTR "Permalink")def
```


List.filterMapTR.{u_1, u_2} {α : Type u_1} {β : Type u_2}
  (f : α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


List.filterMapTR.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} (f : α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


```

Applies a function that returns an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` to each element of a list, collecting the non-`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` values.
`O(|l|)`. This is a tail-recursive version of `[List.filterMap](Basic-Types/Linked-Lists/#List___filterMap "Documentation for List.filterMap")`, used at runtime.
Example:
``[10, 14, 14]`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [1, 2, 5, 2, 7, 7].[filterMapTR](Basic-Types/Linked-Lists/#List___filterMapTR "Documentation for List.filterMapTR") fun x => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x > 2 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (2 * x) [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") ``[10, 14, 14]`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.filterMapM "Permalink")def
```


List.filterMapM.{u, v, w} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type w}
  {β : Type u} (f : α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)) (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


List.filterMapM.{u, v, w}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type w} {β : Type u}
  (f : α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)) (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


```

Applies a monadic function that returns an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` to each element of a list, collecting the non-`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` values.
`O(|l|)`.
Example:
``[10, 14, 14]``Examining 1 Examining 2 Examining 5 Examining 2 Examining 7 Examining 7 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [1, 2, 5, 2, 7, 7].[filterMapM](Basic-Types/Linked-Lists/#List___filterMapM "Documentation for List.filterMapM") fun x => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Examining {x}" if x > 2 then return [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (2 * x) else return [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") ``Examining 1 Examining 2 Examining 5 Examining 2 Examining 7 Examining 7``[10, 14, 14]`
####  20.15.3.12.1. Partitioning[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Linked-Lists--API-Reference--Filtering--Partitioning "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.take "Permalink")def
```


List.take.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.take.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Extracts the first `n` elements of `xs`, or the whole list if `n` is greater than `xs.[length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")`.
`O(min n |xs|)`.
Examples:
  * `[a, b, c, d, e].[take](Basic-Types/Linked-Lists/#List___take "Documentation for List.take") 0 = []`
  * `[a, b, c, d, e].[take](Basic-Types/Linked-Lists/#List___take "Documentation for List.take") 3 = [a, b, c]`
  * `[a, b, c, d, e].[take](Basic-Types/Linked-Lists/#List___take "Documentation for List.take") 6 = [a, b, c, d, e]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.takeTR "Permalink")def
```


List.takeTR.{u_1} {α : Type u_1} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.takeTR.{u_1} {α : Type u_1} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Extracts the first `n` elements of `xs`, or the whole list if `n` is greater than `xs.length`.
`O(min n |xs|)`. This is a tail-recursive version of `[List.take](Basic-Types/Linked-Lists/#List___take "Documentation for List.take")`, used at runtime.
Examples:
  * `[a, b, c, d, e].[takeTR](Basic-Types/Linked-Lists/#List___takeTR "Documentation for List.takeTR") 0 = []`
  * `[a, b, c, d, e].[takeTR](Basic-Types/Linked-Lists/#List___takeTR "Documentation for List.takeTR") 3 = [a, b, c]`
  * `[a, b, c, d, e].[takeTR](Basic-Types/Linked-Lists/#List___takeTR "Documentation for List.takeTR") 6 = [a, b, c, d, e]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.takeWhile "Permalink")def
```


List.takeWhile.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.takeWhile.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Returns the longest initial segment of `xs` for which `p` returns true.
`O(|xs|)`.
Examples:
  * `[7, 6, 4, 8].[takeWhile](Basic-Types/Linked-Lists/#List___takeWhile "Documentation for List.takeWhile") (· > 5) = [7, 6]`
  * `[7, 6, 6, 5].[takeWhile](Basic-Types/Linked-Lists/#List___takeWhile "Documentation for List.takeWhile") (· > 5) = [7, 6, 6]`
  * `[7, 6, 6, 8].[takeWhile](Basic-Types/Linked-Lists/#List___takeWhile "Documentation for List.takeWhile") (· > 5) = [7, 6, 6, 8]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.takeWhileTR "Permalink")def
```


List.takeWhileTR.{u_1} {α : Type u_1} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.takeWhileTR.{u_1} {α : Type u_1}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Returns the longest initial segment of `xs` for which `p` returns true.
`O(|xs|)`. This is a tail-recursive version of `[List.take](Basic-Types/Linked-Lists/#List___take "Documentation for List.take")`, used at runtime.
Examples:
  * `[7, 6, 4, 8].[takeWhileTR](Basic-Types/Linked-Lists/#List___takeWhileTR "Documentation for List.takeWhileTR") (· > 5) = [7, 6]`
  * `[7, 6, 6, 5].[takeWhileTR](Basic-Types/Linked-Lists/#List___takeWhileTR "Documentation for List.takeWhileTR") (· > 5) = [7, 6, 6]`
  * `[7, 6, 6, 8].[takeWhileTR](Basic-Types/Linked-Lists/#List___takeWhileTR "Documentation for List.takeWhileTR") (· > 5) = [7, 6, 6, 8]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.drop "Permalink")def
```


List.drop.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.drop.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Removes the first `n` elements of the list `xs`. Returns the empty list if `n` is greater than the length of the list.
`O(min n |xs|)`.
Examples:
  * `[0, 1, 2, 3, 4].[drop](Basic-Types/Linked-Lists/#List___drop "Documentation for List.drop") 0 = [0, 1, 2, 3, 4]`
  * `[0, 1, 2, 3, 4].[drop](Basic-Types/Linked-Lists/#List___drop "Documentation for List.drop") 3 = [3, 4]`
  * `[0, 1, 2, 3, 4].[drop](Basic-Types/Linked-Lists/#List___drop "Documentation for List.drop") 6 = []`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.dropWhile "Permalink")def
```


List.dropWhile.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.dropWhile.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Removes the longest prefix of a list for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Elements are removed from the list until one is encountered for which `p` returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`. This element and the remainder of the list are returned.
`O(|l|)`.
Examples:
  * `[1, 3, 2, 4, 2, 7, 4].[dropWhile](Basic-Types/Linked-Lists/#List___dropWhile "Documentation for List.dropWhile") (· < 4) = [4, 2, 7, 4]`
  * `[8, 3, 2, 4, 2, 7, 4].[dropWhile](Basic-Types/Linked-Lists/#List___dropWhile "Documentation for List.dropWhile") (· < 4) = [8, 3, 2, 4, 2, 7, 4]`
  * `[8, 3, 2, 4, 2, 7, 4].[dropWhile](Basic-Types/Linked-Lists/#List___dropWhile "Documentation for List.dropWhile") (· < 100) = []`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.dropLast "Permalink")def
```


List.dropLast.{u_1} {α : Type u_1} : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.dropLast.{u_1} {α : Type u_1} :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Removes the last element of the list, if one exists.
Examples:
  * `[].[dropLast](Basic-Types/Linked-Lists/#List___dropLast "Documentation for List.dropLast") = []`
  * `["tea"].[dropLast](Basic-Types/Linked-Lists/#List___dropLast "Documentation for List.dropLast") = []`
  * `["tea", "coffee", "juice"].[dropLast](Basic-Types/Linked-Lists/#List___dropLast "Documentation for List.dropLast") = ["tea", "coffee"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.dropLastTR "Permalink")def
```


List.dropLastTR.{u_1} {α : Type u_1} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.dropLastTR.{u_1} {α : Type u_1}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Removes the last element of the list, if one exists.
This is a tail-recursive version of `[List.dropLast](Basic-Types/Linked-Lists/#List___dropLast "Documentation for List.dropLast")`, used at runtime.
Examples:
  * `[].[dropLastTR](Basic-Types/Linked-Lists/#List___dropLastTR "Documentation for List.dropLastTR") = []`
  * `["tea"].[dropLastTR](Basic-Types/Linked-Lists/#List___dropLastTR "Documentation for List.dropLastTR") = []`
  * `["tea", "coffee", "juice"].[dropLastTR](Basic-Types/Linked-Lists/#List___dropLastTR "Documentation for List.dropLastTR") = ["tea", "coffee"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.splitAt "Permalink")def
```


List.splitAt.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.splitAt.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Splits a list at an index, resulting in the first `n` elements of `l` paired with the remaining elements.
If `n` is greater than the length of `l`, then the resulting pair consists of `l` and the empty list. `[List.splitAt](Basic-Types/Linked-Lists/#List___splitAt "Documentation for List.splitAt")` is equivalent to a combination of `[List.take](Basic-Types/Linked-Lists/#List___take "Documentation for List.take")` and `[List.drop](Basic-Types/Linked-Lists/#List___drop "Documentation for List.drop")`, but it is more efficient.
Examples:
  * `["red", "green", "blue"].[splitAt](Basic-Types/Linked-Lists/#List___splitAt "Documentation for List.splitAt") 2 = (["red", "green"], ["blue"])`
  * `["red", "green", "blue"].splitAt 3 = (["red", "green", "blue], [])`
  * `["red", "green", "blue"].splitAt 4 = (["red", "green", "blue], [])`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.span "Permalink")def
```


List.span.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.span.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Splits a list into the longest initial segment for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, paired with the remainder of the list.
`O(|l|)`.
Examples:
  * `[6, 8, 9, 5, 2, 9].[span](Basic-Types/Linked-Lists/#List___span "Documentation for List.span") (· > 5) = ([6, 8, 9], [5, 2, 9])`
  * `[6, 8, 9, 5, 2, 9].[span](Basic-Types/Linked-Lists/#List___span "Documentation for List.span") (· > 10) = ([], [6, 8, 9, 5, 2, 9])`
  * `[6, 8, 9, 5, 2, 9].[span](Basic-Types/Linked-Lists/#List___span "Documentation for List.span") (· > 0) = ([6, 8, 9, 5, 2, 9], [])`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.splitBy "Permalink")def
```


List.splitBy.{u} {α : Type u} (R : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)


List.splitBy.{u} {α : Type u}
  (R : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)


```

Splits a list into the longest segments in which each pair of adjacent elements are related by `R`.
`O(|l|)`.
Examples:
  * `[1, 1, 2, 2, 2, 3, 2].[splitBy](Basic-Types/Linked-Lists/#List___splitBy "Documentation for List.splitBy") (· == ·) = [[1, 1], [2, 2, 2], [3], [2]]`
  * `[1, 2, 5, 4, 5, 1, 4].[splitBy](Basic-Types/Linked-Lists/#List___splitBy "Documentation for List.splitBy") (· < ·) = [[1, 2, 5], [4, 5], [1, 4]]`
  * `[1, 2, 5, 4, 5, 1, 4].[splitBy](Basic-Types/Linked-Lists/#List___splitBy "Documentation for List.splitBy") (fun _ _ => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) = [[1, 2, 5, 4, 5, 1, 4]]`
  * `[1, 2, 5, 4, 5, 1, 4].[splitBy](Basic-Types/Linked-Lists/#List___splitBy "Documentation for List.splitBy") (fun _ _ => [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) = [[1], [2], [5], [4], [5], [1], [4]]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.partition "Permalink")def
```


List.partition.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.partition.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Returns a pair of lists that together contain all the elements of `as`. The first list contains those elements for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, and the second contains those for which `p` returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
`O(|l|)`. `as.[partition](Basic-Types/Linked-Lists/#List___partition "Documentation for List.partition") p` is equivalent to `(as.[filter](Basic-Types/Linked-Lists/#List___filter "Documentation for List.filter") p, as.[filter](Basic-Types/Linked-Lists/#List___filter "Documentation for List.filter") ([not](Basic-Types/Booleans/#Bool___not "Documentation for Bool.not") ∘ p))`, but it is slightly more efficient since it only has to do one pass over the list.
Examples:
  * `[1, 2, 5, 2, 7, 7].[partition](Basic-Types/Linked-Lists/#List___partition "Documentation for List.partition") (· > 2) = ([5, 7, 7], [1, 2, 2])`
  * `[1, 2, 5, 2, 7, 7].[partition](Basic-Types/Linked-Lists/#List___partition "Documentation for List.partition") (fun _ => [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) = ([], [1, 2, 5, 2, 7, 7])`
  * `[1, 2, 5, 2, 7, 7].[partition](Basic-Types/Linked-Lists/#List___partition "Documentation for List.partition") (fun _ => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) = ([1, 2, 5, 2, 7, 7], [])`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.partitionM "Permalink")def
```


List.partitionM.{u_1} {m : Type → Type u_1} {α : Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : m [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


List.partitionM.{u_1}
  {m : Type → Type u_1} {α : Type}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : m [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Returns a pair of lists that together contain all the elements of `as`. The first list contains those elements for which the monadic predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, and the second contains those for which `p` returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`. The list's elements are examined in order, from left to right.
This is a monadic version of `[List.partition](Basic-Types/Linked-Lists/#List___partition "Documentation for List.partition")`.
Example:
`def posOrNeg (x : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") :=   [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x > 0 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")   [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x < 0 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")   [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") "Zero is not positive or negative" `
```
#eval [-1, 2, 3].partitionM posOrNeg

```
`[Except.ok](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.ok") ([2, 3], [-1])`
```
#eval [0, 2, 3].partitionM posOrNeg

```
`[Except.error](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.error") "Zero is not positive or negative"`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.partitionMap "Permalink")def
```


List.partitionMap.{u_1, u_2, u_3} {α : Type u_1} {β : Type u_2}
  {γ : Type u_3} (f : α → β [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") γ) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") γ


List.partitionMap.{u_1, u_2, u_3}
  {α : Type u_1} {β : Type u_2}
  {γ : Type u_3} (f : α → β [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") γ)
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") γ


```

Applies a function that returns a disjoint union to each element of a list, collecting the `[Sum.inl](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inl")` and `[Sum.inr](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inr")` results into separate lists.
Examples:
  * `[0, 1, 2, 3].[partitionMap](Basic-Types/Linked-Lists/#List___partitionMap "Documentation for List.partitionMap") (fun x => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x % 2 = 0 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [.inl](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inl") x [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [.inr](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inr") x) = ([0, 2], [1, 3])`
  * `[0, 1, 2, 3].[partitionMap](Basic-Types/Linked-Lists/#List___partitionMap "Documentation for List.partitionMap") (fun x => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x = 0 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [.inl](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inl") x [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [.inr](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inr") x) = ([0], [1, 2, 3])`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.groupByKey "Permalink")def
```


List.groupByKey.{u, v} {α : Type u} {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (key : β → α) (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


List.groupByKey.{u, v} {α : Type u}
  {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (key : β → α) (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β) :
  [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


```

Groups the elements of a list `xs` according to the function `key`, returning a hash map in which each group is associated with its key. Groups preserve the relative order of elements in `xs`.
Example:
``Std.HashMap.ofList [(0, [0, 2, 4, 6]), (1, [1, 3, 5])]`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [0, 1, 2, 3, 4, 5, 6].[groupByKey](Basic-Types/Linked-Lists/#List___groupByKey "Documentation for List.groupByKey") (· % 2) ``[Std.HashMap.ofList](Basic-Types/Maps-and-Sets/#Std___HashMap___ofList "Documentation for Std.HashMap.ofList") [(0, [0, 2, 4, 6]), (1, [1, 3, 5])]`
###  20.15.3.13. Element Predicates[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Linked-Lists--API-Reference--Element-Predicates "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.contains "Permalink")def
```


List.contains.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


List.contains.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (as : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether `a` is an element of `as`, using `==` to compare elements.
`O(|as|)`. `[List.elem](Basic-Types/Linked-Lists/#List___elem "Documentation for List.elem")` is a synonym that takes the element before the list.
The preferred simp normal form is `l.contains a`, and when `[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α` is available, `l.contains a = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") ↔ a ∈ l` and `l.contains a = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") ↔ a ∉ l`.
Examples:
  * `[1, 4, 2, 3, 3, 7].[contains](Basic-Types/Linked-Lists/#List___contains "Documentation for List.contains") 3 = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[List.contains](Basic-Types/Linked-Lists/#List___contains "Documentation for List.contains") [1, 4, 2, 3, 3, 7] 5 = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.elem "Permalink")def
```


List.elem.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (a : α) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


List.elem.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (a : α)
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether `a` is an element of `l`, using `==` to compare elements.
`O(|l|)`. `[List.contains](Basic-Types/Linked-Lists/#List___contains "Documentation for List.contains")` is a synonym that takes the list before the element.
The preferred simp normal form is `l.[contains](Basic-Types/Linked-Lists/#List___contains "Documentation for List.contains") a`. When `[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α` is available, `l.[contains](Basic-Types/Linked-Lists/#List___contains "Documentation for List.contains") a = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") ↔ a ∈ l` and `l.[contains](Basic-Types/Linked-Lists/#List___contains "Documentation for List.contains") a = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") ↔ a ∉ l`.
Example:
  * `[List.elem](Basic-Types/Linked-Lists/#List___elem "Documentation for List.elem") 3 [1, 4, 2, 3, 3, 7] = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[List.elem](Basic-Types/Linked-Lists/#List___elem "Documentation for List.elem") 5 [1, 4, 2, 3, 3, 7] = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=List.every%E2%86%AAList.all "Permalink")def
```


List.all.{u} {α : Type u} : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → (α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


List.all.{u} {α : Type u} :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → (α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for every element of `l`.
`O(|l|)`. Short-circuits upon encountering the first `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
Examples:
  * `[a, b, c].[all](Basic-Types/Linked-Lists/#List___all "Documentation for List.all") p = (p a && (p b && p c))`
  * `[2, 4, 6].[all](Basic-Types/Linked-Lists/#List___all "Documentation for List.all") (· % 2 = 0) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[2, 4, 5, 6].[all](Basic-Types/Linked-Lists/#List___all "Documentation for List.all") (· % 2 = 0) = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.allM "Permalink")def
```


List.allM.{u, v} {m : Type → Type u} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type v}
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


List.allM.{u, v} {m : Type → Type u}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type v} (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns true if the monadic predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for every element of `l`.
`O(|l|)`. Short-circuits upon encountering the first `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`. The elements in `l` are examined in order from left to right.
[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=List.some%E2%86%AAList.any "Permalink")def
```


List.any.{u} {α : Type u} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


List.any.{u} {α : Type u} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for any element of `l`.
`O(|l|)`. Short-circuits upon encountering the first `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Examples:
  * `[2, 4, 6].[any](Basic-Types/Linked-Lists/#List___any "Documentation for List.any") (· % 2 = 0) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[2, 4, 6].[any](Basic-Types/Linked-Lists/#List___any "Documentation for List.any") (· % 2 = 1) = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `[2, 4, 5, 6].[any](Basic-Types/Linked-Lists/#List___any "Documentation for List.any") (· % 2 = 0) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[2, 4, 5, 6].[any](Basic-Types/Linked-Lists/#List___any "Documentation for List.any") (· % 2 = 1) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.anyM "Permalink")def
```


List.anyM.{u, v} {m : Type → Type u} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type v}
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


List.anyM.{u, v} {m : Type → Type u}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type v} (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns true if the monadic predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for any element of `l`.
`O(|l|)`. Short-circuits upon encountering the first `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`. The elements in `l` are examined in order from left to right.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.and "Permalink")def
```


List.and (bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


List.and (bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if every element of `bs` is the value `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
`O(|bs|)`. Short-circuits at the first `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` value.
  * `[[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true"), [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true"), [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")].[and](Basic-Types/Linked-Lists/#List___and "Documentation for List.and") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true"), [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false"), [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")].[and](Basic-Types/Linked-Lists/#List___and "Documentation for List.and") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `[[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true"), [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false"), [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")].[and](Basic-Types/Linked-Lists/#List___and "Documentation for List.and") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `[].[and](Basic-Types/Linked-Lists/#List___and "Documentation for List.and") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.or "Permalink")def
```


List.or (bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


List.or (bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` is an element of the list `bs`.
`O(|bs|)`. Short-circuits at the first `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` value.
  * `[[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true"), [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true"), [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")].[or](Basic-Types/Linked-Lists/#List___or "Documentation for List.or") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true"), [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false"), [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")].[or](Basic-Types/Linked-Lists/#List___or "Documentation for List.or") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false"), [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false"), [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")].[or](Basic-Types/Linked-Lists/#List___or "Documentation for List.or") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `[[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false"), [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false"), [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")].[or](Basic-Types/Linked-Lists/#List___or "Documentation for List.or") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[].[or](Basic-Types/Linked-Lists/#List___or "Documentation for List.or") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


###  20.15.3.14. Comparisons[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Linked-Lists--API-Reference--Comparisons "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.beq "Permalink")def
```


List.beq.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


List.beq.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether two lists have the same length and their elements are pairwise `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")`. Normally used via the `==` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.isEqv "Permalink")def
```


List.isEqv.{u} {α : Type u} (as bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (eqv : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


List.isEqv.{u} {α : Type u}
  (as bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (eqv : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if `as` and `bs` have the same length and they are pairwise related by `eqv`.
`O(min |as| |bs|)`. Short-circuits at the first non-related pair of elements.
Examples:
  * `[1, 2, 3].[isEqv](Basic-Types/Linked-Lists/#List___isEqv "Documentation for List.isEqv") [2, 3, 4] (· < ·) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[1, 2, 3].[isEqv](Basic-Types/Linked-Lists/#List___isEqv "Documentation for List.isEqv") [2, 2, 4] (· < ·) = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `[1, 2, 3].[isEqv](Basic-Types/Linked-Lists/#List___isEqv "Documentation for List.isEqv") [2, 3] (· < ·) = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.isPerm "Permalink")def
```


List.isPerm.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


List.isPerm.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if `l₁` and `l₂` are permutations of each other. `O(|l₁| * |l₂|)`.
The relation `[List.Perm](Basic-Types/Linked-Lists/#List___Perm___nil "Documentation for List.Perm")` is a logical characterization of permutations. When the `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α` instance corresponds to `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") α`, `isPerm l₁ l₂ ↔ l₁ ~ l₂` (use the theorem `isPerm_iff`).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.isPrefixOf "Permalink")def
```


List.isPrefixOf.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


List.isPrefixOf.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the first list is a prefix of the second.
The relation `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List").IsPrefixOf` expresses this property with respect to logical equality.
Examples:
  * `[1, 2].[isPrefixOf](Basic-Types/Linked-Lists/#List___isPrefixOf "Documentation for List.isPrefixOf") [1, 2, 3] = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[1, 2].[isPrefixOf](Basic-Types/Linked-Lists/#List___isPrefixOf "Documentation for List.isPrefixOf") [1, 2] = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[1, 2].[isPrefixOf](Basic-Types/Linked-Lists/#List___isPrefixOf "Documentation for List.isPrefixOf") [1] = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `[1, 2].[isPrefixOf](Basic-Types/Linked-Lists/#List___isPrefixOf "Documentation for List.isPrefixOf") [1, 1, 2, 3] = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.isPrefixOf? "Permalink")def
```


List.isPrefixOf?.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (l₁ l₂ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)


List.isPrefixOf?.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (l₁ l₂ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)


```

If the first list is a prefix of the second, returns the result of dropping the prefix.
In other words, `isPrefixOf? l₁ l₂` returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") t` when `l₂ == l₁ ++ t`.
Examples:
  * `[1, 2].[isPrefixOf?](Basic-Types/Linked-Lists/#List___isPrefixOf___ "Documentation for List.isPrefixOf?") [1, 2, 3] = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [3]`
  * `[1, 2].[isPrefixOf?](Basic-Types/Linked-Lists/#List___isPrefixOf___ "Documentation for List.isPrefixOf?") [1, 2] = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") []`
  * `[1, 2].[isPrefixOf?](Basic-Types/Linked-Lists/#List___isPrefixOf___ "Documentation for List.isPrefixOf?") [1] = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `[1, 2].[isPrefixOf?](Basic-Types/Linked-Lists/#List___isPrefixOf___ "Documentation for List.isPrefixOf?") [1, 1, 2, 3] = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.isSublist "Permalink")def
```


List.isSublist.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


List.isSublist.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

True if the first list is a potentially non-contiguous sub-sequence of the second list, comparing elements with the `==` operator.
The relation `[List.Sublist](Basic-Types/Linked-Lists/#List___Sublist___slnil "Documentation for List.Sublist")` is a logical characterization of this property.
Examples:
  * `[1, 3].[isSublist](Basic-Types/Linked-Lists/#List___isSublist "Documentation for List.isSublist") [0, 1, 2, 3, 4] = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[1, 3].[isSublist](Basic-Types/Linked-Lists/#List___isSublist "Documentation for List.isSublist") [0, 1, 2, 4] = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.isSuffixOf "Permalink")def
```


List.isSuffixOf.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (l₁ l₂ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


List.isSuffixOf.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (l₁ l₂ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the first list is a suffix of the second.
The relation `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List").IsSuffixOf` expresses this property with respect to logical equality.
Examples:
  * `[2, 3].[isSuffixOf](Basic-Types/Linked-Lists/#List___isSuffixOf "Documentation for List.isSuffixOf") [1, 2, 3] = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[2, 3].[isSuffixOf](Basic-Types/Linked-Lists/#List___isSuffixOf "Documentation for List.isSuffixOf") [1, 2, 3, 4] = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `[2, 3].[isSuffixOf](Basic-Types/Linked-Lists/#List___isSuffixOf "Documentation for List.isSuffixOf") [1, 2] = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `[2, 3].[isSuffixOf](Basic-Types/Linked-Lists/#List___isSuffixOf "Documentation for List.isSuffixOf") [1, 1, 2, 3] = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.isSuffixOf? "Permalink")def
```


List.isSuffixOf?.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (l₁ l₂ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)


List.isSuffixOf?.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (l₁ l₂ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)


```

If the first list is a suffix of the second, returns the result of dropping the suffix from the second.
In other words, `isSuffixOf? l₁ l₂` returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") t` when `l₂ == t ++ l₁`.
Examples:
  * `[2, 3].[isSuffixOf?](Basic-Types/Linked-Lists/#List___isSuffixOf___ "Documentation for List.isSuffixOf?") [1, 2, 3] = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [1]`
  * `[2, 3].[isSuffixOf?](Basic-Types/Linked-Lists/#List___isSuffixOf___ "Documentation for List.isSuffixOf?") [1, 2, 3, 4] = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `[2, 3].[isSuffixOf?](Basic-Types/Linked-Lists/#List___isSuffixOf___ "Documentation for List.isSuffixOf?") [1, 2] = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `[2, 3].[isSuffixOf?](Basic-Types/Linked-Lists/#List___isSuffixOf___ "Documentation for List.isSuffixOf?") [1, 1, 2, 3] = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [1, 1]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.le "Permalink")def
```


List.le.{u} {α : Type u} [[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") α] (as bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : Prop


List.le.{u} {α : Type u} [[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") α]
  (as bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : Prop


```

Non-strict ordering of lists with respect to a strict ordering of their elements.
`as ≤ bs` if `¬ bs < as`.
This relation can be treated as a lexicographic order if the underlying `[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") α` instance is well-behaved. In particular, it should be irreflexive, asymmetric, and antisymmetric. These requirements are precisely formulated in `List.cons_le_cons_iff`. If these hold, then `as ≤ bs` if and only if:
  * `as` is empty, or
  * both `as` and `bs` are non-empty, and the head of `as` is less than the head of `bs`, or
  * both `as` and `bs` are non-empty, their heads are equal, and the tail of `as` is less than or equal to the tail of `bs`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.lt "Permalink")def
```


List.lt.{u} {α : Type u} [[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") α] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → Prop


List.lt.{u} {α : Type u} [[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") α] :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → Prop


```

Lexicographic ordering of lists with respect to an ordering on their elements.
`as < bs` if
  * `as` is empty and `bs` is non-empty, or
  * both `as` and `bs` are non-empty, and the head of `as` is less than the head of `bs`, or
  * both `as` and `bs` are non-empty, their heads are equal, and the tail of `as` is less than the tail of `bs`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.lex "Permalink")def
```


List.lex.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (l₁ l₂ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (lt : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := by exact (· < ·)) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


List.lex.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (l₁ l₂ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (lt : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := by
    exact (· < ·)) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Compares lists lexicographically with respect to a comparison on their elements.
The lexicographic order with respect to `lt` is:
  * `[].[lex](Basic-Types/Linked-Lists/#List___lex "Documentation for List.lex") (b :: bs)` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `as.lex [] = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `(a :: as).[lex](Basic-Types/Linked-Lists/#List___lex "Documentation for List.lex") (b :: bs)` is true if `lt a b` or `a == b` and `lex lt as bs` is true.


###  20.15.3.15. Termination Helpers[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Linked-Lists--API-Reference--Termination-Helpers "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.attach "Permalink")def
```


List.attach.{u_1} {α : Type u_1} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x ∈ l [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


List.attach.{u_1} {α : Type u_1}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x ∈ l [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


```

“Attaches” the proof that the elements of `l` are in fact elements of `l`, producing a new list with the same elements but in the subtype `{ x // x ∈ l }`.
`O(1)`.
This function is primarily used to allow definitions by [well-founded recursion](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=well-founded-recursion) that use higher-order functions (such as `[List.map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map")`) to prove that an value taken from a list is smaller than the list. This allows the well-founded recursion mechanism to prove that the function terminates.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.attachWith "Permalink")def
```


List.attachWith.{u_1} {α : Type u_1} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (P : α → Prop)
  (H : ∀ (x : α), x ∈ l → P x) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") P x [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


List.attachWith.{u_1} {α : Type u_1}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (P : α → Prop)
  (H : ∀ (x : α), x ∈ l → P x) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") P x [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


```

“Attaches” individual proofs to a list of values that satisfy a predicate `P`, returning a list of elements in the corresponding subtype `{ x // P x }`.
`O(1)`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.unattach "Permalink")def
```


List.unattach.{u_1} {α : Type u_1} {p : α → Prop}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") p x [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


List.unattach.{u_1} {α : Type u_1}
  {p : α → Prop} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") p x [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Maps a list of terms in a subtype to the corresponding terms in the type by forgetting that they satisfy the predicate.
This is the inverse of `[List.attachWith](Basic-Types/Linked-Lists/#List___attachWith "Documentation for List.attachWith")` and a synonym for `l.[map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map") (·.val)`.
Mostly this should not be needed by users. It is introduced as an intermediate step by lemmas such as `map_subtype`, and is ideally subsequently simplified away by `unattach_attach`.
This function is usually inserted automatically by Lean as an intermediate step while proving termination. It is rarely used explicitly in code. It is introduced as an intermediate step during the elaboration of definitions by [well-founded recursion](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=well-founded-recursion). If this function is encountered in a proof state, the right approach is usually the tactic `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [List.unattach, -List.map_subtype]`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=List.pmap "Permalink")def
```


List.pmap.{u_1, u_2} {α : Type u_1} {β : Type u_2} {P : α → Prop}
  (f : (a : α) → P a → β) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (H : ∀ (a : α), a ∈ l → P a) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


List.pmap.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} {P : α → Prop}
  (f : (a : α) → P a → β) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (H : ∀ (a : α), a ∈ l → P a) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


```

Maps a partially defined function (defined on those terms of `α` that satisfy a predicate `P`) over a list `l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α`, given a proof that every element of `l` in fact satisfies `P`.
`O(|l|)`. `[List.pmap](Basic-Types/Linked-Lists/#List___pmap "Documentation for List.pmap")`, named for “partial map,” is the equivalent of `[List.map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map")` for such partial functions.
[←20.14. Sum Types](Basic-Types/Sum-Types/#sum-types "20.14. Sum Types")[20.16. Arrays→](Basic-Types/Arrays/#Array "20.16. Arrays")

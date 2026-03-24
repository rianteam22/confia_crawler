[←4.4. Inductive Types](The-Type-System/Inductive-Types/#inductive-types "4.4. Inductive Types")[5. Source Files and Modules→](Source-Files-and-Modules/#files "5. Source Files and Modules")
#  4.5. Quotients[🔗](find/?domain=Verso.Genre.Manual.section&name=quotients "Permalink")
_Quotient types_ allow a new type to be formed by decreasing the granularity of an existing type's [propositional equality](Basic-Propositions/Propositional-Equality/#--tech-term-Propositional-equality). In particular, given a type `AAA` and an equivalence relation `∼\sim∼`, the quotient `A/∼A / \simA/∼` contains the same elements as `AAA`, but every pair of elements that are related by `∼\sim∼` are considered equal. Equality is respected universally; nothing in Lean's logic can observe any difference between two equal terms. Thus, quotient types provide a way to build an impenetrable abstraction barrier. In particular, all functions from a quotient type must prove that they respect the equivalence relation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quotient "Permalink")def
```


Quotient.{u} {α : Sort u} (s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α) : Sort u


Quotient.{u} {α : Sort u} (s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α) :
  Sort u


```

Quotient types coarsen the propositional equality for a type so that terms related by some equivalence relation are considered equal. The equivalence relation is given by an instance of `[Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid")`.
Set-theoretically, `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s` can seen as the set of equivalence classes of `α` modulo the `[Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid")` instance's relation `s.[r](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid.r")`. Functions from `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s` must prove that they respect `s.[r](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid.r")`: to define a function `f : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s → β`, it is necessary to provide `f' : α → β` and prove that for all `x : α` and `y : α`, `s.[r](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid.r") x y → f' x = f' y`. `[Quotient.lift](The-Type-System/Quotients/#Quotient___lift "Documentation for Quotient.lift")` implements this operation.
The key quotient operators are:
  * `[Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk")` places elements of the underlying type `α` into the quotient.
  * `[Quotient.lift](The-Type-System/Quotients/#Quotient___lift "Documentation for Quotient.lift")` allows the definition of functions from the quotient to some other type.
  * `[Quotient.sound](The-Type-System/Quotients/#Quotient___sound "Documentation for Quotient.sound")` asserts the equality of elements related by `r`
  * `[Quotient.ind](The-Type-System/Quotients/#Quotient___ind "Documentation for Quotient.ind")` is used to write proofs about quotients by assuming that all elements are constructed with `[Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk")`.


`[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")` is built on top of the primitive quotient type `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")`, which does not require a proof that the relation is an equivalence relation. `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")` should be used instead of `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")` for relations that actually are equivalence relations.
A proof that two elements of the underlying type are related by the equivalence relation is sufficient to prove that they are equal in the `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")`. However, [definitional equality](The-Type-System/#--tech-term-definitional-equality) is unaffected by the use of `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")`: two elements in the quotient are definitionally equal if and only if they are definitionally equal in the underlying type.
Quotient types are not widely used in programming. However, they occur regularly in mathematics: 

Integers
    
The integers are traditionally defined as a pair of natural numbers `(n,k)(n, k)(n,k)` that encodes the integer `n−kn - kn−k`. In this encoding, two integers `(n1,k1)(n_1, k_1)(n1​,k1​)` and `(n2,k2)(n_2, k_2)(n2​,k2​)` are equal if `n1+k2=n2+k1n_1 + k_2 = n_2 + k_1n1​+k2​=n2​+k1​`. 

Rational Numbers
    
The number `nd\frac{n}{d}dn​` can be encoded as the pair `(n,d)(n, d)(n,d)`, where `d≠0d \neq 0d=0`. Two rational numbers `n1d1\frac{n_1}{d_1}d1​n1​​` and `n2d2\frac{n_2}{d_2}d2​n2​​` are equal if `n1d2=n2d1n_1 d_2 = n_2 d_1n1​d2​=n2​d1​`. 

Real Numbers
    
The real numbers can be represented as a Cauchy sequence, but this encoding is not unique. Using a quotient type, two Cauchy sequences can be made equal when their difference converges to zero. 

Finite Sets
    
Finite sets can be represented as lists of elements. With a quotient types, two finite sets can be made equal if they contain the same elements; this definition does not impose any requirements (such as decidable equality or an ordering relation) on the type of elements.
One alternative to quotient types would be to reason directly about the equivalence classes introduced by the relation. The downside of this approach is that it does not allow _computation_ : in addition to knowing _that_ there is an integer that is the sum of 5 and 8, it is useful for `5+8=135 + 8 = 135+8=13` to not be a theorem that requires proof. Defining functions out of sets of equivalence classes relies on non-computational classical reasoning principles, while functions from quotient types are ordinary computational functions that additionally respect an equivalence relation.
##  4.5.1. Alternatives to Quotient Types[🔗](find/?domain=Verso.Genre.Manual.section&name=quotient-alternatives "Permalink")
While `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")` is a convenient way to form quotients with reasonable computational properties, it is often possible to define quotients in other ways.
In general, a type `QQQ` is said to be the quotient of `AAA` by an equivalence relation `∼\sim∼` if it respects the universal property of quotients: there is a function `q:A→Qq:A\to Qq:A→Q` with the property that `q(a)=q(b)q(a)=q(b)q(a)=q(b)` if and only if `a∼ba\sim ba∼b` for all `aaa` and `bbb` in `AAA`.
Quotients formed with `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")` have this property up to [propositional equality](Basic-Propositions/Propositional-Equality/#--tech-term-Propositional-equality): elements of `AAA` that are related by `∼\sim∼` are equal, so they cannot be distinguished. However, members of the same equivalence class are not necessarily [definitionally equal](The-Type-System/#--tech-term-definitional-equality) in the quotient.
Quotients may also be implemented by designating a single representative of each equivalence class in `AAA` itself, and then defining `QQQ` as pair of elements in `AAA` with proofs that they are such a canonical representative. Together with a function that maps each `aaa` in `AAA` to its canonical representative, `QQQ` is a quotient of `AAA`. Due to [proof irrelevance](The-Type-System/#--tech-term-proof-irrelevance), representatives in `QQQ` of the same equivalence class are [definitionally equal](The-Type-System/#--tech-term-definitional-equality).
Such a manually implemented quotient `QQQ` can be easier to work with than `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")`. In particular, because each equivalence class is represented by its single canonical representative, there's no need to prove that functions from the quotient respect the equivalence relation. It can also have better computational properties due to the fact that the computations give normalized values (in contrast, elements of `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")` can be represented in multiple ways). Finally, because the manually implemented quotient is an [inductive type](The-Type-System/Inductive-Types/#--tech-term-Inductive-types), it can be used in contexts where other kinds of types cannot, such as when defining a [nested inductive type](The-Type-System/Inductive-Types/#nested-inductive-types). However, not all quotients can be manually implemented.
Manually Quotiented Integers
When implemented as pairs of `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`s, each equivalence class according to the desired equality for integers has a canonical representative in which at least one of the `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`s is zero. This can be represented as a Lean structure:
`structure Z where   a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   b : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   canonical : a = 0 ∨ b = 0 `
Due to [proof irrelevance](The-Type-System/#--tech-term-proof-irrelevance), every value of this structure type that represents the same integer is _already_ equal. Constructing a `[Z](The-Type-System/Quotients/#Z-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example")` can be made more convenient with a wrapper that uses the fact that subtraction of natural numbers truncates at zero to automate the construction of the proof:
`def Z.mk' (n k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Z](The-Type-System/Quotients/#Z-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") where   [a](The-Type-System/Quotients/#Z___a-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") := n - k   [b](The-Type-System/Quotients/#Z___b-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") := k - n   [canonical](The-Type-System/Quotients/#Z___canonical-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") := byn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ n [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 [∨](Basic-Propositions/Logical-Connectives/#Or___inl "Documentation for Or") k [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 [omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic")All goals completed! 🐙 `
This construction respects the equality demanded of integers:
`theorem Z_mk'_respects_eq :     ([Z.mk'](The-Type-System/Quotients/#Z___mk___-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") n k = [Z.mk'](The-Type-System/Quotients/#Z___mk___-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") n' k') ↔ (n + k' = n' + k) := byn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [Z.mk'](The-Type-System/Quotients/#Z___mk___-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") n k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Z.mk'](The-Type-System/Quotients/#Z___mk___-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") n' k' [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n' [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k   [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [[Z.mk'](The-Type-System/Quotients/#Z___mk___-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example")]n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ n [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") k' [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") k [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") n' [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n' [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k   [omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic")All goals completed! 🐙 `
To use this type in examples, it's convenient to have `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg")`, `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat")`, and `ToString` instances. These instances make it easier to read or write examples.
`instance : [Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") [Z](The-Type-System/Quotients/#Z-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") where   [neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg") n := [Z.mk'](The-Type-System/Quotients/#Z___mk___-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") n.[b](The-Type-System/Quotients/#Z___b-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") n.[a](The-Type-System/Quotients/#Z___a-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example")  instance : [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") [Z](The-Type-System/Quotients/#Z-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") n where   [ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") := [Z.mk'](The-Type-System/Quotients/#Z___mk___-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") n 0  instance : ToString [Z](The-Type-System/Quotients/#Z-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") where   toString n :=     [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n.[a](The-Type-System/Quotients/#Z___a-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") = 0 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax")       [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n.[b](The-Type-System/Quotients/#Z___b-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") = 0 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") "0"       [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") s!"-{n.[b](The-Type-System/Quotients/#Z___b-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example")}"     [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") toString n.[a](The-Type-System/Quotients/#Z___a-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") ```5`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (5 : [Z](The-Type-System/Quotients/#Z-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example")) `
```
5
```
``-5`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (-5 : [Z](The-Type-System/Quotients/#Z-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example")) `
```
-5
```

Addition is addition of the underlying `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`s:
`instance : [Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") [Z](The-Type-System/Quotients/#Z-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") where   [add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add.add") n k := [Z.mk'](The-Type-System/Quotients/#Z___mk___-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") (n.[a](The-Type-System/Quotients/#Z___a-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") + k.[a](The-Type-System/Quotients/#Z___a-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example")) (n.[b](The-Type-System/Quotients/#Z___b-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example") + k.[b](The-Type-System/Quotients/#Z___b-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example")) ```17`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (-5 + 22: [Z](The-Type-System/Quotients/#Z-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example")) `
```
17
```

Because each equivalence class is uniquely represented, there's no need to write a proof that these functions from `[Z](The-Type-System/Quotients/#Z-_LPAR_in-Manually-Quotiented-Integers_RPAR_ "Definition of example")` respect the equivalence relation. However, in practice, the [API for quotients](The-Type-System/Quotients/#quotient-api) should be implemented for manually-constructed quotients and proved to respect the universal property.
[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgFqIO4At4IFCMQIaIBciAcgSHogEYnmXVQEB2A9iwJbMA29RAXkQAGRIAoiWoiHCcOACbwAZigB0AWwDWAckQAKFog30KIAJT1UmbPGpFiQgwFpD1OvcOJnLJqw7cCfO40AJ6IbGrwAOYEsiBYbAhqKAD6mlrJCMAADvAwwMnwAI4k1Pi6yOraiAZGQhVp1Tra5oAphHoGANSGOg46XRrmQcHUwJxqWYgA2vXaALrU4VExOJwsoKxQSKRkUSjoWLj4LLsG7jM6LCp0l8ur6yyb9ADyiiZ7BlaHYa+UJHWVFxEsjuIA2W0QABU2ABlcCrSJ7T42fAgGFwlgI04CUqITjKG5SESIOLwbz4cm4/FXQmiEkGABEwnpOPw8B4wCQwAAhPTHABvS40AC+zIpbI5xLRYHh1RUywAxPAAG4BPQAVgsplkipVfF0jg1pGQWpWa1BD3BAEE5HJEQdkYQbdUPGcAe05Yh+nLzPpqV6aCadar9RqugAmMNG0xAA"\))
Built-In Integers as Quotients
Lean's built-in integer type `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` satisfies the universal property of quotients, and can thus be thought of as a quotient of pairs of `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`s. The canonical representative of each equivalence class can be computed via comparison and subtraction:This `[toInt](The-Type-System/Quotients/#toInt-_LPAR_in-Built-In-Integers-as-Quotients_RPAR_ "Definition of example")` function is called `[Int.subNatNat](Basic-Types/Integers/#Int___subNatNat "Documentation for Int.subNatNat")` in the standard library.
`def toInt (n k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") :=   [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n < k [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") - (k - n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))   [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n = k [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") 0   [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") (n - k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) `
It satisfies the universal property. Two pairs of `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`s represent the same integer if and only if `[toInt](The-Type-System/Quotients/#toInt-_LPAR_in-Built-In-Integers-as-Quotients_RPAR_ "Definition of example")` computes the same `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` for both pairs:
`theorem toInt_sound :     n + k' = k + n' ↔     [toInt](The-Type-System/Quotients/#toInt-_LPAR_in-Built-In-Integers-as-Quotients_RPAR_ "Definition of example") n k = [toInt](The-Type-System/Quotients/#toInt-_LPAR_in-Built-In-Integers-as-Quotients_RPAR_ "Definition of example") n' k' := byn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n' [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") [toInt](The-Type-System/Quotients/#toInt-_LPAR_in-Built-In-Integers-as-Quotients_RPAR_ "Definition of example") n k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [toInt](The-Type-System/Quotients/#toInt-_LPAR_in-Built-In-Integers-as-Quotients_RPAR_ "Definition of example") n' k'   [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") only [[toInt](The-Type-System/Quotients/#toInt-_LPAR_in-Built-In-Integers-as-Quotients_RPAR_ "Definition of example")]n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n' [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff")   (if n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k then [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") n[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") else if n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k then 0 else ↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")n [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") k[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")     if n' [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k' then [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") n'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") else if n' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k' then 0 else ↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")n' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") k'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")   [split](Tactic-Proofs/Tactic-Reference/#split "Documentation for tactic")isTruen:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝:n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k⊢ n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n' [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") n[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") if n' [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k' then [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") n'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") else if n' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k' then 0 else ↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")n' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") k'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")isFalsen:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k⊢ n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n' [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") (if n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k then 0 else ↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")n [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") k[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") if n' [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k' then [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") n'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") else if n' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k' then 0 else ↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")n' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") k'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") <;>isTruen:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝:n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k⊢ n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n' [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") n[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") if n' [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k' then [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") n'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") else if n' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k' then 0 else ↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")n' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") k'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")isFalsen:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k⊢ n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n' [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") (if n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k then 0 else ↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")n [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") k[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") if n' [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k' then [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") n'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") else if n' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k' then 0 else ↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")n' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") k'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [split](Tactic-Proofs/Tactic-Reference/#split "Documentation for tactic")isFalse.isTruen:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝¹:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") kh✝:n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k⊢ n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n' [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") if n' [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k' then [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") n'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") else if n' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k' then 0 else ↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")n' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") k'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")isFalse.isFalsen:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝¹:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") kh✝:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k⊢ n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n' [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") ↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")n [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") k[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") if n' [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k' then [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") n'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") else if n' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k' then 0 else ↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")n' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") k'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") <;>isTrue.isTruen:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝¹:n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") kh✝:n' [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k'⊢ n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n' [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") n[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") n'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")isTrue.isFalsen:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝¹:n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") kh✝:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")n' [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k'⊢ n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n' [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") n[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") if n' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k' then 0 else ↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")n' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") k'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")isFalse.isTruen:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝¹:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") kh✝:n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k⊢ n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n' [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") if n' [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k' then [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") n'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") else if n' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k' then 0 else ↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")n' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") k'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")isFalse.isFalsen:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h✝¹:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") kh✝:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k⊢ n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") n' [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") ↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")n [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") k[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") if n' [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") k' then [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")k' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") n'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") else if n' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") k' then 0 else ↑[(](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub")n' [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") k'[)](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") [omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("CYUwZgBALg9gkgOyhAFAiBrCAuCA5AQygEocJFlsBeAKAggEtJ0AeTaACxHQFpUs+6XIRJ0IIADYBnEI2YQq7KF3QAGMZJmpe7YUWI0aykDABOIALbR4SAPpSYAVwTAcY+ugDUmAOQL23gh+gCmE7tYUEOhYirARQb44igBGAJ5iUgwWAA4QMAgSKRAA2rFIALrpWRIMyCwA3AB8EFJVNRD1TTAWIADmBEA"\))
##  4.5.2. Setoids[🔗](find/?domain=Verso.Genre.Manual.section&name=setoids "Permalink")
Quotient types are built on setoids. A _setoid_ is a type paired with a distinguished equivalence relation. Unlike a quotient type, the abstraction barrier is not enforced, and proof automation designed around equality cannot be used with the setoid's equivalence relation. Setoids are useful on their own, in addition to being a building block for quotient types.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Setoid.mk "Permalink")type class
```


Setoid.{u} (α : Sort u) : Sort (max 1 u)


Setoid.{u} (α : Sort u) : Sort (max 1 u)


```

A setoid is a type with a distinguished equivalence relation, denoted `≈`.
The `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")` type constructor requires a `[Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid")` instance.
#  Instance Constructor

```
[Setoid.mk](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid.mk").{u}
```

#  Methods

```
r : α → α → Prop
```

`x ≈ y` is the distinguished equivalence relation of a setoid.

```
iseqv : [Equivalence](The-Type-System/Quotients/#Equivalence___mk "Documentation for Equivalence") [Setoid.r](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid.r")
```

The relation `x ≈ y` is an equivalence relation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Setoid.refl "Permalink")theorem
```


Setoid.refl.{u} {α : Sort u} [[Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α] (a : α) : a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") a


Setoid.refl.{u} {α : Sort u} [[Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α]
  (a : α) : a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") a


```

A setoid's equivalence relation is reflexive.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Setoid.symm "Permalink")theorem
```


Setoid.symm.{u} {α : Sort u} [[Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α] {a b : α} (hab : a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b) : b [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") a


Setoid.symm.{u} {α : Sort u} [[Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α]
  {a b : α} (hab : a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b) : b [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") a


```

A setoid's equivalence relation is symmetric.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Setoid.trans "Permalink")theorem
```


Setoid.trans.{u} {α : Sort u} [[Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α] {a b c : α} (hab : a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b)
  (hbc : b [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") c) : a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") c


Setoid.trans.{u} {α : Sort u} [[Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α]
  {a b c : α} (hab : a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b)
  (hbc : b [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") c) : a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") c


```

A setoid's equivalence relation is transitive.
##  4.5.3. Equivalence Relations[🔗](find/?domain=Verso.Genre.Manual.section&name=equivalence-relations "Permalink")
An _equivalence relation_ is a relation that is reflexive, symmetric, and transitive.
syntaxEquivalence Relations
Equivalence according to some canonical equivalence relation for a type is written using `≈`, which is overloaded using the [type class](Type-Classes/#--tech-term-type-class) `[HasEquiv](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv")`.

```
term ::= ...
    | 


x ≈ y says that x and y are equivalent. Because this is a typeclass,
the notion of equivalence is type-dependent. 


Conventions for notations in identifiers:




  * The recommended spelling of ≈ in identifiers is equiv.




term ≈ term
```

[🔗](find/?domain=Verso.Genre.Manual.doc&name=HasEquiv.mk "Permalink")type class
```


HasEquiv.{u, v} (α : Sort u) : Sort (max u (v + 1))


HasEquiv.{u, v} (α : Sort u) :
  Sort (max u (v + 1))


```

`[HasEquiv](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv") α` is the typeclass which supports the notation `x ≈ y` where `x y : α`.
#  Instance Constructor

```
[HasEquiv.mk](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.mk").{u, v}
```

#  Methods

```
Equiv : α → α → Sort v
```

`x ≈ y` says that `x` and `y` are equivalent. Because this is a typeclass, the notion of equivalence is type-dependent.
Conventions for notations in identifiers:
  * The recommended spelling of `≈` in identifiers is `equiv`.


The fact that a relation `r` is actually an equivalence relation is stated `[Equivalence](The-Type-System/Quotients/#Equivalence___mk "Documentation for Equivalence") r`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Equivalence.mk "Permalink")structure
```


Equivalence.{u} {α : Sort u} (r : α → α → Prop) : Prop


Equivalence.{u} {α : Sort u}
  (r : α → α → Prop) : Prop


```

An equivalence relation `r : α → α → Prop` is a relation that is
  * reflexive: `r x x`,
  * symmetric: `r x y` implies `r y x`, and
  * transitive: `r x y` and `r y z` implies `r x z`.


Equality is an equivalence relation, and equivalence relations share many of the properties of equality.
#  Constructor

```
[Equivalence.mk](The-Type-System/Quotients/#Equivalence___mk "Documentation for Equivalence.mk").{u}
```

#  Fields

```
refl : ∀ (x : α), r x x
```

An equivalence relation is reflexive: `r x x`

```
symm : ∀ {x y : α}, r x y → r y x
```

An equivalence relation is symmetric: `r x y` implies `r y x`

```
trans : ∀ {x y z : α}, r x y → r y z → r x z
```

An equivalence relation is transitive: `r x y` and `r y z` implies `r x z`
Every `[Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid")` instance leads to a corresponding `[HasEquiv](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv")` instance.
##  4.5.4. Quotient API[🔗](find/?domain=Verso.Genre.Manual.section&name=quotient-api "Permalink")
The quotient API relies on a pre-existing `[Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid")` instance.
###  4.5.4.1. Introducing Quotients[🔗](find/?domain=Verso.Genre.Manual.section&name=quotient-intro "Permalink")
The type `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")` expects an instance of `[Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid")` as an ordinary parameter, rather than as an [instance implicit](Type-Classes/#--tech-term-instance-implicit) parameter. This helps ensure that the quotient uses the intended equivalence relation. The instance can be provided either by naming the instance or by using `[inferInstance](Type-Classes/Instance-Synthesis/#inferInstance "Documentation for inferInstance")`.
A value in the quotient is a value from the setoid's underlying type, wrapped in `[Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quotient.mk "Permalink")def
```


Quotient.mk.{u} {α : Sort u} (s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α) (a : α) : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s


Quotient.mk.{u} {α : Sort u}
  (s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α) (a : α) : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s


```

Places an element of a type into the quotient that equates terms according to an equivalence relation.
The setoid instance is provided explicitly. `[Quotient.mk'](The-Type-System/Quotients/#Quotient___mk___ "Documentation for Quotient.mk'")` uses instance synthesis instead.
Given `v : α`, `[Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s v : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s` is like `v`, except all observations of `v`'s value must respect `s.[r](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid.r")`. `[Quotient.lift](The-Type-System/Quotients/#Quotient___lift "Documentation for Quotient.lift")` allows values in a quotient to be mapped to other types, so long as the mapping respects `s.[r](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid.r")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quotient.mk' "Permalink")def
```


Quotient.mk'.{u} {α : Sort u} [s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α] (a : α) : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s


Quotient.mk'.{u} {α : Sort u}
  [s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α] (a : α) : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s


```

Places an element of a type into the quotient that equates terms according to an equivalence relation.
The equivalence relation is found by synthesizing a `[Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid")` instance. `[Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk")` instead expects the instance to be provided explicitly.
Given `v : α`, `[Quotient.mk'](The-Type-System/Quotients/#Quotient___mk___ "Documentation for Quotient.mk'") v : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s` is like `v`, except all observations of `v`'s value must respect `s.[r](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid.r")`. `[Quotient.lift](The-Type-System/Quotients/#Quotient___lift "Documentation for Quotient.lift")` allows values in a quotient to be mapped to other types, so long as the mapping respects `s.[r](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid.r")`.
The Integers as a Quotient Type
The integers, defined as pairs of natural numbers where the represented integer is the difference of the two numbers, can be represented via a quotient type. This representation is not unique: both `(4, 7)` and `(1, 4)` represent `-3`.
Two encoded integers should be considered equal when they are related by `[Z.eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example")`:
`def Z' : Type := [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") × [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")  def Z.eq (n k : [Z'](The-Type-System/Quotients/#Z___-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example")) : Prop :=   n.1 + k.2 = n.2 + k.1 `
This relation is an equivalence relation:
`def Z.eq.eqv : [Equivalence](The-Type-System/Quotients/#Equivalence___mk "Documentation for Equivalence") [Z.eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") where   [refl](The-Type-System/Quotients/#Equivalence___mk "Documentation for Equivalence.refl") := by⊢ ∀ (x : [Z'](The-Type-System/Quotients/#Z___-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example")), [eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") x x     [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") (x, y)x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")     [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") +[arith](The-Simplifier/Configuring-Simplification/#Lean___Meta___Simp___Config___mk "Documentation for Lean.Meta.Simp.Config.arith") [[eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example")]All goals completed! 🐙   [symm](The-Type-System/Quotients/#Equivalence___mk "Documentation for Equivalence.symm") := by⊢ ∀ {x y : [Z'](The-Type-System/Quotients/#Z___-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example")}, [eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") x y → [eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") y x     [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") (x, y) (x', y')x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")x':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x'[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y'[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") → [eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x'[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y'[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") heqx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")x':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")heq:[eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x'[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y'[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")⊢ [eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x'[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y'[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")     [simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic") only [[eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example")]x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")x':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")heq:x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x'⊢ x' [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y' [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x     [omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic")All goals completed! 🐙   [trans](The-Type-System/Quotients/#Equivalence___mk "Documentation for Equivalence.trans") := by⊢ ∀ {x y z : [Z'](The-Type-System/Quotients/#Z___-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example")}, [eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") x y → [eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") y z → [eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") x z     [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") (x, y) (x', y')x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")x':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ ∀ {z : [Z'](The-Type-System/Quotients/#Z___-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example")}, [eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x'[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y'[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") → [eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x'[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y'[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") z → [eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") z (x'', y'')x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")x':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")x'':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y'':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x'[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y'[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") → [eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x'[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y'[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x''[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y''[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") → [eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x''[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y''[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")     [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") heq1 heq2x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")x':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")x'':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y'':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")heq1:[eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x'[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y'[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")heq2:[eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x'[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y'[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x''[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y''[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")⊢ [eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")x''[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") y''[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")     [simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic") only [[eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example")]x:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")x':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")x'':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")y'':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")heq1:x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x'heq2:x' [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y'' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y' [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x''⊢ x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") y'' [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x''     [omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic")All goals completed! 🐙 `
Thus, it can be used as a `[Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid")`:
`instance Z.instSetoid : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") [Z'](The-Type-System/Quotients/#Z___-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") where   [r](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid.r") := [Z.eq](The-Type-System/Quotients/#Z___eq-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example")   [iseqv](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid.iseqv") := [Z.eq.eqv](The-Type-System/Quotients/#Z___eq___eqv-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") `
The type `[Z](The-Type-System/Quotients/#Z-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example")` of integers is then the quotient of `[Z'](The-Type-System/Quotients/#Z___-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example")` by the `[Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid")` instance:
`def Z : Type := [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") [Z.instSetoid](The-Type-System/Quotients/#Z___instSetoid-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") `
The helper `[Z.mk](The-Type-System/Quotients/#Z___mk-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example")` makes it simpler to create integers without worrying about the choice of `[Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid")` instance:
`def Z.mk (n : [Z'](The-Type-System/Quotients/#Z___-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example")) : [Z](The-Type-System/Quotients/#Z-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") := [Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") _ n `
However, numeric literals are even more convenient. An `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat")` instance allows numeric literals to be used for integers:
`instance : [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") [Z](The-Type-System/Quotients/#Z-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") n where   [ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") := [Z.mk](The-Type-System/Quotients/#Z___mk-_LPAR_in-The-Integers-as-a-Quotient-Type_RPAR_ "Definition of example") (n, 0) `
[Live ↪](javascript:openLiveLink\("CYUwZgBAWg5BBcEAqBPADiBBeCA5AhgC4QDreRAUBaJFAHQgCOEAFAHYQDWC0MAlDwAKAJwD2abBQgQ2dAIwQA1FzoAmCDlnrlneVRrQGjIwDceAUUYBXAJYn8AGxBsAxpnpMIAdwAWIYSBSEAFgDtgQAEYoQdI2bIRirAAeADQQKHwxEADONgC2Eor4wjaEPhAA2kwAukHZKHl54VFZcQmiyWkZyTBd/BB+jFm5BQD6jmGibA4olTVZonkgAOb4QQn4bNnN0dKx8YksqekCR73p/WfnKDD8rQcdgwqDqsP5aOMOk9OzVYy1ewgixWawocWyhE2bkM4MIAGUQIRRDZgDwEUiUbxvH4AkFhOEPENYtkmGZ4DhCaZ9OBoDxUBhwgBFKyiQg2ZzEeiw9HI4DU2h0PLcdg8WACRBQJkstkcwXcUYyKiwqGYRAAeTABE5Mmx/kC0lEmqIBLlrDYaQADHwgA"\))
###  4.5.4.2. Eliminating Quotients[🔗](find/?domain=Verso.Genre.Manual.section&name=quotient-elim "Permalink")
Functions from quotients can be defined by proving that a function from the underlying type respects the quotient's equivalence relation. This is accomplished using `[Quotient.lift](The-Type-System/Quotients/#Quotient___lift "Documentation for Quotient.lift")` or its binary counterpart `[Quotient.lift₂](The-Type-System/Quotients/#Quotient___lift___ "Documentation for Quotient.lift₂")`. The variants `[Quotient.liftOn](The-Type-System/Quotients/#Quotient___liftOn "Documentation for Quotient.liftOn")` and `[Quotient.liftOn₂](The-Type-System/Quotients/#Quotient___liftOn___ "Documentation for Quotient.liftOn₂")` place the quotient parameter first rather than last in the parameter list.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quotient.lift "Permalink")def
```


Quotient.lift.{u, v} {α : Sort u} {β : Sort v} {s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α}
  (f : α → β) : (∀ (a b : α), a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b → f a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f b) → [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s → β


Quotient.lift.{u, v} {α : Sort u}
  {β : Sort v} {s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α}
  (f : α → β) :
  (∀ (a b : α), a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b → f a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f b) →
    [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s → β


```

Lifts a function from an underlying type to a function on a quotient, requiring that it respects the quotient's equivalence relation.
Given `s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α` and a quotient `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s`, applying a function `f : α → β` requires a proof `h` that `f` respects the equivalence relation `s.[r](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid.r")`. In this case, the function `[Quotient.lift](The-Type-System/Quotients/#Quotient___lift "Documentation for Quotient.lift") f h : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s → β` computes the same values as `f`.
`[Quotient.liftOn](The-Type-System/Quotients/#Quotient___liftOn "Documentation for Quotient.liftOn")` is a version of this operation that takes the quotient value as its first explicit parameter.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quotient.liftOn "Permalink")def
```


Quotient.liftOn.{u, v} {α : Sort u} {β : Sort v} {s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α}
  (q : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s) (f : α → β) (c : ∀ (a b : α), a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b → f a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f b) : β


Quotient.liftOn.{u, v} {α : Sort u}
  {β : Sort v} {s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α}
  (q : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s) (f : α → β)
  (c : ∀ (a b : α), a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b → f a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f b) : β


```

Lifts a function from an underlying type to a function on a quotient, requiring that it respects the quotient's equivalence relation.
Given `s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α` and a quotient value `q : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s`, applying a function `f : α → β` requires a proof `c` that `f` respects the equivalence relation `s.[r](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid.r")`. In this case, the term `[Quotient.liftOn](The-Type-System/Quotients/#Quotient___liftOn "Documentation for Quotient.liftOn") q f h : β` reduces to the result of applying `f` to the underlying `α` value.
`[Quotient.lift](The-Type-System/Quotients/#Quotient___lift "Documentation for Quotient.lift")` is a version of this operation that takes the quotient value last, rather than first.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quotient.lift%E2%82%82 "Permalink")def
```


Quotient.lift₂.{uA, uB, uC} {α : Sort uA} {β : Sort uB} {φ : Sort uC}
  {s₁ : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α} {s₂ : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") β} (f : α → β → φ)
  (c :
    ∀ (a₁ : α) (b₁ : β) (a₂ : α) (b₂ : β),
      a₁ [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") a₂ → b₁ [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b₂ → f a₁ b₁ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f a₂ b₂)
  (q₁ : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s₁) (q₂ : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s₂) : φ


Quotient.lift₂.{uA, uB, uC} {α : Sort uA}
  {β : Sort uB} {φ : Sort uC}
  {s₁ : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α} {s₂ : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") β}
  (f : α → β → φ)
  (c :
    ∀ (a₁ : α) (b₁ : β) (a₂ : α) (b₂ : β),
      a₁ [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") a₂ →
        b₁ [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b₂ → f a₁ b₁ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f a₂ b₂)
  (q₁ : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s₁) (q₂ : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s₂) :
  φ


```

Lifts a binary function from the underlying types to a binary function on quotients. The function must respect both quotients' equivalence relations.
`[Quotient.lift](The-Type-System/Quotients/#Quotient___lift "Documentation for Quotient.lift")` is a version of this operation for unary functions. `[Quotient.liftOn₂](The-Type-System/Quotients/#Quotient___liftOn___ "Documentation for Quotient.liftOn₂")` is a version that take the quotient parameters first.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quotient.liftOn%E2%82%82 "Permalink")def
```


Quotient.liftOn₂.{uA, uB, uC} {α : Sort uA} {β : Sort uB} {φ : Sort uC}
  {s₁ : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α} {s₂ : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") β} (q₁ : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s₁) (q₂ : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s₂)
  (f : α → β → φ)
  (c :
    ∀ (a₁ : α) (b₁ : β) (a₂ : α) (b₂ : β),
      a₁ [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") a₂ → b₁ [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b₂ → f a₁ b₁ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f a₂ b₂) :
  φ


Quotient.liftOn₂.{uA, uB, uC}
  {α : Sort uA} {β : Sort uB}
  {φ : Sort uC} {s₁ : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α}
  {s₂ : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") β} (q₁ : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s₁)
  (q₂ : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s₂) (f : α → β → φ)
  (c :
    ∀ (a₁ : α) (b₁ : β) (a₂ : α) (b₂ : β),
      a₁ [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") a₂ →
        b₁ [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b₂ → f a₁ b₁ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f a₂ b₂) :
  φ


```

Lifts a binary function from the underlying types to a binary function on quotients. The function must respect both quotients' equivalence relations.
`[Quotient.liftOn](The-Type-System/Quotients/#Quotient___liftOn "Documentation for Quotient.liftOn")` is a version of this operation for unary functions. `[Quotient.lift₂](The-Type-System/Quotients/#Quotient___lift___ "Documentation for Quotient.lift₂")` is a version that take the quotient parameters last.
Integer Negation and Addition
Given the encoding `Z` of integers as a quotient of pairs of natural numbers, negation can be implemented by swapping the first and second projections:
`def neg' : Z' → Z   | (x, y) => .mk (y, x) `
This can be transformed into a function from `Z` to `Z` by proving that negation respects the equivalence relation:
`instance : [Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg") Z where   [neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg") :=     [Quotient.lift](The-Type-System/Quotients/#Quotient___lift "Documentation for Quotient.lift") [neg'](The-Type-System/Quotients/#neg___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") <| by⊢ ∀ (a b : Z'), a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b → [neg'](The-Type-System/Quotients/#neg___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [neg'](The-Type-System/Quotients/#neg___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") b       [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") n kn:Z'k:Z'⊢ n [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") k → [neg'](The-Type-System/Quotients/#neg___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [neg'](The-Type-System/Quotients/#neg___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") k equivn:Z'k:Z'equiv:n [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") k⊢ [neg'](The-Type-System/Quotients/#neg___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [neg'](The-Type-System/Quotients/#neg___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") k       [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") nmkk:Z'fst✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")equiv:[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") k⊢ [neg'](The-Type-System/Quotients/#neg___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [neg'](The-Type-System/Quotients/#neg___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") k; [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") kmk.mkfst✝¹:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝¹:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")fst✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")equiv:[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝¹[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝¹[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")⊢ [neg'](The-Type-System/Quotients/#neg___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝¹[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝¹[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [neg'](The-Type-System/Quotients/#neg___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")       [apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") [Quotient.sound](The-Type-System/Quotients/#Quotient___sound "Documentation for Quotient.sound")mk.mk.afst✝¹:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝¹:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")fst✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")equiv:[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝¹[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝¹[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")⊢ [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")snd✝¹[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") fst✝¹[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")snd✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") fst✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")       [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [· ≈ ·, instHasEquivOfSetoid, [Setoid.r](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid.r"), Z.eq] at *mk.mk.afst✝¹:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝¹:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")fst✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")equiv:fst✝¹ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") snd✝ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") snd✝¹ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") fst✝⊢ snd✝¹ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") fst✝ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") fst✝¹ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") snd✝       [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙  `
Similarly, `[Quotient.lift₂](The-Type-System/Quotients/#Quotient___lift___ "Documentation for Quotient.lift₂")` is useful for defining binary functions from a quotient type. Addition is defined point-wise:
`def add' (n k : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") × [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : Z :=   .mk (n.1 + k.1, n.2 + k.2) `
Lifting it to the quotient requires a proof that addition respects the equivalence relation:
`instance : [Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") Z where   [add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add.add") (n : Z) :=     n.[lift₂](The-Type-System/Quotients/#Quotient___lift___ "Documentation for Quotient.lift₂") [add'](The-Type-System/Quotients/#add___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") <| byn:Z⊢ ∀ (a₁ : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (b₁ : Z') (a₂ : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (b₂ : Z'), a₁ [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") a₂ → b₁ [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b₂ → [add'](The-Type-System/Quotients/#add___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") a₁ b₁ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [add'](The-Type-System/Quotients/#add___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") a₂ b₂       [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") n kn✝:Zn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:Z'⊢ ∀ (a₂ : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (b₂ : Z'), n [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") a₂ → k [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b₂ → [add'](The-Type-System/Quotients/#add___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") n k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [add'](The-Type-System/Quotients/#add___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") a₂ b₂ n'n✝:Zn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:Z'n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ ∀ (b₂ : Z'), n [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") n' → k [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b₂ → [add'](The-Type-System/Quotients/#add___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") n k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [add'](The-Type-System/Quotients/#add___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") n' b₂ k'n✝:Zn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:Z'n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k':Z'⊢ n [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") n' → k [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") k' → [add'](The-Type-System/Quotients/#add___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") n k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [add'](The-Type-System/Quotients/#add___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") n' k'       [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") heq heq'n✝:Zn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:Z'n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k':Z'heq:n [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") n'heq':k [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") k'⊢ [add'](The-Type-System/Quotients/#add___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") n k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [add'](The-Type-System/Quotients/#add___-_LPAR_in-Integer-Negation-and-Addition_RPAR_ "Definition of example") n' k'       [apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") [Quotient.sound](The-Type-System/Quotients/#Quotient___sound "Documentation for Quotient.sound")an✝:Zn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k:Z'n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k':Z'heq:n [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") n'heq':k [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") k'⊢ [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")n.[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k.[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") n.[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k.[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")n'.[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k'.[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") n'.[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k'.[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")       [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") na.mkn:Zk:Z'n':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k':Z'heq':k [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") k'fst✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")heq:[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") n'⊢ [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k.[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k.[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")n'.[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k'.[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") n'.[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k'.[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk"); [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") ka.mk.mkn:Zn':[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")k':Z'fst✝¹:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝¹:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")heq:[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") n'fst✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")heq':[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") k'⊢ [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝¹[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝¹[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝¹[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝¹[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")n'.[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k'.[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") n'.[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k'.[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk"); [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") n'a.mk.mk.mkn:Zk':Z'fst✝²:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝²:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")fst✝¹:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝¹:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")heq':[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") k'fst✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")heq:[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝²[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝²[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")⊢ [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝²[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝²[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝¹[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝¹[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝²[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝²[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝¹[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝¹[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv")   [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k'.[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") k'.[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk"); [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") k'a.mk.mk.mk.mkn:Zfst✝³:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝³:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")fst✝²:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝²:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")fst✝¹:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝¹:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")heq:[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝²[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝²[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")heq':[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝²[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝²[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")⊢ [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝³[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝³[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝²[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝²[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝³[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝³[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝²[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝²[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv")   [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝¹[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝¹[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝¹[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝¹[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")fst✝[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") snd✝[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")       [simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic") only [· ≈ ·, instHasEquivOfSetoid, [Setoid.r](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid.r"), Z.eq]a.mk.mk.mk.mkn:Zfst✝³:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝³:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")fst✝²:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝²:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")fst✝¹:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝¹:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")fst✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")snd✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")heq:fst✝³ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") snd✝¹ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") snd✝³ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") fst✝¹heq':fst✝² [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") snd✝ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") snd✝² [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") fst✝⊢ fst✝³ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") fst✝² [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")snd✝¹ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") snd✝[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") snd✝³ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") snd✝² [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")fst✝¹ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") fst✝[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")       [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("CYUwZgBAWg5BBcEAqBPADiBBeCA5AhgC4QDreRAUBaJFAHQgCOEAFAHYQDWC0MAlDwAKAJwD2abBQgQ2dAIwQA1FzoAmCDlnrlneVRrQGjIwDceAUUYBXAJYn8AGxBsAxpnpMIAdwAWIYSBSEAFgDtgQAEYoQdI2bIRirAAeADQQKHwxEADONgC2Eor4wjaEPhAA2kwAukHZKHl54VFZcQmiyWkZyTBd/BB+jFm5BQD6jmGibA4olTVZonkgAOb4QQn4bNnN0dKx8YksqekCR73p/WfnKDD8rQcdgwqDqsP5aOMOk9OzVYy1ewgixWawocWyhE2bkM4MIAGUQIRRDZgDwEUiUbxvH4AkFhOEPENYtkmGZ4DhCaZ9OBoDxUBhwgBFKyiQg2ZzEeiw9HI4DU2h0PLcdg8WACRBQJkstkcwXcUYyfkyFZwCVwQBJhNAggAfTonDQAPggctYKDSSUyYK2kNcmEQuBWtN8/kC0jYjvJWWZrPZ8ToDhsYGI7uWcAAPLqWoD9u0ZFwIExbCYstIXPgSds2ABuCBpjNcFMQfBoNAzCDemV+7KiKxsPnRnLvSoAdoggAkiCDNtKwgAS6csSYA8mAeSi0qPgHRhGlCdUi8QAFSF5YlOtK/DAYBwEXce1EUjkQji2me6Qm9jyJQqORpLRX3SqS2wqF2iAAQU3TpxrqLn5FEvFLAslkAMg0AIIJfy3CAI0iXZozaRIOG4Ng4E4GBCwQx5PEGdCG2LUtZgrX1CDoata3raM8xATMcyo7ZOFo9NqJkGBGPzNDCxGD4JiBH4W3bTtu2tPtsgHOxhwncdEV5KcZyMAFoxXOJgCAA"\))
When the function's result type is a [subsingleton](The-Type-System/Inductive-Types/#--tech-term-subsingleton), `[Quotient.recOnSubsingleton](The-Type-System/Quotients/#Quotient___recOnSubsingleton "Documentation for Quotient.recOnSubsingleton")` or `[Quotient.recOnSubsingleton₂](The-Type-System/Quotients/#Quotient___recOnSubsingleton___ "Documentation for Quotient.recOnSubsingleton₂")` can be used to define the function. Because all elements of a subsingleton are equal, such a function automatically respects the equivalence relation, so there is no proof obligation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quotient.recOnSubsingleton "Permalink")def
```


Quotient.recOnSubsingleton.{u, v} {α : Sort u} {s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α}
  {motive : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s → Sort v}
  [h : ∀ (a : α), [Subsingleton](Type-Classes/Basic-Classes/#Subsingleton___intro "Documentation for Subsingleton") (motive ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s a))]
  (q : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s) (f : (a : α) → motive ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s a)) : motive q


Quotient.recOnSubsingleton.{u, v}
  {α : Sort u} {s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α}
  {motive : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s → Sort v}
  [h :
    ∀ (a : α),
      [Subsingleton](Type-Classes/Basic-Classes/#Subsingleton___intro "Documentation for Subsingleton")
        (motive ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s a))]
  (q : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s)
  (f :
    (a : α) → motive ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s a)) :
  motive q


```

An alternative recursion or induction principle for quotients that can be used when the target type is a subsingleton, in which all elements are equal.
In these cases, the proof that the function respects the quotient's equivalence relation is trivial, so any function can be lifted.
`[Quotient.rec](The-Type-System/Quotients/#Quotient___rec "Documentation for Quotient.rec")` does not assume that the target type is a subsingleton.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quotient.recOnSubsingleton%E2%82%82 "Permalink")def
```


Quotient.recOnSubsingleton₂.{uA, uB, uC} {α : Sort uA} {β : Sort uB}
  {s₁ : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α} {s₂ : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") β}
  {motive : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s₁ → [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s₂ → Sort uC}
  [s :
    ∀ (a : α) (b : β),
      [Subsingleton](Type-Classes/Basic-Classes/#Subsingleton___intro "Documentation for Subsingleton") (motive ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s₁ a) ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s₂ b))]
  (q₁ : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s₁) (q₂ : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s₂)
  (g :
    (a : α) → (b : β) → motive ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s₁ a) ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s₂ b)) :
  motive q₁ q₂


Quotient.recOnSubsingleton₂.{uA, uB, uC}
  {α : Sort uA} {β : Sort uB}
  {s₁ : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α} {s₂ : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") β}
  {motive :
    [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s₁ → [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s₂ → Sort uC}
  [s :
    ∀ (a : α) (b : β),
      [Subsingleton](Type-Classes/Basic-Classes/#Subsingleton___intro "Documentation for Subsingleton")
        (motive ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s₁ a)
          ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s₂ b))]
  (q₁ : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s₁) (q₂ : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s₂)
  (g :
    (a : α) →
      (b : β) →
        motive ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s₁ a)
          ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s₂ b)) :
  motive q₁ q₂


```

An alternative induction or recursion operator for defining binary operations on quotients that can be used when the target type is a subsingleton.
In these cases, the proof that the function respects the quotient's equivalence relation is trivial, so any function can be lifted.
###  4.5.4.3. Proofs About Quotients[🔗](find/?domain=Verso.Genre.Manual.section&name=quotient-proofs "Permalink")
The fundamental tools for proving properties of elements of quotient types are the soundness axiom and the induction principle. The soundness axiom states that if two elements of the underlying type are related by the quotient's equivalence relation, then they are equal in the quotient type. The induction principle follows the structure of recursors for inductive types: in order to prove that a predicate holds all elements of a quotient type, it suffices to prove that it holds for an application of `[Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk")` to each element of the underlying type. Because `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")` is not an [inductive type](The-Type-System/Inductive-Types/#--tech-term-Inductive-types), tactics such as `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")` and `[induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic")` require that `[Quotient.ind](The-Type-System/Quotients/#Quotient___ind "Documentation for Quotient.ind")` be specified explicitly with the `using` modifier.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quotient.sound "Permalink")theorem
```


Quotient.sound.{u} {α : Sort u} {s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α} {a b : α} :
  a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b → [Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s b


Quotient.sound.{u} {α : Sort u}
  {s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α} {a b : α} :
  a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b →
    [Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s b


```

The **quotient axiom** , which asserts the equality of elements related in the setoid.
Because `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")` is built on a lower-level type `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")`, `[Quotient.sound](The-Type-System/Quotients/#Quotient___sound "Documentation for Quotient.sound")` is implemented as a theorem. It is derived from `[Quot.sound](The-Type-System/Quotients/#Quot___sound "Documentation for Quot.sound")`, the soundness axiom for the lower-level quotient type `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quotient.ind "Permalink")theorem
```


Quotient.ind.{u} {α : Sort u} {s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α}
  {motive : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s → Prop} :
  (∀ (a : α), motive ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s a)) → ∀ (q : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s), motive q


Quotient.ind.{u} {α : Sort u}
  {s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α}
  {motive : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s → Prop} :
  (∀ (a : α), motive ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s a)) →
    ∀ (q : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s), motive q


```

A reasoning principle for quotients that allows proofs about quotients to assume that all values are constructed with `[Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk")`.
Proofs About Quotients
Given the definition of integers as a quotient type from the prior examples, `[Quotient.ind](The-Type-System/Quotients/#Quotient___ind "Documentation for Quotient.ind")` and `[Quotient.sound](The-Type-System/Quotients/#Quotient___sound "Documentation for Quotient.sound")` can be used to prove that negation is an additive inverse. First, `[Quotient.ind](The-Type-System/Quotients/#Quotient___ind "Documentation for Quotient.ind")` is used to replace instances of `n` with applications of `[Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk")`. Having done so, the left side of the equality becomes definitionally equal to a single application of `[Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk")`, via unfolding definitions and the computation rule for `[Quotient.lift](The-Type-System/Quotients/#Quotient___lift "Documentation for Quotient.lift")`. This makes `[Quotient.sound](The-Type-System/Quotients/#Quotient___sound "Documentation for Quotient.sound")` applicable, which yields a new goal: to show that both sides are related by the equivalence relation. This is provable using `[simp_arith](Tactic-Proofs/Tactic-Reference/#simp_arith "Documentation for tactic")`.
`theorem Z.add_neg_inverse (n : Z) : n  + (-n) = 0 := byn:Z⊢ n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0   [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") n using [Quotient.ind](The-Type-System/Quotients/#Quotient___ind "Documentation for Quotient.ind")aa✝:Z'⊢ [Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") instSetoid a✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [-](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")[Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") instSetoid a✝ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0   [apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") [Quotient.sound](The-Type-System/Quotients/#Quotient___sound "Documentation for Quotient.sound")a.aa✝:Z'⊢ [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")a✝.[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")a✝.[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") a✝.[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") a✝.[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd") [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")a✝.[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") a✝.[fst](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.fst")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk").[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")0[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") 0[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")   [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") +[arith](The-Simplifier/Configuring-Simplification/#Lean___Meta___Simp___Config___mk "Documentation for Lean.Meta.Simp.Config.arith") [· ≈ ·, instHasEquivOfSetoid, [Setoid.r](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid.r"), eq]All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("CYUwZgBAWg5BBcEAqBPADiBBeCA5AhgC4QDreRAUBaJFAHQgCOEAFAHYQDWC0MAlDwAKAJwD2abBQgQ2dAIwQA1FzoAmCDlnrlneVRrQGjIwDceAUUYBXAJYn8AGxBsAxpnpMIAdwAWIYSBSEAFgDtgQAEYoQdI2bIRirAAeADQQKHwxEADONgC2Eor4wjaEPhAA2kwAukHZKHl54VFZcQmiyWkZyTBd/BB+jFm5BQD6jmGibA4olTVZAOYlbMBBCfhs2c3R0rHxiSyp6QKHven9p2coMPyt+x2DCoOqw/lo4w6T07NVjLW7ECWcVWFDi2UIGzchjBhAAyiBCKIbMAePDEcjeN4/AEgsJwh4hrFskwzPAcATTPpwNAeKgMOEAIpWUSEGzOYj0GFopEggz0PLcdg8WACRBQRnM1nsugCiCjGRUyBsEALOBiuCAJMJoEEAD6dY4aAB8EBlgpQaSSmVBmwhrkwiFwKppvn8gWkyoWkgBTJZbPidAcNjAxA9cAAPHqWgC9u0ZFwIExbCYstJ8Gg0DMID6pf7sqIrCsUzk3hAppmKgB2iCACSIIBW0jCABL4bKWJMAeTA3ORaW7wDowjSBOqECIEAAVEWgYXqNT8MBgHAhdwHWOyARCKKaWSgqbWLIFDp5GktEoVKorTDIfaIABBBfO7Fu0cPoVi0VYLKyQPBwBBBC/FwgCNIh2aM2kSDhuDYOBOBgItwIeTxBjg6NR3TTNsz9Qg6DzAtVlQlwWxALY2AAbggQjiS2ThyMo4iZBgWiiOolDoxGd4JlLb5KirWt6wgJsWzbOxOz7XsER5AchyMf5o2nEErztHhOw3GkOBdHFpFEMBVLJQxZXYNIAAYrTKEBRACJp6HnYBRg9UY4hMfxiX3YUtw4M8WAAWjYAQcCM7YgjokiICsXI2E9TDpWBII0wzWYotzfNC2kdilGKUpykrGs6wbG1m1bawRK7CSewgPspITP4gA"\))
For more specialized use cases, `[Quotient.rec](The-Type-System/Quotients/#Quotient___rec "Documentation for Quotient.rec")`, `[Quotient.recOn](The-Type-System/Quotients/#Quotient___recOn "Documentation for Quotient.recOn")`, and `[Quotient.hrecOn](The-Type-System/Quotients/#Quotient___hrecOn "Documentation for Quotient.hrecOn")` can be used to define dependent functions from a quotient type to a type in any other universe. Stating that a dependent function respects the quotient's equivalence relation requires a means of dealing with the fact that the dependent result type is instantiated with different values from the quotient on each side of the equality. `[Quotient.rec](The-Type-System/Quotients/#Quotient___rec "Documentation for Quotient.rec")` and `[Quotient.recOn](The-Type-System/Quotients/#Quotient___recOn "Documentation for Quotient.recOn")` use the `[Quotient.sound](The-Type-System/Quotients/#Quotient___sound "Documentation for Quotient.sound")` to equate the related elements, inserting the appropriate cast into the statement of equality, while `[Quotient.hrecOn](The-Type-System/Quotients/#Quotient___hrecOn "Documentation for Quotient.hrecOn")` uses heterogeneous equality.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quotient.rec "Permalink")def
```


Quotient.rec.{u, v} {α : Sort u} {s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α}
  {motive : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s → Sort v}
  (f : (a : α) → motive ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s a))
  (h : ∀ (a b : α) (p : a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b), ⋯ ▸ f a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f b) (q : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s) :
  motive q


Quotient.rec.{u, v} {α : Sort u}
  {s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α}
  {motive : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s → Sort v}
  (f : (a : α) → motive ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s a))
  (h :
    ∀ (a b : α) (p : a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b),
      ⋯ ▸ f a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f b)
  (q : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s) : motive q


```

A dependent recursion principle for `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")`. It is analogous to the [recursor](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=recursors) for a structure, and can be used when the resulting type is not necessarily a proposition.
While it is very general, this recursor can be tricky to use. The following simpler alternatives may be easier to use:
  * `[Quotient.lift](The-Type-System/Quotients/#Quotient___lift "Documentation for Quotient.lift")` is useful for defining non-dependent functions.
  * `[Quotient.ind](The-Type-System/Quotients/#Quotient___ind "Documentation for Quotient.ind")` is useful for proving theorems about quotients.
  * `[Quotient.recOnSubsingleton](The-Type-System/Quotients/#Quotient___recOnSubsingleton "Documentation for Quotient.recOnSubsingleton")` can be used whenever the target type is a `[Subsingleton](Type-Classes/Basic-Classes/#Subsingleton___intro "Documentation for Subsingleton")`.
  * `[Quotient.hrecOn](The-Type-System/Quotients/#Quotient___hrecOn "Documentation for Quotient.hrecOn")` uses heterogeneous equality instead of rewriting with `[Quotient.sound](The-Type-System/Quotients/#Quotient___sound "Documentation for Quotient.sound")`.


`[Quotient.recOn](The-Type-System/Quotients/#Quotient___recOn "Documentation for Quotient.recOn")` is a version of this recursor that takes the quotient parameter first.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quotient.recOn "Permalink")def
```


Quotient.recOn.{u, v} {α : Sort u} {s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α}
  {motive : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s → Sort v} (q : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s)
  (f : (a : α) → motive ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s a))
  (h : ∀ (a b : α) (p : a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b), ⋯ ▸ f a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f b) : motive q


Quotient.recOn.{u, v} {α : Sort u}
  {s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α}
  {motive : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s → Sort v}
  (q : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s)
  (f : (a : α) → motive ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s a))
  (h :
    ∀ (a b : α) (p : a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b),
      ⋯ ▸ f a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f b) :
  motive q


```

A dependent recursion principle for `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")`. It is analogous to the [recursor](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=recursors) for a structure, and can be used when the resulting type is not necessarily a proposition.
While it is very general, this recursor can be tricky to use. The following simpler alternatives may be easier to use:
  * `[Quotient.lift](The-Type-System/Quotients/#Quotient___lift "Documentation for Quotient.lift")` is useful for defining non-dependent functions.
  * `[Quotient.ind](The-Type-System/Quotients/#Quotient___ind "Documentation for Quotient.ind")` is useful for proving theorems about quotients.
  * `[Quotient.recOnSubsingleton](The-Type-System/Quotients/#Quotient___recOnSubsingleton "Documentation for Quotient.recOnSubsingleton")` can be used whenever the target type is a `[Subsingleton](Type-Classes/Basic-Classes/#Subsingleton___intro "Documentation for Subsingleton")`.
  * `[Quotient.hrecOn](The-Type-System/Quotients/#Quotient___hrecOn "Documentation for Quotient.hrecOn")` uses heterogeneous equality instead of rewriting with `[Quotient.sound](The-Type-System/Quotients/#Quotient___sound "Documentation for Quotient.sound")`.


`[Quotient.rec](The-Type-System/Quotients/#Quotient___rec "Documentation for Quotient.rec")` is a version of this recursor that takes the quotient parameter last.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quotient.hrecOn "Permalink")def
```


Quotient.hrecOn.{u, v} {α : Sort u} {s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α}
  {motive : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s → Sort v} (q : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s)
  (f : (a : α) → motive ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s a))
  (c : ∀ (a b : α), a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b → f a [≍](Basic-Propositions/Propositional-Equality/#HEq___refl "Documentation for HEq") f b) : motive q


Quotient.hrecOn.{u, v} {α : Sort u}
  {s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α}
  {motive : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s → Sort v}
  (q : [Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient") s)
  (f : (a : α) → motive ([Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s a))
  (c : ∀ (a b : α), a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b → f a [≍](Basic-Propositions/Propositional-Equality/#HEq___refl "Documentation for HEq") f b) :
  motive q


```

A dependent recursion principle for `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")` that uses [heterogeneous equality](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=HEq), analogous to a [recursor](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=recursors) for a structure.
`[Quotient.recOn](The-Type-System/Quotients/#Quotient___recOn "Documentation for Quotient.recOn")` is a version of this recursor that uses `[Eq](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")` instead of `[HEq](Basic-Propositions/Propositional-Equality/#HEq___refl "Documentation for HEq")`.
If two elements of a type are equal in a quotient, then they are related by the setoid's equivalence relation. This property is called `[Quotient.exact](The-Type-System/Quotients/#Quotient___exact "Documentation for Quotient.exact")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quotient.exact "Permalink")theorem
```


Quotient.exact.{u} {α : Sort u} {s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α} {a b : α} :
  [Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s b → a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b


Quotient.exact.{u} {α : Sort u}
  {s : [Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid") α} {a b : α} :
  [Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Quotient.mk](The-Type-System/Quotients/#Quotient___mk "Documentation for Quotient.mk") s b →
    a [≈](The-Type-System/Quotients/#HasEquiv___mk "Documentation for HasEquiv.Equiv") b


```

If two values are equal in a quotient, then they are related by its equivalence relation.
##  4.5.5. Logical Model[🔗](find/?domain=Verso.Genre.Manual.section&name=quotient-model "Permalink")
Like functions and universes, quotient types are a built-in feature of Lean's type system. However, the underlying primitives are based on the somewhat simpler `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")` type rather than on `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")`, and `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")` is defined in terms of `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")`. The primary difference is that `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")` is based on an arbitrary relation, rather than a `[Setoid](The-Type-System/Quotients/#Setoid___mk "Documentation for Setoid")` instance. The provided relation need not be an equivalence relation; the rules that govern `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")` and `[Eq](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")` automatically extend the provided relation into its reflexive, transitive, symmetric closure. When the relation is already an equivalence relation, `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")` should be used instead of `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")` so Lean can make use of the fact that the relation is an equivalence relation.
The fundamental quotient type API consists of `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")`, `[Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk")`, `[Quot.lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift")`, `[Quot.ind](The-Type-System/Quotients/#Quot___ind "Documentation for Quot.ind")`, and `[Quot.sound](The-Type-System/Quotients/#Quot___sound "Documentation for Quot.sound")`. These are used in the same way as their `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")`-based counterparts.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quot "Permalink")primitive
```


Quot.{u} {α : Sort u} (r : α → α → Prop) : Sort u


Quot.{u} {α : Sort u} (r : α → α → Prop) :
  Sort u


```

Low-level quotient types. Quotient types coarsen the propositional equality for a type `α`, so that terms related by some relation `r` are considered equal in `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r`.
Set-theoretically, `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r` can seen as the set of equivalence classes of `α` modulo `r`. Functions from `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r` must prove that they respect `r`: to define a function `f : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r → β`, it is necessary to provide `f' : α → β` and prove that for all `x : α` and `y : α`, `r x y → f' x = f' y`.
`[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")` is a built-in primitive:
  * `[Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk")` places elements of the underlying type `α` into the quotient.
  * `[Quot.lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift")` allows the definition of functions from the quotient to some other type.
  * `[Quot.sound](The-Type-System/Quotients/#Quot___sound "Documentation for Quot.sound")` asserts the equality of elements related by `r`.
  * `[Quot.ind](The-Type-System/Quotients/#Quot___ind "Documentation for Quot.ind")` is used to write proofs about quotients by assuming that all elements are constructed with `[Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk")`.


The relation `r` is not required to be an equivalence relation; the resulting quotient type's equality extends `r` to an equivalence as a consequence of the rules for equality and quotients. When `r` is an equivalence relation, it can be more convenient to use the higher-level type `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quot.mk "Permalink")primitive
```


Quot.mk.{u} {α : Sort u} (r : α → α → Prop) (a : α) : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r


Quot.mk.{u} {α : Sort u}
  (r : α → α → Prop) (a : α) : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r


```

Places an element of a type into the quotient that equates terms according to the provided relation.
Given `v : α` and relation `r : α → α → Prop`, `[Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r v : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r` is like `v`, except all observations of `v`'s value must respect `r`.
`[Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk")` is a built-in primitive:
  * `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")` is the built-in quotient type.
  * `[Quot.lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift")` allows the definition of functions from the quotient to some other type.
  * `[Quot.sound](The-Type-System/Quotients/#Quot___sound "Documentation for Quot.sound")` asserts the equality of elements related by `r`.
  * `[Quot.ind](The-Type-System/Quotients/#Quot___ind "Documentation for Quot.ind")` is used to write proofs about quotients by assuming that all elements are constructed with `[Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk")`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quot.lift "Permalink")primitive
```


Quot.lift.{u, v} {α : Sort u} {r : α → α → Prop} {β : Sort v}
  (f : α → β) (a : ∀ (a b : α), r a b → f a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f b) : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r → β


Quot.lift.{u, v} {α : Sort u}
  {r : α → α → Prop} {β : Sort v}
  (f : α → β)
  (a : ∀ (a b : α), r a b → f a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f b) :
  [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r → β


```

Lifts a function from an underlying type to a function on a quotient, requiring that it respects the quotient's relation.
Given a relation `r : α → α → Prop` and a quotient `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r`, applying a function `f : α → β` requires a proof `a` that `f` respects `r`. In this case, `Quot.lift f a : Quot r → β` computes the same values as `f`.
Lean's type theory includes a [definitional reduction](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=type-theory) from `[Quot.lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift") f h ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r v)` to `f v`.
`[Quot.lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift")` is a built-in primitive:
  * `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")` is the built-in quotient type.
  * `[Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk")` places elements of the underlying type `α` into the quotient.
  * `[Quot.sound](The-Type-System/Quotients/#Quot___sound "Documentation for Quot.sound")` asserts the equality of elements related by `r`
  * `[Quot.ind](The-Type-System/Quotients/#Quot___ind "Documentation for Quot.ind")` is used to write proofs about quotients by assuming that all elements are constructed with `[Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk")`; it is analogous to the [recursor](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=recursors) for a structure.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quot.ind "Permalink")primitive
```


Quot.ind.{u} {α : Sort u} {r : α → α → Prop} {β : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r → Prop}
  (mk : ∀ (a : α), β ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r a)) (q : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r) : β q


Quot.ind.{u} {α : Sort u}
  {r : α → α → Prop} {β : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r → Prop}
  (mk : ∀ (a : α), β ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r a))
  (q : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r) : β q


```

A reasoning principle for quotients that allows proofs about quotients to assume that all values are constructed with `[Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk")`.
`[Quot.rec](The-Type-System/Quotients/#Quot___rec "Documentation for Quot.rec")` is analogous to the [recursor](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=recursors) for a structure, and can be used when the resulting type is not necessarily a proposition.
`[Quot.ind](The-Type-System/Quotients/#Quot___ind "Documentation for Quot.ind")` is a built-in primitive:
  * `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")` is the built-in quotient type.
  * `[Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk")` places elements of the underlying type `α` into the quotient.
  * `[Quot.lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift")` allows the definition of functions from the quotient to some other type.
  * `[Quot.sound](The-Type-System/Quotients/#Quot___sound "Documentation for Quot.sound")` asserts the equality of elements related by `r`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quot.sound "Permalink")axiom
```


Quot.sound.{u} {α : Sort u} {r : α → α → Prop} {a b : α} :
  r a b → [Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r b


Quot.sound.{u} {α : Sort u}
  {r : α → α → Prop} {a b : α} :
  r a b → [Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r b


```

The **quotient axiom** , which asserts the equality of elements related by the quotient's relation.
The relation `r` does not need to be an equivalence relation to use this axiom. When `r` is not an equivalence relation, the quotient is with respect to the equivalence relation generated by `r`.
`[Quot.sound](The-Type-System/Quotients/#Quot___sound "Documentation for Quot.sound")` is part of the built-in primitive quotient type:
  * `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")` is the built-in quotient type.
  * `[Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk")` places elements of the underlying type `α` into the quotient.
  * `[Quot.lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift")` allows the definition of functions from the quotient to some other type.
  * `[Quot.ind](The-Type-System/Quotients/#Quot___ind "Documentation for Quot.ind")` is used to write proofs about quotients by assuming that all elements are constructed with `[Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk")`; it is analogous to the [recursor](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=recursors) for a structure.


[Quotient types](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=quotients) are described in more detail in the Lean Language Reference.
###  4.5.5.1. Quotient Reduction[🔗](find/?domain=Verso.Genre.Manual.section&name=quotient-reduction "Permalink")
In addition to the above constants, Lean's kernel contains a reduction rule for `[Quot.lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift")` that causes it to reduce when used with `[Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk")`, analogous to [ι-reduction](The-Type-System/Inductive-Types/#--tech-term-___-reduction) for inductive types. Given a relation `r` over `α`, a function `f` from `α` to `β`, and a proof `resp` that `f` respects `r`, the term `[Quot.lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift") f resp ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r x)` is [definitionally equal](The-Type-System/#--tech-term-definitional-equality) to `f x`.
`[variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax")   (r : α → α → Prop)   (f : α → β)   (ok : ∀ x y, r x y → f x = f y)   (x : α)  example : [Quot.lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift") f ok ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r x) = f x := [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
###  4.5.5.2. Quotients and Inductive Types[🔗](find/?domain=Verso.Genre.Manual.section&name=quotients-nested-inductives "Permalink")
Because `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")` is not an inductive type, types implemented as quotients may not occur around [nested occurrences](The-Type-System/Inductive-Types/#nested-inductive-types) in inductive type declarations. These types declarations must be rewritten to remove the nested quotient, which can often be done by defining a quotient-free version and then separately defining an equivalence relation that implements the desired equality relation.
Nested Inductive Types and Quotients
The nested inductive type of rose trees nests the recursive occurrence of `[RoseTree](The-Type-System/Quotients/#RoseTree-_LPAR_in-Nested-Inductive-Types-and-Quotients_RPAR_ "Definition of example")` under `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List")`:
`inductive RoseTree (α : Type u) where   | leaf : α → [RoseTree](The-Type-System/Quotients/#RoseTree-_LPAR_in-Nested-Inductive-Types-and-Quotients_RPAR_ "Definition of example") α   | branch : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([RoseTree](The-Type-System/Quotients/#RoseTree-_LPAR_in-Nested-Inductive-Types-and-Quotients_RPAR_ "Definition of example") α) → [RoseTree](The-Type-System/Quotients/#RoseTree-_LPAR_in-Nested-Inductive-Types-and-Quotients_RPAR_ "Definition of example") α `
However, taking a quotient of the `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List")` that identifies all elements in the style of [squash types](The-Type-System/Quotients/#squash-types) causes Lean to reject the declaration:
``(kernel) arg #2 of 'SetTree.branch' contains a non valid occurrence of the datatypes being declared`inductive SetTree (α : Type u) where | leaf : α → [SetTree](The-Type-System/Quotients/#SetTree-_LPAR_in-Nested-Inductive-Types-and-Quotients_RPAR_ "Definition of example") α | branch : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") (fun (xs ys : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([SetTree](The-Type-System/Quotients/#SetTree-_LPAR_in-Nested-Inductive-Types-and-Quotients_RPAR_ "Definition of example") α)) => [True](Basic-Propositions/Truth/#True___intro "Documentation for True")) → [SetTree](The-Type-System/Quotients/#SetTree-_LPAR_in-Nested-Inductive-Types-and-Quotients_RPAR_ "Definition of example") α `
```
(kernel) arg #2 of 'SetTree.branch' contains a non valid occurrence of the datatypes being declared
```

[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABAJQPYGdEBUBOiKAFII3AyAXMjgJ4AOKEAlMgO4AWiBAUMsgD7IANogCGAMwrIygJMI0WXARQke/ZACM8IkFDaSAMsEwxkRDNnyEpzWWYWWSQA"\))
###  4.5.5.3. Low-Level Quotient API[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--The-Type-System--Quotients--Logical-Model--Low-Level-Quotient-API "Permalink")
`[Quot.liftOn](The-Type-System/Quotients/#Quot___liftOn "Documentation for Quot.liftOn")` is an version of `[Quot.lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift")` that takes the quotient type's value first, by analogy to `[Quotient.liftOn](The-Type-System/Quotients/#Quotient___liftOn "Documentation for Quotient.liftOn")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quot.liftOn "Permalink")def
```


Quot.liftOn.{u, v} {α : Sort u} {β : Sort v} {r : α → α → Prop}
  (q : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r) (f : α → β) (c : ∀ (a b : α), r a b → f a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f b) : β


Quot.liftOn.{u, v} {α : Sort u}
  {β : Sort v} {r : α → α → Prop}
  (q : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r) (f : α → β)
  (c : ∀ (a b : α), r a b → f a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f b) : β


```

Lifts a function from an underlying type to a function on a quotient, requiring that it respects the quotient's relation.
Given a relation `r : α → α → Prop` and a quotient's value `q : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r`, applying a `f : α → β` requires a proof `c` that `f` respects `r`. In this case, `[Quot.liftOn](The-Type-System/Quotients/#Quot___liftOn "Documentation for Quot.liftOn") q f h : β` evaluates to the result of applying `f` to the underlying value in `α` from `q`.
`[Quot.liftOn](The-Type-System/Quotients/#Quot___liftOn "Documentation for Quot.liftOn")` is a version of the built-in primitive `[Quot.lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift")` with its parameters re-ordered.
[Quotient types](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=quotients) are described in more detail in the Lean Language Reference.
Lean also provides convenient elimination from `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")` into any subsingleton without further proof obligations, along with dependent elimination principles that correspond to those used for `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quot.recOnSubsingleton "Permalink")def
```


Quot.recOnSubsingleton.{u, v} {α : Sort u} {r : α → α → Prop}
  {motive : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r → Sort v}
  [h : ∀ (a : α), [Subsingleton](Type-Classes/Basic-Classes/#Subsingleton___intro "Documentation for Subsingleton") (motive ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r a))] (q : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r)
  (f : (a : α) → motive ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r a)) : motive q


Quot.recOnSubsingleton.{u, v} {α : Sort u}
  {r : α → α → Prop}
  {motive : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r → Sort v}
  [h :
    ∀ (a : α),
      [Subsingleton](Type-Classes/Basic-Classes/#Subsingleton___intro "Documentation for Subsingleton") (motive ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r a))]
  (q : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r)
  (f : (a : α) → motive ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r a)) :
  motive q


```

An alternative induction principle for quotients that can be used when the target type is a subsingleton, in which all elements are equal.
In these cases, the proof that the function respects the quotient's relation is trivial, so any function can be lifted.
`[Quot.rec](The-Type-System/Quotients/#Quot___rec "Documentation for Quot.rec")` does not assume that the type is a subsingleton.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quot.rec "Permalink")def
```


Quot.rec.{u, v} {α : Sort u} {r : α → α → Prop}
  {motive : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r → Sort v} (f : (a : α) → motive ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r a))
  (h : ∀ (a b : α) (p : r a b), ⋯ ▸ f a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f b) (q : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r) : motive q


Quot.rec.{u, v} {α : Sort u}
  {r : α → α → Prop}
  {motive : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r → Sort v}
  (f : (a : α) → motive ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r a))
  (h :
    ∀ (a b : α) (p : r a b),
      ⋯ ▸ f a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f b)
  (q : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r) : motive q


```

A dependent recursion principle for `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")`. It is analogous to the [recursor](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=recursors) for a structure, and can be used when the resulting type is not necessarily a proposition.
While it is very general, this recursor can be tricky to use. The following simpler alternatives may be easier to use:
  * `[Quot.lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift")` is useful for defining non-dependent functions.
  * `[Quot.ind](The-Type-System/Quotients/#Quot___ind "Documentation for Quot.ind")` is useful for proving theorems about quotients.
  * `[Quot.recOnSubsingleton](The-Type-System/Quotients/#Quot___recOnSubsingleton "Documentation for Quot.recOnSubsingleton")` can be used whenever the target type is a `[Subsingleton](Type-Classes/Basic-Classes/#Subsingleton___intro "Documentation for Subsingleton")`.
  * `[Quot.hrecOn](The-Type-System/Quotients/#Quot___hrecOn "Documentation for Quot.hrecOn")` uses [heterogeneous equality](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=HEq) instead of rewriting with `[Quot.sound](The-Type-System/Quotients/#Quot___sound "Documentation for Quot.sound")`.


`[Quot.recOn](The-Type-System/Quotients/#Quot___recOn "Documentation for Quot.recOn")` is a version of this recursor that takes the quotient parameter first.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quot.recOn "Permalink")def
```


Quot.recOn.{u, v} {α : Sort u} {r : α → α → Prop}
  {motive : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r → Sort v} (q : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r)
  (f : (a : α) → motive ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r a))
  (h : ∀ (a b : α) (p : r a b), ⋯ ▸ f a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f b) : motive q


Quot.recOn.{u, v} {α : Sort u}
  {r : α → α → Prop}
  {motive : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r → Sort v} (q : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r)
  (f : (a : α) → motive ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r a))
  (h :
    ∀ (a b : α) (p : r a b),
      ⋯ ▸ f a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") f b) :
  motive q


```

A dependent recursion principle for `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")` that takes the quotient first. It is analogous to the [recursor](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=recursors) for a structure, and can be used when the resulting type is not necessarily a proposition.
While it is very general, this recursor can be tricky to use. The following simpler alternatives may be easier to use:
  * `[Quot.lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift")` is useful for defining non-dependent functions.
  * `[Quot.ind](The-Type-System/Quotients/#Quot___ind "Documentation for Quot.ind")` is useful for proving theorems about quotients.
  * `[Quot.recOnSubsingleton](The-Type-System/Quotients/#Quot___recOnSubsingleton "Documentation for Quot.recOnSubsingleton")` can be used whenever the target type is a `[Subsingleton](Type-Classes/Basic-Classes/#Subsingleton___intro "Documentation for Subsingleton")`.
  * `[Quot.hrecOn](The-Type-System/Quotients/#Quot___hrecOn "Documentation for Quot.hrecOn")` uses [heterogeneous equality](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=HEq) instead of rewriting with `[Quot.sound](The-Type-System/Quotients/#Quot___sound "Documentation for Quot.sound")`.


`[Quot.rec](The-Type-System/Quotients/#Quot___rec "Documentation for Quot.rec")` is a version of this recursor that takes the quotient parameter last.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Quot.hrecOn "Permalink")def
```


Quot.hrecOn.{u, v} {α : Sort u} {r : α → α → Prop}
  {motive : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r → Sort v} (q : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r)
  (f : (a : α) → motive ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r a))
  (c : ∀ (a b : α), r a b → f a [≍](Basic-Propositions/Propositional-Equality/#HEq___refl "Documentation for HEq") f b) : motive q


Quot.hrecOn.{u, v} {α : Sort u}
  {r : α → α → Prop}
  {motive : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r → Sort v} (q : [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") r)
  (f : (a : α) → motive ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") r a))
  (c : ∀ (a b : α), r a b → f a [≍](Basic-Propositions/Propositional-Equality/#HEq___refl "Documentation for HEq") f b) :
  motive q


```

A dependent recursion principle for `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")` that uses [heterogeneous equality](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=HEq), analogous to a [recursor](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=recursors) for a structure.
`[Quot.recOn](The-Type-System/Quotients/#Quot___recOn "Documentation for Quot.recOn")` is a version of this recursor that uses `[Eq](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")` instead of `[HEq](Basic-Propositions/Propositional-Equality/#HEq___refl "Documentation for HEq")`.
##  4.5.6. Quotients and Function Extensionality[🔗](find/?domain=Verso.Genre.Manual.section&name=quotient-funext "Permalink")
Because Lean's definitional equality includes a computational reduction rule for `[Quot.lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift")`, quotient types are used in the standard library to prove function extensionality, which would need to be an [axiom](Axioms/#axioms) otherwise. This is done by first defining a type of functions quotiented by extensional equality, for which extensional equality holds by definition.
`[variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax") {α : Sort u} {β : α → Sort v}  def extEq (f g : (x : α) → β x) : Prop :=   ∀ x, f x = g x  def ExtFun (α : Sort u) (β : α → Sort v) :=   [Quot](The-Type-System/Quotients/#Quot "Documentation for Quot") (@[extEq](The-Type-System/Quotients/#extEq "Definition of example") α β) `
Extensional functions can be applied just like ordinary functions. Application respects extensional equality by definition: if applying to functions gives equal results, then applying them gives equal results.
`def extApp     (f : [ExtFun](The-Type-System/Quotients/#ExtFun "Definition of example") α β)     (x : α) :     β x :=   f.[lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift") (· x) fun g g' h => byα:Sort uβ:α → Sort vf:[ExtFun](The-Type-System/Quotients/#ExtFun "Definition of example") α βx:αg:(x : α) → β xg':(x : α) → β xh:[extEq](The-Type-System/Quotients/#extEq "Definition of example") g g'⊢ (fun x_1 => x_1 x) g [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") (fun x_1 => x_1 x) g'     [exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic") h xAll goals completed! 🐙 `
To show that two functions that are extensionally equal are in fact equal, it suffices to show that the functions that result from extensionally applying the corresponding extensional functions are equal. This is because
`[extApp](The-Type-System/Quotients/#extApp "Definition of example") ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") _ f)`
is definitionally equal to
`fun x => ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") [extEq](The-Type-System/Quotients/#extEq "Definition of example") f).[lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift") (· x) (fun _ _ h => h x)`
which is definitionally equal to `fun x => f x`, which is definitionally equal (by [η-equivalence](The-Type-System/#--tech-term-___-equivalence)) to `f`. A propositional version of the computation rule for `[Quot.lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift")` would not suffice, because the reducible expression occurs in the body of a function and rewriting by an equality in a function would already require function extensionality.
From here, it is enough to show that the extensional versions of the two functions are equal. This is true due to `[Quot.sound](The-Type-System/Quotients/#Quot___sound "Documentation for Quot.sound")`: the fact that they are in the quotient's equivalence relation is an assumption. This proof is a much more explicit version of the one in the standard library:
`theorem funext'     {f g : (x : α) → β x}     (h : ∀ x, f x = g x) :     f = g := byα:Sort uβ:α → Sort vf:(x : α) → β xg:(x : α) → β xh:∀ (x : α), f x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g x⊢ f [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g   [suffices](Tactic-Proofs/Tactic-Reference/#suffices "Documentation for tactic") [extApp](The-Type-System/Quotients/#extApp "Definition of example") ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") _ f) = [extApp](The-Type-System/Quotients/#extApp "Definition of example") ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") _ g) byα:Sort uβ:α → Sort vf:(x : α) → β xg:(x : α) → β xh:∀ (x : α), f x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g xthis:[extApp](The-Type-System/Quotients/#extApp "Definition of example") ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") [extEq](The-Type-System/Quotients/#extEq "Definition of example") f) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [extApp](The-Type-System/Quotients/#extApp "Definition of example") ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") [extEq](The-Type-System/Quotients/#extEq "Definition of example") g) := ?m.14⊢ f [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g     [unfold](Tactic-Proofs/Tactic-Reference/#unfold "Documentation for tactic") [extApp](The-Type-System/Quotients/#extApp "Definition of example") at thisα:Sort uβ:α → Sort vf:(x : α) → β xg:(x : α) → β xh:∀ (x : α), f x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g xthis:(fun x => [Quot.lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift") (fun x_1 => x_1 x) ⋯ ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") [extEq](The-Type-System/Quotients/#extEq "Definition of example") f)) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") fun x => [Quot.lift](The-Type-System/Quotients/#Quot___lift "Documentation for Quot.lift") (fun x_1 => x_1 x) ⋯ ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") [extEq](The-Type-System/Quotients/#extEq "Definition of example") g) := ?m.14⊢ f [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g     [dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic") at thisα:Sort uβ:α → Sort vf:(x : α) → β xg:(x : α) → β xh:∀ (x : α), f x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g xthis:(fun x => f x) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") fun x => g x := ?m.14⊢ f [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g     [exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic") thisAll goals completed! 🐙   [suffices](Tactic-Proofs/Tactic-Reference/#suffices "Documentation for tactic") [Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") [extEq](The-Type-System/Quotients/#extEq "Definition of example") f = [Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") [extEq](The-Type-System/Quotients/#extEq "Definition of example") g byα:Sort uβ:α → Sort vf:(x : α) → β xg:(x : α) → β xh:∀ (x : α), f x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g xthis:[Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") [extEq](The-Type-System/Quotients/#extEq "Definition of example") f [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") [extEq](The-Type-System/Quotients/#extEq "Definition of example") g := ?m.26⊢ [extApp](The-Type-System/Quotients/#extApp "Definition of example") ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") [extEq](The-Type-System/Quotients/#extEq "Definition of example") f) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [extApp](The-Type-System/Quotients/#extApp "Definition of example") ([Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") [extEq](The-Type-System/Quotients/#extEq "Definition of example") g)     [apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") [congrArg](Basic-Propositions/Propositional-Equality/#congrArg "Documentation for congrArg")hα:Sort uβ:α → Sort vf:(x : α) → β xg:(x : α) → β xh:∀ (x : α), f x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g xthis:[Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") [extEq](The-Type-System/Quotients/#extEq "Definition of example") f [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") [extEq](The-Type-System/Quotients/#extEq "Definition of example") g := ?m.26⊢ [Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") [extEq](The-Type-System/Quotients/#extEq "Definition of example") f [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Quot.mk](The-Type-System/Quotients/#Quot___mk "Documentation for Quot.mk") [extEq](The-Type-System/Quotients/#extEq "Definition of example") g     [exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic") thisAll goals completed! 🐙   [apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") [Quot.sound](The-Type-System/Quotients/#Quot___sound "Documentation for Quot.sound")aα:Sort uβ:α → Sort vf:(x : α) → β xg:(x : α) → β xh:∀ (x : α), f x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") g x⊢ [extEq](The-Type-System/Quotients/#extEq "Definition of example") f g   [exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic") hAll goals completed! 🐙 `
##  4.5.7. Squash Types[🔗](find/?domain=Verso.Genre.Manual.section&name=squash-types "Permalink")
Squash types are a quotient by the relation that relates all elements, transforming it into a [subsingleton](The-Type-System/Inductive-Types/#--tech-term-subsingleton). In other words, if `α` is inhabited, then `[Squash](The-Type-System/Quotients/#Squash "Documentation for Squash") α` has a single element, and if `α` is uninhabited, then `[Squash](The-Type-System/Quotients/#Squash "Documentation for Squash") α` is also uninhabited. Unlike `[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") α`, which is a proposition stating that `α` is inhabited and is thus represented by a dummy value at runtime, `[Squash](The-Type-System/Quotients/#Squash "Documentation for Squash") α` is a type that is represented identically to `α`. Because `[Squash](The-Type-System/Quotients/#Squash "Documentation for Squash") α` is in the same universe as `α`, it is not subject to the restrictions on computing data from propositions.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Squash "Permalink")def
```


Squash.{u} (α : Sort u) : Sort u


Squash.{u} (α : Sort u) : Sort u


```

The quotient of `α` by the universal relation. The elements of `[Squash](The-Type-System/Quotients/#Squash "Documentation for Squash") α` are those of `α`, but all of them are equal and cannot be distinguished.
`[Squash](The-Type-System/Quotients/#Squash "Documentation for Squash") α` is a `[Subsingleton](Type-Classes/Basic-Classes/#Subsingleton___intro "Documentation for Subsingleton")`: it is empty if `α` is empty, otherwise it has just one element. It is the “universal `[Subsingleton](Type-Classes/Basic-Classes/#Subsingleton___intro "Documentation for Subsingleton")`” mapped from `α`.
`[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") α` also has these properties. It is a proposition, which means that its elements (i.e. proofs) are erased from compiled code and represented by a dummy value. `[Squash](The-Type-System/Quotients/#Squash "Documentation for Squash") α` is a `Type u`, and its representation in compiled code is identical to that of `α`.
Consequently, `[Squash.lift](The-Type-System/Quotients/#Squash___lift "Documentation for Squash.lift")` may extract an `α` value into any subsingleton type `β`, while `Nonempty.rec` can only do the same when `β` is a proposition.
`[Squash](The-Type-System/Quotients/#Squash "Documentation for Squash")` is defined in terms of `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")`, so `[Squash](The-Type-System/Quotients/#Squash "Documentation for Squash")` can be used when a `[Quotient](The-Type-System/Quotients/#Quotient "Documentation for Quotient")` argument is expected.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Squash.mk "Permalink")def
```


Squash.mk.{u} {α : Sort u} (x : α) : [Squash](The-Type-System/Quotients/#Squash "Documentation for Squash") α


Squash.mk.{u} {α : Sort u} (x : α) :
  [Squash](The-Type-System/Quotients/#Squash "Documentation for Squash") α


```

Places a value into its squash type, in which it cannot be distinguished from any other.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Squash.lift "Permalink")def
```


Squash.lift.{u_1, u_2} {α : Sort u_1} {β : Sort u_2} [[Subsingleton](Type-Classes/Basic-Classes/#Subsingleton___intro "Documentation for Subsingleton") β]
  (s : [Squash](The-Type-System/Quotients/#Squash "Documentation for Squash") α) (f : α → β) : β


Squash.lift.{u_1, u_2} {α : Sort u_1}
  {β : Sort u_2} [[Subsingleton](Type-Classes/Basic-Classes/#Subsingleton___intro "Documentation for Subsingleton") β]
  (s : [Squash](The-Type-System/Quotients/#Squash "Documentation for Squash") α) (f : α → β) : β


```

Extracts a squashed value into any subsingleton type.
If `β` is a subsingleton, a function `α → β` cannot distinguish between elements of `α` and thus automatically respects the universal relation that `[Squash](The-Type-System/Quotients/#Squash "Documentation for Squash")` quotients with.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Squash.ind "Permalink")theorem
```


Squash.ind.{u} {α : Sort u} {motive : [Squash](The-Type-System/Quotients/#Squash "Documentation for Squash") α → Prop}
  (h : ∀ (a : α), motive ([Squash.mk](The-Type-System/Quotients/#Squash___mk "Documentation for Squash.mk") a)) (q : [Squash](The-Type-System/Quotients/#Squash "Documentation for Squash") α) : motive q


Squash.ind.{u} {α : Sort u}
  {motive : [Squash](The-Type-System/Quotients/#Squash "Documentation for Squash") α → Prop}
  (h : ∀ (a : α), motive ([Squash.mk](The-Type-System/Quotients/#Squash___mk "Documentation for Squash.mk") a))
  (q : [Squash](The-Type-System/Quotients/#Squash "Documentation for Squash") α) : motive q


```

A reasoning principle that allows proofs about squashed types to assume that all values are constructed with `[Squash.mk](The-Type-System/Quotients/#Squash___mk "Documentation for Squash.mk")`.
[←4.4. Inductive Types](The-Type-System/Inductive-Types/#inductive-types "4.4. Inductive Types")[5. Source Files and Modules→](Source-Files-and-Modules/#files "5. Source Files and Modules")

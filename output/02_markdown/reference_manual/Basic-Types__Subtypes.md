[←20.19. Maps and Sets](Basic-Types/Maps-and-Sets/#maps "20.19. Maps and Sets")[20.21. Lazy Computations→](Basic-Types/Lazy-Computations/#Thunk "20.21. Lazy Computations")
#  20.20. Subtypes[🔗](find/?domain=Verso.Genre.Manual.section&name=Subtype "Permalink")
The structure `[Subtype](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")` represents the elements of a type that satisfy some predicate. They are used pervasively both in mathematics and in programming; in mathematics, they are used similarly to subsets, while in programming, they allow information that is known about a value to be represented in a way that is visible to Lean's logic.
Syntactically, an element of a `[Subtype](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")` resembles a tuple of the base type's element and the proof that it satisfies the proposition. They differ from dependent pair types (`[Sigma](Basic-Types/Tuples/#Sigma___mk "Documentation for Sigma")`) in that the second element is a proof of a proposition rather than data, and from existential quantification in that the entire `[Subtype](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")` is a type rather than a proposition. Even though they are pairs syntactically, `[Subtype](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")` should really be thought of as elements of the base type with associated proof obligations.
Subtypes are [trivial wrappers](The-Type-System/Inductive-Types/#inductive-types-trivial-wrappers). They are thus represented identically to the base type in compiled code.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subtype.val "Permalink")structure
```


Subtype.{u} {α : Sort u} (p : α → Prop) : Sort (max 1 u)


Subtype.{u} {α : Sort u} (p : α → Prop) :
  Sort (max 1 u)


```

All the elements of a type that satisfy a predicate.
`[Subtype](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") p`, usually written `{ x : α // p x }` or `{ x // p x }`, contains all elements `x : α` for which `p x` is true. Its constructor is a pair of the value and the proof that it satisfies the predicate. In run-time code, `{ x : α // p x }` is represented identically to `α`.
There is a coercion from `{ x : α // p x }` to `α`, so elements of a subtype may be used where the underlying type is expected.
Examples:
  * `{ n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") // n % 2 = 0 }` is the type of even numbers.
  * `{ xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") // xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") = 5 }` is the type of arrays with five `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`s.
  * Given `xs : List α`, `List { x : α // x ∈ xs }` is the type of lists in which all elements are contained in `xs`.


Conventions for notations in identifiers:
  * The recommended spelling of `{ x // p x }` in identifiers is `subtype`.


#  Constructor

```
[Subtype.mk](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk").{u}
```

#  Fields

```
val : α
```

The value in the underlying type that satisfies the predicate.

```
property : p self.[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val")
```

The proof that `val` satisfies the predicate `p`.
syntaxSubtypes

```
term ::= ...
    | 


All the elements of a type that satisfy a predicate.


Subtype p, usually written { x : α // p x } or { x // p x }, contains all elements x : α for
which p x is true. Its constructor is a pair of the value and the proof that it satisfies the
predicate. In run-time code, { x : α // p x } is represented identically to α.


There is a coercion from { x : α // p x } to α, so elements of a subtype may be used where the
underlying type is expected.


Examples:




  * 
{ n : Nat // n % 2 = 0 } is the type of even numbers.


  * 
{ xs : Array String // xs.size = 5 } is the type of arrays with five Strings.


  * Given xs : List α, List { x : α // x ∈ xs } is the type of lists in which all elements are
contained in xs.




Conventions for notations in identifiers:




  * The recommended spelling of { x // p x } in identifiers is subtype.




{ ident : term // term }
```

`{ x : α // p }` is a notation for `[Subtype](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") fun (x : α) => p`.
The type ascription may be omitted:

```
term ::= ...
    | 


All the elements of a type that satisfy a predicate.


Subtype p, usually written { x : α // p x } or { x // p x }, contains all elements x : α for
which p x is true. Its constructor is a pair of the value and the proof that it satisfies the
predicate. In run-time code, { x : α // p x } is represented identically to α.


There is a coercion from { x : α // p x } to α, so elements of a subtype may be used where the
underlying type is expected.


Examples:




  * 
{ n : Nat // n % 2 = 0 } is the type of even numbers.


  * 
{ xs : Array String // xs.size = 5 } is the type of arrays with five Strings.


  * Given xs : List α, List { x : α // x ∈ xs } is the type of lists in which all elements are
contained in xs.




Conventions for notations in identifiers:




  * The recommended spelling of { x // p x } in identifiers is subtype.




{ ident // term }
```

`{ x // p }` is a notation for `[Subtype](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") fun (x : _) => p`.
Due to [proof irrelevance](The-Type-System/#--tech-term-proof-irrelevance) and [η-equality](The-Type-System/#--tech-term-___-equivalence), two elements of a subtype are definitionally equal when the elements of the base type are definitionally equal. In a proof, the `[ext](Tactic-Proofs/Tactic-Reference/#ext "Documentation for tactic")` tactic can be used to transform a goal of equality of elements of a subtype into equality of their values.
Definitional Equality of Subtypes
The non-empty strings `[s1](Basic-Types/Subtypes/#s1-_LPAR_in-Definitional-Equality-of-Subtypes_RPAR_ "Definition of example")` and `[s2](Basic-Types/Subtypes/#s2-_LPAR_in-Definitional-Equality-of-Subtypes_RPAR_ "Definition of example")` are definitionally equal despite the fact that their embedded proof terms are different. No case splitting is needed in order to prove that they are equal.
`def NonEmptyString := { x : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") // x ≠ "" }  def s1 : [NonEmptyString](Basic-Types/Subtypes/#NonEmptyString-_LPAR_in-Definitional-Equality-of-Subtypes_RPAR_ "Definition of example") :=   ⟨"equal", ne_of_beq_false [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")⟩  def s2 : [NonEmptyString](Basic-Types/Subtypes/#NonEmptyString-_LPAR_in-Definitional-Equality-of-Subtypes_RPAR_ "Definition of example") where   [val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val") := "equal"   [property](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.property") :=     fun h =>       List.cons_ne_nil _ _ (``String.data_eq_of_eq` has been deprecated: Use `String.toList_inj` instead  Note: The updated constant has a different type:   ∀ {s₁ s₂ : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}, s₁.toList [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") s₂.toList [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") s₁ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") s₂ instead of   ∀ {a b : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}, a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b → a.toList [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b.toList`String.data_eq_of_eq h) theorem s1_eq_s2 : [s1](Basic-Types/Subtypes/#s1-_LPAR_in-Definitional-Equality-of-Subtypes_RPAR_ "Definition of example") = [s2](Basic-Types/Subtypes/#s2-_LPAR_in-Definitional-Equality-of-Subtypes_RPAR_ "Definition of example") := by⊢ [s1](Basic-Types/Subtypes/#s1-_LPAR_in-Definitional-Equality-of-Subtypes_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s2](Basic-Types/Subtypes/#s2-_LPAR_in-Definitional-Equality-of-Subtypes_RPAR_ "Definition of example") [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("CYUwZgBAcg9gdgUQLYAcAuBPAymgTgSzgHMIAuAXggG8IAPMiHA4iAelbokAMiCAIl4gBfAFDDQkAM4BGBrESpMTQiQrCIEQBfkvEAEcArgEMANrwA0EOCAD6MMFYBGuq2GMSQEXGCOBL8lHiIEgBMsvDI6Nh4yhAA7gAWILggahAAbsZklNr6xrzJKLgwKAmYGcnqYHpwELEQ5AB8ZeoQADL4EmgAdADG8BJWlv34RhBWIxAAFErEHcAGaAZWTraLOtUAlKJo8TCJSAFSK1ZBDNK1AcEUEPYYHl5AA"\))
Extensional Equality of Subtypes
The non-empty strings `[s1](Basic-Types/Subtypes/#s1-_LPAR_in-Extensional-Equality-of-Subtypes_RPAR_ "Definition of example")` and `[s2](Basic-Types/Subtypes/#s2-_LPAR_in-Extensional-Equality-of-Subtypes_RPAR_ "Definition of example")` are definitionally equal. Ignoring that fact, the equality of the embedded strings can be used to prove that they are equal. The `[ext](Tactic-Proofs/Tactic-Reference/#ext "Documentation for tactic")` tactic transforms a goal that consists of equality of non-empty strings into a goal that consists of equality of the strings.
`abbrev NonEmptyString := { x : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") // x ≠ "" }  def s1 : [NonEmptyString](Basic-Types/Subtypes/#NonEmptyString-_LPAR_in-Extensional-Equality-of-Subtypes_RPAR_ "Definition of example") :=   ⟨"equal", ne_of_beq_false [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")⟩  def s2 : [NonEmptyString](Basic-Types/Subtypes/#NonEmptyString-_LPAR_in-Extensional-Equality-of-Subtypes_RPAR_ "Definition of example") where   [val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val") := "equal"   [property](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.property") :=     fun h =>       List.cons_ne_nil _ _ (``String.data_eq_of_eq` has been deprecated: Use `String.toList_inj` instead  Note: The updated constant has a different type:   ∀ {s₁ s₂ : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}, s₁.toList [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") s₂.toList [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") s₁ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") s₂ instead of   ∀ {a b : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}, a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b → a.toList [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b.toList`String.data_eq_of_eq h) theorem s1_eq_s2 : [s1](Basic-Types/Subtypes/#s1-_LPAR_in-Extensional-Equality-of-Subtypes_RPAR_ "Definition of example") = [s2](Basic-Types/Subtypes/#s2-_LPAR_in-Extensional-Equality-of-Subtypes_RPAR_ "Definition of example") := by⊢ [s1](Basic-Types/Subtypes/#s1-_LPAR_in-Extensional-Equality-of-Subtypes_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [s2](Basic-Types/Subtypes/#s2-_LPAR_in-Extensional-Equality-of-Subtypes_RPAR_ "Definition of example") [ext](Tactic-Proofs/Tactic-Reference/#ext "Documentation for tactic")a.h.h.ai✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:[Char](Basic-Types/Characters/#Char___mk "Documentation for Char")⊢ [s1](Basic-Types/Subtypes/#s1-_LPAR_in-Extensional-Equality-of-Subtypes_RPAR_ "Definition of example").[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").toList[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")i✝[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a✝ [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") [s2](Basic-Types/Subtypes/#s2-_LPAR_in-Extensional-Equality-of-Subtypes_RPAR_ "Definition of example").[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").toList[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")i✝[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a✝ [dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic") only [[s1](Basic-Types/Subtypes/#s1-_LPAR_in-Extensional-Equality-of-Subtypes_RPAR_ "Definition of example"), [s2](Basic-Types/Subtypes/#s2-_LPAR_in-Extensional-Equality-of-Subtypes_RPAR_ "Definition of example")]a.h.h.ai✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:[Char](Basic-Types/Characters/#Char___mk "Documentation for Char")⊢ "equal".toList[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")i✝[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a✝ [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") "equal".toList[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")i✝[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") a✝ [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("IYIxCcFMDcAIDkD2A7AogWwA4BcCeBlbcAS2QHNYAuAXlgG9YAPK2Qk82Aek6dkAMiWACJBsAL4AocQBNIAM1gBnAIwskaLHjakKNcbFiAL8kGQAjgFdgAG0EAaWMkgB9RLMchTj2VYWRY4WZaAl+SSMvIKAEyqKBg4BETasADuABaQUHqw0FZUtMbmVoIZmOCImGl4ORn6smbIsMmw1AB8VfqwADLECtgAdADGKAqODsPElrCOE7AAFFrkPVLA2MCOHi6rJvUAlJLYqYhQ6IpKG44RLMqNipE0sCC4GZCM2BlSCsRYsCiWuLAA2so7BEALoZfyWIA"\))
There is a coercion from a subtype to its base type. This allows subtypes to be used in positions where the base type is expected, essentially erasing the proof that the value satisfies the predicate.
Subtype Coercions
Elements of subtypes can be coerced to their base type. Here, `[nine](Basic-Types/Subtypes/#nine-_LPAR_in-Subtype-Coercions_RPAR_ "Definition of example")` is coerced from a subtype of `Nat` that contains multiples of `3` to `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`.
`abbrev DivBy3 := { x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") // x % 3 = 0 }  def nine : [DivBy3](Basic-Types/Subtypes/#DivBy3-_LPAR_in-Subtype-Coercions_RPAR_ "Definition of example") := ⟨9, by⊢ 9 [%](Type-Classes/Basic-Classes/#HMod___mk "Documentation for HMod.hMod") 3 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙⟩  set_option [eval.type](Interacting-with-Lean/#eval___type "Documentation for option eval.type") true [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") `10 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") [nine](Basic-Types/Subtypes/#nine-_LPAR_in-Subtype-Coercions_RPAR_ "Definition of example") `
```
10 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

[Live ↪](javascript:openLiveLink\("IYIxCcFMDcAIBECW0BCBPAzLAXAXlgN6wAeOsAcsAC6wD0tJsApLFvgAywC+AUDwCaQAZrAB2iUZDJJUmHPkAX5AE4ANLBBpY4IQBtAl+R8AzpCoB9APYAHKonOjYMYDoB0VNJalVwAVykSeAMSOOhTUzobeAMaRYhKQQA"\))
[←20.19. Maps and Sets](Basic-Types/Maps-and-Sets/#maps "20.19. Maps and Sets")[20.21. Lazy Computations→](Basic-Types/Lazy-Computations/#Thunk "20.21. Lazy Computations")

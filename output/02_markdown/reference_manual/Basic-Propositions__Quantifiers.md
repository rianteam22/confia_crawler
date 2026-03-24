[←19.2. Logical Connectives](Basic-Propositions/Logical-Connectives/#The-Lean-Language-Reference--Basic-Propositions--Logical-Connectives "19.2. Logical Connectives")[19.4. Propositional Equality→](Basic-Propositions/Propositional-Equality/#propositional-equality "19.4. Propositional Equality")
#  19.3. Quantifiers[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Propositions--Quantifiers "Permalink")
Just as implication is implemented as ordinary function types in `Prop`, universal quantification is implemented as dependent function types in `Prop`. Because `Prop` is [impredicative](The-Type-System/Universes/#--tech-term-impredicative), any function type in which the [codomain](The-Type-System/Functions/#--tech-term-codomain) is a `Prop` is itself a `Prop`, even if the [domain](The-Type-System/Functions/#--tech-term-domain) is a `Type`. The typing rules for dependent functions precisely match the introduction and elimination rules for universal quantification: if a predicate holds for any arbitrarily chosen element of a type, then it holds universally. If a predicate holds universally, then it can be instantiated to a proof for any individual.
syntaxUniversal Quantification

```
term ::= ...
    | ∀ ident ident* (: term)?, term
```

```
term ::= ...
    | forall ident ident* (: term)?, term
```

```
term ::= ...
    | ∀ (ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole) | bracketedBinder) (ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole) | bracketedBinder)*, term
```

```
term ::= ...
    | forall (ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole) | bracketedBinder) (ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole) | bracketedBinder)*, term
```

Universal quantifiers bind one or more variables, which are then in scope in the final term. The identifiers may also be `_`. With parenthesized type annotations, multiple bound variables may have different types, while the unparenthesized variant requires that all have the same type.
Even though universal quantifiers are represented by functions, their proofs should not be thought of as computations. Because of proof irrelevance and the elimination restriction for propositions, there's no way to actually compute data using these proofs. As a result, they are free to use reasoning principles that are not readily computed, such as the classical Axiom of Choice.
Existential quantification is implemented as a structure that is similar to `[Subtype](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")` and `[Sigma](Basic-Types/Tuples/#Sigma___mk "Documentation for Sigma")`: it contains a _witness_ , which is a value that satisfies the predicate, along with a proof that the witness does in fact satisfy the predicate. In other words, it is a form of dependent pair type. Unlike both `[Subtype](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")` and `[Sigma](Basic-Types/Tuples/#Sigma___mk "Documentation for Sigma")`, it is a [proposition](The-Type-System/Propositions/#--tech-term-Propositions); this means that programs cannot in general use a proof of an existential statement to obtain a value that satisfies the predicate.
When writing a proof, the `[exists](Tactic-Proofs/Tactic-Reference/#exists "Documentation for tactic")` tactic allows one (or more) witness(es) to be specified for a (potentially nested) existential statement. The `[constructor](Tactic-Proofs/Tactic-Reference/#constructor "Documentation for tactic")` tactic, on the other hand, creates a [metavariable](Tactic-Proofs/Reading-Proof-States/#--tech-term-metavariables) for the witness; providing a proof of the predicate may solve the metavariable as well. The components of an existential assumption can be made available individually by pattern matching with `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` or `[match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic")`, as well as by using `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic")` or `[rcases](Tactic-Proofs/Tactic-Reference/#rcases "Documentation for tactic")`.
Proving Existential Statements
When proving that there exists some natural number that is the sum of four and five, the `[exists](Tactic-Proofs/Tactic-Reference/#exists "Documentation for tactic")` tactic expects the sum to be provided, constructing the equality proof using `[trivial](Tactic-Proofs/Tactic-Reference/#trivial "Documentation for tactic")`:
`theorem ex_four_plus_five : ∃ n, 4 + 5 = n := by⊢ [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") n[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") 4 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 5 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n   [exists](Tactic-Proofs/Tactic-Reference/#exists "Documentation for tactic") 9All goals completed! 🐙 `
The `[constructor](Tactic-Proofs/Tactic-Reference/#constructor "Documentation for tactic")` tactic, on the other hand, expects a proof. The `[rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")` tactic causes the sum to be determined as a side effect of checking definitional equality.
`theorem ex_four_plus_five' : ∃ n, 4 + 5 = n := by⊢ [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") n[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") 4 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 5 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n   [constructor](Tactic-Proofs/Tactic-Reference/#constructor "Documentation for tactic")h⊢ 4 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 5 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ?ww⊢ [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("C4Cwpg9gTmC2AEYAeB9AZhArlFAHANpgM7oCWAbmPAFzyDARPAHYA08ALPANTwCs8AvExqCARgE8AUPERJSRYEXgBOCRNCQYCZOiw4CxMpQDkNek1YdufQY2HxxU+AGMIjeVExPg0R1DT4gA"\))
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Exists.intro "Permalink")inductive predicate
```


Exists.{u} {α : Sort u} (p : α → Prop) : Prop


Exists.{u} {α : Sort u} (p : α → Prop) :
  Prop


```

Existential quantification. If `p : α → Prop` is a predicate, then `∃ x : α, p x` asserts that there is some `x` of type `α` such that `p x` holds. To create an existential proof, use the `[exists](Tactic-Proofs/Tactic-Reference/#exists "Documentation for tactic")` tactic, or the anonymous constructor notation `⟨x, h⟩`. To unpack an existential, use `[cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") h` where `h` is a proof of `∃ x : α, p x`, or `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic") ⟨x, hx⟩ := h` where `.
Because Lean has proof irrelevance, any two proofs of an existential are definitionally equal. One consequence of this is that it is impossible to recover the witness of an existential from the mere fact of its existence. For example, the following does not compile:

```
example (h : ∃ x : Nat, x = x) : Nat :=
  let ⟨x, _⟩ := h  -- fail, because the goal is `Nat : Type`
  x

```

The error message `recursor 'Exists.casesOn' can only eliminate into Prop` means that this only works when the current goal is another proposition:
`example (h : ∃ x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"), x = x) : [True](Basic-Propositions/Truth/#True___intro "Documentation for True") :=   let ⟨x, _⟩ := h  -- ok, because the goal is `True : Prop`   trivial `
#  Constructors

```
intro.{u} {α : Sort u} {p : α → Prop} (w : α) (h : p w) :
  [Exists](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") p
```

Existential introduction. If `a : α` and `h : p a`, then `⟨a, h⟩` is a proof that `∃ x : α, p x`.
syntaxExistential Quantification

```
term ::= ...
    | ∃ 


binderIdent matches an ident or a _. It is used for identifiers in binding
position, where _ means that the value should be left unnamed and inaccessible.


ident 


binderIdent matches an ident or a _. It is used for identifiers in binding
position, where _ means that the value should be left unnamed and inaccessible.


ident* (: term)?, term
```

```
term ::= ...
    | exists 


binderIdent matches an ident or a _. It is used for identifiers in binding
position, where _ means that the value should be left unnamed and inaccessible.


ident 


binderIdent matches an ident or a _. It is used for identifiers in binding
position, where _ means that the value should be left unnamed and inaccessible.


ident* (: term)?, term
```

```
term ::= ...
    | ∃ bracketedExplicitBinders bracketedExplicitBinders*, term
```

```
term ::= ...
    | exists bracketedExplicitBinders bracketedExplicitBinders*, term
```

Existential quantifiers bind one or more variables, which are then in scope in the final term. The identifiers may also be `_`. With parenthesized type annotations, multiple bound variables may have different types, while the unparenthesized variant requires that all have the same type. If more than one variable is bound, then the result is multiple instances of `[Exists](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists")`, nested to the right.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Exists.choose "Permalink")def
```


Exists.choose.{u_1} {α : Sort u_1} {p : α → Prop} (P : [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") p a) : α


Exists.choose.{u_1} {α : Sort u_1}
  {p : α → Prop} (P : [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") p a) : α


```

Extract an element from an existential statement, using `Classical.choose`.
[←19.2. Logical Connectives](Basic-Propositions/Logical-Connectives/#The-Lean-Language-Reference--Basic-Propositions--Logical-Connectives "19.2. Logical Connectives")[19.4. Propositional Equality→](Basic-Propositions/Propositional-Equality/#propositional-equality "19.4. Propositional Equality")

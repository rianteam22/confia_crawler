[←15.2. Rewrite Rules](The-Simplifier/Rewrite-Rules/#simp-rewrites "15.2. Rewrite Rules")[15.4. Simp Normal Forms→](The-Simplifier/Simp-Normal-Forms/#simp-normal-forms "15.4. Simp Normal Forms")
#  15.3. Simp sets[🔗](find/?domain=Verso.Genre.Manual.section&name=simp-sets "Permalink")
A collection of rules used by the simplifier is called a _simp set_. A simp set is specified in terms of modifications from a _default simp set_. These modifications can include adding rules, removing rules, or adding a set of rules. The `only` modifier to the `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` tactic causes it to start with an empty simp set, rather than the default one. Rules are added to the default simp set using the `simp` attribute.
attributeRegistering `simp` Lemmas
The `simp` attribute adds a declaration to the default simp set. If the declaration is a definition, the definition is marked for unfolding; if it is a theorem, then the theorem is registered as a rewrite rule.

```
attr ::= ...
    | 


Theorems tagged with the simp attribute are used by the simplifier
(i.e., the simp tactic, and its variants) to simplify expressions occurring in your goals.
We call theorems tagged with the simp attribute "simp theorems" or "simp lemmas".
Lean maintains a database/index containing all active simp theorems.
Here is an example of a simp theorem.


```
@[simp] theorem ne_eq (a b : α) : (a ≠ b) = Not (a = b) := rfl

```

This simp theorem instructs the simplifier to replace instances of the term `a ≠ b` (e.g. `x + 0 ≠ y`) with `Not (a = b)` (e.g., `Not (x + 0 = y)`). The simplifier applies simp theorems in one direction only: if `A = B` is a simp theorem, then `simp` replaces `A`s with `B`s, but it doesn't replace `B`s with `A`s. Hence a simp theorem should have the property that its right-hand side is "simpler" than its left-hand side. In particular, `=` and `↔` should not be viewed as symmetric operators in this situation. The following would be a terrible simp theorem (if it were even allowed):

```
@[simp] lemma mul_right_inv_bad (a : G) : 1 = a * a⁻¹ := ...

```

Replacing 1 with a * a⁻¹ is not a sensible default direction to travel. Even worse would be a theorem that causes expressions to grow without bound, causing simp to loop forever.
By default the simplifier applies `simp` theorems to an expression `e` after its sub-expressions have been simplified. We say it performs a bottom-up simplification. You can instruct the simplifier to apply a theorem before its sub-expressions have been simplified by using the modifier `↓`. Here is an example

```
@[simp↓] theorem not_and_eq (p q : Prop) : (¬ (p ∧ q)) = (¬p ∨ ¬q) :=

```

You can instruct the simplifier to rewrite the lemma from right-to-left:

```
attribute @[simp ←] and_assoc

```

When multiple simp theorems are applicable, the simplifier uses the one with highest priority. The equational theorems of functions are applied at very low priority (100 and below). If there are several with the same priority, it is uses the "most recent one". Example:

```
@[simp high] theorem cond_true (a b : α) : cond true a b = a := rfl
@[simp low+1] theorem or_true (p : Prop) : (p ∨ True) = True :=
  propext <| Iff.intro (fun _ => trivial) (fun _ => Or.inr trivial)
@[simp 100] theorem ite_self {d : Decidable c} (a : α) : ite c a a = a := by
  cases d <;> rfl

```

`simp
```

```
attr ::= ...
    | 


Theorems tagged with the simp attribute are used by the simplifier
(i.e., the simp tactic, and its variants) to simplify expressions occurring in your goals.
We call theorems tagged with the simp attribute "simp theorems" or "simp lemmas".
Lean maintains a database/index containing all active simp theorems.
Here is an example of a simp theorem.


```
@[simp] theorem ne_eq (a b : α) : (a ≠ b) = Not (a = b) := rfl

```

This simp theorem instructs the simplifier to replace instances of the term `a ≠ b` (e.g. `x + 0 ≠ y`) with `Not (a = b)` (e.g., `Not (x + 0 = y)`). The simplifier applies simp theorems in one direction only: if `A = B` is a simp theorem, then `simp` replaces `A`s with `B`s, but it doesn't replace `B`s with `A`s. Hence a simp theorem should have the property that its right-hand side is "simpler" than its left-hand side. In particular, `=` and `↔` should not be viewed as symmetric operators in this situation. The following would be a terrible simp theorem (if it were even allowed):

```
@[simp] lemma mul_right_inv_bad (a : G) : 1 = a * a⁻¹ := ...

```

Replacing 1 with a * a⁻¹ is not a sensible default direction to travel. Even worse would be a theorem that causes expressions to grow without bound, causing simp to loop forever.
By default the simplifier applies `simp` theorems to an expression `e` after its sub-expressions have been simplified. We say it performs a bottom-up simplification. You can instruct the simplifier to apply a theorem before its sub-expressions have been simplified by using the modifier `↓`. Here is an example

```
@[simp↓] theorem not_and_eq (p q : Prop) : (¬ (p ∧ q)) = (¬p ∨ ¬q) :=

```

You can instruct the simplifier to rewrite the lemma from right-to-left:

```
attribute @[simp ←] and_assoc

```

When multiple simp theorems are applicable, the simplifier uses the one with highest priority. The equational theorems of functions are applied at very low priority (100 and below). If there are several with the same priority, it is uses the "most recent one". Example:

```
@[simp high] theorem cond_true (a b : α) : cond true a b = a := rfl
@[simp low+1] theorem or_true (p : Prop) : (p ∨ True) = True :=
  propext <| Iff.intro (fun _ => trivial) (fun _ => Or.inr trivial)
@[simp 100] theorem ite_self {d : Decidable c} (a : α) : ite c a a = a := by
  cases d <;> rfl

```

`simp `
 
Use this rewrite rule after entering the subterms 
 
`↑ (← ? | <- ?)
```

```
attr ::= ...
    | 


Theorems tagged with the simp attribute are used by the simplifier
(i.e., the simp tactic, and its variants) to simplify expressions occurring in your goals.
We call theorems tagged with the simp attribute "simp theorems" or "simp lemmas".
Lean maintains a database/index containing all active simp theorems.
Here is an example of a simp theorem.


```
@[simp] theorem ne_eq (a b : α) : (a ≠ b) = Not (a = b) := rfl

```

This simp theorem instructs the simplifier to replace instances of the term `a ≠ b` (e.g. `x + 0 ≠ y`) with `Not (a = b)` (e.g., `Not (x + 0 = y)`). The simplifier applies simp theorems in one direction only: if `A = B` is a simp theorem, then `simp` replaces `A`s with `B`s, but it doesn't replace `B`s with `A`s. Hence a simp theorem should have the property that its right-hand side is "simpler" than its left-hand side. In particular, `=` and `↔` should not be viewed as symmetric operators in this situation. The following would be a terrible simp theorem (if it were even allowed):

```
@[simp] lemma mul_right_inv_bad (a : G) : 1 = a * a⁻¹ := ...

```

Replacing 1 with a * a⁻¹ is not a sensible default direction to travel. Even worse would be a theorem that causes expressions to grow without bound, causing simp to loop forever.
By default the simplifier applies `simp` theorems to an expression `e` after its sub-expressions have been simplified. We say it performs a bottom-up simplification. You can instruct the simplifier to apply a theorem before its sub-expressions have been simplified by using the modifier `↓`. Here is an example

```
@[simp↓] theorem not_and_eq (p q : Prop) : (¬ (p ∧ q)) = (¬p ∨ ¬q) :=

```

You can instruct the simplifier to rewrite the lemma from right-to-left:

```
attribute @[simp ←] and_assoc

```

When multiple simp theorems are applicable, the simplifier uses the one with highest priority. The equational theorems of functions are applied at very low priority (100 and below). If there are several with the same priority, it is uses the "most recent one". Example:

```
@[simp high] theorem cond_true (a b : α) : cond true a b = a := rfl
@[simp low+1] theorem or_true (p : Prop) : (p ∨ True) = True :=
  propext <| Iff.intro (fun _ => trivial) (fun _ => Or.inr trivial)
@[simp 100] theorem ite_self {d : Decidable c} (a : α) : ite c a a = a := by
  cases d <;> rfl

```

`simp `
 
Use this rewrite rule before entering the subterms 
 
`↓ (← ? | <- ?)
```

```
attr ::= ...
    | 


Theorems tagged with the simp attribute are used by the simplifier
(i.e., the simp tactic, and its variants) to simplify expressions occurring in your goals.
We call theorems tagged with the simp attribute "simp theorems" or "simp lemmas".
Lean maintains a database/index containing all active simp theorems.
Here is an example of a simp theorem.


```
@[simp] theorem ne_eq (a b : α) : (a ≠ b) = Not (a = b) := rfl

```

This simp theorem instructs the simplifier to replace instances of the term `a ≠ b` (e.g. `x + 0 ≠ y`) with `Not (a = b)` (e.g., `Not (x + 0 = y)`). The simplifier applies simp theorems in one direction only: if `A = B` is a simp theorem, then `simp` replaces `A`s with `B`s, but it doesn't replace `B`s with `A`s. Hence a simp theorem should have the property that its right-hand side is "simpler" than its left-hand side. In particular, `=` and `↔` should not be viewed as symmetric operators in this situation. The following would be a terrible simp theorem (if it were even allowed):

```
@[simp] lemma mul_right_inv_bad (a : G) : 1 = a * a⁻¹ := ...

```

Replacing 1 with a * a⁻¹ is not a sensible default direction to travel. Even worse would be a theorem that causes expressions to grow without bound, causing simp to loop forever.
By default the simplifier applies `simp` theorems to an expression `e` after its sub-expressions have been simplified. We say it performs a bottom-up simplification. You can instruct the simplifier to apply a theorem before its sub-expressions have been simplified by using the modifier `↓`. Here is an example

```
@[simp↓] theorem not_and_eq (p q : Prop) : (¬ (p ∧ q)) = (¬p ∨ ¬q) :=

```

You can instruct the simplifier to rewrite the lemma from right-to-left:

```
attribute @[simp ←] and_assoc

```

When multiple simp theorems are applicable, the simplifier uses the one with highest priority. The equational theorems of functions are applied at very low priority (100 and below). If there are several with the same priority, it is uses the "most recent one". Example:

```
@[simp high] theorem cond_true (a b : α) : cond true a b = a := rfl
@[simp low+1] theorem or_true (p : Prop) : (p ∨ True) = True :=
  propext <| Iff.intro (fun _ => trivial) (fun _ => Or.inr trivial)
@[simp 100] theorem ite_self {d : Decidable c} (a : α) : ite c a a = a := by
  cases d <;> rfl

```

`simp prio
```

_Custom simp sets_ are created with `[registerSimpAttr](The-Simplifier/Simp-sets/#Lean___Meta___registerSimpAttr "Documentation for Lean.Meta.registerSimpAttr")`, which must be run during [initialization](Elaboration-and-Compilation/#--tech-term-initialization) by placing it in an ``Lean.Parser.Command.initialize : command```initialize` block. As a side effect, it creates a new attribute with the same interface as `simp` that adds rules to the custom simp set. The returned value is a `[SimpExtension](The-Simplifier/Simp-sets/#Lean___Meta___SimpExtension "Documentation for Lean.Meta.SimpExtension")`, which can be used to programmatically access the contents of the custom simp set. The `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` tactics can be instructed to use the new simp set by including its attribute name in the rule list.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Meta.registerSimpAttr "Permalink")def
```


Lean.Meta.registerSimpAttr (attrName : Lean.Name) (attrDescr : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (ref : Lean.Name := by exact decl_name%) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Lean.Meta.SimpExtension](The-Simplifier/Simp-sets/#Lean___Meta___SimpExtension "Documentation for Lean.Meta.SimpExtension")


Lean.Meta.registerSimpAttr
  (attrName : Lean.Name)
  (attrDescr : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (ref : Lean.Name := by
    exact decl_name%) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [Lean.Meta.SimpExtension](The-Simplifier/Simp-sets/#Lean___Meta___SimpExtension "Documentation for Lean.Meta.SimpExtension")


```

Registers the given name as a custom simp set. Applying the name as an attribute to a name adds it to the simp set, and using the name as a parameter to the `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` tactic causes `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` to use the included lemmas.
Custom simp sets must be registered during [initialization](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=initialization).
The description should be a short, singular noun phrase that describes the contents of the custom simp set.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Meta.SimpExtension "Permalink")def
```


Lean.Meta.SimpExtension : Type


Lean.Meta.SimpExtension : Type


```

The environment extension that contains a simp set, returned by `[Lean.Meta.registerSimpAttr](The-Simplifier/Simp-sets/#Lean___Meta___registerSimpAttr "Documentation for Lean.Meta.registerSimpAttr")`.
Use the simp set's attribute or `Lean.Meta.addSimpTheorem` to add theorems to the simp set. Use `Lean.Meta.SimpExtension.getTheorems` to get the contents.
[←15.2. Rewrite Rules](The-Simplifier/Rewrite-Rules/#simp-rewrites "15.2. Rewrite Rules")[15.4. Simp Normal Forms→](The-Simplifier/Simp-Normal-Forms/#simp-normal-forms "15.4. Simp Normal Forms")

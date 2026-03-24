[←7.3. Definitions](Definitions/Definitions/#The-Lean-Language-Reference--Definitions--Definitions "7.3. Definitions")[7.5. Example Declarations→](Definitions/Example-Declarations/#The-Lean-Language-Reference--Definitions--Example-Declarations "7.5. Example Declarations")
#  7.4. Theorems[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Definitions--Theorems "Permalink")
Because [propositions](The-Type-System/Propositions/#--tech-term-Propositions) are types whose inhabitants count as proofs, theorems and definitions are technically very similar. However, because their use cases are quite different, they differ in many details:
  * The theorem statement must be a proposition. The types of definitions may inhabit any [universe](The-Type-System/Universes/#--tech-term-universes).
  * A theorem's header (that is, the theorem statement) is completely elaborated before the body is elaborated. Section variables only become parameters to the theorem if they (or their dependents) are mentioned in the header. This prevents changes to a proof from unintentionally changing the theorem statement.
  * Theorems are [irreducible](Definitions/Recursive-Definitions/#--tech-term-Irreducible) by default. Because all proofs of the same proposition are [definitionally equal](The-Type-System/#--tech-term-definitional-equality), there few reasons to unfold a theorem.


Theorems may be recursive, subject to the same conditions as [recursive function definitions](Definitions/Recursive-Definitions/#recursive-definitions). However, it is more common to use tactics such as `[induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic")` or `[fun_induction](Tactic-Proofs/Tactic-Reference/#fun_induction "Documentation for tactic")` instead.
syntaxTheorems
The syntax of theorems is like that of definitions, except the codomain (that is, the theorem statement) in the signature is mandatory.

```
command ::= ...
    | [
declModifiers is the collection of modifiers on a declaration:



  * a doc comment /-- ... -/



  * a list of attributes @[attr1, attr2]



  * a visibility specifier, private or public



  * protected


  * noncomputable


  * unsafe


  * 
partial or nonrec




All modifiers are optional, and have to come in the listed order.
nestedDeclModifiers is the same as declModifiers, but attributes are printed
on the same line as the declaration. It is used for declarations nested inside other syntax,
such as inductive constructors, structure projections, and let rec / where definitions. 
declModifiers](Definitions/Modifiers/#Lean___Parser___Command___declModifiers)
      theorem 


declId matches foo or foo.{u,v}: an identifier possibly followed by a list of universe names 


declId [
declSig matches the signature of a declaration with required type: a list of binders and then : type 
declSig](Definitions/Headers-and-Signatures/#Lean___Parser___Command___declSig) := term


Termination hints are termination_by and decreasing_by, in that order.



```

```
command ::= ...
    | [
declModifiers is the collection of modifiers on a declaration:



  * a doc comment /-- ... -/



  * a list of attributes @[attr1, attr2]



  * a visibility specifier, private or public



  * protected


  * noncomputable


  * unsafe


  * 
partial or nonrec




All modifiers are optional, and have to come in the listed order.
nestedDeclModifiers is the same as declModifiers, but attributes are printed
on the same line as the declaration. It is used for declarations nested inside other syntax,
such as inductive constructors, structure projections, and let rec / where definitions. 
declModifiers](Definitions/Modifiers/#Lean___Parser___Command___declModifiers)
      theorem 


declId matches foo or foo.{u,v}: an identifier possibly followed by a list of universe names 


declId [
declSig matches the signature of a declaration with required type: a list of binders and then : type 
declSig](Definitions/Headers-and-Signatures/#Lean___Parser___Command___declSig)
        (| term => term)*


Termination hints are termination_by and decreasing_by, in that order.



```

```
command ::= ...
    | [
declModifiers is the collection of modifiers on a declaration:



  * a doc comment /-- ... -/



  * a list of attributes @[attr1, attr2]



  * a visibility specifier, private or public



  * protected


  * noncomputable


  * unsafe


  * 
partial or nonrec




All modifiers are optional, and have to come in the listed order.
nestedDeclModifiers is the same as declModifiers, but attributes are printed
on the same line as the declaration. It is used for declarations nested inside other syntax,
such as inductive constructors, structure projections, and let rec / where definitions. 
declModifiers](Definitions/Modifiers/#Lean___Parser___Command___declModifiers)
      theorem 


declId matches foo or foo.{u,v}: an identifier possibly followed by a list of universe names 


declId [
declSig matches the signature of a declaration with required type: a list of binders and then : type 
declSig](Definitions/Headers-and-Signatures/#Lean___Parser___Command___declSig) where
        structInstField*
```

In [modules](Source-Files-and-Modules/#--tech-term-module), proofs of theorems are not exposed by default.
[←7.3. Definitions](Definitions/Definitions/#The-Lean-Language-Reference--Definitions--Definitions "7.3. Definitions")[7.5. Example Declarations→](Definitions/Example-Declarations/#The-Lean-Language-Reference--Definitions--Example-Declarations "7.5. Example Declarations")

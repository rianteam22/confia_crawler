[←7.4. Theorems](Definitions/Theorems/#The-Lean-Language-Reference--Definitions--Theorems "7.4. Theorems")[7.6. Recursive Definitions→](Definitions/Recursive-Definitions/#recursive-definitions "7.6. Recursive Definitions")
#  7.5. Example Declarations[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Definitions--Example-Declarations "Permalink")
An example is an anonymous definition that is elaborated and then discarded. Examples are useful for incremental testing during development and to make it easier to understand a file.
syntaxExamples

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
      example [
optDeclSig matches the signature of a declaration with optional type: a list of binders and then possibly : type 
optDeclSig](Definitions/Headers-and-Signatures/#Lean___Parser___Command___optDeclSig) := term


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
      example [
optDeclSig matches the signature of a declaration with optional type: a list of binders and then possibly : type 
optDeclSig](Definitions/Headers-and-Signatures/#Lean___Parser___Command___optDeclSig)
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
      example [
optDeclSig matches the signature of a declaration with optional type: a list of binders and then possibly : type 
optDeclSig](Definitions/Headers-and-Signatures/#Lean___Parser___Command___optDeclSig) where
        structInstField*
```

[←7.4. Theorems](Definitions/Theorems/#The-Lean-Language-Reference--Definitions--Theorems "7.4. Theorems")[7.6. Recursive Definitions→](Definitions/Recursive-Definitions/#recursive-definitions "7.6. Recursive Definitions")

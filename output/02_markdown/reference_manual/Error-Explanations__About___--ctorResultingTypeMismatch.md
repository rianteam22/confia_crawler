[←Error Explanations](Error-Explanations/#The-Lean-Language-Reference--Error-Explanations "Error Explanations")[About: dependsOnNoncomputable→](Error-Explanations/About___--dependsOnNoncomputable/#The-Lean-Language-Reference--Error-Explanations--About___--dependsOnNoncomputable "About: dependsOnNoncomputable")
#  About: `ctorResultingTypeMismatch`[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--ctorResultingTypeMismatch "Permalink")
Error code: `lean.ctorResultingTypeMismatch`
_Resulting type of constructor was not the inductive type being declared._
**Severity:** Error**Since:** 4.22.0
In an inductive declaration, the resulting type of each constructor must match the type being declared; if it does not, this error is raised. That is, every constructor of an inductive type must return a value of that type. See the [Inductive Types](The-Type-System/Inductive-Types/#inductive-types) manual section for additional details. Note that it is possible to omit the resulting type for a constructor if the inductive type being defined has no indices.
##  Examples[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--ctorResultingTypeMismatch--Examples "Permalink")
Typo in Resulting Type
OriginalFixed
`inductive Tree (α : Type) where   | leaf : Tree α   | node : `Unexpected resulting type for constructor `Tree.node`: Expected an application of   Tree but found   ?m.2`α → Tree α → Treee α `
```
Unexpected resulting type for constructor `Tree.node`: Expected an application of
  Tree
but found
  ?m.2
```

`inductive Tree (α : Type) where   | leaf : Tree α   | node : α → Tree α → Tree α `
Missing Resulting Type After Constructor Parameter
OriginalFixed (resulting type)Fixed (named parameter)
`inductive Credential where   | pin      : `Unexpected resulting type for constructor `Credential.pin`: Expected   Credential but found   [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") | password : String `
```
Unexpected resulting type for constructor `Credential.pin`: Expected
  Credential
but found
  [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

`inductive Credential where   | pin      : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Credential   | password : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → Credential `
`inductive Credential where   | pin (num : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))   | password (str : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) `
If the type of a constructor is annotated, the full type—including the resulting type—must be provided. Alternatively, constructor parameters can be written using named binders; this allows the omission of the constructor's resulting type because it contains no indices.
[←Error Explanations](Error-Explanations/#The-Lean-Language-Reference--Error-Explanations "Error Explanations")[About: dependsOnNoncomputable→](Error-Explanations/About___--dependsOnNoncomputable/#The-Lean-Language-Reference--Error-Explanations--About___--dependsOnNoncomputable "About: dependsOnNoncomputable")

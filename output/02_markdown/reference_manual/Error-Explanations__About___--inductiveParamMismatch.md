[←About: inductionWithNoAlts](Error-Explanations/About___--inductionWithNoAlts/#The-Lean-Language-Reference--Error-Explanations--About___--inductionWithNoAlts "About: inductionWithNoAlts")[About: inductiveParamMissing→](Error-Explanations/About___--inductiveParamMissing/#The-Lean-Language-Reference--Error-Explanations--About___--inductiveParamMissing "About: inductiveParamMissing")
#  About: `inductiveParamMismatch`[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--inductiveParamMismatch "Permalink")
Error code: `lean.inductiveParamMismatch`
_Invalid parameter in an occurrence of an inductive type in one of its constructors._
**Severity:** Error**Since:** 4.22.0
This error occurs when a parameter of an inductive type is not uniform in an inductive declaration. The parameters of an inductive type (i.e., those that appear before the colon following the `inductive` keyword) must be identical in all occurrences of the type being defined in its constructors' types. If a parameter of an inductive type must vary between constructors, make the parameter an index by moving it to the right of the colon. See the manual section on [Inductive Types](The-Type-System/Inductive-Types/#inductive-types) for additional details.
Note that auto-implicit inlay hints always appear left of the colon in an inductive declaration (i.e., as parameters), even when they are actually indices. This means that double-clicking on an inlay hint to insert such parameters may result in this error. If it does, change the inserted parameters to indices.
##  Examples[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--inductiveParamMismatch--Examples "Permalink")
Vector Length Index as a Parameter
OriginalFixed
`inductive Vec (α : Type) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : Type where   `Mismatched inductive type parameter in   Vec α 0 The provided argument   0 is not definitionally equal to the expected parameter   n  Note: The value of parameter `n` must be fixed throughout the inductive declaration. Consider making this parameter an index if it must vary.`| nil : Vec α 0 | cons : α → Vec α n → Vec α (n + 1) `
```
Mismatched inductive type parameter in
  Vec α 0
The provided argument
  0
is not definitionally equal to the expected parameter
  n

Note: The value of parameter `n` must be fixed throughout the inductive declaration. Consider making this parameter an index if it must vary.
```

`inductive Vec (α : Type) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Type where   | nil  : Vec α 0   | cons : α → Vec α n → Vec α (n + 1) `
The length argument `n` of the `Vec` type constructor is declared as a parameter, but other values for this argument appear in the `nil` and `cons` constructors (namely, `0` and `n + 1`). An error therefore appears at the first occurrence of such an argument. To correct this, `n` cannot be a parameter of the inductive declaration and must instead be an index, as in the corrected example. On the other hand, `α` remains unchanged throughout all occurrences of `Vec` in the declaration and so is a valid parameter.
[←About: inductionWithNoAlts](Error-Explanations/About___--inductionWithNoAlts/#The-Lean-Language-Reference--Error-Explanations--About___--inductionWithNoAlts "About: inductionWithNoAlts")[About: inductiveParamMissing→](Error-Explanations/About___--inductiveParamMissing/#The-Lean-Language-Reference--Error-Explanations--About___--inductiveParamMissing "About: inductiveParamMissing")

[←About: inductiveParamMismatch](Error-Explanations/About___--inductiveParamMismatch/#The-Lean-Language-Reference--Error-Explanations--About___--inductiveParamMismatch "About: inductiveParamMismatch")[About: inferBinderTypeFailed→](Error-Explanations/About___--inferBinderTypeFailed/#The-Lean-Language-Reference--Error-Explanations--About___--inferBinderTypeFailed "About: inferBinderTypeFailed")
#  About: `inductiveParamMissing`[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--inductiveParamMissing "Permalink")
Error code: `lean.inductiveParamMissing`
_Parameter not present in an occurrence of an inductive type in one of its constructors._
**Severity:** Error**Since:** 4.22.0
This error occurs when an inductive type constructor is partially applied in the type of one of its constructors such that one or more parameters of the type are omitted. The elaborator requires that all parameters of an inductive type be specified everywhere that type is referenced in its definition, including in the types of its constructors.
If it is necessary to allow the type constructor to be partially applied, without specifying a given type parameter, that parameter must be converted to an index. See the manual section on [Inductive Types](The-Type-System/Inductive-Types/#inductive-types) for further explanation of the difference between indices and parameters.
##  Examples[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--inductiveParamMissing--Examples "Permalink")
Omitting Parameter in Argument to Higher-Order Predicate
OriginalFixed
`inductive List.All {α : Type u} (P : α → Prop) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → Prop   | nil : All P []   | cons {x xs} : P x → All P xs → All P (x :: xs)  structure RoseTree (α : Type u) where   val : α   children : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (RoseTree α)  inductive RoseTree.All (P : α → Prop) (t : RoseTree α) : Prop   `Missing parameter(s) in occurrence of inductive type: In the expression   List.All (All P) t.children found   All P but expected all parameters to be specified:   All P t  Note: All occurrences of an inductive type in the types of its constructors must specify its fixed parameters. Only indices can be omitted in a partial application of the type constructor.`| intro : P t.val → List.All (All P) t.children → All P t `
```
Missing parameter(s) in occurrence of inductive type: In the expression
  List.All (All P) t.children
found
  All P
but expected all parameters to be specified:
  All P t

Note: All occurrences of an inductive type in the types of its constructors must specify its fixed parameters. Only indices can be omitted in a partial application of the type constructor.
```

`inductive List.All {α : Type u} (P : α → Prop) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → Prop   | nil : All P []   | cons {x xs} : P x → All P xs → All P (x :: xs)  structure RoseTree (α : Type u) where   val : α   children : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") (RoseTree α)  inductive RoseTree.All (P : α → Prop) : RoseTree α → Prop   | intro : P t.val → List.All ([All](Error-Explanations/About___--inductiveParamMissing/#RoseTree___All-_LPAR_in-Omitting-Parameter-in-Argument-to-Higher-Order-Predicate_RPAR_ "Definition of example") P) t.children → [All](Error-Explanations/About___--inductiveParamMissing/#RoseTree___All-_LPAR_in-Omitting-Parameter-in-Argument-to-Higher-Order-Predicate_RPAR_ "Definition of example") P t `
Because the `RoseTree.All` type constructor must be partially applied in the argument to `List.All`, the unspecified argument (`t`) must not be a parameter of the `RoseTree.All` predicate. Making it an index to the right of the colon in the header of `RoseTree.All` allows this partial application to succeed.
[←About: inductiveParamMismatch](Error-Explanations/About___--inductiveParamMismatch/#The-Lean-Language-Reference--Error-Explanations--About___--inductiveParamMismatch "About: inductiveParamMismatch")[About: inferBinderTypeFailed→](Error-Explanations/About___--inferBinderTypeFailed/#The-Lean-Language-Reference--Error-Explanations--About___--inferBinderTypeFailed "About: inferBinderTypeFailed")

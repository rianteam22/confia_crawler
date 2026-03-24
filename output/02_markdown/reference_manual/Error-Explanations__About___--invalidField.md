[←About: invalidDottedIdent](Error-Explanations/About___--invalidDottedIdent/#The-Lean-Language-Reference--Error-Explanations--About___--invalidDottedIdent "About: invalidDottedIdent")[About: projNonPropFromProp→](Error-Explanations/About___--projNonPropFromProp/#The-Lean-Language-Reference--Error-Explanations--About___--projNonPropFromProp "About: projNonPropFromProp")
#  About: `invalidField`[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--invalidField "Permalink")
Error code: `lean.invalidField`
_Generalized field notation used in a potentially ambiguous way._
**Severity:** Error**Since:** 4.22.0
This error indicates that an expression containing a dot followed by an identifier was encountered, and that it wasn't possible to understand the identifier as a field.
Lean's field notation is very powerful, but this can also make it confusing: the expression `color.value` can either be a single [identifier](Terms/Identifiers/#identifiers-and-resolution). it can be a reference to the [field of a structure](The-Type-System/Inductive-Types/#structure-fields), and it and be a calling a function on the value `color` with [generalized field notation](Terms/Function-Application/#generalized-field-notation).
##  Examples[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--invalidField--Examples "Permalink")
Incorrect Field Name
OriginalFixed
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (4 + 2).`Invalid field `suc`: The environment does not contain `Nat.suc`, so it is not possible to project the field `suc` from an expression   4 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 of type `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")``suc `
```
Invalid field `suc`: The environment does not contain `Nat.suc`, so it is not possible to project the field `suc` from an expression
  4 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2
of type `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`
```

``6`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (4 + 1).[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") `
The simplest reason for an invalid field error is that the function being sought, like `Nat.suc`, does not exist.
Projecting from the Wrong Expression
OriginalFixed
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") '>'.`Invalid field `leftpad`: The environment does not contain `Char.leftpad`, so it is not possible to project the field `leftpad` from an expression   '>' of type `[Char](Basic-Types/Characters/#Char___mk "Documentation for Char")``leftpad 10 ['a', 'b', 'c'] `
```
Invalid field `leftpad`: The environment does not contain `Char.leftpad`, so it is not possible to project the field `leftpad` from an expression
  '>'
of type `[Char](Basic-Types/Characters/#Char___mk "Documentation for Char")`
```

``[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")'>'[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") '>'[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") '>'[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") '>'[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") '>'[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") '>'[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") '>'[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 'a'[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 'b'[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 'c'[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ['a', 'b', 'c'].[leftpad](Basic-Types/Linked-Lists/#List___leftpad "Documentation for List.leftpad") 10 '>' `
The type of the expression before the dot entirely determines the function being called by the field projection. There is no `Char.leftpad`, and the only way to invoke `List.leftpad` with generalized field notation is to have the list come before the dot.
Type is Not Specific
OriginalFixed
`def double_plus_one {α} [[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") α] (x : α) :=    `Invalid field notation: Field projection operates on types of the form `C ...` where C is a constant. The expression   x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x has type `α` which does not have the necessary form.`(x + x).succ `
```
Invalid field notation: Field projection operates on types of the form `C ...` where C is a constant. The expression
  x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x
has type `α` which does not have the necessary form.
```

`def double_plus_one (x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :=    (x + x).[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") `
The `Add` type class is sufficient for performing the addition `x + x`, but the `.succ` field notation cannot operate without knowing more about the actual type from which `succ` is being projected.
Insufficient Type Information
OriginalFixed
`example := fun (n) => `Invalid field notation: Type of   n is not known; cannot resolve field `succ`  Hint: Consider replacing the field projection with a call to one of the following:   • `[Fin.succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ")`   • `[Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")`   • `Lean.Level.succ`   • `Std.PRange.succ`   • `Lean.Level.PP.Result.succ`   • `Std.Time.Internal.Bounded.LE.succ``n.succ.succ `
```
Invalid field notation: Type of
  n
is not known; cannot resolve field `succ`

Hint: Consider replacing the field projection with a call to one of the following:
  • `[Fin.succ](Basic-Types/Finite-Natural-Numbers/#Fin___succ "Documentation for Fin.succ")`
  • `[Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")`
  • `Lean.Level.succ`
  • `Std.PRange.succ`
  • `Lean.Level.PP.Result.succ`
  • `Std.Time.Internal.Bounded.LE.succ`
```

`example := fun (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) => n.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ").[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") `
Generalized field notation can only be used when it is possible to determine the type that is being projected. Type annotations may need to be added to make generalized field notation work.
[←About: invalidDottedIdent](Error-Explanations/About___--invalidDottedIdent/#The-Lean-Language-Reference--Error-Explanations--About___--invalidDottedIdent "About: invalidDottedIdent")[About: projNonPropFromProp→](Error-Explanations/About___--projNonPropFromProp/#The-Lean-Language-Reference--Error-Explanations--About___--projNonPropFromProp "About: projNonPropFromProp")

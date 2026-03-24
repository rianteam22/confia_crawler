[←About: inductiveParamMissing](Error-Explanations/About___--inductiveParamMissing/#The-Lean-Language-Reference--Error-Explanations--About___--inductiveParamMissing "About: inductiveParamMissing")[About: inferDefTypeFailed→](Error-Explanations/About___--inferDefTypeFailed/#The-Lean-Language-Reference--Error-Explanations--About___--inferDefTypeFailed "About: inferDefTypeFailed")
#  About: `inferBinderTypeFailed`[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--inferBinderTypeFailed "Permalink")
Error code: `lean.inferBinderTypeFailed`
_The type of a binder could not be inferred._
**Severity:** Error**Since:** 4.23.0
This error occurs when the type of a binder in a declaration header or local binding is not fully specified and cannot be inferred by Lean. Generally, this can be resolved by providing more information to help Lean determine the type of the binder, either by explicitly annotating its type or by providing additional type information at sites where it is used. When the binder in question occurs in the header of a declaration, this error is often accompanied by [`lean.inferDefTypeFailed`](Error-Explanations/About___--inferDefTypeFailed/#lean___inferDefTypeFailed).
Note that if a declaration is annotated with an explicit resulting type—even one that contains holes—Lean will not use information from the definition body to infer parameter types. It may therefore be necessary to explicitly specify the types of parameters whose types would otherwise be inferable without the resulting-type annotation; see the “uninferred binder due to resulting type annotation” example below for a demonstration. In `theorem` declarations, the body is never used to infer the types of binders, so any binders whose types cannot be inferred from the rest of the theorem type must include a type annotation.
This error may also arise when identifiers that were intended to be declaration names are inadvertently written in binder position instead. In these cases, the erroneous identifiers are treated as binders with unspecified type, leading to a type inference failure. This frequently occurs when attempting to simultaneously define multiple constants of the same type using syntax that does not support this. Such situations include:
  * Attempting to name an example by writing an identifier after the `example` keyword;
  * Attempting to define multiple constants with the same type and (if applicable) value by listing them sequentially after `def`, `opaque`, or another declaration keyword;
  * Attempting to define multiple fields of a structure of the same type by sequentially listing their names on the same line of a structure declaration; and
  * Omitting vertical bars between inductive constructor names.


The first three cases are demonstrated in examples below.
##  Examples[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--inferBinderTypeFailed--Examples "Permalink")
Binder Type Requires New Type Variable
OriginalFixed
`def `Failed to infer type of definition `identity``identity `Failed to infer type of binder `x``x := x `
```
Failed to infer type of binder `x`
```

`def identity (x : α) :=   x `
In the code above, the type of `x` is unconstrained; as this example demonstrates, Lean does not automatically generate fresh type variables for such binders. Instead, the type `α` of `x` must be specified explicitly. Note that if automatic implicit parameter insertion is enabled (as it is by default), a binder for `α` itself need not be provided; Lean will insert an implicit binder for this parameter automatically.
Uninferred Binder Type Due to Resulting Type Annotation
OriginalFixed
`def plusTwo `Failed to infer type of binder `x`  Note: Because this declaration's type has been explicitly provided, all parameter types and holes (e.g., `_`) in its header are resolved before its body is processed; information from the declaration body cannot be used to infer what these values should be`x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := x + 2 `
```
Failed to infer type of binder `x`

Note: Because this declaration's type has been explicitly provided, all parameter types and holes (e.g., `_`) in its header are resolved before its body is processed; information from the declaration body cannot be used to infer what these values should be
```

`def plusTwo (x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") :=   x + 2 `
Even though `x` is inferred to have type `Nat` in the body of `plusTwo`, this information is not available when elaborating the type of the definition because its resulting type (`Nat`) has been explicitly specified. Considering only the information in the header, the type of `x` cannot be determined, resulting in the shown error. It is therefore necessary to include the type of `x` in its binder.
Attempting to Name an Example Declaration
OriginalFixed
`example `Failed to infer type of binder `trivial_proof`  Note: Examples do not have names. The identifier `trivial_proof` is being interpreted as a parameter `(trivial_proof : _)`.`trivial_proof : [True](Basic-Propositions/Truth/#True___intro "Documentation for True") := trivial `
```
Failed to infer type of binder `trivial_proof`

Note: Examples do not have names. The identifier `trivial_proof` is being interpreted as a parameter `(trivial_proof : _)`.
```

`example : [True](Basic-Propositions/Truth/#True___intro "Documentation for True") :=   trivial `
This code is invalid because it attempts to give a name to an `example` declaration. Examples cannot be named, and an identifier written where a name would appear in other declaration forms is instead elaborated as a binder, whose type cannot be inferred. If a declaration must be named, it should be defined using a declaration form that supports naming, such as `def` or `theorem`.
Attempting to Define Multiple Opaque Constants at Once
OriginalFixed
`opaque m `Failed to infer type of binder `n`  Note: Multiple constants cannot be declared in a single declaration. The identifier `n` is being interpreted as a parameter `(n : _)`.`n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") `
```
Failed to infer type of binder `n`

Note: Multiple constants cannot be declared in a single declaration. The identifier `n` is being interpreted as a parameter `(n : _)`.
```

`opaque m : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") opaque n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") `
This example incorrectly attempts to define multiple constants with a single `opaque` declaration. Such a declaration can define only one constant: it is not possible to list multiple identifiers after `opaque` or `def` to define them all to have the same type (or value). Such a declaration is instead elaborated as defining a single constant (e.g., `m` above) with parameters given by the subsequent identifiers (`n`), whose types are unspecified and cannot be inferred. To define multiple global constants, it is necessary to declare each separately.
Attempting to Define Multiple Structure Fields on the Same Line
OriginalFixed (Fixed (separate lines))Fixed (Fixed (parenthesized))
`structure Person where   givenName `Failed to infer type of binder `familyName``familyName : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") age : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") `
```
Failed to infer type of binder `familyName`
```

`structure Person where   givenName : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")   familyName : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")   age : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") `
`structure Person where   (givenName familyName : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))   age : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") `
This example incorrectly attempts to define multiple structure fields (`givenName` and `familyName`) of the same type by listing them consecutively on the same line. Lean instead interprets this as defining a single field, `givenName`, parametrized by a binder `familyName` with no specified type. The intended behavior can be achieved by either listing each field on a separate line, or enclosing the line specifying multiple field names in parentheses (see the manual section on [Inductive Types](The-Type-System/Inductive-Types/#inductive-types) for further details about structure declarations).
[←About: inductiveParamMissing](Error-Explanations/About___--inductiveParamMissing/#The-Lean-Language-Reference--Error-Explanations--About___--inductiveParamMissing "About: inductiveParamMissing")[About: inferDefTypeFailed→](Error-Explanations/About___--inferDefTypeFailed/#The-Lean-Language-Reference--Error-Explanations--About___--inferDefTypeFailed "About: inferDefTypeFailed")

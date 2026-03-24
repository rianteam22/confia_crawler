[←About: redundantMatchAlt](Error-Explanations/About___--redundantMatchAlt/#The-Lean-Language-Reference--Error-Explanations--About___--redundantMatchAlt "About: redundantMatchAlt")[About: unknownIdentifier→](Error-Explanations/About___--unknownIdentifier/#The-Lean-Language-Reference--Error-Explanations--About___--unknownIdentifier "About: unknownIdentifier")
#  About: `synthInstanceFailed`[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--synthInstanceFailed "Permalink")
Error code: `lean.synthInstanceFailed`
_Failed to synthesize instance of type class._
**Severity:** Error**Since:** 4.26.0
[Type classes](Type-Classes/#type-classes) are the mechanism that Lean and many other programming languages use to handle overloaded operations. The code that handles a particular overloaded operation is an [_instance_](Type-Classes/#--tech-term-instances) of a type class; deciding which instance to use for a given overloaded operation is called _synthesizing_ an instance.
As an example, when Lean encounters an expression `x + y` where `x` and `y` both have type `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`, it is necessary to look up how it should add two integers and also look up what the resulting type will be. This is described as synthesizing an instance of the type class `[HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") t` for some type `t`.
Many failures to synthesize an instance of a type class are the result of using the wrong binary operation. Both success and failure are not always straightforward, because some instances are defined in terms of other instances, and Lean must recursively search to find appropriate instances. It's possible to [inspect Lean's instance synthesis](Type-Classes/Instance-Synthesis/#instance-search), and this can be helpful for diagnosing tricky failures of type class instance synthesis.
##  Examples[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Error-Explanations--About___--synthInstanceFailed--Examples "Permalink")
Using the Wrong Binary Operation
OriginalFixed
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") `failed to synthesize instance of type class   [HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") ?m.4  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`"A" + "3" `
```
failed to synthesize instance of type class
  [HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") ?m.4

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```

``"A3"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") "A" ++ "3" `
The binary operation `+` is associated with the `[HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd")` type class, and there's no way to add two strings. The binary operation `++`, associated with the `[HAppend](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend")` type class, is the correct way to append strings.
Arguments Have the Wrong Type
OriginalFixed
`def x : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") := 3 [#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") `failed to synthesize instance of type class   [HAppend](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") ?m.4  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`x ++ "meters" `
```
failed to synthesize instance of type class
  [HAppend](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") ?m.4

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```

`def x : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") := 3 `"3meters"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ToString.toString x ++ "meters" `
Lean does not allow integers and strings to be added directly. The function `ToString.toString` uses type class overloading to convert values to strings; by successfully searching for an instance of `ToString [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`, the second example will succeed.
Missing Type Class Instance
OriginalFixed (derive instance when defining type)Fixed (derive instance separately)Fixed (define instance)
`inductive MyColor where   | chartreuse | sienna | thistle  def forceColor (oc : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") MyColor) :=   `failed to synthesize instance of type class   [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") MyColor  Hint: Adding the command `deriving instance Inhabited for MyColor` may allow Lean to derive the missing instance.`oc.[get!](Basic-Types/Optional-Values/#Option___get___ "Documentation for Option.get!") `
```
failed to synthesize instance of type class
  [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") MyColor

Hint: Adding the command `deriving instance Inhabited for MyColor` may allow Lean to derive the missing instance.
```

`inductive MyColor where   | chartreuse | sienna | thistle deriving [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited")  def forceColor (oc : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") MyColor) :=   oc.[get!](Basic-Types/Optional-Values/#Option___get___ "Documentation for Option.get!") `
`inductive MyColor where   | chartreuse | sienna | thistle  [deriving](Type-Classes/Deriving-Instances/#Lean___Parser___Command___deriving-next "Documentation for syntax") [instance](Type-Classes/Deriving-Instances/#Lean___Parser___Command___deriving-next "Documentation for syntax") [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [for](Type-Classes/Deriving-Instances/#Lean___Parser___Command___deriving-next "Documentation for syntax") MyColor  def forceColor (oc : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") MyColor) :=   oc.[get!](Basic-Types/Optional-Values/#Option___get___ "Documentation for Option.get!") `
`inductive MyColor where   | chartreuse | sienna | thistle  instance : [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") MyColor where   [default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") := .sienna  def forceColor (oc : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") MyColor) :=   oc.[get!](Basic-Types/Optional-Values/#Option___get___ "Documentation for Option.get!") `
Type class synthesis can fail because an instance of the type class simply needs to be provided. This commonly happens for type classes like `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")`, `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")`, `ToJson` and `[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited")`. Lean can often [automatically generate instances of the type class with the `deriving` keyword](Type-Classes/Deriving-Instances/#deriving-instances) either when the type is defined or with the stand-alone ``Lean.Parser.Command.deriving : command``[`deriving`](Type-Classes/Deriving-Instances/#Lean___Parser___Command___deriving-next) command.
[←About: redundantMatchAlt](Error-Explanations/About___--redundantMatchAlt/#The-Lean-Language-Reference--Error-Explanations--About___--redundantMatchAlt "About: redundantMatchAlt")[About: unknownIdentifier→](Error-Explanations/About___--unknownIdentifier/#The-Lean-Language-Reference--Error-Explanations--About___--unknownIdentifier "About: unknownIdentifier")

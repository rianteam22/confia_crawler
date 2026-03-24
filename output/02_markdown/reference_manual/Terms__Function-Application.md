[←13.3. Functions](Terms/Functions/#function-terms "13.3. Functions")[13.5. Numeric Literals→](Terms/Numeric-Literals/#The-Lean-Language-Reference--Terms--Numeric-Literals "13.5. Numeric Literals")
#  13.4. Function Application[🔗](find/?domain=Verso.Genre.Manual.section&name=function-application "Permalink")
Ordinarily, function application is written using juxtaposition: the argument is placed after the function, with at least one space between them. In Lean's type theory, all functions take exactly one argument and produce exactly one value. All function applications combine a single function with a single argument. Multiple arguments are represented via currying.
The high-level term language treats a function together with one or more arguments as a single unit, and supports additional features such as implicit, optional, and by-name arguments along with ordinary positional arguments. The elaborator converts these to the simpler model of the core type theory.
syntaxFunction Application
A function application consists of a term followed by one or more arguments, or by zero or more arguments and a final ellipsis.

```
term ::= ...
    | term argument+
    | term argument* ..
```

syntaxArguments
Function arguments are either terms or named arguments.

```
argument ::= ...
    | term
    | ((ident | _:ident) :=term)
```

The function's core-language type determines the placement of the arguments in the final expression. Function types include names for their expected parameters. In Lean's core language, non-dependent function types are encoded as dependent function types in which the parameter name does not occur in the body. Furthermore, they are chosen internally such that they cannot be written as the name of a named argument; this is important to prevent accidental capture.
Each parameter expected by the function has a name. Recurring over the function's argument types, arguments are selected from the sequence of arguments as follows:
  * If the parameter's name matches the name provided for a named argument, then that argument is selected.
  * If the parameter is [implicit](Terms/Functions/#--tech-term-implicit), a fresh metavariable is created with the parameter's type and selected.
  * If the parameter is [instance implicit](Type-Classes/#--tech-term-instance-implicit), a fresh instance metavariable is created with the parameter's type and inserted. Instance metavariables are scheduled for later synthesis.
  * If the parameter is a [strict implicit](Terms/Functions/#--tech-term-Strict-implicit) parameter and there are any named or positional arguments that have not yet been selected, a fresh metavariable is created with the parameter's type and selected.
  * If the parameter is explicit, then the next positional argument is selected and elaborated. If there are no positional arguments:
    * If the parameter is declared as an [optional parameter](Definitions/Headers-and-Signatures/#--tech-term-optional-parameters), then its default value is selected as the argument.
    * If the parameter is an [automatic parameter](Definitions/Headers-and-Signatures/#--tech-term-automatic-parameters) then its associated tactic script is executed to construct the argument.
    * If the parameter is neither optional nor automatic, and no ellipsis is present, then a fresh variable is selected as the argument. If there is an ellipsis, a fresh metavariable is selected as if the argument were implicit.


As a special case, when the function application occurs in a [pattern](Terms/Pattern-Matching/#pattern-matching) and there is an ellipsis, optional and automatic arguments become universal patterns (`_`) instead of being inserted.
It is an error if the type is not a function type and arguments remain. After all arguments have been inserted and there is an ellipsis, then the missing arguments are all set to fresh metavariables, just as if they were implicit arguments. If any fresh variables were created for missing explicit positional arguments, the entire application is wrapped in a ``Lean.Parser.Term.fun : term```fun` term that binds them. Finally, instance synthesis is invoked and as many metavariables as possible are solved:
  1. A type is inferred for the entire function application. This may cause some metavariables to be solved due to unification that occurs during type inference.
  2. The instance metavariables are synthesized. [Default instances](Type-Classes/Instance-Synthesis/#--tech-term-default-instances) are only used if the inferred type is a metavariable that is the output parameter of one of the instances.
  3. If there is an expected type, it is unified with the inferred type; however, errors resulting from this unification are discarded. If the expected and inferred types can be equal, unification can solve leftover implicit argument metavariables. If they can't be equal, an error is not thrown because a surrounding elaborator may be able to insert [coercions](Coercions/#--tech-term-coercion) or [monad lifts](Functors___-Monads-and--do--Notation/Lifting-Monads/#--tech-term-lifting).

Named Arguments
The ``Lean.Parser.Command.check : command``[`#check`](Interacting-with-Lean/#Lean___Parser___Command___check) command can be used to inspect the arguments that were inserted for a function call.
The function `[sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example")` takes three explicit `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` parameters, named `x`, `y`, and `z`.
`def sum3 (x y z : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := x + y + z `
All three arguments can be provided positionally.
``[sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") 1 3 8 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") 1 3 8 `
```
[sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") 1 3 8 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

They can also be provided by name.
``[sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") 1 3 8 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") (x := 1) (y := 3) (z := 8) `
```
[sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") 1 3 8 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

When arguments are provided by name, it can be in any order.
``[sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") 1 3 8 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") (y := 3) (z := 8) (x := 1) `
```
[sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") 1 3 8 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

Named and positional arguments may be freely intermixed.
``[sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") 1 3 8 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") 1 (z := 8) (y := 3) `
```
[sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") 1 3 8 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

Named and positional arguments may be freely intermixed. If an argument is provided by name, it is used, even if it occurs after a positional argument that could have been used.
``[sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") 8 3 1 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") 1 (x := 8) (y := 3) `
```
[sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") 8 3 1 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

If a named argument is to be inserted after arguments that aren't provided, a function is created in which the provided argument is filled out.
``fun x y => [sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") x y 8 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") (z := 8) `
```
fun x y => [sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") x y 8 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

Behind the scenes, the names of the arguments are preserved in the function type. This means that the remaining arguments can again be passed by name.
``fun x => (fun x y => [sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") x y 8) x 1 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") ([sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") (z := 8)) (y := 1) `
```
fun x => (fun x y => [sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") x y 8) x 1 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

Parameter names are taken from the function's _type_ , and the names used for function parameters don't need to match the names used in the type. This means that local bindings that conflict with a parameter's name don't prevent the use of named parameters, because Lean avoids this conflicts by renaming the function's parameter while leaving the name intact in the type.
``let x := 15; fun x_1 y => [sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") x_1 y x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") let x := 15; [sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") (z := x) `
Here, the `x` that named `[sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example")`'s first argument has been replaced, so as to not conflict with the surrounding ``Parser.Term.let```let`:

```
let x := 15;
fun x_1 y => [sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") x_1 y x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

Even though `x` was renamed, it can still be passed by name:
``(let x := 15;   fun x_1 y => [sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") x_1 y x)   4 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") (let x := 15; [sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") (z := x)) (x := 4) `
```
(let x := 15;
  fun x_1 y => [sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") x_1 y x)
  4 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

This is because the name `x` is still used in the type. Enabling the option `pp.piBinderNames` shows the parameter names in the type:
`set_option pp.piBinderNames true [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") `let x := 15; fun x_1 y => [sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") x_1 y x : (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") let x := 15; [sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") (z := x) `
```
let x := 15;
fun x_1 y => [sum3](Terms/Function-Application/#sum3-_LPAR_in-Named-Arguments_RPAR_ "Definition of example") x_1 y x : (x y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

[Live ↪](javascript:openLiveLink\("M4UwLg+g9gDmCWUB2ACANvJYQCcB0ArkgaACYBqAhjvJQEZojAoBmlaoAUJ6SCysAIBbAMwoAFAA8UATxQAvFAC4UAOUpgAlMrUblAXhTSA1LJSn53AMQBjABYgbAawHCxARhRiAHNfuOXQVEJaSVDd21xOTCvSMUY700/B2dXYKiDWIl4w0SQzIjkgLSPbMy8jJiRJM5bFMC3FE8pcsjow2qi1KCxcRyURK6XcR6yhM02gpq64sYwIwKAVgBuErHDSWn/VPE5hZj3FbW+zM3I0MMAFhrQSFgEZBQYGDwYeAAhTF4cdSEmFDAOAIIBQmFq2xcewuTSOoxOMU2QA"\))
Optional and automatic parameters are not part of Lean's core type theory. They are encoded using the `[optParam](Terms/Function-Application/#optParam "Documentation for optParam")` and `[autoParam](Terms/Function-Application/#autoParam "Documentation for autoParam")` [gadgets](Type-Classes/Class-Declarations/#--tech-term-gadgets).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=optParam "Permalink")def
```


optParam.{u} (α : Sort u) (default : α) : Sort u


optParam.{u} (α : Sort u) (default : α) :
  Sort u


```

Gadget for optional parameter support.
A binder like `(x : α := default)` in a declaration is syntax sugar for `x : [optParam](Terms/Function-Application/#optParam "Documentation for optParam") α default`, and triggers the elaborator to attempt to use `[default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default")` to supply the argument if it is not supplied.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=autoParam "Permalink")def
```


autoParam.{u} (α : Sort u) (tactic : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")) : Sort u


autoParam.{u} (α : Sort u)
  (tactic : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")) : Sort u


```

Gadget for automatic parameter support. This is similar to the `[optParam](Terms/Function-Application/#optParam "Documentation for optParam")` gadget, but it uses the given tactic. Like `[optParam](Terms/Function-Application/#optParam "Documentation for optParam")`, this gadget only affects elaboration. For example, the tactic will _not_ be invoked during type class resolution.
##  13.4.1. Generalized Field Notation[🔗](find/?domain=Verso.Genre.Manual.section&name=generalized-field-notation "Permalink")
The [section on structure fields](The-Type-System/Inductive-Types/#structure-fields) describes the notation for projecting a field from a term whose type is a structure. Generalized field notation consists of a term followed by a dot (`.`) and an identifier, not separated by spaces.
syntaxField Notation

```
term ::= ...
    | 


The _extended field notation_ e.f is roughly short for T.f e where T is the type of e.
More precisely,




  * if e is of a function type, e.f is translated to Function.f (p := e)
where p is the first explicit parameter of function type


  * if e is of a named type T ... and there is a declaration T.f (possibly from export),
e.f is translated to T.f (p := e) where p is the first explicit parameter of type T ...



  * otherwise, if e is of a structure type,
the above is repeated for every base type of the structure.




The field index notation e.i, where i is a positive number,
is short for accessing the i-th field (1-indexed) of e if it is of a structure type. 


term.ident
```

If a term's type is a constant applied to zero or more arguments, then field notation can be used to apply a function to it, regardless of whether the term is a structure or type class instance that has fields. The use of field notation to apply other functions is called _generalized field notation_.
The identifier after the dot is looked up in the namespace of the term's type, which is the constant's name. If the type is not an application of a constant (e.g. a metavariable or a universe) then it doesn't have a namespace and generalized field notation cannot be used. As a special case, if an expression is a function, generalized field notation will look in the `Function` namespace. Therefore, `[Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add").[uncurry](The-Type-System/Functions/#Function___uncurry "Documentation for Function.uncurry")` is a use of generalized field notation that is equivalent to `[Function.uncurry](The-Type-System/Functions/#Function___uncurry "Documentation for Function.uncurry") [Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add")`.
If the field is not found, but the constant can be unfolded to yield a further type which is a constant or application of a constant, then the process is repeated with the new constant.
When a function is found, the term before the dot becomes an argument to the function. Specifically, it becomes the first explicit argument that would not be a type error. Aside from that, the application is elaborated as usual.
Generalized Field Notation
The type `[Username](Terms/Function-Application/#Username-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example")` is a constant, so functions in the `[Username](Terms/Function-Application/#Username-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example")` namespace can be applied to terms with type `[Username](Terms/Function-Application/#Username-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example")` with generalized field notation.
`def Username := [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") `
One such function is `[Username.validate](Terms/Function-Application/#Username___validate-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example")`, which checks that a username contains no leading whitespace and that only a small set of acceptable characters are used. In its definition, generalized field notation is used to call the functions `[String.isPrefixOf](Basic-Types/Strings/#String___isPrefixOf "Documentation for String.isPrefixOf")`, `[String.any](Basic-Types/Strings/#String___any "Documentation for String.any")`, `[Char.isAlpha](Basic-Types/Characters/#Char___isAlpha "Documentation for Char.isAlpha")`, and `[Char.isDigit](Basic-Types/Characters/#Char___isDigit "Documentation for Char.isDigit")`. In the case of `[String.isPrefixOf](Basic-Types/Strings/#String___isPrefixOf "Documentation for String.isPrefixOf")`, which takes two `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` arguments, `" "` is used as the first because it's the term before the dot. `[String.any](Basic-Types/Strings/#String___any "Documentation for String.any")` can be called on `name` using generalized field notation even though it has type `[Username](Terms/Function-Application/#Username-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example")` because `Username.any` is not defined and `[Username](Terms/Function-Application/#Username-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example")` unfolds to `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`.
`def Username.validate (name : [Username](Terms/Function-Application/#Username-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example")) : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   if " ".[isPrefixOf](Basic-Types/Strings/#String___isPrefixOf "Documentation for String.isPrefixOf") name then     [throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") "Unexpected leading whitespace"   if name.[any](Basic-Types/Strings/#String___any "Documentation for String.any") [notOk](Terms/Function-Application/#Username___validate___notOk-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example") then     [throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") "Unexpected character"   return () where   notOk (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") :=     !c.[isAlpha](Basic-Types/Characters/#Char___isAlpha "Documentation for Char.isAlpha") &&     !c.[isDigit](Basic-Types/Characters/#Char___isDigit "Documentation for Char.isDigit") &&     !c ∈ ['_', ' ']  def adminUser : [Username](Terms/Function-Application/#Username-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example") := "admin" `
However, `[Username.validate](Terms/Function-Application/#Username___validate-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example")` can't be called on `"root"` using field notation, because `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` does not unfold to `[Username](Terms/Function-Application/#Username-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example")`.
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") "admin".`Invalid field `validate`: The environment does not contain `String.validate`, so it is not possible to project the field `validate` from an expression   "admin" of type `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")``validate `
```
Invalid field `validate`: The environment does not contain `String.validate`, so it is not possible to project the field `validate` from an expression
  "admin"
of type `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`
```

`[adminUser](Terms/Function-Application/#adminUser-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example")`, on the other hand, has type `[Username](Terms/Function-Application/#Username-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example")`, so the `[Username.validate](Terms/Function-Application/#Username___validate-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example")` function can be invoked with generalized field notation:
``Except.ok ()`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [adminUser](Terms/Function-Application/#adminUser-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example").[validate](Terms/Function-Application/#Username___validate-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example") `
```
Except.ok ()
```

Going in the other direction, `[String.any](Basic-Types/Strings/#String___any "Documentation for String.any")` **can** be called on the `[Username](Terms/Function-Application/#Username-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example")` value `[adminUser](Terms/Function-Application/#adminUser-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example")` with generalized field notation, because the type `[Username](Terms/Function-Application/#Username-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example")` unfolds to `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`.
``[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [adminUser](Terms/Function-Application/#adminUser-_LPAR_in-Generalized-Field-Notation_RPAR_ "Definition of example").[any](Basic-Types/Strings/#String___any "Documentation for String.any") (· == 'm') `
```
[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")
```

[Live ↪](javascript:openLiveLink\("CYUwZgBAqgziBOA7AhgWxBAXAXggZQBd4BLRAcwCgLRJYEV0A6AN2QBtjhkCMAKBjJmhwkaEAEosEAKIAPAMYgADgXxFSZaImKqcEYAHsKECMUgAiCOcbEYABXjhisgPKQBEAgAsQiYyc8veAMAdysoRBBZJRB5HmAINhBkYA0IEK8dEBglZEVzfzMIAUZkRABPYoMCFwBrQN9/E29gsPMIqJi4kAT5L2R4PJ54ApNHAgBXJAhecQoMhBB/RGq6mfkpAGF++EkhACEDAzYsbCaIAEJ5GxgAQTYlfogAMmfzq5uAEWIyHRe3gKXDaACCIIABtADkAH0IQAaCAQhEAXSoNAgKVQpDo8Ck2I8enMGNIBQoAGIQKwTkTENiWOxONwlmSKex0cBMTSRKUKjMAO0QbC4CGoCHiIA"\))
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=pp.fieldNotation "Permalink")option
```
pp.fieldNotation
```

Default value: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
(pretty printer) use field notation when pretty printing, including for structure projections, unless '@[pp_nodot]' is applied
attributeControlling Field Notation
The `pp_nodot` attribute causes Lean's pretty printer to not use field notation when printing a function.

```
attr ::= ...
    | pp_nodot
```

Turning Off Field Notation
`[Nat.half](Terms/Function-Application/#Nat___half-_LPAR_in-Turning-Off-Field-Notation_RPAR_ "Definition of example")` is printed using field notation by default.
`def Nat.half : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   | 0 | 1 => 0   | n + 2 => n.[half](Terms/Function-Application/#Nat___half-_LPAR_in-Turning-Off-Field-Notation_RPAR_ "Definition of example") + 1 ```[Nat.zero](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.zero").[half](Terms/Function-Application/#Nat___half-_LPAR_in-Turning-Off-Field-Notation_RPAR_ "Definition of example") : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [Nat.half](Terms/Function-Application/#Nat___half-_LPAR_in-Turning-Off-Field-Notation_RPAR_ "Definition of example") [Nat.zero](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.zero") `
```
[Nat.zero](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.zero").[half](Terms/Function-Application/#Nat___half-_LPAR_in-Turning-Off-Field-Notation_RPAR_ "Definition of example") : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

Adding `pp_nodot` to `[Nat.half](Terms/Function-Application/#Nat___half-_LPAR_in-Turning-Off-Field-Notation_RPAR_ "Definition of example")` causes ordinary function application syntax to be used instead when displaying the term.
`[attribute](Attributes/#Lean___Parser___Command___attribute "Documentation for syntax") [pp_nodot] [Nat.half](Terms/Function-Application/#Nat___half-_LPAR_in-Turning-Off-Field-Notation_RPAR_ "Definition of example")  `[Nat.half](Terms/Function-Application/#Nat___half-_LPAR_in-Turning-Off-Field-Notation_RPAR_ "Definition of example") [Nat.zero](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.zero") : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [Nat.half](Terms/Function-Application/#Nat___half-_LPAR_in-Turning-Off-Field-Notation_RPAR_ "Definition of example") [Nat.zero](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.zero") `
```
[Nat.half](Terms/Function-Application/#Nat___half-_LPAR_in-Turning-Off-Field-Notation_RPAR_ "Definition of example") [Nat.zero](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.zero") : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

[Live ↪](javascript:openLiveLink\("CYUwZgBAcghgLgOgBYwDaQFzXhQSYTbgCgIIAfCABjIgEYIBeAPkuOoDsIBqCAJgebbI0kbjUKEAxAGMkIKQGsCQ9EoBeIAE4B7cfDgaAlgCMArnBAQA2gAdrAfTZbgWuAF0lKdOOmyFH4WqaWkA"\))
##  13.4.2. Pipeline Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Terms--Function-Application--Pipeline-Syntax "Permalink")
Pipeline syntax provides alternative ways to write function applications. Repeated pipelines use parsing precedence instead of nested parentheses to nest applications of functions to positional arguments.
syntaxPipelines
Right pipe notation applies the term to the right of the pipe to the one on its left.

```
term ::= ...
    | 


Haskell-like pipe operator |>. x |> f means the same as f x,
and it chains such that x |> f |> g is interpreted as g (f x).


term |> term
```

Left pipe notation applies the term on the left of the pipe to the one on its right.

```
term ::= ...
    | 


Haskell-like pipe operator <|. f <| x means the same as f x,
except that it parses x with lower precedence, which means that f <| g <| x
is interpreted as f (g x) rather than (f g) x.


term <| term
```

The intuition behind right pipeline notation is that the values on the left are being fed to the first function, its results are fed to the second one, and so forth. In left pipeline notation, values on the right are fed leftwards.
Right pipeline notation
Right pipelines can be used to call a series of functions on a term. For readers, they tend to emphasize the data that's being transformed.
``'!'`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") "Hello!" |> String.toList |> [List.reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse") |> [List.head!](Basic-Types/Linked-Lists/#List___head___-next "Documentation for List.head!") `
```
'!'
```

[Live ↪](javascript:openLiveLink\("MQUwbghgNgBARACRFKB7AhHGAfAfDAZQBcAnASwDsBzAOiNQBkyBnInfJ1mk8EE5kOxiciNABYgIAE3RA"\))
Left pipeline notation
Left pipelines can be used to call a series of functions on a term. They tend to emphasize the functions over the data.
``'!'`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [List.head!](Basic-Types/Linked-Lists/#List___head___-next "Documentation for List.head!") <| [List.reverse](Basic-Types/Linked-Lists/#List___reverse "Documentation for List.reverse") <| String.toList <| "Hello!" `
```
'!'
```

[Live ↪](javascript:openLiveLink\("MQUwbghgNgBAMgSwM4BcB0ALEEAmBCGAHgB95l0AncECpEI0gZRQoQDsBzNFAe0VQYwARAAkQUKDzxCgA"\))
syntaxPipeline Fields
There is a version of pipeline notation that's used for [generalized field notation](Terms/Function-Application/#--tech-term-generalized-field-notation).

```
term ::= ...
    | 


e |>.x is a shorthand for (e).x.
It is especially useful for avoiding parentheses with repeated applications.


term |>.ident
```

```
term ::= ...
    | 


e |>.x is a shorthand for (e).x.
It is especially useful for avoiding parentheses with repeated applications.


term |>.fieldIdx
```

`e |>.f arg` is an alternative syntax for `(e).f arg`.
Pipeline Fields
Some functions are inconvenient to use with pipelines because their argument order is not conducive. For example, `[Array.push](Basic-Types/Arrays/#Array___push "Documentation for Array.push")` takes an array as its first argument, not a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, leading to this error:
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #[1, 2, 3] |> [Array.push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") `failed to synthesize instance of type class   [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ?m.2) 4 numerals are polymorphic in Lean, but the numeral `4` cannot be used in a context where the expected type is   [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ?m.2 due to the absence of the instance above  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`4 `
```
failed to synthesize instance of type class
  [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ?m.2) 4
numerals are polymorphic in Lean, but the numeral `4` cannot be used in a context where the expected type is
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ?m.2
due to the absence of the instance above

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```

Using pipeline field notation causes the array to be inserted at the first type-correct position:
``[#[](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 4[]](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #[1, 2, 3] |>.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") 4 `
```
[#[](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 4[]](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")
```

This process can be iterated:
``[#[](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 4[]](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #[1, 2, 3] |>.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") 4 |>.[reverse](Basic-Types/Arrays/#Array___reverse "Documentation for Array.reverse") |>.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") 0 |>.[reverse](Basic-Types/Arrays/#Array___reverse "Documentation for Array.reverse") `
```
[#[](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")0[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 4[]](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")
```

[Live ↪](javascript:openLiveLink\("MQUwbghgNgBMDaBGANDATKgzAXRgHwD4A6ABwFcBnACxgBYAoe0SWBFdLXQ0ym2/YgCdwIQRRACe1GAAZJwsKPFA"\))
[←13.3. Functions](Terms/Functions/#function-terms "13.3. Functions")[13.5. Numeric Literals→](Terms/Numeric-Literals/#The-Lean-Language-Reference--Terms--Numeric-Literals "13.5. Numeric Literals")

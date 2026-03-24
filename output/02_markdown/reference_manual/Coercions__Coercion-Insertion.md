[←11. Coercions](Coercions/#coercions "11. Coercions")[11.2. Coercing Between Types→](Coercions/Coercing-Between-Types/#ordinary-coercion "11.2. Coercing Between Types")
#  11.1. Coercion Insertion[🔗](find/?domain=Verso.Genre.Manual.section&name=coercion-insertion "Permalink")
The process of searching for a coercion from one type to another is called _coercion insertion_. Coercion insertion is attempted in the following situations where an error would otherwise occur:
  * The expected type for a term is not equal to the type found for the term.
  * A type or proposition is expected, but the term's type is not a [universe](The-Type-System/Universes/#--tech-term-universes).
  * A term is applied as though it were a function, but its type is not a function type.


Coercions are also inserted when they are explicitly requested. Each situation in which coercions may be inserted has a corresponding prefix operator that triggers the appropriate insertion.
Because coercions are inserted automatically, nested [type ascriptions](Terms/Type-Ascription/#--tech-term-Type-ascriptions) provide a way to precisely control the types involved in a coercion. If `α` and `β` are not the same type, `((e : α) : β)` arranges for `e` to have type `α` and then inserts a coercion from `α` to `β`.
When a coercion is discovered, the instances used to find it are unfolded and removed from the resulting term. To the extent possible, calls to `[Coe.coe](Coercions/#Coe___mk "Documentation for Coe.coe")` and related functions do not occur in the final term. This process of unfolding makes terms more readable. Even more importantly, it means that coercions can control the evaluation of the coerced terms by wrapping them in functions.
Controlling Evaluation with Coercions
The structure `[Later](Coercions/Coercion-Insertion/#Later-_LPAR_in-Controlling-Evaluation-with-Coercions_RPAR_ "Definition of example")` represents a term that can be evaluated in the future, by calling the contained function.
`structure Later (α : Type u) where   get : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → α `
A coercion from any value to a later value is performed by creating a function that wraps it.
`instance : [CoeTail](Coercions/Coercing-Between-Types/#CoeTail___mk "Documentation for CoeTail") α ([Later](Coercions/Coercion-Insertion/#Later-_LPAR_in-Controlling-Evaluation-with-Coercions_RPAR_ "Definition of example") α) where   [coe](Coercions/Coercing-Between-Types/#CoeTail___mk "Documentation for CoeTail.coe") x := { [get](Coercions/Coercion-Insertion/#Later___get-_LPAR_in-Controlling-Evaluation-with-Coercions_RPAR_ "Definition of example") := fun () => x } `
However, if coercion insertion resulted in an application of `[CoeTail.coe](Coercions/Coercing-Between-Types/#CoeTail___mk "Documentation for CoeTail.coe")`, then this coercion would not have the desired effect at runtime, because the coerced value would be evaluated and then saved in the function's closure. Because coercion implementations are unfolded, this instance is nonetheless useful.
`def tomorrow : [Later](Coercions/Coercion-Insertion/#Later-_LPAR_in-Controlling-Evaluation-with-Coercions_RPAR_ "Definition of example") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=   ([Nat.fold](Basic-Types/Natural-Numbers/#Nat___fold "Documentation for Nat.fold") 10000     (init := "")     (fun _ _ s => s ++ "tomorrow") : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) `
Printing the resulting definition shows that the computation is inside the function's body:
``def tomorrow : [Later](Coercions/Coercion-Insertion/#Later-_LPAR_in-Controlling-Evaluation-with-Coercions_RPAR_ "Definition of example") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := { [get](Coercions/Coercion-Insertion/#Later___get-_LPAR_in-Controlling-Evaluation-with-Coercions_RPAR_ "Definition of example") := fun x => [Nat.fold](Basic-Types/Natural-Numbers/#Nat___fold "Documentation for Nat.fold") 10000 (fun x x_1 s => s [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") "tomorrow") "" }`#print [tomorrow](Coercions/Coercion-Insertion/#tomorrow-_LPAR_in-Controlling-Evaluation-with-Coercions_RPAR_ "Definition of example") `
```
def tomorrow : [Later](Coercions/Coercion-Insertion/#Later-_LPAR_in-Controlling-Evaluation-with-Coercions_RPAR_ "Definition of example") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=
{ [get](Coercions/Coercion-Insertion/#Later___get-_LPAR_in-Controlling-Evaluation-with-Coercions_RPAR_ "Definition of example") := fun x => [Nat.fold](Basic-Types/Natural-Numbers/#Nat___fold "Documentation for Nat.fold") 10000 (fun x x_1 s => s [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") "tomorrow") "" }
```

[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgDIEMTzIgFIRuBEBciAKgJ4AOSEAlIgO4AWm8AUIogObwiGICqAOwCWPQEmEiXCxZCBoVAKhIiAYQD28YqiEAbCTjQYsuWo2ZtEUdYgAehALyIA3p273EAMwgCctOwD4bRABfKQATeHdEEFUAW1UwMFU6XgNMRABlcBkOe3NsADl0ADp3VW1QxABGAAZa6vN2bBkRNwAiVuoGnE9vAH1EfuBEf0QhgGoxxFbouISkjt5MsGzOlgBicmWBHhn4xLogA"\))
Duplicate Evaluation in Coercions
Because the contents of `[Coe](Coercions/#Coe___mk "Documentation for Coe")` instances are unfolded during coercion insertion, coercions that use their argument more than once should be careful to ensure that evaluation occurs just once. This can be done by using a helper function that is not part of the instance, or by using ``Lean.Parser.Term.let : term`
``let` to evaluate the coerced term and then reuse its resulting value.
The structure `[Twice](Coercions/Coercion-Insertion/#Twice-_LPAR_in-Duplicate-Evaluation-in-Coercions_RPAR_ "Definition of example")` requires that both fields have the same value:
`structure Twice (α : Type u) where   first : α   second : α   first_eq_second : first = second `
One way to define a coercion from `α` to `[Twice](Coercions/Coercion-Insertion/#Twice-_LPAR_in-Duplicate-Evaluation-in-Coercions_RPAR_ "Definition of example") α` is with a helper function `[twice](Coercions/Coercion-Insertion/#twice-_LPAR_in-Duplicate-Evaluation-in-Coercions_RPAR_ "Definition of example")`. The `coe` attribute marks it as a coercion so it can be shown correctly in proof goals and error messages.
`@[[coe](Coercions/Coercing-Between-Types/#Lean___Attr___coe "Documentation for syntax")] def twice (x : α) : [Twice](Coercions/Coercion-Insertion/#Twice-_LPAR_in-Duplicate-Evaluation-in-Coercions_RPAR_ "Definition of example") α where   [first](Coercions/Coercion-Insertion/#Twice___first-_LPAR_in-Duplicate-Evaluation-in-Coercions_RPAR_ "Definition of example") := x   [second](Coercions/Coercion-Insertion/#Twice___second-_LPAR_in-Duplicate-Evaluation-in-Coercions_RPAR_ "Definition of example") := x   [first_eq_second](Coercions/Coercion-Insertion/#Twice___first_eq_second-_LPAR_in-Duplicate-Evaluation-in-Coercions_RPAR_ "Definition of example") := [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")  instance : [Coe](Coercions/#Coe___mk "Documentation for Coe") α ([Twice](Coercions/Coercion-Insertion/#Twice-_LPAR_in-Duplicate-Evaluation-in-Coercions_RPAR_ "Definition of example") α) := ⟨[twice](Coercions/Coercion-Insertion/#twice-_LPAR_in-Duplicate-Evaluation-in-Coercions_RPAR_ "Definition of example")⟩ `
When the `[Coe](Coercions/#Coe___mk "Documentation for Coe")` instance is unfolded, the call to `[twice](Coercions/Coercion-Insertion/#twice-_LPAR_in-Duplicate-Evaluation-in-Coercions_RPAR_ "Definition of example")` remains, which causes its argument to be evaluated before the body of the function is executed. As a result, the ``Lean.Parser.Term.dbgTrace : term`
``dbg_trace` is included in the resulting term just once:
``{ first := 5, second := 5, first_eq_second := _ }``hello `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ((dbg_trace "hello"; 5 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Twice](Coercions/Coercion-Insertion/#Twice-_LPAR_in-Duplicate-Evaluation-in-Coercions_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) `
This is used to demonstrate the effect:

```
hello

```

Inlining the helper into the `[Coe](Coercions/#Coe___mk "Documentation for Coe")` instance results in a term that duplicates the ``Lean.Parser.Term.dbgTrace : term`
``dbg_trace`:
`instance : [Coe](Coercions/#Coe___mk "Documentation for Coe") α ([Twice](Coercions/Coercion-Insertion/#Twice-_LPAR_in-Duplicate-Evaluation-in-Coercions_RPAR_ "Definition of example") α) where   [coe](Coercions/#Coe___mk "Documentation for Coe.coe") x := ⟨x, x, [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")⟩  `{ first := 5, second := 5, first_eq_second := _ }``hello hello `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ((dbg_trace "hello"; 5 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Twice](Coercions/Coercion-Insertion/#Twice-_LPAR_in-Duplicate-Evaluation-in-Coercions_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) `
```
hello
hello

```

Introducing an intermediate name for the result of the evaluation prevents the duplication of ``Lean.Parser.Term.dbgTrace : term`
``dbg_trace`:
`instance : [Coe](Coercions/#Coe___mk "Documentation for Coe") α ([Twice](Coercions/Coercion-Insertion/#Twice-_LPAR_in-Duplicate-Evaluation-in-Coercions_RPAR_ "Definition of example") α) where   [coe](Coercions/#Coe___mk "Documentation for Coe.coe") x := let y := x; ⟨y, y, [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")⟩  `{ first := 5, second := 5, first_eq_second := _ }``hello `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ((dbg_trace "hello"; 5 : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Twice](Coercions/Coercion-Insertion/#Twice-_LPAR_in-Duplicate-Evaluation-in-Coercions_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) `
```
hello

```

[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgCoHcCWUkApCNwIgLhQE8AHJCASkVQAt4EAoRRAM3TFEMV2cWHhQA9gDsAJt14t2nEAH14ARzkDh47jK4BefoNFjGjAAIBtYfAC6jMfFaIQGLImwAPSdSJpMSfHQbw+TRBCHRc+VX0QxDDpDlAFZQj1Ah0wVgAbQ3QRUABDESciAGEhH2cvJ1wPHUAL8gdvQEvyQwBieAA3XPTnbDEAIwBzOXBcpwAienT0oVGAbkQAVm4AOVyQDxRHJBW1rJyQfMLEErLsCp9qPyYWc2iompcAGmintPSmxlaOruwegaGwEZIcbwSbTOaLIjbdZnRBQ3Z5ApIYqlHjlTY8C70K6IG5uFKIdLwYLEKIuOY1YhPSmIV7vT6dbp9QbDMYTKazBbLVbQ9FQoA"\))
[←11. Coercions](Coercions/#coercions "11. Coercions")[11.2. Coercing Between Types→](Coercions/Coercing-Between-Types/#ordinary-coercion "11.2. Coercing Between Types")

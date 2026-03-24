[←22.2. Iterator Definitions](Iterators/Iterator-Definitions/#The-Lean-Language-Reference--Iterators--Iterator-Definitions "22.2. Iterator Definitions")[22.4. Iterator Combinators→](Iterators/Iterator-Combinators/#The-Lean-Language-Reference--Iterators--Iterator-Combinators "22.4. Iterator Combinators")
#  22.3. Consuming Iterators[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Iterators--Consuming-Iterators "Permalink")
There are three primary ways to consume an iterator: 

Converting it to a sequential data structure
    
The functions `[Iter.toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList")`, `[Iter.toArray](Iterators/Consuming-Iterators/#Std___Iter___toArray "Documentation for Std.Iter.toArray")`, and their monadic equivalents `[IterM.toList](Iterators/Consuming-Iterators/#Std___IterM___toList "Documentation for Std.IterM.toList")` and `[IterM.toArray](Iterators/Consuming-Iterators/#Std___IterM___toArray "Documentation for Std.IterM.toArray")`, construct a lists or arrays that contain the values from the iterator, in order. Only [finite iterators](Iterators/Iterator-Definitions/#--tech-term-Finite) can be converted to sequential data structures. 

``Lean.Parser.Term.doFor : doElem`
`for x in e do s` iterates over `e` assuming `e`'s type has an instance of the `ForIn` typeclass. `break` and `continue` are supported inside `for` loops. `for x in e, x2 in e2, ... do s` iterates of the given collections in parallel, until at least one of them is exhausted. The types of `e2` etc. must implement the `Std.ToStream` typeclass.
``for` loops
    
A ``Lean.Parser.Term.doFor : doElem`
`for x in e do s` iterates over `e` assuming `e`'s type has an instance of the `ForIn` typeclass. `break` and `continue` are supported inside `for` loops. `for x in e, x2 in e2, ... do s` iterates of the given collections in parallel, until at least one of them is exhausted. The types of `e2` etc. must implement the `Std.ToStream` typeclass.
``for` loop can consume an iterator, making each value available in its body. This requires that the iterator have an instance of `[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop")` for the loop's monad. 

Stepping through iterators
    
Iterators can provide their values one-by-one, with client code explicitly requesting each new value in turn. When stepped through, iterators perform only enough computation to yield the requested value.
Converting Iterators to Lists
In `[countdown](Iterators/Consuming-Iterators/#countdown-_LPAR_in-Converting-Iterators-to-Lists_RPAR_ "Definition of example")`, an iterator over a range is transformed into an iterator over strings using `[Iter.map](Iterators/Iterator-Combinators/#Std___Iter___map "Documentation for Std.Iter.map")`. This call to `[Iter.map](Iterators/Iterator-Combinators/#Std___Iter___map "Documentation for Std.Iter.map")` does not result in any iteration over the range until `[Iter.toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList")` is called, at which point each element of the range is produced and transformed into a string.
`def countdown : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=   let steps : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := (0...10).[iter](Basic-Types/Ranges/#Std___Rco___iter "Documentation for Std.Rco.iter").[map](Iterators/Iterator-Combinators/#Std___Iter___map "Documentation for Std.Iter.map") (s!"{10 - ·}!\n")   [String.join](Basic-Types/Strings/#String___join "Documentation for String.join") steps.[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList")  `10! 9! 8! 7! 6! 5! 4! 3! 2! 1!  `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") [countdown](Iterators/Consuming-Iterators/#countdown-_LPAR_in-Converting-Iterators-to-Lists_RPAR_ "Definition of example") `
```
10!
9!
8!
7!
6!
5!
4!
3!
2!
1!


```

[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAZRgEwHQBECGNOoJIwCmU20AzgFAURiEB2iKVyhAZnAMYQCudKEAdwYAuRlGB0A5nGEBeCnDgAbQvDJEwZGXALExE6XLgAKAAyoLARlMBKVMCJRUITGBNkAhACIA3tbgAtHAA7QC+HgA6dF42CvpSqABWEBJw6oSaqDAQADLA6lQAxIQAbphKOgDyqGDifEoMXLz8QkA"\))
Converting Infinite Iterators to Lists
Attempting to construct a list of all the natural numbers from an iterator will produce an endless loop:
`def allNats : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") :=   let steps : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := (0...*).[iter](Basic-Types/Ranges/#Std___Rci___iter "Documentation for Std.Rci.iter")   steps.[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList") `
The combinator `[Iter.ensureTermination](Iterators/Iterator-Definitions/#Std___Iter___ensureTermination "Documentation for Std.Iter.ensureTermination")` results in an iterator where non-termination is ruled out. These iterators are guaranteed to terminate after finitely many steps, and thus cannot be used when Lean cannot prove the iterator finite.
`def allNats : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") :=   let steps := (0...*).[iter](Basic-Types/Ranges/#Std___Rci___iter "Documentation for Std.Rci.iter").[ensureTermination](Iterators/Iterator-Definitions/#Std___Iter___ensureTermination "Documentation for Std.Iter.ensureTermination")   `failed to synthesize instance of type class   [Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite") (Rxi.Iterator [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`steps.toList `
The resulting error message states that there is no `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")` instance:

```
failed to synthesize instance of type class
  [Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite") (Rxi.Iterator [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```

[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAZRgEwHQBECGNOoJIwCmU20AzgFAURiEB2iKQA"\))
Consuming Iterators in Loops
This program creates an iterator of strings from a range, and then consumes the strings in a ``Lean.Parser.Term.doFor : doElem`
``for` loop:
`def countdown (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let steps : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := (0...n).[iter](Basic-Types/Ranges/#Std___Rco___iter "Documentation for Std.Rco.iter").[map](Iterators/Iterator-Combinators/#Std___Iter___map "Documentation for Std.Iter.map") (s!"{n - ·}!")   for i in steps do     [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") i   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "Blastoff!"  `5! 4! 3! 2! 1! Blastoff! `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [countdown](Iterators/Consuming-Iterators/#countdown-_LPAR_in-Consuming-Iterators-in-Loops_RPAR_ "Definition of example") 5 `
```
5!
4!
3!
2!
1!
Blastoff!

```

[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAZRgEwHQBECGNOoJIwCmU20AzgFAURiEB2iKVyhAZnAMYQCudKEAdwYAKBgC44AOWwBKOBLwB5OAFU6weGIC8cZBApw4AG0LwyRMGXlwCxRlGB0A5vJ3CADKi90ZqDcVQQTDA4YTIAQgAiAG8GAFo4AHaAXyiZAzhWaDhgHIZzQktdfUNDJVQwBz4jBmAM8srHGBq4SIAhI0xzCFZWKKoAYkIAN0wjTh4+PSE4AFYgA"\))
Consuming Iterators Directly
The function `[countdown](Iterators/Consuming-Iterators/#countdown-_LPAR_in-Consuming-Iterators-Directly_RPAR_ "Definition of example")` calls the range iterator's `[step](Iterators/Consuming-Iterators/#Std___Iter___step "Documentation for Std.Iter.step")` function directly, handling each of the three possible cases.
`def countdown (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let steps : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := (0...n).[iter](Basic-Types/Ranges/#Std___Rco___iter "Documentation for Std.Rco.iter")   [go](Iterators/Consuming-Iterators/#countdown___go-_LPAR_in-Consuming-Iterators-Directly_RPAR_ "Definition of example") steps where   go iter := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")     match iter.[step](Iterators/Consuming-Iterators/#Std___Iter___step "Documentation for Std.Iter.step") with     | [.done](Iterators/Iterator-Definitions/#Std___PlausibleIterStep___done "Documentation for Std.PlausibleIterStep.done") _ => [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ()     | [.skip](Iterators/Iterator-Definitions/#Std___PlausibleIterStep___skip "Documentation for Std.PlausibleIterStep.skip") iter' _ => [go](Iterators/Consuming-Iterators/#countdown___go-_LPAR_in-Consuming-Iterators-Directly_RPAR_ "Definition of example") iter'     | [.yield](Iterators/Iterator-Definitions/#Std___PlausibleIterStep___yield "Documentation for Std.PlausibleIterStep.yield") iter' i _ => do       [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"{i}!"       if i == 2 then         [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Almost there..."       [go](Iterators/Consuming-Iterators/#countdown___go-_LPAR_in-Consuming-Iterators-Directly_RPAR_ "Definition of example") iter'   termination_by iter.[finitelyManySteps](Iterators/Consuming-Iterators/#Std___Iter___finitelyManySteps "Documentation for Std.Iter.finitelyManySteps") `
[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAZRgEwHQBECGNOoJIwCmU20AzgFAURiEB2iKVyhAZnAMYQCudKEAdwYAKBgC44AOWwBKOBLwB5OAFU6weGIC8cZBApw4AG0LwyRMGXlwCxKdnk7hABlRu6M1BuIG4Acwg4c0JLCgEAC2JCXwC4byhHXX1DQxBsDnC4oihUYLA4AQ1w30MAHzhUPTpCOAB9OC0APjgwbiga4RkSuHLcgGtgfPiAcjqG5tiR7t6AT2BCI2Qs4lHgMaak7sMlVDAoYD4jBjIAQgAiAG9gAF9zrbj2Na0dACY4GEi6e+3FXf3D47nACCRhAEHM70i7TcqDO90m2WGvmyIAO2GAEDotQARjNljlWAdvEYZgBZTB0GZIEJkIA"\))
##  22.3.1. Stepping Iterators[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Iterators--Consuming-Iterators--Stepping-Iterators "Permalink")
Iterators are manually stepped using `[Iter.step](Iterators/Consuming-Iterators/#Std___Iter___step "Documentation for Std.Iter.step")` or `[IterM.step](Iterators/Consuming-Iterators/#Std___IterM___step "Documentation for Std.IterM.step")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.step "Permalink")def
```


Std.Iter.step.{w} {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) :
  it.[Step](Iterators/Iterator-Definitions/#Std___Iter___Step "Documentation for Std.Iter.Step")


Std.Iter.step.{w} {α β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) :
  it.[Step](Iterators/Iterator-Definitions/#Std___Iter___Step "Documentation for Std.Iter.Step")


```

Makes a single step with the given iterator `it`, potentially emitting a value and providing a succeeding iterator. If this function is used recursively, termination can sometimes be proved with the termination measures `it.[finitelyManySteps](Iterators/Consuming-Iterators/#Std___Iter___finitelyManySteps "Documentation for Std.Iter.finitelyManySteps")` and `it.[finitelyManySkips](Iterators/Consuming-Iterators/#Std___Iter___finitelyManySkips "Documentation for Std.Iter.finitelyManySkips")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.step "Permalink")def
```


Std.IterM.step.{w, w'} {α : Type w} {m : Type w → Type w'} {β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : m ([Std.Shrink](Iterators/Iterator-Definitions/#Std___Shrink "Documentation for Std.Shrink") it.[Step](Iterators/Iterator-Definitions/#Std___IterM___Step "Documentation for Std.IterM.Step"))


Std.IterM.step.{w, w'} {α : Type w}
  {m : Type w → Type w'} {β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) :
  m ([Std.Shrink](Iterators/Iterator-Definitions/#Std___Shrink "Documentation for Std.Shrink") it.[Step](Iterators/Iterator-Definitions/#Std___IterM___Step "Documentation for Std.IterM.Step"))


```

Makes a single step with the given iterator `it`, potentially emitting a value and providing a succeeding iterator. If this function is used recursively, termination can sometimes be proved with the termination measures `it.[finitelyManySteps](Iterators/Consuming-Iterators/#Std___IterM___finitelyManySteps "Documentation for Std.IterM.finitelyManySteps")` and `it.[finitelyManySkips](Iterators/Consuming-Iterators/#Std___IterM___finitelyManySkips "Documentation for Std.IterM.finitelyManySkips")`.
###  22.3.1.1. Termination[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Iterators--Consuming-Iterators--Stepping-Iterators--Termination "Permalink")
When manually stepping an finite iterator, the termination measures `[finitelyManySteps](Iterators/Consuming-Iterators/#Std___Iter___finitelyManySteps "Documentation for Std.Iter.finitelyManySteps")` and `[finitelyManySkips](Iterators/Consuming-Iterators/#Std___Iter___finitelyManySkips "Documentation for Std.Iter.finitelyManySkips")` can be used to express that each step brings iteration closer to the end. The proof automation for [well-founded recursion](Definitions/Recursive-Definitions/#well-founded-recursion) is pre-configured to prove that recursive calls after steps reduce these measures.
Finitely Many Skips
This function returns the first element of an iterator, if there is one, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` otherwise. Because the iterator must be productive, it is guaranteed to return an element after at most a finite number of `[skip](Iterators/Iterator-Definitions/#Std___PlausibleIterStep___skip "Documentation for Std.PlausibleIterStep.skip")`s. This function terminates even for infinite iterators.
`def getFirst {α β} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]     (it : @[Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") α β) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") it.[step](Iterators/Consuming-Iterators/#Std___Iter___step "Documentation for Std.Iter.step") [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | [.done](Iterators/Iterator-Definitions/#Std___PlausibleIterStep___done "Documentation for Std.PlausibleIterStep.done") .. => [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")   | [.skip](Iterators/Iterator-Definitions/#Std___PlausibleIterStep___skip "Documentation for Std.PlausibleIterStep.skip") it' .. => [getFirst](Iterators/Consuming-Iterators/#getFirst-_LPAR_in-Finitely-Many-Skips_RPAR_ "Definition of example") it'   | [.yield](Iterators/Iterator-Definitions/#Std___PlausibleIterStep___yield "Documentation for Std.PlausibleIterStep.yield") _ x .. => [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x termination_by it.[finitelyManySkips](Iterators/Consuming-Iterators/#Std___Iter___finitelyManySkips "Documentation for Std.Iter.finitelyManySkips") `
[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAZRgEwHQBECGNOoJIwCmU20AzgFAURiEB2iK1tDBxpUZcAFAApQRkAVwDGMYADdCASirJCAMzgBzQjABiwTvADegRuA4gJuAAvnADabEjGhwDeZEYC65/oNHiptuPccU4/nmB4AC44AAFLL0NpOFCAeTBxCAZDWIBePzgQbBEACzgg1DIiMDgAdyDczIAfOFRkZMI61Dg0gD44OkaaurIAa2BSoIByZtaO1Q0tYoKYYZ7UAE9gQgAbBwB9OAAPMfa4MCEoJu2KIigQYDpsYGSNgCNF2dQFK6C1xYBZTDpFhAGwGQgA"\))
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.finitelyManySteps "Permalink")def
```


Std.Iter.finitelyManySteps.{w} {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [IterM.TerminationMeasures.Finite](Iterators/Consuming-Iterators/#Std___IterM___TerminationMeasures___Finite___mk "Documentation for Std.IterM.TerminationMeasures.Finite") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")


Std.Iter.finitelyManySteps.{w}
  {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) :
  [IterM.TerminationMeasures.Finite](Iterators/Consuming-Iterators/#Std___IterM___TerminationMeasures___Finite___mk "Documentation for Std.IterM.TerminationMeasures.Finite") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")


```

Termination measure to be used in well-founded recursive functions recursing over a finite iterator (see also `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")`).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.finitelyManySteps "Permalink")def
```


Std.IterM.finitelyManySteps.{w, w'} {α : Type w} {m : Type w → Type w'}
  {β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite") α m] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) :
  [IterM.TerminationMeasures.Finite](Iterators/Consuming-Iterators/#Std___IterM___TerminationMeasures___Finite___mk "Documentation for Std.IterM.TerminationMeasures.Finite") α m


Std.IterM.finitelyManySteps.{w, w'}
  {α : Type w} {m : Type w → Type w'}
  {β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite") α m] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) :
  [IterM.TerminationMeasures.Finite](Iterators/Consuming-Iterators/#Std___IterM___TerminationMeasures___Finite___mk "Documentation for Std.IterM.TerminationMeasures.Finite") α m


```

Termination measure to be used in well-founded recursive functions recursing over a finite iterator (see also `[Finite](Iterators/Iterator-Definitions/#Std___Iterators___Finite___mk "Documentation for Std.Iterators.Finite")`).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.TerminationMeasures.Finite.it "Permalink")structure
```


Std.IterM.TerminationMeasures.Finite.{w, w'} (α : Type w)
  (m : Type w → Type w') {β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] : Type w


Std.IterM.TerminationMeasures.Finite.{w,
    w'}
  (α : Type w) (m : Type w → Type w')
  {β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] : Type w


```

This type is a wrapper around `[IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM")` so that it becomes a useful termination measure for recursion over finite iterators. See also `[IterM.finitelyManySteps](Iterators/Consuming-Iterators/#Std___IterM___finitelyManySteps "Documentation for Std.IterM.finitelyManySteps")` and `[Iter.finitelyManySteps](Iterators/Consuming-Iterators/#Std___Iter___finitelyManySteps "Documentation for Std.Iter.finitelyManySteps")`.
#  Constructor

```
[Std.IterM.TerminationMeasures.Finite.mk](Iterators/Consuming-Iterators/#Std___IterM___TerminationMeasures___Finite___mk "Documentation for Std.IterM.TerminationMeasures.Finite.mk").{w, w'}
```

#  Fields

```
it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β
```

The wrapped iterator.
In the wrapper, its finiteness is used as a termination measure.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.finitelyManySkips "Permalink")def
```


Std.Iter.finitelyManySkips.{w} {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) :
  [IterM.TerminationMeasures.Productive](Iterators/Consuming-Iterators/#Std___IterM___TerminationMeasures___Productive___mk "Documentation for Std.IterM.TerminationMeasures.Productive") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")


Std.Iter.finitelyManySkips.{w}
  {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) :
  [IterM.TerminationMeasures.Productive](Iterators/Consuming-Iterators/#Std___IterM___TerminationMeasures___Productive___mk "Documentation for Std.IterM.TerminationMeasures.Productive") α
    [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")


```

Termination measure to be used in well-founded recursive functions recursing over a productive iterator (see also `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.finitelyManySkips "Permalink")def
```


Std.IterM.finitelyManySkips.{w, w'} {α : Type w} {m : Type w → Type w'}
  {β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive") α m] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) :
  [IterM.TerminationMeasures.Productive](Iterators/Consuming-Iterators/#Std___IterM___TerminationMeasures___Productive___mk "Documentation for Std.IterM.TerminationMeasures.Productive") α m


Std.IterM.finitelyManySkips.{w, w'}
  {α : Type w} {m : Type w → Type w'}
  {β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive") α m] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) :
  [IterM.TerminationMeasures.Productive](Iterators/Consuming-Iterators/#Std___IterM___TerminationMeasures___Productive___mk "Documentation for Std.IterM.TerminationMeasures.Productive") α m


```

Termination measure to be used in well-founded recursive functions recursing over a productive iterator (see also `[Productive](Iterators/Iterator-Definitions/#Std___Iterators___Productive___mk "Documentation for Std.Iterators.Productive")`).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.TerminationMeasures.Productive.it "Permalink")structure
```


Std.IterM.TerminationMeasures.Productive.{w, w'} (α : Type w)
  (m : Type w → Type w') {β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] : Type w


Std.IterM.TerminationMeasures.Productive.{w,
    w'}
  (α : Type w) (m : Type w → Type w')
  {β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] : Type w


```

This type is a wrapper around `[IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM")` so that it becomes a useful termination measure for recursion over productive iterators. See also `[IterM.finitelyManySkips](Iterators/Consuming-Iterators/#Std___IterM___finitelyManySkips "Documentation for Std.IterM.finitelyManySkips")` and `[Iter.finitelyManySkips](Iterators/Consuming-Iterators/#Std___Iter___finitelyManySkips "Documentation for Std.Iter.finitelyManySkips")`.
#  Constructor

```
[Std.IterM.TerminationMeasures.Productive.mk](Iterators/Consuming-Iterators/#Std___IterM___TerminationMeasures___Productive___mk "Documentation for Std.IterM.TerminationMeasures.Productive.mk").{w, w'}
```

#  Fields

```
it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β
```

The wrapped iterator.
In the wrapper, its productivity is used as a termination measure.
##  22.3.2. Consuming Pure Iterators[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Iterators--Consuming-Iterators--Consuming-Pure-Iterators "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.fold "Permalink")def
```


Std.Iter.fold.{w, x} {α β : Type w} {γ : Type x} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (f : γ → β → γ) (init : γ) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : γ


Std.Iter.fold.{w, x} {α β : Type w}
  {γ : Type x} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (f : γ → β → γ)
  (init : γ) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : γ


```

Folds a function over an iterator from the left, accumulating a value starting with `init`. The accumulated value is combined with the each element of the list in order, using `f`.
It is equivalent to `it.[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList").[foldl](Basic-Types/Linked-Lists/#List___foldl "Documentation for List.foldl")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.foldM "Permalink")def
```


Std.Iter.foldM.{x, x', w} {m : Type x → Type x'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α β : Type w} {γ : Type x} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") m]
  (f : γ → β → m γ) (init : γ) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : m γ


Std.Iter.foldM.{x, x', w}
  {m : Type x → Type x'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α β : Type w} {γ : Type x}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") m]
  (f : γ → β → m γ) (init : γ)
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : m γ


```

Folds a monadic function over an iterator from the left, accumulating a value starting with `init`. The accumulated value is combined with the each element of the list in order, using `f`.
It is equivalent to `it.toList.foldlM`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.length "Permalink")def
```


Std.Iter.length.{w} {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Std.Iter.length.{w} {α β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Steps through the whole iterator, counting the number of outputs emitted.
**Performance** :
This function's runtime is linear in the number of steps taken by the iterator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.any "Permalink")def
```


Std.Iter.any.{w} {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  (p : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.Iter.any.{w} {α β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  (p : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the pure predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for any element emitted by the iterator `it`.
`O(|xs|)`. Short-circuits upon encountering the first match. The elements in `it` are examined in order of iteration.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.anyM "Permalink")def
```


Std.Iter.anyM.{w, w'} {α β : Type w} {m : Type → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") m] (p : β → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.Iter.anyM.{w, w'} {α β : Type w}
  {m : Type → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") m]
  (p : β → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the monadic predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for any element emitted by the iterator `it`.
`O(|xs|)`. Short-circuits upon encountering the first match. The elements in `it` are examined in order of iteration.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.all "Permalink")def
```


Std.Iter.all.{w} {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  (p : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.Iter.all.{w} {α β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  (p : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the pure predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for all element emitted by the iterator `it`.
`O(|xs|)`. Short-circuits upon encountering the first match. The elements in `it` are examined in order of iteration.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.allM "Permalink")def
```


Std.Iter.allM.{w, w'} {α β : Type w} {m : Type → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") m] (p : β → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.Iter.allM.{w, w'} {α β : Type w}
  {m : Type → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") m]
  (p : β → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the monadic predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for all element emitted by the iterator `it`.
`O(|xs|)`. Short-circuits upon encountering the first match. The elements in `it` are examined in order of iteration.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.find? "Permalink")def
```


Std.Iter.find?.{w} {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) (f : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


Std.Iter.find?.{w} {α β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) (f : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


```

Returns the first output of the iterator for which the predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such output is found.
`O(|it|)`. Short-circuits upon encountering the first match. The elements in `it` are examined in order of iteration.
If the iterator is not finite, this function might run forever. The variant `it.[ensureTermination](Iterators/Iterator-Definitions/#Std___Iter___ensureTermination "Documentation for Std.Iter.ensureTermination").find?` always terminates after finitely many steps.
Examples:
  * `[7, 6, 5, 8, 1, 2, 6].[iter](Basic-Types/Linked-Lists/#List___iter "Documentation for List.iter").[find?](Iterators/Consuming-Iterators/#Std___Iter___find___ "Documentation for Std.Iter.find?") (· < 5) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 1`
  * `[7, 6, 5, 8, 1, 2, 6].[iter](Basic-Types/Linked-Lists/#List___iter "Documentation for List.iter").[find?](Iterators/Consuming-Iterators/#Std___Iter___find___ "Documentation for Std.Iter.find?") (· < 1) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.findM? "Permalink")def
```


Std.Iter.findM?.{w, w'} {α β : Type w} {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") m] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β)
  (f : β → m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


Std.Iter.findM?.{w, w'} {α β : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") m]
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) (f : β → m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))) :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


```

Returns the first output of the iterator for which the monadic predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such element is found.
`O(|it|)`. Short-circuits when `f` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`. The outputs of `it` are examined in order of iteration.
If the iterator is not finite, this function might run forever. The variant `it.[ensureTermination](Iterators/Iterator-Definitions/#Std___Iter___ensureTermination "Documentation for Std.Iter.ensureTermination").findM?` always terminates after finitely many steps.
Example:

```
#eval [7, 6, 5, 8, 1, 2, 6].iter.findM? fun i => do
  if i < 5 then
    return true
  if i ≤ 6 then
    IO.println s!"Almost! {i}"
  return false

```
`Almost! 6 Almost! 5``[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 1`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.findSome? "Permalink")def
```


Std.Iter.findSome?.{w, x} {α β : Type w} {γ : Type x} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) (f : β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ


Std.Iter.findSome?.{w, x} {α β : Type w}
  {γ : Type x} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β)
  (f : β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ


```

Returns the first non-`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` result of applying `f` to each output of the iterator, in order. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if `f` returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` for all outputs.
`O(|it|)`. Short-circuits when `f` returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") _`.The outputs of `it` are examined in order of iteration.
If the iterator is not finite, this function might run forever. The variant `it.[ensureTermination](Iterators/Iterator-Definitions/#Std___Iter___ensureTermination "Documentation for Std.Iter.ensureTermination").findSome?` always terminates after finitely many steps.
Examples:
  * `[7, 6, 5, 8, 1, 2, 6].[iter](Basic-Types/Linked-Lists/#List___iter "Documentation for List.iter").[findSome?](Iterators/Consuming-Iterators/#Std___Iter___findSome___ "Documentation for Std.Iter.findSome?") (fun x => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x < 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (10 * x) [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 10`
  * `[7, 6, 5, 8, 1, 2, 6].[iter](Basic-Types/Linked-Lists/#List___iter "Documentation for List.iter").[findSome?](Iterators/Consuming-Iterators/#Std___Iter___findSome___ "Documentation for Std.Iter.findSome?") (fun x => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x < 1 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (10 * x) [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.findSomeM? "Permalink")def
```


Std.Iter.findSomeM?.{w, x, w'} {α β : Type w} {γ : Type x}
  {m : Type x → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") m] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) (f : β → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ)) :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ)


Std.Iter.findSomeM?.{w, x, w'}
  {α β : Type w} {γ : Type x}
  {m : Type x → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") m]
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) (f : β → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ)) :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ)


```

Returns the first non-`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` result of applying the monadic function `f` to each output of the iterator, in order. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if `f` returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` for all outputs.
`O(|it|)`. Short-circuits when `f` returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") _`. The outputs of `it` are examined in order of iteration.
If the iterator is not finite, this function might run forever. The variant `it.[ensureTermination](Iterators/Iterator-Definitions/#Std___Iter___ensureTermination "Documentation for Std.Iter.ensureTermination").findSomeM?` always terminates after finitely many steps.
Example:
``some 10``Almost! 6 Almost! 5 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [7, 6, 5, 8, 1, 2, 6].[iter](Basic-Types/Linked-Lists/#List___iter "Documentation for List.iter").[findSomeM?](Iterators/Consuming-Iterators/#Std___Iter___findSomeM___ "Documentation for Std.Iter.findSomeM?") fun i => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") if i < 5 then return [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (i * 10) if i ≤ 6 then [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Almost! {i}" return [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") ``Almost! 6 Almost! 5``[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 10`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.atIdx? "Permalink")def
```


Std.Iter.atIdx?.{u_1} {α β : Type u_1} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β]
  [[IteratorAccess](Iterators/Iterator-Definitions/#Std___IteratorAccess___mk "Documentation for Std.IteratorAccess") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


Std.Iter.atIdx?.{u_1} {α β : Type u_1}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] [[IteratorAccess](Iterators/Iterator-Definitions/#Std___IteratorAccess___mk "Documentation for Std.IteratorAccess") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


```

Returns the `n`-th value emitted by `it`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if `it` terminates earlier.
For monadic iterators, the monadic effects of this operation may differ from manually iterating to the `n`-th value because `atIdx?` can take shortcuts. By the signature, the return value is guaranteed to plausible in the sense of `IterM.IsPlausibleNthOutputStep`.
This function is only available for iterators that explicitly support it by implementing the `[IteratorAccess](Iterators/Iterator-Definitions/#Std___IteratorAccess___mk "Documentation for Std.IteratorAccess")` typeclass.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.atIdxSlow? "Permalink")def
```


Std.Iter.atIdxSlow?.{u_1} {α β : Type u_1} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


Std.Iter.atIdxSlow?.{u_1} {α β : Type u_1}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


```

If possible, takes `n` steps with the iterator `it` and returns the `n`-th emitted value, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if `it` finished before emitting `n` values.
If the iterator is not productive, this function might run forever in an endless loop of iterator steps. The variant `it.[ensureTermination](Iterators/Iterator-Definitions/#Std___Iter___ensureTermination "Documentation for Std.Iter.ensureTermination").atIdxSlow?` is guaranteed to terminate after finitely many steps.
##  22.3.3. Consuming Monadic Iterators[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Iterators--Consuming-Iterators--Consuming-Monadic-Iterators "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.drain "Permalink")def
```


Std.IterM.drain.{w, w'} {α : Type w} {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m] :
  m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


Std.IterM.drain.{w, w'} {α : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m] :
  m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Iterates over the whole iterator, applying the monadic effects of each step, discarding all emitted values.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.fold "Permalink")def
```


Std.IterM.fold.{w, w'} {m : Type w → Type w'} {α β γ : Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m] (f : γ → β → γ) (init : γ)
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : m γ


Std.IterM.fold.{w, w'}
  {m : Type w → Type w'} {α β γ : Type w}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m] (f : γ → β → γ)
  (init : γ) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : m γ


```

Folds a function over an iterator from the left, accumulating a value starting with `init`. The accumulated value is combined with the each element of the list in order, using `f`.
It is equivalent to `it.[toList](Iterators/Consuming-Iterators/#Std___IterM___toList "Documentation for Std.IterM.toList").foldl`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.foldM "Permalink")def
```


Std.IterM.foldM.{w, w', w''} {m : Type w → Type w'}
  {n : Type w → Type w''} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") n] {α β γ : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m n] [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n] (f : γ → β → n γ) (init : γ)
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : n γ


Std.IterM.foldM.{w, w', w''}
  {m : Type w → Type w'}
  {n : Type w → Type w''} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") n]
  {α β γ : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m n] [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m n]
  (f : γ → β → n γ) (init : γ)
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : n γ


```

Folds a monadic function over an iterator from the left, accumulating a value starting with `init`. The accumulated value is combined with the each element of the list in order, using `f`.
The monadic effects of `f` are interleaved with potential effects caused by the iterator's step function. Therefore, it may _not_ be equivalent to `(← it.toList).foldlM`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.length "Permalink")def
```


Std.IterM.length.{w, w'} {α : Type w} {m : Type w → Type w'}
  {β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m] [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))


Std.IterM.length.{w, w'} {α : Type w}
  {m : Type w → Type w'} {β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m]
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) :
  m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))


```

Steps through the whole iterator, counting the number of outputs emitted.
**Performance** :
This function's runtime is linear in the number of steps taken by the iterator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.any "Permalink")def
```


Std.IterM.any.{w, w'} {α β : Type w} {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m] (p : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))


Std.IterM.any.{w, w'} {α β : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m]
  (p : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) :
  m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))


```

Returns `[ULift.up](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the pure predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for any element emitted by the iterator `it`.
`O(|it|)`. Short-circuits upon encountering the first match. The outputs of `it` are examined in order of iteration.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.anyM "Permalink")def
```


Std.IterM.anyM.{w, w'} {α β : Type w} {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m] (p : β → m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))


Std.IterM.anyM.{w, w'} {α β : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m]
  (p : β → m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))


```

Returns `[ULift.up](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the monadic predicate `p` returns `[ULift.up](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for any element emitted by the iterator `it`.
`O(|it|)`. Short-circuits upon encountering the first match. The outputs of `it` are examined in order of iteration.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.all "Permalink")def
```


Std.IterM.all.{w, w'} {α β : Type w} {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m] (p : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))


Std.IterM.all.{w, w'} {α β : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m]
  (p : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) :
  m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))


```

Returns `[ULift.up](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the pure predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for all elements emitted by the iterator `it`.
`O(|it|)`. Short-circuits upon encountering the first mismatch. The outputs of `it` are examined in order of iteration.
If the iterator is not finite, this function might run forever. The variant `it.[ensureTermination](Iterators/Iterator-Definitions/#Std___IterM___ensureTermination "Documentation for Std.IterM.ensureTermination").toListRev` always terminates after finitely many steps.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.allM "Permalink")def
```


Std.IterM.allM.{w, w'} {α β : Type w} {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m] (p : β → m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))


Std.IterM.allM.{w, w'} {α β : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m]
  (p : β → m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")))
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))


```

Returns `[ULift.up](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the monadic predicate `p` returns `[ULift.up](The-Type-System/Universes/#ULift___up "Documentation for ULift.up") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for all elements emitted by the iterator `it`.
`O(|it|)`. Short-circuits upon encountering the first mismatch. The outputs of `it` are examined in order of iteration.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.find? "Permalink")def
```


Std.IterM.find?.{w, w'} {α β : Type w} {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β)
  (f : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


Std.IterM.find?.{w, w'} {α β : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m]
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) (f : β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


```

Returns the first output of the iterator for which the predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such output is found.
`O(|it|)`. Short-circuits upon encountering the first match. The elements in `it` are examined in order of iteration.
If the iterator is not finite, this function might run forever. The variant `it.[ensureTermination](Iterators/Iterator-Definitions/#Std___IterM___ensureTermination "Documentation for Std.IterM.ensureTermination").find?` always terminates after finitely many steps.
Examples:
  * `([7, 6, 5, 8, 1, 2, 6].[iterM](Basic-Types/Linked-Lists/#List___iterM "Documentation for List.iterM") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")).[find?](Iterators/Consuming-Iterators/#Std___IterM___find___ "Documentation for Std.IterM.find?") (· < 5) = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 1)`
  * `([7, 6, 5, 8, 1, 2, 6].[iterM](Basic-Types/Linked-Lists/#List___iterM "Documentation for List.iterM") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")).[find?](Iterators/Consuming-Iterators/#Std___IterM___find___ "Documentation for Std.IterM.find?") (· < 1) = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.findM? "Permalink")def
```


Std.IterM.findM?.{w, w'} {α β : Type w} {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β)
  (f : β → m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


Std.IterM.findM?.{w, w'} {α β : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m]
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β)
  (f : β → m ([ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


```

Returns the first output of the iterator for which the monadic predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such element is found.
`O(|it|)`. Short-circuits when `f` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`. The outputs of `it` are examined in order of iteration.
If the iterator is not finite, this function might run forever. The variant `it.[ensureTermination](Iterators/Iterator-Definitions/#Std___IterM___ensureTermination "Documentation for Std.IterM.ensureTermination").findM?` always terminates after finitely many steps.
Example:

```
#eval ([7, 6, 5, 8, 1, 2, 6].iterM IO).findM? fun i => do
  if i < 5 then
    return true
  if i ≤ 6 then
    IO.println s!"Almost! {i}"
  return false

```
`Almost! 6 Almost! 5``[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 1`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.findSome? "Permalink")def
```


Std.IterM.findSome?.{w, w'} {α β γ : Type w} {m : Type w → Type w'}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β)
  (f : β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ)


Std.IterM.findSome?.{w, w'}
  {α β γ : Type w} {m : Type w → Type w'}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β)
  (f : β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ)


```

Returns the first non-`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` result of applying `f` to each output of the iterator, in order. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if `f` returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` for all outputs.
`O(|it|)`. Short-circuits when `f` returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") _`.The outputs of `it` are examined in order of iteration.
If the iterator is not finite, this function might run forever. The variant `it.[ensureTermination](Iterators/Iterator-Definitions/#Std___IterM___ensureTermination "Documentation for Std.IterM.ensureTermination").findSome?` always terminates after finitely many steps.
Examples:
  * `([7, 6, 5, 8, 1, 2, 6].[iterM](Basic-Types/Linked-Lists/#List___iterM "Documentation for List.iterM") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")).[findSome?](Iterators/Consuming-Iterators/#Std___IterM___findSome___ "Documentation for Std.IterM.findSome?") (fun x => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x < 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (10 * x) [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 10)`
  * `([7, 6, 5, 8, 1, 2, 6].[iterM](Basic-Types/Linked-Lists/#List___iterM "Documentation for List.iterM") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")).[findSome?](Iterators/Consuming-Iterators/#Std___IterM___findSome___ "Documentation for Std.IterM.findSome?") (fun x => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x < 1 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (10 * x) [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.findSomeM? "Permalink")def
```


Std.IterM.findSomeM?.{w, w'} {α β γ : Type w} {m : Type w → Type w'}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β)
  (f : β → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ)) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ)


Std.IterM.findSomeM?.{w, w'}
  {α β γ : Type w} {m : Type w → Type w'}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  [[IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") α m m] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β)
  (f : β → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ)) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ)


```

Returns the first non-`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` result of applying the monadic function `f` to each output of the iterator, in order. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if `f` returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` for all outputs.
`O(|it|)`. Short-circuits when `f` returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") _`. The outputs of `it` are examined in order of iteration.
If the iterator is not finite, this function might run forever. The variant `it.[ensureTermination](Iterators/Iterator-Definitions/#Std___IterM___ensureTermination "Documentation for Std.IterM.ensureTermination").findSomeM?` always terminates after finitely many steps.
Example:
``some 10``Almost! 6 Almost! 5 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ([7, 6, 5, 8, 1, 2, 6].[iterM](Basic-Types/Linked-Lists/#List___iterM "Documentation for List.iterM") [IO](IO/Logical-Model/#IO "Documentation for IO")).[findSomeM?](Iterators/Consuming-Iterators/#Std___IterM___findSomeM___ "Documentation for Std.IterM.findSomeM?") fun i => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") if i < 5 then return [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (i * 10) if i ≤ 6 then [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Almost! {i}" return [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") ``Almost! 6 Almost! 5``[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 10`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.atIdx? "Permalink")def
```


Std.IterM.atIdx?.{u_1, u_2} {α : Type u_1} {m : Type u_1 → Type u_2}
  {β : Type u_1} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorAccess](Iterators/Iterator-Definitions/#Std___IteratorAccess___mk "Documentation for Std.IteratorAccess") α m] [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


Std.IterM.atIdx?.{u_1, u_2} {α : Type u_1}
  {m : Type u_1 → Type u_2} {β : Type u_1}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] [[IteratorAccess](Iterators/Iterator-Definitions/#Std___IteratorAccess___mk "Documentation for Std.IteratorAccess") α m]
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


```

Returns the `n`-th value emitted by `it`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if `it` terminates earlier.
For monadic iterators, the monadic effects of this operation may differ from manually iterating to the `n`-th value because `atIdx?` can take shortcuts. By the signature, the return value is guaranteed to plausible in the sense of `IterM.IsPlausibleNthOutputStep`.
This function is only available for iterators that explicitly support it by implementing the `[IteratorAccess](Iterators/Iterator-Definitions/#Std___IteratorAccess___mk "Documentation for Std.IteratorAccess")` typeclass.
##  22.3.4. Collectors[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Iterators--Consuming-Iterators--Collectors "Permalink")
Collectors consume an iterator, returning all of its data in a list or array. To be collected, an iterator must be finite.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.toArray "Permalink")def
```


Std.Iter.toArray.{w} {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


Std.Iter.toArray.{w} {α β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


```

Traverses the given iterator and stores the emitted values in an array.
If the iterator is not finite, this function might run forever. The variant `it.[ensureTermination](Iterators/Iterator-Definitions/#Std___Iter___ensureTermination "Documentation for Std.Iter.ensureTermination").toArray` always terminates after finitely many steps.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.toArray "Permalink")def
```


Std.IterM.toArray.{w, w'} {α β : Type w} {m : Type w → Type w'}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β)


Std.IterM.toArray.{w, w'} {α β : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) :
  m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β)


```

Traverses the given iterator and stores the emitted values in an array.
If the iterator is not finite, this function might run forever. The variant `it.[ensureTermination](Iterators/Iterator-Definitions/#Std___IterM___ensureTermination "Documentation for Std.IterM.ensureTermination").toArray` always terminates after finitely many steps.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.toList "Permalink")def
```


Std.Iter.toList.{w} {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


Std.Iter.toList.{w} {α β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


```

Traverses the given iterator and stores the emitted values in a list. Because lists are prepend-only, `toListRev` is usually more efficient that `toList`.
If the iterator is not finite, this function might run forever. The variant `it.[ensureTermination](Iterators/Iterator-Definitions/#Std___Iter___ensureTermination "Documentation for Std.Iter.ensureTermination").toList` always terminates after finitely many steps.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.toList "Permalink")def
```


Std.IterM.toList.{w, w'} {α : Type w} {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


Std.IterM.toList.{w, w'} {α : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


```

Traverses the given iterator and stores the emitted values in a list. Because lists are prepend-only, `toListRev` is usually more efficient that `toList`.
If the iterator is not finite, this function might run forever. The variant `it.[ensureTermination](Iterators/Iterator-Definitions/#Std___IterM___ensureTermination "Documentation for Std.IterM.ensureTermination").toList` always terminates after finitely many steps.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Iter.toListRev "Permalink")def
```


Std.Iter.toListRev.{w} {α β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


Std.Iter.toListRev.{w} {α β : Type w}
  [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") β] (it : [Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


```

Traverses the given iterator and stores the emitted values in reverse order in a list. Because lists are prepend-only, this `toListRev` is usually more efficient that `toList`.
If the iterator is not finite, this function might run forever. The variant `it.[ensureTermination](Iterators/Iterator-Definitions/#Std___Iter___ensureTermination "Documentation for Std.Iter.ensureTermination").toListRev` always terminates after finitely many steps.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.IterM.toListRev "Permalink")def
```


Std.IterM.toListRev.{w, w'} {α : Type w} {m : Type w → Type w'}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β] (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


Std.IterM.toListRev.{w, w'} {α : Type w}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {β : Type w} [[Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") α m β]
  (it : [IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m β) : m ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β)


```

Traverses the given iterator and stores the emitted values in reverse order in a list. Because lists are prepend-only, this `toListRev` is usually more efficient that `toList`.
If the iterator is not finite, this function might run forever. The variant `it.[ensureTermination](Iterators/Iterator-Definitions/#Std___IterM___ensureTermination "Documentation for Std.IterM.ensureTermination").toListRev` always terminates after finitely many steps.
[←22.2. Iterator Definitions](Iterators/Iterator-Definitions/#The-Lean-Language-Reference--Iterators--Iterator-Definitions "22.2. Iterator Definitions")[22.4. Iterator Combinators→](Iterators/Iterator-Combinators/#The-Lean-Language-Reference--Iterators--Iterator-Combinators "22.4. Iterator Combinators")

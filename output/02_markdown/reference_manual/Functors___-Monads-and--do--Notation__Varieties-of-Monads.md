[←18.4. API Reference](Functors___-Monads-and--do--Notation/API-Reference/#The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--API-Reference "18.4. API Reference")[19. Basic Propositions→](Basic-Propositions/#basic-props "19. Basic Propositions")
#  18.5. Varieties of Monads[🔗](find/?domain=Verso.Genre.Manual.section&name=monad-varieties "Permalink")
The `[IO](IO/Logical-Model/#IO "Documentation for IO")` monad has many, many effects, and is used for writing programs that need to interact with the world. It is described in [its own section](IO/#io). Programs that use `[IO](IO/Logical-Model/#IO "Documentation for IO")` are essentially black boxes: they are typically not particularly amenable to verification.
Many algorithms are easiest to express with a much smaller set of effects. These effects can often be simulated; for example, mutable state can be simulated by passing around a tuple that contains both the program's value and the state. These simulated effects are easier to reason formally about, because they are defined using ordinary code rather than new language primitives.
The standard library provides abstractions for working with commonly-used effects. Many frequently-used effects fall into a small number of categories: 

State monads have mutable state
    
Computations that have access to some data that may be modified by other parts of the computation use _mutable state_. State can be implemented in a variety of ways, described in the section on [state monads](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#state-monads) and captured in the `[MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState")` type class. 

Reader monads are parameterized computations
    
Computations that can read the value of some parameter provided by a context exist in most programming languages, but many languages that feature state and exceptions as first-class features do not have built-in facilities for defining new parameterized computations. Typically, these computations are provided with a parameter value when invoked, and sometimes they can locally override it. Parameter values have _dynamic extent_ : the value provided most recently in the call stack is the one that is used. They can be simulated by passing a value unchanged through a sequence of function calls; however, this technique can make code harder to read and introduces a risk that the values may be passed incorrectly to further calls by mistake. They can also be simulated using mutable state with a careful discipline surrounding the modification of the state. Monads that maintain a parameter, potentially allowing it to be overridden in a section of the call stack, are called _reader monads_. Reader monads are captured in the `[MonadReader](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadReader___mk "Documentation for MonadReader")` type class. Additionally, reader monads that allow the parameter value to be locally overridden are captured in the `[MonadWithReader](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadWithReader___mk "Documentation for MonadWithReader")` type class. 

Exception monads have exceptions
    
Computations that may terminate early with an exceptional value use _exceptions_. They are typically modeled with a sum type that has a constructor for ordinary termination and a constructor for early termination with errors. Exception monads are described in the section on [exception monads](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#exception-monads), and captured in the `[MonadExcept](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept")` type class.
##  18.5.1. Monad Type Classes[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Varieties-of-Monads--Monad-Type-Classes "Permalink")
Using type classes like `[MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState")` and `[MonadExcept](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept")` allow client code to be polymorphic with respect to monads. Together with automatic lifting, this allows programs to be reusable in many different monads and makes them more robust to refactoring.
It's important to be aware that effects in a monad may not interact in only one way. For example, a monad with state and exceptions may or may not roll back state changes when an exception is thrown. If this matters for the correctness of a function, then it should use a more specific signature.
Effect Ordering
The function `[sumNonFives](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#sumNonFives-_LPAR_in-Effect-Ordering_RPAR_ "Definition of example")` adds the contents of a list using a state monad, terminating early if it encounters a `5`.
`def sumNonFives {m}     [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") m] [[MonadExcept](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") m]     (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :     m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   for x in xs do     if x == 5 then       [throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") "Five was encountered"     else       [modify](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#modify "Documentation for modify") (· + x) `
Running it in one monad returns the state at the time that `5` was encountered:
``(Except.error "Five was encountered", 10)`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [sumNonFives](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#sumNonFives-_LPAR_in-Effect-Ordering_RPAR_ "Definition of example") (m := [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") ([StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))) [1, 2, 3, 4, 5, 6] |>.[run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT___run "Documentation for ExceptT.run") |>.[run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT___run "Documentation for StateT.run") 0 `
```
(Except.error "Five was encountered", 10)
```

In another, the state is discarded:
``Except.error "Five was encountered"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [sumNonFives](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#sumNonFives-_LPAR_in-Effect-Ordering_RPAR_ "Definition of example") (m := [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))) [1, 2, 3, 4, 5, 6] |>.[run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT___run "Documentation for StateT.run") 0 `
```
Except.error "Five was encountered"
```

In the second case, an exception handler would roll back the state to its value at the start of the ``Lean.Parser.Term.termTry : term```try`. The following function is thus incorrect:
`/-- Computes the sum of the non-5 prefix of a list. -/ def sumUntilFive {m}     [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") m] [[MonadExcept](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") m]     (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :     m [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   [MonadState.set](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState.set") 0   try     [sumNonFives](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#sumNonFives-_LPAR_in-Effect-Ordering_RPAR_ "Definition of example") xs   catch _ =>     [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ()   get `
In one monad, the answer is correct:
``Except.ok 10`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [sumUntilFive](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#sumUntilFive-_LPAR_in-Effect-Ordering_RPAR_ "Definition of example") (m := [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") ([StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))) [1, 2, 3, 4, 5, 6] |>.[run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT___run "Documentation for ExceptT.run") |>.[run'](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT___run___ "Documentation for StateT.run'") 0 `
```
Except.ok 10
```

In the other, it is not:
``Except.ok 0`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [sumUntilFive](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#sumUntilFive-_LPAR_in-Effect-Ordering_RPAR_ "Definition of example") (m := [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))) [1, 2, 3, 4, 5, 6] |>.[run'](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT___run___ "Documentation for StateT.run'") 0 `
```
Except.ok 0
```

[Live ↪](javascript:openLiveLink\("CYUwZgBAzgrgtgOQPYDsBiBLAbiKEDecAvgFATkQDaAsqgIbARwC6VtKDAygC53cgQEfJqxr1gAUQAeAYxAAHbhB4AnDCgDmIshQAUUvAC4IAGQxQlQ7gEoIhneTgQAqigxLDAXgjAkOsEgqEFIQ6sF4vg6hkCGe3gCsENwAFiAoUeQpKkgA7hAARJg4EDl0eGkySDAo/CogwPlRIAA2UCAZTEjAGGAAnhC6AO0QANTB1iQkAMQgWHTNOrCIqEW4A05eENJyigAqytxqmgM8fCDUgnzWExRUAIwANBAATE8AzE8ALE/xTwBsrAAPgA+AB0KmqEBB4MhAAZJjM5gtyEtkOhsGtdBtvKd+PsrANtgolKp1BprlFKI8Xu8vj9/kCwRCUBB4SQAPQAWk5EAAwkg4PIYPw8CkBEsIEhIGKIChUJzEvI6mAMCEpRA6BBmuZuKCIJz2SRQJAlq5uBhmqsCMRKewGCI2OJcQICSxHRxJLJiQcjloWFF9EZTDrLjY7FEnATNpFyHbgM7QW0lPDMipelFUSsMXgDDoZHwZMkIAB9CCeYFRIV1AY3CAaEDcBGzeaLeBmi1WrF2bxEvY+sknXj8C5WCm3KlPV4QD4Qb4QX4QAFQpmQ6HMgDkrKbSNbcHblox627BzO+OEul7JMOZLHFAnNOndPnDOXMJQm9hQA"\))
A single monad may support multiple version of the same effect. For example, there might be a mutable `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` and a mutable `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` or two separate reader parameters. As long as they have different types, it should be convenient to access both. In typical use, some monadic operations that are overloaded in type classes have type information available for [instance synthesis](Type-Classes/#--tech-term-synthesizes), while others do not. For example, the argument passed to `[set](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState.set")` determines the type of the state to be used, while `get` takes no such argument. The type information present in applications of `[set](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState.set")` can be used to pick the correct instance when multiple states are available, which suggests that the type of the mutable state should be an input parameter or [semi-output parameter](Type-Classes/Instance-Synthesis/#--tech-term-Semi-output-parameters) so that it can be used to select instances. The lack of type information present in uses of `get`, on the other hand, suggests that the type of the mutable state should be an [output parameter](Type-Classes/Instance-Synthesis/#--tech-term-output-parameter) in `[MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState")`, so type class synthesis determines the state's type from the monad itself.
This dichotomy is solved by having two versions of many of the effect type classes. The version with a semi-output parameter has the suffix `-Of`, and its operations take types explicitly as needed. Examples include `[MonadStateOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf")`, `[MonadReaderOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadReaderOf___mk "Documentation for MonadReaderOf")`, and `[MonadExceptOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExceptOf___mk "Documentation for MonadExceptOf")`. The operations with explicit type parameters have names ending in `-The`, such as `[getThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#getThe "Documentation for getThe")`, `[readThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#readThe "Documentation for readThe")`, and `[tryCatchThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#tryCatchThe "Documentation for tryCatchThe")`. The name of the version with an output parameter is undecorated. The standard library exports a mix of operations from the `-Of` and undecorated versions of each type class, based on what has good inference behavior in typical use cases.  
|  Operation  |  From Class  |  Notes   |  
| --- | --- | --- |  
|  `get`  |  `[MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState")`  |  Output parameter improves type inference   |  
|  `[set](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf.set")`  |  `[MonadStateOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf")`  |  Semi-output parameter uses type information from `[set](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf.set")`'s argument   |  
|  `[modify](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#modify "Documentation for modify")`  |  `[MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState")`  |  Output parameter is needed to allow functions without annotations   |  
|  `modifyGet`  |  `[MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState")`  |  Output parameter is needed to allow functions without annotations   |  
|  `[read](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadReader___mk "Documentation for MonadReader.read")`  |  `[MonadReader](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadReader___mk "Documentation for MonadReader")`  |  Output parameter is needed due to lack of type information from arguments   |  
|  `[readThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#readThe "Documentation for readThe")`  |  `[MonadReaderOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadReaderOf___mk "Documentation for MonadReaderOf")`  |  Semi-output parameter uses the provided type to guide synthesis   |  
|  `[withReader](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadWithReader___mk "Documentation for MonadWithReader.withReader")`  |  `[MonadWithReader](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadWithReader___mk "Documentation for MonadWithReader")`  |  Output parameter avoids the need for type annotations on the function   |  
|  `[withTheReader](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#withTheReader "Documentation for withTheReader")`  |  `[MonadWithReaderOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadWithReaderOf___mk "Documentation for MonadWithReaderOf")`  |  Semi-output parameter uses provided type to guide synthesis   |  
|  `[throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw")`  |  `[MonadExcept](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept")`  |  Output parameter enables the use of constructor dot notation for the exception   |  
|  `[throwThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#throwThe "Documentation for throwThe")`  |  `[MonadExceptOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExceptOf___mk "Documentation for MonadExceptOf")`  |  Semi-output parameter uses provided type to guide synthesis   |  
|  `[tryCatch](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.tryCatch")`  |  `[MonadExcept](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept")`  |  Output parameter enables the use of constructor dot notation for the exception   |  
|  `[tryCatchThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#tryCatchThe "Documentation for tryCatchThe")`  |  `[MonadExceptOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExceptOf___mk "Documentation for MonadExceptOf")`  |  Semi-output parameter uses provided type to guide synthesis  |  
State Types
The state monad `[M](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#M-_LPAR_in-State-Types_RPAR_ "Definition of example")` has two separate states: a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` and a `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`.
`abbrev M := [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ([StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) `
Because `get` is an alias for `MonadState.get`, the state type is an output parameter. This means that Lean selects a state type automatically, in this case the one from the outermost monad transformer:
``get : [M](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#M-_LPAR_in-State-Types_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") (get : [M](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#M-_LPAR_in-State-Types_RPAR_ "Definition of example") _) `
```
get : [M](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#M-_LPAR_in-State-Types_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

Only the outermost may be used, because the type of the state is an output parameter.
`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") (`failed to synthesize instance of type class   [MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [M](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#M-_LPAR_in-State-Types_RPAR_ "Definition of example")  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`get : [M](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#M-_LPAR_in-State-Types_RPAR_ "Definition of example") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) `
```
failed to synthesize instance of type class
  [MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [M](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#M-_LPAR_in-State-Types_RPAR_ "Definition of example")

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```

Providing the state type explicitly using `[getThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#getThe "Documentation for getThe")` from `[MonadStateOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf")` allows both states to be read.
``[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[getThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#getThe "Documentation for getThe") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [getThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#getThe "Documentation for getThe") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") : [M](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#M-_LPAR_in-State-Types_RPAR_ "Definition of example") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [M](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#M-_LPAR_in-State-Types_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") (([getThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#getThe "Documentation for getThe") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"), [getThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#getThe "Documentation for getThe") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [M](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#M-_LPAR_in-State-Types_RPAR_ "Definition of example") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") × [M](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#M-_LPAR_in-State-Types_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) `
```
[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[getThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#getThe "Documentation for getThe") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [getThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#getThe "Documentation for getThe") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") : [M](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#M-_LPAR_in-State-Types_RPAR_ "Definition of example") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [M](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#M-_LPAR_in-State-Types_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

Setting a state works for either type, because the state type is a [semi-output parameter](Type-Classes/Instance-Synthesis/#--tech-term-Semi-output-parameters) on `[MonadStateOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf")`.
``[set](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf.set") 4 : [M](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#M-_LPAR_in-State-Types_RPAR_ "Definition of example") [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") ([set](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf.set") 4 : [M](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#M-_LPAR_in-State-Types_RPAR_ "Definition of example") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")) `
```
[set](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf.set") 4 : [M](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#M-_LPAR_in-State-Types_RPAR_ "Definition of example") [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")
```
``[set](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf.set") "Four" : [M](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#M-_LPAR_in-State-Types_RPAR_ "Definition of example") [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") ([set](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf.set") "Four" : [M](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#M-_LPAR_in-State-Types_RPAR_ "Definition of example") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")) `
```
[set](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf.set") "Four" : [M](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#M-_LPAR_in-State-Types_RPAR_ "Definition of example") [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")
```

[Live ↪](javascript:openLiveLink\("IYIxCcFMDcAIFlYC4C8sDKAXYnIBVYA5HWACix0kS3AEsA7AcwEoAoVgYgGMALSLgNZlGkTMgSwA+m069+Q0qRGY8fDJjpMANLGWrIRHM3HUNDRrADrE4phnc+gsgGdRsACwnYAVXq077A7yLm4ARABiAPYAruChXr7+zEA"\))
##  18.5.2. Monad Transformers[🔗](find/?domain=Verso.Genre.Manual.section&name=monad-transformers "Permalink")
A _monad transformer_ is a function that, when provided with a monad, gives back a new monad. Typically, this new monad has all the effects of the original monad along with some additional ones.
A monad transformer consists of the following:
  * A function `T` that constructs the new monad's type from an existing monad
  * A `run` function that adapts a `T m α` into some variant of `m`, often requiring additional parameters and returning a more specific type under `m`
  * An instance of `[[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] → [Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") (T m)` that allows the transformed monad to be used as a monad
  * An instance of `[MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift")` that allows the original monad's code to be used in the transformed monad
  * If possible, an instance of `[MonadControl](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControl___mk "Documentation for MonadControl") m (T m)` that allows actions from the transformed monad to be used in the original monad


Typically, a monad transformer also provides instances of one or more type classes that describe the effects that it introduces. The transformer's `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")` and `[MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift")` instances make it practical to write code in the transformed monad, while the type class instances allow the transformed monad to be used with polymorphic functions.
The Identity Monad Transformer 
The identity monad transformer neither adds nor removes capabilities to the transformed monad. Its definition is the identity function, suitably specialized:
`def IdT (m : Type u → Type v) : Type u → Type v := m `
Similarly, the `[run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#IdT___run-_LPAR_in-The-Identity-Monad-Transformer-_RPAR_ "Definition of example")` function requires no additional arguments and just returns an `m α`:
`def IdT.run (act : [IdT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#IdT-_LPAR_in-The-Identity-Monad-Transformer-_RPAR_ "Definition of example") m α) : m α := act `
The monad instance relies on the monad instance for the transformed monad, selecting it via [type ascriptions](Terms/Type-Ascription/#--tech-term-Type-ascriptions):
`instance [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] : [Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") ([IdT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#IdT-_LPAR_in-The-Identity-Monad-Transformer-_RPAR_ "Definition of example") m) where   [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x := ([pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x : m _)   [bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") x f := (x >>= f : m _) `
Because `[IdT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#IdT-_LPAR_in-The-Identity-Monad-Transformer-_RPAR_ "Definition of example") m` is definitionally equal to `m`, the `[MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift") m ([IdT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#IdT-_LPAR_in-The-Identity-Monad-Transformer-_RPAR_ "Definition of example") m)` instance doesn't need to modify the action being lifted:
`instance : [MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift") m ([IdT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#IdT-_LPAR_in-The-Identity-Monad-Transformer-_RPAR_ "Definition of example") m) where   [monadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift.monadLift") x := x `
The `[MonadControl](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControl___mk "Documentation for MonadControl")` instance is similarly simple.
`instance [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] : [MonadControl](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControl___mk "Documentation for MonadControl") m ([IdT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#IdT-_LPAR_in-The-Identity-Monad-Transformer-_RPAR_ "Definition of example") m) where   [stM](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControl___mk "Documentation for MonadControl.stM") α := α   [liftWith](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControl___mk "Documentation for MonadControl.liftWith") f := f (fun x => [Id.run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id___run "Documentation for Id.run") <| [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x)   [restoreM](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadControl___mk "Documentation for MonadControl.restoreM") v := v `
[Live ↪](javascript:openLiveLink\("CYUwZgBAksAqEAoC2EBcFYE8AOIIFcJAkwgxzwDcBKNU3A42itAXgiQCh3RIZYA6AE74AdogCGAYwAuNXmwiBG4GroUClhElTOAS2EBnKWOES8AbQCyAe2FjgbALo0rNuwjlJqAdwAWIASHYICGx8fwgAD3UEELDIlQgAfUpAiAAjXTtIyFRWBEiAPnzWbPkknX1DYzx0Z1sAGW0wGRQ3ODYvX38UpGt6xpk41nDygyMTCAteuyRHGqmAYWspAUsAG3lW+A8IHz8AoINzRXUFFNX+gHVtKW8IbOLEMBEIiGZ86GBBZ4AeAB9g0J4cLJIL+AyWfxHcjqchAA"\))
The Lean standard library provides transformer versions of many different monads, including `[ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT")`, `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT")`, and `[StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT")`, along with variants using other representations such as `[StateCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateCpsT "Documentation for StateCpsT")`, `[StateRefT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateRefT___ "Documentation for StateRefT'")`, and `[ExceptCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptCpsT "Documentation for ExceptCpsT")`. Additionally, the `[EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM")` monad is equivalent to combining `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT")` and `[StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT")`, but it can use a more specialized representation to improve performance.
##  18.5.3. Identity[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Varieties-of-Monads--Identity "Permalink")
The identity monad `[Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")` has no effects whatsoever. Both `[Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")` and the corresponding implementation of `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` are the identity function, and `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")` is reversed function application. The identity monad has two primary use cases:
  1. It can be the type of a ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block that implements a pure function with local effects.
  2. It can be placed at the bottom of a stack of monad transformers.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Id "Permalink")def
```


Id.{u} (type : Type u) : Type u


Id.{u} (type : Type u) : Type u


```

The identity function on types, used primarily for its `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")` instance.
The identity monad is useful together with monad transformers to construct monads for particular purposes. Additionally, it can be used with `do`-notation in order to use control structures such as local mutability, `for`-loops, and early returns in code that does not otherwise use monads.
Examples:
`def containsFive (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [Id.run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id___run "Documentation for Id.run") [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   for x in xs do     if x == 5 then return [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")   return [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") `
```
#eval containsFive [1, 3, 5, 7]

```
`[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Id.run "Permalink")def
```


Id.run.{u_1} {α : Type u_1} (x : [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") α) : α


Id.run.{u_1} {α : Type u_1} (x : [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") α) : α


```

Runs a computation in the identity monad.
This function is the identity function. Because its parameter has type `[Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") α`, it causes `do`-notation in its arguments to use the `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")` instance.
Local Effects with the Identity Monad
This code block implements a countdown procedure by using simulated local mutability in the identity monad.
``[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")9[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 8[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 7[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 6[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 5[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 4[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 0[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Id.run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id___run "Documentation for Id.run") [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let mut xs := [] for x in [0:10] do xs := x :: xs [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") xs `
```
[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")9[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 8[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 7[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 6[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 5[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 4[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 0[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

[Live ↪](javascript:openLiveLink\("MQUwbghgNgBAkgEwHQCcCuA7GCD2AoGGKEAFxgFs0yAPAZxgC4BeGAbQF0CYAzHFGajACWWVgAYGARjHts+QoTqMWghgwG0uABzQoQGoA"\))
##  18.5.4. State[🔗](find/?domain=Verso.Genre.Manual.section&name=state-monads "Permalink")
[State monads](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#--tech-term-State-monads) provide access to a mutable value. The underlying implementation may use a tuple to simulate mutability, or it may use something like `[ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref")` to ensure mutation. Even those implementations that use a tuple may in fact use mutation at run-time due to Lean's use of mutation when there are unique references to values, but this requires a programming style that prefers `[modify](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#modify "Documentation for modify")` and `modifyGet` over `get` and `[set](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf.set")`.
###  18.5.4.1. General State API[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Varieties-of-Monads--State--General-State-API "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadState.get "Permalink")type class
```


MonadState.{u, v} (σ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type u)) (m : Type u → Type v) :
  Type (max (u + 1) v)


MonadState.{u, v} (σ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type u))
  (m : Type u → Type v) :
  Type (max (u + 1) v)


```

State monads provide a value of a given type (the _state_) that can be retrieved or replaced. Instances may implement these operations by passing state values around, by using a mutable reference cell (e.g. `[ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ`), or in other ways.
In this class, `σ` is an `[outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam")`, which means that it is inferred from `m`. `[MonadStateOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf") σ` provides the same operations, but allows `σ` to influence instance synthesis.
The mutable state of a state monad is visible between multiple `do`-blocks or functions, unlike [local mutable state](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=do-notation-let-mut) in `do`-notation.
#  Instance Constructor

```
[MonadState.mk](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState.mk").{u, v}
```

#  Methods

```
get : m σ
```

Retrieves the current value of the monad's mutable state.

```
set : σ → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")
```

Replaces the current value of the mutable state with a new one.

```
modifyGet : {α : Type u} → (σ → α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ) → m α
```

Applies a function to the current state that both computes a new state and a value. The new state replaces the current state, and the value is returned.
It is equivalent to `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let (a, s) := f (← get); set s; pure a`. However, using `modifyGet` may lead to higher performance because it doesn't add a new reference to the state value. Additional references can inhibit in-place updates of data.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadState.get "Permalink")def
```


MonadState.get.{u, v} {σ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type u)} {m : Type u → Type v}
  [self : [MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState") σ m] : m σ


MonadState.get.{u, v}
  {σ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type u)}
  {m : Type u → Type v}
  [self : [MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState") σ m] : m σ


```

Retrieves the current value of the monad's mutable state.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=modify "Permalink")def
```


modify.{u, v} {σ : Type u} {m : Type u → Type v} [[MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState") σ m]
  (f : σ → σ) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


modify.{u, v} {σ : Type u}
  {m : Type u → Type v} [[MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState") σ m]
  (f : σ → σ) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Mutates the current state, replacing its value with the result of applying `f` to it.
Use `[modifyThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#modifyThe "Documentation for modifyThe")` to explicitly select a state type to modify.
It is equivalent to `do set (f (← get))`. However, using `[modify](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#modify "Documentation for modify")` may lead to higher performance because it doesn't add a new reference to the state value. Additional references can inhibit in-place updates of data.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadState.modifyGet "Permalink")def
```


MonadState.modifyGet.{u, v} {σ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type u)}
  {m : Type u → Type v} [self : [MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState") σ m] {α : Type u} :
  (σ → α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ) → m α


MonadState.modifyGet.{u, v}
  {σ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type u)}
  {m : Type u → Type v}
  [self : [MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState") σ m] {α : Type u} :
  (σ → α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ) → m α


```

Applies a function to the current state that both computes a new state and a value. The new state replaces the current state, and the value is returned.
It is equivalent to `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let (a, s) := f (← get); set s; pure a`. However, using `modifyGet` may lead to higher performance because it doesn't add a new reference to the state value. Additional references can inhibit in-place updates of data.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=getModify "Permalink")def
```


getModify.{u, v} {σ : Type u} {m : Type u → Type v} [[MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState") σ m]
  (f : σ → σ) : m σ


getModify.{u, v} {σ : Type u}
  {m : Type u → Type v} [[MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState") σ m]
  (f : σ → σ) : m σ


```

Replaces the state with the result of applying `f` to it. Returns the old value of the state.
It is equivalent to `get <* modify f` but may be more efficient.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadStateOf.mk "Permalink")type class
```


MonadStateOf.{u, v} (σ : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Type u)) (m : Type u → Type v) :
  Type (max (u + 1) v)


MonadStateOf.{u, v}
  (σ : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Type u))
  (m : Type u → Type v) :
  Type (max (u + 1) v)


```

State monads provide a value of a given type (the _state_) that can be retrieved or replaced. Instances may implement these operations by passing state values around, by using a mutable reference cell (e.g. `[ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ`), or in other ways.
In this class, `σ` is a `[semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam")`, which means that it can influence the choice of instance. `[MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState") σ` provides the same operations, but requires that `σ` be inferable from `m`.
The mutable state of a state monad is visible between multiple `do`-blocks or functions, unlike [local mutable state](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=do-notation-let-mut) in `do`-notation.
#  Instance Constructor

```
[MonadStateOf.mk](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf.mk").{u, v}
```

#  Methods

```
get : m σ
```

Retrieves the current value of the monad's mutable state.

```
set : σ → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")
```

Replaces the current value of the mutable state with a new one.

```
modifyGet : {α : Type u} → (σ → α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ) → m α
```

Applies a function to the current state that both computes a new state and a value. The new state replaces the current state, and the value is returned.
It is equivalent to `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let (a, s) := f (← get); set s; pure a`. However, using `modifyGet` may lead to higher performance because it doesn't add a new reference to the state value. Additional references can inhibit in-place updates of data.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=getThe "Permalink")def
```


getThe.{u, v} (σ : Type u) {m : Type u → Type v} [[MonadStateOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf") σ m] :
  m σ


getThe.{u, v} (σ : Type u)
  {m : Type u → Type v}
  [[MonadStateOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf") σ m] : m σ


```

Gets the current state that has the explicitly-provided type `σ`. When the current monad has multiple state types available, this function selects one of them.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=modifyThe "Permalink")def
```


modifyThe.{u, v} (σ : Type u) {m : Type u → Type v} [[MonadStateOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf") σ m]
  (f : σ → σ) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


modifyThe.{u, v} (σ : Type u)
  {m : Type u → Type v} [[MonadStateOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf") σ m]
  (f : σ → σ) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Mutates the current state that has the explicitly-provided type `σ`, replacing its value with the result of applying `f` to it. When the current monad has multiple state types available, this function selects one of them.
It is equivalent to `do set (f (← get))`. However, using `[modify](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#modify "Documentation for modify")` may lead to higher performance because it doesn't add a new reference to the state value. Additional references can inhibit in-place updates of data.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=modifyGetThe "Permalink")def
```


modifyGetThe.{u, v} {α : Type u} (σ : Type u) {m : Type u → Type v}
  [[MonadStateOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf") σ m] (f : σ → α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ) : m α


modifyGetThe.{u, v} {α : Type u}
  (σ : Type u) {m : Type u → Type v}
  [[MonadStateOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf") σ m] (f : σ → α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ) : m α


```

Applies a function to the current state that has the explicitly-provided type `σ`. The function both computes a new state and a value. The new state replaces the current state, and the value is returned.
It is equivalent to `do let (a, s) := f (← getThe σ); set s; pure a`. However, using `[modifyGetThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#modifyGetThe "Documentation for modifyGetThe")` may lead to higher performance because it doesn't add a new reference to the state value. Additional references can inhibit in-place updates of data.
###  18.5.4.2. Tuple-Based State Monads[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Varieties-of-Monads--State--Tuple-Based-State-Monads "Permalink")
The tuple-based state monads represent a computation with states that have type `σ` yielding values of type `α` as functions that take a starting state and yield a value paired with a final state, e.g. `σ → α × σ`. The `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")` operations thread the state correctly through the computation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateM "Permalink")def
```


StateM.{u} (σ α : Type u) : Type u


StateM.{u} (σ α : Type u) : Type u


```

A tuple-based state monad.
Actions in `[StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") σ` are functions that take an initial state and return a value paired with a final state.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateT "Permalink")def
```


StateT.{u, v} (σ : Type u) (m : Type u → Type v) (α : Type u) :
  Type (max u v)


StateT.{u, v} (σ : Type u)
  (m : Type u → Type v) (α : Type u) :
  Type (max u v)


```

Adds a mutable state of type `σ` to a monad.
Actions in the resulting monad are functions that take an initial state and return, in `m`, a tuple of a value and a state.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateT.run "Permalink")def
```


StateT.run.{u, v} {σ : Type u} {m : Type u → Type v} {α : Type u}
  (x : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α) (s : σ) : m [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


StateT.run.{u, v} {σ : Type u}
  {m : Type u → Type v} {α : Type u}
  (x : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α) (s : σ) : m [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Executes an action from a monad with added state in the underlying monad `m`. Given an initial state, it returns a value paired with the final state.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateT.get "Permalink")def
```


StateT.get.{u, v} {σ : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] :
  [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m σ


StateT.get.{u, v} {σ : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] :
  [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m σ


```

Retrieves the current value of the monad's mutable state.
This increments the reference count of the state, which may inhibit in-place updates.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateT.set "Permalink")def
```


StateT.set.{u, v} {σ : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] :
  σ → [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


StateT.set.{u, v} {σ : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] :
  σ → [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Replaces the mutable state with a new value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateT.orElse "Permalink")def
```


StateT.orElse.{u, v} {σ : Type u} {m : Type u → Type v} [[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative") m]
  {α : Type u} (x₁ : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α) (x₂ : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α) :
  [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α


StateT.orElse.{u, v} {σ : Type u}
  {m : Type u → Type v} [[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative") m]
  {α : Type u} (x₁ : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α)
  (x₂ : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α) :
  [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α


```

Recovers from errors. The state is rolled back on error recovery. Typically used via the `<|>` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateT.failure "Permalink")def
```


StateT.failure.{u, v} {σ : Type u} {m : Type u → Type v} [[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative") m]
  {α : Type u} : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α


StateT.failure.{u, v} {σ : Type u}
  {m : Type u → Type v} [[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative") m]
  {α : Type u} : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α


```

Fails with a recoverable error. The state is rolled back on error recovery.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateT.run' "Permalink")def
```


StateT.run'.{u, v} {σ : Type u} {m : Type u → Type v} [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m]
  {α : Type u} (x : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α) (s : σ) : m α


StateT.run'.{u, v} {σ : Type u}
  {m : Type u → Type v} [[Functor](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor") m]
  {α : Type u} (x : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α)
  (s : σ) : m α


```

Executes an action from a monad with added state in the underlying monad `m`. Given an initial state, it returns a value, discarding the final state.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateT.bind "Permalink")def
```


StateT.bind.{u, v} {σ : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α β : Type u} (x : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α) (f : α → [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m β) :
  [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m β


StateT.bind.{u, v} {σ : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α β : Type u} (x : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α)
  (f : α → [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m β) : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m β


```

Sequences two actions. Typically used via the `>>=` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateT.modifyGet "Permalink")def
```


StateT.modifyGet.{u, v} {σ : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type u} (f : σ → α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ) : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α


StateT.modifyGet.{u, v} {σ : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type u} (f : σ → α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ) :
  [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α


```

Applies a function to the current state that both computes a new state and a value. The new state replaces the current state, and the value is returned.
It is equivalent to `do let (a, s) := f (← StateT.get); StateT.set s; pure a`. However, using `[StateT.modifyGet](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT___modifyGet "Documentation for StateT.modifyGet")` may lead to better performance because it doesn't add a new reference to the state value, and additional references can inhibit in-place updates of data.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateT.lift "Permalink")def
```


StateT.lift.{u, v} {σ : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type u} (t : m α) : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α


StateT.lift.{u, v} {σ : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type u} (t : m α) : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α


```

Runs an action from the underlying monad in the monad with state. The state is not modified.
This function is typically implicitly accessed via a `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT")` instance as part of [automatic lifting](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=monad-lifting).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateT.map "Permalink")def
```


StateT.map.{u, v} {σ : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α β : Type u} (f : α → β) (x : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α) : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m β


StateT.map.{u, v} {σ : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α β : Type u} (f : α → β)
  (x : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α) : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m β


```

Modifies the value returned by a computation. Typically used via the `<$>` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateT.pure "Permalink")def
```


StateT.pure.{u, v} {σ : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type u} (a : α) : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α


StateT.pure.{u, v} {σ : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type u} (a : α) : [StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ m α


```

Returns the given value without modifying the state. Typically used via `[Pure.pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")`.
###  18.5.4.3. State Monads in Continuation Passing Style[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Varieties-of-Monads--State--State-Monads-in-Continuation-Passing-Style "Permalink")
Continuation-passing-style state monads represent stateful computations as functions that, for any type whatsoever, take an initial state and a continuation (modeled as a function) that accepts a value and an updated state. An example of such a type is `(δ : Type u) → σ → (α → σ → δ) → δ`, though `[StateCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateCpsT "Documentation for StateCpsT")` is a transformer that can be applied to any monad. State monads in continuation passing style have different performance characteristics than tuple-based state monads; for some applications, it may be worth benchmarking them.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateCpsT "Permalink")def
```


StateCpsT.{u, v} (σ : Type u) (m : Type u → Type v) (α : Type u) :
  Type (max (u + 1) v)


StateCpsT.{u, v} (σ : Type u)
  (m : Type u → Type v) (α : Type u) :
  Type (max (u + 1) v)


```

An alternative implementation of a state monad transformer that internally uses continuation passing style instead of tuples.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateCpsT.lift "Permalink")def
```


StateCpsT.lift.{u, v} {α σ : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (x : m α) : [StateCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateCpsT "Documentation for StateCpsT") σ m α


StateCpsT.lift.{u, v} {α σ : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (x : m α) : [StateCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateCpsT "Documentation for StateCpsT") σ m α


```

Runs an action from the underlying monad in the monad with state. The state is not modified.
This function is typically implicitly accessed via a `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT")` instance as part of [automatic lifting](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=monad-lifting).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateCpsT.runK "Permalink")def
```


StateCpsT.runK.{u, v} {α σ : Type u} {m : Type u → Type v} {β : Type u}
  (x : [StateCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateCpsT "Documentation for StateCpsT") σ m α) (s : σ) (k : α → σ → m β) : m β


StateCpsT.runK.{u, v} {α σ : Type u}
  {m : Type u → Type v} {β : Type u}
  (x : [StateCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateCpsT "Documentation for StateCpsT") σ m α) (s : σ)
  (k : α → σ → m β) : m β


```

Runs a stateful computation that's represented using continuation passing style by providing it with an initial state and a continuation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateCpsT.run' "Permalink")def
```


StateCpsT.run'.{u, v} {α σ : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (x : [StateCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateCpsT "Documentation for StateCpsT") σ m α) (s : σ) : m α


StateCpsT.run'.{u, v} {α σ : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (x : [StateCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateCpsT "Documentation for StateCpsT") σ m α) (s : σ) : m α


```

Executes an action from a monad with added state in the underlying monad `m`. Given an initial state, it returns a value, discarding the final state.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateCpsT.run "Permalink")def
```


StateCpsT.run.{u, v} {α σ : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (x : [StateCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateCpsT "Documentation for StateCpsT") σ m α) (s : σ) : m [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


StateCpsT.run.{u, v} {α σ : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (x : [StateCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateCpsT "Documentation for StateCpsT") σ m α) (s : σ) :
  m [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Executes an action from a monad with added state in the underlying monad `m`. Given an initial state, it returns a value paired with the final state.
While the state is internally represented in continuation passing style, the resulting value is the same as for a non-CPS state monad.
###  18.5.4.4. State Monads from Mutable References[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Varieties-of-Monads--State--State-Monads-from-Mutable-References "Permalink")
The monad `[StateRefT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Lean___Parser___Term___stateRefT "Documentation for syntax") σ m` is a specialized state monad transformer that can be used when `m` is a monad to which `[ST](IO/Mutable-References/#ST "Documentation for ST")` computations can be lifted. It implements the operations of `[MonadState](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadState___mk "Documentation for MonadState")` using an `[ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref")`, rather than pure functions. This ensures that mutation is actually used at run time.
`[ST](IO/Mutable-References/#ST "Documentation for ST")` and `[EST](IO/Mutable-References/#EST "Documentation for EST")` require a phantom type parameter that's used together with `[runST](IO/Mutable-References/#runST "Documentation for runST")`'s polymorphic function argument to encapsulate mutability. Rather than require this as a parameter to the transformer, an auxiliary type class `[STWorld](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#STWorld___mk "Documentation for STWorld")` is used to propagate it directly from `m`.
The transformer itself is defined as a [syntax extension](Notations-and-Macros/Defining-New-Syntax/#syntax-ext) and an [elaborator](Notations-and-Macros/Elaborators/#elaborators), rather than an ordinary function. This is because `[STWorld](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#STWorld___mk "Documentation for STWorld")` has no methods: it exists only to propagate information from the inner monad to the transformed monad. Nonetheless, its instances are terms; keeping them around could lead to unnecessarily large types.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=STWorld "Permalink")type class
```


STWorld (σ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") Type) (m : Type → Type) : Type


STWorld (σ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") Type)
  (m : Type → Type) : Type


```

An auxiliary class used to infer the “state” of `[EST](IO/Mutable-References/#EST "Documentation for EST")` and `[ST](IO/Mutable-References/#ST "Documentation for ST")` monads.
#  Instance Constructor

```
[STWorld.mk](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#STWorld___mk "Documentation for STWorld.mk")
```

syntax`StateRefT`
The syntax for `[StateRefT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Lean___Parser___Term___stateRefT "Documentation for syntax") σ m` accepts two arguments:

```
term ::= ...
    | 


A state monad that uses an actual mutable reference cell (i.e. an ST.Ref).


This is syntax, rather than a function, to make it easier to use. Its elaborator synthesizes an
appropriate parameter for the underlying monad's ST effects, then passes it to StateRefT'.


StateRefT term (macroDollarArg
       | term)
```

Its elaborator synthesizes an instance of `[STWorld](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#STWorld___mk "Documentation for STWorld") ω m` to ensure that `m` supports mutable references. Having discovered the value of `ω`, it then produces the term `[StateRefT'](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateRefT___ "Documentation for StateRefT'") ω σ m`, discarding the synthesized instance.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateRefT' "Permalink")def
```


StateRefT' (ω σ : Type) (m : Type → Type) (α : Type) : Type


StateRefT' (ω σ : Type) (m : Type → Type)
  (α : Type) : Type


```

A state monad that uses an actual mutable reference cell (i.e. an `[ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") ω σ`).
The macro `[StateRefT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Lean___Parser___Term___stateRefT "Documentation for syntax") σ m α` infers `ω` from `m`. It should normally be used instead.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateRefT'.get "Permalink")def
```


StateRefT'.get {ω σ : Type} {m : Type → Type} [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") ω) m] :
  [StateRefT'](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateRefT___ "Documentation for StateRefT'") ω σ m σ


StateRefT'.get {ω σ : Type}
  {m : Type → Type}
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") ω) m] :
  [StateRefT'](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateRefT___ "Documentation for StateRefT'") ω σ m σ


```

Retrieves the current value of the monad's mutable state.
This increments the reference count of the state, which may inhibit in-place updates.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateRefT'.set "Permalink")def
```


StateRefT'.set {ω σ : Type} {m : Type → Type} [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") ω) m]
  (s : σ) : [StateRefT'](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateRefT___ "Documentation for StateRefT'") ω σ m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


StateRefT'.set {ω σ : Type}
  {m : Type → Type} [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") ω) m]
  (s : σ) : [StateRefT'](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateRefT___ "Documentation for StateRefT'") ω σ m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Replaces the mutable state with a new value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateRefT'.modifyGet "Permalink")def
```


StateRefT'.modifyGet {ω σ : Type} {m : Type → Type} {α : Type}
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") ω) m] (f : σ → α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ) : [StateRefT'](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateRefT___ "Documentation for StateRefT'") ω σ m α


StateRefT'.modifyGet {ω σ : Type}
  {m : Type → Type} {α : Type}
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") ω) m] (f : σ → α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ) :
  [StateRefT'](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateRefT___ "Documentation for StateRefT'") ω σ m α


```

Applies a function to the current state that both computes a new state and a value. The new state replaces the current state, and the value is returned.
It is equivalent to a `get` followed by a `[set](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf.set")`. However, using `modifyGet` may lead to higher performance because it doesn't add a new reference to the state value. Additional references can inhibit in-place updates of data.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateRefT'.run "Permalink")def
```


StateRefT'.run {ω σ : Type} {m : Type → Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") ω) m] {α : Type} (x : [StateRefT'](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateRefT___ "Documentation for StateRefT'") ω σ m α) (s : σ) :
  m [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


StateRefT'.run {ω σ : Type}
  {m : Type → Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") ω) m] {α : Type}
  (x : [StateRefT'](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateRefT___ "Documentation for StateRefT'") ω σ m α) (s : σ) :
  m [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Executes an action from a monad with added state in the underlying monad `m`. Given an initial state, it returns a value paired with the final state.
The monad `m` must support `[ST](IO/Mutable-References/#ST "Documentation for ST")` effects in order to create and mutate reference cells.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateRefT'.run' "Permalink")def
```


StateRefT'.run' {ω σ : Type} {m : Type → Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") ω) m] {α : Type} (x : [StateRefT'](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateRefT___ "Documentation for StateRefT'") ω σ m α) (s : σ) :
  m α


StateRefT'.run' {ω σ : Type}
  {m : Type → Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") ω) m] {α : Type}
  (x : [StateRefT'](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateRefT___ "Documentation for StateRefT'") ω σ m α) (s : σ) : m α


```

Executes an action from a monad with added state in the underlying monad `m`. Given an initial state, it returns a value, discarding the final state.
The monad `m` must support `[ST](IO/Mutable-References/#ST "Documentation for ST")` effects in order to create and mutate reference cells.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StateRefT'.lift "Permalink")def
```


StateRefT'.lift {ω σ : Type} {m : Type → Type} {α : Type} (x : m α) :
  [StateRefT'](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateRefT___ "Documentation for StateRefT'") ω σ m α


StateRefT'.lift {ω σ : Type}
  {m : Type → Type} {α : Type} (x : m α) :
  [StateRefT'](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateRefT___ "Documentation for StateRefT'") ω σ m α


```

Runs an action from the underlying monad in the monad with state. The state is not modified.
This function is typically implicitly accessed via a `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT")` instance as part of [automatic lifting](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=monad-lifting).
##  18.5.5. Reader[🔗](find/?domain=Verso.Genre.Manual.section&name=reader-monad "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadReader "Permalink")type class
```


MonadReader.{u, v} (ρ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type u)) (m : Type u → Type v) :
  Type v


MonadReader.{u, v} (ρ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type u))
  (m : Type u → Type v) : Type v


```

Reader monads provide the ability to implicitly thread a value through a computation. The value can be read, but not written. A `[MonadWithReader](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadWithReader___mk "Documentation for MonadWithReader") ρ` instance additionally allows the value to be locally overridden for a sub-computation.
In this class, `ρ` is an `[outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam")`, which means that it is inferred from `m`. `[MonadReaderOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadReaderOf___mk "Documentation for MonadReaderOf") ρ` provides the same operations, but allows `ρ` to influence instance synthesis.
#  Instance Constructor

```
[MonadReader.mk](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadReader___mk "Documentation for MonadReader.mk").{u, v}
```

#  Methods

```
read : m ρ
```

Retrieves the local value.
Use `[readThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#readThe "Documentation for readThe")` to explicitly specify a type when more than one value is available.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadReaderOf "Permalink")type class
```


MonadReaderOf.{u, v} (ρ : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Type u)) (m : Type u → Type v) :
  Type v


MonadReaderOf.{u, v}
  (ρ : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Type u))
  (m : Type u → Type v) : Type v


```

Reader monads provide the ability to implicitly thread a value through a computation. The value can be read, but not written. A `[MonadWithReader](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadWithReader___mk "Documentation for MonadWithReader") ρ` instance additionally allows the value to be locally overridden for a sub-computation.
In this class, `ρ` is a `[semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam")`, which means that it can influence the choice of instance. `[MonadReader](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadReader___mk "Documentation for MonadReader") ρ` provides the same operations, but requires that `ρ` be inferable from `m`.
#  Instance Constructor

```
[MonadReaderOf.mk](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadReaderOf___mk "Documentation for MonadReaderOf.mk").{u, v}
```

#  Methods

```
read : m ρ
```

Retrieves the local value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=readThe "Permalink")def
```


readThe.{u, v} (ρ : Type u) {m : Type u → Type v} [[MonadReaderOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadReaderOf___mk "Documentation for MonadReaderOf") ρ m] :
  m ρ


readThe.{u, v} (ρ : Type u)
  {m : Type u → Type v}
  [[MonadReaderOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadReaderOf___mk "Documentation for MonadReaderOf") ρ m] : m ρ


```

Retrieves the local value whose type is `ρ`. This is useful when a monad supports reading more than one type of value.
Use `[read](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadReader___mk "Documentation for MonadReader.read")` for a version that expects the type `ρ` to be inferred from `m`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadWithReader.mk "Permalink")type class
```


MonadWithReader.{u, v} (ρ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type u)) (m : Type u → Type v) :
  Type (max (u + 1) v)


MonadWithReader.{u, v}
  (ρ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type u))
  (m : Type u → Type v) :
  Type (max (u + 1) v)


```

A reader monad that additionally allows the value to be locally overridden.
In this class, `ρ` is an `[outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam")`, which means that it is inferred from `m`. `[MonadWithReaderOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadWithReaderOf___mk "Documentation for MonadWithReaderOf") ρ` provides the same operations, but allows `ρ` to influence instance synthesis.
#  Instance Constructor

```
[MonadWithReader.mk](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadWithReader___mk "Documentation for MonadWithReader.mk").{u, v}
```

#  Methods

```
withReader : {α : Type u} → (ρ → ρ) → m α → m α
```

Locally modifies the reader monad's value while running an action.
During the inner action `x`, reading the value returns `f` applied to the original value. After control returns from `x`, the reader monad's value is restored.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadWithReaderOf.withReader "Permalink")type class
```


MonadWithReaderOf.{u, v} (ρ : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Type u))
  (m : Type u → Type v) : Type (max (u + 1) v)


MonadWithReaderOf.{u, v}
  (ρ : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Type u))
  (m : Type u → Type v) :
  Type (max (u + 1) v)


```

A reader monad that additionally allows the value to be locally overridden.
In this class, `ρ` is a `[semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam")`, which means that it can influence the choice of instance. `[MonadWithReader](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadWithReader___mk "Documentation for MonadWithReader") ρ` provides the same operations, but requires that `ρ` be inferable from `m`.
#  Instance Constructor

```
[MonadWithReaderOf.mk](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadWithReaderOf___mk "Documentation for MonadWithReaderOf.mk").{u, v}
```

#  Methods

```
withReader : {α : Type u} → (ρ → ρ) → m α → m α
```

Locally modifies the reader monad's value while running an action.
During the inner action `x`, reading the value returns `f` applied to the original value. After control returns from `x`, the reader monad's value is restored.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=withTheReader "Permalink")def
```


withTheReader.{u, v} (ρ : Type u) {m : Type u → Type v}
  [[MonadWithReaderOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadWithReaderOf___mk "Documentation for MonadWithReaderOf") ρ m] {α : Type u} (f : ρ → ρ) (x : m α) : m α


withTheReader.{u, v} (ρ : Type u)
  {m : Type u → Type v}
  [[MonadWithReaderOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadWithReaderOf___mk "Documentation for MonadWithReaderOf") ρ m] {α : Type u}
  (f : ρ → ρ) (x : m α) : m α


```

Locally modifies the reader monad's value while running an action, with the reader monad's local value type specified explicitly. This is useful when a monad supports reading more than one type of value.
During the inner action `x`, reading the value returns `f` applied to the original value. After control returns from `x`, the reader monad's value is restored.
Use `[withReader](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadWithReader___mk "Documentation for MonadWithReader.withReader")` for a version that expects the local value's type to be inferred from `m`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ReaderT "Permalink")def
```


ReaderT.{u, v} (ρ : Type u) (m : Type u → Type v) (α : Type u) :
  Type (max u v)


ReaderT.{u, v} (ρ : Type u)
  (m : Type u → Type v) (α : Type u) :
  Type (max u v)


```

Adds the ability to access a read-only value of type `ρ` to a monad. The value can be locally overridden by `[withReader](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadWithReader___mk "Documentation for MonadWithReader.withReader")`, but it cannot be mutated.
Actions in the resulting monad are functions that take the local value as a parameter, returning ordinary actions in `m`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ReaderM "Permalink")def
```


ReaderM.{u} (ρ α : Type u) : Type u


ReaderM.{u} (ρ α : Type u) : Type u


```

A monad with access to a read-only value of type `ρ`. The value can be locally overridden by `[withReader](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadWithReader___mk "Documentation for MonadWithReader.withReader")`, but it cannot be mutated.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ReaderT.run "Permalink")def
```


ReaderT.run.{u, v} {ρ : Type u} {m : Type u → Type v} {α : Type u}
  (x : [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m α) (r : ρ) : m α


ReaderT.run.{u, v} {ρ : Type u}
  {m : Type u → Type v} {α : Type u}
  (x : [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m α) (r : ρ) : m α


```

Executes an action from a monad with a read-only value in the underlying monad `m`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ReaderT.read "Permalink")def
```


ReaderT.read.{u, v} {ρ : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] :
  [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m ρ


ReaderT.read.{u, v} {ρ : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] :
  [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m ρ


```

Retrieves the reader monad's local value. Typically accessed via `[read](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadReader___mk "Documentation for MonadReader.read")`, or via `[readThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#readThe "Documentation for readThe")` when more than one local value is available.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ReaderT.adapt "Permalink")def
```


ReaderT.adapt.{u, v} {ρ : Type u} {m : Type u → Type v} {ρ' α : Type u}
  (f : ρ' → ρ) : [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m α → [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ' m α


ReaderT.adapt.{u, v} {ρ : Type u}
  {m : Type u → Type v} {ρ' α : Type u}
  (f : ρ' → ρ) :
  [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m α → [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ' m α


```

Modifies a reader monad's local value with `f`. The resulting computation applies `f` to the incoming local value and passes the result to the inner computation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ReaderT.pure "Permalink")def
```


ReaderT.pure.{u, v} {ρ : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type u} (a : α) : [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m α


ReaderT.pure.{u, v} {ρ : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type u} (a : α) : [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m α


```

Returns the provided value `a`, ignoring the reader monad's local value. Typically used via `[Pure.pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ReaderT.bind "Permalink")def
```


ReaderT.bind.{u, v} {ρ : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α β : Type u} (x : [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m α) (f : α → [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m β) :
  [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m β


ReaderT.bind.{u, v} {ρ : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α β : Type u} (x : [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m α)
  (f : α → [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m β) : [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m β


```

Sequences two reader monad computations. Both are provided with the local value, and the second is passed the value of the first. Typically used via the `>>=` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ReaderT.orElse "Permalink")def
```


ReaderT.orElse.{u_1, u_2} {m : Type u_1 → Type u_2} {ρ α : Type u_1}
  [[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative") m] (x₁ : [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m α) (x₂ : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m α) :
  [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m α


ReaderT.orElse.{u_1, u_2}
  {m : Type u_1 → Type u_2}
  {ρ α : Type u_1} [[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative") m]
  (x₁ : [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m α)
  (x₂ : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m α) :
  [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m α


```

Recovers from errors. The same local value is provided to both branches. Typically used via the `<|>` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ReaderT.failure "Permalink")def
```


ReaderT.failure.{u_1, u_2} {m : Type u_1 → Type u_2} {ρ α : Type u_1}
  [[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative") m] : [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m α


ReaderT.failure.{u_1, u_2}
  {m : Type u_1 → Type u_2}
  {ρ α : Type u_1} [[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative") m] :
  [ReaderT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ReaderT "Documentation for ReaderT") ρ m α


```

Fails with a recoverable error.
##  18.5.6. Option[🔗](find/?domain=Verso.Genre.Manual.section&name=option-monad "Permalink")
Ordinarily, `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` is thought of as data, similarly to a nullable type. It can also be considered as a monad, and thus a way of performing computations. The `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` monad and its transformer `[OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT")` can be understood as describing computations that may terminate early, discarding the results. Callers can check for early termination and invoke a fallback if desired using `OrElse.orElse` or by treating it as a `[MonadExcept](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=OptionT "Permalink")def
```


OptionT.{u, v} (m : Type u → Type v) (α : Type u) : Type v


OptionT.{u, v} (m : Type u → Type v)
  (α : Type u) : Type v


```

Adds the ability to fail to a monad. Unlike ordinary exceptions, there is no way to signal why a failure occurred.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=OptionT.run "Permalink")def
```


OptionT.run.{u, v} {m : Type u → Type v} {α : Type u}
  (x : [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)


OptionT.run.{u, v} {m : Type u → Type v}
  {α : Type u} (x : [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α) :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)


```

Executes an action that might fail in the underlying monad `m`, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` in case of failure.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=OptionT.lift "Permalink")def
```


OptionT.lift.{u, v} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type u}
  (x : m α) : [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α


OptionT.lift.{u, v} {m : Type u → Type v}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type u} (x : m α) :
  [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α


```

Converts a computation from the underlying monad into one that could fail, even though it does not.
This function is typically implicitly accessed via a `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT")` instance as part of [automatic lifting](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=monad-lifting).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=OptionT.mk "Permalink")def
```


OptionT.mk.{u, v} {m : Type u → Type v} {α : Type u}
  (x : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)) : [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α


OptionT.mk.{u, v} {m : Type u → Type v}
  {α : Type u} (x : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)) :
  [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α


```

Converts an action that returns an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` into one that might fail, with `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` indicating failure.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=OptionT.pure "Permalink")def
```


OptionT.pure.{u, v} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type u}
  (a : α) : [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α


OptionT.pure.{u, v} {m : Type u → Type v}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type u} (a : α) :
  [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α


```

Succeeds with the provided value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=OptionT.bind "Permalink")def
```


OptionT.bind.{u, v} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α β : Type u}
  (x : [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α) (f : α → [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m β) : [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m β


OptionT.bind.{u, v} {m : Type u → Type v}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α β : Type u}
  (x : [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α)
  (f : α → [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m β) : [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m β


```

Sequences two potentially-failing actions. The second action is run only if the first succeeds.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=OptionT.fail "Permalink")def
```


OptionT.fail.{u, v} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type u} :
  [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α


OptionT.fail.{u, v} {m : Type u → Type v}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type u} : [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α


```

A recoverable failure.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=OptionT.orElse "Permalink")def
```


OptionT.orElse.{u, v} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {α : Type u}
  (x : [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α) (y : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α) : [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α


OptionT.orElse.{u, v}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type u} (x : [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α)
  (y : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α) : [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α


```

Recovers from failures. Typically used via the `<|>` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=OptionT.tryCatch "Permalink")def
```


OptionT.tryCatch.{u, v, u_1} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type u} (x : [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α) (handle : [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit") → [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α) :
  [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α


OptionT.tryCatch.{u, v, u_1}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type u} (x : [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α)
  (handle : [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit") → [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α) :
  [OptionT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#OptionT "Documentation for OptionT") m α


```

Handles failures by treating them as exceptions of type `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")`.
##  18.5.7. Exceptions[🔗](find/?domain=Verso.Genre.Manual.section&name=exception-monads "Permalink")
Exception monads describe computations that terminate early (fail). Failing computations provide their caller with an _exception_ value that describes _why_ they failed. In other words, computations either return a value or an exception. The inductive type `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except")` captures this pattern, and is itself a monad.
###  18.5.7.1. Exceptions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Varieties-of-Monads--Exceptions--Exceptions "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=Exception%E2%86%AAExcept "Permalink")inductive type
```


Except.{u, v} (ε : Type u) (α : Type v) : Type (max u v)


Except.{u, v} (ε : Type u) (α : Type v) :
  Type (max u v)


```

`[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α` is a type which represents either an error of type `ε` or a successful result with a value of type `α`.
`Except ε : Type u → Type v` is a `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")` that represents computations that may throw exceptions: the `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")` operation is `[Except.ok](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.ok")` and the `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")` operation returns the first encountered `[Except.error](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.error")`.
#  Constructors

```
error.{u, v} {ε : Type u} {α : Type v} : ε → [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α
```

A failure value of type `ε`

```
ok.{u, v} {ε : Type u} {α : Type v} : α → [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α
```

A success value of type `α`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Except.pure "Permalink")def
```


Except.pure.{u, u_1} {ε : Type u} {α : Type u_1} (a : α) : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α


Except.pure.{u, u_1} {ε : Type u}
  {α : Type u_1} (a : α) : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α


```

A successful computation in the `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε` monad: `a` is returned, and no exception is thrown.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Except.bind "Permalink")def
```


Except.bind.{u, u_1, u_2} {ε : Type u} {α : Type u_1} {β : Type u_2}
  (ma : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α) (f : α → [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε β) : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε β


Except.bind.{u, u_1, u_2} {ε : Type u}
  {α : Type u_1} {β : Type u_2}
  (ma : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α) (f : α → [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε β) :
  [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε β


```

Sequences two operations that may throw exceptions, allowing the second to depend on the value returned by the first.
If the first operation throws an exception, then it is the result of the computation. If the first succeeds but the second throws an exception, then that exception is the result. If both succeed, then the result is the result of the second computation.
This is the implementation of the `>>=` operator for `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Except.map "Permalink")def
```


Except.map.{u, u_1, u_2} {ε : Type u} {α : Type u_1} {β : Type u_2}
  (f : α → β) : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α → [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε β


Except.map.{u, u_1, u_2} {ε : Type u}
  {α : Type u_1} {β : Type u_2}
  (f : α → β) : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α → [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε β


```

Transforms a successful result with a function, doing nothing when an exception is thrown.
Examples:
  * `([pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") 2 : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")).[map](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___map "Documentation for Except.map") toString = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") 2`
  * `([throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") "Error" : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")).[map](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___map "Documentation for Except.map") toString = [throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") "Error"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Except.mapError "Permalink")def
```


Except.mapError.{u, u_1, u_2} {ε : Type u} {ε' : Type u_1}
  {α : Type u_2} (f : ε → ε') : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α → [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε' α


Except.mapError.{u, u_1, u_2} {ε : Type u}
  {ε' : Type u_1} {α : Type u_2}
  (f : ε → ε') : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α → [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε' α


```

Transforms exceptions with a function, doing nothing on successful results.
Examples:
  * `([pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") 2 : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")).[mapError](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___mapError "Documentation for Except.mapError") (·.[length](Basic-Types/Strings/#String___length "Documentation for String.length")) = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") 2`
  * `([throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") "Error" : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")).[mapError](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___mapError "Documentation for Except.mapError") (·.[length](Basic-Types/Strings/#String___length "Documentation for String.length")) = [throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") 5`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Except.tryCatch "Permalink")def
```


Except.tryCatch.{u, u_1} {ε : Type u} {α : Type u_1} (ma : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α)
  (handle : ε → [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α) : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α


Except.tryCatch.{u, u_1} {ε : Type u}
  {α : Type u_1} (ma : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α)
  (handle : ε → [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α) : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α


```

Handles exceptions thrown in the `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε` monad.
If `ma` is successful, its result is returned. If it throws an exception, then `handle` is invoked on the exception's value.
Examples:
  * `([pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") 2 : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")).[tryCatch](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___tryCatch "Documentation for Except.tryCatch") ([pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ·.[length](Basic-Types/Strings/#String___length "Documentation for String.length")) = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") 2`
  * `([throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") "Error" : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")).[tryCatch](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___tryCatch "Documentation for Except.tryCatch") ([pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ·.[length](Basic-Types/Strings/#String___length "Documentation for String.length")) = [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") 5`
  * `([throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") "Error" : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")).[tryCatch](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___tryCatch "Documentation for Except.tryCatch") (fun x => [throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") ("E: " ++ x)) = [throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") "E: Error"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Except.orElseLazy "Permalink")def
```


Except.orElseLazy.{u, u_1} {ε : Type u} {α : Type u_1} (x : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α)
  (y : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α) : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α


Except.orElseLazy.{u, u_1} {ε : Type u}
  {α : Type u_1} (x : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α)
  (y : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α) : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α


```

Recovers from exceptions thrown in the `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε` monad. Typically used via the `<|>` operator.
`[Except.tryCatch](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___tryCatch "Documentation for Except.tryCatch")` is a related operator that allows the recovery procedure to depend on _which_ exception was thrown.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Except.isOk "Permalink")def
```


Except.isOk.{u, u_1} {ε : Type u} {α : Type u_1} : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Except.isOk.{u, u_1} {ε : Type u}
  {α : Type u_1} : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the value is `[Except.ok](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.ok")`, `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` otherwise.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Except.toOption "Permalink")def
```


Except.toOption.{u, u_1} {ε : Type u} {α : Type u_1} :
  [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Except.toOption.{u, u_1} {ε : Type u}
  {α : Type u_1} : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if an exception was thrown, or `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` around the value on success.
Examples:
  * `([pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") 10 : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")).[toOption](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___toOption "Documentation for Except.toOption") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 10`
  * `([throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") "Failure" : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")).[toOption](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___toOption "Documentation for Except.toOption") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Except.toBool "Permalink")def
```


Except.toBool.{u, u_1} {ε : Type u} {α : Type u_1} : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Except.toBool.{u, u_1} {ε : Type u}
  {α : Type u_1} : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the value is `[Except.ok](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.ok")`, `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` otherwise.
###  18.5.7.2. Type Class[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Varieties-of-Monads--Exceptions--Type-Class "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadExcept "Permalink")type class
```


MonadExcept.{u, v, w} (ε : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type u)) (m : Type v → Type w) :
  Type (max (max u (v + 1)) w)


MonadExcept.{u, v, w}
  (ε : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type u))
  (m : Type v → Type w) :
  Type (max (max u (v + 1)) w)


```

Exception monads provide the ability to throw errors and handle errors.
In this class, `ε` is an `[outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam")`, which means that it is inferred from `m`. `[MonadExceptOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExceptOf___mk "Documentation for MonadExceptOf") ε` provides the same operations, but allows `ε` to influence instance synthesis.
`[MonadExcept.tryCatch](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.tryCatch")` is used to desugar `try ... catch ...` steps inside `do`-blocks when the handlers do not have exception type annotations.
#  Instance Constructor

```
[MonadExcept.mk](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.mk").{u, v, w}
```

#  Methods

```
throw : {α : Type v} → ε → m α
```

Throws an exception of type `ε` to the nearest enclosing handler.

```
tryCatch : {α : Type v} → m α → (ε → m α) → m α
```

Catches errors thrown in `body`, passing them to `handler`. Errors in `handler` are not caught.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadExcept.ofExcept "Permalink")def
```


MonadExcept.ofExcept.{u_1, u_2, u_3} {m : Type u_1 → Type u_2}
  {ε : Type u_3} {α : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[MonadExcept](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept") ε m] :
  [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α → m α


MonadExcept.ofExcept.{u_1, u_2, u_3}
  {m : Type u_1 → Type u_2} {ε : Type u_3}
  {α : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[MonadExcept](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept") ε m] : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α → m α


```

Re-interprets an `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε` action in an exception monad `m`, succeeding if it succeeds and throwing an exception if it throws an exception.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadExcept.orElse "Permalink")def
```


MonadExcept.orElse.{u, v, w} {ε : Type u} {m : Type v → Type w}
  [[MonadExcept](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept") ε m] {α : Type v} (t₁ : m α) (t₂ : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → m α) : m α


MonadExcept.orElse.{u, v, w} {ε : Type u}
  {m : Type v → Type w} [[MonadExcept](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept") ε m]
  {α : Type v} (t₁ : m α)
  (t₂ : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → m α) : m α


```

Unconditional error recovery that ignores which exception was thrown. Usually used via the `<|>` operator.
If both computations throw exceptions, then the result is the second exception.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadExcept.orelse' "Permalink")def
```


MonadExcept.orelse'.{u, v, w} {ε : Type u} {m : Type v → Type w}
  [[MonadExcept](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept") ε m] {α : Type v} (t₁ t₂ : m α)
  (useFirstEx : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : m α


MonadExcept.orelse'.{u, v, w} {ε : Type u}
  {m : Type v → Type w} [[MonadExcept](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept") ε m]
  {α : Type v} (t₁ t₂ : m α)
  (useFirstEx : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : m α


```

An alternative unconditional error recovery operator that allows callers to specify which exception to throw in cases where both operations throw exceptions.
By default, the first is thrown, because the `<|>` operator throws the second.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadExceptOf.tryCatch "Permalink")type class
```


MonadExceptOf.{u, v, w} (ε : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Type u))
  (m : Type v → Type w) : Type (max (max u (v + 1)) w)


MonadExceptOf.{u, v, w}
  (ε : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Type u))
  (m : Type v → Type w) :
  Type (max (max u (v + 1)) w)


```

Exception monads provide the ability to throw errors and handle errors.
In this class, `ε` is a `[semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam")`, which means that it can influence the choice of instance. `[MonadExcept](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept") ε` provides the same operations, but requires that `ε` be inferable from `m`.
`[tryCatchThe](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#tryCatchThe "Documentation for tryCatchThe")`, which takes an explicit exception type, is used to desugar `try ... catch ...` steps inside `do`-blocks when the handlers have type annotations.
#  Instance Constructor

```
[MonadExceptOf.mk](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExceptOf___mk "Documentation for MonadExceptOf.mk").{u, v, w}
```

#  Methods

```
throw : {α : Type v} → ε → m α
```

Throws an exception of type `ε` to the nearest enclosing `catch`.

```
tryCatch : {α : Type v} → m α → (ε → m α) → m α
```

Catches errors thrown in `body`, passing them to `handler`. Errors in `handler` are not caught.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=throwThe "Permalink")def
```


throwThe.{u, v, w} (ε : Type u) {m : Type v → Type w}
  [[MonadExceptOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExceptOf___mk "Documentation for MonadExceptOf") ε m] {α : Type v} (e : ε) : m α


throwThe.{u, v, w} (ε : Type u)
  {m : Type v → Type w}
  [[MonadExceptOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExceptOf___mk "Documentation for MonadExceptOf") ε m] {α : Type v}
  (e : ε) : m α


```

Throws an exception, with the exception type specified explicitly. This is useful when a monad supports throwing more than one type of exception.
Use `[throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw")` for a version that expects the exception type to be inferred from `m`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=tryCatchThe "Permalink")def
```


tryCatchThe.{u, v, w} (ε : Type u) {m : Type v → Type w}
  [[MonadExceptOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExceptOf___mk "Documentation for MonadExceptOf") ε m] {α : Type v} (x : m α) (handle : ε → m α) : m α


tryCatchThe.{u, v, w} (ε : Type u)
  {m : Type v → Type w}
  [[MonadExceptOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExceptOf___mk "Documentation for MonadExceptOf") ε m] {α : Type v}
  (x : m α) (handle : ε → m α) : m α


```

Catches errors, recovering using `handle`. The exception type is specified explicitly. This is useful when a monad supports throwing or handling more than one type of exception.
Use `[tryCatch](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.tryCatch")`, for a version that expects the exception type to be inferred from `m`.
###  18.5.7.3. “Finally” Computations[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Varieties-of-Monads--Exceptions--___Finally___-Computations "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadFinally.mk "Permalink")type class
```


MonadFinally.{u, v} (m : Type u → Type v) : Type (max (u + 1) v)


MonadFinally.{u, v}
  (m : Type u → Type v) :
  Type (max (u + 1) v)


```

Monads that provide the ability to ensure an action happens, regardless of exceptions or other failures.
`[MonadFinally.tryFinally'](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally.tryFinally'")` is used to desugar `try ... finally ...` syntax.
#  Instance Constructor

```
[MonadFinally.mk](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally.mk").{u, v}
```

#  Methods

```
tryFinally' : {α β : Type u} → m α → ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → m β) → m [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")
```

Runs an action, ensuring that some other action always happens afterward.
More specifically, `tryFinally' x f` runs `x` and then the “finally” computation `f`. If `x` succeeds with some value `a : α`, `f (some a)` is returned. If `x` fails for `m`'s definition of failure, `f [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` is returned.
`[tryFinally'](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally.tryFinally'")` can be thought of as performing the same role as a `finally` block in an imperative programming language.
###  18.5.7.4. Transformer[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Varieties-of-Monads--Exceptions--Transformer "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ExceptT "Permalink")def
```


ExceptT.{u, v} (ε : Type u) (m : Type u → Type v) (α : Type u) : Type v


ExceptT.{u, v} (ε : Type u)
  (m : Type u → Type v) (α : Type u) :
  Type v


```

Adds exceptions of type `ε` to a monad `m`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ExceptT.lift "Permalink")def
```


[ExceptT.lift.{u,](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") [v}](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") [{](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")ε [:](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") Type u[}](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") [{](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")m [:](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") Type u → Type v[}](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") [[](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m[]](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")
  [{](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")α [:](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") Type u[}](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") [(](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")t [:](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m α[)](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") [:](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α


[ExceptT.lift.{u,](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") [v}](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") [{](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")ε [:](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") Type u[}](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")
  [{](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")m [:](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") Type u → Type v[}](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") [[](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m[]](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")
  [{](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")α [:](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") Type u[}](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") [(](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")t [:](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m α[)](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") [:](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α


```

Runs a computation from an underlying monad in the transformed monad with exceptions.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ExceptT.run "Permalink")def
```


ExceptT.run.{u, v} {ε : Type u} {m : Type u → Type v} {α : Type u}
  (x : [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α) : m ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α)


ExceptT.run.{u, v} {ε : Type u}
  {m : Type u → Type v} {α : Type u}
  (x : [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α) : m ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α)


```

Use a monadic action that may throw an exception as an action that may return an exception's value.
This is the inverse of `[ExceptT.mk](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT___mk "Documentation for ExceptT.mk")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ExceptT.pure "Permalink")def
```


ExceptT.pure.{u, v} {ε : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type u} (a : α) : [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α


ExceptT.pure.{u, v} {ε : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type u} (a : α) : [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α


```

Returns the value `a` without throwing exceptions or having any other effect.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ExceptT.bind "Permalink")def
```


ExceptT.bind.{u, v} {ε : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α β : Type u} (ma : [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α) (f : α → [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m β) :
  [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m β


ExceptT.bind.{u, v} {ε : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α β : Type u} (ma : [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α)
  (f : α → [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m β) : [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m β


```

Sequences two actions that may throw exceptions. Typically used via `do`-notation or the `>>=` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ExceptT.bindCont "Permalink")def
```


ExceptT.bindCont.{u, v} {ε : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α β : Type u} (f : α → [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m β) : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α → m ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε β)


ExceptT.bindCont.{u, v} {ε : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α β : Type u} (f : α → [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m β) :
  [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α → m ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε β)


```

Handles exceptions thrown by an action that can have no effects _other_ than throwing exceptions.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ExceptT.tryCatch "Permalink")def
```


ExceptT.tryCatch.{u, v} {ε : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type u} (ma : [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α) (handle : ε → [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α) :
  [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α


ExceptT.tryCatch.{u, v} {ε : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α : Type u} (ma : [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α)
  (handle : ε → [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α) :
  [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α


```

Handles exceptions produced in the `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε` transformer.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ExceptT.mk "Permalink")def
```


ExceptT.mk.{u, v} {ε : Type u} {m : Type u → Type v} {α : Type u}
  (x : m ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α)) : [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α


ExceptT.mk.{u, v} {ε : Type u}
  {m : Type u → Type v} {α : Type u}
  (x : m ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α)) : [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α


```

Use a monadic action that may return an exception's value as an action in the transformed monad that may throw the corresponding exception.
This is the inverse of `[ExceptT.run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT___run "Documentation for ExceptT.run")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ExceptT.map "Permalink")def
```


ExceptT.map.{u, v} {ε : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α β : Type u} (f : α → β) (x : [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α) : [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m β


ExceptT.map.{u, v} {ε : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {α β : Type u} (f : α → β)
  (x : [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α) : [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m β


```

Transforms a successful computation's value using `f`. Typically used via the `<$>` operator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ExceptT.adapt "Permalink")def
```


ExceptT.adapt.{u, v} {ε : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {ε' α : Type u} (f : ε → ε') : [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α → [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε' m α


ExceptT.adapt.{u, v} {ε : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {ε' α : Type u} (f : ε → ε') :
  [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε m α → [ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε' m α


```

Transforms exceptions using the function `f`.
This is the `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT")` version of `[Except.mapError](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___mapError "Documentation for Except.mapError")`.
###  18.5.7.5. Exception Monads in Continuation Passing Style[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Varieties-of-Monads--Exceptions--Exception-Monads-in-Continuation-Passing-Style "Permalink")
Continuation-passing-style exception monads represent potentially-failing computations as functions that take success and failure continuations, both of which return the same type, returning that type. They must work for _any_ return type. An example of such a type is `(β : Type u) → (α → β) → (ε → β) → β`. `[ExceptCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptCpsT "Documentation for ExceptCpsT")` is a transformer that can be applied to any monad, so `[ExceptCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptCpsT "Documentation for ExceptCpsT") ε m α` is actually defined as `(β : Type u) → (α → m β) → (ε → m β) → m β`. Exception monads in continuation passing style have different performance characteristics than `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except")`-based state monads; for some applications, it may be worth benchmarking them.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ExceptCpsT "Permalink")def
```


ExceptCpsT.{u, v} (ε : Type u) (m : Type u → Type v) (α : Type u) :
  Type (max (u + 1) v)


ExceptCpsT.{u, v} (ε : Type u)
  (m : Type u → Type v) (α : Type u) :
  Type (max (u + 1) v)


```

Adds exceptions of type `ε` to a monad `m`.
Instead of using `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε` to model exceptions, this implementation uses continuation passing style. This has different performance characteristics from `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ExceptCpsT.runCatch "Permalink")def
```


ExceptCpsT.runCatch.{u_1, u_2} {m : Type u_1 → Type u_2} {α : Type u_1}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (x : [ExceptCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptCpsT "Documentation for ExceptCpsT") α m α) : m α


ExceptCpsT.runCatch.{u_1, u_2}
  {m : Type u_1 → Type u_2} {α : Type u_1}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (x : [ExceptCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptCpsT "Documentation for ExceptCpsT") α m α) : m α


```

Returns the value of a computation, forgetting whether it was an exception or a success.
This corresponds to early return.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ExceptCpsT.runK "Permalink")def
```


ExceptCpsT.runK.{u, u_1} {m : Type u → Type u_1} {β ε α : Type u}
  (x : [ExceptCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptCpsT "Documentation for ExceptCpsT") ε m α) (s : ε) (ok : α → m β) (error : ε → m β) : m β


ExceptCpsT.runK.{u, u_1}
  {m : Type u → Type u_1} {β ε α : Type u}
  (x : [ExceptCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptCpsT "Documentation for ExceptCpsT") ε m α) (s : ε)
  (ok : α → m β) (error : ε → m β) : m β


```

Use a monadic action that may throw an exception by providing explicit success and failure continuations.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ExceptCpsT.run "Permalink")def
```


ExceptCpsT.run.{u, u_1} {m : Type u → Type u_1} {ε α : Type u} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (x : [ExceptCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptCpsT "Documentation for ExceptCpsT") ε m α) : m ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α)


ExceptCpsT.run.{u, u_1}
  {m : Type u → Type u_1} {ε α : Type u}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (x : [ExceptCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptCpsT "Documentation for ExceptCpsT") ε m α) :
  m ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α)


```

Use a monadic action that may throw an exception as an action that may return an exception's value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ExceptCpsT.lift "Permalink")def
```


ExceptCpsT.lift.{u_1, u_2} {m : Type u_1 → Type u_2} {α ε : Type u_1}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (x : m α) : [ExceptCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptCpsT "Documentation for ExceptCpsT") ε m α


ExceptCpsT.lift.{u_1, u_2}
  {m : Type u_1 → Type u_2}
  {α ε : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (x : m α) :
  [ExceptCpsT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptCpsT "Documentation for ExceptCpsT") ε m α


```

Run an action from the transformed monad in the exception monad.
##  18.5.8. Combined Error and State Monads[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Varieties-of-Monads--Combined-Error-and-State-Monads "Permalink")
The `[EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM")` monad has both exceptions and mutable state. `[EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α` is logically equivalent to `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε ([StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") σ) α`. While `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε ([StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") σ)` evaluates to the type `σ → [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α × σ`, the type `[EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α` evaluates to `σ → [EStateM.Result](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Result___ok "Documentation for EStateM.Result") ε σ α`. `[EStateM.Result](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Result___ok "Documentation for EStateM.Result")` is an inductive type that's very similar to `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except")`, except both constructors have an additional field for the state. In compiled code, this representation removes one level of indirection from each monadic bind.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EStateM "Permalink")def
```


EStateM.{u} (ε σ α : Type u) : Type u


EStateM.{u} (ε σ α : Type u) : Type u


```

A combined state and exception monad in which exceptions do not automatically roll back the state.
Instances of `[EStateM.Backtrackable](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Backtrackable___mk "Documentation for EStateM.Backtrackable")` provide a way to roll back some part of the state if needed.
`[EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ` is equivalent to `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") ε ([StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") σ)`, but it is more efficient.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EStateM.Result.error "Permalink")inductive type
```


EStateM.Result.{u} (ε σ α : Type u) : Type u


EStateM.Result.{u} (ε σ α : Type u) :
  Type u


```

The value returned from a combined state and exception monad in which exceptions do not automatically roll back the state.
`Result ε σ α` is equivalent to `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α × σ`, but using a single combined inductive type yields a more efficient data representation.
#  Constructors

```
ok.{u} {ε σ α : Type u} : α → σ → [EStateM.Result](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Result___ok "Documentation for EStateM.Result") ε σ α
```

A success value of type `α` and a new state `σ`.

```
error.{u} {ε σ α : Type u} : ε → σ → [EStateM.Result](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Result___ok "Documentation for EStateM.Result") ε σ α
```

An exception of type `ε` and a new state `σ`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EStateM.run "Permalink")def
```


EStateM.run.{u} {ε σ α : Type u} (x : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α) (s : σ) :
  [EStateM.Result](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Result___ok "Documentation for EStateM.Result") ε σ α


EStateM.run.{u} {ε σ α : Type u}
  (x : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α) (s : σ) :
  [EStateM.Result](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Result___ok "Documentation for EStateM.Result") ε σ α


```

Executes an `[EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM")` action with the initial state `s`. The returned value includes the final state and indicates whether an exception was thrown or a value was returned.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EStateM.run' "Permalink")def
```


EStateM.run'.{u} {ε σ α : Type u} (x : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α) (s : σ) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


EStateM.run'.{u} {ε σ α : Type u}
  (x : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α) (s : σ) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Executes an `[EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM")` with the initial state `s` for the returned value `α`, discarding the final state. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if an unhandled exception was thrown.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EStateM.adaptExcept "Permalink")def
```


EStateM.adaptExcept.{u} {ε σ α ε' : Type u} (f : ε → ε')
  (x : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α) : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε' σ α


EStateM.adaptExcept.{u}
  {ε σ α ε' : Type u} (f : ε → ε')
  (x : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α) : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε' σ α


```

Transforms exceptions with a function, doing nothing on successful results.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EStateM.fromStateM "Permalink")def
```


EStateM.fromStateM {ε σ α : Type} (x : [StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") σ α) : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α


EStateM.fromStateM {ε σ α : Type}
  (x : [StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") σ α) : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α


```

Converts a state monad action into a state monad action with exceptions.
The resulting action does not throw an exception.
###  18.5.8.1. State Rollback[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Varieties-of-Monads--Combined-Error-and-State-Monads--State-Rollback "Permalink")
Composing `[StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT")` and `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT")` in different orders causes exceptions to interact differently with state. In one ordering, state changes are rolled back when exceptions are caught; in the other, they persist. The latter option matches the semantics of most imperative programming languages, but the former is very useful for search-based problems. Often, some but not all state should be rolled back; this can be achieved by “sandwiching” `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT")` between two separate uses of `[StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT")`.
To avoid yet another layer of indirection via the use of `[StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") σ ([EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ') α`, `[EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM")` offers the `[EStateM.Backtrackable](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Backtrackable___mk "Documentation for EStateM.Backtrackable")` [type class](Type-Classes/#--tech-term-type-class). This class specifies some part of the state that can be saved and restored. `[EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM")` then arranges for the saving and restoring to take place around error handling.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EStateM.Backtrackable.restore "Permalink")type class
```


EStateM.Backtrackable.{u} (δ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type u)) (σ : Type u) : Type u


EStateM.Backtrackable.{u}
  (δ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type u)) (σ : Type u) :
  Type u


```

Exception handlers in `[EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM")` save some part of the state, determined by `δ`, and restore it if an exception is caught. By default, `δ` is `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")`, and no information is saved.
#  Instance Constructor

```
[EStateM.Backtrackable.mk](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Backtrackable___mk "Documentation for EStateM.Backtrackable.mk").{u}
```

#  Methods

```
save : σ → δ
```

Extracts the information in the state that should be rolled back if an exception is handled.

```
restore : σ → δ → σ
```

Updates the current state with the saved information that should be rolled back. This updated state becomes the current state when an exception is handled.
There is a universally-applicable instance of `[Backtrackable](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Backtrackable___mk "Documentation for EStateM.Backtrackable")` that neither saves nor restores anything. Because instance synthesis chooses the most recent instance first, the universal instance is used only if no other instance has been defined.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EStateM.nonBacktrackable "Permalink")def
```


EStateM.nonBacktrackable.{u} {σ : Type u} :
  [EStateM.Backtrackable](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Backtrackable___mk "Documentation for EStateM.Backtrackable") [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit") σ


EStateM.nonBacktrackable.{u}
  {σ : Type u} :
  [EStateM.Backtrackable](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Backtrackable___mk "Documentation for EStateM.Backtrackable") [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit") σ


```

A fallback `Backtrackable` instance that saves no information from a state. This allows every type to be used as a state in `[EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM")`, with no rollback.
Because this is the first declared instance of `Backtrackable _ σ`, it will be picked only if there are no other `Backtrackable _ σ` instances registered.
###  18.5.8.2. Implementations[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Varieties-of-Monads--Combined-Error-and-State-Monads--Implementations "Permalink")
These functions are typically not called directly, but rather are accessed through their corresponding type classes.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EStateM.map "Permalink")def
```


EStateM.map.{u} {ε σ α β : Type u} (f : α → β) (x : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α) :
  [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ β


EStateM.map.{u} {ε σ α β : Type u}
  (f : α → β) (x : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α) :
  [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ β


```

Transforms the value returned from an `[EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ` action using a function.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EStateM.pure "Permalink")def
```


EStateM.pure.{u} {ε σ α : Type u} (a : α) : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α


EStateM.pure.{u} {ε σ α : Type u}
  (a : α) : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α


```

Returns a value without modifying the state or throwing an exception.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EStateM.bind "Permalink")def
```


EStateM.bind.{u} {ε σ α β : Type u} (x : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α)
  (f : α → [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ β) : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ β


EStateM.bind.{u} {ε σ α β : Type u}
  (x : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α)
  (f : α → [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ β) : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ β


```

Sequences two `[EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ` actions, passing the returned value from the first into the second.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EStateM.orElse "Permalink")def
```


EStateM.orElse.{u} {ε σ α δ : Type u} [[EStateM.Backtrackable](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Backtrackable___mk "Documentation for EStateM.Backtrackable") δ σ]
  (x₁ : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α) (x₂ : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α) : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α


EStateM.orElse.{u} {ε σ α δ : Type u}
  [[EStateM.Backtrackable](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Backtrackable___mk "Documentation for EStateM.Backtrackable") δ σ]
  (x₁ : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α)
  (x₂ : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α) :
  [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α


```

Failure handling that does not depend on specific exception values.
The `Backtrackable δ σ` instance is used to save a snapshot of part of the state prior to running `x₁`. If an exception is caught, the state is updated with the saved snapshot, rolling back part of the state. If no instance of `Backtrackable` is provided, a fallback instance in which `δ` is `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")` is used, and no information is rolled back.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EStateM.orElse' "Permalink")def
```


EStateM.orElse'.{u} {ε σ α δ : Type u} [[EStateM.Backtrackable](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Backtrackable___mk "Documentation for EStateM.Backtrackable") δ σ]
  (x₁ x₂ : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α) (useFirstEx : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α


EStateM.orElse'.{u} {ε σ α δ : Type u}
  [[EStateM.Backtrackable](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Backtrackable___mk "Documentation for EStateM.Backtrackable") δ σ]
  (x₁ x₂ : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α)
  (useFirstEx : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) :
  [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α


```

Alternative orElse operator that allows callers to select which exception should be used when both operations fail. The default is to use the first exception since the standard `orElse` uses the second.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EStateM.seqRight "Permalink")def
```


EStateM.seqRight.{u} {ε σ α β : Type u} (x : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α)
  (y : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ β) : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ β


EStateM.seqRight.{u} {ε σ α β : Type u}
  (x : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α)
  (y : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ β) :
  [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ β


```

Sequences two `[EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ` actions, running `x` before `y`. The first action's return value is ignored.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EStateM.tryCatch "Permalink")def
```


EStateM.tryCatch.{u} {ε σ δ : Type u} [[EStateM.Backtrackable](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Backtrackable___mk "Documentation for EStateM.Backtrackable") δ σ]
  {α : Type u} (x : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α) (handle : ε → [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α) :
  [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α


EStateM.tryCatch.{u} {ε σ δ : Type u}
  [[EStateM.Backtrackable](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM___Backtrackable___mk "Documentation for EStateM.Backtrackable") δ σ] {α : Type u}
  (x : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α)
  (handle : ε → [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α) :
  [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α


```

Handles exceptions thrown in the combined error and state monad.
The `Backtrackable δ σ` instance is used to save a snapshot of part of the state prior to running `x`. If an exception is caught, the state is updated with the saved snapshot, rolling back part of the state. If no instance of `Backtrackable` is provided, a fallback instance in which `δ` is `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")` is used, and no information is rolled back.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EStateM.throw "Permalink")def
```


EStateM.throw.{u} {ε σ α : Type u} (e : ε) : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α


EStateM.throw.{u} {ε σ α : Type u}
  (e : ε) : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α


```

Throws an exception of type `ε` to the nearest enclosing handler.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EStateM.get "Permalink")def
```


EStateM.get.{u} {ε σ : Type u} : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ σ


EStateM.get.{u} {ε σ : Type u} :
  [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ σ


```

Retrieves the current value of the monad's mutable state.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EStateM.set "Permalink")def
```


EStateM.set.{u} {ε σ : Type u} (s : σ) : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


EStateM.set.{u} {ε σ : Type u} (s : σ) :
  [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Replaces the current value of the mutable state with a new one.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EStateM.modifyGet "Permalink")def
```


EStateM.modifyGet.{u} {ε σ α : Type u} (f : σ → α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ) : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α


EStateM.modifyGet.{u} {ε σ α : Type u}
  (f : σ → α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") σ) : [EStateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#EStateM "Documentation for EStateM") ε σ α


```

Applies a function to the current state that both computes a new state and a value. The new state replaces the current state, and the value is returned.
It is equivalent to `do let (a, s) := f (← get); set s; pure a`. However, using `modifyGet` may lead to higher performance because it doesn't add a new reference to the state value. Additional references can inhibit in-place updates of data.
[←18.4. API Reference](Functors___-Monads-and--do--Notation/API-Reference/#The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--API-Reference "18.4. API Reference")[19. Basic Propositions→](Basic-Propositions/#basic-props "19. Basic Propositions")

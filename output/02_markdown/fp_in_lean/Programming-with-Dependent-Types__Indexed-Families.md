[←7. Programming with Dependent Types](Programming-with-Dependent-Types/#Functional-Programming-in-Lean--Programming-with-Dependent-Types "7. Programming with Dependent Types")[7.2. The Universe Design Pattern→](Programming-with-Dependent-Types/The-Universe-Design-Pattern/#universe-pattern "7.2. The Universe Design Pattern")
#  7.1. Indexed Families[🔗](find/?domain=Verso.Genre.Manual.section&name=indexed-families "Permalink")
Polymorphic inductive types take type arguments. For instance, `[List](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List in Lean Language Reference")` takes an argument that determines the type of the entries in the list, and `[Except](https://lean-lang.org/doc/reference/4.26.0/Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except in Lean Language Reference")` takes arguments that determine the types of the exceptions or values. These type arguments, which are the same in every constructor of the datatype, are referred to as _parameters_.
Arguments to inductive types need not be the same in every constructor, however. Inductive types in which the arguments to the type vary based on the choice of constructor are called _indexed families_ , and the arguments that vary are referred to as _indices_. The “hello world” of indexed families is a type of lists that contains the length of the list in addition to the type of entries, conventionally referred to as “vectors”:
`inductive Vect (α : Type u) : [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference") → Type u where    | nil : Vect α 0    | cons : α → Vect α n → Vect α (n + 1)`
The type of a vector of three `[String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference")`s includes the fact that it contains three `[String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference")`s:
`example : Vect [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference") 3 :=   .cons "one" (.cons "two" (.cons "three" .nil))`
Function declarations may take some arguments before the colon, indicating that they are available in the entire definition, and some arguments after, indicating a desire to pattern-match on them and define the function case by case. Inductive datatypes have a similar principle: the argument `α` is named at the top of the datatype declaration, prior to the colon, which indicates that it is a parameter that must be provided as the first argument in all occurrences of `Vect` in the definition, while the `[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")` argument occurs after the colon, indicating that it is an index that may vary. Indeed, the three occurrences of `Vect` in the `nil` and `cons` constructor declarations consistently provide `α` as the first argument, while the second argument is different in each case.
The declaration of `nil` states that it is a constructor of type `Vect α 0`. This means that using `Vect.nil` in a context expecting a `Vect [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference") 3` is a type error, just as `[1, 2, 3]` is a type error in a context that expects a `[List](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List in Lean Language Reference") [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference")`:
`example : Vect [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference") 3 := `Type mismatch   Vect.nil has type   Vect ?m.3 0 but is expected to have type   Vect [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference") 3`Vect.nil`
```
Type mismatch
  Vect.nil
has type
  Vect ?m.3 0
but is expected to have type
  Vect [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference") 3
```

The mismatch between `0` and `3` in this example plays exactly the same role as any other type mismatch, even though `0` and `3` are not themselves types. The metavariable in the message can be ignored because its presence indicates that `Vect.nil` can have any element type.
Indexed families are called _families_ of types because different index values can make different constructors available for use. In some sense, an indexed family is not a type; rather, it is a collection of related types, and the choice of index values also chooses a type from the collection. Choosing the index `5` for `Vect` means that only the constructor `cons` is available, and choosing the index `0` means that only `nil` is available.
If the index is not yet known (e.g. because it is a variable), then no constructor can be used until it becomes known. Using `n` for the length allows neither `Vect.nil` nor `Vect.cons`, because there's no way to know whether the variable `n` should stand for a `[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")` that matches `0` or `n + 1`:
`example : Vect [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference") n := `Type mismatch   Vect.nil has type   Vect ?m.2 0 but is expected to have type   Vect [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference") n`Vect.nil`
```
Type mismatch
  Vect.nil
has type
  Vect ?m.2 0
but is expected to have type
  Vect [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference") n
```
`example : Vect [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference") n := `Type mismatch   Vect.cons "Hello" (Vect.cons "world" Vect.nil) has type   Vect [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference") [(](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference")0 [+](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference") 1 [+](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference") 1[)](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference") but is expected to have type   Vect [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference") n`Vect.cons "Hello" (Vect.cons "world" Vect.nil)`
```
Type mismatch
  Vect.cons "Hello" (Vect.cons "world" Vect.nil)
has type
  Vect [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference") [(](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference")0 [+](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference") 1 [+](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference") 1[)](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference")
but is expected to have type
  Vect [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference") n
```

Having the length of the list as part of its type means that the type becomes more informative. For example, `Vect.replicate` is a function that creates a `Vect` with a number of copies of a given value. The type that says this precisely is:
`def Vect.replicate (n : [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")) (x : α) : Vect α n := `don't know how to synthesize placeholder context: α:Type u_1n:[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")x:α⊢ Vect α n`_`
The argument `n` appears as the length of the result. The message associated with the underscore placeholder describes the task at hand:

```
don't know how to synthesize placeholder
context:
α:Type u_1n:[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")x:α⊢ Vect α n
```

When working with indexed families, constructors can only be applied when Lean can see that the constructor's index matches the index in the expected type. However, neither constructor has an index that matches `n`—`nil` matches `[Nat.zero](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.zero in Lean Language Reference")`, and `cons` matches `[Nat.succ](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ in Lean Language Reference")`. Just as in the example type errors, the variable `n` could stand for either, depending on which `[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")` is provided to the function as an argument. The solution is to use pattern matching to consider both of the possible cases:
`def Vect.replicate (n : [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")) (x : α) : Vect α n :=   [match](https://lean-lang.org/doc/reference/4.26.0/Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax in Lean Language Reference") n [with](https://lean-lang.org/doc/reference/4.26.0/Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax in Lean Language Reference")   | 0 => `don't know how to synthesize placeholder context: α:Type u_1n:[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")x:α⊢ Vect α 0`_ | k + 1 => `don't know how to synthesize placeholder context: α:Type u_1n:[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")x:αk:[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")⊢ Vect α [(](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference")k [+](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference") 1[)](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference")`_`
Because `n` occurs in the expected type, pattern matching on `n` _refines_ the expected type in the two cases of the match. In the first underscore, the expected type has become `Vect α 0`:

```
don't know how to synthesize placeholder
context:
α:Type u_1n:[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")x:α⊢ Vect α 0
```

In the second underscore, it has become `Vect α (k + 1)`:

```
don't know how to synthesize placeholder
context:
α:Type u_1n:[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")x:αk:[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")⊢ Vect α [(](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference")k [+](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference") 1[)](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference")
```

When pattern matching refines the type of a program in addition to discovering the structure of a value, it is called _dependent pattern matching_.
The refined type makes it possible to apply the constructors. The first underscore matches `Vect.nil`, and the second matches `Vect.cons`:
`def Vect.replicate (n : [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")) (x : α) : Vect α n :=   [match](https://lean-lang.org/doc/reference/4.26.0/Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax in Lean Language Reference") n [with](https://lean-lang.org/doc/reference/4.26.0/Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax in Lean Language Reference")   | 0 => .nil   | k + 1 => .cons `don't know how to synthesize placeholder context: α:Type u_1n:[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")x:αk:[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")⊢ α`_ `don't know how to synthesize placeholder context: α:Type u_1n:[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")x:αk:[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")⊢ Vect α k`_`
The first underscore under the `.cons` should have type `α`. There is an `α` available, namely `x`:

```
don't know how to synthesize placeholder
context:
α:Type u_1n:[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")x:αk:[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")⊢ α
```

The second underscore should be a `Vect α k`, which can be produced by a recursive call to `replicate`:

```
don't know how to synthesize placeholder
context:
α:Type u_1n:[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")x:αk:[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")⊢ Vect α k
```

Here is the final definition of `replicate`:
`def Vect.replicate (n : [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")) (x : α) : Vect α n :=   [match](https://lean-lang.org/doc/reference/4.26.0/Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax in Lean Language Reference") n [with](https://lean-lang.org/doc/reference/4.26.0/Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax in Lean Language Reference")   | 0 => .nil   | k + 1 => .cons x (replicate k x)`
In addition to providing assistance while writing the function, the informative type of `Vect.replicate` also allows client code to rule out a number of unexpected functions without having to read the source code. A version of `[replicate](Programming-with-Dependent-Types/Indexed-Families/#Extras___List___replicate "Definition of example")` for lists could produce a list of the wrong length:
`def List.replicate (n : [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")) (x : α) : [List](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List in Lean Language Reference") α :=   [match](https://lean-lang.org/doc/reference/4.26.0/Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax in Lean Language Reference") n [with](https://lean-lang.org/doc/reference/4.26.0/Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax in Lean Language Reference")   | 0 => []   | k + 1 => x :: x :: [replicate](Programming-with-Dependent-Types/Indexed-Families/#Extras___List___replicate "Definition of example") k x`
However, making this mistake with `Vect.replicate` is a type error:
`def Vect.replicate (n : [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")) (x : α) : Vect α n :=   [match](https://lean-lang.org/doc/reference/4.26.0/Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax in Lean Language Reference") n [with](https://lean-lang.org/doc/reference/4.26.0/Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax in Lean Language Reference")   | 0 => .nil   | k + 1 => .cons x `Application type mismatch: The argument   cons x (replicate k x) has type   Vect α [(](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference")k [+](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference") 1[)](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference") but is expected to have type   Vect α k in the application   cons x (cons x (replicate k x))`(.cons x (replicate k x))`
```
Application type mismatch: The argument
  cons x (replicate k x)
has type
  Vect α [(](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference")k [+](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference") 1[)](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference")
but is expected to have type
  Vect α k
in the application
  cons x (cons x (replicate k x))
```

The function `[List.zip](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___zip "Documentation for List.zip in Lean Language Reference")` combines two lists by pairing the first entry in the first list with the first entry in the second list, the second entry in the first list with the second entry in the second list, and so forth. `[List.zip](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___zip "Documentation for List.zip in Lean Language Reference")` can be used to pair the three highest peaks in the US state of Oregon with the three highest peaks in Denmark:
`["Mount Hood",  "Mount Jefferson",  "South Sister"].[zip](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___zip "Documentation for List.zip in Lean Language Reference") ["Møllehøj", "Yding Skovhøj", "Ejer Bavnehøj"]`
The result is a list of three pairs:
`[("Mount Hood", "Møllehøj"),  ("Mount Jefferson", "Yding Skovhøj"),  ("South Sister", "Ejer Bavnehøj")]`
It's somewhat unclear what should happen when the lists have different lengths. Like many languages, Lean chooses to ignore the extra entries in one of the lists. For instance, combining the heights of the five highest peaks in Oregon with those of the three highest peaks in Denmark yields three pairs. In particular,
`[3428.8, 3201, 3158.5, 3075, 3064].[zip](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___zip "Documentation for List.zip in Lean Language Reference") [170.86, 170.77, 170.35]`
evaluates to
`[(3428.8, 170.86), (3201, 170.77), (3158.5, 170.35)]`
While this approach is convenient because it always returns an answer, it runs the risk of throwing away data when the lists unintentionally have different lengths. F# takes a different approach: its version of `List.zip` throws an exception when the lengths don't match, as can be seen in this `fsi` session:

```
> List.zip [3428.8; 3201.0; 3158.5; 3075.0; 3064.0] [170.86; 170.77; 170.35];;

```

```
System.ArgumentException: The lists had different lengths.
list2 is 2 elements shorter than list1 (Parameter 'list2')
   at Microsoft.FSharp.Core.DetailedExceptions.invalidArgDifferentListLength[?](String arg1, String arg2, Int32 diff) in /builddir/build/BUILD/dotnet-v3.1.424-SDK/src/fsharp.3ef6f0b514198c0bfa6c2c09fefe41a740b024d5/src/fsharp/FSharp.Core/local.fs:line 24
   at Microsoft.FSharp.Primitives.Basics.List.zipToFreshConsTail[a,b](FSharpList`1 cons, FSharpList`1 xs1, FSharpList`1 xs2) in /builddir/build/BUILD/dotnet-v3.1.424-SDK/src/fsharp.3ef6f0b514198c0bfa6c2c09fefe41a740b024d5/src/fsharp/FSharp.Core/local.fs:line 918
   at Microsoft.FSharp.Primitives.Basics.List.zip[T1,T2](FSharpList`1 xs1, FSharpList`1 xs2) in /builddir/build/BUILD/dotnet-v3.1.424-SDK/src/fsharp.3ef6f0b514198c0bfa6c2c09fefe41a740b024d5/src/fsharp/FSharp.Core/local.fs:line 929
   at Microsoft.FSharp.Collections.ListModule.Zip[T1,T2](FSharpList`1 list1, FSharpList`1 list2) in /builddir/build/BUILD/dotnet-v3.1.424-SDK/src/fsharp.3ef6f0b514198c0bfa6c2c09fefe41a740b024d5/src/fsharp/FSharp.Core/list.fs:line 466
   at <StartupCode$FSI_0006>.$FSI_0006.main@()
Stopped due to error

```

This avoids accidentally discarding information, but crashing a program comes with its own difficulties. The Lean equivalent, which would use the `[Option](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Optional-Values/#Option___none "Documentation for Option in Lean Language Reference")` or `[Except](https://lean-lang.org/doc/reference/4.26.0/Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except in Lean Language Reference")` monads, would introduce a burden that may not be worth the safety.
Using `Vect`, however, it is possible to write a version of `zip` with a type that requires that both arguments have the same length:
`def Vect.zip : Vect α n → Vect β n → Vect (α × β) n   | .nil, .nil => .nil   | .cons x xs, .cons y ys => .cons (x, y) (zip xs ys)`
This definition only has patterns for the cases where either both arguments are `Vect.nil` or both arguments are `Vect.cons`, and Lean accepts the definition without a “missing cases” error like the one that results from a similar definition for `[List](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List in Lean Language Reference")`:
`def List.zip : [List](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List in Lean Language Reference") α → [List](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List in Lean Language Reference") β → [List](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List in Lean Language Reference") (α × β)   `Missing cases: ([List.cons](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons in Lean Language Reference") _ _), [[](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil in Lean Language Reference")[]](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil in Lean Language Reference") [[](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil in Lean Language Reference")[]](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil in Lean Language Reference"), ([List.cons](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons in Lean Language Reference") _ _)`| [], [] => [] | x :: xs, y :: ys => (x, y) :: [zip](Programming-with-Dependent-Types/Indexed-Families/#Other___List___zip "Definition of example") xs ys`
```
Missing cases:
([List.cons](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons in Lean Language Reference") _ _), [[](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil in Lean Language Reference")[]](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil in Lean Language Reference")
[[](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil in Lean Language Reference")[]](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil in Lean Language Reference"), ([List.cons](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons in Lean Language Reference") _ _)
```

This is because the constructor used in the first pattern, `nil` or `cons`, _refines_ the type checker's knowledge about the length `n`. When the first pattern is `nil`, the type checker can additionally determine that the length was `0`, so the only possible choice for the second pattern is `nil`. Similarly, when the first pattern is `cons`, the type checker can determine that the length was `k+1` for some `[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")` `k`, so the only possible choice for the second pattern is `cons`. Indeed, adding a case that uses `nil` and `cons` together is a type error, because the lengths don't match:
`def Vect.zip : Vect α n → Vect β n → Vect (α × β) n   | .nil, .nil => .nil   | .nil, `Type mismatch   Vect.cons y ys has type   Vect ?m.10 [(](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference")?m.16 [+](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference") 1[)](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference") but is expected to have type   Vect β 0`.cons y ys => .nil | .cons x xs, .cons y ys => .cons (x, y) (zip xs ys)`
```
Type mismatch
  Vect.cons y ys
has type
  Vect ?m.10 [(](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference")?m.16 [+](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference") 1[)](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference")
but is expected to have type
  Vect β 0
```

The refinement of the length can be observed by making `n` into an explicit argument:
`def Vect.zip : (n : [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")) → Vect α n → Vect β n → Vect (α × β) n   | 0, .nil, .nil => .nil   | k + 1, .cons x xs, .cons y ys => .cons (x, y) ([zip](Programming-with-Dependent-Types/Indexed-Families/#Details___Vect___zip "Definition of example") k xs ys)`
##  7.1.1. Exercises[🔗](find/?domain=Verso.Genre.Manual.section&name=indexed-families-exercises "Permalink")
Getting a feel for programming with dependent types requires experience, and the exercises in this section are very important. For each exercise, try to see which mistakes the type checker can catch, and which ones it can't, by experimenting with the code as you go. This is also a good way to develop a feel for the error messages.
  * Double-check that `Vect.zip` gives the right answer when combining the three highest peaks in Oregon with the three highest peaks in Denmark. Because `Vect` doesn't have the syntactic sugar that `[List](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Linked-Lists/#List___nil "Documentation for List in Lean Language Reference")` has, it can be helpful to begin by defining `oregonianPeaks : Vect [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference") 3` and `danishPeaks : Vect [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference") 3`.
  * Define a function `Vect.map` with type `(α → β) → Vect α n → Vect β n`.
  * Define a function `Vect.zipWith` that combines the entries in a `Vect` one at a time with a function. It should have the type `(α → β → γ) → Vect α n → Vect β n → Vect γ n`.
  * Define a function `Vect.unzip` that splits a `Vect` of pairs into a pair of `Vect`s. It should have the type `Vect (α × β) n → Vect α n × Vect β n`.
  * Define a function `Vect.push` that adds an entry to the _end_ of a `Vect`. Its type should be `Vect α n → α → Vect α (n + 1)` and `[#eval](https://lean-lang.org/doc/reference/4.26.0/Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax in Lean Language Reference") [Vect.push](Programming-with-Dependent-Types/Indexed-Families/#Vect___push "Definition of example") (.cons "snowy" .nil) "peaks"` should yield `Vect.cons "snowy" (Vect.cons "peaks" (Vect.nil))`.
  * Define a function `Vect.reverse` that reverses the order of a `Vect`.
  * Define a function `Vect.drop` with the following type: `(n : [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")) → Vect α (k + n) → Vect α k`. Verify that it works by checking that `[#eval](https://lean-lang.org/doc/reference/4.26.0/Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax in Lean Language Reference") [danishPeaks](Programming-with-Dependent-Types/Indexed-Families/#danishPeaks "Definition of example").[drop](Programming-with-Dependent-Types/Indexed-Families/#Vect___drop "Definition of example") 2` yields `Vect.cons "Ejer Bavnehøj" (Vect.nil)`.
  * Define a function `Vect.take` with type `(n : [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")) → Vect α (k + n) → Vect α n` that returns the first `n` entries in the `Vect`. Check that it works on an example. 

[←7. Programming with Dependent Types](Programming-with-Dependent-Types/#Functional-Programming-in-Lean--Programming-with-Dependent-Types "7. Programming with Dependent Types")[7.2. The Universe Design Pattern→](Programming-with-Dependent-Types/The-Universe-Design-Pattern/#universe-pattern "7.2. The Universe Design Pattern")

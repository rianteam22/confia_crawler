[←7.3. Worked Example: Typed Queries](Programming-with-Dependent-Types/Worked-Example___-Typed-Queries/#typed-queries "7.3. Worked Example: Typed Queries")[7.5. Pitfalls of Programming with Dependent Types→](Programming-with-Dependent-Types/Pitfalls-of-Programming-with-Dependent-Types/#dependent-type-pitfalls "7.5. Pitfalls of Programming with Dependent Types")
#  7.4. Indices, Parameters, and Universe Levels[🔗](find/?domain=Verso.Genre.Manual.section&name=indices-parameters-universe-levels "Permalink")
The distinction between indices and parameters of an inductive type is more than just a way to describe arguments to the type that either vary or do not between the constructors. Whether an argument to an inductive type is a parameter or an index also matters when it comes time to determine the relationships between their universe levels. In particular, an inductive type may have the same universe level as a parameter, but it must be in a larger universe than its indices. This restriction is necessary to ensure that Lean can be used as a theorem prover as well as a programming language—without it, Lean's logic would be inconsistent. Experimenting with error messages is a good way to illustrate these rules, as well as the precise rules that determine whether an argument to a type is a parameter or an index.
Generally speaking, the definition of an inductive type takes its parameters before a colon and its indices after the colon. Parameters are given names like function arguments, whereas indices only have their types described. This can be seen in the definition of `Vect`:
`inductive Vect (α : Type u) : [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference") → Type u where    | nil : Vect α 0    | cons : α → Vect α n → Vect α (n + 1)`
In this definition, `α` is a parameter and the `[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")` is an index. Parameters may be referred to throughout the definition (for example, `Vect.cons` uses `α` for the type of its first argument), but they must always be used consistently. Because indices are expected to change, they are assigned individual values at each constructor, rather than being provided as arguments at the top of the datatype definition.
A very simple datatype with a parameter is `WithParameter`:
`inductive WithParameter (α : Type u) : Type u where   | test : α → WithParameter α`
The universe level `u` can be used for both the parameter and for the inductive type itself, illustrating that parameters do not increase the universe level of a datatype. Similarly, when there are multiple parameters, the inductive type receives whichever universe level is greater:
`inductive WithTwoParameters (α : Type u) (β : Type v) : Type (max u v) where   | test : α → β → [WithTwoParameters](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithTwoParameters "Definition of example") α β`
Because parameters do not increase the universe level of a datatype, they can be more convenient to work with. Lean attempts to identify arguments that are described like indices (after the colon), but used like parameters, and turn them into parameters: Both of the following inductive datatypes have their parameter written after the colon:
`inductive WithParameterAfterColon : Type u → Type u where   | test : α → [WithParameterAfterColon](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithParameterAfterColon "Definition of example") α``inductive WithParameterAfterColon2 : Type u → Type u where   | test1 : α → [WithParameterAfterColon2](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithParameterAfterColon2 "Definition of example") α   | test2 : [WithParameterAfterColon2](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithParameterAfterColon2 "Definition of example") α`
When a parameter is not named in the initial datatype declaration, different names may be used for it in each constructor, so long as they are used consistently. The following declaration is accepted:
`inductive WithParameterAfterColonDifferentNames : Type u → Type u where   | test1 : α → [WithParameterAfterColonDifferentNames](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithParameterAfterColonDifferentNames "Definition of example") α   | test2 : β → [WithParameterAfterColonDifferentNames](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithParameterAfterColonDifferentNames "Definition of example") β`
However, this flexibility does not extend to datatypes that explicitly declare the names of their parameters:
`inductive WithParameterBeforeColonDifferentNames (α : Type u) : Type u where   | test1 : α → [WithParameterBeforeColonDifferentNames](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithParameterBeforeColonDifferentNames "Definition of example") α   `Mismatched inductive type parameter in   [WithParameterBeforeColonDifferentNames](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithParameterBeforeColonDifferentNames "Definition of example") β The provided argument   β is not definitionally equal to the expected parameter   α  Note: The value of parameter `α` must be fixed throughout the inductive declaration. Consider making this parameter an index if it must vary.`| test2 : β → [WithParameterBeforeColonDifferentNames](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithParameterBeforeColonDifferentNames "Definition of example") β`
```
Mismatched inductive type parameter in
  [WithParameterBeforeColonDifferentNames](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithParameterBeforeColonDifferentNames "Definition of example") β
The provided argument
  β
is not definitionally equal to the expected parameter
  α

Note: The value of parameter `α` must be fixed throughout the inductive declaration. Consider making this parameter an index if it must vary.
```

Similarly, attempting to name an index results in an error:
`inductive WithNamedIndex (α : Type u) : Type (u + 1) where   | test1 : [WithNamedIndex](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithNamedIndex "Definition of example") α   `Mismatched inductive type parameter in   [WithNamedIndex](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithNamedIndex "Definition of example") [(](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Tuples/#Prod___mk "Documentation for Prod in Lean Language Reference")α [×](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Tuples/#Prod___mk "Documentation for Prod in Lean Language Reference") α[)](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Tuples/#Prod___mk "Documentation for Prod in Lean Language Reference") The provided argument   α [×](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Tuples/#Prod___mk "Documentation for Prod in Lean Language Reference") α is not definitionally equal to the expected parameter   α  Note: The value of parameter `α` must be fixed throughout the inductive declaration. Consider making this parameter an index if it must vary.`| test2 : [WithNamedIndex](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithNamedIndex "Definition of example") α → [WithNamedIndex](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithNamedIndex "Definition of example") α → [WithNamedIndex](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithNamedIndex "Definition of example") (α × α)`
```
Mismatched inductive type parameter in
  [WithNamedIndex](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithNamedIndex "Definition of example") [(](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Tuples/#Prod___mk "Documentation for Prod in Lean Language Reference")α [×](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Tuples/#Prod___mk "Documentation for Prod in Lean Language Reference") α[)](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Tuples/#Prod___mk "Documentation for Prod in Lean Language Reference")
The provided argument
  α [×](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Tuples/#Prod___mk "Documentation for Prod in Lean Language Reference") α
is not definitionally equal to the expected parameter
  α

Note: The value of parameter `α` must be fixed throughout the inductive declaration. Consider making this parameter an index if it must vary.
```

Using an appropriate universe level and placing the index after the colon results in a declaration that is acceptable:
`inductive WithIndex : Type u → Type (u + 1) where   | test1 : [WithIndex](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithIndex "Definition of example") α   | test2 : [WithIndex](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithIndex "Definition of example") α → [WithIndex](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithIndex "Definition of example") α → [WithIndex](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#WithIndex "Definition of example") (α × α)`
Even though Lean can sometimes determine that an argument after the colon in an inductive type declaration is a parameter when it is used consistently in all constructors, all parameters are still required to come before all indices. Attempting to place a parameter after an index results in the argument being considered an index itself, which would require the universe level of the datatype to increase:
`inductive ParamAfterIndex : [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference") → Type u → Type u where   `Invalid universe level in constructor `ParamAfterIndex.test1`: Parameter `γ` has type   Type u at universe level   u+2 which is not less than or equal to the inductive type's resulting universe level   u+1`| test1 : [ParamAfterIndex](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#ParamAfterIndex "Definition of example") 0 γ | test2 : [ParamAfterIndex](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#ParamAfterIndex "Definition of example") n γ → [ParamAfterIndex](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#ParamAfterIndex "Definition of example") k γ → [ParamAfterIndex](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#ParamAfterIndex "Definition of example") (n + k) γ`
```
Invalid universe level in constructor `ParamAfterIndex.test1`: Parameter `γ` has type
  Type u
at universe level
  u+2
which is not less than or equal to the inductive type's resulting universe level
  u+1
```

Parameters need not be types. This example shows that ordinary datatypes such as `[Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")` may be used as parameters:
`inductive [NatParam](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#NatParam "Definition of example") (n : [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")) : [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference") → Type u where   `Mismatched inductive type parameter in   [NatParam](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#NatParam "Definition of example") 4 5 The provided argument   4 is not definitionally equal to the expected parameter   n  Note: The value of parameter `n` must be fixed throughout the inductive declaration. Consider making this parameter an index if it must vary.`| five : [NatParam](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#NatParam "Definition of example") 4 5`
```
Mismatched inductive type parameter in
  [NatParam](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#NatParam "Definition of example") 4 5
The provided argument
  4
is not definitionally equal to the expected parameter
  n

Note: The value of parameter `n` must be fixed throughout the inductive declaration. Consider making this parameter an index if it must vary.
```

Using the `n` as suggested causes the declaration to be accepted:
`inductive NatParam (n : [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")) : [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference") → Type u where   | five : [NatParam](Programming-with-Dependent-Types/Indices___-Parameters___-and-Universe-Levels/#NatParam "Definition of example") n 5`
What can be concluded from these experiments? The rules of parameters and indices are as follows:
  1. Parameters must be used identically in each constructor's type.
  2. All parameters must come before all indices.
  3. The universe level of the datatype being defined must be at least as large as the largest parameter, and strictly larger than the largest index.
  4. Named arguments written before the colon are always parameters, while arguments after the colon are typically indices. Lean may determine that the usage of arguments after the colon makes them into parameters if they are used consistently in all constructors and don't come after any indices.


When in doubt, the Lean command `#print` can be used to check how many of a datatype's arguments are parameters. For example, for `Vect`, it points out that the number of parameters is 1:
``inductive Vect.{u} : Type u → [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference") → Type u number of parameters: 1 constructors: Vect.nil : {α : Type u} → Vect α 0 Vect.cons : {α : Type u} → {n : [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")} → α → Vect α n → Vect α [(](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference")n [+](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference") 1[)](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference")`#print Vect`
```
inductive Vect.{u} : Type u → [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference") → Type u
number of parameters: 1
constructors:
Vect.nil : {α : Type u} → Vect α 0
Vect.cons : {α : Type u} → {n : [Nat](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat in Lean Language Reference")} → α → Vect α n → Vect α [(](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference")n [+](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference") 1[)](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd in Lean Language Reference")
```

It is worth thinking about which arguments should be parameters and which should be indices when choosing the order of arguments to a datatype. Having as many arguments as possible be parameters helps keep universe levels under control, which can make a complicated program easier to type check. One way to make this possible is to ensure that all parameters come before all indices in the argument list.
Additionally, even though Lean is capable of determining that arguments after the colon are nonetheless parameters by their usage, it's a good idea to write parameters with explicit names. This makes the intention clear to readers, and it causes Lean to report an error if the argument is mistakenly used inconsistently across the constructors. 
[←7.3. Worked Example: Typed Queries](Programming-with-Dependent-Types/Worked-Example___-Typed-Queries/#typed-queries "7.3. Worked Example: Typed Queries")[7.5. Pitfalls of Programming with Dependent Types→](Programming-with-Dependent-Types/Pitfalls-of-Programming-with-Dependent-Types/#dependent-type-pitfalls "7.5. Pitfalls of Programming with Dependent Types")

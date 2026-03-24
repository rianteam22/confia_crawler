[←5. Functors, Applicative Functors, and Monads](Functors___-Applicative-Functors___-and-Monads/#Functional-Programming-in-Lean--Functors___-Applicative-Functors___-and-Monads "5. Functors, Applicative Functors, and Monads")[5.2. Applicative Functors→](Functors___-Applicative-Functors___-and-Monads/Applicative-Functors/#applicative "5.2. Applicative Functors")
#  5.1. Structures and Inheritance[🔗](find/?domain=Verso.Genre.Manual.section&name=structure-inheritance "Permalink")
In order to understand the full definitions of `[Functor](https://lean-lang.org/doc/reference/4.26.0/Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor in Lean Language Reference")`, `[Applicative](https://lean-lang.org/doc/reference/4.26.0/Functors___-Monads-and--do--Notation/#Applicative___mk "Documentation for Applicative in Lean Language Reference")`, and `[Monad](https://lean-lang.org/doc/reference/4.26.0/Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad in Lean Language Reference")`, another Lean feature is necessary: structure inheritance. Structure inheritance allows one structure type to provide the interface of another, along with additional fields. This can be useful when modeling concepts that have a clear taxonomic relationship. For example, take a model of mythical creatures. Some of them are large, and some are small:
`structure MythicalCreature where   large : [Bool](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool in Lean Language Reference") deriving [Repr](https://lean-lang.org/doc/reference/4.26.0/Interacting-with-Lean/#Repr___mk "Documentation for Repr in Lean Language Reference")`
Behind the scenes, defining the `MythicalCreature` structure creates an inductive type with a single constructor called `mk`:
``MythicalCreature.mk (large : [Bool](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool in Lean Language Reference")) : MythicalCreature`[#check](https://lean-lang.org/doc/reference/4.26.0/Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax in Lean Language Reference") MythicalCreature.mk`
```
MythicalCreature.mk (large : [Bool](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool in Lean Language Reference")) : MythicalCreature
```

Similarly, a function `MythicalCreature.large` is created that actually extracts the field from the constructor:
``MythicalCreature.large (self : MythicalCreature) : [Bool](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool in Lean Language Reference")`[#check](https://lean-lang.org/doc/reference/4.26.0/Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax in Lean Language Reference") MythicalCreature.large`
```
MythicalCreature.large (self : MythicalCreature) : [Bool](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool in Lean Language Reference")
```

In most old stories, each monster can be defeated in some way. A description of a monster should include this information, along with whether it is large:
`structure Monster extends MythicalCreature where   vulnerability : [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference") deriving [Repr](https://lean-lang.org/doc/reference/4.26.0/Interacting-with-Lean/#Repr___mk "Documentation for Repr in Lean Language Reference")`
The `extends MythicalCreature` in the heading states that every monster is also mythical. To define a `Monster`, both the fields from `MythicalCreature` and the fields from `Monster` should be provided. A troll is a large monster that is vulnerable to sunlight:
`def troll : Monster where   large := [true](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool.true in Lean Language Reference")   [vulnerability](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#Monster___vulnerability "Definition of example") := "sunlight"`
Behind the scenes, inheritance is implemented using composition. The constructor `Monster.mk` takes a `MythicalCreature` as its argument:
``Monster.mk (toMythicalCreature : MythicalCreature) (vulnerability : [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference")) : Monster`[#check](https://lean-lang.org/doc/reference/4.26.0/Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax in Lean Language Reference") Monster.mk`
```
Monster.mk (toMythicalCreature : MythicalCreature) (vulnerability : [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference")) : Monster
```

In addition to defining functions to extract the value of each new field, a function `Monster.toMythicalCreature` is defined with type `Monster → MythicalCreature`. This can be used to extract the underlying creature.
Moving up the inheritance hierarchy in Lean is not the same thing as upcasting in object-oriented languages. An upcast operator causes a value from a derived class to be treated as an instance of the parent class, but the value retains its identity and structure. In Lean, however, moving up the inheritance hierarchy actually erases the underlying information. To see this in action, consider the result of evaluating `[troll](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#troll "Definition of example").toMythicalCreature`:
``{ large := true }`[#eval](https://lean-lang.org/doc/reference/4.26.0/Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax in Lean Language Reference") [troll](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#troll "Definition of example").toMythicalCreature`
```
{ large := true }
```

Only the fields of `MythicalCreature` remain.
Just like the `where` syntax, curly-brace notation with field names also works with structure inheritance:
`def troll : Monster := {large := [true](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool.true in Lean Language Reference"), [vulnerability](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#Monster___vulnerability "Definition of example") := "sunlight"}`
However, the anonymous angle-bracket notation that delegates to the underlying constructor reveals the internal details:
`def [troll](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#Foo___troll "Definition of example") : Monster := ⟨`Application type mismatch: The argument   [true](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool.true in Lean Language Reference") has type   [Bool](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool in Lean Language Reference") but is expected to have type   MythicalCreature in the application   Monster.mk [true](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool.true in Lean Language Reference")`[true](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool.true in Lean Language Reference"), "sunlight"⟩`
```
Application type mismatch: The argument
  [true](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool.true in Lean Language Reference")
has type
  [Bool](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool in Lean Language Reference")
but is expected to have type
  MythicalCreature
in the application
  Monster.mk [true](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool.true in Lean Language Reference")
```

An extra set of angle brackets is required, which invokes `MythicalCreature.mk` on `[true](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool.true in Lean Language Reference")`:
`def troll : Monster := ⟨⟨[true](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool.true in Lean Language Reference")⟩, "sunlight"⟩`
Lean's dot notation is capable of taking inheritance into account. In other words, the existing `MythicalCreature.large` can be used with a `Monster`, and Lean automatically inserts the call to `Monster.toMythicalCreature` before the call to `MythicalCreature.large`. However, this only occurs when using dot notation, and applying the field lookup function using normal function call syntax results in a type error:
`[#eval](https://lean-lang.org/doc/reference/4.26.0/Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax in Lean Language Reference") MythicalCreature.large `Application type mismatch: The argument   [troll](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#troll "Definition of example") has type   Monster but is expected to have type   MythicalCreature in the application   MythicalCreature.large [troll](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#troll "Definition of example")`[troll](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#troll "Definition of example")`
```
Application type mismatch: The argument
  [troll](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#troll "Definition of example")
has type
  Monster
but is expected to have type
  MythicalCreature
in the application
  MythicalCreature.large [troll](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#troll "Definition of example")
```

Dot notation can also take inheritance into account for user-defined functions. A small creature is one that is not large:
`def MythicalCreature.small (c : MythicalCreature) : [Bool](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool in Lean Language Reference") := !c.large`
Evaluating `[troll](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#troll "Definition of example").[small](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#MythicalCreature___small "Definition of example")` yields `[false](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool.false in Lean Language Reference")`, while attempting to evaluate `[MythicalCreature.small](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#MythicalCreature___small "Definition of example") [troll](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#troll "Definition of example")` results in:

```
Application type mismatch: The argument
  [troll](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#troll "Definition of example")
has type
  Monster
but is expected to have type
  MythicalCreature
in the application
  [MythicalCreature.small](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#MythicalCreature___small "Definition of example") [troll](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#troll "Definition of example")
```

##  5.1.1. Multiple Inheritance[🔗](find/?domain=Verso.Genre.Manual.section&name=multiple-structure-inheritance "Permalink")
A helper is a mythical creature that can provide assistance when given the correct payment:
`structure Helper extends MythicalCreature where   assistance : [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference")   payment : [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference") deriving [Repr](https://lean-lang.org/doc/reference/4.26.0/Interacting-with-Lean/#Repr___mk "Documentation for Repr in Lean Language Reference")`
For example, a _nisse_ is a kind of small elf that's known to help around the house when provided with tasty porridge:
`def nisse : Helper where   large := [false](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool.false in Lean Language Reference")   [assistance](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#Helper___assistance "Definition of example") := "household tasks"   [payment](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#Helper___payment "Definition of example") := "porridge"`
If domesticated, trolls make excellent helpers. They are strong enough to plow a whole field in a single night, though they require model goats to keep them satisfied with their lot in life. A monstrous assistant is a monster that is also a helper:
`structure MonstrousAssistant extends Monster, Helper where deriving [Repr](https://lean-lang.org/doc/reference/4.26.0/Interacting-with-Lean/#Repr___mk "Documentation for Repr in Lean Language Reference")`
A value of this structure type must fill in all of the fields from both parent structures:
`def domesticatedTroll : MonstrousAssistant where   large := [true](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool.true in Lean Language Reference")   assistance := "heavy labor"   payment := "toy goats"   [vulnerability](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#Monster___vulnerability "Definition of example") := "sunlight"`
Both of the parent structure types extend `MythicalCreature`. If multiple inheritance were implemented naïvely, then this could lead to a “diamond problem”, where it would be unclear which path to `large` should be taken from a given `MonstrousAssistant`. Should it take `large` from the contained `Monster` or from the contained `Helper`? In Lean, the answer is that the first specified path to the grandparent structure is taken, and the additional parent structures' fields are copied rather than having the new structure include both parents directly.
This can be seen by examining the signature of the constructor for `MonstrousAssistant`:
``MonstrousAssistant.mk (toMonster : Monster) (assistance payment : [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference")) : MonstrousAssistant`[#check](https://lean-lang.org/doc/reference/4.26.0/Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax in Lean Language Reference") MonstrousAssistant.mk`
```
MonstrousAssistant.mk (toMonster : Monster) (assistance payment : [String](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Strings/#String___mk "Documentation for String in Lean Language Reference")) : MonstrousAssistant
```

It takes a `Monster` as an argument, along with the two fields that `Helper` introduces on top of `MythicalCreature`. Similarly, while `MonstrousAssistant.toMonster` merely extracts the `Monster` from the constructor, `MonstrousAssistant.toHelper` has no `Helper` to extract. The `#print` command exposes its implementation:
``@[reducible] def MonstrousAssistant.toHelper : MonstrousAssistant → Helper := fun self => { toMythicalCreature := self.toMythicalCreature, [assistance](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#Helper___assistance "Definition of example") := self.assistance, [payment](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#Helper___payment "Definition of example") := self.payment }`#print MonstrousAssistant.toHelper`
```
@[reducible] def MonstrousAssistant.toHelper : MonstrousAssistant → Helper :=
fun self => { toMythicalCreature := self.toMythicalCreature, [assistance](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#Helper___assistance "Definition of example") := self.assistance, [payment](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#Helper___payment "Definition of example") := self.payment }
```

This function constructs a `Helper` from the fields of `MonstrousAssistant`. The `@[reducible]` attribute has the same effect as writing `abbrev`.
###  5.1.1.1. Default Declarations[🔗](find/?domain=Verso.Genre.Manual.section&name=inheritance-defaults "Permalink")
When one structure inherits from another, default field definitions can be used to instantiate the parent structure's fields based on the child structure's fields. If more size specificity is required than whether a creature is large or not, a dedicated datatype describing sizes can be used together with inheritance, yielding a structure in which the `large` field is computed from the contents of the `size` field:
`inductive Size where   | small   | medium   | large deriving [BEq](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq in Lean Language Reference")  structure SizedCreature extends MythicalCreature where   size : [Size](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#Size "Definition of example")   large := size == [Size.large](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#Size___large "Definition of example")`
This default definition is only a default definition, however. Unlike property inheritance in a language like C# or Scala, the definitions in the child structure are only used when no specific value for `large` is provided, and nonsensical results can occur:
`def nonsenseCreature : [SizedCreature](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#SizedCreature "Definition of example") where   large := [false](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool.false in Lean Language Reference")   size := [.large](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#Size___large "Definition of example")`
If the child structure should not deviate from the parent structure, there are a few options:
  1. Documenting the relationship, as is done for `[BEq](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq in Lean Language Reference")` and `[Hashable](https://lean-lang.org/doc/reference/4.26.0/Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable in Lean Language Reference")`
  2. Defining a proposition that the fields are related appropriately, and designing the API to require evidence that the proposition is true where it matters
  3. Not using inheritance at all


The second option could look like this:
`abbrev SizesMatch (sc : [SizedCreature](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#SizedCreature "Definition of example")) : Prop :=   sc.large = (sc.size == [Size.large](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#Size___large "Definition of example"))`
Note that a single equality sign is used to indicate the equality _proposition_ , while a double equality sign is used to indicate a function that checks equality and returns a `[Bool](https://lean-lang.org/doc/reference/4.26.0/Basic-Types/Booleans/#Bool___false "Documentation for Bool in Lean Language Reference")`. `SizesMatch` is defined as an `abbrev` because it should automatically be unfolded in proofs, so that `[decide](https://lean-lang.org/doc/reference/4.26.0/Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic in Lean Language Reference")` can see the equality that should be proven.
A _huldre_ is a medium-sized mythical creature—in fact, they are the same size as humans. The two sized fields on `huldre` match one another:
`def huldre : [SizedCreature](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#SizedCreature "Definition of example") where   size := [.medium](Functors___-Applicative-Functors___-and-Monads/Structures-and-Inheritance/#Size___medium "Definition of example")  example : SizesMatch huldre := by⊢ SizesMatch huldre   [decide](https://lean-lang.org/doc/reference/4.26.0/Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic in Lean Language Reference")All goals completed! 🐙`
###  5.1.1.2. Type Class Inheritance[🔗](find/?domain=Verso.Genre.Manual.section&name=type-class-inheritance "Permalink")
Behind the scenes, type classes are structures. Defining a new type class defines a new structure, and defining an instance creates a value of that structure type. They are then added to internal tables in Lean that allow it to find the instances upon request. A consequence of this is that type classes may inherit from other type classes.
Because it uses precisely the same language features, type class inheritance supports all the features of structure inheritance, including multiple inheritance, default implementations of parent types' methods, and automatic collapsing of diamonds. This is useful in many of the same situations that multiple interface inheritance is useful in languages like Java, C# and Kotlin. By carefully designing type class inheritance hierarchies, programmers can get the best of both worlds: a fine-grained collection of independently-implementable abstractions, and automatic construction of these specific abstractions from larger, more general abstractions. 
[←5. Functors, Applicative Functors, and Monads](Functors___-Applicative-Functors___-and-Monads/#Functional-Programming-in-Lean--Functors___-Applicative-Functors___-and-Monads "5. Functors, Applicative Functors, and Monads")[5.2. Applicative Functors→](Functors___-Applicative-Functors___-and-Monads/Applicative-Functors/#applicative "5.2. Applicative Functors")

[←21.9. Processes](IO/Processes/#io-processes "21.9. Processes")[21.11. Tasks and Threads→](IO/Tasks-and-Threads/#concurrency "21.11. Tasks and Threads")
#  21.10. Random Numbers[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Random-Numbers "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.setRandSeed "Permalink")def
```


IO.setRandSeed (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.setRandSeed (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Seeds the random number generator state used by `[IO.rand](IO/Random-Numbers/#IO___rand "Documentation for IO.rand")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.rand "Permalink")def
```


IO.rand (lo hi : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


IO.rand (lo hi : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns a pseudorandom number between `lo` and `hi`, using and updating a saved random generator state.
This state can be seeded using `[IO.setRandSeed](IO/Random-Numbers/#IO___setRandSeed "Documentation for IO.setRandSeed")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=randBool "Permalink")def
```


randBool.{u} {gen : Type u} [[RandomGen](IO/Random-Numbers/#RandomGen___mk "Documentation for RandomGen") gen] (g : gen) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") gen


randBool.{u} {gen : Type u}
  [[RandomGen](IO/Random-Numbers/#RandomGen___mk "Documentation for RandomGen") gen] (g : gen) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") gen


```

Generates a random Boolean.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=randNat "Permalink")def
```


randNat.{u} {gen : Type u} [[RandomGen](IO/Random-Numbers/#RandomGen___mk "Documentation for RandomGen") gen] (g : gen) (lo hi : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") gen


randNat.{u} {gen : Type u} [[RandomGen](IO/Random-Numbers/#RandomGen___mk "Documentation for RandomGen") gen]
  (g : gen) (lo hi : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") gen


```

Generates a random natural number in the interval [lo, hi].
##  21.10.1. Random Generators[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Random-Numbers--Random-Generators "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=RandomGen "Permalink")type class
```


RandomGen.{u} (g : Type u) : Type u


RandomGen.{u} (g : Type u) : Type u


```

Interface for random number generators.
#  Instance Constructor

```
[RandomGen.mk](IO/Random-Numbers/#RandomGen___mk "Documentation for RandomGen.mk").{u}
```

#  Methods

```
range : g → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

`range` returns the range of values returned by the generator.

```
next : g → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") g
```

`next` operation returns a natural number that is uniformly distributed the range returned by `range` (including both end points), and a new generator.

```
split : g → g [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") g
```

The 'split' operation allows one to obtain two distinct random number generators. This is very useful in functional programs (for example, when passing a random number generator down to recursive calls).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=StdGen "Permalink")structure
```


StdGen : Type


StdGen : Type


```

"Standard" random number generator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=stdRange "Permalink")def
```


stdRange : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


stdRange : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The range of values returned by `[StdGen](IO/Random-Numbers/#StdGen "Documentation for StdGen")`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=stdNext "Permalink")def
```


stdNext : [StdGen](IO/Random-Numbers/#StdGen "Documentation for StdGen") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [StdGen](IO/Random-Numbers/#StdGen "Documentation for StdGen")


stdNext : [StdGen](IO/Random-Numbers/#StdGen "Documentation for StdGen") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [StdGen](IO/Random-Numbers/#StdGen "Documentation for StdGen")


```

The next value from a `[StdGen](IO/Random-Numbers/#StdGen "Documentation for StdGen")`, paired with an updated generator state.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=stdSplit "Permalink")def
```


stdSplit : [StdGen](IO/Random-Numbers/#StdGen "Documentation for StdGen") → [StdGen](IO/Random-Numbers/#StdGen "Documentation for StdGen") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [StdGen](IO/Random-Numbers/#StdGen "Documentation for StdGen")


stdSplit : [StdGen](IO/Random-Numbers/#StdGen "Documentation for StdGen") → [StdGen](IO/Random-Numbers/#StdGen "Documentation for StdGen") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [StdGen](IO/Random-Numbers/#StdGen "Documentation for StdGen")


```

Splits a `[StdGen](IO/Random-Numbers/#StdGen "Documentation for StdGen")` into two separate states.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=mkStdGen "Permalink")def
```


mkStdGen (s : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) : [StdGen](IO/Random-Numbers/#StdGen "Documentation for StdGen")


mkStdGen (s : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) : [StdGen](IO/Random-Numbers/#StdGen "Documentation for StdGen")


```

Returns a standard number generator.
##  21.10.2. System Randomness[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Random-Numbers--System-Randomness "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.getRandomBytes "Permalink")opaque
```


IO.getRandomBytes (nBytes : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


IO.getRandomBytes (nBytes : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


```

Reads bytes from a system entropy source. It is not guaranteed to be cryptographically secure.
If `nBytes` is `0`, returns immediately with an empty buffer.
[←21.9. Processes](IO/Processes/#io-processes "21.9. Processes")[21.11. Tasks and Threads→](IO/Tasks-and-Threads/#concurrency "21.11. Tasks and Threads")

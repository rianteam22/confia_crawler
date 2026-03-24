[←21.3. Console Output](IO/Console-Output/#The-Lean-Language-Reference--IO--Console-Output "21.3. Console Output")[21.5. Files, File Handles, and Streams→](IO/Files___-File-Handles___-and-Streams/#The-Lean-Language-Reference--IO--Files___-File-Handles___-and-Streams "21.5. Files, File Handles, and Streams")
#  21.4. Mutable References[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Mutable-References "Permalink")
While ordinary [state monads](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#--tech-term-State-monads) encode stateful computations with tuples that track the contents of the state along with the computation's value, Lean's runtime system also provides mutable references that are always backed by mutable memory cells. Mutable references have a type `[IO.Ref](IO/Mutable-References/#IO___Ref "Documentation for IO.Ref")` that indicates that a cell is mutable, and reads and writes must be explicit. `[IO.Ref](IO/Mutable-References/#IO___Ref "Documentation for IO.Ref")` is implemented using `[ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref")`, so the entire [``](IO/Mutable-References/#mutable-st-references)`[ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref")` API may also be used with `[IO.Ref](IO/Mutable-References/#IO___Ref "Documentation for IO.Ref")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Ref "Permalink")def
```


IO.Ref (α : Type) : Type


IO.Ref (α : Type) : Type


```

Mutable reference cells that contain values of type `α`. These cells can read from and mutated in the `[IO](IO/Logical-Model/#IO "Documentation for IO")` monad.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.mkRef "Permalink")def
```


IO.mkRef {α : Type} (a : α) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([IO.Ref](IO/Mutable-References/#IO___Ref "Documentation for IO.Ref") α)


IO.mkRef {α : Type} (a : α) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([IO.Ref](IO/Mutable-References/#IO___Ref "Documentation for IO.Ref") α)


```

Creates a new mutable reference cell that contains `a`.
##  21.4.1. State Transformers[🔗](find/?domain=Verso.Genre.Manual.section&name=mutable-st-references "Permalink")
Mutable references are often useful in contexts where arbitrary side effects are undesired. They can give a significant speedup when Lean is unable to optimize pure operations into mutation, and some algorithms are more easily expressed using mutable references than with state monads. Additionally, it has a property that other side effects do not have: if all of the mutable references used by a piece of code are created during its execution, and no mutable references from the code escape to other code, then the result of evaluation is deterministic.
The `[ST](IO/Mutable-References/#ST "Documentation for ST")` monad is a restricted version of `[IO](IO/Logical-Model/#IO "Documentation for IO")` in which mutable state is the only side effect, and mutable references cannot escape.`[ST](IO/Mutable-References/#ST "Documentation for ST")` was first described by John Launchbury and Simon L Peyton Jones, 1994. “Lazy functional state threads”. In  _Proceedings of the ACM SIGPLAN 1994 Conference on Programming Language Design and Implementation._. `[ST](IO/Mutable-References/#ST "Documentation for ST")` takes a type parameter that is never used to classify any terms. The `[runST](IO/Mutable-References/#runST "Documentation for runST")` function, which allow escape from `[ST](IO/Mutable-References/#ST "Documentation for ST")`, requires that the `[ST](IO/Mutable-References/#ST "Documentation for ST")` action that is passed to it can instantiate this type parameter with _any_ type. This unknown type does not exist except as a parameter to a function, which means that values whose types are “marked” by it cannot escape its scope.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ST "Permalink")def
```


ST (σ α : Type) : Type


ST (σ α : Type) : Type


```

A restricted version of `[IO](IO/Logical-Model/#IO "Documentation for IO")` in which mutable state is the only side effect.
It is possible to run `[ST](IO/Mutable-References/#ST "Documentation for ST")` computations in a non-monadic context using `[runST](IO/Mutable-References/#runST "Documentation for runST")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=runST "Permalink")def
```


runST {α : Type} (x : (σ : Type) → [ST](IO/Mutable-References/#ST "Documentation for ST") σ α) : α


runST {α : Type}
  (x : (σ : Type) → [ST](IO/Mutable-References/#ST "Documentation for ST") σ α) : α


```

Runs an `[ST](IO/Mutable-References/#ST "Documentation for ST")` computation, in which mutable state via `[ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref")` is the only side effect.
As with `[IO](IO/Logical-Model/#IO "Documentation for IO")` and `[EIO](IO/Logical-Model/#EIO "Documentation for EIO")`, there is also a variation of `[ST](IO/Mutable-References/#ST "Documentation for ST")` that takes a custom error type as a parameter. Here, `[ST](IO/Mutable-References/#ST "Documentation for ST")` is analogous to `[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` rather than `[IO](IO/Logical-Model/#IO "Documentation for IO")`, because `[ST](IO/Mutable-References/#ST "Documentation for ST")` cannot result in errors being thrown.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EST "Permalink")def
```


EST (ε σ α : Type) : Type


EST (ε σ α : Type) : Type


```

A restricted version of `[IO](IO/Logical-Model/#IO "Documentation for IO")` in which mutable state and exceptions are the only side effects.
It is possible to run `[EST](IO/Mutable-References/#EST "Documentation for EST")` computations in a non-monadic context using `[runEST](IO/Mutable-References/#runEST "Documentation for runEST")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=runEST "Permalink")def
```


runEST {ε α : Type} (x : (σ : Type) → [EST](IO/Mutable-References/#EST "Documentation for EST") ε σ α) : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α


runEST {ε α : Type}
  (x : (σ : Type) → [EST](IO/Mutable-References/#EST "Documentation for EST") ε σ α) :
  [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α


```

Runs an `[EST](IO/Mutable-References/#EST "Documentation for EST")` computation, in which mutable state and exceptions are the only side effects.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ST.Ref.mk "Permalink")structure
```


ST.Ref (σ α : Type) : Type


ST.Ref (σ α : Type) : Type


```

Mutable reference cells that contain values of type `α`. These cells can read from and mutated in the `[ST](IO/Mutable-References/#ST "Documentation for ST") σ` monad.
#  Constructor

```
[ST.Ref.mk](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref.mk")
```

[🔗](find/?domain=Verso.Genre.Manual.doc&name=ST.mkRef "Permalink")def
```


ST.mkRef {σ : Type} {m : Type → Type} [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") σ) m] {α : Type}
  (a : α) : m ([ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ α)


ST.mkRef {σ : Type} {m : Type → Type}
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") σ) m] {α : Type}
  (a : α) : m ([ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ α)


```

Creates a new mutable reference that contains the provided value `a`.
###  21.4.1.1. Reading and Writing[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Mutable-References--State-Transformers--Reading-and-Writing "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ST.Ref.get "Permalink")def
```


ST.Ref.get {σ : Type} {m : Type → Type} [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") σ) m] {α : Type}
  (r : [ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ α) : m α


ST.Ref.get {σ : Type} {m : Type → Type}
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") σ) m] {α : Type}
  (r : [ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ α) : m α


```

Reads the value of a mutable reference.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ST.Ref.set "Permalink")def
```


ST.Ref.set {σ : Type} {m : Type → Type} [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") σ) m] {α : Type}
  (r : [ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ α) (a : α) : m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


ST.Ref.set {σ : Type} {m : Type → Type}
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") σ) m] {α : Type}
  (r : [ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ α) (a : α) : m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Replaces the value of a mutable reference.
Data races with `[get](IO/Mutable-References/#ST___Ref___get "Documentation for ST.Ref.get")` and `[set](IO/Mutable-References/#ST___Ref___set "Documentation for ST.Ref.set")`
`def main : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let balance ← [IO.mkRef](IO/Mutable-References/#IO___mkRef "Documentation for IO.mkRef") (100 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int"))    let mut orders := #[]   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "Sending out orders..."   for _ in [0:100] do     let o ← [IO.asTask](IO/Tasks-and-Threads/#IO___asTask "Documentation for IO.asTask") (prio := [.dedicated](IO/Tasks-and-Threads/#Task___Priority___dedicated "Documentation for Task.Priority.dedicated")) [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")       let cost ← [IO.rand](IO/Random-Numbers/#IO___rand "Documentation for IO.rand") 1 100       [IO.sleep](IO/Timing/#IO___sleep "Documentation for IO.sleep") (← [IO.rand](IO/Random-Numbers/#IO___rand "Documentation for IO.rand") 10 100).[toUInt32](Basic-Types/Natural-Numbers/#Nat___toUInt32 "Documentation for Nat.toUInt32")       if cost < (← balance.[get](IO/Mutable-References/#ST___Ref___get "Documentation for ST.Ref.get")) then         [IO.sleep](IO/Timing/#IO___sleep "Documentation for IO.sleep") (← [IO.rand](IO/Random-Numbers/#IO___rand "Documentation for IO.rand") 10 100).[toUInt32](Basic-Types/Natural-Numbers/#Nat___toUInt32 "Documentation for Nat.toUInt32")         balance.[set](IO/Mutable-References/#ST___Ref___set "Documentation for ST.Ref.set") ((← balance.[get](IO/Mutable-References/#ST___Ref___get "Documentation for ST.Ref.get")) - cost)     orders := orders.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") o    -- Wait until all orders are completed   for o in orders do     match o.[get](IO/Tasks-and-Threads/#Task___get "Documentation for Task.get") with     | [.ok](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.ok") () => [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ()     | [.error](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.error") e => [throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") e    if (← balance.[get](IO/Mutable-References/#ST___Ref___get "Documentation for ST.Ref.get")) < 0 then     [IO.eprintln](IO/Console-Output/#IO___eprintln "Documentation for IO.eprintln") "Final balance is negative!"   else     [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "Final balance is zero or positive." `
`stdout``Sending out orders...`
`stderr``Final balance is negative!`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ST.Ref.modify "Permalink")def
```


ST.Ref.modify {σ : Type} {m : Type → Type} [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") σ) m]
  {α : Type} (r : [ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ α) (f : α → α) : m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


ST.Ref.modify {σ : Type} {m : Type → Type}
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") σ) m] {α : Type}
  (r : [ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ α) (f : α → α) : m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Atomically modifies a mutable reference cell by replacing its contents with the result of a function call.
Avoiding data races with `[modify](IO/Mutable-References/#ST___Ref___modify "Documentation for ST.Ref.modify")`
This program launches 100 threads. Each thread simulates a purchase attempt: it generates a random price, and if the account balance is sufficient, it decrements it by the price. The balance check and the computation of the new value occur in an atomic call to `[ST.Ref.modify](IO/Mutable-References/#ST___Ref___modify "Documentation for ST.Ref.modify")`.
`def main : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let balance ← [IO.mkRef](IO/Mutable-References/#IO___mkRef "Documentation for IO.mkRef") (100 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int"))    let mut orders := #[]   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "Sending out orders..."   for _ in [0:100] do     let o ← [IO.asTask](IO/Tasks-and-Threads/#IO___asTask "Documentation for IO.asTask") (prio := [.dedicated](IO/Tasks-and-Threads/#Task___Priority___dedicated "Documentation for Task.Priority.dedicated")) [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")       let cost ← [IO.rand](IO/Random-Numbers/#IO___rand "Documentation for IO.rand") 1 100       [IO.sleep](IO/Timing/#IO___sleep "Documentation for IO.sleep") (← [IO.rand](IO/Random-Numbers/#IO___rand "Documentation for IO.rand") 10 100).[toUInt32](Basic-Types/Natural-Numbers/#Nat___toUInt32 "Documentation for Nat.toUInt32")       balance.[modify](IO/Mutable-References/#ST___Ref___modify "Documentation for ST.Ref.modify") fun b =>         [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") cost < b [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax")           b - cost         [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") b     orders := orders.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") o    -- Wait until all orders are completed   for o in orders do     match o.[get](IO/Tasks-and-Threads/#Task___get "Documentation for Task.get") with     | [.ok](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.ok") () => [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ()     | [.error](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.error") e => [throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") e    if (← balance.[get](IO/Mutable-References/#ST___Ref___get "Documentation for ST.Ref.get")) < 0 then     [IO.eprintln](IO/Console-Output/#IO___eprintln "Documentation for IO.eprintln") "Final balance negative!"   else     [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "Final balance is zero or positive." `
`stdout``Sending out orders...``Final balance is zero or positive.`
`stderr``<empty>`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ST.Ref.modifyGet "Permalink")def
```


ST.Ref.modifyGet {σ : Type} {m : Type → Type} [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") σ) m]
  {α β : Type} (r : [ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ α) (f : α → β [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") α) : m β


ST.Ref.modifyGet {σ : Type}
  {m : Type → Type} [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") σ) m]
  {α β : Type} (r : [ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ α)
  (f : α → β [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") α) : m β


```

Atomically modifies a mutable reference cell by replacing its contents with the result of a function call that simultaneously computes a value to return.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ST.Ref.swap "Permalink")def
```


ST.Ref.swap {σ : Type} {m : Type → Type} [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") σ) m]
  {α : Type} (r : [ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ α) (a : α) : m α


ST.Ref.swap {σ : Type} {m : Type → Type}
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") σ) m] {α : Type}
  (r : [ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ α) (a : α) : m α


```

Atomically swaps the value of a mutable reference cell with another value. The reference cell's original value is returned.
###  21.4.1.2. Comparisons[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Mutable-References--State-Transformers--Comparisons "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ST.Ref.ptrEq "Permalink")def
```


ST.Ref.ptrEq {σ : Type} {m : Type → Type} [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") σ) m]
  {α : Type} (r1 r2 : [ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ α) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


ST.Ref.ptrEq {σ : Type} {m : Type → Type}
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") σ) m] {α : Type}
  (r1 r2 : [ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ α) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether two reference cells are in fact aliases for the same cell.
Even if they contain the same value, two references allocated by different executions of `[IO.mkRef](IO/Mutable-References/#IO___mkRef "Documentation for IO.mkRef")` or `[ST.mkRef](IO/Mutable-References/#ST___mkRef "Documentation for ST.mkRef")` are distinct. Modifying one has no effect on the other. Likewise, a single reference cell may be aliased, and modifications to one alias also modify the other.
###  21.4.1.3. `ST`-Backed State Monads[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Mutable-References--State-Transformers--ST--Backed-State-Monads "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ST.Ref.toMonadStateOf "Permalink")def
```


ST.Ref.toMonadStateOf {σ : Type} {m : Type → Type} [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") σ) m]
  {α : Type} (r : [ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ α) : [MonadStateOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf") α m


ST.Ref.toMonadStateOf {σ : Type}
  {m : Type → Type} [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") σ) m]
  {α : Type} (r : [ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ α) :
  [MonadStateOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf") α m


```

Creates a `[MonadStateOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf")` instance from a reference cell.
This allows programs written against the [state monad](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=state-monads) API to be executed using a mutable reference cell to track the state.
##  21.4.2. Concurrency[🔗](find/?domain=Verso.Genre.Manual.section&name=ref-locks "Permalink")
Mutable references can be used as a locking mechanism. _Taking_ the contents of the reference causes attempts to take it or to read from it to block until it is `[set](IO/Mutable-References/#ST___Ref___set "Documentation for ST.Ref.set")` again. This is a low-level feature that can be used to implement other synchronization mechanisms; it's usually better to rely on higher-level abstractions when possible.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ST.Ref.take "Permalink")unsafe def
```


ST.Ref.take {σ : Type} {m : Type → Type} [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") σ) m]
  {α : Type} (r : [ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ α) : m α


ST.Ref.take {σ : Type} {m : Type → Type}
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") ([ST](IO/Mutable-References/#ST "Documentation for ST") σ) m] {α : Type}
  (r : [ST.Ref](IO/Mutable-References/#ST___Ref___mk "Documentation for ST.Ref") σ α) : m α


```

Reads the value of a mutable reference cell, removing it.
This causes subsequent attempts to read from or take the reference cell to block until a new value is written using `[ST.Ref.set](IO/Mutable-References/#ST___Ref___set "Documentation for ST.Ref.set")`.
Reference Cells as Locks
This program launches 100 threads. Each thread simulates a purchase attempt: it generates a random price, and if the account balance is sufficient, it decrements it by the price. If the balance is not sufficient, then it is not decremented. Because each thread `[take](IO/Mutable-References/#ST___Ref___take "Documentation for ST.Ref.take")`s the balance cell prior to checking it and only returns it when it is finished, the cell acts as a lock. Unlike using `[ST.Ref.modify](IO/Mutable-References/#ST___Ref___modify "Documentation for ST.Ref.modify")`, which atomically modifies the contents of the cell using a pure function, other `[IO](IO/Logical-Model/#IO "Documentation for IO")` actions may occur in the critical section This program's `main` function is marked ``Lean.Parser.Command.declaration : command```unsafe` because `[take](IO/Mutable-References/#ST___Ref___take "Documentation for ST.Ref.take")` itself is unsafe.
`unsafe def main : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let balance ← [IO.mkRef](IO/Mutable-References/#IO___mkRef "Documentation for IO.mkRef") (100 : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int"))   let validationUsed ← [IO.mkRef](IO/Mutable-References/#IO___mkRef "Documentation for IO.mkRef") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")    let mut orders := #[]    [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "Sending out orders..."   for _ in [0:100] do     let o ← [IO.asTask](IO/Tasks-and-Threads/#IO___asTask "Documentation for IO.asTask") (prio := [.dedicated](IO/Tasks-and-Threads/#Task___Priority___dedicated "Documentation for Task.Priority.dedicated")) [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")       let cost ← [IO.rand](IO/Random-Numbers/#IO___rand "Documentation for IO.rand") 1 100       [IO.sleep](IO/Timing/#IO___sleep "Documentation for IO.sleep") (← [IO.rand](IO/Random-Numbers/#IO___rand "Documentation for IO.rand") 10 100).[toUInt32](Basic-Types/Natural-Numbers/#Nat___toUInt32 "Documentation for Nat.toUInt32")       let b ← balance.[take](IO/Mutable-References/#ST___Ref___take "Documentation for ST.Ref.take")       if cost ≤ b then         balance.[set](IO/Mutable-References/#ST___Ref___set "Documentation for ST.Ref.set") (b - cost)       else         balance.[set](IO/Mutable-References/#ST___Ref___set "Documentation for ST.Ref.set") b         validationUsed.[set](IO/Mutable-References/#ST___Ref___set "Documentation for ST.Ref.set") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")     orders := orders.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") o    -- Wait until all orders are completed   for o in orders do     match o.[get](IO/Tasks-and-Threads/#Task___get "Documentation for Task.get") with     | [.ok](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.ok") () => [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ()     | [.error](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.error") e => [throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") e    if (← validationUsed.[get](IO/Mutable-References/#ST___Ref___get "Documentation for ST.Ref.get")) then     [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "Validation prevented a negative balance."    if (← balance.[get](IO/Mutable-References/#ST___Ref___get "Documentation for ST.Ref.get")) < 0 then     [IO.eprintln](IO/Console-Output/#IO___eprintln "Documentation for IO.eprintln") "Final balance negative!"   else     [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "Final balance is zero or positive." `
The program's output is:
`stdout``Sending out orders...``Validation prevented a negative balance.``Final balance is zero or positive.`
[←21.3. Console Output](IO/Console-Output/#The-Lean-Language-Reference--IO--Console-Output "21.3. Console Output")[21.5. Files, File Handles, and Streams→](IO/Files___-File-Handles___-and-Streams/#The-Lean-Language-Reference--IO--Files___-File-Handles___-and-Streams "21.5. Files, File Handles, and Streams")

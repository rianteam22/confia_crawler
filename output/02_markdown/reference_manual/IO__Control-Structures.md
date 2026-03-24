[←21.1. Logical Model](IO/Logical-Model/#The-Lean-Language-Reference--IO--Logical-Model "21.1. Logical Model")[21.3. Console Output→](IO/Console-Output/#The-Lean-Language-Reference--IO--Console-Output "21.3. Console Output")
#  21.2. Control Structures[🔗](find/?domain=Verso.Genre.Manual.section&name=io-monad-control "Permalink")
Normally, programs written in `[IO](IO/Logical-Model/#IO "Documentation for IO")` use [the same control structures as those written in other monads](Functors___-Monads-and--do--Notation/#monads-and-do). There is one specific `[IO](IO/Logical-Model/#IO "Documentation for IO")` helper.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.iterate "Permalink")opaque
```


IO.iterate {α β : Type} (a : α) (f : α → [IO](IO/Logical-Model/#IO "Documentation for IO") [(](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β[)](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")) : [IO](IO/Logical-Model/#IO "Documentation for IO") β


IO.iterate {α β : Type} (a : α)
  (f : α → [IO](IO/Logical-Model/#IO "Documentation for IO") [(](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")α [⊕](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") β[)](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum")) : [IO](IO/Logical-Model/#IO "Documentation for IO") β


```

Iterates an `[IO](IO/Logical-Model/#IO "Documentation for IO")` action. Starting with an initial state, the action is applied repeatedly until it returns a final value in `[Sum.inr](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inr")`. Each time it returns `[Sum.inl](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inl")`, the returned value is treated as a new state.
[←21.1. Logical Model](IO/Logical-Model/#The-Lean-Language-Reference--IO--Logical-Model "21.1. Logical Model")[21.3. Console Output→](IO/Console-Output/#The-Lean-Language-Reference--IO--Console-Output "21.3. Console Output")

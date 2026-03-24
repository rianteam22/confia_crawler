[←20.21. Lazy Computations](Basic-Types/Lazy-Computations/#Thunk "20.21. Lazy Computations")[21.1. Logical Model→](IO/Logical-Model/#The-Lean-Language-Reference--IO--Logical-Model "21.1. Logical Model")
#  21. IO[🔗](find/?domain=Verso.Genre.Manual.section&name=io "Permalink")
Lean is a pure functional programming language. While Lean code is strictly evaluated at run time, the order of evaluation that is used during type checking, especially while checking [definitional equality](The-Type-System/#--tech-term-definitional-equality), is formally unspecified and makes use of a number of heuristics that improve performance but are subject to change. This means that simply adding operations that perform side effects (such as file I/O, exceptions, or mutable references) would lead to programs in which the order of effects is unspecified. During type checking, even terms with free variables are reduced; this would make side effects even more difficult to predict. Finally, a basic principle of Lean's logic is that functions are _functions_ that map each element of the domain to a unique element of the range. Including side effects such as console I/O, arbitrary mutable state, or random number generation would violate this principle.
Programs that may have side effects have a type (typically `[IO](IO/Logical-Model/#IO "Documentation for IO") α`) that distinguishes them from pure functions. Logically speaking, `[IO](IO/Logical-Model/#IO "Documentation for IO")` describes the sequencing and data dependencies of side effects. Many of the basic side effects, such as reading from files, are opaque constants from the perspective of Lean's logic. Others are specified by code that is logically equivalent to the run-time version. At run time, the compiler produces ordinary code.
  1. [21.1. Logical Model](IO/Logical-Model/#The-Lean-Language-Reference--IO--Logical-Model)
  2. [21.2. Control Structures](IO/Control-Structures/#io-monad-control)
  3. [21.3. Console Output](IO/Console-Output/#The-Lean-Language-Reference--IO--Console-Output)
  4. [21.4. Mutable References](IO/Mutable-References/#The-Lean-Language-Reference--IO--Mutable-References)
  5. [21.5. Files, File Handles, and Streams](IO/Files___-File-Handles___-and-Streams/#The-Lean-Language-Reference--IO--Files___-File-Handles___-and-Streams)
  6. [21.6. System and Platform Information](IO/System-and-Platform-Information/#platform-info)
  7. [21.7. Environment Variables](IO/Environment-Variables/#io-monad-getenv)
  8. [21.8. Timing](IO/Timing/#io-timing)
  9. [21.9. Processes](IO/Processes/#io-processes)
  10. [21.10. Random Numbers](IO/Random-Numbers/#The-Lean-Language-Reference--IO--Random-Numbers)
  11. [21.11. Tasks and Threads](IO/Tasks-and-Threads/#concurrency)

[←20.21. Lazy Computations](Basic-Types/Lazy-Computations/#Thunk "20.21. Lazy Computations")[21.1. Logical Model→](IO/Logical-Model/#The-Lean-Language-Reference--IO--Logical-Model "21.1. Logical Model")

[1. Introduction→](Introduction/#introduction "1. Introduction")
#  The Lean Language Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=lean-language-reference "Permalink")
This is the _Lean Language Reference_. It is intended to be a comprehensive, precise description of Lean: a reference work in which Lean users can look up detailed information, rather than a tutorial intended for new users. For other documentation, please refer to the [Lean documentation overview](https://lean-lang.org/documentation/). This manual covers Lean version `4.29.0-rc6`.
Lean is an **interactive theorem prover** based on dependent type theory, designed for use both in cutting-edge mathematics and in software verification. Lean's core type theory is expressive enough to capture very complicated mathematical objects, but simple enough to admit independent implementations, reducing the risk of bugs that affect soundness. The core type theory is implemented in a minimal [kernel](Elaboration-and-Compilation/#--tech-term-kernel) that does nothing other than check proof terms. This core theory and kernel are supported by advanced automation, realized in [an expressive tactic language](Tactic-Proofs/#tactics). Each tactic produces a term in the core type theory that is checked by the kernel, so bugs in tactics do not threaten the soundness of Lean as a whole. Along with many other parts of Lean, the tactic language is user-extensible, so it can be built up to meet the needs of a given formalization project. Tactics are written in Lean itself, and can be used immediately upon definition; rebuilding the prover or loading external modules is not required.
Lean is also a pure **functional programming language** , with features such as a run-time system based on reference counting that can efficiently work with packed array structures, multi-threading, and monadic `[IO](IO/Logical-Model/#IO "Documentation for IO")`. As befits a programming language, Lean is primarily implemented in itself, including the language server, build tool, [elaborator](Elaboration-and-Compilation/#--tech-term-Elaboration), and tactic system. This very book is written in [Verso](https://github.com/leanprover/verso), a documentation authoring tool written in Lean.
Familiarity with Lean's programming features is valuable even for users whose primary interest is in writing proofs, because Lean programs are used to implement new tactics and proof automation. Thus, this reference manual does not draw a barrier between the two aspects, but rather describes them together so they can shed light on one another.
##  Contents
  1. [1. Introduction](Introduction/#introduction)
  2. [2. Elaboration and Compilation](Elaboration-and-Compilation/#The-Lean-Language-Reference--Elaboration-and-Compilation)
  3. [3. Interacting with Lean](Interacting-with-Lean/#interaction)
  4. [4. The Type System](The-Type-System/#type-system)
  5. [5. Source Files and Modules](Source-Files-and-Modules/#files)
  6. [6. Namespaces and Sections](Namespaces-and-Sections/#namespaces-sections)
  7. [7. Definitions](Definitions/#definitions)
  8. [8. Axioms](Axioms/#axioms)
  9. [9. Attributes](Attributes/#attributes)
  10. [10. Type Classes](Type-Classes/#type-classes)
  11. [11. Coercions](Coercions/#coercions)
  12. [12. Run-Time Code](Run-Time-Code/#runtime)
  13. [13. Terms](Terms/#terms)
  14. [14. Tactic Proofs](Tactic-Proofs/#tactics)
  15. [15. The Simplifier](The-Simplifier/#the-simplifier)
  16. [16. The `grind` tactic](The--grind--tactic/#grind-tactic)
  17. [17. The `mvcgen` tactic](The--mvcgen--tactic/#mvcgen-tactic)
  18. [18. Functors, Monads and `do`-Notation](Functors___-Monads-and--do--Notation/#monads-and-do)
  19. [19. Basic Propositions](Basic-Propositions/#basic-props)
  20. [20. Basic Types](Basic-Types/#basic-types)
  21. [21. IO](IO/#io)
  22. [22. Iterators](Iterators/#iterators)
  23. [23. Notations and Macros](Notations-and-Macros/#language-extension)
  24. [24. Build Tools and Distribution](Build-Tools-and-Distribution/#build-tools-and-distribution)
  25. [Validating a Lean Proof](ValidatingProofs/#validating-proofs)
  26. [Error Explanations](Error-Explanations/#The-Lean-Language-Reference--Error-Explanations)
  27. [Release Notes](releases/#release-notes)
  28. [Supported Platforms](platforms/#platforms)
  29. [Index](the-index/#The-Lean-Language-Reference--Index)


[1. Introduction→](Introduction/#introduction "1. Introduction")

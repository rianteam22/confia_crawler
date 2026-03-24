[←23.7. Extending Lean's Output](Notations-and-Macros/Extending-Lean___s-Output/#unexpand-and-delab "23.7. Extending Lean's Output")[24.1. Lake→](Build-Tools-and-Distribution/Lake/#lake "24.1. Lake")
#  24. Build Tools and Distribution[🔗](find/?domain=Verso.Genre.Manual.section&name=build-tools-and-distribution "Permalink")
The Lean _toolchain_ is the collection of command-line tools that are used to check proofs and compile programs in collections of Lean files. Toolchains are managed by `elan`, which installs toolchains as needed. Lean toolchains are designed to be self-contained, and most command-line users will never need to explicitly invoke any other than `lake` and `elan`. They contain the following tools: 

`lean` 
    
The Lean compiler, used to elaborate and compile a Lean source file. 

`lake` 
    
The Lean build tool, used to incrementally invoke `lean` and other tools while tracking dependencies. 

`leanc` 
    
The C compiler that ships with Lean, which is a version of [Clang](https://clang.llvm.org/). 

`leanmake` 
    
An implementation of the `make` build tool, used for compiling C dependencies. 

`leanchecker` 
    
A tool that replays elaboration results from [`.olean` files](Elaboration-and-Compilation/#--tech-term-___olean-file) through the Lean kernel, providing additional assurance that all terms were properly checked.
In addition to these build tools, toolchains contain files that are needed to build Lean code. This includes source code, [`.olean` files](Elaboration-and-Compilation/#--tech-term-___olean-file), compiled libraries, C header files, and the compiled Lean run-time system. They also include external proof automation tools that are used by tactics included with Lean, such as `cadical` for `[bv_decide](Tactic-Proofs/Tactic-Reference/#bv_decide "Documentation for tactic")`.
  1. [24.1. Lake](Build-Tools-and-Distribution/Lake/#lake)
  2. [24.2. Managing Toolchains with Elan](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#elan)

[←23.7. Extending Lean's Output](Notations-and-Macros/Extending-Lean___s-Output/#unexpand-and-delab "23.7. Extending Lean's Output")[24.1. Lake→](Build-Tools-and-Distribution/Lake/#lake "24.1. Lake")

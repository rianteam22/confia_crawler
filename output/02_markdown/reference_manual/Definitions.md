[←6. Namespaces and Sections](Namespaces-and-Sections/#namespaces-sections "6. Namespaces and Sections")[7.1. Modifiers→](Definitions/Modifiers/#declaration-modifiers "7.1. Modifiers")
#  7. Definitions[🔗](find/?domain=Verso.Genre.Manual.section&name=definitions "Permalink")
The following commands in Lean are definition-like: 
  * `def`
  * `abbrev`
  * `example`
  * `theorem`
  * `opaque`


All of these commands cause Lean to [elaborate](Notations-and-Macros/Elaborators/#--tech-term-elaborators) a term based on a [signature](Definitions/Headers-and-Signatures/#--tech-term-signature). With the exception of ``Lean.Parser.Command.example```example`, which discards the result, the resulting expression in Lean's core language is saved for future use in the environment. The ``Lean.Parser.Command.declaration : command```instance` command is described in the [section on instance declarations](Type-Classes/Instance-Declarations/#instance-declarations).
  1. [7.1. Modifiers](Definitions/Modifiers/#declaration-modifiers)
  2. [7.2. Headers and Signatures](Definitions/Headers-and-Signatures/#signature-syntax)
  3. [7.3. Definitions](Definitions/Definitions/#The-Lean-Language-Reference--Definitions--Definitions)
  4. [7.4. Theorems](Definitions/Theorems/#The-Lean-Language-Reference--Definitions--Theorems)
  5. [7.5. Example Declarations](Definitions/Example-Declarations/#The-Lean-Language-Reference--Definitions--Example-Declarations)
  6. [7.6. Recursive Definitions](Definitions/Recursive-Definitions/#recursive-definitions)

[←6. Namespaces and Sections](Namespaces-and-Sections/#namespaces-sections "6. Namespaces and Sections")[7.1. Modifiers→](Definitions/Modifiers/#declaration-modifiers "7.1. Modifiers")

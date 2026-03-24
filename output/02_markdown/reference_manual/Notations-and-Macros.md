[←22.5. Reasoning About Iterators](Iterators/Reasoning-About-Iterators/#The-Lean-Language-Reference--Iterators--Reasoning-About-Iterators "22.5. Reasoning About Iterators")[23.1. Custom Operators→](Notations-and-Macros/Custom-Operators/#operators "23.1. Custom Operators")
#  23. Notations and Macros[🔗](find/?domain=Verso.Genre.Manual.section&name=language-extension "Permalink")
Different mathematical fields have their own notational conventions, and many notations are reused with differing meanings in different fields. It is important that formal developments are able to use established notations: formalizing mathematics is already difficult, and the mental overhead of translating between syntaxes can be substantial. At the same time, it's important to be able to control the scope of notational extensions. Many fields use related notations with very different meanings, and it should be possible to combine developments from these separate fields in a way where both readers and the system know which convention is in force in any given region of a file.
Lean addresses the problem of notational extensibility with a variety of mechanisms, each of which solves a different aspect of the problem. They can be combined flexibly to achieve the necessary results:
  * The [_extensible parser_](Elaboration-and-Compilation/#parser) allows a great variety of notational conventions to be implemented declaratively, and combined flexibly.
  * [Macros](Elaboration-and-Compilation/#macro-and-elab) allow new syntax to be easily mapped to existing syntax, which is a simple way to provide meaning to new constructs. Due to [hygiene](Notations-and-Macros/Macros/#--tech-term-hygienic) and automatic propagation of source positions, this process doesn't interfere with Lean's interactive features.
  * [Elaborators](Elaboration-and-Compilation/#macro-and-elab) provide new syntax with the same tools available to Lean's own syntax in cases where a macro is insufficiently expressive.
  * [Notations](Notations-and-Macros/Notations/#notations) allow the simultaneous definition of a parser extension, a macro, and a pretty printer. When defining infix, prefix, or postfix operators, [custom operators](Notations-and-Macros/Custom-Operators/#operators) automatically take care of precedence and associativity.
  * Low-level parser extensions allow the parser to be extended in ways that modify its rules for tokens and whitespace, or that even completely replace Lean's syntax. This is an advanced topic that requires familiarity with Lean internals; nevertheless, the possibility of doing this without modifying the compiler is important. This reference manual is written using a language extension that replaces Lean's concrete syntax with a Markdown-like language for writing documents, but the source files are still Lean files.


  1. [23.1. Custom Operators](Notations-and-Macros/Custom-Operators/#operators)
  2. [23.2. Precedence](Notations-and-Macros/Precedence/#precedence)
  3. [23.3. Notations](Notations-and-Macros/Notations/#notations)
  4. [23.4. Defining New Syntax](Notations-and-Macros/Defining-New-Syntax/#syntax-ext)
  5. [23.5. Macros](Notations-and-Macros/Macros/#macros)
  6. [23.6. Elaborators](Notations-and-Macros/Elaborators/#elaborators)
  7. [23.7. Extending Lean's Output](Notations-and-Macros/Extending-Lean___s-Output/#unexpand-and-delab)

[←22.5. Reasoning About Iterators](Iterators/Reasoning-About-Iterators/#The-Lean-Language-Reference--Iterators--Reasoning-About-Iterators "22.5. Reasoning About Iterators")[23.1. Custom Operators→](Notations-and-Macros/Custom-Operators/#operators "23.1. Custom Operators")

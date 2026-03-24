[← The Lean Language Reference](./../ " The Lean Language Reference")[2. Elaboration and Compilation→](Elaboration-and-Compilation/#The-Lean-Language-Reference--Elaboration-and-Compilation "2. Elaboration and Compilation")
#  1. Introduction[🔗](find/?domain=Verso.Genre.Manual.section&name=introduction "Permalink")
The _Lean Language Reference_ is intended as a comprehensive, precise description of Lean. It is a reference work in which Lean users can look up detailed information, rather than a tutorial for new users. At the moment, this reference manual is a public preview. For tutorials and learning materials, please visit [the Lean documentation page](https://lean-lang.org/documentation/).
This document describes version `4.29.0-rc6` of Lean.
##  1.1. History[🔗](find/?domain=Verso.Genre.Manual.section&name=history-of-lean "Permalink")
Leonardo de Moura launched the Lean project when he was at Microsoft Research in 2013, and Lean 0.1 was officially released on June 16, 2014. The goal of the Lean project is to combine the high level of trust provided by a small, independently-implementable logical kernel with the convenience and automation of tools like SMT solvers, while scaling to large problems. This vision still guides the development of Lean, as we invest in improved automation, improved performance, and user-friendliness; the trusted core proof checker is still minimal and independent implementations exist.
The initial versions of Lean were primarily configured as C++ libraries in which client code could carry out trustworthy proofs that were independently checkable. In these early years, the design of Lean rapidly evolved towards traditional interactive provers, first with tactics written in Lua, and later with a dedicated front-end syntax. January 20, 2017 saw the first release of the Lean 3.0 series. Lean 3 achieved widespread adoption by mathematicians, and pioneered self-extensibility: tactics, notations, and top-level commands could all be defined in Lean itself. The mathematics community built Mathlib, which at the end of Lean 3 had over one million lines of formalized mathematics, with all proofs mechanically checked. The system itself, however, was still implemented in C++, which imposed limits on Lean's flexibility and made it more difficult to develop due to the diverse skills required.
Development of Lean 4 began in 2018, culminating in the 4.0 release on September 8, 2023. Lean 4 represents an important milestone: as of version 4, Lean is self-hosted—approximately 90% of the code that implements Lean is itself written in Lean. Lean 4's rich extension API provides users with the ability to adapt it to their needs, rather than relying on the core developers to add necessary features. Additionally, self-hosting makes the development process much faster, so features and performance can be delivered more quickly; Lean 4 is faster and scales to larger problems than Lean 3. Mathlib was successfully ported to Lean 4 in 2023 through a community effort supported by the Lean developers, and it has now grown to over 1.5 million lines. Even though Mathlib has grown by 50%, Lean 4 checks it faster than Lean 3 could check its smaller library. The development process for Lean 4 was approximately as long as that of all prior versions combined, and we are now delighted with its design—no further rewrites are planned.
Leonardo de Moura and his co-founder, Sebastian Ullrich, launched the Lean Focused Research Organization (FRO) nonprofit in July of 2023 within Convergent Research, with philanthropic support from the Simons Foundation International, the Alfred P. Sloan Foundation, and Richard Merkin. The FRO currently has more than ten employees working to support the growth and scalability of Lean and the broader Lean community.
##  1.2. Typographical Conventions[🔗](find/?domain=Verso.Genre.Manual.section&name=typographical-conventions "Permalink")
This document makes use of a number of typographical and layout conventions to indicate various aspects of the information being presented.
###  1.2.1. Lean Code[🔗](find/?domain=Verso.Genre.Manual.section&name=code-samples "Permalink")
This document contains many Lean code examples. They are formatted as follows:
`def hello : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "Hello, world!" `
Compiler output (which may be errors, warnings, or just information) is shown both in the code and separately:
``"The answer is 4"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") s!"The answer is {2 + 2}" theorem `declaration uses `sorry``bogus : [False](Basic-Propositions/Truth/#False "Documentation for False") := by⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [sorry](Tactic-Proofs/Tactic-Reference/#sorry "Documentation for tactic")All goals completed! 🐙 example := [Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") `Application type mismatch: The argument   "two" has type   [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") but is expected to have type   [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") in the application   [Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") "two"`"two" `
Informative output, such as the result of ``Lean.Parser.Command.eval : command`
`#eval e` evaluates the expression `e` by compiling and evaluating it.
  * The command attempts to use `ToExpr`, `Repr`, or `ToString` instances to print the result.
  * If `e` is a monadic value of type `m ty`, then the command tries to adapt the monad `m` to one of the monads that `#eval` supports, which include `IO`, `CoreM`, `MetaM`, `TermElabM`, and `CommandElabM`. Users can define `MonadEval` instances to extend the list of supported monads.


The `#eval` command gracefully degrades in capability depending on what is imported. Importing the `Lean.Elab.Command` module provides full capabilities.
Due to unsoundness, `#eval` refuses to evaluate expressions that depend on `sorry`, even indirectly, since the presence of `sorry` can lead to runtime instability and crashes. This check can be overridden with the `#eval! e` command.
Options:
  * If `eval.pp` is true (default: true) then tries to use `ToExpr` instances to make use of the usual pretty printer. Otherwise, only tries using `Repr` and `ToString` instances.
  * If `eval.type` is true (default: false) then pretty prints the type of the evaluated value.
  * If `eval.derive.repr` is true (default: true) then attempts to auto-derive a `Repr` instance when there is no other way to print the result.


See also: `#reduce e` for evaluation by term reduction.
`[`#eval`](Interacting-with-Lean/#Lean___Parser___Command___eval), is shown like this:

```
"The answer is 4"
```

Warnings are shown like this:

```
declaration uses `sorry`
```

Error messages are shown like this:

```
Application type mismatch: The argument
  "two"
has type
  [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
but is expected to have type
  [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
in the application
  [Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") "two"
```

The presence of tactic proof states is indicated by the presence of small lozenges that can be clicked to show the proof state, such as after `[rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")` below:
`example : 2 + 2 = 4 := by⊢ 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 4 [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 `
Proof states may also be shown on their own. When attempting to prove that `2 + 2 = 4`, the initial proof state is:
⊢ 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 4
After using `[rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙`, the resulting state is:
All goals completed! 🐙
Identifiers in code examples are hyperlinked to their documentation.
Examples of code with syntax errors are shown with an indicator of where the parser error occurred, along with the error message:

```
def f : Option Nat → Type  | some 0 => Unit  |unexpected token '=>'; expected term => Option (f t)  | none => Empty
```

```
<example>:3:3-3:6: unexpected token '=>'; expected term
```

###  1.2.2. Examples[🔗](find/?domain=Verso.Genre.Manual.section&name=example-boxes "Permalink")
Illustrative examples are in callout boxes, as below:
Even Numbers
This is an example of an example.
One way to define even numbers is via an inductive predicate:
`inductive Even : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Prop where   | zero : [Even](Introduction/#Even___zero-next "Documentation for Even") 0   | plusTwo : [Even](Introduction/#Even___zero-next "Documentation for Even") n → [Even](Introduction/#Even___zero-next "Documentation for Even") (n + 2) `
[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABAUSSZAuZA5AhjMoEmEyACgE4D2ADsgO4AWiFiAUMsgD7IBeLVbGgzIADB27IaAGwgBnACr1BOdIkyZSazAApMAamQAmAJRA"\))
###  1.2.3. Technical Terminology[🔗](find/?domain=Verso.Genre.Manual.section&name=technical-terms "Permalink")
_Technical terminology_ refers to terms used in a very specific sense when writing technical material, such as this reference. Uses of [technical terminology](Introduction/#--tech-term-Technical-terminology) are frequently hyperlinked to their definition sites, using links like this one.
###  1.2.4. Constant, Syntax, and Tactic References[🔗](find/?domain=Verso.Genre.Manual.section&name=reference-boxes "Permalink")
Definitions, inductive types, syntax formers, and tactics have specific descriptions. These descriptions are marked as follows:
`/-- Evenness: a number is even if it can be evenly divided by two. -/ inductive Even : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Prop where   | /-- 0 is considered even here -/     zero : [Even](Introduction/#Even___zero-next "Documentation for Even") 0   | /-- If `n` is even, then so is `n + 2`. -/     plusTwo : [Even](Introduction/#Even___zero-next "Documentation for Even") n → [Even](Introduction/#Even___zero-next "Documentation for Even") (n + 2) `
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Even.zero "Permalink")inductive predicate
```


Even : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Prop


Even : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Prop


```

Evenness: a number is even if it can be evenly divided by two.
#  Constructors

```
zero : [Even](Introduction/#Even___zero-next "Documentation for Even") 0
```

0 is considered even here

```
plusTwo {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} : [Even](Introduction/#Even___zero-next "Documentation for Even") n → [Even](Introduction/#Even___zero-next "Documentation for Even") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")
```

If `n` is even, then so is `n + 2`.
##  1.3. How to Cite This Work[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Introduction--How-to-Cite-This-Work "Permalink")
In formal citations, please cite this work as _The Lean Language Reference_ by The Lean Developers. Additionally, please include the corresponding version of Lean in the citation, which is `4.29.0-rc6`.
##  Open-Source Licenses[🔗](find/?domain=Verso.Genre.Manual.section&name=dependency-licenses "Permalink")
###  Editable Combobox With Both List and Inline Autocomplete Example, from the W3C's ARIA Authoring Practices Guide (APG)
<https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/combobox-autocomplete-both/>
The search box component includes code derived from the example code in the linked article from the W3C's ARIA Authoring Practices Guide (APG).
`W3C-20150513`
####  Software and Document License - 2023 Version
Permission to copy, modify, and distribute this work, with or without modification, for any purpose and without fee or royalty is hereby granted, provided that you include the following on ALL copies of the work or portions thereof, including modifications:
* The full text of this NOTICE in a location viewable to users of the redistributed or derivative work.
* Any pre-existing intellectual property disclaimers, notices, or terms and conditions. If none exist, the W3C software and document short notice should be included.
* Notice of any changes or modifications, through a copyright statement on the new code or document such as "This software or document includes material copied from or derived from "Editable Combobox With Both List and Inline Autocomplete Example" at https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/combobox-autocomplete-both/. Copyright © 2024 World Wide Web Consortium. https://www.w3.org/copyright/software-license-2023/"
###  elasticlunr.js
<http://elasticlunr.com/>
Elasticlunr.js is used for full-text search
`MIT`
####  The MIT License
Copyright (C) 2017 by Wei Song
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
###  fuzzysort v3.1.0
<https://github.com/farzher/fuzzysort>
The fuzzysort library is used in the search box to quickly filter results.
`MIT`
####  The MIT License
Copyright (c) 2018 Stephen Kamenar
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
###  KaTeX
<https://katex.org/>
KaTeX is used to render mathematical notation.
`MIT`
####  The MIT License
Copyright (c) 2013-2020 Khan Academy and other contributors
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
###  Popper.js
<https://popper.js.org/docs/v2/>
Popper.js is used (as a dependency of Tippy.js) to show information (primarily in Lean code) when hovering the mouse over an item of interest.
`MIT`
####  The MIT License
Copyright (c) 2019 Federico Zivolo
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
###  Tippy.js
<https://atomiks.github.io/tippyjs/>
Tippy.js is used together with Popper.js to show information (primarily in Lean code) when hovering the mouse over an item of interest.
`MIT`
####  The MIT License
Copyright (c) 2017-present atomiks
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
[← The Lean Language Reference](./../ " The Lean Language Reference")[2. Elaboration and Compilation→](Elaboration-and-Compilation/#The-Lean-Language-Reference--Elaboration-and-Compilation "2. Elaboration and Compilation")

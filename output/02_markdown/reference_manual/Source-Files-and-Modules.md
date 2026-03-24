[←4.5. Quotients](The-Type-System/Quotients/#quotients "4.5. Quotients")[6. Namespaces and Sections→](Namespaces-and-Sections/#namespaces-sections "6. Namespaces and Sections")
#  5. Source Files and Modules[🔗](find/?domain=Verso.Genre.Manual.section&name=files "Permalink")
The smallest unit of compilation in Lean is a single [source file](Source-Files-and-Modules/#--tech-term-source-files). Source files may import other source files based on their file names. In other words, the names and folder structures of files are significant in Lean code.
Each source file has an _import name_ that is derived from a combination of its filename and the way in which Lean was invoked: Lean has a set of _root directories_ in which it expects to find code, and the source file's import name is the names of the directories from the root to the filename, with dots (`.`) interspersed and `.lean` removed. For example, if Lean is invoked with `Projects/MyLib/src` as its root, the file `Projects/MyLib/src/Literature/Novel/SciFi.lean` could be imported as `Literature.Novel.SciFi`.
##  5.1. Encoding and Representation[🔗](find/?domain=Verso.Genre.Manual.section&name=module-encoding "Permalink")
Lean source files are Unicode text files encoded in UTF-8. Lines may end either with newline characters (`"\n"`, Unicode `'LINE FEED (LF)' (U+000A)`) or with a form feed and newline sequence (`"\r\n"`, Unicode `'CARRIAGE RETURN (CR)' (U+000D)` followed by `'LINE FEED (LF)' (U+000A)`). However, Lean normalizes line endings when parsing or comparing files, so all files are compared as if all their line endings are `"\n"`.
##  5.2. Concrete Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=module-syntax "Permalink")
Lean's concrete syntax is [extensible](Notations-and-Macros/#language-extension). In a language like Lean, it's not possible to completely describe the syntax once and for all, because libraries may define syntax in addition to new constants or [inductive types](The-Type-System/Inductive-Types/#--tech-term-Inductive-types). Rather than completely describing the language here, the overall framework is described, while the syntax of each language construct is documented in the section to which it belongs.
###  5.2.1. Whitespace[🔗](find/?domain=Verso.Genre.Manual.section&name=whitespace "Permalink")
Tokens in Lean may be separated by any number of _whitespace_ character sequences. Whitespace may be a space (`" "`, Unicode `'SPACE (SP)' (U+0020)`), a valid newline sequence, or a comment. Neither tab characters nor carriage returns not followed by newlines are valid whitespace sequences.
###  5.2.2. Comments[🔗](find/?domain=Verso.Genre.Manual.section&name=comments "Permalink")
Comments are stretches of the file that, despite not being whitespace, are treated as such. Lean has two syntaxes for comments: 

Line comments
    
A `--` that does not occur as part of a token begins a _line comment_. All characters from the initial `-` to the newline are treated as whitespace. 

Block comments
    
A `/-` that does not occur as part of a token and is not immediately followed by a `-` character begins a _block comment_. The block comment continues until a terminating `-/` is found. Block comments may be nested; a `-/` only terminates the comment if prior nested block comment openers `/-` have been terminated by a matching `-/`.
`/--` and `/-!` begin _documentation_ rather than comments, which are also terminated with `-/` and may contain nested block comments. Even though documentation resembles comments, they are their own syntactic category; their valid placement is determined by Lean's grammar.
###  5.2.3. Keywords and Identifiers[🔗](find/?domain=Verso.Genre.Manual.section&name=keywords-and-identifiers "Permalink")
An [identifier](Notations-and-Macros/Defining-New-Syntax/#--tech-term-Identifiers) consists of one or more identifier components, separated by `'.'`.
Identifier components consist of a letter or letter-like character or an underscore (`'_'`), followed by zero or more identifier continuation characters. Letters are English letters, upper- or lowercase, and the letter-like characters include a range of non-English alphabetic scripts, including the Greek script which is widely used in Lean, the Coptic script, the members of the Unicode letter-like symbol block, which contains a number of double-struck characters (including `ℕ` and `ℤ`) and abbreviations, the Latin-1 supplemental letters (with the exception of `×` and `÷`), and the Latin Extended-A block. Identifier continuation characters consist of letters, letter-like characters, underscores (`'_'`), exclamation marks (`!`), question marks (`?`), subscripts, and single quotes (`'`). As an exception, underscore alone is not a valid identifier.
Identifiers components may also be surrounded by double guillemets (`'«'` and `'»'`). Such identifier components may contain any character at all aside from `'»'`, even `'«'`, `'.'`, and newlines. The guillemets are not part of the resulting identifier component, so `«x»` and `x` denote the same identifier. `«Nat.add»`, on the other hand, is an identifier with a single component, while `Nat.add` has two.
Some potential identifier components may be reserved keywords. The specific set of reserved keywords depends on the set of active syntax extensions, which may depend on the set of imported files and the currently-opened namespaces; it is impossible to enumerate for Lean as a whole. These keywords must also be quoted with guillemets to be used as identifier components in most syntactic contexts. Contexts in which keywords may be used as identifiers without guillemets, such as constructor names in inductive types, are _raw identifier_ contexts.
Identifiers that contain one or more `'.'` characters, and thus consist of more than one identifier component, are called hierarchical identifiers. Hierarchical identifiers are used to represent both import names and names in a namespace.
##  5.3. Structure[🔗](find/?domain=Verso.Genre.Manual.section&name=module-structure "Permalink")
syntaxModules

```
[
Parser for a Lean module. We never actually run this parser but instead use the imperative definitions below that
return the same syntax tree structure, but add error recovery. Still, it is helpful to have a Parser definition
for it in order to auto-generate helpers such as the pretty printer. 
module](Source-Files-and-Modules/#Lean___Parser___Module___module-next) ::=
    


Parser for a Lean module. We never actually run this parser but instead use the imperative definitions below that
return the same syntax tree structure, but add error recovery. Still, it is helpful to have a Parser definition
for it in order to auto-generate helpers such as the pretty printer. 


header command*
```

A source file consists of a _file header_ followed by a sequence of _commands_.
If a source file's header begins with ``Lean.Parser.Module.header```module`, then it is referred to as a [_module_](Source-Files-and-Modules/#--tech-term-module). Modules provide greater control over what information is exposed to clients. Modules are an experimental feature in Lean. To use modules, the `[experimental.module](Source-Files-and-Modules/#experimental___module "Documentation for option experimental.module")` must be set to `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` in the project's Lake configuration file.
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=experimental.module "Permalink")option
```
experimental.module
```

Default value: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
no-op, deprecated
###  5.3.1. Headers[🔗](find/?domain=Verso.Genre.Manual.section&name=module-headers "Permalink")
Module headers list the modules that should be elaborated prior to the current module. Their declarations are visible in the current module.
syntaxModule Headers
The module header consists of an optional ``Lean.Parser.Module.header```module` keyword followed by a sequence of `import` statements:

```
header ::=
    module?
    import*
```

The optional `prelude` keyword should only be used in Lean's source code:

```
header ::= ...
    | module?
      [prelude](Source-Files-and-Modules/#Lean___Parser___Module___prelude-next)
      import*
```

If present, the `prelude` keyword indicates that the file is part of the implementation of the Lean _prelude_ , which is the code that is available without any explicit imports—it should not be used outside of Lean's implementation.
syntaxPrelude Modules

```
[prelude](Source-Files-and-Modules/#Lean___Parser___Module___prelude-next) ::=
    prelude
```

syntaxImports
All [source files](Source-Files-and-Modules/#--tech-term-source-files) may use plain imports:

```
import ::= ...
    | import ident
```

In source files that are not modules, this imports the specified Lean file. Importing a file makes its contents available in the current source file, as well as those from source files transitively imported by its imports.
Source file names do not necessarily correspond to namespaces. Source files may add names to any namespace, and importing a source file has no effect on the set of currently open namespaces.
The [import name](Source-Files-and-Modules/#--tech-term-import-name) is translated to a filename by replacing dots (`'.'`) in its name with directory separators and appending `.lean` or `.olean`. Lean searches its include path for the corresponding intermediate build product or importable module file.
[Modules](Source-Files-and-Modules/#--tech-term-module) may use the following import syntax:

```
import ::= ...
    | public? meta? import all? ident
```

All imports to a module must themselves be modules. Without modifiers, the imported module's public scope is added to the current module's private scope. The imported module is not made available to modules that import the current module. The modifiers have the following meanings: 

`public` 
    
The imported module's public scope is added to the current module's public scope and made available to the current module's importers. 

`meta` 
    
The contents of the imported module are made available at the [meta phase](Source-Files-and-Modules/#--tech-term-meta-phase) in the current module. 

`all` 
    
The imported module's private scope is added to the current module's [private scope](Source-Files-and-Modules/#--tech-term-private-scope).
###  5.3.2. Commands[🔗](find/?domain=Verso.Genre.Manual.section&name=commands "Permalink")
[Commands](Source-Files-and-Modules/#--tech-term-commands) are top-level statements in Lean. Some examples are inductive type declarations, theorems, function definitions, namespace modifiers like `open` or `variable`, and interactive queries such as `#check`. The syntax of commands is user-extensible, and commands may even [add new syntax that is used to parse subsequent commands](Notations-and-Macros/#language-extension). Specific Lean commands are documented in the corresponding chapters of this manual, rather than being listed here.
##  5.4. Modules and Visibility[🔗](find/?domain=Verso.Genre.Manual.section&name=module-scopes "Permalink")
A module is a source file that has opted in to a distinction between public and private information. Lean ensures that private information can change without affecting clients that import only its public information. This discipline brings a number of benefits: 

Much-improved average build times
    
Changes to files that affect only non-exported information (e.g. proofs, comments, and docstrings) will not trigger rebuilds outside of these files. Even when dependent files have to be rebuilt, those files that cannot be affected (as determined by their ``Lean.Parser.Module.import```import` annotations) can be skipped. 

Control over API evolution
    
Library authors can trust that changes to non-exported information will not affect downstream users of their library. If only a function's signature is exposed, then downstream users cannot rely on definitional equalities that involve its unfolding; this means that the library's author is free to adopt a more efficient algorithm without unintentionally breaking client code. 

Avoiding accidental unfolding
    
Limiting the scope in which definitions can be unfolded allows for avoiding both reductions that should be replaced by application of more specific theorems as well as unproductive reductions that were not in fact necessary. This improves the speed of proof elaboration. 

Smaller executables
    
Separating compile-time and run-time code allows for more aggressive dead code elimination, guaranteeing that metaprograms such as tactics do not make it into the final binary. 

Reduced memory usage
    
Excluding private information such as proofs from importing can improve Lean's memory use both while building and editing a project. Porting mathlib4 to the module system has shown savings close to 50% from this even before imports are further minimized.
Modules contain two separate scopes: the _public scope_ consists of information that is visible in modules that import a module, while the _private scope_ consists of information that is generally visible only within the module. Some examples of information that can be private or public include: 

Names
    
Constants (such as definitions, inductive types, or constructors) may be private or public. A public constant's type may only refer to public names. 

Definitions
    
A public definition may be exposed or not. If a public definition is not exposed, then it cannot be unfolded in contexts that only have access to the public scope. Instead, clients must rely on the theorems about the definition that are provided in the public scope.
Each declaration has default visibility rules. Generally speaking, all names are private by default, unless defined in a [public section](Namespaces-and-Sections/#--tech-term-public-section). Even public names usually place the bodies of definitions in the private scope, and even proofs in exposed definitions are kept private. The specific visibility rules for each declaration command are documented together with the declaration itself.
Private and Public Definitions
The module `Greet.Create` defines a function `greeting`. Because there are no visibility modifiers, this function defaults to the [private scope](Source-Files-and-Modules/#--tech-term-private-scope):
`Greet/Create.lean``module def greeting (name : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=   s!"Hello, {name}" `
The definition of `greeting` is not visible in the module `Greet`, even though it imports `Greet.Create`:
`Greet.lean``module import Greet.Create def greetTwice (name1 name2 : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=   `Unknown identifier `greeting``greeting name1 ++ "\n" ++ `Unknown identifier `greeting``greeting name2 `

```
Unknown identifier `greeting`
```

If `greeting` is made public, then `greetTwice` can refer to it:
`Greet/Create.lean``module public def greeting (name : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=   s!"Hello, {name}" `
`Greet.lean``module import Greet.Create def greetTwice (name1 name2 : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=   [greeting](Source-Files-and-Modules/#greeting-_LPAR_in-Private-and-Public-Definitions_RPAR_ "Definition of example") name1 ++ "\n" ++ [greeting](Source-Files-and-Modules/#greeting-_LPAR_in-Private-and-Public-Definitions_RPAR_ "Definition of example") name2 `
Exposed and Unexposed Definitions
The module `Greet.Create` defines a public function `greeting`.
`Greet/Create.lean``module public def greeting (name : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=   s!"Hello, {name}" `
Although the definition of `greeting` is visible in the module `Greet`, it cannot be unfolded in a proof because the definition's body is in the [private scope](Source-Files-and-Modules/#--tech-term-private-scope) of `Greet`:
`Greet.lean``module import Greet.Create def greetTwice (name1 name2 : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=   greeting name1 ++ "\n" ++ greeting name2  theorem greetTwice_is_greet_twice {name1 name2 : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} :     greetTwice name1 name2 = "Hello, " ++ name1 ++ "\n" ++ "Hello, " ++ name2 := `unsolved goals name1 name2:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")⊢ greeting name1 [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") "\n" [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") greeting name2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") "Hello, " [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") name1 [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") "\n" [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") "Hello, " [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") name2`byname1:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")name2:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")⊢ greetTwice name1 name2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") "Hello, " [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") name1 [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") "\n" [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") "Hello, " [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") name2 [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [greetTwice, `Invalid simp theorem `greeting`: Expected a definition with an exposed body`greeting]name1:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")name2:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")⊢ greeting name1 [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") "\n" [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") greeting name2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") "Hello, " [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") name1 [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") "\n" [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") "Hello, " [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") name2 `

```
Invalid simp theorem `greeting`: Expected a definition with an exposed body
```

Adding the `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")expose[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")` attribute exposes the definition so that downstream modules can unfold `greeting`:
`Greet/Create.lean``module @[expose] public def greeting (name : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=   s!"Hello, {name}" `
Now, the proof can proceed:
`Greet.lean``module import Greet.Create def greetTwice (name1 name2 : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=   greeting name1 ++ "\n" ++ greeting name2  theorem greetTwice_is_greet_twice {name1 name2 : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} :     greetTwice name1 name2 = "Hello, " ++ name1 ++ "\n" ++ "Hello, " ++ name2 := byname1:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")name2:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")⊢ greetTwice name1 name2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") "Hello, " [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") name1 [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") "\n" [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") "Hello, " [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") name2   [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [greetTwice, greeting, toString]name1:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")name2:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")⊢ "Hello, " [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") name1 [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") "\n" [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") [(](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend")"Hello, " [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") name2[)](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") "Hello, " [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") name1 [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") "\n" [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") "Hello, " [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") name2   [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic") [String.append_assoc]All goals completed! 🐙 `
Proofs are Private
In this module, the function `incr` is public, but its implementation is not exposed:
`Main.lean``module  public def incr : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   | 0 => 1   | n + 1 => [incr](Source-Files-and-Modules/#incr-_LPAR_in-Proofs-are-Private_RPAR_ "Definition of example") n + 1  public theorem incr_eq_plus1 : [incr](Source-Files-and-Modules/#incr-_LPAR_in-Proofs-are-Private_RPAR_ "Definition of example") = (· + 1) := by⊢ [incr](Source-Files-and-Modules/#incr-_LPAR_in-Proofs-are-Private_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") fun x => x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1   [funext](Tactic-Proofs/Tactic-Reference/#funext-next "Documentation for tactic") nhn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [incr](Source-Files-and-Modules/#incr-_LPAR_in-Proofs-are-Private_RPAR_ "Definition of example") n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1   [induction](Tactic-Proofs/Tactic-Reference/#induction "Documentation for tactic") nh.zero⊢ [incr](Source-Files-and-Modules/#incr-_LPAR_in-Proofs-are-Private_RPAR_ "Definition of example") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1h.succn✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:[incr](Source-Files-and-Modules/#incr-_LPAR_in-Proofs-are-Private_RPAR_ "Definition of example") n✝ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1⊢ [incr](Source-Files-and-Modules/#incr-_LPAR_in-Proofs-are-Private_RPAR_ "Definition of example") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 <;>h.zero⊢ [incr](Source-Files-and-Modules/#incr-_LPAR_in-Proofs-are-Private_RPAR_ "Definition of example") 0 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1h.succn✝:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")a✝:[incr](Source-Files-and-Modules/#incr-_LPAR_in-Proofs-are-Private_RPAR_ "Definition of example") n✝ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1⊢ [incr](Source-Files-and-Modules/#incr-_LPAR_in-Proofs-are-Private_RPAR_ "Definition of example") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") n✝ [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [[incr](Source-Files-and-Modules/#incr-_LPAR_in-Proofs-are-Private_RPAR_ "Definition of example"), *]All goals completed! 🐙 `
Nonetheless, the proof of the theorem `incr_eq_plus1` can unfold its definition. This is because proofs of theorems are in the private scope. This is the case both for public and private theorems.
The option `[backward.privateInPublic](Source-Files-and-Modules/#backward___privateInPublic "Documentation for option backward.privateInPublic")` can be used while transitioning from ordinary source files to modules. When it is set to `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, private definitions are exported, though their names are not accessible in importing modules. However, references to them in the public part of their defining module are allowed. Such references result in a warning unless the option `[backward.privateInPublic.warn](Source-Files-and-Modules/#backward___privateInPublic___warn "Documentation for option backward.privateInPublic.warn")` is set to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`. These warnings can be used to locate and eventually eliminate these references, allowing `[backward.privateInPublic](Source-Files-and-Modules/#backward___privateInPublic "Documentation for option backward.privateInPublic")` to be disabled. Similarly, `[backward.proofsInPublic](Source-Files-and-Modules/#backward___proofsInPublic "Documentation for option backward.proofsInPublic")` causes proofs created with ``Lean.Parser.Term.by```by` to be public, rather than private; this can enable ``Lean.Parser.Term.by```by` to fill in metavariables in its expected type. Most use cases for `[backward.proofsInPublic](Source-Files-and-Modules/#backward___proofsInPublic "Documentation for option backward.proofsInPublic")` also require that `[backward.privateInPublic](Source-Files-and-Modules/#backward___privateInPublic "Documentation for option backward.privateInPublic")` is enabled.
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=backward.privateInPublic "Permalink")option
```
backward.privateInPublic
```

Default value: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
(module system) Export `private` declarations, allowing for arbitrary access to them while code is being ported to the module system. Such accesses will generate warnings unless `[backward.privateInPublic.warn](Source-Files-and-Modules/#backward___privateInPublic___warn "Documentation for option backward.privateInPublic.warn")` is disabled.
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=backward.privateInPublic.warn "Permalink")option
```
backward.privateInPublic.warn
```

Default value: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
(module system) Warn on accesses to `private` declarations that are allowed only by `[backward.privateInPublic](Source-Files-and-Modules/#backward___privateInPublic "Documentation for option backward.privateInPublic")` being enabled.
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=backward.proofsInPublic "Permalink")option
```
backward.proofsInPublic
```

Default value: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
(module system) Do not abstract proofs used in the public scope into auxiliary theorems. Enabling this option may lead to failures or, when `[backward.privateInPublic](Source-Files-and-Modules/#backward___privateInPublic "Documentation for option backward.privateInPublic")` and its `warn` sub-option are enabled, additional warnings from private accesses.
Exporting Private Definitions
In the module `L.Defs`, the public definition of `f` refers to the private definition `drop2` in its signature. Because `[backward.privateInPublic](Source-Files-and-Modules/#backward___privateInPublic "Documentation for option backward.privateInPublic")` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, this is allowed, resulting in a warning:
`L/Defs.lean``module  set_option [backward.privateInPublic](Source-Files-and-Modules/#backward___privateInPublic "Documentation for option backward.privateInPublic") true  def drop2 (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α := xs.[drop](Basic-Types/Linked-Lists/#List___drop "Documentation for List.drop") 2  public def f (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) (transform : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α:= `Private declaration `[drop2](Source-Files-and-Modules/#_private___0___drop2-_LPAR_in-Exporting-Private-Definitions_RPAR_ "Definition of example")` accessed publicly; this is allowed only because the `backward.privateInPublic` option is enabled.   Disable `backward.privateInPublic.warn` to silence this warning.`[drop2](Source-Files-and-Modules/#_private___0___drop2-_LPAR_in-Exporting-Private-Definitions_RPAR_ "Definition of example")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α := transform xs `

```
Private declaration `[drop2](Source-Files-and-Modules/#_private___0___drop2-_LPAR_in-Exporting-Private-Definitions_RPAR_ "Definition of example")` accessed publicly; this is allowed only because the `backward.privateInPublic` option is enabled. 

Disable `backward.privateInPublic.warn` to silence this warning.
```

When the module is imported, references to `f` use `drop2` as a default argument value; however, its name is inaccessible in the module `L`:
`L.lean``module import L.Defs  def xs := [1, 2, 3]  set_option pp.explicit true [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") `@[f](Source-Files-and-Modules/#f-_LPAR_in-Exporting-Private-Definitions_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [xs](Source-Files-and-Modules/#_private___0___xs-_LPAR_in-Exporting-Private-Definitions_RPAR_ "Definition of example") (@drop2✝ [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [f](Source-Files-and-Modules/#f-_LPAR_in-Exporting-Private-Definitions_RPAR_ "Definition of example") [xs](Source-Files-and-Modules/#_private___0___xs-_LPAR_in-Exporting-Private-Definitions_RPAR_ "Definition of example") `

```
@[f](Source-Files-and-Modules/#f-_LPAR_in-Exporting-Private-Definitions_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [xs](Source-Files-and-Modules/#_private___0___xs-_LPAR_in-Exporting-Private-Definitions_RPAR_ "Definition of example") (@drop2✝ [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

Proofs in Public
In the plain source file `NotMod`, the definition of `two` uses the content of the proof to fill out the numeric value in the definition by solving a [`metavariable`](Tactic-Proofs/Reading-Proof-States/#--tech-term-metavariables):
`NotMod.lean``structure Half (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) where   val : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   ok : val + val = n  abbrev two := Half.mk _ <| by⊢ ?m.3 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") ?m.3 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ?m.5   [show](Tactic-Proofs/Tactic-Reference/#show "Documentation for tactic") 2 + 2 = 4⊢ 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 4   [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 `
Converting this file to a module results in an error, because the body of the definition is exposed in the public part but the proof is private and thus cannot change the public type:
`Mod.lean``module public [section](Namespaces-and-Sections/#Lean___Parser___Command___section "Documentation for syntax")  structure Half (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) where   val : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   ok : val + val = n  abbrev two := Half.mk _ <| `tactic execution is stuck, goal contains metavariables   ?m.3 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") ?m.3 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ?m.5`by [show](Tactic-Proofs/Tactic-Reference/#show "Documentation for tactic") 2 + 2 = 4 [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic") `

```
tactic execution is stuck, goal contains metavariables
  ?m.3 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") ?m.3 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ?m.5
```

Setting the option `[backward.proofsInPublic](Source-Files-and-Modules/#backward___proofsInPublic "Documentation for option backward.proofsInPublic")` causes the proof to be in the public part of the module so it can solve the metavariable:
`Mod.lean``module public [section](Namespaces-and-Sections/#Lean___Parser___Command___section "Documentation for syntax")  structure Half (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) where   val : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   ok : val + val = n  set_option [backward.proofsInPublic](Source-Files-and-Modules/#backward___proofsInPublic "Documentation for option backward.proofsInPublic") true [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") abbrev two := Half.mk _ <| by⊢ ?m.3 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") ?m.3 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") ?m.5   [show](Tactic-Proofs/Tactic-Reference/#show "Documentation for tactic") 2 + 2 = 4⊢ 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 4   [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 `
However, it is typically better style to reformulate the definition so that the proof has a complete goal:
`Mod.lean``module public [section](Namespaces-and-Sections/#Lean___Parser___Command___section "Documentation for syntax")  structure Half (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) where   val : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   ok : val + val = n  abbrev two : Half 4 := Half.mk 2 <| by⊢ 2 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 4   [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 `
The private scope of a module may be imported into another module using the ``Lean.Parser.Module.import```all` modifier. By default, this is only allowed if the imported module and the current module are from the same Lake [package](Build-Tools-and-Distribution/Lake/#--tech-term-package), as its main purpose is to allow for separating definitions and proofs into separate modules for internal organization of a library. The Lake package or library option [`allowImportAll`](Build-Tools-and-Distribution/Lake/#Lake___PackageConfig-allowImportAll) can be set to allow other packages to access to the current package's private scopes via ``Lean.Parser.Module.import```import all`. The imported private scope includes private imports of the imported module, including nested ``Lean.Parser.Module.import```import all`s. As a consequence, the set of private scopes accessible to the current module is the transitive closure of ``Lean.Parser.Module.import```import all` declarations.
The module system's ``Lean.Parser.Module.import```import all` is more powerful than ``Lean.Parser.Module.import```import` without the module system. It makes imported private definitions accessible directly by name, as if they were defined in the current module. A secondary use case for ``Lean.Parser.Module.import```import all` is to access code in multiple modules within a library that should nonetheless not be provided to downstream consumers, as well as to allow tests to access information that is not part of the public API.
Importing Private Information
This library separates a module of definitions from a module of lemmas. This is a common pattern in Lean code.
`Tree/Basic.lean``module  public inductive Tree (α : Type u) : Type u where   | leaf   | branch (left : Tree α) (val : α) (right : Tree α)  public def Tree.count : Tree α → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   | .leaf => 0   | .branch left _ right => left.count + 1 + right.count `
However, because `Tree.count` is not exposed, the proof in the lemma file cannot unfold it:
`Tree/Lemmas.lean``module public import Tree.Basic theorem Tree.count_leaf_eq_zero : count (.leaf : Tree α) = 0 := byα:Type u_1⊢ leaf.count [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0   ``simp` made no progress`[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [`Invalid simp theorem `count`: Expected a definition with an exposed body`count]α:Type u_1⊢ leaf.count [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0 `

```
Invalid simp theorem `count`: Expected a definition with an exposed body
```

Importing the private scope from `Tree.Basic` into the lemma module allows the definition to be unfolded in the proof.
`Tree/Basic.lean``module  public inductive Tree (α : Type u) : Type u where   | leaf   | branch (left : Tree α) (val : α) (right : Tree α)  public def Tree.count : Tree α → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   | .leaf => 0   | .branch left _ right => left.count + 1 + right.count `
`Tree/Lemmas.lean``module import all Tree.Basic public import Tree.Basic theorem Tree.count_leaf_eq_zero : count (.leaf : Tree α) = 0 := byα:Type u_1⊢ leaf.count [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 0   [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [count]All goals completed! 🐙 `
###  5.4.1. The Meta Phase[🔗](find/?domain=Verso.Genre.Manual.section&name=meta-phase "Permalink")
Definitions in Lean result in both a representation in the type theory that is designed for formal reasoning and a compiled representation that is designed for execution. This compiled representation is used to generate machine code, but it can also be executed directly using an interpreter. The code runs during [elaboration](Elaboration-and-Compilation/#--tech-term-elaboration), such as [tactics](Tactic-Proofs/#tactics) or [macros](Notations-and-Macros/Macros/#macros), is the compiled form of definitions. If this compiled representation changes, then any code created by it may no longer be up to date, and it must be re-run. Because the compiler performs non-trivial optimizations, changes to any definition in the transitive dependency chain of a function could in principle invalidate its compiled representation. This means that metaprograms exported by modules induce a much stronger coupling than ordinary definitions. Furthermore, metaprograms run _during_ the construction of ordinary terms; thus, they must be fully defined and compiled before use. After all, a function definition without a body cannot be run. The time at which metaprograms are run is referred to as the _metaprogramming phase_ , frequently just called the _meta phase_.
Just as they distinguish between public and private information, modules additionally distinguish code that is available in the meta phase from ordinary code. Any declaration used as an entry point to compile-time execution has to be tagged with the ``Lean.Parser.Module.import```meta` modifier, which indicates that the declaration is available for use as a metaprogram. This is automatically done in built-in metaprogramming syntax such as ``Lean.Parser.Command.syntax : command``[`syntax`](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax), ``Lean.Parser.Command.macro : command``[`macro`](Notations-and-Macros/Macros/#Lean___Parser___Command___macro), and ``Lean.Parser.Command.elab : command```elab` but may need to be done explicitly when manually applying metaprogramming attributes such as `app_delab` or when defining helper declarations. A ``Parser.Command.declModifiers```meta` definition may only access (and thus invoke) other ``Parser.Command.declModifiers```meta` definitions in execution-relevant positions; a non-``Parser.Command.declModifiers```meta` definition likewise may only access other non-``Parser.Command.declModifiers```meta` definitions.
Meta Definitions
In this module, the helper function `revArrays` reverses the order of the elements in each array literal in a term. This is called by the macro `rev!`.
`Main.lean``module  [open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Lean  [variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax") [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadRef m] [MonadQuotation m]  partial def revArrays : [Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax") → m [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")   | `(#[$xs,*]) => `(#[$((xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")).[reverse](Basic-Types/Arrays/#Array___reverse "Documentation for Array.reverse")),*])   | other => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")     match other with     | [.node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node") k i args =>       [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ⟨[.node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node") k i (← args.[mapM](Basic-Types/Arrays/#Array___mapM "Documentation for Array.mapM") revArrays)⟩     | _ => [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ⟨other⟩  `Invalid `meta` definition `_aux___macroRules_termRev!__1`, `revArrays` not marked `meta``[macro](Notations-and-Macros/Macros/#Lean___Parser___Command___macro "Documentation for syntax") "rev!" e:term : term => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") revArrays e `
The error message indicates that `revArrays` cannot be used from the macro because it is not defined in the module's [metaprogramming phase](Source-Files-and-Modules/#--tech-term-metaprogramming-phase):

```
Invalid `meta` definition `_aux___macroRules_termRev!__1`, `revArrays` not marked `meta`
```

Marking `revArrays` with the ``Lean.Parser.Command.declModifiers`
`[`meta`](Definitions/Modifiers/#Lean___Parser___Command___declModifiers) modifier allows the macro definition to call it:
`Main.lean``module  [open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Lean  [variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax") [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadRef m] [MonadQuotation m]  meta partial def revArrays : [Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax") → m [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")   | `(#[$xs,*]) => `(#[$((xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")).[reverse](Basic-Types/Arrays/#Array___reverse "Documentation for Array.reverse")),*])   | other => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")     match other with     | [.node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node") k i args =>       [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ⟨[.node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node") k i (← args.[mapM](Basic-Types/Arrays/#Array___mapM "Documentation for Array.mapM") revArrays)⟩     | _ => [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ⟨other⟩  [macro](Notations-and-Macros/Macros/#Lean___Parser___Command___macro "Documentation for syntax") "rev!" e:term : term => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   revArrays e  `#[3, 2, 1]`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") rev! #[1, 2, 3] `

```
#[3, 2, 1]
```

Libraries that were not originally part of the meta phase can be brought into it by importing a module with ``Parser.Module.import```meta import`. When a module is imported at the meta phase, all of its definitions are made available at that phase, whether or not they were marked ``Parser.Command.declModifiers```meta`. There is no meta-meta phase. In addition to making the imported module's public contents available at the meta phase, ``Parser.Module.import```meta import` indicates that the current module should be rebuilt if the compiled representation of the imported module changes, ensuring that modified metaprograms are re-run. If a definition should be usable in both phases, then it must be defined in a separate module and imported at both phases.
Cross-Phase Code Reuse
In this module, the function `toPalindrome` is defined in the meta phase, which allows it to be used in a macro but not in an ordinary definition:
`Phases.lean``module  [open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Lean  [variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax") [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadRef m] [MonadQuotation m]  meta def toPalindrome (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α := xs ++ xs.[reverse](Basic-Types/Arrays/#Array___reverse "Documentation for Array.reverse")  meta partial def palArrays : [Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax") → m [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")   | `(#[$xs,*]) => `(#[$([toPalindrome](Source-Files-and-Modules/#_private___0___toPalindrome-_LPAR_in-Cross-Phase-Code-Reuse_RPAR_ "Definition of example") (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term"))),*])   | other => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")     match other with     | [.node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node") k i args =>       [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ⟨[.node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node") k i (← args.[mapM](Basic-Types/Arrays/#Array___mapM "Documentation for Array.mapM") palArrays)⟩     | _ => [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ⟨other⟩  [macro](Notations-and-Macros/Macros/#Lean___Parser___Command___macro "Documentation for syntax") "pal!" e:term : term => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   palArrays e  `[#[](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[]](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray") [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")6[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 7[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 8[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") pal! (#[1, 2, 3] ++ [6, 7, 8]) public def `Invalid definition `[colors](Source-Files-and-Modules/#colors-_LPAR_in-Cross-Phase-Code-Reuse_RPAR_ "Definition of example")`, may not access declaration `[toPalindrome](Source-Files-and-Modules/#_private___0___toPalindrome-_LPAR_in-Cross-Phase-Code-Reuse_RPAR_ "Definition of example")` marked as `meta``colors := [toPalindrome](Source-Files-and-Modules/#_private___0___toPalindrome-_LPAR_in-Cross-Phase-Code-Reuse_RPAR_ "Definition of example") #["red", "green", "blue"] `

```
Invalid definition `[colors](Source-Files-and-Modules/#colors-_LPAR_in-Cross-Phase-Code-Reuse_RPAR_ "Definition of example")`, may not access declaration `[toPalindrome](Source-Files-and-Modules/#_private___0___toPalindrome-_LPAR_in-Cross-Phase-Code-Reuse_RPAR_ "Definition of example")` marked as `meta`
```

Moving `toPalindrome` to its own module, `Phases.Pal`, allows this module to be imported at both phases:
`Phases/Pal.lean``module  public def toPalindrome (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α := xs ++ xs.[reverse](Basic-Types/Arrays/#Array___reverse "Documentation for Array.reverse") `
`Phases.lean``module  meta import Phases.Pal import Phases.Pal  [open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Lean  [variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax") [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [MonadRef m] [MonadQuotation m]  meta partial def palArrays : [Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax") → m [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")   | `(#[$xs,*]) => `(#[$([toPalindrome](Source-Files-and-Modules/#toPalindrome-_LPAR_in-Cross-Phase-Code-Reuse_RPAR_ "Definition of example") (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term"))),*])   | other => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")     match other with     | [.node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node") k i args =>       [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ⟨[.node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node") k i (← args.[mapM](Basic-Types/Arrays/#Array___mapM "Documentation for Array.mapM") palArrays)⟩     | _ => [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") ⟨other⟩  local [macro](Notations-and-Macros/Macros/#Lean___Parser___Command___macro "Documentation for syntax") "pal!" e:term : term => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   palArrays e  `[#[](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 3[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 2[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[]](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray") [++](Type-Classes/Basic-Classes/#HAppend___mk "Documentation for HAppend.hAppend") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")6[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 7[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 8[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") pal! (#[1, 2, 3] ++ [6, 7, 8]) public def colors := [toPalindrome](Source-Files-and-Modules/#toPalindrome-_LPAR_in-Cross-Phase-Code-Reuse_RPAR_ "Definition of example") #["red", "green", "blue"] `
If the macro `pal!` were public (that is, if it was not declared with the `local` modifier) then the ``Lean.Parser.Module.import```meta import` of `Phases.Pal` would need to be declared ``Lean.Parser.Module.import```public` as well.
In addition, the import must be public if the imported definition may be executed at compile time outside the current module, i.e. if it is reachable from some public ``Parser.Command.declModifiers```meta` definition in the current module. Use ``Parser.Module.import```public meta import`. If the declaration is already declared ``Parser.Command.declModifiers```meta`, then ``Parser.Module.import```public import` is sufficient.
Unlike definitions, most metaprograms are public by default. Thus, most ``Lean.Parser.Module.import```meta import` are also ``Parser.Module.import```public` in practice. The exception is when a definition is imported solely for use in local metaprograms, such as those declared with ``Parser.Command.syntax```local syntax`, ``Parser.Command.macro```local macro`, or ``Parser.Command.elab```local elab`.
As a guideline, it is usually preferable to keep the amount of ``Lean.Parser.Command.declModifiers`
`declModifiers` is the collection of modifiers on a declaration:
  * a doc comment `/-- ... -/`
  * a list of attributes `@[attr1, attr2]`
  * a visibility specifier, `private` or `public`
  * `protected`
  * `noncomputable`
  * `unsafe`
  * `partial` or `nonrec`


All modifiers are optional, and have to come in the listed order.
`nestedDeclModifiers` is the same as `declModifiers`, but attributes are printed on the same line as the declaration. It is used for declarations nested inside other syntax, such as inductive constructors, structure projections, and `let rec` / `where` definitions. 
`[`meta`](Definitions/Modifiers/#Lean___Parser___Command___declModifiers) annotations as small as possible. This avoids locking otherwise-reusable declarations into the [meta phase](Source-Files-and-Modules/#--tech-term-meta-phase) and it helps the build system avoid more rebuilds. Thus, when a metaprogram depends on other code that does not itself need to be marked ``Lean.Parser.Command.declModifiers`
`declModifiers` is the collection of modifiers on a declaration:
  * a doc comment `/-- ... -/`
  * a list of attributes `@[attr1, attr2]`
  * a visibility specifier, `private` or `public`
  * `protected`
  * `noncomputable`
  * `unsafe`
  * `partial` or `nonrec`


All modifiers are optional, and have to come in the listed order.
`nestedDeclModifiers` is the same as `declModifiers`, but attributes are printed on the same line as the declaration. It is used for declarations nested inside other syntax, such as inductive constructors, structure projections, and `let rec` / `where` definitions. 
`[`meta`](Definitions/Modifiers/#Lean___Parser___Command___declModifiers), this other code should be placed in a separate module and not marked ``Lean.Parser.Command.declModifiers`
`declModifiers` is the collection of modifiers on a declaration:
  * a doc comment `/-- ... -/`
  * a list of attributes `@[attr1, attr2]`
  * a visibility specifier, `private` or `public`
  * `protected`
  * `noncomputable`
  * `unsafe`
  * `partial` or `nonrec`


All modifiers are optional, and have to come in the listed order.
`nestedDeclModifiers` is the same as `declModifiers`, but attributes are printed on the same line as the declaration. It is used for declarations nested inside other syntax, such as inductive constructors, structure projections, and `let rec` / `where` definitions. 
`[`meta`](Definitions/Modifiers/#Lean___Parser___Command___declModifiers). Only the final module that actually registers a metaprogram needs the helpers to be in the meta phase. This module should use ``Lean.Parser.Module.import```public meta import` to import those helpers and then define its metaprograms using built-in syntax like ``Parser.Command.elab```elab`, using ``Lean.Parser.Command.declaration : command```meta def`, or using ``Lean.Parser.Command.section : command`
A `section`/`end` pair delimits the scope of `variable`, `include`, `open`, `set_option`, and `local` commands. Sections can be nested. `section <id>` provides a label to the section that has to appear with the matching `end`. In either case, the `end` can be omitted, in which case the section is closed at the end of the file.
`[`meta section`](Namespaces-and-Sections/#Lean___Parser___Command___section).
##  5.5. Elaborated Modules[🔗](find/?domain=Verso.Genre.Manual.section&name=module-contents "Permalink")
When Lean elaborates a source file, the result is an [environment](Elaboration-and-Compilation/#--tech-term-environments). The environment includes the constants, [inductive types](The-Type-System/Inductive-Types/#--tech-term-Inductive-types), [theorems](Definitions/Theorems/#--tech-term-theorems), [type classes](Type-Classes/#--tech-term-type-class), [instances](Type-Classes/#--tech-term-instances), and everything else declared in the file, along with side tables that track data as diverse as [simp sets](The-Simplifier/Simp-sets/#--tech-term-simp-set), namespace aliases, and [documentation comments](Definitions/Modifiers/#--tech-term-Documentation-comments). If the file contains a module, then the environment additionally tracks which information is public and private, and the phase at which definitions are available.
As the source file is processed by Lean, commands add content to the environment. After elaboration, the environment is serialized to a `.olean` file, which contains both the environment and a compacted heap region with the run-time objects needed by the environment. This means that an imported source file can be loaded without re-executing all of its commands. Environments that result from elaborating modules are serialized into three [`.olean` files](Source-Files-and-Modules/#--tech-term-___olean-file-next), containing the private, public, and server information in the environment. The server information consists of data such as API documentation and source positions of definitions that is only needed when using the Lean language server and does not need to be loaded along with the public information in other contexts.
##  5.6. Module System Errors and Patterns[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Source-Files-and-Modules--Module-System-Errors-and-Patterns "Permalink")
The following list contains common errors one might encounter when using the module system and especially porting existing files to the module system: 

Unknown constant errors
    
Check whether a private definition is being accessed in the [public scope](Source-Files-and-Modules/#--tech-term-public-scope). If so, the problem can be solved by making the current declaration private as well, or by placing the reference into the private scope using the ``Lean.Parser.Term.structInstFieldDef : structInstFieldDecl```private` modifier on a field or ``Lean.Parser.Term.by```by` for a proof. 

Definitional equality errors, especially after porting
    
Failures of expected definitional equalities are usually due to a missing `expose` attribute on a definition or alternatively, if imported, an ``Lean.Parser.Module.import```import all`. Prefer the former if anyone outside your library might feasibly require the same access. The error message should list non-exposed definitions that could not be unfolded. This may also appear as a kernel error when a tactic directly emits proof terms that reference specific declarations without going through the elaborator, such as for proof by reflection. In this case, there is no readily available trace for debugging; consider using `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")expose[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")`‍` ```Parser.Command.section```section`s generously on the closure of relevant modules.
###  5.6.1. Recipe for Porting Existing Files[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Source-Files-and-Modules--Module-System-Errors-and-Patterns--Recipe-for-Porting-Existing-Files "Permalink")
To gain the benefits of the module system, source files must be made into modules. Start by enabling the module system throughout all files with minimal breaking changes:
  1. Prefix all files with ``Lean.Parser.Module.header```module`.
  2. Make all existing imports ``Lean.Parser.Command.declModifiers`
`declModifiers` is the collection of modifiers on a declaration:
     * a doc comment `/-- ... -/`
     * a list of attributes `@[attr1, attr2]`
     * a visibility specifier, `private` or `public`
     * `protected`
     * `noncomputable`
     * `unsafe`
     * `partial` or `nonrec`
All modifiers are optional, and have to come in the listed order.
`nestedDeclModifiers` is the same as `declModifiers`, but attributes are printed on the same line as the declaration. It is used for declarations nested inside other syntax, such as inductive constructors, structure projections, and `let rec` / `where` definitions. 
`[`public`](Definitions/Modifiers/#Lean___Parser___Command___declModifiers) unless they will be used only in proofs.


  * Add ``Lean.Parser.Module.import```import all` when errors that mention references to private data occur.
  * Add ``Lean.Parser.Module.import```public meta import` when errors that mention “must be ``Lean.Parser.Module.import```meta`” occur. The ``Lean.Parser.Module.import```public` may be omitted when defining local-only metaprograms.


  3. Prefix the remainder of the file with `@[expose] public section` or, for programming-focused files, with ``Lean.Parser.Command.section : command`
A `section`/`end` pair delimits the scope of `variable`, `include`, `open`, `set_option`, and `local` commands. Sections can be nested. `section <id>` provides a label to the section that has to appear with the matching `end`. In either case, the `end` can be omitted, in which case the section is closed at the end of the file.
`[`public section`](Namespaces-and-Sections/#Lean___Parser___Command___section). The latter should be used for programs that will be run but not reasoned about.


After an initial build under the module system succeeds, the dependencies between modules can be iteratively minimized. In particular, removing uses of ``Lean.Parser.Command.declModifiers`
`declModifiers` is the collection of modifiers on a declaration:
  * a doc comment `/-- ... -/`
  * a list of attributes `@[attr1, attr2]`
  * a visibility specifier, `private` or `public`
  * `protected`
  * `noncomputable`
  * `unsafe`
  * `partial` or `nonrec`


All modifiers are optional, and have to come in the listed order.
`nestedDeclModifiers` is the same as `declModifiers`, but attributes are printed on the same line as the declaration. It is used for declarations nested inside other syntax, such as inductive constructors, structure projections, and `let rec` / `where` definitions. 
`[`public`](Definitions/Modifiers/#Lean___Parser___Command___declModifiers) and `[@[](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")expose[]](Attributes/#Lean___Parser___Term___attributes-next "Documentation for syntax")` will help avoid unnecessary rebuilds.
##  5.7. Packages, Libraries, and Targets[🔗](find/?domain=Verso.Genre.Manual.section&name=code-distribution "Permalink")
Lean modules are organized into [_packages_](Build-Tools-and-Distribution/Lake/#--tech-term-package), which are units of code distribution. A [package](Build-Tools-and-Distribution/Lake/#--tech-term-package) may contain multiple libraries or executables.
Code in a package that is intended for use by other Lean packages is organized into libraries. Code that is intended to be compiled and run as independent programs is organized into executables. Packages, libraries, and executables are described in detail in the section on [Lake, the standard Lean build tool](Build-Tools-and-Distribution/Lake/#lake). 
[←4.5. Quotients](The-Type-System/Quotients/#quotients "4.5. Quotients")[6. Namespaces and Sections→](Namespaces-and-Sections/#namespaces-sections "6. Namespaces and Sections")

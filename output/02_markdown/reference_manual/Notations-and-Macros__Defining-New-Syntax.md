[←23.3. Notations](Notations-and-Macros/Notations/#notations "23.3. Notations")[23.5. Macros→](Notations-and-Macros/Macros/#macros "23.5. Macros")
#  23.4. Defining New Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=syntax-ext "Permalink")
Lean's uniform representation of syntax is very general and flexible. This means that extensions to Lean's parser do not require extensions to the representation of parsed syntax.
##  23.4.1. Syntax Model[🔗](find/?domain=Verso.Genre.Manual.section&name=syntax-data "Permalink")
Lean's parser produces a concrete syntax tree, of type `[Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")`. `[Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")` is an inductive type that represents all of Lean's syntax, including commands, terms, tactics, and any custom extensions. All of these are represented by a few basic building blocks: 

Atoms 
    
Atoms are the fundamental terminals of the grammar, including literals (such as those for characters and numbers), parentheses, operators, and keywords. 

Identifiers 
    
Identifiers represent names, such as `x`, `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, or `[Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add")`. Identifier syntax includes a list of pre-resolved names that the identifier might refer to. 

Nodes 
    
Nodes represent the parsing of nonterminals. Nodes contain a _syntax kind_ , which identifies the syntax rule that the node results from, along with an array of child `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")` values. 

Missing Syntax
    
When the parser encounters an error, it returns a partial result, so Lean can provide some feedback about partially-written programs or programs that contain mistakes. Partial results contain one or more instances of missing syntax.
Atoms and identifiers are collectively referred to as _tokens_.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.atom "Permalink")inductive type
```


Lean.Syntax : Type


Lean.Syntax : Type


```

Lean syntax trees.
Syntax trees are used pervasively throughout Lean: they are produced by the parser, transformed by the macro expander, and elaborated. They are also produced by the delaborator and presented to users.
#  Constructors

```
missing : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")
```

A portion of the syntax tree that is missing because of a parse error.
The indexing operator on `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")` also returns `[Syntax.missing](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.missing")` when the index is out of bounds.

```
node (info : [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo")) (kind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind"))
  (args : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")) : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")
```

A node in the syntax tree that may have further syntax as child nodes. The node's `kind` determines its interpretation.
For nodes produced by the parser, the `info` field is typically `[Lean.SourceInfo.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none")`, and source information is stored in the corresponding fields of identifiers and atoms. This field is used in two ways:
  1. The delaborator uses it to associate nodes with metadata that are used to implement interactive features.
  2. Nodes created by quotations use the field to mark the syntax as synthetic (storing the result of `Lean.SourceInfo.fromRef`) even when its leading or trailing tokens are not.



```
atom (info : [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo")) (val : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")
```

A non-identifier atomic component of syntax.
All of the following are atoms:
  * keywords, such as `def`, `fun`, and `inductive`
  * literals, such as numeric or string literals
  * punctuation and delimiters, such as `(`, `)`, and `=>`.


Identifiers are represented by the `[Lean.Syntax.ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.ident")` constructor. Atoms also correspond to quoted strings inside `syntax` declarations.

```
ident (info : [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo")) (rawVal : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw"))
  (val : Lean.Name)
  (preresolved : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Lean.Syntax.Preresolved](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Preresolved___namespace "Documentation for Lean.Syntax.Preresolved")) : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")
```

An identifier.
In addition to source information, identifiers have the following fields:
  * `rawVal` is the literal substring from the input file
  * `val` is the parsed Lean name, potentially including macro scopes.
  * `preresolved` is the list of possible declarations this could refer to, populated by [quotations](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=quasiquotation).


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.Preresolved "Permalink")inductive type
```


Lean.Syntax.Preresolved : Type


Lean.Syntax.Preresolved : Type


```

A possible binding of an identifier in the context in which it was quoted.
Identifiers in quotations may refer to either global declarations or to namespaces that are in scope at the site of the quotation. These are saved in the `Syntax.ident` constructor and are part of the implementation of hygienic macros.
#  Constructors

```
«namespace» (ns : Lean.Name) : [Lean.Syntax.Preresolved](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Preresolved___namespace "Documentation for Lean.Syntax.Preresolved")
```

A potential namespace reference

```
decl (n : Lean.Name) (fields : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [Lean.Syntax.Preresolved](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Preresolved___namespace "Documentation for Lean.Syntax.Preresolved")
```

A potential global constant or section variable reference, with additional field accesses
##  23.4.2. Syntax Node Kinds[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Notations-and-Macros--Defining-New-Syntax--Syntax-Node-Kinds "Permalink")
Syntax node kinds typically identify the parser that produced the node. This is one place where the names given to operators or notations (or their automatically-generated internal names) occur. While only nodes contain a field that identifies their kind, identifiers have the kind `[identKind](Notations-and-Macros/Defining-New-Syntax/#Lean___identKind "Documentation for Lean.identKind")` by convention, while atoms have their internal string as their kind by convention. Lean's parser wraps each keyword atom `KW` in a singleton node whose kind is ``token.KW`. The kind of a syntax value can be extracted using `[Syntax.getKind](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___getKind "Documentation for Lean.Syntax.getKind")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.SyntaxNodeKind "Permalink")def
```


Lean.SyntaxNodeKind : Type


Lean.SyntaxNodeKind : Type


```

Specifies the interpretation of a `Syntax.node` value. An abbreviation for `Name`.
Node kinds may be any name, and do not need to refer to declarations in the environment. Conventionally, however, a node's kind corresponds to the `Parser` or `ParserDesc` declaration that produces it. There are also a number of built-in node kinds that are used by the parsing infrastructure, such as `nullKind` and `choiceKind`; these do not correspond to parser declarations.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.isOfKind "Permalink")def
```


Lean.Syntax.isOfKind (stx : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")) (k : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Lean.Syntax.isOfKind (stx : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax"))
  (k : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether syntax has the given kind or pseudo-kind.
“Pseudo-kinds” are kinds that are assigned by convention to non-`Syntax.node` values: `identKind` for `Syntax.ident`, ``missing` for `Syntax.missing`, and the atom's string literal for atoms.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.getKind "Permalink")def
```


Lean.Syntax.getKind (stx : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")) : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


Lean.Syntax.getKind (stx : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")) :
  [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


```

Gets the kind of a `Syntax.node` value, or the pseudo-kind of any other `Syntax` value.
“Pseudo-kinds” are kinds that are assigned by convention to non-`Syntax.node` values: `identKind` for `Syntax.ident`, ``missing` for `Syntax.missing`, and the atom's string literal for atoms.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.setKind "Permalink")def
```


Lean.Syntax.setKind (stx : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")) (k : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")) :
  [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")


Lean.Syntax.setKind (stx : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax"))
  (k : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")) : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")


```

Changes the kind at the root of a `Syntax.node` to `k`.
Returns all other `Syntax` values unchanged.
##  23.4.3. Token and Literal Kinds[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Notations-and-Macros--Defining-New-Syntax--Token-and-Literal-Kinds "Permalink")
A number of named kinds are associated with the basic tokens produced by the parser. Typically, single-token syntax productions consist of a `[node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node")` that contains a single `[atom](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.atom")`; the kind saved in the node allows the value to be recognized. Atoms for literals are not interpreted by the parser: string atoms include their leading and trailing double-quote characters along with any escape sequences contained within, and hexadecimal numerals are saved as a string that begins with `"0x"`. [Helpers](Notations-and-Macros/Defining-New-Syntax/#typed-syntax-helpers) such as `[Lean.TSyntax.getString](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___getString "Documentation for Lean.TSyntax.getString")` are provided to perform this decoding on demand.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.identKind "Permalink")def
```


Lean.identKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


Lean.identKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


```

The pseudo-kind assigned to identifiers: ``ident`.
The name ``ident` is not actually used as a kind for `Syntax.node` values. It is used by convention as the kind of `Syntax.ident` values.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.strLitKind "Permalink")def
```


Lean.strLitKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


Lean.strLitKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


```

``str` is the node kind of string literals like `"foo"`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.interpolatedStrKind "Permalink")def
```


Lean.interpolatedStrKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


Lean.interpolatedStrKind :
  [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


```

``interpolatedStrKind` is the node kind of an interpolated string literal like `"value = {x}"` in `s!"value = {x}"`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.interpolatedStrLitKind "Permalink")def
```


Lean.interpolatedStrLitKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


Lean.interpolatedStrLitKind :
  [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


```

``interpolatedStrLitKind` is the node kind of interpolated string literal fragments like `"value = {` and `}"` in `s!"value = {x}"`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.charLitKind "Permalink")def
```


Lean.charLitKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


Lean.charLitKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


```

``char` is the node kind of character literals like `'A'`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.numLitKind "Permalink")def
```


Lean.numLitKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


Lean.numLitKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


```

``num` is the node kind of number literals like `42` and `0xa1`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.scientificLitKind "Permalink")def
```


Lean.scientificLitKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


Lean.scientificLitKind :
  [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


```

``scientific` is the node kind of floating point literals like `1.23e-3`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.nameLitKind "Permalink")def
```


Lean.nameLitKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


Lean.nameLitKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


```

``name` is the node kind of name literals like ``foo`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.fieldIdxKind "Permalink")def
```


Lean.fieldIdxKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


Lean.fieldIdxKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


```

``fieldIdx` is the node kind of projection indices like the `2` in `x.2`.
##  23.4.4. Internal Kinds[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Notations-and-Macros--Defining-New-Syntax--Internal-Kinds "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.groupKind "Permalink")def
```


Lean.groupKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


Lean.groupKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


```

The ``group` kind is used for nodes that result from `Lean.Parser.group`. This avoids confusion with the null kind when used inside `[optional](Functors___-Monads-and--do--Notation/API-Reference/#optional "Documentation for optional")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.nullKind "Permalink")def
```


Lean.nullKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


Lean.nullKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


```

``null` is the “fallback” kind, used when no other kind applies. Null nodes result from repetition operators, and empty null nodes represent the failure of an optional parse.
The null kind is used for raw list parsers like `many`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.choiceKind "Permalink")def
```


Lean.choiceKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


Lean.choiceKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


```

The ``choice` kind is used to represent ambiguous parse results.
The parser prioritizes longer matches over shorter ones, but there is not always a unique longest match. All the parse results are saved, and the determination of which to use is deferred until typing information is available.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.hygieneInfoKind "Permalink")def
```


Lean.hygieneInfoKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


Lean.hygieneInfoKind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")


```

``hygieneInfo` is the node kind of the `Lean.Parser.hygieneInfo` parser, which produces an “invisible token” that captures the hygiene information at the current point without parsing anything.
They can be used to generate identifiers (with `Lean.HygieneInfo.mkIdent`) as if they were introduced in a macro's input, rather than by its implementation.
##  23.4.5. Source Positions[🔗](find/?domain=Verso.Genre.Manual.section&name=source-info "Permalink")
Atoms, identifiers, and nodes optionally contain source information that tracks their correspondence with the original file. The parser saves source information for all tokens, but not for nodes; position information for parsed nodes is reconstructed from their first and last tokens. Not all `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")` data results from the parser: it may be the result of [macro expansion](Notations-and-Macros/Macros/#--tech-term-macro-expansion), in which case it typically contains a mix of generated and parsed syntax, or it may be the result of [delaborating](Notations-and-Macros/Extending-Lean___s-Output/#--tech-term-delaborators) an internal term to display it to a user. In these use cases, nodes may themselves contain source information.
Source information comes in two varieties: 

Original 
    
Original source information comes from the parser. In addition to the original source location, it also contains leading and trailing whitespace that was skipped by the parser, which allows the original string to be reconstructed. This whitespace is saved as offsets into the string representation of the original source code (that is, as `Substring`) to avoid having to allocate copies of substrings. 

Synthetic 
    
Synthetic source information comes from metaprograms (including macros) or from Lean's internals. Because there is no original string to be reconstructed, it does not save leading and trailing whitespace. Synthetic source positions are used to provide accurate feedback even when terms have been automatically transformed, as well as to track the correspondence between elaborated expressions and their presentation in Lean's output. A synthetic position may be marked _canonical_ , in which case some operations that would ordinarily ignore synthetic positions will treat it as if it were not.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.SourceInfo.synthetic "Permalink")inductive type
```


Lean.SourceInfo : Type


Lean.SourceInfo : Type


```

Source information that relates syntax to the context that it came from.
The primary purpose of `SourceInfo` is to relate the output of the parser and the macro expander to the original source file. When produced by the parser, `Syntax.node` does not carry source info; the parser associates it only with atoms and identifiers. If a `Syntax.node` is introduced by a quotation, then it has synthetic source info that both associates it with an original reference position and indicates that the original atoms in it may not originate from the Lean file under elaboration.
Source info is also used to relate Lean's output to the internal data that it represents; this is the basis for many interactive features. When used this way, it can occur on `Syntax.node` as well.
#  Constructors

```
original (leading : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) (pos : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (trailing : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) (endPos : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) :
  [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo")
```

A token produced by the parser from original input that includes both leading and trailing whitespace as well as position information.
The `leading` whitespace is inferred after parsing by `Syntax.updateLeading`. This is because the “preceding token” is not well-defined during parsing, especially in the presence of backtracking.

```
synthetic (pos endPos : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (canonical : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo")
```

Synthetic syntax is syntax that was produced by a metaprogram or by Lean itself (e.g. by a quotation). Synthetic syntax is annotated with a source span from the original syntax, which relates it to the source file.
The delaborator uses this constructor to store an encoded indicator of which core language expression gave rise to the syntax.
The `canonical` flag on synthetic syntax is enabled for syntax that is not literally part of the original input syntax but should be treated “as if” the user really wrote it for the purpose of hovers and error messages. This is usually used on identifiers in order to connect the binding site to the user's original syntax even if the name of the identifier changes during expansion, as well as on tokens that should receive targeted messages.
Generally speaking, a macro expansion should only use a given piece of input syntax in a single canonical token. An exception to this rule is when the same identifier is used to declare two binders, as in the macro expansion for dependent if:

```
`(if $h : $cond then $t else $e) ~>
`(dite $cond (fun $h => $t) (fun $h => $t))

```

In these cases, if the user hovers over `h` they will see information about both binding sites.

```
none : [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo")
```

A synthesized token without position information.
##  23.4.6. Inspecting Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Notations-and-Macros--Defining-New-Syntax--Inspecting-Syntax "Permalink")
There are three primary ways to inspect `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")` values: 

The `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` Instance
    
The `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") [Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")` instance produces a very detailed representation of syntax in terms of the constructors of the `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")` type. 

The `ToString` Instance
    
The `ToString [Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")` instance produces a compact view, representing certain syntax kinds with particular conventions that can make it easier to read at a glance. This instance suppresses source position information. 

The Pretty Printer
    
Lean's pretty printer attempts to render the syntax as it would look in a source file, but fails if the nesting structure of the syntax doesn't match the expected shape. Representing Syntax as Constructors
The `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instance's representation of syntax can be inspected by quoting it in the context of ``Lean.Parser.Command.eval : command`
`[`#eval`](Interacting-with-Lean/#Lean___Parser___Command___eval), which can run actions in the command elaboration monad `CommandElabM`. To reduce the size of the example output, the helper `[removeSourceInfo](Notations-and-Macros/Defining-New-Syntax/#removeSourceInfo-_LPAR_in-Representing-Syntax-as-Constructors_RPAR_ "Definition of example")` is used to remove source information prior to display.
`partial def removeSourceInfo : [Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax") → [Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")   | [.atom](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.atom") _ str => [.atom](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.atom") [.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none") str   | [.ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.ident") _ str x pre => [.ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.ident") [.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none") str x pre   | [.node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node") _ k children => [.node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node") [.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none") k (children.[map](Basic-Types/Arrays/#Array___map "Documentation for Array.map") [removeSourceInfo](Notations-and-Macros/Defining-New-Syntax/#removeSourceInfo-_LPAR_in-Representing-Syntax-as-Constructors_RPAR_ "Definition of example"))   | [.missing](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.missing") => .missing ```Lean.Syntax.node   (Lean.SourceInfo.none)   `«term_+_»   #[Lean.Syntax.node (Lean.SourceInfo.none) `num #[Lean.Syntax.atom (Lean.SourceInfo.none) "2"],     Lean.Syntax.atom (Lean.SourceInfo.none) "+", Lean.Syntax.missing]`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let stx ← `(2 + $(⟨[.missing](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.missing")⟩)) logInfo ([repr](Interacting-with-Lean/#repr-next "Documentation for repr") ([removeSourceInfo](Notations-and-Macros/Defining-New-Syntax/#removeSourceInfo-_LPAR_in-Representing-Syntax-as-Constructors_RPAR_ "Definition of example") stx.[raw](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.raw"))) `
```
Lean.Syntax.node
  (Lean.SourceInfo.none)
  `«term_+_»
  #[Lean.Syntax.node (Lean.SourceInfo.none) `num #[Lean.Syntax.atom (Lean.SourceInfo.none) "2"],
    Lean.Syntax.atom (Lean.SourceInfo.none) "+", Lean.Syntax.missing]
```

In the second example, [macro scopes](Notations-and-Macros/Macros/#--tech-term-macro-scopes) inserted by quotation are visible on the call to `[List.length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")`.
``Lean.Syntax.node   (Lean.SourceInfo.none)   `Lean.Parser.Term.app   #[Lean.Syntax.ident       (Lean.SourceInfo.none)       "List.length".toRawSubstring       (Lean.Name.mkNum `List.length._@.Manual.NotationsMacros.SyntaxDef._hyg 2)       [Lean.Syntax.Preresolved.decl `List.length []],     Lean.Syntax.node       (Lean.SourceInfo.none)       `null       #[Lean.Syntax.node           (Lean.SourceInfo.none)           `«term[_]»           #[Lean.Syntax.atom (Lean.SourceInfo.none) "[",             Lean.Syntax.node               (Lean.SourceInfo.none)               `null               #[Lean.Syntax.node (Lean.SourceInfo.none) `str #[Lean.Syntax.atom (Lean.SourceInfo.none) "\"Rose\""],                 Lean.Syntax.atom (Lean.SourceInfo.none) ",",                 Lean.Syntax.node (Lean.SourceInfo.none) `str #[Lean.Syntax.atom (Lean.SourceInfo.none) "\"Daffodil\""],                 Lean.Syntax.atom (Lean.SourceInfo.none) ",",                 Lean.Syntax.node (Lean.SourceInfo.none) `str #[Lean.Syntax.atom (Lean.SourceInfo.none) "\"Lily\""]],             Lean.Syntax.atom (Lean.SourceInfo.none) "]"]]]`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let stx ← `(List.length ["Rose", "Daffodil", "Lily"]) logInfo ([repr](Interacting-with-Lean/#repr-next "Documentation for repr") ([removeSourceInfo](Notations-and-Macros/Defining-New-Syntax/#removeSourceInfo-_LPAR_in-Representing-Syntax-as-Constructors_RPAR_ "Definition of example") stx.[raw](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.raw"))) `
The contents of the [pre-resolved identifier](Notations-and-Macros/Macros/#--tech-term-pre-resolved-identifiers) `[List.length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")` are visible here:

```
Lean.Syntax.node
  (Lean.SourceInfo.none)
  `Lean.Parser.Term.app
  #[Lean.Syntax.ident
      (Lean.SourceInfo.none)
      "List.length".toRawSubstring
      (Lean.Name.mkNum `List.length._@.Manual.NotationsMacros.SyntaxDef._hyg 2)
      [Lean.Syntax.Preresolved.decl `List.length []],
    Lean.Syntax.node
      (Lean.SourceInfo.none)
      `null
      #[Lean.Syntax.node
          (Lean.SourceInfo.none)
          `«term[_]»
          #[Lean.Syntax.atom (Lean.SourceInfo.none) "[",
            Lean.Syntax.node
              (Lean.SourceInfo.none)
              `null
              #[Lean.Syntax.node (Lean.SourceInfo.none) `str #[Lean.Syntax.atom (Lean.SourceInfo.none) "\"Rose\""],
                Lean.Syntax.atom (Lean.SourceInfo.none) ",",
                Lean.Syntax.node (Lean.SourceInfo.none) `str #[Lean.Syntax.atom (Lean.SourceInfo.none) "\"Daffodil\""],
                Lean.Syntax.atom (Lean.SourceInfo.none) ",",
                Lean.Syntax.node (Lean.SourceInfo.none) `str #[Lean.Syntax.atom (Lean.SourceInfo.none) "\"Lily\""]],
            Lean.Syntax.atom (Lean.SourceInfo.none) "]"]]]
```

[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAGQKYEMB2A6AogGxQIwChCIwk1FU1iwVZgUc4ATJAMziiRAgDckAyhACuUAMZIAkmjYQ4ALjgCAnmhgoAHnEBJhEtXqNhOHAA+cDChgQQcAPpwAzjChwAvAD5zl6+bQQ0SI7ORqbmwKxqdkEuWmBcbp4Y4eTwGH4B0XCxXCFmaRCsUQDWcGIAFsA4zFwUHr4FgfkZJQAU5ZXV5BggKGCc3HyCIuJSMhAAlLnmIMAODsBoAOYJ07PzS8QAxEi8jCwQIThI8E5agAmEcAAGLQBMcADUcAAkLYAX5N1rC4uAl+Tjk8Y4CCLaSyOAtLhxMFcHj8ISiCQguSnDBQFAAdz+Wx2e2YBwBxyC5yuLQQsxgGCOSxgZTgAG0AEQAJQgDiQ9IANHB6QARFBsWTMSocrmknDKekAXX+cEBwLGUKQkPBA1hwwR8uRqIx4yAA"\))
The `ToString` instance represents the constructors of `[Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")` as follows:
  * The `[ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.ident")` constructor is represented as the underlying name. Source information and pre-resolved names are not shown.
  * The `[atom](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.atom")` constructor is represented as a string.
  * The `[missing](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.missing")` constructor is represented by `<missing>`.
  * The representation of the `[node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node")` constructor depends on the kind. If the kind is ``null`, then the node is represented by its child nodes order in square brackets. Otherwise, the node is represented by its kind followed by its child nodes, both surrounded by parentheses.

Syntax as Strings
The string representation of syntax can be inspected by quoting it in the context of ``Lean.Parser.Command.eval : command`
`[`#eval`](Interacting-with-Lean/#Lean___Parser___Command___eval), which can run actions in the command elaboration monad `CommandElabM`.
``(«term_+_» (num "2") "+" <missing>)`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let stx ← `(2 + $(⟨[.missing](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.missing")⟩)) logInfo (toString stx) `
```
(«term_+_» (num "2") "+" <missing>)
```

In the second example, [macro scopes](Notations-and-Macros/Macros/#--tech-term-macro-scopes) inserted by quotation are visible on the call to `[List.length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")`.
``(Term.app  `List.length._@.Manual.NotationsMacros.SyntaxDef._hyg.2  [(«term[_]» "[" [(str "\"Rose\"") "," (str "\"Daffodil\"") "," (str "\"Lily\"")] "]")])`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let stx ← `(List.length ["Rose", "Daffodil", "Lily"]) logInfo (toString stx) `
```
(Term.app
 `List.length._@.Manual.NotationsMacros.SyntaxDef._hyg.2
 [(«term[_]» "[" [(str "\"Rose\"") "," (str "\"Daffodil\"") "," (str "\"Lily\"")] "]")])
```

[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAGQKYEMB2A6AogGxQIwChCIwk1FU1iBiJANxRzgBMJC44cl4BnGAB5xACYRwABgAoATHADUcACQTAF+QYQwXr2BoA5oEvyAJQGOXCDoCSaAGYQ4EmBADKMKNp1x+A44TqNmbE24+QRFxCQQNGAxuXRgACzgAbQAiACUIXiRkgBo4ZIARFCsbFmAcHLyInABPZIBdY04cM0sbOwdnV10PQQMgA"\))
Pretty printing syntax is typically most useful when including it in a message to a user. Normally, Lean automatically invokes the pretty printer when necessary. However, `ppTerm` can be explicitly invoked if needed.
Pretty-Printed Syntax
The string representation of syntax can be inspected by quoting it in the context of ``Lean.Parser.Command.eval : command`
`[`#eval`](Interacting-with-Lean/#Lean___Parser___Command___eval), which can run actions in the command elaboration monad `CommandElabM`. Because new syntax declarations also equip the pretty printer with instructions for displaying them, the pretty printer requires a configuration object. This context can be constructed with a helper:
`def getPPContext : CommandElabM PPContext := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   return {     env := (← getEnv),     opts := (← getOptions),     currNamespace := (← getCurrNamespace),     openDecls := (← getOpenDecls)   } ```2 + 5`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") show CommandElabM [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") from [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let stx ← `(2 + 5) let fmt ← ppTerm (← [getPPContext](Notations-and-Macros/Defining-New-Syntax/#getPPContext-_LPAR_in-Pretty-Printed-Syntax_RPAR_ "Definition of example")) stx logInfo fmt `
```
2 + 5
```

In the second example, the [macro scopes](Notations-and-Macros/Macros/#--tech-term-macro-scopes) inserted on `[List.length](Basic-Types/Linked-Lists/#List___length "Documentation for List.length")` by quotation cause it to be displayed with a dagger (`✝`).
``List.length✝ ["Rose", "Daffodil", "Lily"]`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let stx ← `(List.length ["Rose", "Daffodil", "Lily"]) let fmt ← ppTerm (← [getPPContext](Notations-and-Macros/Defining-New-Syntax/#getPPContext-_LPAR_in-Pretty-Printed-Syntax_RPAR_ "Definition of example")) stx logInfo fmt `
```
List.length✝ ["Rose", "Daffodil", "Lily"]
```

Pretty printing wraps lines and inserts indentation automatically. A [coercion](Coercions/#--tech-term-coercion) typically converts the pretty printer's output to the type expected by `logInfo`, using a default layout width. The width can be controlled by explicitly calling `[pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty")` with a named argument.
``List.length✝   ["Rose", "Daffodil", "Lily", "Rose",     "Daffodil", "Lily", "Rose",     "Daffodil", "Lily"]`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let flowers := #["Rose", "Daffodil", "Lily"] let manyFlowers := flowers ++ flowers ++ flowers let stx ← `(List.length [$(manyFlowers.[map](Basic-Types/Arrays/#Array___map "Documentation for Array.map") ([quote](Notations-and-Macros/Defining-New-Syntax/#Lean___Quote___mk "Documentation for Lean.Quote.quote") (k := `term))),*]) let fmt ← ppTerm (← [getPPContext](Notations-and-Macros/Defining-New-Syntax/#getPPContext-_LPAR_in-Pretty-Printed-Syntax_RPAR_ "Definition of example")) stx logInfo (fmt.[pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") (width := 40)) `
```
List.length✝
  ["Rose", "Daffodil", "Lily", "Rose",
    "Daffodil", "Lily", "Rose",
    "Daffodil", "Lily"]
```

[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAGQKYEMB2A6AogGxQIwChCIwk1FULcC4BhCEEdAE2JaQDM4BzJGAAoCGaGEgAe8AFz1GzNCxr4AsnCEixkuFIC8cFhEJw4UfgFcoFAN5HjccgDdtegBSAEwl78saBwEoANLbGpDAAzs5w7p4wAPJgMMAQaKEBQXAAxhZQAHIoIEihYCjpSBFRfDB0Wbn5hcVIqXZwpOQAIkjpOOG6kR4VcW0dXb62AL7EAMRIDig4cKEAFhAA7rJMrEqqAKpowPCcUIz6hsY4/PMw4nAeAAYuAExwANRwAKwjp+ecIPAeYGAAFSQUBAvWi6iSmhgvgu4lsOAgPAAkmhOBA4N8YJNprNjvDzqFLtc4HcEMBCRgzmgeDAFnAANoAIgAShBQkhGf44IzWihOGiWMAcJzuWScABPRkAXQ+cDO+x+xP+QJBYIqENEEmhsPhiJRaIxP2xMzmBnx+wRy2B3T0EyZrPZIp5fIFQqdYslUvNcHk4oAYpbrRFOIGoOEni8QysgxGMaHQt7CVdbi4yRSqTS6fSACQuX0B6NhjDMMCRACOZggYkiAGsIjcxCDfM3/AAqGXezFKwHA0HlfgaqEwpO65Go9EuTEYMCmGAwcWRZbAFi0iIAFgADM2gA"\))
##  23.4.7. Typed Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=typed-syntax "Permalink")
Syntax may additionally be annotated with a type that specifies which [syntax category](Notations-and-Macros/Defining-New-Syntax/#--tech-term-syntax-categories) it belongs to. The `[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")` structure contains a type-level list of syntax categories along with a syntax tree. The list of syntax categories typically contains precisely one element, in which case the list structure itself is not shown.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.TSyntax "Permalink")structure
```


Lean.TSyntax (ks : [Lean.SyntaxNodeKinds](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKinds "Documentation for Lean.SyntaxNodeKinds")) : Type


Lean.TSyntax (ks : [Lean.SyntaxNodeKinds](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKinds "Documentation for Lean.SyntaxNodeKinds")) :
  Type


```

Typed syntax, which tracks the potential kinds of the `Syntax` it contains.
While syntax quotations produce or expect `TSyntax` values of the correct kinds, this is not otherwise enforced; it can easily be circumvented by direct use of the constructor.
#  Constructor

```
[Lean.TSyntax.mk](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax.mk")
```

#  Fields

```
raw : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")
```

The underlying `Syntax` value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.SyntaxNodeKinds "Permalink")def
```


Lean.SyntaxNodeKinds : Type


Lean.SyntaxNodeKinds : Type


```

`SyntaxNodeKinds` is a set of `SyntaxNodeKind`, implemented as a list.
Singleton `SyntaxNodeKinds` are extremely common. They are written as name literals, rather than as lists; list syntax is required only for empty or non-singleton sets of kinds.
[Quasiquotations](Notations-and-Macros/Macros/#--tech-term-Quasiquotation) prevent the substitution of typed syntax that does not come from the correct syntactic category. For many of Lean's built-in syntactic categories, there is a set of [coercions](Coercions/#--tech-term-coercion) that appropriately wrap one kind of syntax for another category, such as a coercion from the syntax of string literals to the syntax of terms. Additionally, many helper functions that are only valid on some syntactic categories are defined for the appropriate typed syntax only.
The constructor of `[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")` is public, and nothing prevents users from constructing values that break internal invariants. The use of `[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")` should be seen as a way to reduce common mistakes, rather than rule them out entirely.
In addition to `[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax")`, there are types that represent arrays of syntax, with or without separators. These correspond to repeated elements in syntax declarations or antiquotations. `[TSyntaxArray](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntaxArray "Documentation for Lean.TSyntaxArray") ks` is an [abbreviation](Definitions/Definitions/#--tech-term-Abbreviations) for `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ([TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") ks)`, while `[TSepArray](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___mk "Documentation for Lean.Syntax.TSepArray") ks sep` is a structure; this means that [generalized field notation](Terms/Function-Application/#--tech-term-generalized-field-notation) can be used to apply array functions to `[TSyntaxArray](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntaxArray "Documentation for Lean.TSyntaxArray")` but not `[TSepArray](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___mk "Documentation for Lean.Syntax.TSepArray")`. There is a [coercion](Coercions/#--tech-term-coercion) between `[TSepArray](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___mk "Documentation for Lean.Syntax.TSepArray") ks` and `[TSyntaxArray](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntaxArray "Documentation for Lean.TSyntaxArray") ks`, as well as explicit conversion functions. This conversion inserts or removes separator elements from the underlying array, and takes time linear in the number of elements.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.TSyntaxArray "Permalink")def
```


Lean.TSyntaxArray (ks : [Lean.SyntaxNodeKinds](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKinds "Documentation for Lean.SyntaxNodeKinds")) : Type


Lean.TSyntaxArray
  (ks : [Lean.SyntaxNodeKinds](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKinds "Documentation for Lean.SyntaxNodeKinds")) : Type


```

An array of syntaxes of kind `ks`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.TSyntaxArray.raw "Permalink")opaque
```


Lean.TSyntaxArray.raw {ks : [Lean.SyntaxNodeKinds](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKinds "Documentation for Lean.SyntaxNodeKinds")}
  (as : [Lean.TSyntaxArray](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntaxArray "Documentation for Lean.TSyntaxArray") ks) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")


Lean.TSyntaxArray.raw
  {ks : [Lean.SyntaxNodeKinds](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKinds "Documentation for Lean.SyntaxNodeKinds")}
  (as : [Lean.TSyntaxArray](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntaxArray "Documentation for Lean.TSyntaxArray") ks) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")


```

Converts a `TSyntaxArray` to an `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") Syntax`, without reallocation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.TSepArray.elemsAndSeps "Permalink")structure
```


Lean.Syntax.TSepArray (ks : [Lean.SyntaxNodeKinds](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKinds "Documentation for Lean.SyntaxNodeKinds")) (sep : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : Type


Lean.Syntax.TSepArray
  (ks : [Lean.SyntaxNodeKinds](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKinds "Documentation for Lean.SyntaxNodeKinds"))
  (sep : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : Type


```

An array of syntax elements that alternate with the given separator. Each syntax element has a kind drawn from `ks`.
Separator arrays result from repetition operators such as `,*`. [Coercions](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=coercions) to and from `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") (TSyntax ks)` insert or remove separators as required. The untyped equivalent is `Lean.Syntax.SepArray`.
#  Constructor

```
[Lean.Syntax.TSepArray.mk](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___mk "Documentation for Lean.Syntax.TSepArray.mk")
```

#  Fields

```
elemsAndSeps : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")
```

The array of elements and separators, ordered like `#[el1, sep1, el2, sep2, el3]`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.TSepArray.getElems "Permalink")def
```


Lean.Syntax.TSepArray.getElems {k : [Lean.SyntaxNodeKinds](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKinds "Documentation for Lean.SyntaxNodeKinds")} {sep : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}
  (sa : [Lean.Syntax.TSepArray](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___mk "Documentation for Lean.Syntax.TSepArray") k sep) : [Lean.TSyntaxArray](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntaxArray "Documentation for Lean.TSyntaxArray") k


Lean.Syntax.TSepArray.getElems
  {k : [Lean.SyntaxNodeKinds](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKinds "Documentation for Lean.SyntaxNodeKinds")}
  {sep : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}
  (sa : [Lean.Syntax.TSepArray](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___mk "Documentation for Lean.Syntax.TSepArray") k sep) :
  [Lean.TSyntaxArray](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntaxArray "Documentation for Lean.TSyntaxArray") k


```

Extracts the non-separator elements of a separated array.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.TSepArray.elemsAndSeps "Permalink")def
```


Lean.Syntax.TSepArray.elemsAndSeps {ks : [Lean.SyntaxNodeKinds](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKinds "Documentation for Lean.SyntaxNodeKinds")}
  {sep : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (self : [Lean.Syntax.TSepArray](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___mk "Documentation for Lean.Syntax.TSepArray") ks sep) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")


Lean.Syntax.TSepArray.elemsAndSeps
  {ks : [Lean.SyntaxNodeKinds](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKinds "Documentation for Lean.SyntaxNodeKinds")}
  {sep : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}
  (self : [Lean.Syntax.TSepArray](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___mk "Documentation for Lean.Syntax.TSepArray") ks sep) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")


```

The array of elements and separators, ordered like `#[el1, sep1, el2, sep2, el3]`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.TSepArray.ofElems "Permalink")def
```


Lean.Syntax.TSepArray.ofElems {k : [Lean.SyntaxNodeKinds](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKinds "Documentation for Lean.SyntaxNodeKinds")} {sep : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}
  (elems : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ([Lean.TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") k)) : [Lean.Syntax.TSepArray](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___mk "Documentation for Lean.Syntax.TSepArray") k sep


Lean.Syntax.TSepArray.ofElems
  {k : [Lean.SyntaxNodeKinds](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKinds "Documentation for Lean.SyntaxNodeKinds")}
  {sep : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}
  (elems : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ([Lean.TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") k)) :
  [Lean.Syntax.TSepArray](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___mk "Documentation for Lean.Syntax.TSepArray") k sep


```

Constructs a typed separated array from elements by adding suitable separators. The provided array should not include the separators.
Like `Syntax.SepArray.ofElems` but for typed syntax.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.TSepArray.push "Permalink")def
```


Lean.Syntax.TSepArray.push {k : [Lean.SyntaxNodeKinds](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKinds "Documentation for Lean.SyntaxNodeKinds")} {sep : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}
  (sa : [Lean.Syntax.TSepArray](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___mk "Documentation for Lean.Syntax.TSepArray") k sep) (e : [Lean.TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") k) :
  [Lean.Syntax.TSepArray](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___mk "Documentation for Lean.Syntax.TSepArray") k sep


Lean.Syntax.TSepArray.push
  {k : [Lean.SyntaxNodeKinds](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKinds "Documentation for Lean.SyntaxNodeKinds")}
  {sep : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}
  (sa : [Lean.Syntax.TSepArray](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___mk "Documentation for Lean.Syntax.TSepArray") k sep)
  (e : [Lean.TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") k) :
  [Lean.Syntax.TSepArray](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___TSepArray___mk "Documentation for Lean.Syntax.TSepArray") k sep


```

Adds an element to the end of a separated array, adding a separator as needed.
##  23.4.8. Aliases[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Notations-and-Macros--Defining-New-Syntax--Aliases "Permalink")
A number of aliases are provided for commonly-used typed syntax varieties. These aliases allow code to be written at a higher level of abstraction.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.Term "Permalink")def
```


Lean.Syntax.Term : Type


Lean.Syntax.Term : Type


```

Syntax that represents a Lean term.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.Command "Permalink")def
```


Lean.Syntax.Command : Type


Lean.Syntax.Command : Type


```

Syntax that represents a command.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.Level "Permalink")def
```


Lean.Syntax.Level : Type


Lean.Syntax.Level : Type


```

Syntax that represents a universe level.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.Tactic "Permalink")def
```


Lean.Syntax.Tactic : Type


Lean.Syntax.Tactic : Type


```

Syntax that represents a tactic.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.Prec "Permalink")def
```


Lean.Syntax.Prec : Type


Lean.Syntax.Prec : Type


```

Syntax that represents a precedence (e.g. for an operator).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.Prio "Permalink")def
```


Lean.Syntax.Prio : Type


Lean.Syntax.Prio : Type


```

Syntax that represents a priority (e.g. for an instance declaration).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.Ident "Permalink")def
```


Lean.Syntax.Ident : Type


Lean.Syntax.Ident : Type


```

Syntax that represents an identifier.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.StrLit "Permalink")def
```


Lean.Syntax.StrLit : Type


Lean.Syntax.StrLit : Type


```

Syntax that represents a string literal.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.CharLit "Permalink")def
```


Lean.Syntax.CharLit : Type


Lean.Syntax.CharLit : Type


```

Syntax that represents a character literal.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.NameLit "Permalink")def
```


Lean.Syntax.NameLit : Type


Lean.Syntax.NameLit : Type


```

Syntax that represents a quoted name literal that begins with a back-tick.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.NumLit "Permalink")def
```


Lean.Syntax.NumLit : Type


Lean.Syntax.NumLit : Type


```

Syntax that represents a numeric literal.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.ScientificLit "Permalink")def
```


Lean.Syntax.ScientificLit : Type


Lean.Syntax.ScientificLit : Type


```

Syntax that represents a scientific numeric literal that may have decimal and exponential parts.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.HygieneInfo "Permalink")def
```


Lean.Syntax.HygieneInfo : Type


Lean.Syntax.HygieneInfo : Type


```

Syntax that represents macro hygiene info.
##  23.4.9. Helpers for Constructing Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=syntax-construction-helpers "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.mkIdent "Permalink")def
```


Lean.mkIdent (val : Lean.Name) : [Lean.Ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Ident "Documentation for Lean.Syntax.Ident")


Lean.mkIdent (val : Lean.Name) :
  [Lean.Ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Ident "Documentation for Lean.Syntax.Ident")


```

Creates an identifier from a name. The resulting identifier has no source position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.mkIdentFrom "Permalink")def
```


Lean.mkIdentFrom (src : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")) (val : Lean.Name)
  (canonical : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [Lean.Ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Ident "Documentation for Lean.Syntax.Ident")


Lean.mkIdentFrom (src : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax"))
  (val : Lean.Name)
  (canonical : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [Lean.Ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Ident "Documentation for Lean.Syntax.Ident")


```

Creates an identifier with its position copied from `src`.
To refer to a specific constant without a risk of variable capture, use `mkCIdentFrom` instead.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.mkIdentFromRef "Permalink")def
```


Lean.mkIdentFromRef {m : Type → Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [Lean.MonadRef m]
  (val : Lean.Name) (canonical : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : m [Lean.Ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Ident "Documentation for Lean.Syntax.Ident")


Lean.mkIdentFromRef {m : Type → Type}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [Lean.MonadRef m]
  (val : Lean.Name)
  (canonical : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) :
  m [Lean.Ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Ident "Documentation for Lean.Syntax.Ident")


```

Creates an identifier with its position copied from the syntax returned by `getRef`.
To refer to a specific constant without a risk of variable capture, use `mkCIdentFromRef` instead.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.mkCIdent "Permalink")def
```


Lean.mkCIdent (c : Lean.Name) : [Lean.Ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Ident "Documentation for Lean.Syntax.Ident")


Lean.mkCIdent (c : Lean.Name) : [Lean.Ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Ident "Documentation for Lean.Syntax.Ident")


```

Creates an identifier that refers to a constant `c`. The identifier has no source position.
This variant of `mkIdent` makes sure that the identifier cannot accidentally be captured.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.mkCIdentFrom "Permalink")def
```


Lean.mkCIdentFrom (src : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")) (c : Lean.Name)
  (canonical : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [Lean.Ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Ident "Documentation for Lean.Syntax.Ident")


Lean.mkCIdentFrom (src : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax"))
  (c : Lean.Name)
  (canonical : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [Lean.Ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Ident "Documentation for Lean.Syntax.Ident")


```

Creates an identifier referring to a constant `c`. The identifier's position is copied from `src`.
This variant of `mkIdentFrom` makes sure that the identifier cannot accidentally be captured.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.mkCIdentFromRef "Permalink")def
```


Lean.mkCIdentFromRef {m : Type → Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [Lean.MonadRef m]
  (c : Lean.Name) (canonical : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : m [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")


Lean.mkCIdentFromRef {m : Type → Type}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [Lean.MonadRef m]
  (c : Lean.Name)
  (canonical : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) :
  m [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")


```

Creates an identifier referring to a constant `c`. The identifier's position is copied from the syntax returned by `getRef`.
This variant of `mkIdentFrom` makes sure that the identifier cannot accidentally be captured.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.mkApp "Permalink")def
```


Lean.Syntax.mkApp (fn : [Lean.Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")) (args : [Lean.TSyntaxArray](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntaxArray "Documentation for Lean.TSyntaxArray") `term) :
  [Lean.Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")


Lean.Syntax.mkApp (fn : [Lean.Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term"))
  (args : [Lean.TSyntaxArray](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntaxArray "Documentation for Lean.TSyntaxArray") `term) :
  [Lean.Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")


```

Creates syntax representing a Lean term application, but avoids degenerate empty applications.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.mkCApp "Permalink")def
```


Lean.Syntax.mkCApp (fn : Lean.Name) (args : [Lean.TSyntaxArray](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntaxArray "Documentation for Lean.TSyntaxArray") `term) :
  [Lean.Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")


Lean.Syntax.mkCApp (fn : Lean.Name)
  (args : [Lean.TSyntaxArray](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntaxArray "Documentation for Lean.TSyntaxArray") `term) :
  [Lean.Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")


```

Creates syntax representing a Lean constant application, but avoids degenerate empty applications.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.mkLit "Permalink")def
```


Lean.Syntax.mkLit (kind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind")) (val : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (info : [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo") := [Lean.SourceInfo.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none")) : [Lean.TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") kind


Lean.Syntax.mkLit
  (kind : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind"))
  (val : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (info : [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo") :=
    [Lean.SourceInfo.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none")) :
  [Lean.TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") kind


```

Creates a literal of the given kind. It is the caller's responsibility to ensure that the provided literal is a valid atom for the provided kind.
If `info` is provided, then the literal's source information is copied from it.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.mkCharLit "Permalink")def
```


Lean.Syntax.mkCharLit (val : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))
  (info : [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo") := [Lean.SourceInfo.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none")) : [Lean.CharLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___CharLit "Documentation for Lean.Syntax.CharLit")


Lean.Syntax.mkCharLit (val : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))
  (info : [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo") :=
    [Lean.SourceInfo.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none")) :
  [Lean.CharLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___CharLit "Documentation for Lean.Syntax.CharLit")


```

Creates literal syntax for the given character.
If `info` is provided, then the literal's source information is copied from it.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.mkStrLit "Permalink")def
```


Lean.Syntax.mkStrLit (val : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (info : [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo") := [Lean.SourceInfo.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none")) : [Lean.StrLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___StrLit "Documentation for Lean.Syntax.StrLit")


Lean.Syntax.mkStrLit (val : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (info : [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo") :=
    [Lean.SourceInfo.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none")) :
  [Lean.StrLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___StrLit "Documentation for Lean.Syntax.StrLit")


```

Creates literal syntax for the given string.
If `info` is provided, then the literal's source information is copied from it.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.mkNumLit "Permalink")def
```


Lean.Syntax.mkNumLit (val : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (info : [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo") := [Lean.SourceInfo.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none")) : [Lean.NumLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___NumLit "Documentation for Lean.Syntax.NumLit")


Lean.Syntax.mkNumLit (val : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (info : [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo") :=
    [Lean.SourceInfo.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none")) :
  [Lean.NumLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___NumLit "Documentation for Lean.Syntax.NumLit")


```

Creates literal syntax for a number, which is provided as a string. The caller must ensure that the string is a valid token for the `num` token parser.
If `info` is provided, then the literal's source information is copied from it.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.mkNatLit "Permalink")def
```


Lean.Syntax.mkNatLit (val : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (info : [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo") := [Lean.SourceInfo.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none")) : [Lean.NumLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___NumLit "Documentation for Lean.Syntax.NumLit")


Lean.Syntax.mkNatLit (val : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (info : [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo") :=
    [Lean.SourceInfo.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none")) :
  [Lean.NumLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___NumLit "Documentation for Lean.Syntax.NumLit")


```

Creates literal syntax for a natural number.
If `info` is provided, then the literal's source information is copied from it.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.mkScientificLit "Permalink")def
```


Lean.Syntax.mkScientificLit (val : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (info : [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo") := [Lean.SourceInfo.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none")) :
  [Lean.TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") [Lean.scientificLitKind](Notations-and-Macros/Defining-New-Syntax/#Lean___scientificLitKind "Documentation for Lean.scientificLitKind")


Lean.Syntax.mkScientificLit (val : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (info : [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo") :=
    [Lean.SourceInfo.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none")) :
  [Lean.TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") [Lean.scientificLitKind](Notations-and-Macros/Defining-New-Syntax/#Lean___scientificLitKind "Documentation for Lean.scientificLitKind")


```

Creates literal syntax for a number in scientific notation. The caller must ensure that the provided string is a valid scientific notation literal.
If `info` is provided, then the literal's source information is copied from it.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Syntax.mkNameLit "Permalink")def
```


Lean.Syntax.mkNameLit (val : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (info : [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo") := [Lean.SourceInfo.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none")) : [Lean.NameLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___NameLit "Documentation for Lean.Syntax.NameLit")


Lean.Syntax.mkNameLit (val : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (info : [Lean.SourceInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo") :=
    [Lean.SourceInfo.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none")) :
  [Lean.NameLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___NameLit "Documentation for Lean.Syntax.NameLit")


```

Creates literal syntax for a name. The caller must ensure that the provided string is a valid name literal.
If `info` is provided, then the literal's source information is copied from it.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.mkOptionalNode "Permalink")def
```


Lean.mkOptionalNode (arg : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")) : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")


Lean.mkOptionalNode
  (arg : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")) : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")


```

Creates an optional node.
Optional nodes consist of null nodes that contain either zero or one element.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.mkGroupNode "Permalink")def
```


Lean.mkGroupNode (args : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax") := [#[](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")[]](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")) : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")


Lean.mkGroupNode
  (args : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax") := [#[](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")[]](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")) :
  [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")


```

Creates a group node, as if it were parsed by `Lean.Parser.group`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.mkHole "Permalink")def
```


Lean.mkHole (ref : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")) (canonical : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [Lean.Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")


Lean.mkHole (ref : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax"))
  (canonical : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : [Lean.Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term")


```

Creates a hole (`_`). The hole's position is copied from `ref`.
###  23.4.9.1. Quoting Data[🔗](find/?domain=Verso.Genre.Manual.section&name=quote-class "Permalink")
The `[Quote](Notations-and-Macros/Defining-New-Syntax/#Lean___Quote___mk "Documentation for Lean.Quote")` class allows values to be converted into typed syntax that represents them. For example, `[quote](Notations-and-Macros/Defining-New-Syntax/#Lean___Quote___mk "Documentation for Lean.Quote.quote") 5` represents `⟨[.node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node") [.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none") `num #[[.atom](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.atom") [.none](Notations-and-Macros/Defining-New-Syntax/#Lean___SourceInfo___original "Documentation for Lean.SourceInfo.none") "5"]⟩`. The class is parameterized over syntax kinds; this allows the same value to be represented appropriately at different kinds. Instance resolution for `[Quote](Notations-and-Macros/Defining-New-Syntax/#Lean___Quote___mk "Documentation for Lean.Quote")` takes typed syntax [coercions](Coercions/#--tech-term-coercion) into account. The syntax kind's default value is ``term`.
There is no guarantee that the result of `[Quote.quote](Notations-and-Macros/Defining-New-Syntax/#Lean___Quote___mk "Documentation for Lean.Quote.quote")` will successfully elaborate. Generally speaking, the resulting syntax contains quoted versions of all explicit arguments and omits implicit arguments.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Quote "Permalink")type class
```


Lean.Quote (α : Type) (k : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind") := `term) : Type


Lean.Quote (α : Type)
  (k : [Lean.SyntaxNodeKind](Notations-and-Macros/Defining-New-Syntax/#Lean___SyntaxNodeKind "Documentation for Lean.SyntaxNodeKind") := `term) :
  Type


```

Converts a runtime value into surface syntax that denotes it.
Instances do not need to guarantee that the resulting syntax will always re-elaborate into an equivalent value. For example, the syntax may omit implicit arguments that can usually be found automatically.
#  Instance Constructor

```
[Lean.Quote.mk](Notations-and-Macros/Defining-New-Syntax/#Lean___Quote___mk "Documentation for Lean.Quote.mk")
```

#  Methods

```
quote : α → [Lean.TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") k
```

Returns syntax for the given value.
When defining instances of `[Quote](Notations-and-Macros/Defining-New-Syntax/#Lean___Quote___mk "Documentation for Lean.Quote")`, use `[mkCIdent](Notations-and-Macros/Defining-New-Syntax/#Lean___mkCIdent "Documentation for Lean.mkCIdent")` and `[mkCApp](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___mkCApp "Documentation for Lean.Syntax.mkCApp")` to avoid variable capture in the generated syntax.
Defining `Quote` Instances
To quote a tree of type `[Tree](Notations-and-Macros/Defining-New-Syntax/#Tree-_LPAR_in-Defining--Quote--Instances_RPAR_ "Definition of example")`, `[mkCIdent](Notations-and-Macros/Defining-New-Syntax/#Lean___mkCIdent "Documentation for Lean.mkCIdent")` and `[mkCApp](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___mkCApp "Documentation for Lean.Syntax.mkCApp")` are used to ensure that local bindings with similar names cannot interfere. Using double backticks ensures that the constructor names don't contain typos and are correctly resolved.
`inductive Tree (α : Type u) : Type u where   | leaf   | branch (left : [Tree](Notations-and-Macros/Defining-New-Syntax/#Tree-_LPAR_in-Defining--Quote--Instances_RPAR_ "Definition of example") α) (val : α) (right : [Tree](Notations-and-Macros/Defining-New-Syntax/#Tree-_LPAR_in-Defining--Quote--Instances_RPAR_ "Definition of example") α)  instance [[Quote](Notations-and-Macros/Defining-New-Syntax/#Lean___Quote___mk "Documentation for Lean.Quote") α] : [Quote](Notations-and-Macros/Defining-New-Syntax/#Lean___Quote___mk "Documentation for Lean.Quote") ([Tree](Notations-and-Macros/Defining-New-Syntax/#Tree-_LPAR_in-Defining--Quote--Instances_RPAR_ "Definition of example") α) where   [quote](Notations-and-Macros/Defining-New-Syntax/#Lean___Quote___mk "Documentation for Lean.Quote.quote") := [quoteTree](Notations-and-Macros/Defining-New-Syntax/#instQuoteTreeMkStr1___quoteTree-_LPAR_in-Defining--Quote--Instances_RPAR_ "Definition of example") where   quoteTree     | [.leaf](Notations-and-Macros/Defining-New-Syntax/#Tree___leaf-_LPAR_in-Defining--Quote--Instances_RPAR_ "Definition of example") =>       [mkCIdent](Notations-and-Macros/Defining-New-Syntax/#Lean___mkCIdent "Documentation for Lean.mkCIdent") ``[Tree.leaf](Notations-and-Macros/Defining-New-Syntax/#Tree___leaf-_LPAR_in-Defining--Quote--Instances_RPAR_ "Definition of example")     | [.branch](Notations-and-Macros/Defining-New-Syntax/#Tree___branch-_LPAR_in-Defining--Quote--Instances_RPAR_ "Definition of example") l v r =>       [mkCApp](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___mkCApp "Documentation for Lean.Syntax.mkCApp") ``[Tree.branch](Notations-and-Macros/Defining-New-Syntax/#Tree___branch-_LPAR_in-Defining--Quote--Instances_RPAR_ "Definition of example") #[[quoteTree](Notations-and-Macros/Defining-New-Syntax/#instQuoteTreeMkStr1___quoteTree-_LPAR_in-Defining--Quote--Instances_RPAR_ "Definition of example") l, [quote](Notations-and-Macros/Defining-New-Syntax/#Lean___Quote___mk "Documentation for Lean.Quote.quote") v, [quoteTree](Notations-and-Macros/Defining-New-Syntax/#instQuoteTreeMkStr1___quoteTree-_LPAR_in-Defining--Quote--Instances_RPAR_ "Definition of example") r] `
[Live ↪](javascript:openLiveLink\("PYBwpgdgBAMmCG0DKBPCAXeAPAUDglhACYCuAxuvgG5hQAqATmLQBSCNwFAFz0rhQkBKLjz4koAdwAWYJjihQAPlAA2CAGZzFUAEYNEZSVBaq16YY2ZQ2QllXjLh1ow3wBzSWe4Xa1vIQDOmBBktADaAIokwOg+ALrCkdGs3lZCUjJgmgCOUTFcALxQOUneOOmy8sUxpfLySgB0qvBqUPkAfJq1UAC2ANYAwgCSRJBmAAZj3o3qnVr1uvqGDlRQDK0dXfJ9/QCCICBQE1MLwYYAxKFVYCnKADRFubRU91cpDLFAA"\))
##  23.4.10. Decoding Typed Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=typed-syntax-helpers "Permalink")
For literals, Lean's parser produces a singleton node that contains an `[atom](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.atom")`. The inner atom contains a string with source information, while the node's kind specifies how the atom is to be interpreted. This may involve decoding string escape sequences or interpreting base-16 numeric literals. The helpers in this section perform the correct interpretation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.TSyntax.getId "Permalink")def
```


Lean.TSyntax.getId (s : [Lean.Ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Ident "Documentation for Lean.Syntax.Ident")) : Lean.Name


Lean.TSyntax.getId (s : [Lean.Ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Ident "Documentation for Lean.Syntax.Ident")) :
  Lean.Name


```

Extracts the parsed name from the syntax of an identifier.
Returns `Name.anonymous` if the syntax is malformed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.TSyntax.getName "Permalink")def
```


Lean.TSyntax.getName (s : [Lean.NameLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___NameLit "Documentation for Lean.Syntax.NameLit")) : Lean.Name


Lean.TSyntax.getName (s : [Lean.NameLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___NameLit "Documentation for Lean.Syntax.NameLit")) :
  Lean.Name


```

Decodes a quoted name literal, returning the name.
Returns `Lean.Name.anonymous` if the syntax is malformed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.TSyntax.getNat "Permalink")def
```


Lean.TSyntax.getNat (s : [Lean.NumLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___NumLit "Documentation for Lean.Syntax.NumLit")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Lean.TSyntax.getNat (s : [Lean.NumLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___NumLit "Documentation for Lean.Syntax.NumLit")) :
  [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Interprets a numeric literal as a natural number.
Returns `0` if the syntax is malformed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.TSyntax.getScientific "Permalink")def
```


Lean.TSyntax.getScientific (s : [Lean.ScientificLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___ScientificLit "Documentation for Lean.Syntax.ScientificLit")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Lean.TSyntax.getScientific
  (s : [Lean.ScientificLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___ScientificLit "Documentation for Lean.Syntax.ScientificLit")) :
  [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Extracts the components of a scientific numeric literal.
Returns a triple `(n, sign, e) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") × [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") × [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`; the number's value is given by:
`[if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") sign [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n * 10 ^ (-e) [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n * 10 ^ e`
Returns `(0, [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false"), 0)` if the syntax is malformed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.TSyntax.getString "Permalink")def
```


Lean.TSyntax.getString (s : [Lean.StrLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___StrLit "Documentation for Lean.Syntax.StrLit")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


Lean.TSyntax.getString (s : [Lean.StrLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___StrLit "Documentation for Lean.Syntax.StrLit")) :
  [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Decodes a string literal, removing quotation marks and unescaping escaped characters.
Returns `""` if the syntax is malformed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.TSyntax.getChar "Permalink")def
```


Lean.TSyntax.getChar (s : [Lean.CharLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___CharLit "Documentation for Lean.Syntax.CharLit")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


Lean.TSyntax.getChar (s : [Lean.CharLit](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___CharLit "Documentation for Lean.Syntax.CharLit")) :
  [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Decodes a character literal.
Returns `([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))` if the syntax is malformed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.TSyntax.getHygieneInfo "Permalink")def
```


Lean.TSyntax.getHygieneInfo (s : [Lean.HygieneInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___HygieneInfo "Documentation for Lean.Syntax.HygieneInfo")) : Lean.Name


Lean.TSyntax.getHygieneInfo
  (s : [Lean.HygieneInfo](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___HygieneInfo "Documentation for Lean.Syntax.HygieneInfo")) : Lean.Name


```

Decodes macro hygiene information.
##  23.4.11. Syntax Categories[🔗](find/?domain=Verso.Genre.Manual.section&name=syntax-categories "Permalink")
Lean's parser contains a table of _syntax categories_ , which correspond to nonterminals in a context-free grammar. Some of the most important categories are terms, commands, universe levels, priorities, precedences, and the categories that represent tokens such as literals. Typically, each [syntax kind](Notations-and-Macros/Defining-New-Syntax/#--tech-term-syntax-kind) corresponds to a category. New categories can be declared using ``Lean.Parser.Command.syntaxCat : command``[`declare_syntax_cat`](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntaxCat).
syntaxDeclaring Syntactic Categories
Declares a new syntactic category.

```
command ::= ...
    | [
A docComment parses a "documentation comment" like /-- foo -/. This is not treated like
a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure.
At parse time, docComment checks the value of the doc.verso option. If it is true, the contents
are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use
plainDocComment to always treat the contents as plain text.
A plain text doc comment node contains a /-- atom and then the remainder of the comment, foo -/
in this example. Use TSyntax.getDocString to extract the body text from a doc string syntax node.
A Verso comment node contains the /-- atom, the document's syntax tree, and a closing -/ atom.
docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)?
      declare_syntax_cat ident ((behavior := (catBehaviorBoth | catBehaviorSymbol)))?
```

The leading identifier behavior is an advanced feature that usually does not need to be modified. It controls the behavior of the parser when it encounters an identifier, and can sometimes cause the identifier to be treated as a non-reserved keyword instead. This is used to avoid turning the name of every [tactic](Tactic-Proofs/#tactics) into a reserved keyword.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Parser.LeadingIdentBehavior.default "Permalink")inductive type
```


Lean.Parser.LeadingIdentBehavior : Type


Lean.Parser.LeadingIdentBehavior : Type


```

Specifies how the parsing table lookup function behaves for identifiers.
The function `Lean.Parser.prattParser` uses two tables: one each for leading and trailing parsers. These tables map tokens to parsers. Because keyword tokens are distinct from identifier tokens, keywords and identifiers cannot be confused, even when they are syntactically identical. Specifying an alternative leading identifier behavior allows greater flexibility and makes it possible to avoid reserved keywords in some situations.
When the leading token is syntactically an identifier, the current syntax category's `LeadingIdentBehavior` specifies how the parsing table lookup function behaves, and allows controlled “punning” between identifiers and keywords. This feature is used to avoid creating a reserved symbol for each built-in tactic (e.g., `[apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic")` or `[assumption](Tactic-Proofs/Tactic-Reference/#assumption "Documentation for tactic")`). As a result, tactic names can be used as identifiers.
#  Constructors

```
default : [Lean.Parser.LeadingIdentBehavior](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___LeadingIdentBehavior___default "Documentation for Lean.Parser.LeadingIdentBehavior")
```

If the leading token is an identifier, then the parser just executes the parsers associated with the auxiliary token “ident”, which parses identifiers.

```
symbol : [Lean.Parser.LeadingIdentBehavior](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___LeadingIdentBehavior___default "Documentation for Lean.Parser.LeadingIdentBehavior")
```

If the leading token is an identifier `<foo>`, and there are parsers `P` associated with the token `<foo>`, then the parser executes `P`. Otherwise, it executes only the parsers associated with the auxiliary token “ident”, which parses identifiers.

```
both : [Lean.Parser.LeadingIdentBehavior](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___LeadingIdentBehavior___default "Documentation for Lean.Parser.LeadingIdentBehavior")
```

If the leading token is an identifier `<foo>`, then it executes the parsers associated with token `<foo>` and parsers associated with the auxiliary token “ident”, which parses identifiers.
##  23.4.12. Syntax Rules[🔗](find/?domain=Verso.Genre.Manual.section&name=syntax-rules "Permalink")
Each [syntax category](Notations-and-Macros/Defining-New-Syntax/#--tech-term-syntax-categories) is associated with a set of _syntax rules_ , which correspond to productions in a context-free grammar. Syntax rules can be defined using the ``Lean.Parser.Command.syntax : command``[`syntax`](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax) command.
syntaxSyntax Rules

```
command ::= ...
    | [
A docComment parses a "documentation comment" like /-- foo -/. This is not treated like
a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure.
At parse time, docComment checks the value of the doc.verso option. If it is true, the contents
are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use
plainDocComment to always treat the contents as plain text.
A plain text doc comment node contains a /-- atom and then the remainder of the comment, foo -/
in this example. Use TSyntax.getDocString to extract the body text from a doc string syntax node.
A Verso comment node contains the /-- atom, the document's syntax tree, and a closing -/ atom.
docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)?
      [attributes](Attributes/#Lean___Parser___Term___attributes-next)?
      


attrKind matches ("scoped" <|> "local")?, used before an attribute like @[local simp]. 


attrKind
      syntax(:prec)? ((name := ident))? ((priority := prio))? 


p* is shorthand for many(p). It uses parser p 0 or more times, and produces a
nullNode containing the array of parsed results. This parser has arity 1.


If p has arity more than 1, it is auto-grouped in the items generated by the parser.


stx[*](Notations-and-Macros/Defining-New-Syntax/#_FLQQ_stx_____FLQQ_) : ident
```

As with operator and notation declarations, the contents of the documentation comments are shown to users while they interact with the new syntax. Attributes may be added to invoke compile-time metaprograms on the resulting definition.
Syntax rules interact with [section scopes](Namespaces-and-Sections/#--tech-term-section-scope) in the same manner as attributes, operators, and notations. By default, syntax rules are available to the parser in any module that transitively imports the one in which they are established, but they may be declared `scoped` or `local` to restrict their availability either to contexts in which the current namespace has been opened or to the current [section scope](Namespaces-and-Sections/#--tech-term-section-scope), respectively.
When multiple syntax rules for a category can match the current input, the [local longest-match rule](Notations-and-Macros/Custom-Operators/#--tech-term-local-longest-match-rule) is used to select one of them. Like notations and operators, if there is a tie for the longest match then the declared priorities are used to determine which parse result applies. If this still does not resolve the ambiguity, then all the results that tied are saved. The elaborator is expected to attempt all of them, succeeding when exactly one can be elaborated.
The syntax rule's precedence, written immediately after the ``Lean.Parser.Command.syntax : command``[`syntax`](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax) keyword, restricts the parser to use this new syntax only when the precedence context is at least the provided value. Just as with operators and notations, syntax rules may be manually provided with a name; if they are not, an otherwise-unused name is generated. Whether provided or generated, this name is used as the syntax kind in the resulting `[node](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax.node")`.
The body of a syntax declaration is even more flexible than that of a notation. String literals specify atoms to match. Subterms may be drawn from any syntax category, rather than just terms, and they may be optional or repeated, with or without interleaved comma separators. Identifiers in syntax rules indicate syntax categories, rather than naming subterms as they do in notations.
Finally, the syntax rule specifies which syntax category it extends. It is an error to declare a syntax rule in a nonexistent category.
syntaxSyntax Specifiers
The syntactic category `stx` is the grammar of specifiers that may occur in the body of a ``Lean.Parser.Command.syntax : command``[`syntax`](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax) command.
String literals are parsed as [atoms](Notations-and-Macros/Defining-New-Syntax/#--tech-term-Atoms) (including both keywords such as `if`, `#eval`, or `where`):

```
stx ::=
    


Parses the literal symbol.


The symbol is automatically included in the set of reserved tokens ("keywords").
Keywords cannot be used as identifiers, unless the identifier is otherwise escaped.
For example, "fun" reserves fun as a keyword; to refer an identifier named fun one can write «fun».
Adding a & prefix prevents it from being reserved, for example &"true".


Whitespace before or after the atom is used as a pretty printing hint.
For example, " + " parses + and pretty prints it with whitespace on both sides.
The whitespace has no effect on parsing behavior.


str
```

Leading and trailing spaces in the strings do not affect parsing, but they cause Lean to insert spaces in the corresponding position when displaying the syntax in [proof states](Tactic-Proofs/#--tech-term-proof-state) and error messages. Ordinarily, valid identifiers occurring as atoms in syntax rules become reserved keywords. Preceding a string literal with an ampersand (`&`) suppresses this behavior:

```
stx ::= ...
    | 


Parses a literal symbol. The & prefix prevents it from being included in the set of reserved tokens ("keywords").
This means that the symbol can still be recognized as an identifier by other parsers.


Some syntax categories, such as tactic, automatically apply & to the first symbol.


Whitespace before or after the atom is used as a pretty printing hint.
For example, " + " parses + and pretty prints it with whitespace on both sides.
The whitespace has no effect on parsing behavior.


(Not exposed by parser description syntax:
If the includeIdent argument is true, lets ident be reinterpreted as atom if it matches.)


&str
```

Identifiers specify the syntactic category expected in a given position, and may optionally provide a precedence:

```
stx ::= ...
    | ident(:prec)?
```

The `*` modifier is the Kleene star, matching zero or more repetitions of the preceding syntax. It can also be written using `many`.

```
stx ::= ...
    | 


p* is shorthand for many(p). It uses parser p 0 or more times, and produces a
nullNode containing the array of parsed results. This parser has arity 1.


If p has arity more than 1, it is auto-grouped in the items generated by the parser.


stx *
```

The `+` modifier matches one or more repetitions of the preceding syntax. It can also be written using `many1`.

```
stx ::= ...
    | 


p+ is shorthand for many1(p). It uses parser p 1 or more times, and produces a
nullNode containing the array of parsed results. This parser has arity 1.


If p has arity more than 1, it is auto-grouped in the items generated by the parser.


stx +
```

The `?` modifier makes a subterm optional, and matches zero or one, but not more, repetitions of the preceding syntax. It can also be written as `optional`.

```
stx ::= ...
    | 


(p)? is shorthand for optional(p). It uses parser p 0 or 1 times, and produces a
nullNode containing the array of parsed results. This parser has arity 1.


p is allowed to have arity n > 1 (in which case the node will have either 0 or n children),
but if it has arity 0 then the result will be ambiguous.


Because ? is an identifier character, ident? will not work as intended.
You have to write either ident ? or (ident)? for it to parse as the ? combinator
applied to the ident parser.


stx ?
```

```
stx ::= ...
    | optional(stx)
```

The `,*` modifier matches zero or more repetitions of the preceding syntax with interleaved commas. It can also be written using `sepBy`.

```
stx ::= ...
    | 


p,* is shorthand for sepBy(p, ","). It parses 0 or more occurrences of
p separated by ,, that is: empty | p | p,p | p,p,p | ....


It produces a nullNode containing a SepArray with the interleaved parser
results. It has arity 1, and auto-groups its component parser if needed.


stx ,*
```

The `,+` modifier matches one or more repetitions of the preceding syntax with interleaved commas. It can also be written using `sepBy1`.

```
stx ::= ...
    | 


p,+ is shorthand for sepBy1(p, ","). It parses 1 or more occurrences of
p separated by ,, that is: p | p,p | p,p,p | ....


It produces a nullNode containing a SepArray with the interleaved parser
results. It has arity 1, and auto-groups its component parser if needed.


stx ,+
```

The `,*,?` modifier matches zero or more repetitions of the preceding syntax with interleaved commas, allowing an optional trailing comma after the final repetition. It can also be written using `sepBy` with the `allowTrailingSep` modifier.

```
stx ::= ...
    | 


p,*,? is shorthand for sepBy(p, ",", allowTrailingSep).
It parses 0 or more occurrences of p separated by ,, possibly including
a trailing ,, that is: empty | p | p, | p,p | p,p, | p,p,p | ....


It produces a nullNode containing a SepArray with the interleaved parser
results. It has arity 1, and auto-groups its component parser if needed.


stx ,*,?
```

The `,+,?` modifier matches one or more repetitions of the preceding syntax with interleaved commas, allowing an optional trailing comma after the final repetition. It can also be written using `sepBy1` with the `allowTrailingSep` modifier.

```
stx ::= ...
    | 


p,+,? is shorthand for sepBy1(p, ",", allowTrailingSep).
It parses 1 or more occurrences of p separated by ,, possibly including
a trailing ,, that is: p | p, | p,p | p,p, | p,p,p | ....


It produces a nullNode containing a SepArray with the interleaved parser
results. It has arity 1, and auto-groups its component parser if needed.


stx ,+,?
```

The `<|>` operator, which can be written `orelse`, matches either syntax. However, if the first branch consumes any tokens, then it is committed to, and failures will not be backtracked:

```
stx ::= ...
    | 


p1 <|> p2 is shorthand for orelse(p1, p2), and parses either p1 or p2.
It does not backtrack, meaning that if p1 consumes at least one token then
p2 will not be tried. Therefore, the parsers should all differ in their first
token. The atomic(p) parser combinator can be used to locally backtrack a parser.
(For full backtracking, consider using extensible syntax classes instead.)


On success, if the inner parser does not generate exactly one node, it will be
automatically wrapped in a group node, so the result will always be arity 1.


The <|> combinator does not generate a node of its own, and in particular
does not tag the inner parsers to distinguish them, which can present a problem
when reconstructing the parse. A well formed <|> parser should use disjoint
node kinds for p1 and p2.


stx <|> stx
```

```
stx ::= ...
    | orelse(stx, stx)
```

The `!` operator matches the complement of its argument. If its argument fails, then it succeeds, resetting the parsing state.

```
stx ::= ...
    | 


!p parses the negation of p. That is, it fails if p succeeds, and
otherwise parses nothing. It has arity 0.


! stx
```

Syntax specifiers may be grouped using parentheses.

```
stx ::= ...
    | (stx)
```

Repetitions may be defined using `many` and `many1`. The latter requires at least one instance of the repeated syntax.

```
stx ::= ...
    | many(stx)
```

```
stx ::= ...
    | many1(stx)
```

Repetitions with separators may be defined using `sepBy` and `sepBy1`, which respectively match zero or more occurrences and one or more occurrences, separated by some other syntax. They come in three varieties:
  * The two-parameter version uses the atom provided in the string literal to parse the separators, and does not allow trailing separators.
  * The three-parameter version uses the third parameter to parse the separators, using the atom for pretty-printing.
  * The four-parameter version optionally allows the separator to occur an extra time at the end of the sequence. The fourth argument must always literally be the keyword `allowTrailingSep`.


```
stx ::= ...
    | sepBy(stx, str)
```

```
stx ::= ...
    | sepBy(stx, str, stx)
```

```
stx ::= ...
    | sepBy(stx, str, stx, allowTrailingSep)
```

```
stx ::= ...
    | sepBy1(stx, str)
```

```
stx ::= ...
    | sepBy1(stx, str, stx)
```

```
stx ::= ...
    | sepBy1(stx, str, stx, allowTrailingSep)
```

Parsing Matched Parentheses and Brackets
A language that consists of matched parentheses and brackets can be defined using syntax rules. The first step is to declare a new [syntax category](Notations-and-Macros/Defining-New-Syntax/#--tech-term-syntax-categories):
`[declare_syntax_cat](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntaxCat "Documentation for syntax") balanced `
Next, rules can be added for parentheses and square brackets. To rule out empty strings, the base cases consist of empty pairs.
`[syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") "(" ")" : [balanced](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Category___balanced-_LPAR_in-Parsing-Matched-Parentheses-and-Brackets_RPAR_ "Definition of example") [syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") "[" "]" : [balanced](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Category___balanced-_LPAR_in-Parsing-Matched-Parentheses-and-Brackets_RPAR_ "Definition of example") [syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") "(" [balanced](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Category___balanced-_LPAR_in-Parsing-Matched-Parentheses-and-Brackets_RPAR_ "Definition of example") ")" : [balanced](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Category___balanced-_LPAR_in-Parsing-Matched-Parentheses-and-Brackets_RPAR_ "Definition of example") [syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") "[" [balanced](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Category___balanced-_LPAR_in-Parsing-Matched-Parentheses-and-Brackets_RPAR_ "Definition of example") "]" : [balanced](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Category___balanced-_LPAR_in-Parsing-Matched-Parentheses-and-Brackets_RPAR_ "Definition of example") [syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") [balanced](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Category___balanced-_LPAR_in-Parsing-Matched-Parentheses-and-Brackets_RPAR_ "Definition of example") [balanced](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Category___balanced-_LPAR_in-Parsing-Matched-Parentheses-and-Brackets_RPAR_ "Definition of example") : [balanced](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Category___balanced-_LPAR_in-Parsing-Matched-Parentheses-and-Brackets_RPAR_ "Definition of example") `
In order to invoke Lean's parser on these rules, there must also be an embedding from the new syntax category into one that may already be parsed:
`[syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") (name := termBalanced) "balanced " [balanced](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Category___balanced-_LPAR_in-Parsing-Matched-Parentheses-and-Brackets_RPAR_ "Definition of example") : term `
These terms cannot be elaborated, but reaching an elaboration error indicates that parsing succeeded:
`/-- error: elaboration function for `termBalanced` has not been implemented   balanced () -/ [#guard_msgs](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax") [in](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax") example := balanced ()  /-- error: elaboration function for `termBalanced` has not been implemented   balanced [] -/ [#guard_msgs](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax") [in](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax") example := balanced []  /-- error: elaboration function for `termBalanced` has not been implemented   balanced [[]()([])] -/ [#guard_msgs](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax") [in](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax") example := balanced [[] () ([])] `
Similarly, parsing fails when they are mismatched:

```
example := balanced [() (unexpected token ']'; expected ')' or balanced]]
```

```
<example>:1:25-1:26: unexpected token ']'; expected ')' or balanced
```

[Live ↪](javascript:openLiveLink\("CYUwxgNghgTiD6BnAngOwC5QB7zFdABAEZTSpgjABQVKG2BARABSNMCUbAXMaVOZVppMWJgG02jALrdeZCtToimrOfwUdZJeYKUNGEtQOBMZBHtvW7hDS8aMaLfYzT2jmqKAFsQ5gLwE6CAwXgBCzgrsTHYabDGU5oHBXjQA9AC06VTBMAD2MDwg0ET5+ACWuagEAGYAruToFVXV+QQABkEh4TrAbQQAFlCIBKi5hEQgIFVlXgAOECA+GIIEDgnM7FTpqVQAxADmtbDA8F6I+8NlqNlY3vO+XAHxJhtpmdkweQUERVAlMOVKjV6mBGkCWjB2p0whFKH1BsNRuNJtM5gslkFqKtngQxFItjsDkcYCczhcCFcbncFv41iY8W8sjl8oViqUwc0QRyaq0OslulZegMhiMxsQURS0YsppiqNjYfS8RtmHj2PjtntDsdTudLtcQLcpbScWI8QQNubVVIgA"\))
Parsing Comma-Separated Repetitions
A variant of list literals that requires double square brackets and allows a trailing comma can be added with the following syntax:
`[syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") "[[" term,*,? "]]" : term `
Adding a [macro](Notations-and-Macros/Macros/#--tech-term-Macros) that describes how to translate it into an ordinary list literal allows it to be used in tests.
`[macro_rules](Notations-and-Macros/Macros/#Lean___Parser___Command___macro_rules "Documentation for syntax")   | `(term|[[$e:term,*]]) => `([$e,*]) ```[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")"Dandelion"[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") "Thistle"[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [["Dandelion", "Thistle",]] `
```
[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")"Dandelion"[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") "Thistle"[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
```

[Live ↪](javascript:openLiveLink\("M4TwdgLghgHgBAIgNpIXCBTATgWwDQBUeA/IgLploBc62OAUPTlAMZYD2A+lgK4A2GYPThwAPnAAGACky5RKACQYqs/AQoBKOAF4AfJKlIlhMhsYBiDADcofOCgQARKGAAmGPgEt2YBHkQAKgAWnsAQAn4UQA"\))
##  23.4.13. Indentation[🔗](find/?domain=Verso.Genre.Manual.section&name=syntax-indentation "Permalink")
Internally, the parser maintains a saved source position. Syntax rules may include instructions that interact with these saved positions, causing parsing to fail when a condition is not met. Indentation-sensitive constructs, such as ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do), save a source position, parse their constituent parts while taking this saved position into account, and then restore the original position.
In particular, Indentation-sensitvity is specified by combining `withPosition` or `withPositionAfterLinebreak`, which save the source position at the start of parsing some other syntax, with `colGt`, `colGe`, and `colEq`, which compare the current column with the column from the most recently-saved position. `lineEq` can also be used to ensure that two positions are on the same line in the source file.
[🔗](find/?domain=Manual.parserAlias&name=withPosition "Permalink")parser alias
```
withPosition(p)
```

Arity is sum of arguments' arities
`withPosition(p)` runs `p` while setting the "saved position" to the current position. This has no effect on its own, but various other parsers access this position to achieve some composite effect:
  * `colGt`, `colGe`, `colEq` compare the column of the saved position to the current position, used to implement Python-style indentation sensitive blocks
  * `lineEq` ensures that the current position is still on the same line as the saved position, used to implement composite tokens


The saved position is only available in the read-only state, which is why this is a scoping parser: after the `withPosition(..)` block the saved position will be restored to its original value.
This parser has the same arity as `p` - it just forwards the results of `p`.
[🔗](find/?domain=Manual.parserAlias&name=withoutPosition "Permalink")parser alias
```
withoutPosition(p)
```

Arity is sum of arguments' arities
`withoutPosition(p)` runs `p` without the saved position, meaning that position-checking parsers like `colGt` will have no effect. This is usually used by bracketing constructs like `(...)` so that the user can locally override whitespace sensitivity.
This parser has the same arity as `p` - it just forwards the results of `p`.
[🔗](find/?domain=Manual.parserAlias&name=withPositionAfterLinebreak "Permalink")parser alias
```
withPositionAfterLinebreak
```

  * Arity: 1
  * Automatically wraps arguments in a `null` node unless there's exactly one


[🔗](find/?domain=Manual.parserAlias&name=colGt "Permalink")parser alias
```
colGt
```

  * Arity: 0
  * Automatically wraps arguments in a `null` node unless there's exactly one


The `colGt` parser requires that the next token starts a strictly greater column than the saved position (see `withPosition`). This can be used for whitespace sensitive syntax for the arguments to a tactic, to ensure that the following tactic is not interpreted as an argument.

```
example (x : False) : False := by
  revert x
  exact id

```

Here, the `revert` tactic is followed by a list of `colGt ident`, because otherwise it would interpret `exact` as an identifier and try to revert a variable named `exact`.
This parser has arity 0 - it does not capture anything.
[🔗](find/?domain=Manual.parserAlias&name=colGe "Permalink")parser alias
```
colGe
```

  * Arity: 0
  * Automatically wraps arguments in a `null` node unless there's exactly one


The `colGe` parser requires that the next token starts from at least the column of the saved position (see `withPosition`), but allows it to be more indented. This can be used for whitespace sensitive syntax to ensure that a block does not go outside a certain indentation scope. For example it is used in the lean grammar for `else if`, to ensure that the `else` is not less indented than the `if` it matches with.
This parser has arity 0 - it does not capture anything.
[🔗](find/?domain=Manual.parserAlias&name=colEq "Permalink")parser alias
```
colEq
```

  * Arity: 0
  * Automatically wraps arguments in a `null` node unless there's exactly one


The `colEq` parser ensures that the next token starts at exactly the column of the saved position (see `withPosition`). This can be used to do whitespace sensitive syntax like a `by` block or `do` block, where all the lines have to line up.
This parser has arity 0 - it does not capture anything.
[🔗](find/?domain=Manual.parserAlias&name=lineEq "Permalink")parser alias
```
lineEq
```

  * Arity: 0
  * Automatically wraps arguments in a `null` node unless there's exactly one


The `lineEq` parser requires that the current token is on the same line as the saved position (see `withPosition`). This can be used to ensure that composite tokens are not "broken up" across different lines. For example, `else if` is parsed using `lineEq` to ensure that the two tokens are on the same line.
This parser has arity 0 - it does not capture anything.
Aligned Columns
This syntax for saving notes takes a bulleted list of items, each of which must be aligned at the same column.
`[syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Parser___Command___syntax "Documentation for syntax") "note " ppLine withPosition((colEq "◦ " str ppLine)+) : term `
There is no elaborator or macro associated with this syntax, but the following example is accepted by the parser:
`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax")   `elaboration function for `«termNote__◦__»` has not been implemented   note     ◦ "One"     ◦ "Two"     `note ◦ "One" ◦ "Two" `
```
elaboration function for `«termNote__◦__»` has not been implemented
  note
    ◦ "One"
    ◦ "Two"
    
```

The syntax does not require that the list is indented with respect to the opening token, which would require an extra `withPosition` and a `colGt`.
`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax")   `elaboration function for `«termNote__◦__»` has not been implemented   note     ◦ "One"     ◦ "Two"     `note ◦ "One" ◦ "Two" `
```
elaboration function for `«termNote__◦__»` has not been implemented
  note
    ◦ "One"
    ◦ "Two"
    
```

The following examples are not syntactically valid because the columns of the bullet points do not match.

```
#check  note    ◦ "One"   expected end of input◦ "Two"
```

```
<example>:4:3-4:4: expected end of input
```

```
#check  note   ◦ "One"     expected end of input◦ "Two"
```

```
<example>:4:5-4:6: expected end of input
```

[Live ↪](javascript:openLiveLink\("M4TwdgLghgHgBAIjAewgU0XADlgMgSzAwHd8IALABWWDP2TAApGBjZAGwFEBHRQM9JMwCACdseQmgCUAaklwAXHHTCAtkA"\))
[←23.3. Notations](Notations-and-Macros/Notations/#notations "23.3. Notations")[23.5. Macros→](Notations-and-Macros/Macros/#macros "23.5. Macros")

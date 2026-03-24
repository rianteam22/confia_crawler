[←8. Axioms](Axioms/#axioms "8. Axioms")[10. Type Classes→](Type-Classes/#type-classes "10. Type Classes")
#  9. Attributes[🔗](find/?domain=Verso.Genre.Manual.section&name=attributes "Permalink")
_Attributes_ are an extensible set of compile-time annotations on declarations. They can be added as a [declaration modifier](Definitions/Modifiers/#declaration-modifiers) or using the ``Lean.Parser.Command.attribute : command``[`attribute`](Attributes/#Lean___Parser___Command___attribute) command.
Attributes can associate information with declarations in compile-time tables (including [custom simp sets](The-Simplifier/Simp-sets/#--tech-term-Custom-simp-sets), [macros](Notations-and-Macros/Macros/#--tech-term-Macros), and [instances](Type-Classes/#--tech-term-instances)), impose additional requirements on definitions (e.g. rejecting them if their type is not a type class), or generate additional code. As with [macros](Notations-and-Macros/Macros/#--tech-term-Macros) and custom [elaborators](Notations-and-Macros/Elaborators/#--tech-term-elaborators) for terms, commands, and tactics, the [syntax category](Notations-and-Macros/Defining-New-Syntax/#--tech-term-syntax-categories) `attr` of attributes is designed to be extended, and there is a table that maps each extension to a compile-time program that interprets it.
Attributes are applied as _attribute instances_ that pair a scope indicator with an attribute. These may occur either in attributes as declaration modifiers or the stand-alone ``Lean.Parser.Command.attribute : command``[`attribute`](Attributes/#Lean___Parser___Command___attribute) command.
syntaxAttribute Instances

```
[attrInstance](Attributes/#Lean___Parser___Term___attrInstance-next) ::= ...
    | 


attrKind matches ("scoped" <|> "local")?, used before an attribute like @[local simp]. 


attrKind attr
```

An `attrKind` is the optional [attribute scope](Attributes/#scoped-attributes) keywords `local` or `scoped`. These control the visibility of the attribute's effects. The attribute itself is anything from the extensible [syntax category](Notations-and-Macros/Defining-New-Syntax/#--tech-term-syntax-categories) `attr`.
The attribute system is very powerful: attributes can associate arbitrary information with declarations and generate any number of helpers. This imposes some design trade-offs: storing this information takes space, and retrieving it takes time. As a result, some attributes can only be applied to a declaration in the module where the declaration is defined. This allows lookups to be much faster in large projects, because they don't need to examine data for all modules. Each attribute determines how to store its own metadata and what the appropriate tradeoff between flexibility and performance is for a given use case.
##  9.1. Attributes as Modifiers[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Attributes--Attributes-as-Modifiers "Permalink")
Attributes can be added to declarations as a [declaration modifier](Definitions/Modifiers/#declaration-modifiers). They are placed between the documentation comment and the visibility modifiers.
syntaxAttributes

```
[attributes](Attributes/#Lean___Parser___Term___attributes-next) ::=
    @[[attrInstance](Attributes/#Lean___Parser___Term___attrInstance-next),*]
```

##  9.2. The `attribute` Command[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Attributes--The--attribute--Command "Permalink")
The ``Lean.Parser.Command.attribute : command``[`attribute`](Attributes/#Lean___Parser___Command___attribute) command can be used to modify a declaration's attributes. Some example uses include:
  * registering a pre-existing declaration as an [instance](Type-Classes/#--tech-term-instances) in the local scope by adding `instance`,
  * marking a pre-existing theorem as a simp lemma or an extensionality lemma, using `simp` or `ext`, and
  * temporarily removing a simp lemma from the default [simp set](The-Simplifier/Simp-sets/#--tech-term-simp-set).


syntaxAttribute Modification
The ``Lean.Parser.Command.attribute : command``[`attribute`](Attributes/#Lean___Parser___Command___attribute) command adds or removes attributes from an existing declaration. The identifier is the name whose attributes are being modified.

```
command ::= ...
    | attribute [([eraseAttr](Attributes/#Lean___Parser___Command___eraseAttr-next) | [attrInstance](Attributes/#Lean___Parser___Term___attrInstance-next)),*] ident
```

In addition to attribute instances that add an attribute to an existing declaration, some attributes can be removed; this is called _erasing_ the attribute. Attributes can be erased by preceding their name with `-`. Not all attributes support erasure, however.
syntaxErasing Attributes
Attributes are erased by preceding their name with a `-`.

```
[eraseAttr](Attributes/#Lean___Parser___Command___eraseAttr-next) ::= ...
    | -ident
```

##  9.3. Scoped Attributes[🔗](find/?domain=Verso.Genre.Manual.section&name=scoped-attributes "Permalink")
Many attributes can be applied in a particular scope. This determines whether the attribute's effect is visible only in the current section scope, in namespaces that open the current namespace, or everywhere. These scope indications are also used to control [syntax extensions](Notations-and-Macros/Defining-New-Syntax/#syntax-rules) and [type class instances](Type-Classes/Instance-Declarations/#instance-attribute). Each attribute is responsible for defining precisely what these terms mean for its particular effect.
syntaxAttribute Scopes
Globally-scoped declarations (the default) are in effect whenever the [module](Source-Files-and-Modules/#--tech-term-module) in which they're established is transitively imported. They are indicated by the absence of another scope modifier.

```
attrKind ::=
    


attrKind matches ("scoped" <|> "local")?, used before an attribute like @[local simp]. 



```

Locally-scoped declarations are in effect only for the extent of the [section scope](Namespaces-and-Sections/#--tech-term-section-scope) in which they are established.

```
attrKind ::= ...
    | 


attrKind matches ("scoped" <|> "local")?, used before an attribute like @[local simp]. 


local
```

Scoped declarations are in effect whenever the [namespace](Namespaces-and-Sections/#--tech-term-current-namespace) in which they are established is opened.

```
attrKind ::= ...
    | 


attrKind matches ("scoped" <|> "local")?, used before an attribute like @[local simp]. 


scoped
```

[←8. Axioms](Axioms/#axioms "8. Axioms")[10. Type Classes→](Type-Classes/#type-classes "10. Type Classes")

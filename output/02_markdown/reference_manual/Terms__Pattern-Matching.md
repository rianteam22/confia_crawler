[←13.7. Conditionals](Terms/Conditionals/#if-then-else "13.7. Conditionals")[13.9. Holes→](Terms/Holes/#The-Lean-Language-Reference--Terms--Holes "13.9. Holes")
#  13.8. Pattern Matching[🔗](find/?domain=Verso.Genre.Manual.section&name=pattern-matching "Permalink")
_Pattern matching_ is a way to recognize and destructure values using a syntax of _patterns_ that are a subset of the terms. A pattern that recognizes and destructures a value is similar to the syntax that would be used to construct the value. One or more _match discriminants_ are simultaneously compared to a series of _match alternatives_. Discriminants may be named. Each alternative contains one or more comma-separated sequences of patterns; all pattern sequences must contain the same number of patterns as there are discriminants. When a pattern sequence matches all of the discriminants, the term following the corresponding ``Lean.Parser.Term.match : term`
Pattern matching. `match e, ... with | p, ... => f | ...` matches each given term `e` against each pattern `p` of a match alternative. When all patterns of an alternative match, the `match` term evaluates to the value of the corresponding right-hand side `f` with the pattern variables bound to the respective matched values. If used as `match h : e, ... with | p, ... => f | ...`, `h : e = p` is available within `f`.
When not constructing a proof, `match` does not automatically substitute variables matched on in dependent variables' types. Use `match (generalizing := true) ...` to enforce this.
Syntax quotations can also be used in a pattern match. This matches a `Syntax` value against quotations, pattern variables, or `_`.
Quoted identifiers only match identical identifiers - custom matching such as by the preresolved names only should be done explicitly.
`Syntax.atom`s are ignored during matching by default except when part of a built-in literal. For users introducing new atoms, we recommend wrapping them in dedicated syntax kinds if they should participate in matching. For example, in

```
syntax "c" ("foo" <|> "bar") ...

```

`foo` and `bar` are indistinguishable during matching, but in

```
syntax foo := "foo"
syntax "c" (foo <|> "bar") ...

```

they are not.
`[`=>`](Terms/Pattern-Matching/#Lean___Parser___Term___match) is evaluated in an environment extended with values for each [pattern variable](Terms/Pattern-Matching/#--tech-term-Pattern-variables) as well as an equality hypothesis for each named discriminant. This term is called the _right-hand side_ of the match alternative.
syntaxPattern Matching

```
term ::= ...
    | 


Pattern matching. match e, ... with | p, ... => f | ... matches each given
term e against each pattern p of a match alternative. When all patterns
of an alternative match, the match term evaluates to the value of the
corresponding right-hand side f with the pattern variables bound to the
respective matched values.
If used as match h : e, ... with | p, ... => f | ..., h : e = p is available
within f.


When not constructing a proof, match does not automatically substitute variables
matched on in dependent variables' types. Use match (generalizing := true) ... to
enforce this.


Syntax quotations can also be used in a pattern match.
This matches a Syntax value against quotations, pattern variables, or _.


Quoted identifiers only match identical identifiers - custom matching such as by the preresolved
names only should be done explicitly.


Syntax.atoms are ignored during matching by default except when part of a built-in literal.
For users introducing new atoms, we recommend wrapping them in dedicated syntax kinds if they
should participate in matching.
For example, in


```
syntax "c" ("foo" <|> "bar") ...

```

`foo` and `bar` are indistinguishable during matching, but in

```
syntax foo := "foo"
syntax "c" (foo <|> "bar") ...

```

they are not.
`match ((generalizing := (trueVal | falseVal)))? ((motive := term))? `
 
`matchDiscr` matches a "match discriminant", either `h : tm` or `tm`, used in `match` as `match h1 : e1, e2, h3 : e3 with ...`. 
`matchDiscr,* with (| (term,*)|* => term)*
```

syntaxMatch Discriminants

```
matchDiscr ::=
    


matchDiscr matches a "match discriminant", either h : tm or tm, used in match as
match h1 : e1, e2, h3 : e3 with .... 


term
```

```
matchDiscr ::= ...
    | 


matchDiscr matches a "match discriminant", either h : tm or tm, used in match as
match h1 : e1, e2, h3 : e3 with .... 


ident : term
```

Pattern matching expressions may alternatively use [quasiquotations](Notations-and-Macros/Macros/#--tech-term-Quasiquotation) as patterns, matching the corresponding `[Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")` values and treating the contents of [antiquotations](Notations-and-Macros/Macros/#--tech-term-antiquotations) as ordinary patterns. Quotation patterns are compiled differently than other patterns, so if one pattern in a ``Lean.Parser.Term.match : term`
Pattern matching. `match e, ... with | p, ... => f | ...` matches each given term `e` against each pattern `p` of a match alternative. When all patterns of an alternative match, the `match` term evaluates to the value of the corresponding right-hand side `f` with the pattern variables bound to the respective matched values. If used as `match h : e, ... with | p, ... => f | ...`, `h : e = p` is available within `f`.
When not constructing a proof, `match` does not automatically substitute variables matched on in dependent variables' types. Use `match (generalizing := true) ...` to enforce this.
Syntax quotations can also be used in a pattern match. This matches a `Syntax` value against quotations, pattern variables, or `_`.
Quoted identifiers only match identical identifiers - custom matching such as by the preresolved names only should be done explicitly.
`Syntax.atom`s are ignored during matching by default except when part of a built-in literal. For users introducing new atoms, we recommend wrapping them in dedicated syntax kinds if they should participate in matching. For example, in

```
syntax "c" ("foo" <|> "bar") ...

```

`foo` and `bar` are indistinguishable during matching, but in

```
syntax foo := "foo"
syntax "c" (foo <|> "bar") ...

```

they are not.
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match) is syntax, then all of them must be. Quotation patterns are described in [the section on quotations](Notations-and-Macros/Macros/#quote-patterns).
Patterns are a subset of the terms. They consist of the following: 

Catch-All Patterns
    
The hole syntax `_` is a pattern that matches any value and binds no pattern variables. Catch-all patterns are not entirely equivalent to unused pattern variables. They can be used in positions where the pattern's typing would otherwise require a more specific [inaccessible pattern](Terms/Pattern-Matching/#--tech-term-Inaccessible-patterns), while variables cannot be used in these positions. 

Identifiers
    
If an identifier is not bound in the current scope and is not applied to arguments, then it represents a pattern variable. _Pattern variables_ match any value, and the values thus matched are bound to the pattern variable in the local environment in which the [right-hand side](Terms/Pattern-Matching/#--tech-term-right-hand-side) is evaluated. If the identifier is bound, it is a pattern if it is bound to the [constructor](The-Type-System/Inductive-Types/#--tech-term-constructors) of an [inductive type](The-Type-System/Inductive-Types/#--tech-term-Inductive-types) or if its definition has the `match_pattern` attribute. 

Applications
    
Function applications are patterns if the function being applied is an identifier that is bound to a constructor or that has the `match_pattern` attribute and if all arguments are also patterns. If the identifier is a constructor, the pattern matches values built with that constructor if the argument patterns match the constructor's arguments. If it is a function with the `match_pattern` attribute, then the function application is unfolded and the resulting term's [normal form](The-Type-System/#--tech-term-normal-form) is used as the pattern. Default arguments are inserted as usual, and their normal forms are used as patterns. [Ellipses](Terms/Function-Application/#--tech-term-ellipsis), however, result in all further arguments being treated as universal patterns, even those with associated default values or tactics. 

Literals
    
[Character literals](Basic-Types/Characters/#char-syntax) and [string literals](Basic-Types/Strings/#string-syntax) are patterns that match the corresponding character or string. [Raw string literals](Basic-Types/Strings/#raw-string-literals) are allowed as patterns, but [interpolated strings](Basic-Types/Strings/#string-interpolation) are not. [Natural number literals](Basic-Types/Natural-Numbers/#nat-syntax) in patterns are interpreted by synthesizing the corresponding `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat")` instance and reducing the resulting term to [normal form](The-Type-System/#--tech-term-normal-form), which must be a pattern. Similarly, [scientific literals](Terms/Numeric-Literals/#--tech-term-scientific-literals) are interpreted via the corresponding `[OfScientific](Terms/Numeric-Literals/#OfScientific___mk "Documentation for OfScientific")` instance. While `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` has such an instance, `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")`s cannot be used as patterns because the instance relies on an opaque function that can't be reduced to a valid pattern. 

Structure Instances
    
[Structure instances](The-Type-System/Inductive-Types/#--tech-term-structure-instance) may be used as patterns. They are interpreted as the corresponding structure constructor. 

Quoted names
    
Quoted names, such as ``x` and ```[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, match the corresponding `Lean.Name` value. 

Macros
    
Macros in patterns are expanded. They are patterns if the resulting expansions are patterns. 

Inaccessible patterns
    
Inaccessible patterns are patterns that are forced to have a particular value by later typing constraints. Any term may be used as an inaccessible term. Inaccessible terms are parenthesized, with a preceding period (`.`).
syntaxInaccessible Patterns

```
term ::= ...
    | 


.(e) marks an "inaccessible pattern", which does not influence evaluation of the pattern match, but may be necessary for type-checking.
In contrast to regular patterns, e may be an arbitrary term of the appropriate type.


.(term)
```

Inaccessible Patterns
A number's _parity_ is whether it's even or odd:
`inductive Parity : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Type where   | even (h : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Parity](Terms/Pattern-Matching/#Parity-_LPAR_in-Inaccessible-Patterns_RPAR_ "Definition of example") (h + h)   | odd (h : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Parity](Terms/Pattern-Matching/#Parity-_LPAR_in-Inaccessible-Patterns_RPAR_ "Definition of example") ((h + h) + 1)  def Nat.parity (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Parity](Terms/Pattern-Matching/#Parity-_LPAR_in-Inaccessible-Patterns_RPAR_ "Definition of example") n :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") n [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | 0 => [.even](Terms/Pattern-Matching/#Parity___even-_LPAR_in-Inaccessible-Patterns_RPAR_ "Definition of example") 0   | n' + 1 =>     [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") n'.[parity](Terms/Pattern-Matching/#Nat___parity-_LPAR_in-Inaccessible-Patterns_RPAR_ "Definition of example") [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")     | [.even](Terms/Pattern-Matching/#Parity___even-_LPAR_in-Inaccessible-Patterns_RPAR_ "Definition of example") h => [.odd](Terms/Pattern-Matching/#Parity___odd-_LPAR_in-Inaccessible-Patterns_RPAR_ "Definition of example") h     | [.odd](Terms/Pattern-Matching/#Parity___odd-_LPAR_in-Inaccessible-Patterns_RPAR_ "Definition of example") h =>       have eq : (h + 1) + (h + 1) = (h + h + 1 + 1) :=         byn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ h [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")h [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") h [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") h [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 [omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic")All goals completed! 🐙       eq ▸ [.even](Terms/Pattern-Matching/#Parity___even-_LPAR_in-Inaccessible-Patterns_RPAR_ "Definition of example") (h + 1) `
Because a value of type `[Parity](Terms/Pattern-Matching/#Parity-_LPAR_in-Inaccessible-Patterns_RPAR_ "Definition of example")` contains half of a number (rounded down) as part of its representation of evenness or oddness, division by two can be implemented (in an unconventional manner) by finding a parity and then extracting the number.
`def half (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") n, n.[parity](Terms/Pattern-Matching/#Nat___parity-_LPAR_in-Inaccessible-Patterns_RPAR_ "Definition of example") [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | .(h + h),     [.even](Terms/Pattern-Matching/#Parity___even-_LPAR_in-Inaccessible-Patterns_RPAR_ "Definition of example") h => h   | .(h + h + 1), [.odd](Terms/Pattern-Matching/#Parity___odd-_LPAR_in-Inaccessible-Patterns_RPAR_ "Definition of example") h  => h `
Because the index structure of `[Parity.even](Terms/Pattern-Matching/#Parity___even-_LPAR_in-Inaccessible-Patterns_RPAR_ "Definition of example")` and `[Parity.odd](Terms/Pattern-Matching/#Parity___odd-_LPAR_in-Inaccessible-Patterns_RPAR_ "Definition of example")` force the number to have a certain form that is not otherwise a valid pattern, patterns that match on it must use inaccessible patterns for the number being divided.
[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABABQIYCdgwJ7IC5kA5dGZQJMJkAVXABxQHcALRTRAKGWQB9lEkIZAApmhEmQCU4jNjwixAamTNJXXsgD2YMAvGkY0orJz5ho5MtWXkARjUcwiAGYSYAOjpZTIoUQNGaN7yfgC86gC2ZFBiQow4zOp8AAzIoQB8yO4CiELJScggAOQ2tmnp6txRMDGFRZ7B+PEwidzcfNmCKuVZ2rqtbR193RmVbczoSPwAjuIWyvY283bSoXpWpaVG4W27yABG+JoRiADm6GPciLOAHaRZOULL9hyOLiroADauwn5ugQaEHbIaq1EAAGkKDTkTQSBXcy1UEN2nVyI0yAw6CK2EPcwzEPWYQA"\))
Patterns may additionally be named. Named patterns associate a name with a pattern; in subsequent patterns and on the right-hand side of the match alternative, the name refers to the part of the value that was matched by the given pattern. Named patterns are written with an `@` between the name and the pattern. Just like discriminants, named patterns may also be provided with names for equality assumptions.
syntaxNamed Patterns

```
term ::= ...
    | 


x@e or x@h:e matches the pattern e and binds its value to the identifier x.
If present, the identifier h is bound to a proof of x = e. 


ident@term
```

```
term ::= ...
    | 


x@e or x@h:e matches the pattern e and binds its value to the identifier x.
If present, the identifier h is bound to a proof of x = e. 


ident@ident:term
```

##  13.8.1. Types[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Terms--Pattern-Matching--Types "Permalink")
Each discriminant must be well typed. Because patterns are a subset of terms, their types can also be checked. Each pattern that matches a given discriminant must have the same type as the corresponding discriminant.
The [right-hand side](Terms/Pattern-Matching/#--tech-term-right-hand-side) of each match alternative should have the same type as the overall ``Lean.Parser.Term.match : term`
Pattern matching. `match e, ... with | p, ... => f | ...` matches each given term `e` against each pattern `p` of a match alternative. When all patterns of an alternative match, the `match` term evaluates to the value of the corresponding right-hand side `f` with the pattern variables bound to the respective matched values. If used as `match h : e, ... with | p, ... => f | ...`, `h : e = p` is available within `f`.
When not constructing a proof, `match` does not automatically substitute variables matched on in dependent variables' types. Use `match (generalizing := true) ...` to enforce this.
Syntax quotations can also be used in a pattern match. This matches a `Syntax` value against quotations, pattern variables, or `_`.
Quoted identifiers only match identical identifiers - custom matching such as by the preresolved names only should be done explicitly.
`Syntax.atom`s are ignored during matching by default except when part of a built-in literal. For users introducing new atoms, we recommend wrapping them in dedicated syntax kinds if they should participate in matching. For example, in

```
syntax "c" ("foo" <|> "bar") ...

```

`foo` and `bar` are indistinguishable during matching, but in

```
syntax foo := "foo"
syntax "c" (foo <|> "bar") ...

```

they are not.
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match) term. To support dependent types, matching a discriminant against a pattern refines the types that are expected within the scope of the pattern. In both subsequent patterns in the same match alternative and the right-hand side's type, occurrences of the discriminant are replaced by the pattern that it was matched against.
Type Refinement
This [indexed family](The-Type-System/Inductive-Types/#--tech-term-indexed-families) describes mostly-balanced trees, with the depth encoded in the type.
`inductive BalancedTree (α : Type u) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Type u where   | empty : [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α 0   | branch     (left : [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α n)     (val : α)     (right : [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α n) :     [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α (n + 1)   | lbranch     (left : [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α (n + 1))     (val : α)     (right : [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α n) :     [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α (n + 2)   | rbranch     (left : [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α n)     (val : α)     (right : [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α (n + 1)) :     [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α (n + 2) `
To begin the implementation of a function to construct a perfectly balanced tree with some initial element and a given depth, a [hole](Terms/Holes/#--tech-term-hole) can be used for the definition.
`def BalancedTree.filledWith     (x : α) (depth : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :     [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α depth :=   `don't know how to synthesize placeholder context: α:Type ux:αdepth:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α depth`_ `
The error message demonstrates that the tree should have the indicated depth.

```
don't know how to synthesize placeholder
context:
α:Type ux:αdepth:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α depth
```

Matching on the expected depth and inserting holes results in an error message for each hole. These messages demonstrate that the expected type has been refined, with `depth` replaced by the matched values.
`def BalancedTree.filledWith     (x : α) (depth : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :     [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α depth :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") depth [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | 0 => `don't know how to synthesize placeholder context: α:Type ux:αdepth:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α 0`_ | n + 1 => `don't know how to synthesize placeholder context: α:Type ux:αdepth n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")`_ `
The first hole yields the following message:

```
don't know how to synthesize placeholder
context:
α:Type ux:αdepth:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α 0
```

The second hole yields the following message:

```
don't know how to synthesize placeholder
context:
α:Type ux:αdepth n:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")n [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")
```

Matching on the depth of a tree and the tree itself leads to a refinement of the tree's type according to the depth's pattern. This means that certain combinations are not well-typed, such as `0` and `[branch](Terms/Pattern-Matching/#BalancedTree___branch-_LPAR_in-Type-Refinement_RPAR_ "Definition of example")`, because refining the second discriminant's type yields `[BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α 0` which does not match the constructor's type.
`def BalancedTree.isPerfectlyBalanced     (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (t : [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α n) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") n, t [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | 0, [.empty](Terms/Pattern-Matching/#BalancedTree___empty-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")   | 0, `Type mismatch   left.[branch](Terms/Pattern-Matching/#BalancedTree___branch-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") val right has type   [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") ?m.13 [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")?m.12 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") but is expected to have type   [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α 0`[.branch](Terms/Pattern-Matching/#BalancedTree___branch-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") left val right => isPerfectlyBalanced left && isPerfectlyBalanced right | _, _ => false `
```
Type mismatch
  left.[branch](Terms/Pattern-Matching/#BalancedTree___branch-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") val right
has type
  [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") ?m.13 [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")?m.12 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")
but is expected to have type
  [BalancedTree](Terms/Pattern-Matching/#BalancedTree-_LPAR_in-Type-Refinement_RPAR_ "Definition of example") α 0
```

[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABAIQIYBt0iosAKgE6IoAUgjcDIBcyBAngA4oQCUNyAcujMoEmEdJi2QB3ABaISAKGTIAPskQBbRjHocM2XPmKlkVAAwz5yAEZEcUMcdllMiAGa9amyzpIoqIVjeRl4WBwUPrK2RMAA5mLOaFhuhB76yN40vq7aCXpUZCDIANTIAIwhJpjmltahfvZOGnEZup5+uQXFJbYBmEHtfuFRMel4mU0p1Gn1Q41JOfnIAEwlCkTluJWhdo4DE+5ZyT3+gbTBvmR90XVak4nZLUWs7GNVgztNMwULQA"\))
###  13.8.1.1. Pattern Equality Proofs[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Terms--Pattern-Matching--Types--Pattern-Equality-Proofs "Permalink")
When a discriminant is named, ``Lean.Parser.Term.match : term`
Pattern matching. `match e, ... with | p, ... => f | ...` matches each given term `e` against each pattern `p` of a match alternative. When all patterns of an alternative match, the `match` term evaluates to the value of the corresponding right-hand side `f` with the pattern variables bound to the respective matched values. If used as `match h : e, ... with | p, ... => f | ...`, `h : e = p` is available within `f`.
When not constructing a proof, `match` does not automatically substitute variables matched on in dependent variables' types. Use `match (generalizing := true) ...` to enforce this.
Syntax quotations can also be used in a pattern match. This matches a `Syntax` value against quotations, pattern variables, or `_`.
Quoted identifiers only match identical identifiers - custom matching such as by the preresolved names only should be done explicitly.
`Syntax.atom`s are ignored during matching by default except when part of a built-in literal. For users introducing new atoms, we recommend wrapping them in dedicated syntax kinds if they should participate in matching. For example, in

```
syntax "c" ("foo" <|> "bar") ...

```

`foo` and `bar` are indistinguishable during matching, but in

```
syntax foo := "foo"
syntax "c" (foo <|> "bar") ...

```

they are not.
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match) generates a proof that the pattern and discriminant are equal, binding it to the provided name in the [right-hand side](Terms/Pattern-Matching/#--tech-term-right-hand-side). This is useful to bridge the gap between dependent pattern matching on indexed families and APIs that expect explicit propositional arguments, and it can help tactics that make use of assumptions to succeed.
Pattern Equality Proofs
The function `[last?](Terms/Pattern-Matching/#last___-_LPAR_in-Pattern-Equality-Proofs_RPAR_ "Definition of example")`, which either throws an exception or returns the last element of its argument, uses the standard library function `[List.getLast](Basic-Types/Linked-Lists/#List___getLast "Documentation for List.getLast")`. This function expects a proof that the list in question is nonempty. Naming the match on `xs` ensures that there's an assumption in scope that states that `xs` is equal to `_ :: _`, which `[simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic")` uses to discharge the goal.
`def last? (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") α :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") h : xs [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | [] =>     [.error](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.error") "Can't take first element of empty list"   | _ :: _ =>     [.ok](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.ok") <| xs.[getLast](Basic-Types/Linked-Lists/#List___getLast "Documentation for List.getLast") (show xs ≠ [] byAll goals completed! 🐙 [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") h'α:Type ?u.7xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") αhead✝:αtail✝:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") αh:xs [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") head✝ [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") tail✝h':xs [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")⊢ [False](Basic-Propositions/Truth/#False "Documentation for False"); [simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic")All goals completed! 🐙) `
Without the name, `[simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic")` is unable to find the contradiction.
`def last?' (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") α :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") xs [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | [] =>     [.error](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.error") "Can't take first element of empty list"   | _ :: _ =>     [.ok](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.ok") <| xs.[getLast](Basic-Types/Linked-Lists/#List___getLast "Documentation for List.getLast") (show xs ≠ [] byα:Type ?u.7xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") αhead✝:αtail✝:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") αh':xs [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")⊢ [False](Basic-Propositions/Truth/#False "Documentation for False") [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") h'α:Type ?u.7xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") αhead✝:αtail✝:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") αh':xs [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")⊢ [False](Basic-Propositions/Truth/#False "Documentation for False"); `simp_all made no progress`[simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic")α:Type ?u.7xs:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") αhead✝:αtail✝:[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") αh':xs [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.nil")⊢ [False](Basic-Propositions/Truth/#False "Documentation for False")) `
```
simp_all made no progress
```

[Live ↪](javascript:openLiveLink\("CYUwZgBANghgzgFwPwQBQA84QFwQDICWiEgjcACUOEAougMYgAOCEAyggE4EB2A5qTgF4AUBAgBbGAloALCLNyYIAdwIJpIiAB8IAbQC6EAQD4NogHQh27APbsIAIgDCMLgHJmCGAGsQEMAXZiECgQMRAuZmtIUKYAT2giBHsNbQB9HFx041MIM2svCAAebUwzHhAEPHhmVDhpayUIRUADIl0DACN47g5rOVcAbgg4AjEGVJgoKDIgA"\))
###  13.8.1.2. Explicit Motives[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Terms--Pattern-Matching--Types--Explicit-Motives "Permalink")
Pattern matching is not a built-in primitive of Lean. Instead, it is translated to applications of [recursors](The-Type-System/Inductive-Types/#--tech-term-recursor) via [auxiliary matching functions](Elaboration-and-Compilation/#--tech-term-auxiliary-matching-functions). Both require a [_motive_](The-Type-System/Inductive-Types/#--tech-term-motive) that explains the relationship between the discriminant and the resulting type. Generally, the ``Lean.Parser.Term.match : term`
Pattern matching. `match e, ... with | p, ... => f | ...` matches each given term `e` against each pattern `p` of a match alternative. When all patterns of an alternative match, the `match` term evaluates to the value of the corresponding right-hand side `f` with the pattern variables bound to the respective matched values. If used as `match h : e, ... with | p, ... => f | ...`, `h : e = p` is available within `f`.
When not constructing a proof, `match` does not automatically substitute variables matched on in dependent variables' types. Use `match (generalizing := true) ...` to enforce this.
Syntax quotations can also be used in a pattern match. This matches a `Syntax` value against quotations, pattern variables, or `_`.
Quoted identifiers only match identical identifiers - custom matching such as by the preresolved names only should be done explicitly.
`Syntax.atom`s are ignored during matching by default except when part of a built-in literal. For users introducing new atoms, we recommend wrapping them in dedicated syntax kinds if they should participate in matching. For example, in

```
syntax "c" ("foo" <|> "bar") ...

```

`foo` and `bar` are indistinguishable during matching, but in

```
syntax foo := "foo"
syntax "c" (foo <|> "bar") ...

```

they are not.
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match) elaborator is capable of synthesizing an appropriate motive, and the refinement of types that occurs during pattern matching is a result of the motive that was selected. In some specialized circumstances, a different motive may be needed and may be provided explicitly using the `(motive := …)` syntax of ``Lean.Parser.Term.match : term`
Pattern matching. `match e, ... with | p, ... => f | ...` matches each given term `e` against each pattern `p` of a match alternative. When all patterns of an alternative match, the `match` term evaluates to the value of the corresponding right-hand side `f` with the pattern variables bound to the respective matched values. If used as `match h : e, ... with | p, ... => f | ...`, `h : e = p` is available within `f`.
When not constructing a proof, `match` does not automatically substitute variables matched on in dependent variables' types. Use `match (generalizing := true) ...` to enforce this.
Syntax quotations can also be used in a pattern match. This matches a `Syntax` value against quotations, pattern variables, or `_`.
Quoted identifiers only match identical identifiers - custom matching such as by the preresolved names only should be done explicitly.
`Syntax.atom`s are ignored during matching by default except when part of a built-in literal. For users introducing new atoms, we recommend wrapping them in dedicated syntax kinds if they should participate in matching. For example, in

```
syntax "c" ("foo" <|> "bar") ...

```

`foo` and `bar` are indistinguishable during matching, but in

```
syntax foo := "foo"
syntax "c" (foo <|> "bar") ...

```

they are not.
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match). This motive should be a function type that expects at least as many parameters as there are discriminants. The type that results from applying a function with this type to the discriminants in order is the type of the entire ``Lean.Parser.Term.match : term`
Pattern matching. `match e, ... with | p, ... => f | ...` matches each given term `e` against each pattern `p` of a match alternative. When all patterns of an alternative match, the `match` term evaluates to the value of the corresponding right-hand side `f` with the pattern variables bound to the respective matched values. If used as `match h : e, ... with | p, ... => f | ...`, `h : e = p` is available within `f`.
When not constructing a proof, `match` does not automatically substitute variables matched on in dependent variables' types. Use `match (generalizing := true) ...` to enforce this.
Syntax quotations can also be used in a pattern match. This matches a `Syntax` value against quotations, pattern variables, or `_`.
Quoted identifiers only match identical identifiers - custom matching such as by the preresolved names only should be done explicitly.
`Syntax.atom`s are ignored during matching by default except when part of a built-in literal. For users introducing new atoms, we recommend wrapping them in dedicated syntax kinds if they should participate in matching. For example, in

```
syntax "c" ("foo" <|> "bar") ...

```

`foo` and `bar` are indistinguishable during matching, but in

```
syntax foo := "foo"
syntax "c" (foo <|> "bar") ...

```

they are not.
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match) term, and the type that results from applying a function with this type to all patterns in each alternative is the type of that alternative's [right-hand side](Terms/Pattern-Matching/#--tech-term-right-hand-side).
Matching with an Explicit Motive
An explicit motive can be used to provide type information that is otherwise unavailable from the surrounding context. Attempting to match on a number and a proof that it is in fact `5` is an error, because there's no reason to connect the number to the proof:
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax")   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") 5, [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | `Invalid match expression: This pattern contains metavariables:   [Eq.refl](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq.refl") ?m.14`5, [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") => "ok" `
```
Invalid match expression: This pattern contains metavariables:
  [Eq.refl](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq.refl") ?m.14
```

An explicit motive explains the relationship between the discriminants:
``"ok"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") (motive := (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → n = 5 → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) 5, [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") | 5, [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") => "ok" `
```
"ok"
```

[Live ↪](javascript:openLiveLink\("MQUwbghgNgUABHAthALgYwBZwBSIPYoCWYIcAXALw4B25cAcqgJRyBJhHLVQKxtwDKKAE6FqAcxZcANHEEAzKHADuhFBnhwAPnCkz5cCgD44AIjwBrY0A"\))
###  13.8.1.3. Discriminant Refinement[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Terms--Pattern-Matching--Types--Discriminant-Refinement "Permalink")
When matching on an indexed family, the indices must also be discriminants. Otherwise, the pattern would not be well typed: it is a type error if an index is just a variable but the type of a constructor requires a more specific value. However, a process called discriminant refinement automatically adds indices as additional discriminants.
Discriminant Refinement
In the definition of `[f](Terms/Pattern-Matching/#f-_LPAR_in-Discriminant-Refinement_RPAR_ "Definition of example")`, the equality proof is the only discriminant. However, equality is an indexed family, and the match is only valid when `n` is an additional discriminant.
`def f (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (p : n = 3) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") p [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") => "ok" `
Using ``Lean.Parser.Command.print : command```#print` demonstrates that the additional discriminant was added automatically.
``def f : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 3 → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := fun n p =>   match 3, p with   | .(n), ⋯ => "ok"`#print [f](Terms/Pattern-Matching/#f-_LPAR_in-Discriminant-Refinement_RPAR_ "Definition of example") `
```
def f : (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → n [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") 3 → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=
fun n p =>
  match 3, p with
  | .(n), ⋯ => "ok"
```

[Live ↪](javascript:openLiveLink\("CYUwZgBJAUB2EC4IDkCGAXAlBaAHRE8AvBAMzZIDK6ATgJawDmiRAUBBALYYDGAFhHwB3Ouj7sIAHwg0wAGwhEAfBABEAewDWq1qwDEuerHRQgA"\))
###  13.8.1.4. Generalization[🔗](find/?domain=Verso.Genre.Manual.section&name=match-generalization "Permalink")
The pattern match elaborator automatically determines the motive by finding occurrences of the discriminants in the expected type, generalizing them in the types of subsequent discriminants so that the appropriate pattern can be substituted. Additionally, occurrences of the discriminants in the types of variables in the context are generalized and substituted by default. This latter behavior can be turned off by passing the `(generalizing := false)` flag to ``Lean.Parser.Term.match : term`
Pattern matching. `match e, ... with | p, ... => f | ...` matches each given term `e` against each pattern `p` of a match alternative. When all patterns of an alternative match, the `match` term evaluates to the value of the corresponding right-hand side `f` with the pattern variables bound to the respective matched values. If used as `match h : e, ... with | p, ... => f | ...`, `h : e = p` is available within `f`.
When not constructing a proof, `match` does not automatically substitute variables matched on in dependent variables' types. Use `match (generalizing := true) ...` to enforce this.
Syntax quotations can also be used in a pattern match. This matches a `Syntax` value against quotations, pattern variables, or `_`.
Quoted identifiers only match identical identifiers - custom matching such as by the preresolved names only should be done explicitly.
`Syntax.atom`s are ignored during matching by default except when part of a built-in literal. For users introducing new atoms, we recommend wrapping them in dedicated syntax kinds if they should participate in matching. For example, in

```
syntax "c" ("foo" <|> "bar") ...

```

`foo` and `bar` are indistinguishable during matching, but in

```
syntax foo := "foo"
syntax "c" (foo <|> "bar") ...

```

they are not.
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match).
Matching, With and Without Generalization
In this definition of `boolCases`, the assumption `b` is generalized in the type of `h` and then replaced with the actual pattern. This means that `ifTrue` and `ifFalse` have the types `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → α` and `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") → α` in their respective cases, but `h`'s type mentions the original discriminant.
`def boolCases (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))     (ifTrue : b = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → α)     (ifFalse : b = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") → α) :     α :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") h : b [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")  => ifTrue `Application type mismatch: The argument   h has type   b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") but is expected to have type   [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") in the application   ifTrue h`h | [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") => ifFalse `Application type mismatch: The argument   h has type   b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") but is expected to have type   [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") in the application   ifFalse h`h `
The error for the first case is typical of both:

```
Application type mismatch: The argument
  h
has type
  b [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")
but is expected to have type
  [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")
in the application
  ifTrue h
```

Turning off generalization allows type checking to succeed, because `b` remains in the types of `ifTrue` and `ifFalse`.
`def boolCases (b : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))     (ifTrue : b = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") → α)     (ifFalse : b = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") → α) :     α :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") (generalizing := false) h : b [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")  => ifTrue h   | [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") => ifFalse h `
In the generalized version, `[rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")` could have been used as the proof arguments as an alternative.
[Live ↪](javascript:openLiveLink\("G4QwTgliBGA2CmACA3oRuBEC5EBUCeAHJAVwF9EAKaTRAIQHs7YBKCiAM2zCKSyoF5EAFy5JASYSJULcuwBiIWAGceifojbylicZIBQOgCbw2KhrADCIJQopUs9Rkx2JnrDiOqrh3LRMcvXcorKqupBPpKYTi7oGHxRALYgggDGABYUAObwAHbwYPIQAF4Q2RmYAqFKLOm8iADuEIKpUQA+Qu6IfAB8iOyc3s3ObZVI3b1sgZqpQA"\))
##  13.8.2. Custom Pattern Functions[🔗](find/?domain=Verso.Genre.Manual.section&name=match_pattern-functions "Permalink")
In patterns, defined constants with the `match_pattern` attribute are unfolded and normalized rather than rejected. This allows a more convenient syntax to be used for many patterns. In the standard library, `[Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add")`, `[HAdd.hAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")`, `[Add.add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add.add")`, and `[Neg.neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg.neg")` all have this attribute, which allows patterns like `n + 1` instead of `[Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") n`. Similarly, `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")` and `[Unit.unit](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")` are definitions that set the respective [universe parameters](The-Type-System/Universes/#--tech-term-universe-parameters) of `[PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")` and `[PUnit.unit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit.unit")` to 0; the `match_pattern` attribute on `[Unit.unit](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")` allows it to be used in patterns, where it expands to `[PUnit.unit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit.unit").{0}`.
attributeAttribute for Match Patterns
The `match_pattern` attribute indicates that a definition should be unfolded, rather than rejected, in a pattern.

```
attr ::= ...
    | match_pattern
```

Match Patterns Follow Reduction
The following function can't be compiled:
`def nonzero (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") n [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | 0 => [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")   `Invalid pattern(s): `k` is an explicit pattern variable, but it only occurs in positions that are inaccessible to pattern matching:   .([Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add") 1 k)`| 1 + k => true `
The error message on the pattern `1 + _` is:

```
Invalid pattern(s): `k` is an explicit pattern variable, but it only occurs in positions that are inaccessible to pattern matching:
  .([Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add") 1 k)
```

This is because `[Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add")` is defined by recursion on its second parameter, equivalently to:
`def add : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   | a, [Nat.zero](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.zero")   => a   | a, [Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") b => [Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") ([Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add") a b) `
No [ι-reduction](The-Type-System/Inductive-Types/#--tech-term-___-reduction) is possible, because the value being matched is a variable, not a constructor. `1 + k` gets stuck as `[Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add") 1 k`, which is not a valid pattern.
In the case of `k + 1`, that is, `[Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add") k ([.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") [.zero](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.zero"))`, the second pattern matches, so it reduces to `[Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") ([Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add") k [.zero](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.zero"))`. The second pattern now matches, yielding `[Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") k`, which is a valid pattern.
[Live ↪](javascript:openLiveLink\("CYUwZgBAhswQXBAclALhQSYTLZ7qBQEEAPtADR4B0AXiAE4D2REAvAHzSEnlUDOArgGNBEAEasOKVJQHCIACimUYcKGICUQA"\))
##  13.8.3. Pattern Matching Functions[🔗](find/?domain=Verso.Genre.Manual.section&name=pattern-fun "Permalink")
syntaxPattern-Matching Functions
Functions may be specified via pattern matching by writing a sequence of patterns after ``Lean.Parser.Term.fun : term```fun`, each preceded by a vertical bar (`|`).

```
term ::= ...
    | fun
        (| term,* => term)*
```

This desugars to a function that immediately pattern-matches on its arguments.
Pattern-Matching Functions
`[isZero](Terms/Pattern-Matching/#isZero-_LPAR_in-Pattern-Matching-Functions_RPAR_ "Definition of example")` is defined using a pattern-matching function abstraction, while `[isZero'](Terms/Pattern-Matching/#isZero___-_LPAR_in-Pattern-Matching-Functions_RPAR_ "Definition of example")` is defined using a pattern match expression:
`def isZero : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") :=   fun     | 0 => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")     | _ => [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")  def isZero' : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") :=   fun n =>     [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") n [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")     | 0 => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")     | _ => [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") `
Because the former is syntactic sugar for the latter, they are definitionally equal:
`example : [isZero](Terms/Pattern-Matching/#isZero-_LPAR_in-Pattern-Matching-Functions_RPAR_ "Definition of example") = [isZero'](Terms/Pattern-Matching/#isZero___-_LPAR_in-Pattern-Matching-Functions_RPAR_ "Definition of example") := [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
The desugaring is visible in the output of ``Lean.Parser.Command.print : command```#print`:
``def isZero : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := fun x =>   match x with   | 0 => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")   | x => [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`#print [isZero](Terms/Pattern-Matching/#isZero-_LPAR_in-Pattern-Matching-Functions_RPAR_ "Definition of example") `
outputs

```
def isZero : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") :=
fun x =>
  match x with
  | 0 => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")
  | x => [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")
```

while
``def isZero' : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := fun n =>   match n with   | 0 => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")   | x => [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`#print [isZero'](Terms/Pattern-Matching/#isZero___-_LPAR_in-Pattern-Matching-Functions_RPAR_ "Definition of example") `
outputs

```
def isZero' : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") :=
fun n =>
  match n with
  | 0 => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")
  | x => [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")
```

[Live ↪](javascript:openLiveLink\("CYUwZgBAlgzgWiATgewgLggOQIYBcKBJhBAELLIA26AvAFAQRgCuAdnfRAD4QAMEVAfBFyJGINvS4B9PoLDZyMMTVCRYCFAHJ0WPIRJlKaWvSbMIZgeIgBbPAGMAFuYgB3KLgdWuvAUJFj2TghpXzkFJRAAD2xrAAdyEG01JFQqaHgUrSMIRDByGhoAYljEKGZ8ZJQC4tLy9PVkDSA"\))
##  13.8.4. Other Pattern Matching Operators[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Terms--Pattern-Matching--Other-Pattern-Matching-Operators "Permalink")
In addition to ``Lean.Parser.Term.match : term`
Pattern matching. `match e, ... with | p, ... => f | ...` matches each given term `e` against each pattern `p` of a match alternative. When all patterns of an alternative match, the `match` term evaluates to the value of the corresponding right-hand side `f` with the pattern variables bound to the respective matched values. If used as `match h : e, ... with | p, ... => f | ...`, `h : e = p` is available within `f`.
When not constructing a proof, `match` does not automatically substitute variables matched on in dependent variables' types. Use `match (generalizing := true) ...` to enforce this.
Syntax quotations can also be used in a pattern match. This matches a `Syntax` value against quotations, pattern variables, or `_`.
Quoted identifiers only match identical identifiers - custom matching such as by the preresolved names only should be done explicitly.
`Syntax.atom`s are ignored during matching by default except when part of a built-in literal. For users introducing new atoms, we recommend wrapping them in dedicated syntax kinds if they should participate in matching. For example, in

```
syntax "c" ("foo" <|> "bar") ...

```

`foo` and `bar` are indistinguishable during matching, but in

```
syntax foo := "foo"
syntax "c" (foo <|> "bar") ...

```

they are not.
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match) and ``termIfLet : term`
`if let pat := d then t else e` is a shorthand syntax for:

```
match d with
| pat => t
| _ => e

```

It matches `d` against the pattern `pat` and the bindings are available in `t`. If the pattern does not match, it returns `e` instead.
`[`if let`](Terms/Conditionals/#termIfLet), there are a few other operators that perform pattern matching.
syntaxThe `matches` Operator
The ``Lean.«term_Matches_|» : term``[`matches`](Terms/Pattern-Matching/#Lean____FLQQ_term_Matches_____FLQQ_) operator returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the term on the left matches the pattern on the right.

```
term ::= ...
    | term matches term
```

When branching on the result of ``Lean.«term_Matches_|» : term``[`matches`](Terms/Pattern-Matching/#Lean____FLQQ_term_Matches_____FLQQ_), it's usually better to use ``termIfLet : term`
`if let pat := d then t else e` is a shorthand syntax for:

```
match d with
| pat => t
| _ => e

```

It matches `d` against the pattern `pat` and the bindings are available in `t`. If the pattern does not match, it returns `e` instead.
`[`if let`](Terms/Conditionals/#termIfLet), which can bind pattern variables in addition to checking whether a pattern matches.
If there are no constructor patterns that could match a discriminant or sequence of discriminants, then the code in question is unreachable, as there must be a false assumption in the local context. The ``Lean.Parser.Term.nomatch : term`
Empty match/ex falso. `nomatch e` is of arbitrary type `α : Sort u` if Lean can show that an empty set of patterns is exhaustive given `e`'s type, e.g. because it has no constructors.
`[`nomatch`](Terms/Pattern-Matching/#Lean___Parser___Term___nomatch) expression is a match with zero cases that can have any type whatsoever, so long as there are no possible cases that could match the discriminants.
syntaxCaseless Pattern Matches

```
term ::= ...
    | 


Empty match/ex falso. nomatch e is of arbitrary type α : Sort u if
Lean can show that an empty set of patterns is exhaustive given e's type,
e.g. because it has no constructors.


nomatch term,*
```

Inconsistent Indices
There are no constructor patterns that can match both proofs in this example:
`example (p1 : x = "Hello") (p2 : x = "world") : [False](Basic-Propositions/Truth/#False "Documentation for False") :=   [nomatch](Terms/Pattern-Matching/#Lean___Parser___Term___nomatch "Documentation for syntax") p1, p2 `
This is because they separately refine the value of `x` to unequal strings. Thus, the ``Lean.Parser.Term.nomatch : term`
`[`nomatch`](Terms/Pattern-Matching/#Lean___Parser___Term___nomatch) operator allows the example's body to prove `[False](Basic-Propositions/Truth/#False "Documentation for False")` (or any other proposition or type).
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAKKBGeAueJ4F54CIAJYGGAe3wEokoAmDLXAgdzICcYATKhgMTBgBnBOhwAoePAB2ZCGAAuAYwAW8VABo1tIA"\))
When the expected type is a function type, ``Lean.Parser.Term.nofun : term``[`nofun`](Terms/Pattern-Matching/#Lean___Parser___Term___nofun) is shorthand for a function that takes as many parameters as the type indicates in which the body is ``Lean.Parser.Term.nomatch : term`
Empty match/ex falso. `nomatch e` is of arbitrary type `α : Sort u` if Lean can show that an empty set of patterns is exhaustive given `e`'s type, e.g. because it has no constructors.
`[`nomatch`](Terms/Pattern-Matching/#Lean___Parser___Term___nomatch) applied to all of the parameters.
syntaxCaseless Functions

```
term ::= ...
    | nofun
```

Impossible Functions
Instead of introducing arguments for both equality proofs and then using both in a ``Lean.Parser.Term.nomatch : term`
`[`nomatch`](Terms/Pattern-Matching/#Lean___Parser___Term___nomatch), it is possible to use ``Lean.Parser.Term.nofun : term``[`nofun`](Terms/Pattern-Matching/#Lean___Parser___Term___nofun).
`example : x = "Hello" → x = "world" → [False](Basic-Propositions/Truth/#False "Documentation for False") := [nofun](Terms/Pattern-Matching/#Lean___Parser___Term___nofun "Documentation for syntax") `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAueJ4F54CIASwYwHtN5AkwhXSwHcCAnGAE2LIDEwYBnBRDAOwIDMArjyA"\))
[←13.7. Conditionals](Terms/Conditionals/#if-then-else "13.7. Conditionals")[13.9. Holes→](Terms/Holes/#The-Lean-Language-Reference--Terms--Holes "13.9. Holes")

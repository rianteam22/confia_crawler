[←3. Interacting with Lean](Interacting-with-Lean/#interaction "3. Interacting with Lean")[4.1. Functions→](The-Type-System/Functions/#functions "4.1. Functions")
#  4. The Type System[🔗](find/?domain=Verso.Genre.Manual.section&name=type-system "Permalink")
_Terms_ , also known as _expressions_ , are the fundamental units of meaning in Lean's core language. They are produced from user-written syntax by the [elaborator](Terms/#--tech-term-elaborator). Lean's type system relates terms to their _types_ , which are also themselves terms. Types can be thought of as denoting sets, while terms denote individual elements of these sets. A term is _well-typed_ if it has a type under the rules of Lean's type theory. Only well-typed terms have a meaning.
Terms are a dependently typed λ-calculus: they include function abstraction, application, variables, and `let`-bindings. In addition to bound variables, variables in the term language may refer to [constructors](The-Type-System/Inductive-Types/#--tech-term-constructors), [type constructors](The-Type-System/Inductive-Types/#--tech-term-type-constructors), [recursors](The-Type-System/Inductive-Types/#--tech-term-recursor), defined constants, or opaque constants. Constructors, type constructors, recursors, and opaque constants are not subject to substitution, while defined constants may be replaced with their definitions.
A _derivation_ demonstrates the well-typedness of a term by explicitly indicating the precise inference rules that are used. Implicitly, well-typed terms can stand in for the derivations that demonstrate their well-typedness. Lean's type theory is explicit enough that derivations can be reconstructed from well-typed terms, which greatly reduces the overhead that would be incurred from storing a complete derivation, while still being expressive enough to represent modern research mathematics. This means that proof terms are sufficient evidence of the truth of a theorem and are amenable to independent verification.
In addition to having types, terms are also related by _definitional equality_. This is the mechanically-checkable relation that syntactically equates terms modulo their computational behavior. Definitional equality includes the following forms of reduction: 

β (beta)
    
Applying a function abstraction to an argument by substitution for the bound variable 

δ (delta)
    
Replacing occurrences of [defined constants](The-Type-System/#--tech-term-defined-constants) by the definition's value 

ι (iota)
    
Reduction of recursors whose targets are constructors (primitive recursion) 

ζ (zeta)
    
Replacement of let-bound variables by their defined values 

Quotient reduction
    
[Reduction of the quotient type's function lifting operator](The-Type-System/Quotients/#quotient-model) when applied to an element of a quotient
Terms in which all possible reductions have been carried out are in _normal form_.
Definitional equality includes η-equivalence of functions and single-constructor inductive types. That is, `fun x => [f](releases/v4.27.0/#f "Definition of example") x` is definitionally equal to `[f](releases/v4.27.0/#f "Definition of example")`, and `S.mk x.f1 x.f2` is definitionally equal to `x`, if `[S](The-Type-System/Inductive-Types/#S "Definition of example")` is a structure with fields `f1` and `f2`. It also features _proof irrelevance_ : any two proofs of the same proposition are definitionally equal. It is reflexive and symmetric, but not transitive.
Definitional equality is used by conversion: if two terms are definitionally equal, and a given term has one of them as its type, then it also has the other as its type. Because definitional equality includes reduction, types can result from computations over data.
Computing types
When passed a natural number, the function `[LengthList](The-Type-System/#LengthList-_LPAR_in-Computing-types_RPAR_ "Definition of example")` computes a type that corresponds to a list with precisely that many entries in it:
`def LengthList (α : Type u) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Type u   | 0 => [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")   | n + 1 => α × [LengthList](The-Type-System/#LengthList-_LPAR_in-Computing-types_RPAR_ "Definition of example") α n `
Because Lean's tuples nest to the right, multiple nested parentheses are not needed:
`example : [LengthList](The-Type-System/#LengthList-_LPAR_in-Computing-types_RPAR_ "Definition of example") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") 0 := ()  example : [LengthList](The-Type-System/#LengthList-_LPAR_in-Computing-types_RPAR_ "Definition of example") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") 2 :=   ("Hello", "there", ()) `
If the length does not match the number of entries, then the computed type will not match the term:
`example : [LengthList](The-Type-System/#LengthList-_LPAR_in-Computing-types_RPAR_ "Definition of example") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") 5 :=   ("Wrong", "number", `Application type mismatch: The argument   [(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit") has type   [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") but is expected to have type   [LengthList](The-Type-System/#LengthList-_LPAR_in-Computing-types_RPAR_ "Definition of example") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") 3 in the application   [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")"number"[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")`()) `
```
Application type mismatch: The argument
  [(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")
has type
  [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")
but is expected to have type
  [LengthList](The-Type-System/#LengthList-_LPAR_in-Computing-types_RPAR_ "Definition of example") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") 3
in the application
  [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")"number"[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") [(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")
```

[Live ↪](javascript:openLiveLink\("CYUwZgBAMiB2DmAXAFlAlgZ0RAFIRuAIAuCAFQE8AHECAVwEoiIA5AQ20CTCUy6mgKAggAfCAAYIAXgB8EAAoBVWGkT8hEWBADUEAIwTpBAOvQ4SVJmwFYvXiAAeLALYUANtWIwEKdFggBJWNhihOK4dNZ2ji5uxp5mPgDKiABOaAgQAExE4io4AEQAEiDOzgD2uQA0ELkoIEkgFaF0QA"\))
The basic types in Lean are [universes](The-Type-System/Universes/#--tech-term-universes), [function](The-Type-System/Functions/#--tech-term-Functions) types, the quotient former `[Quot](The-Type-System/Quotients/#Quot "Documentation for Quot")`, and [type constructors](The-Type-System/Inductive-Types/#--tech-term-type-constructors) of [inductive types](The-Type-System/Inductive-Types/#--tech-term-Inductive-types). [Defined constants](The-Type-System/#--tech-term-defined-constants), applications of [recursors](The-Type-System/Inductive-Types/#--tech-term-recursor), function application, [axioms](Axioms/#--tech-term-Axioms) or [opaque constants](Definitions/Definitions/#--tech-term-Opaque-constants) may additionally give types, just as they can give rise to terms in any other type.
  1. [4.1. Functions](The-Type-System/Functions/#functions)
  2. [4.2. Propositions](The-Type-System/Propositions/#propositions)
  3. [4.3. Universes](The-Type-System/Universes/#The-Lean-Language-Reference--The-Type-System--Universes)
  4. [4.4. Inductive Types](The-Type-System/Inductive-Types/#inductive-types)
  5. [4.5. Quotients](The-Type-System/Quotients/#quotients)

[←3. Interacting with Lean](Interacting-with-Lean/#interaction "3. Interacting with Lean")[4.1. Functions→](The-Type-System/Functions/#functions "4.1. Functions")

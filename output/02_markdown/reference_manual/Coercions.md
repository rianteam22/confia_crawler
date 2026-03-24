[←10.5. Basic Classes](Type-Classes/Basic-Classes/#basic-classes "10.5. Basic Classes")[11.1. Coercion Insertion→](Coercions/Coercion-Insertion/#coercion-insertion "11.1. Coercion Insertion")
#  11. Coercions[🔗](find/?domain=Verso.Genre.Manual.section&name=coercions "Permalink")
When the Lean elaborator is expecting one type but produces a term with a different type, it attempts to automatically insert a _coercion_ , which is a specially designated function from the term's type to the expected type. Coercions make it possible to use specific types to represent data while interacting with APIs that expect less-informative types. They also allow mathematical developments to follow the usual practice of “punning”, where the same symbol is used to stand for both an algebraic structure and its carrier set, with the precise meaning determined by context.
Lean's standard library and metaprogramming APIs define many coercions. Some examples include:
  * A `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` may be used where an `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` is expected.
  * A `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")` may be used where a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` is expected.
  * An `α` may be used where an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α` is expected. The coercion wraps the value in `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")`.
  * An `α` may be used where a `[Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") α` is expected. The coercion wraps the term in a function to delay its evaluation.
  * When one syntax category `c1` embeds into another category `c2`, a coercion from `[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") c1` to `[TSyntax](Notations-and-Macros/Defining-New-Syntax/#Lean___TSyntax___mk "Documentation for Lean.TSyntax") c2` performs any necessary wrapping to construct a valid syntax tree.


Coercions are found using type class [synthesis](Type-Classes/#--tech-term-synthesizes). The set of coercions can be extended by adding further instances of the appropriate type classes.
Coercions
All of the following examples rely on coercions:
`example (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") := n example (n : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") k) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := n example (x : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α := x  def th (f : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := f x  [open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Lean [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") example (n : [Ident](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Ident "Documentation for Lean.Syntax.Ident")) : [Term](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___Term "Documentation for Lean.Syntax.Term") := n `
In the case of `[th](Coercions/#th-_LPAR_in-Coercions_RPAR_ "Definition of example")`, using ``Lean.Parser.Command.print : command```#print` demonstrates that evaluation of the function application is delayed until the thunk's value is requested:
``def th : ([Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := fun f x => [{](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk.mk") [fn](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk.fn") [:=](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk.mk") fun x_1 => f ↑x [}](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk.mk")`#print [th](Coercions/#th-_LPAR_in-Coercions_RPAR_ "Definition of example") `
```
def th : ([Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Thunk](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=
fun f x => [{](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk.mk") [fn](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk.fn") [:=](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk.mk") fun x_1 => f ↑x [}](Basic-Types/Lazy-Computations/#Thunk___mk "Documentation for Thunk.mk")
```

[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAKAdvAXPAcmALgSnXgElkd0BeeZAKFElgRUIDEBLVAawI2zLUpp1ocJCEKBG4G7wA8lBysA9qnEV4IatQAmwAGbwcACyR6MJMoCTCeAGUcAJ3YBzAojE9cUgCoGArsg7W7R1U9dWoFKGBUABlgMFR2WnBhRlRTbVJPYFsIVRpqAGIoe1J9AyA"\))
Coercions are not used to resolve [generalized field notation](Terms/Function-Application/#--tech-term-generalized-field-notation): only the inferred type of the term is considered. However, a [type ascription](Terms/Type-Ascription/#--tech-term-Type-ascriptions) can be used to trigger a coercion to the type that has the desired generalized field. Coercions are also not used to resolve `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat")` instances: even though there is a default instance for `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, a coercion from `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` to `α` does not allow natural number literals to be used for `α`.
Coercions and Generalized Field Notation
The name `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat").bdiv` is not defined, but `[Int.bdiv](Basic-Types/Integers/#Int___bdiv "Documentation for Int.bdiv")` exists. The coercion from `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` to `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` is not considered when looking up the field `bdiv`:
`example (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) := n.`Invalid field `bdiv`: The environment does not contain `Nat.bdiv`, so it is not possible to project the field `bdiv` from an expression   n of type `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")``bdiv 2 `
```
Invalid field `bdiv`: The environment does not contain `Nat.bdiv`, so it is not possible to project the field `bdiv` from an expression
  n
of type `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`
```

This is because coercions are only inserted when there is an expected type that differs from an inferred type, and generalized fields are resolved based on the inferred type of the term before the dot. Coercions can be triggered by adding a type ascription, which additionally causes the inferred type of the entire ascription term to be `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`, allowing the function `[Int.bdiv](Basic-Types/Integers/#Int___bdiv "Documentation for Int.bdiv")` to be found.
`example (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) := (n : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")).[bdiv](Basic-Types/Integers/#Int___bdiv "Documentation for Int.bdiv") 2 `
[Live ↪](javascript:openLiveLink\("KYDwhgtgDgNsAEAKAdvAXPAcmALgSnQF4lUMBJZfAOgCMATASwDd4AmIA"\))
Coercions and `OfNat`
`[Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example")` is an inductive type that represents binary numbers.
`inductive Bin where   | done   | zero : [Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") → [Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example")   | one : [Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") → [Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example")  def Bin.toString : [Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")   | [.done](Coercions/#Bin___done-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") => ""   | [.one](Coercions/#Bin___one-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") b => b.[toString](Coercions/#Bin___toString-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") ++ "1"   | [.zero](Coercions/#Bin___zero-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") b => b.[toString](Coercions/#Bin___toString-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") ++ "0"  instance : ToString [Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") where   toString     | [.done](Coercions/#Bin___done-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") => "0"     | b => [Bin.toString](Coercions/#Bin___toString-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") b `
Binary numbers can be converted to natural numbers by repeatedly applying `[Bin.succ](Coercions/#Bin___succ-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example")`:
`def Bin.succ (b : [Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example")) : [Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") b [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | [.done](Coercions/#Bin___done-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") => [Bin.done](Coercions/#Bin___done-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example").[one](Coercions/#Bin___one-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example")   | [.zero](Coercions/#Bin___zero-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") b => [.one](Coercions/#Bin___one-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") b   | [.one](Coercions/#Bin___one-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") b => [.zero](Coercions/#Bin___zero-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") b.[succ](Coercions/#Bin___succ-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example")  def Bin.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") n [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | 0 => .done   | n + 1 => ([Bin.ofNat](Coercions/#Bin___ofNat-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") n).[succ](Coercions/#Bin___succ-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") `
Even if `[Bin.ofNat](Coercions/#Bin___ofNat-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example")` is registered as a coercion, natural number literals cannot be used for `[Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example")`:
`[attribute](Attributes/#Lean___Parser___Command___attribute "Documentation for syntax") [[coe](Coercions/Coercing-Between-Types/#Lean___Attr___coe "Documentation for syntax")] [Bin.ofNat](Coercions/#Bin___ofNat-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example")  instance : [Coe](Coercions/#Coe___mk "Documentation for Coe") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") where   [coe](Coercions/#Coe___mk "Documentation for Coe.coe") := [Bin.ofNat](Coercions/#Bin___ofNat-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") ``[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (`failed to synthesize instance of type class   [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") [Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") 9 numerals are polymorphic in Lean, but the numeral `9` cannot be used in a context where the expected type is   [Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") due to the absence of the instance above  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`9 : [Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example")) `
```
failed to synthesize instance of type class
  [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") [Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") 9
numerals are polymorphic in Lean, but the numeral `9` cannot be used in a context where the expected type is
  [Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example")
due to the absence of the instance above

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```

This is because coercions are inserted in response to mismatched types, but a failure to synthesize an `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat")` instance is not a type mismatch.
The coercion can be used in the definition of the `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") [Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example")` instance:
`instance : [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") [Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example") n where   [ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") := n  `1010`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (10 : [Bin](Coercions/#Bin-_LPAR_in-Coercions-and--OfNat_RPAR_ "Definition of example")) `
```
1010
```

[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABAIVMg7gC0QJ0QChlkAfZMAexCJPIC99LkAuNDQJMJ2RizlqUbdCGRdhhQmEQAzbgDoYlAMow8oAOatuo5CrUh1vcnKo1kAXgB8yAEQ2jyOQOQAjC9ZcLlqjcgDUfrYAjPZ0jox4zG5Wrl56vgG2AAz2hKAAzjAAhiBQgsgAKt76msJYuAS8ivEGvGEmzjE2KXV80dbCcT4GrhJSsp3p0FDIABRuQqAAlFplLOa8ALZZMFDYrljAMNgODWYxnaaITjS7EVHujs4uu9eXcuexQ1BQfTLylNIAcitjImw/GAzSb/BYkZardYiTBbHZhJL3I4OESBIKXUadT6A5AgKZyZ6vSTvTqKbEgnSA3ZHS5JM5MDYxABMyAAVLFSStbmZ2shmWzPByYP5kEE3gNQA0IC4ADb5MpiUBUxrWPa0PiUbb4e6PDUVCSaygERbyQUAfQJpsQAEdzcNkABvCbcAC+WgFlGx5hxOk8BK8nu9qNYXpcAE9eKBVMxsABRK0R8DQODUDbqRA0PBZaXAei+EQAHgA3NZ0sBFgAHU1Z6X+LJqbbIADaJI9KwANPICQBdfW4Q2IY0twGmqhS2WWm2jmUoR2zUCutjugMiLieKey/2/L0iNnM+aucMkSORZCx+NHxOwYAptxpjNZnN55BFktlyvV2v19bNiWCjuHSgx0QHtCANI0Pm+FZTTNa0HX+ZBAQXMZMUgoVcU3IVt2DA8E0gK8UwLYtkFLCsq2lGsfxAJxUP/X9WxgWiqLNC1rVtF4QJWHwXAgGAUEbKBKGAiDKTSEBMhyPItAAYUEhDfjKHB8DVATBC9FCRIybJcnyAB5VDtGhCo1SxX59x4QgAGJEHgLMxiCBEQSmIA"\))
Most new coercions can be defined by declaring an instance of the `[Coe](Coercions/#Coe___mk "Documentation for Coe")` [type class](Type-Classes/#--tech-term-type-class) and applying the `coe` attribute to the function that performs the coercion. To enable more control over coercions or to enable them in more contexts, Lean provides further classes that can be implemented, described in the rest of this chapter.
Defining Coercions: Decimal Numbers
Decimal numbers can be defined as arrays of digits.
`structure Decimal where   digits : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 10) `
Adding a coercion allows them to be used in contexts that expect `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, but also contexts that expect any type that `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` can be coerced to.
`@[[coe](Coercions/Coercing-Between-Types/#Lean___Attr___coe "Documentation for syntax")] def Decimal.toNat (d : [Decimal](Coercions/#Decimal-_LPAR_in-Defining-Coercions___-Decimal-Numbers_RPAR_ "Definition of example")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") :=   d.[digits](Coercions/#Decimal___digits-_LPAR_in-Defining-Coercions___-Decimal-Numbers_RPAR_ "Definition of example").[foldl](Basic-Types/Arrays/#Array___foldl "Documentation for Array.foldl") (init := 0) fun n d => n * 10 + d.[val](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin.val")  instance : [Coe](Coercions/#Coe___mk "Documentation for Coe") [Decimal](Coercions/#Decimal-_LPAR_in-Defining-Coercions___-Decimal-Numbers_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") where   [coe](Coercions/#Coe___mk "Documentation for Coe.coe") := [Decimal.toNat](Coercions/#Decimal___toNat-_LPAR_in-Defining-Coercions___-Decimal-Numbers_RPAR_ "Definition of example") `
This can be demonstrated by treating a `[Decimal](Coercions/#Decimal-_LPAR_in-Defining-Coercions___-Decimal-Numbers_RPAR_ "Definition of example")` as an `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` as well as a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`:
`def twoHundredThirteen : [Decimal](Coercions/#Decimal-_LPAR_in-Defining-Coercions___-Decimal-Numbers_RPAR_ "Definition of example") where   [digits](Coercions/#Decimal___digits-_LPAR_in-Defining-Coercions___-Decimal-Numbers_RPAR_ "Definition of example") := #[2, 1, 3]  def one : [Decimal](Coercions/#Decimal-_LPAR_in-Defining-Coercions___-Decimal-Numbers_RPAR_ "Definition of example") where   [digits](Coercions/#Decimal___digits-_LPAR_in-Defining-Coercions___-Decimal-Numbers_RPAR_ "Definition of example") := #[1]  `-212`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ([one](Coercions/#one-_LPAR_in-Defining-Coercions___-Decimal-Numbers_RPAR_ "Definition of example") : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) - ([twoHundredThirteen](Coercions/#twoHundredThirteen-_LPAR_in-Defining-Coercions___-Decimal-Numbers_RPAR_ "Definition of example") : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) `
```
-212
```

[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgCLygSwLYEMA2iB3AC3gQChFEATdAc3RGEQC5EBBMMbAT0QAoAYugB2iAIwAGAJRkyAAQDaUAPbwAumSrwAZijRY8AOhDKActhD8qLPRhy4pN85eYBeCtUM16jQ9uW4VPh8IgwsrojSiNoQoqLWrgB8iKIAVOISiADUngBueLIioNjCUEisAMKqtgb4zoQk5JQq5RGodkYmzrJauiAEygASsVQIVAAqROhgIPDwoqzttQ2k8B7eDExuiADECgBMADTixwDMGpo6iMrC5TX2K03UdJvhuwpiFzvw+cE3dwBJYQgRwAWn4/SGIzGk2ms3mTgsUiAA"\))
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Coe.coe "Permalink")type class
```


Coe.{u, v} (α : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Sort u)) (β : Sort v) :
  Sort (max (max 1 u) v)


Coe.{u, v} (α : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Sort u))
  (β : Sort v) : Sort (max (max 1 u) v)


```

`[Coe](Coercions/#Coe___mk "Documentation for Coe") α β` is the typeclass for coercions from `α` to `β`. It can be transitively chained with other `[Coe](Coercions/#Coe___mk "Documentation for Coe")` instances, and coercion is automatically used when `x` has type `α` but it is used in a context where `β` is expected. You can use the `↑x` operator to explicitly trigger coercion.
#  Instance Constructor

```
[Coe.mk](Coercions/#Coe___mk "Documentation for Coe.mk").{u, v}
```

#  Methods

```
coe : α → β
```

Coerces a value of type `α` to type `β`. Accessible by the notation `↑x`, or by double type ascription `((x : α) : β)`.
  1. [11.1. Coercion Insertion](Coercions/Coercion-Insertion/#coercion-insertion)
  2. [11.2. Coercing Between Types](Coercions/Coercing-Between-Types/#ordinary-coercion)
  3. [11.3. Coercing to Sorts](Coercions/Coercing-to-Sorts/#sort-coercion)
  4. [11.4. Coercing to Function Types](Coercions/Coercing-to-Function-Types/#fun-coercion)
  5. [11.5. Implementation Details](Coercions/Implementation-Details/#coercion-impl-details)

[←10.5. Basic Classes](Type-Classes/Basic-Classes/#basic-classes "10.5. Basic Classes")[11.1. Coercion Insertion→](Coercions/Coercion-Insertion/#coercion-insertion "11.1. Coercion Insertion")

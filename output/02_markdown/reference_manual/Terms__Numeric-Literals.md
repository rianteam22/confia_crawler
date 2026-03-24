[←13.4. Function Application](Terms/Function-Application/#function-application "13.4. Function Application")[13.6. Structures and Constructors→](Terms/Structures-and-Constructors/#The-Lean-Language-Reference--Terms--Structures-and-Constructors "13.6. Structures and Constructors")
#  13.5. Numeric Literals[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Terms--Numeric-Literals "Permalink")
There are two kinds of numeric literal: natural number literals and scientific literals. Both are overloaded via [type classes](Type-Classes/#--tech-term-type-class).
##  13.5.1. Natural Numbers[🔗](find/?domain=Verso.Genre.Manual.section&name=nat-literals "Permalink")
Natural numbers can be specified in several forms:
  * A sequence of digits 0 through 9 is a decimal literal
  * `0b` or `0B` followed by a sequence of one or more 0s and 1s is a binary literal
  * `0o` or `0O` followed by a sequence of one or more digits 0 through 7 is an octal literal
  * `0x` or `0X` followed by a sequence of one or more hex digits (0 through 9 and A through F, case-insensitive) is a hexadecimal literal


All numeric literals can also contain internal underscores, except for between the first two characters in a binary, octal, or hexadecimal literal. These are intended to help groups of digits in natural ways, for instance `1_000_000` or `0x_c0de_cafe`. (While it is possible to write the number 123 as `1_2__3`, this is not recommended.)
When Lean encounters a natural number literal `n`, it interprets it via the overloaded method `[OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") n`. A [default instance](Type-Classes/Instance-Synthesis/#--tech-term-default-instances) of `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") n` ensures that the type `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` can be inferred when no other type information is present.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=OfNat.ofNat "Permalink")type class
```


OfNat.{u} (α : Type u) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Type u


OfNat.{u} (α : Type u) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Type u


```

The class `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") α n` powers the numeric literal parser. If you write `37 : α`, Lean will attempt to synthesize `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") α 37`, and will generate the term `([OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") 37 : α)`.
There is a bit of infinite regress here since the desugaring apparently still contains a literal `37` in it. The type of expressions contains a primitive constructor for "raw natural number literals", which you can directly access using the macro `nat_lit 37`. Raw number literals are always of type `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`. So it would be more correct to say that Lean looks for an instance of `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") α (nat_lit 37)`, and it generates the term `([OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") (nat_lit 37) : α)`.
#  Instance Constructor

```
[OfNat.mk](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.mk").{u}
```

#  Methods

```
ofNat : α
```

The `[OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat")` function is automatically inserted by the parser when the user writes a numeric literal like `1 : α`. Implementations of this typeclass can therefore customize the behavior of `n : α` based on `n` and `α`.
Custom Natural Number Literals
The structure `[NatInterval](Terms/Numeric-Literals/#NatInterval-_LPAR_in-Custom-Natural-Number-Literals_RPAR_ "Definition of example")` represents an interval of natural numbers.
`structure NatInterval where   low : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   high : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   low_le_high : low ≤ high  instance : [Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") [NatInterval](Terms/Numeric-Literals/#NatInterval-_LPAR_in-Custom-Natural-Number-Literals_RPAR_ "Definition of example") where   [add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add.add")     | ⟨lo1, hi1, le1⟩, ⟨lo2, hi2, le2⟩ =>       ⟨lo1 + lo2, hi1 + hi2, bylo1:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")hi1:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")le1:lo1 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") hi1lo2:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")hi2:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")le2:lo2 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") hi2⊢ lo1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") lo2 [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") hi1 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") hi2 [grind](Tactic-Proofs/Tactic-Reference/#grind "Documentation for tactic")All goals completed! 🐙⟩ `
An `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat")` instance allows natural number literals to be used to represent intervals:
`instance : [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") [NatInterval](Terms/Numeric-Literals/#NatInterval-_LPAR_in-Custom-Natural-Number-Literals_RPAR_ "Definition of example") n where   [ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") := ⟨n, n, byn:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")⊢ n [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") n [omega](Tactic-Proofs/Tactic-Reference/#omega "Documentation for tactic")All goals completed! 🐙⟩ ```{ low := 8, high := 8, low_le_high := _ }`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (8 : [NatInterval](Terms/Numeric-Literals/#NatInterval-_LPAR_in-Custom-Natural-Number-Literals_RPAR_ "Definition of example")) `
```
{ low := 8, high := 8, low_le_high := _ }
```
``{ low := 7, high := 7, low_le_high := _ }`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (0b111 : [NatInterval](Terms/Numeric-Literals/#NatInterval-_LPAR_in-Custom-Natural-Number-Literals_RPAR_ "Definition of example")) `
```
{ low := 7, high := 7, low_le_high := _ }
```

[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgHIEMQEkB2J5gG6oA2iA7gBZ7wBQiiRA9qYgFwrq2LkCWA5ua3YhOjUgH0i8MT36DRiQCZEXPuWrVuWUKixQkbAIIATQ0Oy4CxMpQSdUxznQA+iQBfkjAIwAaZV/rx3gJfk3m4MAEzePOF+oQGIALwAfA50rh6IANT0YRHc7hnKUQBGAJ6IvGAahgFqGlo6eogA8gBmaCCmOHiEJFhWVJwMreisca5Y3uOIJYgMALbwvKjV1ADE8N2IABQAHIJtZl3EAJRqaxubAAyF7jd76AcWREdAA"\))
There are no separate integer literals. Terms such as `-5` consist of a prefix negation (which can be overloaded via the `[Neg](Type-Classes/Basic-Classes/#Neg___mk "Documentation for Neg")` type class) applied to a natural number literal.
##  13.5.2. Scientific Numbers[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Terms--Numeric-Literals--Scientific-Numbers "Permalink")
Scientific number literals consist of a sequence of decimal digits followed (without intervening whitespace) by an optional decimal part (a period followed by zero or more decimal digits) and an optional exponent part (the letter `e` followed by an optional `+` or `-` and then followed by one or more decimal digits). Scientific numbers are overloaded via the `[OfScientific](Terms/Numeric-Literals/#OfScientific___mk "Documentation for OfScientific")` type class.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=OfScientific.ofScientific "Permalink")type class
```


OfScientific.{u} (α : Type u) : Type u


OfScientific.{u} (α : Type u) : Type u


```

For decimal and scientific numbers (e.g., `1.23`, `3.12e10`). Examples:
  * `1.23` is syntax for `[OfScientific.ofScientific](Terms/Numeric-Literals/#OfScientific___mk "Documentation for OfScientific.ofScientific") (nat_lit 123) [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") (nat_lit 2)`
  * `121e100` is syntax for `[OfScientific.ofScientific](Terms/Numeric-Literals/#OfScientific___mk "Documentation for OfScientific.ofScientific") (nat_lit 121) [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") (nat_lit 100)`


Note the use of `nat_lit`; there is no wrapping `[OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat")` in the resulting term.
#  Instance Constructor

```
[OfScientific.mk](Terms/Numeric-Literals/#OfScientific___mk "Documentation for OfScientific.mk").{u}
```

#  Methods

```
ofScientific : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → α
```

Produces a value from the given mantissa, exponent sign, and decimal exponent. For the exponent sign, `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` indicates a negative exponent.
Examples:
  * `1.23` is syntax for `[OfScientific.ofScientific](Terms/Numeric-Literals/#OfScientific___mk "Documentation for OfScientific.ofScientific") (nat_lit 123) [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") (nat_lit 2)`
  * `121e100` is syntax for `[OfScientific.ofScientific](Terms/Numeric-Literals/#OfScientific___mk "Documentation for OfScientific.ofScientific") (nat_lit 121) [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") (nat_lit 100)`


Note the use of `nat_lit`; there is no wrapping `[OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat")` in the resulting term.
There are an `[OfScientific](Terms/Numeric-Literals/#OfScientific___mk "Documentation for OfScientific")` instances for `[Float](Basic-Types/Floating-Point-Numbers/#Float-next "Documentation for Float")` and `[Float32](Basic-Types/Floating-Point-Numbers/#Float32 "Documentation for Float32")`, but no separate floating-point literals.
##  13.5.3. Strings[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Terms--Numeric-Literals--Strings "Permalink")
String literals are described in the [chapter on strings.](Basic-Types/Strings/#string-syntax)
##  13.5.4. Lists and Arrays[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Terms--Numeric-Literals--Lists-and-Arrays "Permalink")
List and array literals contain comma-separated sequences of elements inside of brackets, with arrays prefixed by a hash mark (`#`). Array literals are interpreted as list literals wrapped in a call to a conversion. For performance reasons, very large list and array literals are converted to sequences of local definitions, rather than just iterated applications of the list constructor.
syntaxList Literals

```
term ::= ...
    | 


The syntax [a, b, c] is shorthand for a :: b :: c :: [], or
List.cons a (List.cons b (List.cons c List.nil)). It allows conveniently constructing
list literals.


For lists of length at least 64, an alternative desugaring strategy is used
which uses let bindings as intermediates as in
let left := [d, e, f]; a :: b :: c :: left to avoid creating very deep expressions.
Note that this changes the order of evaluation, although it should not be observable
unless you use side effecting operations like dbg_trace.


Conventions for notations in identifiers:




  * 

The recommended spelling of [] in identifiers is nil.




  * 

The recommended spelling of [a] in identifiers is singleton.






[term,*]
```

syntaxArray Literals

```
term ::= ...
    | 


Syntax for Array α. 


Conventions for notations in identifiers:




  * 

The recommended spelling of #[] in identifiers is empty.




  * 

The recommended spelling of #[x] in identifiers is singleton.






#[term,*]
```

Long List Literals
This list contains 32 elements. The generated code is an iterated application of `[List.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")`:
``[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1] `
```
[[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

With 33 elements, the list literal becomes a sequence of local definitions:
``let y :=   let y :=     let y := [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons");     1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") y;   let y := 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") y;   1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") y; let y :=   let y := 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") y;   1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") y; let y := 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") y; 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") y : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1, 1] `
```
let y :=
  let y :=
    let y := [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons");
    1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") y;
  let y := 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") y;
  1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") y;
let y :=
  let y := 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") y;
  1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") y;
let y := 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") y;
1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") 1 [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") y : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

[Live ↪](javascript:openLiveLink\("MQYwFgpiDWBQAE8DaBGANOzHtYYrBO2e8hZxipR5KAurLKJDHqte+iTe1xz5d0JdaQA"\))
[←13.4. Function Application](Terms/Function-Application/#function-application "13.4. Function Application")[13.6. Structures and Constructors→](Terms/Structures-and-Constructors/#The-Lean-Language-Reference--Terms--Structures-and-Constructors "13.6. Structures and Constructors")

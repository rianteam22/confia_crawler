[←23.1. Custom Operators](Notations-and-Macros/Custom-Operators/#operators "23.1. Custom Operators")[23.3. Notations→](Notations-and-Macros/Notations/#notations "23.3. Notations")
#  23.2. Precedence[🔗](find/?domain=Verso.Genre.Manual.section&name=precedence "Permalink")
Infix operators, notations, and other syntactic extensions to Lean make use of explicit [precedence](Notations-and-Macros/Custom-Operators/#--tech-term-precedence) annotations. While precedences in Lean can technically be any natural number, by convention they range from 10 to 1024, respectively denoted `min` and `max`. Function application has the highest precedence.
syntaxParser Precedences
Most operator precedences consist of explicit numbers. The named precedence levels denote the outer edges of the range, close to the minimum or maximum, and are typically used by more involved syntax extensions.

```
prec ::=
    num
```

Precedences may also be denoted as sums or differences of precedences; these are typically used to assign precedences that are relative to one of the named precedences.

```
prec ::= ...
    | 


Addition of precedences. This is normally used only for offsetting, e.g. max + 1. 


prec + prec
```

```
prec ::= ...
    | 


Subtraction of precedences. This is normally used only for offsetting, e.g. max - 1. 


prec - prec
```

```
prec ::= ...
    | 


Parentheses are used for grouping precedence expressions. 


(prec)
```

The maximum precedence is used to parse terms that occur in a function position. Operators should typically not use this level, because it can interfere with users' expectation that function application binds more tightly than any other operator, but it is useful in more involved syntax extensions to indicate how other constructs interact with function application.

```
prec ::= ...
    | 


Maximum precedence used in term parsers, in particular for terms in
function position (ident, paren, ...)


max
```

Argument precedence is one less than the maximum precedence. This level is useful for defining syntax that should be treated as an argument to a function, such as ``Lean.Parser.Term.fun : term```fun` or ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do).

```
prec ::= ...
    | 


Precedence used for application arguments (do, by, ...). 


arg
```

Lead precedence is less than argument precedence, and should be used for custom syntax that should not occur as a function argument, such as ``Lean.Parser.Term.let : term`
`let` is used to declare a local definition. Example:

```
let x := 1
let y := x + 1
x + y

```

Since functions are first class citizens in Lean, you can use `let` to declare local functions too.

```
let double := fun x => 2*x
double (double 3)

```

For recursive definitions, you should use `let rec`. You can also perform pattern matching using `let`. For example, assume `p` has type `Nat × Nat`, then you can write

```
let (x, y) := p
x + y

```

The _anaphoric let_ `let := v` defines a variable called `this`.
``let`.

```
prec ::= ...
    | 


Precedence used for terms not supposed to be used as arguments (let, have, ...). 


lead
```

The minimum precedence can be used to ensure that an operator binds less tightly than all other operators.

```
prec ::= ...
    | 


Minimum precedence used in term parsers. 


min
```

[←23.1. Custom Operators](Notations-and-Macros/Custom-Operators/#operators "23.1. Custom Operators")[23.3. Notations→](Notations-and-Macros/Notations/#notations "23.3. Notations")

[←13.2. Function Types](Terms/Function-Types/#function-types "13.2. Function Types")[13.4. Function Application→](Terms/Function-Application/#function-application "13.4. Function Application")
#  13.3. Functions[🔗](find/?domain=Verso.Genre.Manual.section&name=function-terms "Permalink")
Terms with function types can be created via abstractions, introduced with the ``Lean.Parser.Term.fun : term```fun` keyword.In various communities, function abstractions are also known as _lambdas_ , due to Alonzo Church's notation for them, or _anonymous functions_ because they don't need to be defined with a name in the global environment. While abstractions in the core type theory only allow a single variable to be bound, function terms are quite flexible in the high-level Lean syntax.
syntaxFunction Abstraction
The most basic function abstraction introduces a variable to stand for the function's parameter:

```
term ::= ...
    | fun ident => term
```

At elaboration time, Lean must be able to determine the function's domain. A type ascription is one way to provide this information:

```
term ::= ...
    | fun ident : term => term
```

Function definitions defined with keywords such as ``Lean.Parser.Command.definition : command```def` desugar to ``Lean.Parser.Term.fun : term```fun`. Inductive type declarations, on the other hand, introduce new values with function types (constructors and type constructors) that cannot themselves be implemented using just ``Lean.Parser.Term.fun : term```fun`.
syntaxCurried Functions
Multiple parameter names are accepted after ``Lean.Parser.Term.fun : term```fun`:

```
term ::= ...
    | fun ident ident* => term
```

```
term ::= ...
    | fun ident ident* : term => term
```

Different type annotations for multiple parameters require parentheses:

```
term ::= ...
    | fun (ident* : term) =>term
```

These are equivalent to writing nested ``Lean.Parser.Term.fun : term```fun` terms.
The ``Lean.Parser.Term.fun : term```=>` may be replaced by ``Lean.Parser.Term.fun : term```↦` in all of the syntax described in this section.
Function abstractions may also use pattern matching syntax as part of their parameter specification, avoiding the need to introduce a local variable that is immediately destructured. This syntax is described in the [section on pattern matching](Terms/Pattern-Matching/#pattern-fun).
##  13.3.1. Implicit Parameters[🔗](find/?domain=Verso.Genre.Manual.section&name=implicit-functions "Permalink")
Lean supports implicit parameters to functions. This means that Lean itself can supply arguments to functions, rather than requiring users to supply all needed arguments. Implicit parameters come in three varieties: 

Ordinary implicit parameters
    
Ordinary implicit parameters are function parameters that Lean should determine values for via unification. In other words, each call site should have exactly one potential argument value that would cause the function call as a whole to be well-typed. The Lean elaborator attempts to find values for all implicit arguments at each occurrence of a function. Ordinary implicit parameters are written in curly braces (`{` and `}`). 

Strict implicit parameters
    
_Strict implicit_ parameters are identical to ordinary implicit parameters, except Lean will only attempt to find argument values when subsequent explicit arguments are provided at a call site. Strict implicit parameters are written in double curly braces (`⦃` and `⦄`, or `{{` and `}}`). 

Instance implicit parameters
    
Arguments for [_instance implicit_](Type-Classes/#--tech-term-instance-implicit) parameters are found via [type class synthesis](Type-Classes/Instance-Synthesis/#instance-synth). Instance implicit parameters are written in square brackets (`[` and `]`). Unlike the other kinds of implicit parameter, instance implicit parameters that are written without a `:` specify the parameter's type rather than providing a name. Furthermore, only a single name is allowed. Most instance implicit parameters omit the parameter name because instances synthesized as parameters to functions are already available in the functions' bodies, even without being named explicitly. Ordinary vs Strict Implicit Parameters
The difference between the functions `[f](Terms/Functions/#f-_LPAR_in-Ordinary-vs-Strict-Implicit-Parameters_RPAR_ "Definition of example")` and `[g](Terms/Functions/#g-_LPAR_in-Ordinary-vs-Strict-Implicit-Parameters_RPAR_ "Definition of example")` is that `α` is strictly implicit in `[f](Terms/Functions/#f-_LPAR_in-Ordinary-vs-Strict-Implicit-Parameters_RPAR_ "Definition of example")`:
`def f ⦃α : Type⦄ : α → α := fun x => x def g {α : Type} : α → α := fun x => x `
These functions are elaborated identically when applied to concrete arguments:
`example : [f](Terms/Functions/#f-_LPAR_in-Ordinary-vs-Strict-Implicit-Parameters_RPAR_ "Definition of example") 2 = [g](Terms/Functions/#g-_LPAR_in-Ordinary-vs-Strict-Implicit-Parameters_RPAR_ "Definition of example") 2 := [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
However, when the explicit argument is not provided, uses of `[f](Terms/Functions/#f-_LPAR_in-Ordinary-vs-Strict-Implicit-Parameters_RPAR_ "Definition of example")` do not require the implicit `α` to be solved:
`example := [f](Terms/Functions/#f-_LPAR_in-Ordinary-vs-Strict-Implicit-Parameters_RPAR_ "Definition of example") `
However, uses of `g` do require it to be solved, and fail to elaborate if there is insufficient information available:
``Failed to infer type of example`example := `don't know how to synthesize implicit argument `α`   @[g](Terms/Functions/#g-_LPAR_in-Ordinary-vs-Strict-Implicit-Parameters_RPAR_ "Definition of example") ?m.3 context: ⊢ Type`[g](Terms/Functions/#g-_LPAR_in-Ordinary-vs-Strict-Implicit-Parameters_RPAR_ "Definition of example") `
```
don't know how to synthesize implicit argument `α`
  @[g](Terms/Functions/#g-_LPAR_in-Ordinary-vs-Strict-Implicit-Parameters_RPAR_ "Definition of example") ?m.3
context:
⊢ Type
```

[Live ↪](javascript:openLiveLink\("CYUwZgBJjBlIjcAQLggFQJ4AcSBDKRF6CTCPRAXigFcA7CADwmID4aAoUSAcwgG94k1MBfXASIJSYSjTqNqTJiGoBDALboANiFyQATHQgcdoiACcwq2fOVqNhsEA"\))
syntaxFunctions with Varying Binders
The most general syntax for ``Lean.Parser.Term.fun : term```fun` accepts a sequence of binders:

```
term ::= ...
    | fun funBinder funBinder* => term
```

syntaxFunction Binders
Function binders may be identifiers:

```
funBinder ::= ...
    | ident
```

parenthesized sequences of identifiers:

```
funBinder ::= ...
    | 


Parentheses, used for grouping expressions (e.g., a * (b + c)).
Can also be used for creating simple functions when combined with ·. Here are some examples:




  * 
(· + 1) is shorthand for fun x => x + 1



  * 
(· + ·) is shorthand for fun x y => x + y



  * 
(f · a b) is shorthand for fun x => f x a b



  * 
(h (· + 1) ·) is shorthand for fun x => h (fun y => y + 1) x



  * also applies to other parentheses-like notations such as (·, 1) and (· : Nat → Nat)





([anonymous]ident ident*)
```

sequences of identifiers with a type ascription:

```
funBinder ::= ...
    | 


Type ascription notation: (0 : Int) instructs Lean to process 0 as a value of type Int.
An empty type ascription (e :) elaborates e without the expected type.
This is occasionally useful when Lean's heuristics for filling arguments from the expected type
do not yield the right result.


([anonymous]ident ident* : term)
```

implicit parameters, with or without a type ascription:

```
funBinder ::= ...
    | 


Implicit binder, like {x y : A} or {x y}.
In regular applications, whenever all parameters before it have been specified,
then a _ placeholder is automatically inserted for this parameter.
Implicit parameters should be able to be determined from the other arguments and the return type
by unification.


In @ explicit mode, implicit binders behave like explicit binders.


{ident ident*}
```

```
funBinder ::= ...
    | 


Implicit binder, like {x y : A} or {x y}.
In regular applications, whenever all parameters before it have been specified,
then a _ placeholder is automatically inserted for this parameter.
Implicit parameters should be able to be determined from the other arguments and the return type
by unification.


In @ explicit mode, implicit binders behave like explicit binders.


{ident ident* : term}
```

instance implicits, anonymous or named:

```
funBinder ::= ...
    | 


Instance-implicit binder, like [C] or [inst : C].
In regular applications without @ explicit mode, it is automatically inserted
and solved for by typeclass inference for the specified class C.
In @ explicit mode, if _ is used for an instance-implicit parameter, then it is still solved for by typeclass inference;
use (_) to inhibit this and have it be solved for by unification instead, like an implicit argument.


[term]
```

```
funBinder ::= ...
    | 


Instance-implicit binder, like [C] or [inst : C].
In regular applications without @ explicit mode, it is automatically inserted
and solved for by typeclass inference for the specified class C.
In @ explicit mode, if _ is used for an instance-implicit parameter, then it is still solved for by typeclass inference;
use (_) to inhibit this and have it be solved for by unification instead, like an implicit argument.


[ident : term]
```

or strict implicit parameters, with or without a type ascription:

```
funBinder ::= ...
    | 


Strict-implicit binder, like ⦃x y : A⦄ or ⦃x y⦄.
In contrast to { ... } implicit binders, strict-implicit binders do not automatically insert
a _ placeholder until at least one subsequent explicit parameter is specified.
Do _not_ use strict-implicit binders unless there is a subsequent explicit parameter.
Assuming this rule is followed, for fully applied expressions implicit and strict-implicit binders have the same behavior.


Example: If h : ∀ ⦃x : A⦄, x ∈ s → p x and hs : y ∈ s,
then h by itself elaborates to itself without inserting _ for the x : A parameter,
and h hs has type p y.
In contrast, if h' : ∀ {x : A}, x ∈ s → p x, then h by itself elaborates to have type ?m ∈ s → p ?m
with ?m a fresh metavariable.


⦃ident ident*⦄
```

```
funBinder ::= ...
    | 


Strict-implicit binder, like ⦃x y : A⦄ or ⦃x y⦄.
In contrast to { ... } implicit binders, strict-implicit binders do not automatically insert
a _ placeholder until at least one subsequent explicit parameter is specified.
Do _not_ use strict-implicit binders unless there is a subsequent explicit parameter.
Assuming this rule is followed, for fully applied expressions implicit and strict-implicit binders have the same behavior.


Example: If h : ∀ ⦃x : A⦄, x ∈ s → p x and hs : y ∈ s,
then h by itself elaborates to itself without inserting _ for the x : A parameter,
and h hs has type p y.
In contrast, if h' : ∀ {x : A}, x ∈ s → p x, then h by itself elaborates to have type ?m ∈ s → p ?m
with ?m a fresh metavariable.


⦃ident* : term⦄
```

As usual, an `_` may be used instead of an identifier to create an anonymous parameter, and `⦃` and `⦄` may alternatively be written using `{{` and `}}`, respectively.
Lean's core language does not distinguish between implicit, instance, and explicit parameters: the various kinds of function and function type are definitionally equal. The differences can be observed only during elaboration.
If the expected type of a function includes implicit parameters, but its binders do not, then the resulting function may end up with more parameters than the binders indicated in the code. This is because the implicit parameters are added automatically.
Implicit Parameters from Types
The identity function can be written with a single explicit parameter. As long as its type is known, the implicit type parameter is added automatically.
``fun {α} x => x : {α : Type} → α → α`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") (fun x => x : {α : Type} → α → α) `
```
fun {α} x => x : {α : Type} → α → α
```

The following are all equivalent:
``fun {α} x => x : {α : Type} → α → α`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") (fun {α} x => x : {α : Type} → α → α) `
```
fun {α} x => x : {α : Type} → α → α
```
``fun {α} x => x : {α : Type} → α → α`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") (fun {α} (x : α) => x : {α : Type} → α → α) `
```
fun {α} x => x : {α : Type} → α → α
```
``fun {α} x => x : {α : Type} → α → α`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") (fun {α : Type} (x : α) => x : {α : Type} → α → α) `
```
fun {α} x => x : {α : Type} → α → α
```

[Live ↪](javascript:openLiveLink\("MQYwFgpiDWAEAUAzArgO1gD1gXgHydgC5YBvQRuAjYAVATwAcIBfWQJMJYK2yBKAKB9EgwEKdOWZY8BYuUq0GzTq3a9+4KHCRpSZZvCzFuOfPu2z6TJR2V8B64VpnE5FvZUOSTj6uYXtLXIA"\))
[←13.2. Function Types](Terms/Function-Types/#function-types "13.2. Function Types")[13.4. Function Application→](Terms/Function-Application/#function-application "13.4. Function Application")

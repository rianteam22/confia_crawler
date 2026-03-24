[←13.1. Identifiers](Terms/Identifiers/#identifiers-and-resolution "13.1. Identifiers")[13.3. Functions→](Terms/Functions/#function-terms "13.3. Functions")
#  13.2. Function Types[🔗](find/?domain=Verso.Genre.Manual.section&name=function-types "Permalink")
Lean's function types describe more than just the function's domain and codomain. They also provide instructions for elaborating application sites by indicating that some parameters are to be discovered automatically via unification or [type class synthesis](Type-Classes/Instance-Synthesis/#instance-synth), that others are optional with default values, and that yet others should be synthesized using a custom tactic script. Furthermore, their syntax contains support for abbreviating [curried](The-Type-System/Functions/#--tech-term-currying) functions.
syntaxFunction types
Dependent function types include an explicit name:

```
term ::= ...
    | 


Explicit binder, like (x y : A) or (x y).
Default values can be specified using (x : A := v) syntax, and tactics using (x : A := by tac).


(ident : term) → term
```

Non-dependent function types do not:

```
term ::= ...
    | term → term
```

syntaxCurried Function Types
Dependent function types may include multiple parameters that have the same type in a single set of parentheses:

```
term ::= ...
    | 


Explicit binder, like (x y : A) or (x y).
Default values can be specified using (x : A := v) syntax, and tactics using (x : A := by tac).


(ident* : term) → term
```

This is equivalent to repeating the type annotation for each parameter name in a nested function type.
syntaxImplicit, Optional, and Auto Parameters
Function types can describe functions that take implicit, instance implicit, optional, and automatic parameters. All but instance implicit parameters require one or more names.

```
term ::= ...
    | 


Explicit binder, like (x y : A) or (x y).
Default values can be specified using (x : A := v) syntax, and tactics using (x : A := by tac).


(ident* : term := term) → term
```

```
term ::= ...
    | 


Explicit binder, like (x y : A) or (x y).
Default values can be specified using (x : A := v) syntax, and tactics using (x : A := by tac).


(ident* : term := by 


A sequence of tactics in brackets, or a delimiter-free indented sequence of tactics.
Delimiter-free indentation is determined by the _first_ tactic of the sequence. 


tacticSeq) → term
```

```
term ::= ...
    | 


Implicit binder, like {x y : A} or {x y}.
In regular applications, whenever all parameters before it have been specified,
then a _ placeholder is automatically inserted for this parameter.
Implicit parameters should be able to be determined from the other arguments and the return type
by unification.


In @ explicit mode, implicit binders behave like explicit binders.


{ident* : term} → term
```

```
term ::= ...
    | 


Instance-implicit binder, like [C] or [inst : C].
In regular applications without @ explicit mode, it is automatically inserted
and solved for by typeclass inference for the specified class C.
In @ explicit mode, if _ is used for an instance-implicit parameter, then it is still solved for by typeclass inference;
use (_) to inhibit this and have it be solved for by unification instead, like an implicit argument.


[term] → term
```

```
term ::= ...
    | 


Instance-implicit binder, like [C] or [inst : C].
In regular applications without @ explicit mode, it is automatically inserted
and solved for by typeclass inference for the specified class C.
In @ explicit mode, if _ is used for an instance-implicit parameter, then it is still solved for by typeclass inference;
use (_) to inhibit this and have it be solved for by unification instead, like an implicit argument.


[ident : term] → term
```

```
term ::= ...
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


⦃ident* : term⦄ → term
```

Multiple Parameters, Same Type
The type of `[Nat.add](Basic-Types/Natural-Numbers/#Nat___add "Documentation for Nat.add")` can be written in the following ways:
  * `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`
  * `(a : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → (b : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`
  * `(a b : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`


The last two types allow the function to be used with [named arguments](Terms/Function-Application/#--tech-term-named-arguments); aside from this, all three are equivalent.
[←13.1. Identifiers](Terms/Identifiers/#identifiers-and-resolution "13.1. Identifiers")[13.3. Functions→](Terms/Functions/#function-terms "13.3. Functions")

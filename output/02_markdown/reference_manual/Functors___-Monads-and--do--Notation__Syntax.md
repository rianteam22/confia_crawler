[←18.2. Lifting Monads](Functors___-Monads-and--do--Notation/Lifting-Monads/#lifting-monads "18.2. Lifting Monads")[18.4. API Reference→](Functors___-Monads-and--do--Notation/API-Reference/#The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--API-Reference "18.4. API Reference")
#  18.3. Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Syntax "Permalink")
Lean supports programming with functors, applicative functors, and monads via special syntax:
  * Infix operators are provided for the most common operations.
  * An embedded language called [``Lean.Parser.Term.do : term``](Functors___-Monads-and--do--Notation/Syntax/#--tech-term-do-notation)[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do)-notation allows the use of imperative syntax when writing programs in a monad.


##  18.3.1. Infix Operators[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Syntax--Infix-Operators "Permalink")
Infix operators are primarily useful in smaller expressions, or when there is no `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")` instance.
###  18.3.1.1. Functors[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Syntax--Infix-Operators--Functors "Permalink")
There are two infix operators for `[Functor.map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map")`.
syntaxFunctor Operators
`g <$> x` is short for `[Functor.map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") g x`.

```
term ::= ...
    | 


Applies a function inside a functor. This is used to overload the <$> operator.


When mapping a constant function, use Functor.mapConst instead, because it may be more
efficient.


Conventions for notations in identifiers:




  * The recommended spelling of <$> in identifiers is map.




term <$> term
```

`x <&> g` is short for `[Functor.map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map") g x`.

```
term ::= ...
    | 


Maps a function over a functor, with parameters swapped so that the function comes last.


This function is Functor.map with the parameters reversed, typically used via the <&> operator.


Conventions for notations in identifiers:




  * The recommended spelling of <&> in identifiers is mapRev.




term <&> term
```

###  18.3.1.2. Applicative Functors[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Syntax--Infix-Operators--Applicative-Functors "Permalink")
syntaxApplicative Operators
`g <*> x` is short for `[Seq.seq](Functors___-Monads-and--do--Notation/#Seq___mk "Documentation for Seq.seq") g (fun () => x)`. The function is inserted to delay evaluation because control might not reach the argument.

```
term ::= ...
    | 


The implementation of the <*> operator.


In a monad, mf <*> mx is the same as do let f ← mf; x ← mx; pure (f x): it evaluates the
function first, then the argument, and applies one to the other.


To avoid surprising evaluation semantics, mx is taken "lazily", using a Unit → f α function.


Conventions for notations in identifiers:




  * The recommended spelling of <*> in identifiers is seq.




term <*> term
```

`e1 *> e2` is short for `[SeqRight.seqRight](Functors___-Monads-and--do--Notation/#SeqRight___mk "Documentation for SeqRight.seqRight") e1 (fun () => e2)`.

```
term ::= ...
    | 


Sequences the effects of two terms, discarding the value of the first. This function is usually
invoked via the *> operator.


Given x : f α and y : f β, x *> y runs x, then runs y, and finally returns the result of
y.


The evaluation of the second argument is delayed by wrapping it in a function, enabling
“short-circuiting” behavior from f.


Conventions for notations in identifiers:




  * The recommended spelling of *> in identifiers is seqRight.




term *> term
```

`e1 <* e2` is short for `[SeqLeft.seqLeft](Functors___-Monads-and--do--Notation/#SeqLeft___mk "Documentation for SeqLeft.seqLeft") e1 (fun () => e2)`.

```
term ::= ...
    | 


Sequences the effects of two terms, discarding the value of the second. This function is usually
invoked via the <* operator.


Given x : f α and y : f β, x <* y runs x, then runs y, and finally returns the result of
x.


The evaluation of the second argument is delayed by wrapping it in a function, enabling
“short-circuiting” behavior from f.


Conventions for notations in identifiers:




  * The recommended spelling of <* in identifiers is seqLeft.




term <* term
```

Many applicative functors also support failure and recovery via the `[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative")` type class. This class also has an infix operator.
syntaxAlternative Operators
`e <|> e'` is short for `OrElse.orElse e (fun () => e')`. The function is inserted to delay evaluation because control might not reach the argument.

```
term ::= ...
    | 


a <|> b executes a and returns the result, unless it fails in which
case it executes and returns b. Because b is not always executed, it
is passed as a thunk so it can be forced only when needed.
The meaning of this notation is type-dependent. 


Conventions for notations in identifiers:




  * The recommended spelling of <|> in identifiers is orElse.




term <|> term
```

`structure User where   name : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")   favoriteNat : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") def main : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") () `Infix `Functor` and `Applicative` Operators
A common functional programming idiom is to use a pure function in some context with effects by applying it via `[Functor.map](Functors___-Monads-and--do--Notation/#Functor___mk "Documentation for Functor.map")` and `[Seq.seq](Functors___-Monads-and--do--Notation/#Seq___mk "Documentation for Seq.seq")`. The function is applied to its sequence of arguments using `<$>`, and the arguments are separated by `<*>`.
In this example, the constructor `User.mk` is applied via this idiom in the body of `[main](Functors___-Monads-and--do--Notation/Syntax/#main-_LPAR_in-Infix--Functor--and--Applicative--Operators_RPAR_ "Definition of example")`.
`def getName : [IO](IO/Logical-Model/#IO "Documentation for IO") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "What is your name?"   return (← (← [IO.getStdin](IO/Files___-File-Handles___-and-Streams/#IO___getStdin "Documentation for IO.getStdin")).[getLine](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream.getLine")).[trimAsciiEnd](Basic-Types/Strings/#String___trimAsciiEnd "Documentation for String.trimAsciiEnd").[copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")  partial def getFavoriteNat : [IO](IO/Logical-Model/#IO "Documentation for IO") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "What is your favorite natural number?"   let line ← (← [IO.getStdin](IO/Files___-File-Handles___-and-Streams/#IO___getStdin "Documentation for IO.getStdin")).[getLine](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream.getLine")   if let [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") n := line.[trimAscii](Basic-Types/Strings/#String___trimAscii "Documentation for String.trimAscii").[copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy").[toNat?](Basic-Types/Strings/#String___toNat___ "Documentation for String.toNat?") then     return n   else     [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "Let's try again."     [getFavoriteNat](Functors___-Monads-and--do--Notation/Syntax/#getFavoriteNat-_LPAR_in-Infix--Functor--and--Applicative--Operators_RPAR_ "Definition of example")  structure User where   name : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")   favoriteNat : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") deriving [Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")  def main : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let user ← User.mk <$> [getName](Functors___-Monads-and--do--Notation/Syntax/#getName-_LPAR_in-Infix--Functor--and--Applicative--Operators_RPAR_ "Definition of example") <*> [getFavoriteNat](Functors___-Monads-and--do--Notation/Syntax/#getFavoriteNat-_LPAR_in-Infix--Functor--and--Applicative--Operators_RPAR_ "Definition of example")   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([repr](Interacting-with-Lean/#repr-next "Documentation for repr") user) `
When run with this input:
`stdin``A. Lean User``None``42`
it produces this output:
`stdout``What is your name?``What is your favorite natural number?``Let's try again.``What is your favorite natural number?``{ name := "A. Lean User", favoriteNat := 42 }`
###  18.3.1.3. Monads[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Syntax--Infix-Operators--Monads "Permalink")
Monads are primarily used via [``Lean.Parser.Term.do : term``](Functors___-Monads-and--do--Notation/Syntax/#--tech-term-do-notation)[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do)-notation. However, it can sometimes be convenient to describe monadic computations via operators.
syntaxMonad Operators
`act >>= f` is syntax for `[Bind.bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") act f`.

```
term ::= ...
    | 


Sequences two computations, allowing the second to depend on the value computed by the first.


If x : m α and f : α → m β, then x >>= f : m β represents the result of executing x to get
a value of type α and then passing it to f.


Conventions for notations in identifiers:




  * The recommended spelling of >>= in identifiers is bind.




term >>= term
```

Similarly, the reversed operator `f =<< act` is syntax for `[Bind.bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind") act f`.

```
term ::= ...
    | 


Same as Bind.bind but with arguments swapped. 


Conventions for notations in identifiers:




  * The recommended spelling of =<< in identifiers is bindLeft.




term =<< term
```

The Kleisli composition operators `[Bind.kleisliRight](Functors___-Monads-and--do--Notation/API-Reference/#Bind___kleisliRight "Documentation for Bind.kleisliRight")` and `[Bind.kleisliLeft](Functors___-Monads-and--do--Notation/API-Reference/#Bind___kleisliLeft "Documentation for Bind.kleisliLeft")` also have infix operators.

```
term ::= ...
    | 


Left-to-right composition of Kleisli arrows. 


Conventions for notations in identifiers:




  * The recommended spelling of >=> in identifiers is kleisliRight.




term >=> term
```

```
term ::= ...
    | 


Right-to-left composition of Kleisli arrows. 


Conventions for notations in identifiers:




  * The recommended spelling of <=< in identifiers is kleisliLeft.




term <=< term
```

##  18.3.2. `do`-Notation[🔗](find/?domain=Verso.Genre.Manual.section&name=do-notation "Permalink")
Monads are primarily used via ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do)-notation, which is an embedded language for programming in an imperative style. It provides familiar syntax for sequencing effectful operations, early return, local mutable variables, loops, and exception handling. All of these features are translated to the operations of the `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")` type class, with a few of them requiring addition instances of classes such as `[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn")` that specify iteration over containers. For more details about the design of ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do)-notation, please consult Ullrich and de Moura (2022)Sebastian Ullrich and Leonardo de Moura, 2022. [“`do` Unchained: Embracing Local Imperativity in a Purely Functional Language”](https://dl.acm.org/doi/10.1145/3547640). In  _Proceedings of the ACM on Programming Languages: ICFP 2022._. A ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) term consists of the keyword ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) followed by a sequence of _``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do)items_.
syntax`do`-Notation

```
term ::= ...
    | do doSeqItem*
```

The items in a ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) may be separated by semicolons; otherwise, each should be on its own line and they should have equal indentation.
###  18.3.2.1. Sequential Computations[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Syntax--do--Notation--Sequential-Computations "Permalink")
One form of [``Lean.Parser.Term.do : term``](Functors___-Monads-and--do--Notation/Syntax/#--tech-term-do-items)[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) item is a term.
syntaxTerms in `do`-Notation

```
doSeqItem ::= ...
    | term
```

A term followed by a sequence of items is translated to a use of `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")`; in particular, `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") e1; es` is translated to `e1 >>= fun () => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") es`.  
|  ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) Item  |  Desugaring   |  
| --- | --- |  
| `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") e1 es`  | `e1 >>= fun () => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") es`  |  
The result of the term's computation may also be named, allowing it to be used in subsequent steps. This is done using ``Lean.Parser.Term.doLet : doElem```let`.
syntaxData Dependence in `do`-Notation
There are two forms of monadic ``Lean.Parser.Term.doLet : doElem```let`-binding in a ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block. The first binds an identifier to the result, with an optional type annotation:

```
doSeqItem ::= ...
    | let ident(:term)? ← term
```

The second binds a pattern to the result. The fallback clause, beginning with `|`, specifies the behavior when the pattern does not match the result.

```
doSeqItem ::= ...
    | let term ← term
        (| doSeqIndent)?
```

This syntax is also translated to a use of `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")`. `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let x ← e1; es` is translated to `e1 >>= fun x => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") es`, and fallback clauses are translated to default pattern matches. ``Lean.Parser.Term.doLet : doElem```let` may also be used with the standard definition syntax `:=` instead of `←`. This indicates a pure, rather than monadic, definition:
syntaxLocal Definitions in `do`-Notation

```
doSeqItem ::= ...
    | let 


letDecl matches the body of a let declaration let f x1 x2 := e,
let pat := e (where pat is an arbitrary term) or let f | pat1 => e1 | pat2 => e2 ...
(a pattern matching declaration), except for the let keyword itself.
let rec declarations are not handled here. 


(ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole)) := term
```

`[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let x := e; es` is translated to `let x := e; [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") es`.  
|  ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) Item  |  Desugaring   |  
| --- | --- |  
| `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let x ← e1 es`  | `e1 >>= fun x =>   [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") es`  |  
| `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let some x ← e1?   | fallback es`  | `e1? >>= fun   | [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")     es   | _ => fallback`  |  
| `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let x := e es`  | `let x := e [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") es`  |  
Within a ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block, `←` may be used as a prefix operator. The expression to which it is applied is replaced with a fresh variable, which is bound using `[bind](Functors___-Monads-and--do--Notation/#Bind___mk "Documentation for Bind.bind")` just before the current step. This allows monadic effects to be used in positions that otherwise might expect a pure value, while still maintaining the distinction between _describing_ an effectful computation and actually _executing_ its effects. Multiple occurrences of `←` are processed from left to right, inside to outside.  
|  Example ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) Item  |  Desugaring   |  
| --- | --- |  
| `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") f (← e1) (← e2) es`  | `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let x ← e1 let y ← e2 f x y es`  |  
| `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let x := g (← h (← e1)) es`  | `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let y ← e1 let z ← h y let x := g z es`  |  
Example Nested Action Desugarings
In addition to convenient support for sequential computations with data dependencies, ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do)-notation also supports the local addition of a variety of effects, including early return, local mutable state, and loops with early termination. These effects are implemented via transformations of the entire ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block in a manner akin to [monad transformers](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#--tech-term-monad-transformer), rather than via a local desugaring.
###  18.3.2.2. Early Return[🔗](find/?domain=Verso.Genre.Manual.section&name=early-return "Permalink")
Early return terminates a computation immediately with a given value. The value is returned from the closest containing ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block; however, this may not be the closest `do` keyword. The rules for determining the extent of a ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block are described [in their own section](Functors___-Monads-and--do--Notation/Syntax/#closest-do-block).
syntaxEarly Return

```
doSeqItem ::= ...
    | 


return e inside of a do block makes the surrounding block evaluate to pure e,
skipping any further statements.
Note that uses of the do keyword in other syntax like in for _ in _ do
do not constitute a surrounding block in this sense;
in supported editors, the corresponding do keyword of the surrounding block
is highlighted when hovering over return.


return not followed by a term starting on the same line is equivalent to return ().


return term
```

```
doSeqItem ::= ...
    | 


return e inside of a do block makes the surrounding block evaluate to pure e,
skipping any further statements.
Note that uses of the do keyword in other syntax like in for _ in _ do
do not constitute a surrounding block in this sense;
in supported editors, the corresponding do keyword of the surrounding block
is highlighted when hovering over return.


return not followed by a term starting on the same line is equivalent to return ().


return
```

Not all monads include early return. Thus, when a ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block contains ``Lean.Parser.Term.doReturn : doElem`
`return e` inside of a `do` block makes the surrounding block evaluate to `pure e`, skipping any further statements. Note that uses of the `do` keyword in other syntax like in `for _ in _ do` do not constitute a surrounding block in this sense; in supported editors, the corresponding `do` keyword of the surrounding block is highlighted when hovering over `return`.
`return` not followed by a term starting on the same line is equivalent to `return ()`.
``return`, the code needs to be rewritten to simulate the effect. A program that uses early return to compute a value of type `α` in a monad `m` can be thought of as a program in the monad `[ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") α m α`: early-returned values take the exception pathway, while ordinary returns do not. Then, an outer handler can return the value from either code paths. Internally, the ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) elaborator performs a translation very much like this one.
On its own, ``Lean.Parser.Term.doReturn : doElem`
`return e` inside of a `do` block makes the surrounding block evaluate to `pure e`, skipping any further statements. Note that uses of the `do` keyword in other syntax like in `for _ in _ do` do not constitute a surrounding block in this sense; in supported editors, the corresponding `do` keyword of the surrounding block is highlighted when hovering over `return`.
`return` not followed by a term starting on the same line is equivalent to `return ()`.
``return` is short for ``Lean.Parser.Term.doReturn : doElem`
`return e` inside of a `do` block makes the surrounding block evaluate to `pure e`, skipping any further statements. Note that uses of the `do` keyword in other syntax like in `for _ in _ do` do not constitute a surrounding block in this sense; in supported editors, the corresponding `do` keyword of the surrounding block is highlighted when hovering over `return`.
`return` not followed by a term starting on the same line is equivalent to `return ()`.
``return`​` `​`()`.
###  18.3.2.3. Local Mutable State[🔗](find/?domain=Verso.Genre.Manual.section&name=let-mut "Permalink")
Local mutable state is mutable state that cannot escape the ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block in which it is defined. The ``Lean.Parser.Term.doLet : doElem```let mut` binder introduces a locally-mutable binding.
syntaxLocal Mutability
Mutable bindings may be initialized either with pure computations or with monadic computations:

```
doSeqItem ::= ...
    | let mut 


letDecl matches the body of a let declaration let f x1 x2 := e,
let pat := e (where pat is an arbitrary term) or let f | pat1 => e1 | pat2 => e2 ...
(a pattern matching declaration), except for the let keyword itself.
let rec declarations are not handled here. 


(ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole)) := term
```

```
doSeqItem ::= ...
    | let mut ident ← doElem
```

Similarly, they can be mutated either with pure values or the results of monad computations:

```
doElem ::= ...
    | ident(: term)?  := term
```

```
doElem ::= ...
    | term(: term)? := term
```

```
doElem ::= ...
    | ident(: term)? ← term
```

```
doElem ::= ...
    | term ← term
        (| doSeqIndent)?
```

These locally-mutable bindings are less powerful than a [state monad](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#--tech-term-State-monads) because they are not mutable outside their lexical scope; this also makes them easier to reason about. When ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) blocks contain mutable bindings, the ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) elaborator transforms the expression similarly to the way that `[StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT")` would, constructing a new monad and initializing it with the correct values.
###  18.3.2.4. Control Structures[🔗](find/?domain=Verso.Genre.Manual.section&name=do-control-structures "Permalink")
There are ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) items that correspond to most of Lean's term-level control structures. When they occur as a step in a ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block, they are interpreted as ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) items rather than terms. Each branch of the control structures is a sequence of ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) items, rather than a term, and some of them are more syntactically flexible than their corresponding terms.
syntaxConditionals
In a ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block, ``Lean.Parser.Term.doIf : doElem```if` statements may omit their ``Lean.Parser.Term.doIf : doElem```else` branch. Omitting an ``Lean.Parser.Term.doIf : doElem```else` branch is equivalent to using `[pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure")``()` as the contents of the branch.

```
doSeqItem ::= ...
    | if ((ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole)) :)? term then
        doSeqItem*
      (else
        doSeqItem*)?
```

Syntactically, the ``Lean.Parser.Term.doIf : doElem```then` branch cannot be omitted. For these cases, ``Lean.Parser.Term.doUnless : doElem```unless` only executes its body when the condition is false. The ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) in ``Lean.Parser.Term.doUnless : doElem```unless` is part of its syntax and does not induce a nested ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block.
syntaxReverse Conditionals

```
doSeqItem ::= ...
    | unless term do
        doSeqItem*
```

When ``Lean.Parser.Term.doMatch : doElem```match` is used in a ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block, each branch is considered to be part of the same block. Otherwise, it is equivalent to the ``Lean.Parser.Term.match : term`
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
`[`match`](Terms/Pattern-Matching/#Lean___Parser___Term___match) term.
syntaxPattern Matching

```
doSeqItem ::= ...
    | match (


matchDiscr matches a "match discriminant", either h : tm or tm, used in match as
match h1 : e1, e2, h3 : e3 with .... 


((ident | [
A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.
The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.
Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:



  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.



Related concept: implicit parameters are automatically filled in with holes during the elaboration process.
See also ?m syntax (synthetic holes).
hole](Terms/Holes/#Lean___Parser___Term___hole)) :)? term),* with
        (| term,* => doSeqItem*)*
```

###  18.3.2.5. Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=monad-iteration-syntax "Permalink")
Within a ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block, ``Lean.Parser.Term.doFor : doElem`
`for x in e do s` iterates over `e` assuming `e`'s type has an instance of the `ForIn` typeclass. `break` and `continue` are supported inside `for` loops. `for x in e, x2 in e2, ... do s` iterates of the given collections in parallel, until at least one of them is exhausted. The types of `e2` etc. must implement the `Std.ToStream` typeclass.
``for`​`…`​``Lean.Parser.Term.doFor : doElem`
`for x in e do s` iterates over `e` assuming `e`'s type has an instance of the `ForIn` typeclass. `break` and `continue` are supported inside `for` loops. `for x in e, x2 in e2, ... do s` iterates of the given collections in parallel, until at least one of them is exhausted. The types of `e2` etc. must implement the `Std.ToStream` typeclass.
``in` loops allow iteration over a data structure. The body of the loop is part of the containing ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block, so local effects such as early return and mutable variables may be used.
syntaxIteration over Collections

```
doSeqItem ::= ...
    | 


for x in e do s  iterates over e assuming e's type has an instance of the ForIn typeclass.
break and continue are supported inside for loops.
for x in e, x2 in e2, ... do s iterates of the given collections in parallel,
until at least one of them is exhausted.
The types of e2 etc. must implement the Std.ToStream typeclass.


for ((ident :)? term in term),* do
        doSeqItem*
```

A ``Lean.Parser.Term.doFor : doElem`
`for x in e do s` iterates over `e` assuming `e`'s type has an instance of the `ForIn` typeclass. `break` and `continue` are supported inside `for` loops. `for x in e, x2 in e2, ... do s` iterates of the given collections in parallel, until at least one of them is exhausted. The types of `e2` etc. must implement the `Std.ToStream` typeclass.
``for`​`…`​``Lean.Parser.Term.doFor : doElem`
`for x in e do s` iterates over `e` assuming `e`'s type has an instance of the `ForIn` typeclass. `break` and `continue` are supported inside `for` loops. `for x in e, x2 in e2, ... do s` iterates of the given collections in parallel, until at least one of them is exhausted. The types of `e2` etc. must implement the `Std.ToStream` typeclass.
``in` loop requires at least one clause that specifies the iteration to be performed, which consists of an optional membership proof name followed by a colon (`:`), a pattern to bind, the keyword ``Lean.Parser.Term.doFor : doElem`
`for x in e do s` iterates over `e` assuming `e`'s type has an instance of the `ForIn` typeclass. `break` and `continue` are supported inside `for` loops. `for x in e, x2 in e2, ... do s` iterates of the given collections in parallel, until at least one of them is exhausted. The types of `e2` etc. must implement the `Std.ToStream` typeclass.
``in`, and a collection term. The pattern, which may just be an [identifier](Notations-and-Macros/Defining-New-Syntax/#--tech-term-Identifiers), must match any element of the collection; patterns in this position cannot be used as implicit filters. Further clauses may be provided by separating them with commas. Each collection is iterated over at the same time, and iteration stops when any of the collections runs out of elements.
Iteration Over Multiple Collections
When iterating over multiple collections, iteration stops when any of the collections runs out of elements.
``[#[](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")0[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") 'a'[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")1[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") 'b'[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[]](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Id.run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id___run "Documentation for Id.run") [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let mut v := #[] for x in [0:43], y in ['a', 'b'] do v := v.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") (x, y) return v `
```
[#[](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")0[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") 'a'[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")1[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") 'b'[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[]](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")
```

[Live ↪](javascript:openLiveLink\("MQUwbghgNgBAkgEwHQCcCuA7GCD2AoGGKEAFxgFs0ywYAuAXhmAG0BdAmAMxxRgA8YASyzMADLQAsAZlYAaGAE8hIgOQQV8lQCMVrbPkKEaDGGCQAHNAGcAFjAAUfeQoCUHFKTQosYIA"\))
Iteration over Array Indices with ``Lean.Parser.Term.doFor : doElem`
`for x in e do s` iterates over `e` assuming `e`'s type has an instance of the `ForIn` typeclass. `break` and `continue` are supported inside `for` loops. `for x in e, x2 in e2, ... do s` iterates of the given collections in parallel, until at least one of them is exhausted. The types of `e2` etc. must implement the `Std.ToStream` typeclass.
``for`
When iterating over the valid indices for an array with ``Lean.Parser.Term.doFor : doElem`
``for`, naming the membership proof allows the tactic that searches for proofs that array indices are in bounds to succeed.
`def satisfyingIndices     (p : α → Prop) [[DecidablePred](Type-Classes/Basic-Classes/#DecidablePred "Documentation for DecidablePred") p]     (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := [Id.run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id___run "Documentation for Id.run") [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let mut out := #[]   for h : i in [0:xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")] do     if p xs[i] then out := out.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") i   return out `
Omitting the hypothesis name causes the array lookup to fail, because no proof is available in the context that the iteration variable is within the specified range.
Iteration with `for`-loops is translated into uses of `ForIn.forIn`, which is an analogue of `ForM.forM` with added support for local mutations and early termination. `[ForIn.forIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn.forIn")` receives an initial value for the local mutable state and a monadic action as parameters, along with the collection being iterated over. The monadic action passed to `[ForIn.forIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn.forIn")` takes a current state as a parameter and, after carrying out actions in the monad `m`, returns either `[ForInStep.yield](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep.yield")` to indicate that iteration should continue with an updated set of local mutable values, or `[ForInStep.done](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep.done")` to indicate that ``Lean.Parser.Term.doBreak : doElem`
`break` exits the surrounding `for` loop. 
``break` or ``Lean.Parser.Term.doReturn : doElem`
`return e` inside of a `do` block makes the surrounding block evaluate to `pure e`, skipping any further statements. Note that uses of the `do` keyword in other syntax like in `for _ in _ do` do not constitute a surrounding block in this sense; in supported editors, the corresponding `do` keyword of the surrounding block is highlighted when hovering over `return`.
`return` not followed by a term starting on the same line is equivalent to `return ()`.
``return` was executed. When iteration is complete, `[ForIn.forIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn.forIn")` returns the final values of the local mutable values.
The specific desugaring of a loop depends on how state and early termination are used in its body. Here are some examples:  
|  ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) Item  |  Desugaring   |  
| --- | --- |  
| `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let mut b := … for x in xs do   b ← f x b es`  | `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let b := … let b ← [ForIn.forIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn.forIn") xs b fun x b => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let b ← f x b   return [ForInStep.yield](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep.yield") b es`  |  
| `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let mut b := … for x in xs do   b ← f x b   break es`  | `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let b := … let b ← [ForIn.forIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn.forIn") xs b fun x b => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let b ← f x b   return [ForInStep.done](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep.done") b es`  |  
| `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let mut b := … for h : x in xs do   b ← f' x h b es`  | `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let b := … let b ← [ForIn'.forIn'](Functors___-Monads-and--do--Notation/Syntax/#ForIn______mk "Documentation for ForIn'.forIn'") xs b fun x h b => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let b ← f' x h b   return [ForInStep.yield](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep.yield") b es`  |  
| `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let mut b := … for h : x in xs do   b ← f' x h b   break es`  | `[do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let b := … let b ← [ForIn'.forIn'](Functors___-Monads-and--do--Notation/Syntax/#ForIn______mk "Documentation for ForIn'.forIn'") xs b fun x h b => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let b ← f' x h b   return [ForInStep.done](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep.done") b es`  |  
The body of a ``Lean.doElemWhile_Do_ : doElem```while` loop is repeated while the condition remains true. It is possible to write infinite loops using them in functions that are not marked ``Lean.Parser.Command.declaration : command```partial`. This is because the ``Lean.Parser.Command.declaration : command```partial` modifier only applies to non-termination or infinite regress induced by the function being defined, and not by those that it calls. The translation of ``Lean.doElemWhile_Do_ : doElem```while` loops relies on a separate helper.
syntaxConditional Loops

```
doSeqItem ::= ...
    | while term do
        doSeqItem*
```

```
doSeqItem ::= ...
    | while ident : term do
        doSeqItem*
```

The body of a ``Lean.doElemRepeat__Until_ : doElem```repeat`-``Lean.doElemRepeat__Until_ : doElem```until` loop is always executed at least once. After each iteration, the condition is checked, and the loop is repeated when the condition is **false**. When the condition becomes true, iteration stops.
syntaxPost-Tested Loops

```
doSeqItem ::= ...
    | repeat
        doSeqItem*
      until term
```

The body of a ``Lean.doElemRepeat_ : doElem```repeat` loop is repeated until a ``Lean.Parser.Term.doBreak : doElem`
`break` exits the surrounding `for` loop. 
``break` statement is executed. Just like ``Lean.doElemWhile_Do_ : doElem```while` loops, these loops can be used in functions that are not marked ``Lean.Parser.Command.declaration : command```partial`.
syntaxUnconditional Loops

```
doSeqItem ::= ...
    | repeat
        doSeqItem*
```

The ``Lean.Parser.Term.doContinue : doElem`
`continue` skips to the next iteration of the surrounding `for` loop. 
``continue` statement skips the rest of the body of the closest enclosing ``Lean.doElemRepeat_ : doElem```repeat`, ``Lean.doElemWhile_Do_ : doElem```while`, or ``Lean.Parser.Term.doFor : doElem`
`for x in e do s` iterates over `e` assuming `e`'s type has an instance of the `ForIn` typeclass. `break` and `continue` are supported inside `for` loops. `for x in e, x2 in e2, ... do s` iterates of the given collections in parallel, until at least one of them is exhausted. The types of `e2` etc. must implement the `Std.ToStream` typeclass.
``for` loop, moving on to the next iteration. The ``Lean.Parser.Term.doBreak : doElem`
`break` exits the surrounding `for` loop. 
``break` statement terminates the closest enclosing ``Lean.doElemRepeat_ : doElem```repeat`, ``Lean.doElemWhile_Do_ : doElem```while`, or ``Lean.Parser.Term.doFor : doElem`
`for x in e do s` iterates over `e` assuming `e`'s type has an instance of the `ForIn` typeclass. `break` and `continue` are supported inside `for` loops. `for x in e, x2 in e2, ... do s` iterates of the given collections in parallel, until at least one of them is exhausted. The types of `e2` etc. must implement the `Std.ToStream` typeclass.
``for` loop, stopping iteration.
syntaxLoop Control Statements

```
doSeqItem ::= ...
    | 


continue skips to the next iteration of the surrounding for loop. 


continue
```

```
doSeqItem ::= ...
    | 


break exits the surrounding for loop. 


break
```

In addition to ``Lean.Parser.Term.doBreak : doElem`
`break` exits the surrounding `for` loop. 
``break`, loops can always be terminated by effects in the current monad. Throwing an exception from a loop terminates the loop.
Terminating Loops in the `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` Monad
The `failure` method from the `[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative")` class can be used to terminate an otherwise-infinite loop in the `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` monad.
``[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") show [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") from [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let mut i := 0 repeat if i > 1000 then failure else i := 2 * (i + 1) return i `
```
[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")
```

[Live ↪](javascript:openLiveLink\("MQUwbghgNgBAzgCwPYHcYHkAOAXAlkgOxgDkJsYAzAJyQFsYATJAKBhihHNoFdzcYAXAF4YABlYwqITCDIS2uCjH4A+GAEZRWmNgQgiFCLijcp8mCChwQywSIBMMAFQwAFPwDUGgJQSp2UyJcIA"\))
###  18.3.2.6. Identifying `do` Blocks[🔗](find/?domain=Verso.Genre.Manual.section&name=closest-do-block "Permalink")
Many features of ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do)-notation have an effect on the current ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block. In particular, early return aborts the current block, causing it to evaluate to the returned value, and mutable bindings can only be mutated in the block in which they are defined. Understanding these features requires a precise definition of what it means to be in the “same” block.
Empirically, this can be checked using the Lean language server. When the cursor is on a ``Lean.Parser.Term.doReturn : doElem`
`return e` inside of a `do` block makes the surrounding block evaluate to `pure e`, skipping any further statements. Note that uses of the `do` keyword in other syntax like in `for _ in _ do` do not constitute a surrounding block in this sense; in supported editors, the corresponding `do` keyword of the surrounding block is highlighted when hovering over `return`.
`return` not followed by a term starting on the same line is equivalent to `return ()`.
``return` statement, the corresponding ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) keyword is highlighted. Attempting to mutate a mutable binding outside of the same ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block results in an error message.
Highlighting ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do)
The rules are as follows:
  * Each item immediately nested under the ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) keyword that begins a block belongs to that block.
  * Each item immediately nested under the ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) keyword that is an item in a containing ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block belongs to the outer block.
  * Items in the branches of an ``Lean.Parser.Term.doIf : doElem```if`, ``Lean.Parser.Term.doMatch : doElem```match`, or ``Lean.Parser.Term.doUnless : doElem```unless` item belong to the same ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block as the control structure that contains them. The ``Lean.Parser.Term.doUnless : doElem```do` keyword that is part of the syntax of ``Lean.Parser.Term.doUnless : doElem```unless` does not introduce a new ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block.
  * Items in the body of ``Lean.doElemRepeat_ : doElem```repeat`, ``Lean.doElemWhile_Do_ : doElem```while`, and ``Lean.Parser.Term.doFor : doElem`
`for x in e do s` iterates over `e` assuming `e`'s type has an instance of the `ForIn` typeclass. `break` and `continue` are supported inside `for` loops. `for x in e, x2 in e2, ... do s` iterates of the given collections in parallel, until at least one of them is exhausted. The types of `e2` etc. must implement the `Std.ToStream` typeclass.
``for` belong to the same ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block as the loop that contains them. The ``Lean.Parser.Term.doFor : doElem`
`for x in e do s` iterates over `e` assuming `e`'s type has an instance of the `ForIn` typeclass. `break` and `continue` are supported inside `for` loops. `for x in e, x2 in e2, ... do s` iterates of the given collections in parallel, until at least one of them is exhausted. The types of `e2` etc. must implement the `Std.ToStream` typeclass.
``do` keyword that is part of the syntax of ``Lean.doElemWhile_Do_ : doElem```while` and ``Lean.Parser.Term.doFor : doElem`
`for x in e do s` iterates over `e` assuming `e`'s type has an instance of the `ForIn` typeclass. `break` and `continue` are supported inside `for` loops. `for x in e, x2 in e2, ... do s` iterates of the given collections in parallel, until at least one of them is exhausted. The types of `e2` etc. must implement the `Std.ToStream` typeclass.
``for` does not introduce a new ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) block.

Nested `do` and Branches
The following example outputs `6` rather than `7`:
`def test : [StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   [set](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf.set") 5   if [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") then     [set](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf.set") 6     do return   [set](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadStateOf___mk "Documentation for MonadStateOf.set") 7   return  `[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") 6[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [test](Functors___-Monads-and--do--Notation/Syntax/#test-_LPAR_in-Nested--do--and-Branches_RPAR_ "Definition of example").[run](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT___run "Documentation for StateT.run") 0 `
```
[(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")[(](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[)](Basic-Types/The-Unit-Type/#Unit___unit "Documentation for Unit.unit")[,](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") 6[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk")
```

This is because the ``Lean.Parser.Term.doReturn : doElem`
``return` statement under the ``Lean.Parser.Term.doIf : doElem```if` belongs to the same ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) as its immediate parent, which itself belongs to the same ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) as the ``Lean.Parser.Term.doIf : doElem```if`. If ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) blocks that occurred as items in other ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) blocks instead created new blocks, then the example would output `7`.
[Live ↪](javascript:openLiveLink\("CYUwZgBALiDOUQFwQMpQIYwLIQHKYgFUA7ASwUQF4JgB7AKAglhAQFZGJTIoAnAVxDQAFiGKcmLBADYJNWhF6t+vcZNYQA7JyVQV4+gGIQAN3QAbaHCgA6AcQgAGIA"\))
###  18.3.2.7. Type Classes for Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--Syntax--do--Notation--Type-Classes-for-Iteration "Permalink")
To be used with ``Lean.Parser.Term.doFor : doElem`
`for x in e do s` iterates over `e` assuming `e`'s type has an instance of the `ForIn` typeclass. `break` and `continue` are supported inside `for` loops. `for x in e, x2 in e2, ... do s` iterates of the given collections in parallel, until at least one of them is exhausted. The types of `e2` etc. must implement the `Std.ToStream` typeclass.
``for` loops without membership proofs, collections must implement the `[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn")` type class. Implementing `[ForIn'](Functors___-Monads-and--do--Notation/Syntax/#ForIn______mk "Documentation for ForIn'")` additionally allows the use of ``Lean.Parser.Term.doFor : doElem`
`for x in e do s` iterates over `e` assuming `e`'s type has an instance of the `ForIn` typeclass. `break` and `continue` are supported inside `for` loops. `for x in e, x2 in e2, ... do s` iterates of the given collections in parallel, until at least one of them is exhausted. The types of `e2` etc. must implement the `Std.ToStream` typeclass.
``for` loops with membership proofs.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ForIn.forIn "Permalink")type class
```


ForIn.{u, v, u₁, u₂} (m : Type u₁ → Type u₂) (ρ : Type u)
  (α : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type v)) : Type (max (max (max u (u₁ + 1)) u₂) v)


ForIn.{u, v, u₁, u₂}
  (m : Type u₁ → Type u₂) (ρ : Type u)
  (α : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type v)) :
  Type (max (max (max u (u₁ + 1)) u₂) v)


```

Monadic iteration in `do`-blocks, using the `for x in xs` notation.
The parameter `m` is the monad of the `do`-block in which iteration is performed, `ρ` is the type of the collection being iterated over, and `α` is the type of elements.
#  Instance Constructor

```
[ForIn.mk](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn.mk").{u, v, u₁, u₂}
```

#  Methods

```
forIn : {β : Type u₁} → ρ → β → (α → β → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") β)) → m β
```

Monadically iterates over the contents of a collection `xs`, with a local state `b` and the possibility of early termination.
Because a `do` block supports local mutable bindings along with `return`, and `break`, the monadic action passed to `[ForIn.forIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn.forIn")` takes a starting state in addition to the current element of the collection and returns an updated state together with an indication of whether iteration should continue or terminate. If the action returns `[ForInStep.done](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep.done")`, then `[ForIn.forIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn.forIn")` should stop iteration and return the updated state. If the action returns `[ForInStep.yield](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep.yield")`, then `[ForIn.forIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn.forIn")` should continue iterating if there are further elements, passing the updated state to the action.
More information about the translation of `for` loops into `[ForIn.forIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn.forIn")` is available in [the Lean reference manual](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=monad-iteration-syntax).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ForIn'.forIn' "Permalink")type class
```


ForIn'.{u, v, u₁, u₂} (m : Type u₁ → Type u₂) (ρ : Type u)
  (α : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type v)) (d : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Membership α ρ)) :
  Type (max (max (max u (u₁ + 1)) u₂) v)


ForIn'.{u, v, u₁, u₂}
  (m : Type u₁ → Type u₂) (ρ : Type u)
  (α : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type v))
  (d : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Membership α ρ)) :
  Type (max (max (max u (u₁ + 1)) u₂) v)


```

Monadic iteration in `do`-blocks with a membership proof, using the `for h : x in xs` notation.
The parameter `m` is the monad of the `do`-block in which iteration is performed, `ρ` is the type of the collection being iterated over, `α` is the type of elements, and `d` is the specific membership predicate to provide.
#  Instance Constructor

```
[ForIn'.mk](Functors___-Monads-and--do--Notation/Syntax/#ForIn______mk "Documentation for ForIn'.mk").{u, v, u₁, u₂}
```

#  Methods

```
forIn' : {β : Type u₁} → (x : ρ) → β → ((a : α) → a ∈ x → β → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") β)) → m β
```

Monadically iterates over the contents of a collection `xs`, with a local state `b` and the possibility of early termination. At each iteration, the body of the loop is provided with a proof that the current element is in the collection.
Because a `do` block supports local mutable bindings along with `return`, and `break`, the monadic action passed to `[ForIn'.forIn'](Functors___-Monads-and--do--Notation/Syntax/#ForIn______mk "Documentation for ForIn'.forIn'")` takes a starting state in addition to the current element of the collection with its membership proof. The action returns an updated state together with an indication of whether iteration should continue or terminate. If the action returns `[ForInStep.done](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep.done")`, then `[ForIn'.forIn'](Functors___-Monads-and--do--Notation/Syntax/#ForIn______mk "Documentation for ForIn'.forIn'")` should stop iteration and return the updated state. If the action returns `[ForInStep.yield](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep.yield")`, then `[ForIn'.forIn'](Functors___-Monads-and--do--Notation/Syntax/#ForIn______mk "Documentation for ForIn'.forIn'")` should continue iterating if there are further elements, passing the updated state to the action.
More information about the translation of `for` loops into `[ForIn'.forIn'](Functors___-Monads-and--do--Notation/Syntax/#ForIn______mk "Documentation for ForIn'.forIn'")` is available in [the Lean reference manual](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=monad-iteration-syntax).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ForInStep "Permalink")inductive type
```


ForInStep.{u} (α : Type u) : Type u


ForInStep.{u} (α : Type u) : Type u


```

An indication of whether a loop's body terminated early that's used to compile the `for x in xs` notation.
A collection's `[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn")` or `[ForIn'](Functors___-Monads-and--do--Notation/Syntax/#ForIn______mk "Documentation for ForIn'")` instance describes how to iterate over its elements. The monadic action that represents the body of the loop returns a `[ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") α`, where `α` is the local state used to implement features such as `let mut`.
#  Constructors

```
done.{u} {α : Type u} : α → [ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") α
```

The loop should terminate early.
`[ForInStep.done](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep.done")` is produced by uses of `break` or `return` in the loop body.

```
yield.{u} {α : Type u} : α → [ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") α
```

The loop should continue with the next iteration, using the returned state.
`[ForInStep.yield](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep.yield")` is produced by `continue` and by reaching the bottom of the loop body.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ForInStep.value "Permalink")def
```


ForInStep.value.{u_1} {α : Type u_1} (x : [ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") α) : α


ForInStep.value.{u_1} {α : Type u_1}
  (x : [ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") α) : α


```

Extracts the value from a `[ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep")`, ignoring whether it is `[ForInStep.done](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep.done")` or `[ForInStep.yield](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep.yield")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ForM.mk "Permalink")type class
```


ForM.{u, v, w₁, w₂} (m : Type u → Type v) (γ : Type w₁)
  (α : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w₂)) : Type (max (max v w₁) w₂)


ForM.{u, v, w₁, w₂} (m : Type u → Type v)
  (γ : Type w₁) (α : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") (Type w₂)) :
  Type (max (max v w₁) w₂)


```

Overloaded monadic iteration over some container type.
An instance of `[ForM](Functors___-Monads-and--do--Notation/Syntax/#ForM___mk "Documentation for ForM") m γ α` describes how to iterate a monadic operator over a container of type `γ` with elements of type `α` in the monad `m`. The element type should be uniquely determined by the monad and the container.
Use `[ForM.forIn](Functors___-Monads-and--do--Notation/Syntax/#ForM___forIn "Documentation for ForM.forIn")` to construct a `[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn")` instance from a `[ForM](Functors___-Monads-and--do--Notation/Syntax/#ForM___mk "Documentation for ForM")` instance, thus enabling the use of the `for` operator in `do`-notation.
#  Instance Constructor

```
[ForM.mk](Functors___-Monads-and--do--Notation/Syntax/#ForM___mk "Documentation for ForM.mk").{u, v, w₁, w₂}
```

#  Methods

```
forM : γ → (α → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")
```

Runs the monadic action `f` on each element of the collection `coll`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ForM.forIn "Permalink")def
```


ForM.forIn.{u_1, u_2, u_3, u_4} {m : Type u_1 → Type u_2} {β : Type u_1}
  {ρ : Type u_3} {α : Type u_4} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[ForM](Functors___-Monads-and--do--Notation/Syntax/#ForM___mk "Documentation for ForM") ([StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") β ([ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") β m)) ρ α] (x : ρ) (b : β)
  (f : α → β → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") β)) : m β


ForM.forIn.{u_1, u_2, u_3, u_4}
  {m : Type u_1 → Type u_2} {β : Type u_1}
  {ρ : Type u_3} {α : Type u_4} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[ForM](Functors___-Monads-and--do--Notation/Syntax/#ForM___mk "Documentation for ForM") ([StateT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateT "Documentation for StateT") β ([ExceptT](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#ExceptT "Documentation for ExceptT") β m)) ρ α]
  (x : ρ) (b : β)
  (f : α → β → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") β)) : m β


```

Creates a suitable implementation of `[ForIn.forIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn.forIn")` from a `[ForM](Functors___-Monads-and--do--Notation/Syntax/#ForM___mk "Documentation for ForM")` instance.
[←18.2. Lifting Monads](Functors___-Monads-and--do--Notation/Lifting-Monads/#lifting-monads "18.2. Lifting Monads")[18.4. API Reference→](Functors___-Monads-and--do--Notation/API-Reference/#The-Lean-Language-Reference--Functors___-Monads-and--do--Notation--API-Reference "18.4. API Reference")

[←2. Elaboration and Compilation](Elaboration-and-Compilation/#The-Lean-Language-Reference--Elaboration-and-Compilation "2. Elaboration and Compilation")[4. The Type System→](The-Type-System/#type-system "4. The Type System")
#  3. Interacting with Lean[🔗](find/?domain=Verso.Genre.Manual.section&name=interaction "Permalink")
Lean is designed for interactive use, rather than as a batch-mode system in which whole files are fed in and then translated to either object code or error messages. Many programming languages designed for interactive use provide a REPL,Short for “**R** ead-**E** val-**P** rint **L** oop”, because code is parsed (“read”), evaluated, and the result displayed, with this process repeated as many times as desired. at which code can be input and tested, along with commands for loading source files, type checking terms, or querying the environment. Lean's interactive features are based on a different paradigm. Rather than a separate command prompt outside of the program, Lean provides [commands](Source-Files-and-Modules/#--tech-term-commands) for accomplishing the same tasks in the context of a source file. By convention, commands that are intended for interactive use rather than as part of a durable code artifact are prefixed with `#`.
Information from Lean commands is available in the _message log_ , which accumulates output from the [elaborator](Terms/#--tech-term-elaborator). Each entry in the message log is associated with a specific source range and has a _severity_. There are three severities: `information` is used for messages that do not indicate a problem, `warning` indicates a potential problem, and `error` indicates a definite problem. For interactive commands, results are typically returned as informational messages that are associated with the command's leading keyword.
##  3.1. Evaluating Terms[🔗](find/?domain=Verso.Genre.Manual.section&name=hash-eval "Permalink")
The ``Lean.Parser.Command.eval : command`
`#eval e` evaluates the expression `e` by compiling and evaluating it.
  * The command attempts to use `ToExpr`, `Repr`, or `ToString` instances to print the result.
  * If `e` is a monadic value of type `m ty`, then the command tries to adapt the monad `m` to one of the monads that `#eval` supports, which include `IO`, `CoreM`, `MetaM`, `TermElabM`, and `CommandElabM`. Users can define `MonadEval` instances to extend the list of supported monads.


The `#eval` command gracefully degrades in capability depending on what is imported. Importing the `Lean.Elab.Command` module provides full capabilities.
Due to unsoundness, `#eval` refuses to evaluate expressions that depend on `sorry`, even indirectly, since the presence of `sorry` can lead to runtime instability and crashes. This check can be overridden with the `#eval! e` command.
Options:
  * If `eval.pp` is true (default: true) then tries to use `ToExpr` instances to make use of the usual pretty printer. Otherwise, only tries using `Repr` and `ToString` instances.
  * If `eval.type` is true (default: false) then pretty prints the type of the evaluated value.
  * If `eval.derive.repr` is true (default: true) then attempts to auto-derive a `Repr` instance when there is no other way to print the result.


See also: `#reduce e` for evaluation by term reduction.
`[`#eval`](Interacting-with-Lean/#Lean___Parser___Command___eval) command is used to run code as a program. In particular, it is capable of executing `[IO](IO/Logical-Model/#IO "Documentation for IO")` actions, it uses a call-by-value evaluation strategy, [`partial` functions are executed](Definitions/Recursive-Definitions/#partial-unsafe), and both types and proofs are erased. Use ``Lean.reduceCmd : command`
`#reduce <expression>` reduces the expression `<expression>` to its normal form. This involves applying reduction rules until no further reduction is possible.
By default, proofs and types within the expression are not reduced. Use modifiers `(proofs := true)` and `(types := true)` to reduce them. Recall that propositions are types in Lean.
**Warning:** This can be a computationally expensive operation, especially for complex expressions.
Consider using `#eval <expression>` for simple evaluation/execution of expressions.
`[`#reduce`](Interacting-with-Lean/#Lean___reduceCmd) to instead reduce terms using the reduction rules that are part of [definitional equality](The-Type-System/#--tech-term-definitional-equality).
syntaxEvaluating Terms

```
command ::= ...
    | 


#eval e evaluates the expression e by compiling and evaluating it.




  * The command attempts to use ToExpr, Repr, or ToString instances to print the result.


  * If e is a monadic value of type m ty, then the command tries to adapt the monad m
to one of the monads that #eval supports, which include IO, CoreM, MetaM, TermElabM, and CommandElabM.
Users can define MonadEval instances to extend the list of supported monads.




The #eval command gracefully degrades in capability depending on what is imported.
Importing the Lean.Elab.Command module provides full capabilities.


Due to unsoundness, #eval refuses to evaluate expressions that depend on sorry, even indirectly,
since the presence of sorry can lead to runtime instability and crashes.
This check can be overridden with the #eval! e command.


Options:




  * If eval.pp is true (default: true) then tries to use ToExpr instances to make use of the
usual pretty printer. Otherwise, only tries using Repr and ToString instances.


  * If eval.type is true (default: false) then pretty prints the type of the evaluated value.


  * If eval.derive.repr is true (default: true) then attempts to auto-derive a Repr instance
when there is no other way to print the result.




See also: #reduce e for evaluation by term reduction.


#eval term
```

```
command ::= ...
    | 


#eval e evaluates the expression e by compiling and evaluating it.




  * The command attempts to use ToExpr, Repr, or ToString instances to print the result.


  * If e is a monadic value of type m ty, then the command tries to adapt the monad m
to one of the monads that #eval supports, which include IO, CoreM, MetaM, TermElabM, and CommandElabM.
Users can define MonadEval instances to extend the list of supported monads.




The #eval command gracefully degrades in capability depending on what is imported.
Importing the Lean.Elab.Command module provides full capabilities.


Due to unsoundness, #eval refuses to evaluate expressions that depend on sorry, even indirectly,
since the presence of sorry can lead to runtime instability and crashes.
This check can be overridden with the #eval! e command.


Options:




  * If eval.pp is true (default: true) then tries to use ToExpr instances to make use of the
usual pretty printer. Otherwise, only tries using Repr and ToString instances.


  * If eval.type is true (default: false) then pretty prints the type of the evaluated value.


  * If eval.derive.repr is true (default: true) then attempts to auto-derive a Repr instance
when there is no other way to print the result.




See also: #reduce e for evaluation by term reduction.


#eval! term
```

`#eval e` evaluates the expression `e` by compiling and evaluating it.
  * The command attempts to use `ToExpr`, `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")`, or `ToString` instances to print the result.
  * If `e` is a monadic value of type `m ty`, then the command tries to adapt the monad `m` to one of the monads that `#eval` supports, which include `[IO](IO/Logical-Model/#IO "Documentation for IO")`, `CoreM`, `MetaM`, `TermElabM`, and `CommandElabM`. Users can define `[MonadEval](Interacting-with-Lean/#MonadEval___mk "Documentation for MonadEval")` instances to extend the list of supported monads.


The `#eval` command gracefully degrades in capability depending on what is imported. Importing the `Lean.Elab.Command` module provides full capabilities.
Due to unsoundness, `#eval` refuses to evaluate expressions that depend on `[sorry](Tactic-Proofs/Tactic-Reference/#sorry "Documentation for tactic")`, even indirectly, since the presence of `[sorry](Tactic-Proofs/Tactic-Reference/#sorry "Documentation for tactic")` can lead to runtime instability and crashes. This check can be overridden with the `#eval! e` command.
Options:
  * If `[eval.pp](Interacting-with-Lean/#eval___pp "Documentation for option eval.pp")` is true (default: true) then tries to use `ToExpr` instances to make use of the usual pretty printer. Otherwise, only tries using `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` and `ToString` instances.
  * If `[eval.type](Interacting-with-Lean/#eval___type "Documentation for option eval.type")` is true (default: false) then pretty prints the type of the evaluated value.
  * If `[eval.derive.repr](Interacting-with-Lean/#eval___derive___repr "Documentation for option eval.derive.repr")` is true (default: true) then attempts to auto-derive a `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instance when there is no other way to print the result.


See also: `#reduce e` for evaluation by term reduction.
``Lean.Parser.Command.eval : command`
`#eval e` evaluates the expression `e` by compiling and evaluating it.
  * The command attempts to use `ToExpr`, `Repr`, or `ToString` instances to print the result.
  * If `e` is a monadic value of type `m ty`, then the command tries to adapt the monad `m` to one of the monads that `#eval` supports, which include `IO`, `CoreM`, `MetaM`, `TermElabM`, and `CommandElabM`. Users can define `MonadEval` instances to extend the list of supported monads.


The `#eval` command gracefully degrades in capability depending on what is imported. Importing the `Lean.Elab.Command` module provides full capabilities.
Due to unsoundness, `#eval` refuses to evaluate expressions that depend on `sorry`, even indirectly, since the presence of `sorry` can lead to runtime instability and crashes. This check can be overridden with the `#eval! e` command.
Options:
  * If `eval.pp` is true (default: true) then tries to use `ToExpr` instances to make use of the usual pretty printer. Otherwise, only tries using `Repr` and `ToString` instances.
  * If `eval.type` is true (default: false) then pretty prints the type of the evaluated value.
  * If `eval.derive.repr` is true (default: true) then attempts to auto-derive a `Repr` instance when there is no other way to print the result.


See also: `#reduce e` for evaluation by term reduction.
`[`#eval`](Interacting-with-Lean/#Lean___Parser___Command___eval) always [elaborates](Terms/#--tech-term-elaborator) and compiles the provided term. It then checks whether the term transitively depends on any uses of `sorry`, in which case evaluation is terminated unless the command was invoked as ``Lean.Parser.Command.eval : command`
`#eval e` evaluates the expression `e` by compiling and evaluating it.
  * The command attempts to use `ToExpr`, `Repr`, or `ToString` instances to print the result.
  * If `e` is a monadic value of type `m ty`, then the command tries to adapt the monad `m` to one of the monads that `#eval` supports, which include `IO`, `CoreM`, `MetaM`, `TermElabM`, and `CommandElabM`. Users can define `MonadEval` instances to extend the list of supported monads.


The `#eval` command gracefully degrades in capability depending on what is imported. Importing the `Lean.Elab.Command` module provides full capabilities.
Due to unsoundness, `#eval` refuses to evaluate expressions that depend on `sorry`, even indirectly, since the presence of `sorry` can lead to runtime instability and crashes. This check can be overridden with the `#eval! e` command.
Options:
  * If `eval.pp` is true (default: true) then tries to use `ToExpr` instances to make use of the usual pretty printer. Otherwise, only tries using `Repr` and `ToString` instances.
  * If `eval.type` is true (default: false) then pretty prints the type of the evaluated value.
  * If `eval.derive.repr` is true (default: true) then attempts to auto-derive a `Repr` instance when there is no other way to print the result.


See also: `#reduce e` for evaluation by term reduction.
`[`#eval!`](Interacting-with-Lean/#Lean___Parser___Command___eval). This is because compiled code may rely on compile-time invariants (such as array lookups being in-bounds) that are ensured by proofs of suitable statements, and running code that contains incomplete proofs (or uses of `sorry` that “prove” incorrect statements) can cause Lean itself to crash.
The way the code is run depends on its type:
  * If the type is in the `[IO](IO/Logical-Model/#IO "Documentation for IO")` monad, then it is executed in a context where [standard output](IO/Files___-File-Handles___-and-Streams/#--tech-term-standard-output) and [standard error](IO/Files___-File-Handles___-and-Streams/#--tech-term-standard-error) are captured and redirected to the Lean [message log](Interacting-with-Lean/#--tech-term-message-log). If the returned value's type is not `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")`, then it is displayed as if it were the result of a non-monadic expression.
  * If the type is in one of the internal Lean metaprogramming monads (`CommandElabM`, `TermElabM`, `MetaM`, or `CoreM`), then it is run in the current context. For example, the environment will contain the definitions that are in scope where ``Lean.Parser.Command.eval : command`
`#eval e` evaluates the expression `e` by compiling and evaluating it.
    * The command attempts to use `ToExpr`, `Repr`, or `ToString` instances to print the result.
    * If `e` is a monadic value of type `m ty`, then the command tries to adapt the monad `m` to one of the monads that `#eval` supports, which include `IO`, `CoreM`, `MetaM`, `TermElabM`, and `CommandElabM`. Users can define `MonadEval` instances to extend the list of supported monads.
The `#eval` command gracefully degrades in capability depending on what is imported. Importing the `Lean.Elab.Command` module provides full capabilities.
Due to unsoundness, `#eval` refuses to evaluate expressions that depend on `sorry`, even indirectly, since the presence of `sorry` can lead to runtime instability and crashes. This check can be overridden with the `#eval! e` command.
Options:
    * If `eval.pp` is true (default: true) then tries to use `ToExpr` instances to make use of the usual pretty printer. Otherwise, only tries using `Repr` and `ToString` instances.
    * If `eval.type` is true (default: false) then pretty prints the type of the evaluated value.
    * If `eval.derive.repr` is true (default: true) then attempts to auto-derive a `Repr` instance when there is no other way to print the result.
See also: `#reduce e` for evaluation by term reduction.
`[`#eval`](Interacting-with-Lean/#Lean___Parser___Command___eval) is invoked. As with `[IO](IO/Logical-Model/#IO "Documentation for IO")`, the resulting value is displayed as if it were the result of a non-monadic expression. When Lean is running under [Lake](Build-Tools-and-Distribution/Lake/#lake), its working directory (and thus the working directory for `[IO](IO/Logical-Model/#IO "Documentation for IO")` actions) is the current [`workspace`](Build-Tools-and-Distribution/Lake/#--tech-term-workspace).
  * If the type is in some other monad `m`, and there is a `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") m CommandElabM` or `[MonadEvalT](Interacting-with-Lean/#MonadEvalT___mk "Documentation for MonadEvalT") m CommandElabM` instance, then `[MonadLiftT.monadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT.monadLift")` or `[MonadEvalT.monadEval](Interacting-with-Lean/#MonadEvalT___mk "Documentation for MonadEvalT.monadEval")` is used to transform the monad into one that may be run with ``Lean.Parser.Command.eval : command`
`#eval e` evaluates the expression `e` by compiling and evaluating it.
    * The command attempts to use `ToExpr`, `Repr`, or `ToString` instances to print the result.
    * If `e` is a monadic value of type `m ty`, then the command tries to adapt the monad `m` to one of the monads that `#eval` supports, which include `IO`, `CoreM`, `MetaM`, `TermElabM`, and `CommandElabM`. Users can define `MonadEval` instances to extend the list of supported monads.
The `#eval` command gracefully degrades in capability depending on what is imported. Importing the `Lean.Elab.Command` module provides full capabilities.
Due to unsoundness, `#eval` refuses to evaluate expressions that depend on `sorry`, even indirectly, since the presence of `sorry` can lead to runtime instability and crashes. This check can be overridden with the `#eval! e` command.
Options:
    * If `eval.pp` is true (default: true) then tries to use `ToExpr` instances to make use of the usual pretty printer. Otherwise, only tries using `Repr` and `ToString` instances.
    * If `eval.type` is true (default: false) then pretty prints the type of the evaluated value.
    * If `eval.derive.repr` is true (default: true) then attempts to auto-derive a `Repr` instance when there is no other way to print the result.
See also: `#reduce e` for evaluation by term reduction.
`[`#eval`](Interacting-with-Lean/#Lean___Parser___Command___eval), after which it is run as usual.
  * If the term's type is not in any of the supported monads, then it is treated as a pure value. The compiled code is run, and the result is displayed.


Auxiliary definitions or other environment modifications that result from elaborating the term in ``Lean.Parser.Command.eval : command`
`#eval e` evaluates the expression `e` by compiling and evaluating it.
  * The command attempts to use `ToExpr`, `Repr`, or `ToString` instances to print the result.
  * If `e` is a monadic value of type `m ty`, then the command tries to adapt the monad `m` to one of the monads that `#eval` supports, which include `IO`, `CoreM`, `MetaM`, `TermElabM`, and `CommandElabM`. Users can define `MonadEval` instances to extend the list of supported monads.


The `#eval` command gracefully degrades in capability depending on what is imported. Importing the `Lean.Elab.Command` module provides full capabilities.
Due to unsoundness, `#eval` refuses to evaluate expressions that depend on `sorry`, even indirectly, since the presence of `sorry` can lead to runtime instability and crashes. This check can be overridden with the `#eval! e` command.
Options:
  * If `eval.pp` is true (default: true) then tries to use `ToExpr` instances to make use of the usual pretty printer. Otherwise, only tries using `Repr` and `ToString` instances.
  * If `eval.type` is true (default: false) then pretty prints the type of the evaluated value.
  * If `eval.derive.repr` is true (default: true) then attempts to auto-derive a `Repr` instance when there is no other way to print the result.


See also: `#reduce e` for evaluation by term reduction.
`[`#eval`](Interacting-with-Lean/#Lean___Parser___Command___eval) are discarded. If the term is an action in a metaprogramming monad, then changes made to the environment by running the monadic action are preserved.
Results are displayed using a `ToExpr`, `ToString`, or `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instance, if they exist. If not, and `[eval.derive.repr](Interacting-with-Lean/#eval___derive___repr "Documentation for option eval.derive.repr")` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, Lean attempts to derive a suitable `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instance. It is an error if no suitable instance can be found or derived. Setting `[eval.pp](Interacting-with-Lean/#eval___pp "Documentation for option eval.pp")` to `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` disables the use of `ToExpr` instances by ``Lean.Parser.Command.eval : command`
`#eval e` evaluates the expression `e` by compiling and evaluating it.
  * The command attempts to use `ToExpr`, `Repr`, or `ToString` instances to print the result.
  * If `e` is a monadic value of type `m ty`, then the command tries to adapt the monad `m` to one of the monads that `#eval` supports, which include `IO`, `CoreM`, `MetaM`, `TermElabM`, and `CommandElabM`. Users can define `MonadEval` instances to extend the list of supported monads.


The `#eval` command gracefully degrades in capability depending on what is imported. Importing the `Lean.Elab.Command` module provides full capabilities.
Due to unsoundness, `#eval` refuses to evaluate expressions that depend on `sorry`, even indirectly, since the presence of `sorry` can lead to runtime instability and crashes. This check can be overridden with the `#eval! e` command.
Options:
  * If `eval.pp` is true (default: true) then tries to use `ToExpr` instances to make use of the usual pretty printer. Otherwise, only tries using `Repr` and `ToString` instances.
  * If `eval.type` is true (default: false) then pretty prints the type of the evaluated value.
  * If `eval.derive.repr` is true (default: true) then attempts to auto-derive a `Repr` instance when there is no other way to print the result.


See also: `#reduce e` for evaluation by term reduction.
`[`#eval`](Interacting-with-Lean/#Lean___Parser___Command___eval).
Displaying Output
``Lean.Parser.Command.eval : command`
`[`#eval`](Interacting-with-Lean/#Lean___Parser___Command___eval) cannot display functions:
``could not synthesize a `ToExpr`, `Repr`, or `ToString` instance for type   [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") fun x => x + 1 `
```
could not synthesize a `ToExpr`, `Repr`, or `ToString` instance for type
  [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

It is capable of deriving instances to display output that has no `ToString` or `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instance:
`inductive Quadrant where   | nw | sw | se | ne  `Quadrant.nw`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Quadrant.nw](Interacting-with-Lean/#Quadrant___nw-_LPAR_in-Displaying-Output_RPAR_ "Definition of example") `
```
Quadrant.nw
```

The derived instance is not saved. Disabling `[eval.derive.repr](Interacting-with-Lean/#eval___derive___repr "Documentation for option eval.derive.repr")` causes ``Lean.Parser.Command.eval : command`
`[`#eval`](Interacting-with-Lean/#Lean___Parser___Command___eval) to fail:
`set_option [eval.derive.repr](Interacting-with-Lean/#eval___derive___repr "Documentation for option eval.derive.repr") false `could not synthesize a `ToExpr`, `Repr`, or `ToString` instance for type   [Quadrant](Interacting-with-Lean/#Quadrant-_LPAR_in-Displaying-Output_RPAR_ "Definition of example")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Quadrant.nw](Interacting-with-Lean/#Quadrant___nw-_LPAR_in-Displaying-Output_RPAR_ "Definition of example") `
```
could not synthesize a `ToExpr`, `Repr`, or `ToString` instance for type
  [Quadrant](Interacting-with-Lean/#Quadrant-_LPAR_in-Displaying-Output_RPAR_ "Definition of example")
```

[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABARQgQzAJwyGyA7gBaLaIBQyyAPsiIbcgM6N3Mp0iUUDEi8DABs0mHHhgA6BkA"\))
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=eval.pp "Permalink")option
```
eval.pp
```

Default value: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
('#eval' command) enables using 'ToExpr' instances to pretty print the result, otherwise uses 'Repr' or 'ToString' instances
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=eval.type "Permalink")option
```
eval.type
```

Default value: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
('#eval' command) enables pretty printing the type of the result
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=eval.derive.repr "Permalink")option
```
eval.derive.repr
```

Default value: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
('#eval' command) enables auto-deriving 'Repr' instances as a fallback
Monads can be given the ability to execute in ``Lean.Parser.Command.eval : command`
`#eval e` evaluates the expression `e` by compiling and evaluating it.
  * The command attempts to use `ToExpr`, `Repr`, or `ToString` instances to print the result.
  * If `e` is a monadic value of type `m ty`, then the command tries to adapt the monad `m` to one of the monads that `#eval` supports, which include `IO`, `CoreM`, `MetaM`, `TermElabM`, and `CommandElabM`. Users can define `MonadEval` instances to extend the list of supported monads.


The `#eval` command gracefully degrades in capability depending on what is imported. Importing the `Lean.Elab.Command` module provides full capabilities.
Due to unsoundness, `#eval` refuses to evaluate expressions that depend on `sorry`, even indirectly, since the presence of `sorry` can lead to runtime instability and crashes. This check can be overridden with the `#eval! e` command.
Options:
  * If `eval.pp` is true (default: true) then tries to use `ToExpr` instances to make use of the usual pretty printer. Otherwise, only tries using `Repr` and `ToString` instances.
  * If `eval.type` is true (default: false) then pretty prints the type of the evaluated value.
  * If `eval.derive.repr` is true (default: true) then attempts to auto-derive a `Repr` instance when there is no other way to print the result.


See also: `#reduce e` for evaluation by term reduction.
`[`#eval`](Interacting-with-Lean/#Lean___Parser___Command___eval) by defining a suitable `[MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift")``[MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift")` is described in [the section on lifting monads.](Functors___-Monads-and--do--Notation/Lifting-Monads/#lifting-monads) or `[MonadEval](Interacting-with-Lean/#MonadEval___mk "Documentation for MonadEval")` instance. Just as `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT")` is the transitive closure of `[MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift")` instances, `[MonadEvalT](Interacting-with-Lean/#MonadEvalT___mk "Documentation for MonadEvalT")` is the transitive closure of `[MonadEval](Interacting-with-Lean/#MonadEval___mk "Documentation for MonadEval")` instances. As with `[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT")` users should not define additional instances of `[MonadEvalT](Interacting-with-Lean/#MonadEvalT___mk "Documentation for MonadEvalT")` directly.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadEval.monadEval "Permalink")type class
```


MonadEval.{u, v, w} (m : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Type u → Type v))
  (n : Type u → Type w) : Type (max (max (u + 1) v) w)


MonadEval.{u, v, w}
  (m : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") (Type u → Type v))
  (n : Type u → Type w) :
  Type (max (max (u + 1) v) w)


```

Typeclass used for adapting monads. This is similar to `[MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift")`, but instances are allowed to make use of default state for the purpose of synthesizing such an instance, if necessary. Every `[MonadLift](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLift___mk "Documentation for MonadLift")` instance gives a `[MonadEval](Interacting-with-Lean/#MonadEval___mk "Documentation for MonadEval")` instance.
The purpose of this class is for the `#eval` command, which looks for a `[MonadEval](Interacting-with-Lean/#MonadEval___mk "Documentation for MonadEval") m CommandElabM` or `[MonadEval](Interacting-with-Lean/#MonadEval___mk "Documentation for MonadEval") m [IO](IO/Logical-Model/#IO "Documentation for IO")` instance.
#  Instance Constructor

```
[MonadEval.mk](Interacting-with-Lean/#MonadEval___mk "Documentation for MonadEval.mk").{u, v, w}
```

#  Methods

```
monadEval : {α : Type u} → m α → n α
```

Evaluates a value from monad `m` into monad `n`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=MonadEvalT.monadEval "Permalink")type class
```


MonadEvalT.{u, v, w} (m : Type u → Type v) (n : Type u → Type w) :
  Type (max (max (u + 1) v) w)


MonadEvalT.{u, v, w} (m : Type u → Type v)
  (n : Type u → Type w) :
  Type (max (max (u + 1) v) w)


```

The transitive closure of `[MonadEval](Interacting-with-Lean/#MonadEval___mk "Documentation for MonadEval")`.
#  Instance Constructor

```
[MonadEvalT.mk](Interacting-with-Lean/#MonadEvalT___mk "Documentation for MonadEvalT.mk").{u, v, w}
```

#  Methods

```
monadEval : {α : Type u} → m α → n α
```

Evaluates a value from monad `m` into monad `n`.
##  3.2. Reducing Terms[🔗](find/?domain=Verso.Genre.Manual.section&name=hash-reduce "Permalink")
The ``Lean.reduceCmd : command`
`#reduce <expression>` reduces the expression `<expression>` to its normal form. This involves applying reduction rules until no further reduction is possible.
By default, proofs and types within the expression are not reduced. Use modifiers `(proofs := true)` and `(types := true)` to reduce them. Recall that propositions are types in Lean.
**Warning:** This can be a computationally expensive operation, especially for complex expressions.
Consider using `#eval <expression>` for simple evaluation/execution of expressions.
`[`#reduce`](Interacting-with-Lean/#Lean___reduceCmd) command repeatedly applies reductions to a term until no further reductions are possible. Reductions are performed under binders, but to avoid unexpected slowdowns, proofs and types are skipped unless the corresponding options to ``Lean.reduceCmd : command`
`#reduce <expression>` reduces the expression `<expression>` to its normal form. This involves applying reduction rules until no further reduction is possible.
By default, proofs and types within the expression are not reduced. Use modifiers `(proofs := true)` and `(types := true)` to reduce them. Recall that propositions are types in Lean.
**Warning:** This can be a computationally expensive operation, especially for complex expressions.
Consider using `#eval <expression>` for simple evaluation/execution of expressions.
`[`#reduce`](Interacting-with-Lean/#Lean___reduceCmd) are enabled. Unlike ``Lean.Parser.Command.eval : command`
`#eval e` evaluates the expression `e` by compiling and evaluating it.
  * The command attempts to use `ToExpr`, `Repr`, or `ToString` instances to print the result.
  * If `e` is a monadic value of type `m ty`, then the command tries to adapt the monad `m` to one of the monads that `#eval` supports, which include `IO`, `CoreM`, `MetaM`, `TermElabM`, and `CommandElabM`. Users can define `MonadEval` instances to extend the list of supported monads.


The `#eval` command gracefully degrades in capability depending on what is imported. Importing the `Lean.Elab.Command` module provides full capabilities.
Due to unsoundness, `#eval` refuses to evaluate expressions that depend on `sorry`, even indirectly, since the presence of `sorry` can lead to runtime instability and crashes. This check can be overridden with the `#eval! e` command.
Options:
  * If `eval.pp` is true (default: true) then tries to use `ToExpr` instances to make use of the usual pretty printer. Otherwise, only tries using `Repr` and `ToString` instances.
  * If `eval.type` is true (default: false) then pretty prints the type of the evaluated value.
  * If `eval.derive.repr` is true (default: true) then attempts to auto-derive a `Repr` instance when there is no other way to print the result.


See also: `#reduce e` for evaluation by term reduction.
`[`#eval`](Interacting-with-Lean/#Lean___Parser___Command___eval) command, reduction cannot have side effects and the result is displayed as a term rather than via a `ToString` or `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instance.
Generally speaking, ``Lean.reduceCmd : command`
`#reduce <expression>` reduces the expression `<expression>` to its normal form. This involves applying reduction rules until no further reduction is possible.
By default, proofs and types within the expression are not reduced. Use modifiers `(proofs := true)` and `(types := true)` to reduce them. Recall that propositions are types in Lean.
**Warning:** This can be a computationally expensive operation, especially for complex expressions.
Consider using `#eval <expression>` for simple evaluation/execution of expressions.
`[`#reduce`](Interacting-with-Lean/#Lean___reduceCmd) is primarily useful for diagnosing issues with definitional equality and proof terms, while ``Lean.Parser.Command.eval : command`
`#eval e` evaluates the expression `e` by compiling and evaluating it.
  * The command attempts to use `ToExpr`, `Repr`, or `ToString` instances to print the result.
  * If `e` is a monadic value of type `m ty`, then the command tries to adapt the monad `m` to one of the monads that `#eval` supports, which include `IO`, `CoreM`, `MetaM`, `TermElabM`, and `CommandElabM`. Users can define `MonadEval` instances to extend the list of supported monads.


The `#eval` command gracefully degrades in capability depending on what is imported. Importing the `Lean.Elab.Command` module provides full capabilities.
Due to unsoundness, `#eval` refuses to evaluate expressions that depend on `sorry`, even indirectly, since the presence of `sorry` can lead to runtime instability and crashes. This check can be overridden with the `#eval! e` command.
Options:
  * If `eval.pp` is true (default: true) then tries to use `ToExpr` instances to make use of the usual pretty printer. Otherwise, only tries using `Repr` and `ToString` instances.
  * If `eval.type` is true (default: false) then pretty prints the type of the evaluated value.
  * If `eval.derive.repr` is true (default: true) then attempts to auto-derive a `Repr` instance when there is no other way to print the result.


See also: `#reduce e` for evaluation by term reduction.
`[`#eval`](Interacting-with-Lean/#Lean___Parser___Command___eval) is more suitable for computing the value of a term. In particular, functions defined using [well-founded recursion](Definitions/Recursive-Definitions/#--tech-term-well-founded-recursion) or as [partial fixpoints](Definitions/Recursive-Definitions/#--tech-term-partial-fixpoint) are either very slow to compute with the reduction engine, or will not reduce at all.
syntaxReducing Terms

```
command ::= ...
    | 


#reduce <expression> reduces the expression <expression> to its normal form. This
involves applying reduction rules until no further reduction is possible.


By default, proofs and types within the expression are not reduced. Use modifiers
(proofs := true)  and (types := true) to reduce them.
Recall that propositions are types in Lean.


**Warning:** This can be a computationally expensive operation,
especially for complex expressions.


Consider using #eval <expression> for simple evaluation/execution
of expressions.


#reduce ((proofs := true))? ((types := true))? term
```

`#reduce <expression>` reduces the expression `<expression>` to its normal form. This involves applying reduction rules until no further reduction is possible.
By default, proofs and types within the expression are not reduced. Use modifiers `(proofs := true)` and `(types := true)` to reduce them. Recall that propositions are types in Lean.
**Warning:** This can be a computationally expensive operation, especially for complex expressions.
Consider using `#eval <expression>` for simple evaluation/execution of expressions.
Reducing Functions
Reducing a term results in its normal form in Lean's logic. Because the underlying term is reduced and then displayed, there is no need for a `ToString` or `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instance. Functions can be displayed just as well as any other term.
In some cases, this normal form is short and resembles a term that a person might write:
``fun x => x.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")`[#reduce](Interacting-with-Lean/#Lean___reduceCmd "Documentation for syntax") (fun x => x + 1) `
```
fun x => x.[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")
```

In other cases, the details of [the elaboration of functions](Definitions/Recursive-Definitions/#elab-as-course-of-values) such as addition to Lean's core logic are exposed:
``fun x => (Nat.rec ⟨fun x => x, [PUnit.unit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit.unit")⟩ (fun n n_ih => ⟨fun x => (n_ih.1 x).[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ"), n_ih⟩) x).1 1`[#reduce](Interacting-with-Lean/#Lean___reduceCmd "Documentation for syntax") (fun x => 1 + x) `
```
fun x => (Nat.rec ⟨fun x => x, [PUnit.unit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit.unit")⟩ (fun n n_ih => ⟨fun x => (n_ih.1 x).[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ"), n_ih⟩) x).1 1
```

[Live ↪](javascript:openLiveLink\("MQJwpgJgrgxmAEAKAZlAdvAHvAvAPi3gGp4BGASgChLRJYEV1D8zityg"\))
##  3.3. Checking Types[🔗](find/?domain=Verso.Genre.Manual.section&name=hash-check "Permalink")
syntaxChecking Types
`#check` can be used to elaborate a term and check its type.

```
command ::= ...
    | #check term
```

If the provided term is an identifier that is the name of a global constant, then `#check` prints its signature. Otherwise, the term is elaborated as a Lean term and its type is printed.
Elaboration of the term in ``Lean.Parser.Command.check : command``[`#check`](Interacting-with-Lean/#Lean___Parser___Command___check) does not require that the term is fully elaborated; it may contain metavariables. If the term as written _could_ have a type, elaboration succeeds. If a required instance could never be synthesized, then elaboration fails; synthesis problems that are due to metavariables do not block elaboration.
`#check` and Underdetermined Types
In this example, the type of the list's elements is not determined, so the type contains a metavariable:
``fun x => [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") : ?m.4 → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ?m.4`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") fun x => [x] `
```
fun x => [[](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")x[]](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") : ?m.4 → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ?m.4
```

In this example, both the type of the terms being added and the result type of the addition are unknown, because `[HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd")` allows terms of different types to be added. Behind the scenes, a metavariable represents the unknown `[HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd")` instance.
``fun x => x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x : (x : ?m.7) → ?m.8 x`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") fun x => x + x `
```
fun x => x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x : (x : ?m.7) → ?m.8 x
```

[Live ↪](javascript:openLiveLink\("MQYwFgpiDWAEBmBXAdrAHrAvAPlgbTQF0AoY0SGBFdLXDAanSA"\))
syntaxTesting Type Errors

```
command ::= ...
    | #check_failure term
```

This variant of ``Lean.Parser.Command.check : command``[`#check`](Interacting-with-Lean/#Lean___Parser___Command___check) elaborates the term using the same process as ``Lean.Parser.Command.check : command``[`#check`](Interacting-with-Lean/#Lean___Parser___Command___check). If elaboration succeeds, it is an error; if it fails, there is no error. The partially-elaborated term and any type information that was discovered are added to the [message log](Interacting-with-Lean/#--tech-term-message-log).
Checking for Type Errors
Attempting to add a string to a natural number fails, as expected:
``"one" [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 : ?m.5`[#check_failure](Interacting-with-Lean/#Lean___Parser___Command___check_failure "Documentation for syntax") `failed to synthesize instance of type class   [HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ?m.5  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`"one" + 1 `
```
failed to synthesize instance of type class
  [HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ?m.5

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```

Nonetheless, a partially-elaborated term is available:

```
"one" [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1 : ?m.5
```

[Live ↪](javascript:openLiveLink\("MQYwFgpiDWD6BmBDAlgGwK4CcIAIBEA9gHYR44DUOAjEA"\))
##  3.4. Synthesizing Instances[🔗](find/?domain=Verso.Genre.Manual.section&name=hash-synth "Permalink")
syntaxSynthesizing Instances

```
command ::= ...
    | #synth term
```

The ``Lean.Parser.Command.synth : command``[`#synth`](Interacting-with-Lean/#Lean___Parser___Command___synth) command invokes Lean's [type class](Type-Classes/#--tech-term-type-class) resolution machinery and attempts to perform [instance synthesis](Type-Classes/Instance-Synthesis/#instance-synth) to find an instance for the given type class. If it succeeds, then the resulting instance term is output.
Synthesizing a Type Class Instance
Lean uses type classes to overload operations like addition. The `+` operator is notation for a call to `[HAdd.hAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")`, which is the single method in the `[HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd")` type class. This example shows that Lean will let us add two integers, and the result will be an integer:
``instHAdd`[#synth](Interacting-with-Lean/#Lean___Parser___Command___synth "Documentation for syntax") [HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") `
```
instHAdd
```

By default, Lean does not show the implicit arguments in the output term. Instance arguments are implicit, however, which decreases the usefulness of this output for understanding instance synthesis. Setting the option `pp.explicit` to `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` causes Lean to display implicit arguments, including instances:
`set_option pp.explicit true [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") `@instHAdd [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") Int.instAdd`[#synth](Interacting-with-Lean/#Lean___Parser___Command___synth "Documentation for syntax") [HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") `
```
@instHAdd [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") Int.instAdd
```

Lean does not allow the addition of integers and strings, as demonstrated by this failure of type class instance synthesis:
``failed to synthesize   [HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")  Hint: Additional diagnostic information may be available using the `set_option diagnostics true` command.`[#synth](Interacting-with-Lean/#Lean___Parser___Command___synth "Documentation for syntax") [HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") `
```
failed to synthesize
  [HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")

Hint: Additional diagnostic information may be available using the `set_option diagnostics true` command.
```

##  3.5. Querying the Context[🔗](find/?domain=Verso.Genre.Manual.section&name=hash-print "Permalink")
The `#print` family of commands are used to query Lean for information about definitions.
syntaxPrinting Definitions

```
command ::= ...
    | #print ident
```

Prints the definition of a constant.
Printing a definition with ``Lean.Parser.Command.print : command```#print` prints the definition as a term. Theorems that were proved using [tactics](Tactic-Proofs/#tactics) may be very large when printed as terms.
syntaxPrinting Strings

```
command ::= ...
    | #print str
```

Adds the string literal to Lean's [message log](Interacting-with-Lean/#--tech-term-message-log).
syntaxPrinting Axioms

```
command ::= ...
    | #print axioms ident
```

Lists all axioms that the constant transitively relies on. See [the documentation for axioms](Axioms/#print-axioms) for more information.
Printing Axioms
These two functions each swap the elements in a pair of bitvectors:
`def swap (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32 × [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32 :=   (y, x)  def swap' (x y : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32) : [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32 × [BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32 :=   let x := x ^^^ y   let y := x ^^^ y   let x := x ^^^ y   (x, y) `
They can be proven equal using [function extensionality](The-Type-System/Functions/#function-extensionality), the [simplifier](The-Simplifier/#the-simplifier), and `[bv_decide](Tactic-Proofs/Tactic-Reference/#bv_decide "Documentation for tactic")`:
`theorem swap_eq_swap' : [swap](Interacting-with-Lean/#swap-_LPAR_in-Printing-Axioms_RPAR_ "Definition of example") = [swap'](Interacting-with-Lean/#swap___-_LPAR_in-Printing-Axioms_RPAR_ "Definition of example") := by⊢ [swap](Interacting-with-Lean/#swap-_LPAR_in-Printing-Axioms_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [swap'](Interacting-with-Lean/#swap___-_LPAR_in-Printing-Axioms_RPAR_ "Definition of example")   [funext](Tactic-Proofs/Tactic-Reference/#funext-next "Documentation for tactic") x yh.hx:[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32y:[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32⊢ [swap](Interacting-with-Lean/#swap-_LPAR_in-Printing-Axioms_RPAR_ "Definition of example") x y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [swap'](Interacting-with-Lean/#swap___-_LPAR_in-Printing-Axioms_RPAR_ "Definition of example") x y   [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") only [[swap](Interacting-with-Lean/#swap-_LPAR_in-Printing-Axioms_RPAR_ "Definition of example"), [swap'](Interacting-with-Lean/#swap___-_LPAR_in-Printing-Axioms_RPAR_ "Definition of example"), Prod.mk.injEq]h.hx:[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32y:[BitVec](Basic-Types/Bitvectors/#BitVec___ofFin "Documentation for BitVec") 32⊢ y [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [^^^](Type-Classes/Basic-Classes/#HXor___mk "Documentation for HXor.hXor") y [^^^](Type-Classes/Basic-Classes/#HXor___mk "Documentation for HXor.hXor") [(](Type-Classes/Basic-Classes/#HXor___mk "Documentation for HXor.hXor")x [^^^](Type-Classes/Basic-Classes/#HXor___mk "Documentation for HXor.hXor") y [^^^](Type-Classes/Basic-Classes/#HXor___mk "Documentation for HXor.hXor") y[)](Type-Classes/Basic-Classes/#HXor___mk "Documentation for HXor.hXor") [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") x [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x [^^^](Type-Classes/Basic-Classes/#HXor___mk "Documentation for HXor.hXor") y [^^^](Type-Classes/Basic-Classes/#HXor___mk "Documentation for HXor.hXor") y   bv_decideAll goals completed! 🐙 `
The resulting proof makes use of a number of axioms:
``'swap_eq_swap'' depends on axioms: [[propext](The-Type-System/Propositions/#propext "Documentation for propext"), Classical.choice, [Quot.sound](The-Type-System/Quotients/#Quot___sound "Documentation for Quot.sound"), swap_eq_swap'._native.bv_decide.ax_3]`[#print](Interacting-with-Lean/#Lean___Parser___Command___printAxioms "Documentation for syntax") [axioms](Interacting-with-Lean/#Lean___Parser___Command___printAxioms "Documentation for syntax") [swap_eq_swap'](Interacting-with-Lean/#swap_eq_swap___-_LPAR_in-Printing-Axioms_RPAR_ "Definition of example") `
```
'swap_eq_swap'' depends on axioms: [[propext](The-Type-System/Propositions/#propext "Documentation for propext"), Classical.choice, [Quot.sound](The-Type-System/Quotients/#Quot___sound "Documentation for Quot.sound"), swap_eq_swap'._native.bv_decide.ax_3]
```

The axiom `swap_eq_swap'._native.bv_decide.ax_3` was generated by `[bv_decide](Tactic-Proofs/Tactic-Reference/#bv_decide "Documentation for tactic")`, showing that native code was used to translate an external proof certificate into a Lean proof term.
[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAZRgEwHQBUCGBjGxuoBCAagCICm2wy5AULTQGZwDOA7pmHABQAecATzgAuOIWAxilOAGYATAEoRYiVOyy5cAOsrJ0+SIC8tODwEAaOLwX0mrDmADkPfkNHi96+Uver9mnQ81DSMTOAAbcnh+YUMrOAA9JMEwyPg3OP4khJTTNPjY+Ozcl0sBG1oYAAtyaHIQe04AfXIARyb2TmdRTq443u64gCMBMMYAVwA7cl5okpZQLghJ8KEAbV7LAcsABSgINBAAa1RgSYArAFFWgF0woYA3JpoqGnoAYjAoM/hMXmAICAWI0wC12gMgA"\))
syntaxPrinting Equations
The command ``Lean.Parser.Command.printEqns : command```#print equations`, which can be abbreviated ``Lean.Parser.Command.printEqns : command```#print eqns`, displays the [equational lemmas](Elaboration-and-Compilation/#--tech-term-equational-lemmas) for a function.

```
command ::= ...
    | #print equations ident
```

```
command ::= ...
    | #print eqns ident
```

Printing Equations
`def intersperse (x : α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α   | y :: z :: zs => y :: x :: [intersperse](Interacting-with-Lean/#intersperse-_LPAR_in-Printing-Equations_RPAR_ "Definition of example") x (z :: zs)   | xs => xs  `equations: @[defeq] theorem intersperse.eq_1.{u_1} : ∀ {α : Type u_1} (x y z : α) (zs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α),   [intersperse](Interacting-with-Lean/#intersperse-_LPAR_in-Printing-Equations_RPAR_ "Definition of example") x [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") z [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") zs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [intersperse](Interacting-with-Lean/#intersperse-_LPAR_in-Printing-Equations_RPAR_ "Definition of example") x [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")z [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") zs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") theorem intersperse.eq_2.{u_1} : ∀ {α : Type u_1} (x : α) (x_1 : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α),   (∀ (y z : α) (zs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α), x_1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") z [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") zs → [False](Basic-Propositions/Truth/#False "Documentation for False")) → [intersperse](Interacting-with-Lean/#intersperse-_LPAR_in-Printing-Equations_RPAR_ "Definition of example") x x_1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x_1`#print equations [intersperse](Interacting-with-Lean/#intersperse-_LPAR_in-Printing-Equations_RPAR_ "Definition of example") `
```
equations:
@[defeq] theorem intersperse.eq_1.{u_1} : ∀ {α : Type u_1} (x y z : α) (zs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α),
  [intersperse](Interacting-with-Lean/#intersperse-_LPAR_in-Printing-Equations_RPAR_ "Definition of example") x [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") z [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") zs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [intersperse](Interacting-with-Lean/#intersperse-_LPAR_in-Printing-Equations_RPAR_ "Definition of example") x [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")z [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") zs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
theorem intersperse.eq_2.{u_1} : ∀ {α : Type u_1} (x : α) (x_1 : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α),
  (∀ (y z : α) (zs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α), x_1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") z [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") zs → [False](Basic-Propositions/Truth/#False "Documentation for False")) → [intersperse](Interacting-with-Lean/#intersperse-_LPAR_in-Printing-Equations_RPAR_ "Definition of example") x x_1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") x_1
```

It does not print the defining equation, nor the unfolding equation:
``intersperse.eq_def.{u_1} {α : Type u_1} (x : α) (x✝ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :   [intersperse](Interacting-with-Lean/#intersperse-_LPAR_in-Printing-Equations_RPAR_ "Definition of example") x x✝ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")     match x✝ with     | y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") z [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") zs => y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [intersperse](Interacting-with-Lean/#intersperse-_LPAR_in-Printing-Equations_RPAR_ "Definition of example") x [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")z [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") zs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")     | xs => xs`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") intersperse.eq_def `
```
intersperse.eq_def.{u_1} {α : Type u_1} (x : α) (x✝ : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [intersperse](Interacting-with-Lean/#intersperse-_LPAR_in-Printing-Equations_RPAR_ "Definition of example") x x✝ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
    match x✝ with
    | y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") z [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") zs => y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [intersperse](Interacting-with-Lean/#intersperse-_LPAR_in-Printing-Equations_RPAR_ "Definition of example") x [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")z [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") zs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
    | xs => xs
```
``intersperse.eq_unfold.{u_1} :   [@](Interacting-with-Lean/#intersperse-_LPAR_in-Printing-Equations_RPAR_ "Definition of example")[intersperse](Interacting-with-Lean/#intersperse-_LPAR_in-Printing-Equations_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") fun {α} x x_1 =>     match x_1 with     | y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") z [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") zs => y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [intersperse](Interacting-with-Lean/#intersperse-_LPAR_in-Printing-Equations_RPAR_ "Definition of example") x [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")z [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") zs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")     | xs => xs`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") intersperse.eq_unfold `
```
intersperse.eq_unfold.{u_1} :
  [@](Interacting-with-Lean/#intersperse-_LPAR_in-Printing-Equations_RPAR_ "Definition of example")[intersperse](Interacting-with-Lean/#intersperse-_LPAR_in-Printing-Equations_RPAR_ "Definition of example") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") fun {α} x x_1 =>
    match x_1 with
    | y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") z [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") zs => y [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") x [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") [intersperse](Interacting-with-Lean/#intersperse-_LPAR_in-Printing-Equations_RPAR_ "Definition of example") x [(](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")z [::](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") zs[)](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")
    | xs => xs
```

[Live ↪](javascript:openLiveLink\("CYUwZgBAlgdgLiATgZwA5OSCAKAHhALgkEbgASkIgBkpk4SJAkwipruICgIIAfCAT0KIAvAREHIIAXgB8fEfgJFYCFOhRZ82YQtHJSHbhFzjph5GzYBiVIiUQQARwCuAQzhQA9jHFKMqzOYsAYwALEECAa2h4XwwQADoHAH1QMACQsMifFViE+0THGDB3ABtgIA"\))
syntaxScope Information
`#where` gives a description of the state of the current scope scope. This includes the current namespace, `[open](Tactic-Proofs/The-Tactic-Language/#open "Documentation for tactic")` namespaces, `universe` and `variable` commands, and options set with `[set_option](Tactic-Proofs/The-Tactic-Language/#set_option "Documentation for tactic")`.

```
command ::= ...
    | 


#where gives a description of the state of the current scope scope.
This includes the current namespace, open namespaces, universe and variable commands,
and options set with set_option.


#where
```

Scope Information
The ``Lean.Parser.Command.where : command`
`[`#where`](Interacting-with-Lean/#Lean___Parser___Command___where) command displays all the modifications made to the current [section scope](Namespaces-and-Sections/#--tech-term-section-scope), both in the current scope and in the scopes in which it is nested.
`[section](Namespaces-and-Sections/#Lean___Parser___Command___section "Documentation for syntax") [open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Nat  [namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") A [variable](Namespaces-and-Sections/#Lean___Parser___Command___variable "Documentation for syntax") (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) [namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") B  [open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") List set_option pp.funBinderTypes true  `namespace A.B  open Nat List  variable (n : Nat)  set_option pp.funBinderTypes true set_option pp.tagAppFns true`[#where](Interacting-with-Lean/#Lean___Parser___Command___where "Documentation for syntax") end A.B end `
```
namespace A.B

open Nat List

variable (n : Nat)

set_option pp.funBinderTypes true
set_option pp.tagAppFns true
```

[Live ↪](javascript:openLiveLink\("M4UwxgLglg9gdgKBgBxHABAOQIYQQubAWxGGWzBHQEEEA3bAJymwCMAbKgCgwC4tcASgLFS5SugBC+FGnQAZKMDygIAfRTR46ZMgB0AMwCucSVDgATEIwAqAT1TB0ERkZD4AxAHcAFtfcIaBY0etJBQA"\))
syntaxChecking the Lean Version
Shows the current Lean version. Prints `Lean.versionString`.

```
command ::= ...
    | 


Shows the current Lean version. Prints Lean.versionString. 


#version
```

##  3.6. Testing Output with `#guard_msgs`[🔗](find/?domain=Verso.Genre.Manual.section&name=hash-guard_msgs "Permalink")
The ``Lean.guardMsgsCmd : command`
`/-- ... -/ #guard_msgs in cmd` captures the messages generated by the command `cmd` and checks that they match the contents of the docstring.
Basic example:

```
/--
error: Unknown identifier `x`
-/
#guard_msgs in
example : α := x

```

This checks that there is such an error and then consumes the message.
By default, the command captures all messages, but the filter condition can be adjusted. For example, we can select only warnings:

```
/--
warning: declaration uses 'sorry'
-/
#guard_msgs(warning) in
example : α := sorry

```

or only errors

```
#guard_msgs(error) in
example : α := sorry

```

In the previous example, since warnings are not captured there is a warning on `sorry`. We can drop the warning completely with

```
#guard_msgs(error, drop warning) in
example : α := sorry

```

In general, `#guard_msgs` accepts a comma-separated list of configuration clauses in parentheses:

```
#guard_msgs (configElt,*) in cmd

```

By default, the configuration list is `(check all, whitespace := normalized, ordering := exact, positions := false)`.
Message filters select messages by severity:
  * `info`, `warning`, `error`: (non-trace) messages with the given severity level.
  * `trace`: trace messages
  * `all`: all messages.


The filters can be prefixed with the action to take:
  * `check` (the default): capture and check the message
  * `drop`: drop the message
  * `pass`: let the message pass through


If no filter is specified, `check all` is assumed. Otherwise, these filters are processed in left-to-right order, with an implicit `pass all` at the end.
Whitespace handling (after trimming leading and trailing whitespace):
  * `whitespace := exact` requires an exact whitespace match.
  * `whitespace := normalized` converts all newline characters to a space before matching (the default). This allows breaking long lines.
  * `whitespace := lax` collapses whitespace to a single space before matching.


Message ordering:
  * `ordering := exact` uses the exact ordering of the messages (the default).
  * `ordering := sorted` sorts the messages in lexicographic order. This helps with testing commands that are non-deterministic in their ordering.


Position reporting:
  * `positions := true` reports the ranges of all messages relative to the line on which `#guard_msgs` appears.
  * `positions := false` does not report position info.


Substring matching:
  * `substring := true` checks that the docstring appears as a substring of the output (after whitespace normalization). This is useful when you only care about part of the message.
  * `substring := false` (the default) requires exact matching (modulo whitespace normalization).


Stabilizing output: When messages contain autogenerated names (e.g., metavariables like `?m.47`), the output may differ between runs or Lean versions. Use `set_option pp.mvars.anonymous false` to replace anonymous metavariables with `?_` while preserving user-named metavariables like `?a`. Alternatively, `set_option pp.mvars false` replaces all metavariables with `?_`. Similarly, `set_option pp.fvars.anonymous false` replaces loose free variable names like `_fvar.22` with `_fvar._`.
For example, `#guard_msgs (error, drop all) in cmd` means to check errors and drop everything else.
The command elaborator has special support for `#guard_msgs` for linting. The `#guard_msgs` itself wants to capture linter warnings, so it elaborates the command it is attached to as if it were a top-level command. However, the command elaborator runs linters for _all_ top-level commands, which would include `#guard_msgs` itself, and would cause duplicate and/or uncaptured linter warnings. The top-level command elaborator only runs the linters if `#guard_msgs` is not present.
`[`#guard_msgs`](Interacting-with-Lean/#Lean___guardMsgsCmd) command can be used to ensure that the messages output by a command are as expected. Together with the interaction commands in this section, it can be used to construct a file that will only elaborate if the output is as expected; such a file can be used as a [test driver](Build-Tools-and-Distribution/Lake/#--tech-term-test-driver) in [Lake](Build-Tools-and-Distribution/Lake/#lake).
syntaxDocumenting Expected Output

```
command ::= ...
    | 


/-- ... -/ #guard_msgs in cmd captures the messages generated by the command cmd
and checks that they match the contents of the docstring.


Basic example:


```
/--
error: Unknown identifier `x`
-/
#guard_msgs in
example : α := x

```

This checks that there is such an error and then consumes the message.
By default, the command captures all messages, but the filter condition can be adjusted. For example, we can select only warnings:

```
/--
warning: declaration uses 'sorry'
-/
#guard_msgs(warning) in
example : α := sorry

```

or only errors

```
#guard_msgs(error) in
example : α := sorry

```

In the previous example, since warnings are not captured there is a warning on `sorry`. We can drop the warning completely with

```
#guard_msgs(error, drop warning) in
example : α := sorry

```

In general, `#guard_msgs` accepts a comma-separated list of configuration clauses in parentheses:

```
#guard_msgs (configElt,*) in cmd

```

By default, the configuration list is `(check all, whitespace := normalized, ordering := exact, positions := false)`.
Message filters select messages by severity:
  * `info`, `warning`, `error`: (non-trace) messages with the given severity level.
  * `trace`: trace messages
  * `all`: all messages.


The filters can be prefixed with the action to take:
  * `check` (the default): capture and check the message
  * `drop`: drop the message
  * `pass`: let the message pass through


If no filter is specified, `check all` is assumed. Otherwise, these filters are processed in left-to-right order, with an implicit `pass all` at the end.
Whitespace handling (after trimming leading and trailing whitespace):
  * `whitespace := exact` requires an exact whitespace match.
  * `whitespace := normalized` converts all newline characters to a space before matching (the default). This allows breaking long lines.
  * `whitespace := lax` collapses whitespace to a single space before matching.


Message ordering:
  * `ordering := exact` uses the exact ordering of the messages (the default).
  * `ordering := sorted` sorts the messages in lexicographic order. This helps with testing commands that are non-deterministic in their ordering.


Position reporting:
  * `positions := true` reports the ranges of all messages relative to the line on which `#guard_msgs` appears.
  * `positions := false` does not report position info.


Substring matching:
  * `substring := true` checks that the docstring appears as a substring of the output (after whitespace normalization). This is useful when you only care about part of the message.
  * `substring := false` (the default) requires exact matching (modulo whitespace normalization).


Stabilizing output: When messages contain autogenerated names (e.g., metavariables like `?m.47`), the output may differ between runs or Lean versions. Use `set_option pp.mvars.anonymous false` to replace anonymous metavariables with `?_` while preserving user-named metavariables like `?a`. Alternatively, `set_option pp.mvars false` replaces all metavariables with `?_`. Similarly, `set_option pp.fvars.anonymous false` replaces loose free variable names like `_fvar.22` with `_fvar._`.
For example, `#guard_msgs (error, drop all) in cmd` means to check errors and drop everything else.
The command elaborator has special support for `#guard_msgs` for linting. The `#guard_msgs` itself wants to capture linter warnings, so it elaborates the command it is attached to as if it were a top-level command. However, the command elaborator runs linters for _all_ top-level commands, which would include `#guard_msgs` itself, and would cause duplicate and/or uncaptured linter warnings. The top-level command elaborator only runs the linters if `#guard_msgs` is not present.
`[` A `docComment` parses a "documentation comment" like `/-- foo -/`. This is not treated like a regular comment (that is, as whitespace); it is parsed and forms part of the syntax tree structure. At parse time, `docComment` checks the value of the `doc.verso` option. If it is true, the contents are parsed as Verso markup. If not, the contents are treated as plain text or Markdown. Use `plainDocComment` to always treat the contents as plain text. A plain text doc comment node contains a `/--` atom and then the remainder of the comment, `foo -/` in this example. Use `TSyntax.getDocString` to extract the body text from a doc string syntax node. A Verso comment node contains the `/--` atom, the document's syntax tree, and a closing `-/` atom. `docComment](Definitions/Modifiers/#Lean___Parser___Command___docComment)? #guard_msgs ((guardMsgsSpecElt,*))? in command
```

`/-- ... -/ #guard_msgs in cmd` captures the messages generated by the command `cmd` and checks that they match the contents of the docstring.
Basic example:
`/-- error: Unknown identifier `x` -/ [#guard_msgs](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax") [in](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax") example : α := x `
This checks that there is such an error and then consumes the message.
By default, the command captures all messages, but the filter condition can be adjusted. For example, we can select only warnings:

```
/--
warning: declaration uses 'sorry'
-/
#guard_msgs(warning) in
example : α := sorry

```

or only errors
`[#guard_msgs](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax")(error) [in](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax") `declaration uses `sorry``example : α := sorry `
In the previous example, since warnings are not captured there is a warning on `[sorry](Tactic-Proofs/Tactic-Reference/#sorry "Documentation for tactic")`. We can drop the warning completely with
`[#guard_msgs](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax")(error, drop warning) [in](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax") example : α := sorry `
In general, `#guard_msgs` accepts a comma-separated list of configuration clauses in parentheses:
`[#guard_msgs](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax") (`
By default, the configuration list is `(check all, whitespace := normalized, ordering := exact, positions := false)`.
Message filters select messages by severity:
  * `info`, `warning`, `error`: (non-trace) messages with the given severity level.
  * `[trace](Tactic-Proofs/Tactic-Reference/#trace "Documentation for tactic")`: trace messages
  * `all`: all messages.


The filters can be prefixed with the action to take:
  * `check` (the default): capture and check the message
  * `drop`: drop the message
  * `pass`: let the message pass through


If no filter is specified, `check all` is assumed. Otherwise, these filters are processed in left-to-right order, with an implicit `pass all` at the end.
Whitespace handling (after trimming leading and trailing whitespace):
  * `whitespace := exact` requires an exact whitespace match.
  * `whitespace := normalized` converts all newline characters to a space before matching (the default). This allows breaking long lines.
  * `whitespace := lax` collapses whitespace to a single space before matching.


Message ordering:
  * `ordering := exact` uses the exact ordering of the messages (the default).
  * `ordering := sorted` sorts the messages in lexicographic order. This helps with testing commands that are non-deterministic in their ordering.


Position reporting:
  * `positions := true` reports the ranges of all messages relative to the line on which `#guard_msgs` appears.
  * `positions := false` does not report position info.


Substring matching:
  * `substring := true` checks that the docstring appears as a substring of the output (after whitespace normalization). This is useful when you only care about part of the message.
  * `substring := false` (the default) requires exact matching (modulo whitespace normalization).


Stabilizing output: When messages contain autogenerated names (e.g., metavariables like `?m.47`), the output may differ between runs or Lean versions. Use `set_option pp.mvars.anonymous false` to replace anonymous metavariables with `?_` while preserving user-named metavariables like `?a`. Alternatively, `set_option pp.mvars false` replaces all metavariables with `?_`. Similarly, `set_option pp.fvars.anonymous false` replaces loose free variable names like `_fvar.22` with `_fvar._`.
For example, `#guard_msgs (error, drop all) in cmd` means to check errors and drop everything else.
The command elaborator has special support for `#guard_msgs` for linting. The `#guard_msgs` itself wants to capture linter warnings, so it elaborates the command it is attached to as if it were a top-level command. However, the command elaborator runs linters for _all_ top-level commands, which would include `#guard_msgs` itself, and would cause duplicate and/or uncaptured linter warnings. The top-level command elaborator only runs the linters if `#guard_msgs` is not present.
Testing Return Values
The ``Lean.guardMsgsCmd : command`
`[`#guard_msgs`](Interacting-with-Lean/#Lean___guardMsgsCmd) command can ensure that a set of test cases pass:
`def reverse : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α := [helper](Interacting-with-Lean/#reverse___helper-_LPAR_in-Testing-Return-Values_RPAR_ "Definition of example") [] where   helper acc     | [] => acc     | x :: xs => [helper](Interacting-with-Lean/#reverse___helper-_LPAR_in-Testing-Return-Values_RPAR_ "Definition of example") (x :: acc) xs  /-- info: [] -/ [#guard_msgs](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax") [in](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax") [#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [reverse](Interacting-with-Lean/#reverse-_LPAR_in-Testing-Return-Values_RPAR_ "Definition of example") ([] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))  /-- info: ['c', 'b', 'a'] -/ [#guard_msgs](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax") [in](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax") [#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [reverse](Interacting-with-Lean/#reverse-_LPAR_in-Testing-Return-Values_RPAR_ "Definition of example") "abc".toList `
[Live ↪](javascript:openLiveLink\("CYUwZgBATiBuJQM4ggLggGQJaIC4UEbgCQJMJMd8jUBeCACxABsAHBCAbQF0AoAd3pi4Q6jFlAgBDAMaTBQiAB92HCFQB8E6bKGKAHmnQ7EK9fWasAFHtTopkgJQRDXLgHoAtG4hYAdmAD26JwQbi5cAMQA5gCu4lDAAPoAtogRRj7hcOIM0HAIyBDmQejYeBAAcuK4ds7unj7+gQDkko0ANBCNAEZtHeKNyiHh0bEJyale3hmwWTnwSCgAROKdkgsAdLh+JbhAA"\))
The behavior of the ``Lean.guardMsgsCmd : command`
`/-- ... -/ #guard_msgs in cmd` captures the messages generated by the command `cmd` and checks that they match the contents of the docstring.
Basic example:

```
/--
error: Unknown identifier `x`
-/
#guard_msgs in
example : α := x

```

This checks that there is such an error and then consumes the message.
By default, the command captures all messages, but the filter condition can be adjusted. For example, we can select only warnings:

```
/--
warning: declaration uses 'sorry'
-/
#guard_msgs(warning) in
example : α := sorry

```

or only errors

```
#guard_msgs(error) in
example : α := sorry

```

In the previous example, since warnings are not captured there is a warning on `sorry`. We can drop the warning completely with

```
#guard_msgs(error, drop warning) in
example : α := sorry

```

In general, `#guard_msgs` accepts a comma-separated list of configuration clauses in parentheses:

```
#guard_msgs (configElt,*) in cmd

```

By default, the configuration list is `(check all, whitespace := normalized, ordering := exact, positions := false)`.
Message filters select messages by severity:
  * `info`, `warning`, `error`: (non-trace) messages with the given severity level.
  * `trace`: trace messages
  * `all`: all messages.


The filters can be prefixed with the action to take:
  * `check` (the default): capture and check the message
  * `drop`: drop the message
  * `pass`: let the message pass through


If no filter is specified, `check all` is assumed. Otherwise, these filters are processed in left-to-right order, with an implicit `pass all` at the end.
Whitespace handling (after trimming leading and trailing whitespace):
  * `whitespace := exact` requires an exact whitespace match.
  * `whitespace := normalized` converts all newline characters to a space before matching (the default). This allows breaking long lines.
  * `whitespace := lax` collapses whitespace to a single space before matching.


Message ordering:
  * `ordering := exact` uses the exact ordering of the messages (the default).
  * `ordering := sorted` sorts the messages in lexicographic order. This helps with testing commands that are non-deterministic in their ordering.


Position reporting:
  * `positions := true` reports the ranges of all messages relative to the line on which `#guard_msgs` appears.
  * `positions := false` does not report position info.


Substring matching:
  * `substring := true` checks that the docstring appears as a substring of the output (after whitespace normalization). This is useful when you only care about part of the message.
  * `substring := false` (the default) requires exact matching (modulo whitespace normalization).


Stabilizing output: When messages contain autogenerated names (e.g., metavariables like `?m.47`), the output may differ between runs or Lean versions. Use `set_option pp.mvars.anonymous false` to replace anonymous metavariables with `?_` while preserving user-named metavariables like `?a`. Alternatively, `set_option pp.mvars false` replaces all metavariables with `?_`. Similarly, `set_option pp.fvars.anonymous false` replaces loose free variable names like `_fvar.22` with `_fvar._`.
For example, `#guard_msgs (error, drop all) in cmd` means to check errors and drop everything else.
The command elaborator has special support for `#guard_msgs` for linting. The `#guard_msgs` itself wants to capture linter warnings, so it elaborates the command it is attached to as if it were a top-level command. However, the command elaborator runs linters for _all_ top-level commands, which would include `#guard_msgs` itself, and would cause duplicate and/or uncaptured linter warnings. The top-level command elaborator only runs the linters if `#guard_msgs` is not present.
`[`#guard_msgs`](Interacting-with-Lean/#Lean___guardMsgsCmd) command can be specified in three ways:
  1. Providing a filter that selects a subset of messages to be checked
  2. Specifying a whitespace comparison strategy
  3. Deciding to sort messages by their content or by the order in which they were produced


These configuration options are provided in parentheses, separated by commas.
syntaxSpecifying `#guard_msgs` Behavior

```
guardMsgsSpecElt ::=
    


A message filter specification for #guard_msgs.




  * 
info, warning, error: capture (non-trace) messages with the given severity level.


  * 
trace: captures trace messages


  * 
all: capture all messages.




The filters can be prefixed with




  * 
check (the default): capture and check the message


  * 
drop: drop the message


  * 
pass: let the message pass through




If no filter is specified, check all is assumed.  Otherwise, these filters are processed in
left-to-right order, with an implicit pass all at the end.


guardMsgsFilter
```

```
guardMsgsSpecElt ::= ...
    | 


Whitespace handling for #guard_msgs:




  * 
whitespace := exact requires an exact whitespace match.


  * 
whitespace := normalized converts all newline characters to a space before matching
(the default). This allows breaking long lines.


  * 
whitespace := lax collapses whitespace to a single space before matching.
In all cases, leading and trailing whitespace is trimmed before matching.




whitespace := guardMsgsWhitespaceArg
```

```
guardMsgsSpecElt ::= ...
    | 


Message ordering for #guard_msgs:




  * 
ordering := exact uses the exact ordering of the messages (the default).


  * 
ordering := sorted sorts the messages in lexicographic order.
This helps with testing commands that are non-deterministic in their ordering.




ordering := guardMsgsOrderingArg
```

There are three kinds of options for ``Lean.guardMsgsCmd : command`
`/-- ... -/ #guard_msgs in cmd` captures the messages generated by the command `cmd` and checks that they match the contents of the docstring.
Basic example:

```
/--
error: Unknown identifier `x`
-/
#guard_msgs in
example : α := x

```

This checks that there is such an error and then consumes the message.
By default, the command captures all messages, but the filter condition can be adjusted. For example, we can select only warnings:

```
/--
warning: declaration uses 'sorry'
-/
#guard_msgs(warning) in
example : α := sorry

```

or only errors

```
#guard_msgs(error) in
example : α := sorry

```

In the previous example, since warnings are not captured there is a warning on `sorry`. We can drop the warning completely with

```
#guard_msgs(error, drop warning) in
example : α := sorry

```

In general, `#guard_msgs` accepts a comma-separated list of configuration clauses in parentheses:

```
#guard_msgs (configElt,*) in cmd

```

By default, the configuration list is `(check all, whitespace := normalized, ordering := exact, positions := false)`.
Message filters select messages by severity:
  * `info`, `warning`, `error`: (non-trace) messages with the given severity level.
  * `trace`: trace messages
  * `all`: all messages.


The filters can be prefixed with the action to take:
  * `check` (the default): capture and check the message
  * `drop`: drop the message
  * `pass`: let the message pass through


If no filter is specified, `check all` is assumed. Otherwise, these filters are processed in left-to-right order, with an implicit `pass all` at the end.
Whitespace handling (after trimming leading and trailing whitespace):
  * `whitespace := exact` requires an exact whitespace match.
  * `whitespace := normalized` converts all newline characters to a space before matching (the default). This allows breaking long lines.
  * `whitespace := lax` collapses whitespace to a single space before matching.


Message ordering:
  * `ordering := exact` uses the exact ordering of the messages (the default).
  * `ordering := sorted` sorts the messages in lexicographic order. This helps with testing commands that are non-deterministic in their ordering.


Position reporting:
  * `positions := true` reports the ranges of all messages relative to the line on which `#guard_msgs` appears.
  * `positions := false` does not report position info.


Substring matching:
  * `substring := true` checks that the docstring appears as a substring of the output (after whitespace normalization). This is useful when you only care about part of the message.
  * `substring := false` (the default) requires exact matching (modulo whitespace normalization).


Stabilizing output: When messages contain autogenerated names (e.g., metavariables like `?m.47`), the output may differ between runs or Lean versions. Use `set_option pp.mvars.anonymous false` to replace anonymous metavariables with `?_` while preserving user-named metavariables like `?a`. Alternatively, `set_option pp.mvars false` replaces all metavariables with `?_`. Similarly, `set_option pp.fvars.anonymous false` replaces loose free variable names like `_fvar.22` with `_fvar._`.
For example, `#guard_msgs (error, drop all) in cmd` means to check errors and drop everything else.
The command elaborator has special support for `#guard_msgs` for linting. The `#guard_msgs` itself wants to capture linter warnings, so it elaborates the command it is attached to as if it were a top-level command. However, the command elaborator runs linters for _all_ top-level commands, which would include `#guard_msgs` itself, and would cause duplicate and/or uncaptured linter warnings. The top-level command elaborator only runs the linters if `#guard_msgs` is not present.
`[`#guard_msgs`](Interacting-with-Lean/#Lean___guardMsgsCmd): filters, whitespace comparison strategies, and orderings.
syntaxOutput Filters for `#guard_msgs`

```



A message filter specification for #guard_msgs.




  * 
info, warning, error: capture (non-trace) messages with the given severity level.


  * 
trace: captures trace messages


  * 
all: capture all messages.




The filters can be prefixed with




  * 
check (the default): capture and check the message


  * 
drop: drop the message


  * 
pass: let the message pass through




If no filter is specified, check all is assumed.  Otherwise, these filters are processed in
left-to-right order, with an implicit pass all at the end.


guardMsgsFilter ::=
    


A message filter specification for #guard_msgs.




  * 
info, warning, error: capture (non-trace) messages with the given severity level.


  * 
trace: captures trace messages


  * 
all: capture all messages.




The filters can be prefixed with




  * 
check (the default): capture and check the message


  * 
drop: drop the message


  * 
pass: let the message pass through




If no filter is specified, check all is assumed.  Otherwise, these filters are processed in
left-to-right order, with an implicit pass all at the end.


drop? all
```

```



A message filter specification for #guard_msgs.




  * 
info, warning, error: capture (non-trace) messages with the given severity level.


  * 
trace: captures trace messages


  * 
all: capture all messages.




The filters can be prefixed with




  * 
check (the default): capture and check the message


  * 
drop: drop the message


  * 
pass: let the message pass through




If no filter is specified, check all is assumed.  Otherwise, these filters are processed in
left-to-right order, with an implicit pass all at the end.


guardMsgsFilter ::= ...
    | 


A message filter specification for #guard_msgs.




  * 
info, warning, error: capture (non-trace) messages with the given severity level.


  * 
trace: captures trace messages


  * 
all: capture all messages.




The filters can be prefixed with




  * 
check (the default): capture and check the message


  * 
drop: drop the message


  * 
pass: let the message pass through




If no filter is specified, check all is assumed.  Otherwise, these filters are processed in
left-to-right order, with an implicit pass all at the end.


drop? info
```

```



A message filter specification for #guard_msgs.




  * 
info, warning, error: capture (non-trace) messages with the given severity level.


  * 
trace: captures trace messages


  * 
all: capture all messages.




The filters can be prefixed with




  * 
check (the default): capture and check the message


  * 
drop: drop the message


  * 
pass: let the message pass through




If no filter is specified, check all is assumed.  Otherwise, these filters are processed in
left-to-right order, with an implicit pass all at the end.


guardMsgsFilter ::= ...
    | 


A message filter specification for #guard_msgs.




  * 
info, warning, error: capture (non-trace) messages with the given severity level.


  * 
trace: captures trace messages


  * 
all: capture all messages.




The filters can be prefixed with




  * 
check (the default): capture and check the message


  * 
drop: drop the message


  * 
pass: let the message pass through




If no filter is specified, check all is assumed.  Otherwise, these filters are processed in
left-to-right order, with an implicit pass all at the end.


drop? warning
```

```



A message filter specification for #guard_msgs.




  * 
info, warning, error: capture (non-trace) messages with the given severity level.


  * 
trace: captures trace messages


  * 
all: capture all messages.




The filters can be prefixed with




  * 
check (the default): capture and check the message


  * 
drop: drop the message


  * 
pass: let the message pass through




If no filter is specified, check all is assumed.  Otherwise, these filters are processed in
left-to-right order, with an implicit pass all at the end.


guardMsgsFilter ::= ...
    | 


A message filter specification for #guard_msgs.




  * 
info, warning, error: capture (non-trace) messages with the given severity level.


  * 
trace: captures trace messages


  * 
all: capture all messages.




The filters can be prefixed with




  * 
check (the default): capture and check the message


  * 
drop: drop the message


  * 
pass: let the message pass through




If no filter is specified, check all is assumed.  Otherwise, these filters are processed in
left-to-right order, with an implicit pass all at the end.


drop? error
```

A message filter specification for `#guard_msgs`.
  * `info`, `warning`, `error`: capture (non-trace) messages with the given severity level.
  * `[trace](Tactic-Proofs/Tactic-Reference/#trace "Documentation for tactic")`: captures trace messages
  * `all`: capture all messages.


The filters can be prefixed with
  * `check` (the default): capture and check the message
  * `drop`: drop the message
  * `pass`: let the message pass through


If no filter is specified, `check all` is assumed. Otherwise, these filters are processed in left-to-right order, with an implicit `pass all` at the end.
syntaxWhitespace Comparison for `#guard_msgs`

```
guardMsgsWhitespaceArg ::=
    exact
```

```
guardMsgsWhitespaceArg ::= ...
    | lax
```

```
guardMsgsWhitespaceArg ::= ...
    | normalized
```

Leading and trailing whitespace is always ignored when comparing messages. On top of that, the following settings are available:
  * `whitespace := exact` requires an exact whitespace match.
  * `whitespace := normalized` converts all newline characters to a space before matching (the default). This allows breaking long lines.
  * `whitespace := lax` collapses whitespace to a single space before matching.


The option `[guard_msgs.diff](Interacting-with-Lean/#guard_msgs___diff "Documentation for option guard_msgs.diff")` controls the content of the error message that ``Lean.guardMsgsCmd : command`
`/-- ... -/ #guard_msgs in cmd` captures the messages generated by the command `cmd` and checks that they match the contents of the docstring.
Basic example:

```
/--
error: Unknown identifier `x`
-/
#guard_msgs in
example : α := x

```

This checks that there is such an error and then consumes the message.
By default, the command captures all messages, but the filter condition can be adjusted. For example, we can select only warnings:

```
/--
warning: declaration uses 'sorry'
-/
#guard_msgs(warning) in
example : α := sorry

```

or only errors

```
#guard_msgs(error) in
example : α := sorry

```

In the previous example, since warnings are not captured there is a warning on `sorry`. We can drop the warning completely with

```
#guard_msgs(error, drop warning) in
example : α := sorry

```

In general, `#guard_msgs` accepts a comma-separated list of configuration clauses in parentheses:

```
#guard_msgs (configElt,*) in cmd

```

By default, the configuration list is `(check all, whitespace := normalized, ordering := exact, positions := false)`.
Message filters select messages by severity:
  * `info`, `warning`, `error`: (non-trace) messages with the given severity level.
  * `trace`: trace messages
  * `all`: all messages.


The filters can be prefixed with the action to take:
  * `check` (the default): capture and check the message
  * `drop`: drop the message
  * `pass`: let the message pass through


If no filter is specified, `check all` is assumed. Otherwise, these filters are processed in left-to-right order, with an implicit `pass all` at the end.
Whitespace handling (after trimming leading and trailing whitespace):
  * `whitespace := exact` requires an exact whitespace match.
  * `whitespace := normalized` converts all newline characters to a space before matching (the default). This allows breaking long lines.
  * `whitespace := lax` collapses whitespace to a single space before matching.


Message ordering:
  * `ordering := exact` uses the exact ordering of the messages (the default).
  * `ordering := sorted` sorts the messages in lexicographic order. This helps with testing commands that are non-deterministic in their ordering.


Position reporting:
  * `positions := true` reports the ranges of all messages relative to the line on which `#guard_msgs` appears.
  * `positions := false` does not report position info.


Substring matching:
  * `substring := true` checks that the docstring appears as a substring of the output (after whitespace normalization). This is useful when you only care about part of the message.
  * `substring := false` (the default) requires exact matching (modulo whitespace normalization).


Stabilizing output: When messages contain autogenerated names (e.g., metavariables like `?m.47`), the output may differ between runs or Lean versions. Use `set_option pp.mvars.anonymous false` to replace anonymous metavariables with `?_` while preserving user-named metavariables like `?a`. Alternatively, `set_option pp.mvars false` replaces all metavariables with `?_`. Similarly, `set_option pp.fvars.anonymous false` replaces loose free variable names like `_fvar.22` with `_fvar._`.
For example, `#guard_msgs (error, drop all) in cmd` means to check errors and drop everything else.
The command elaborator has special support for `#guard_msgs` for linting. The `#guard_msgs` itself wants to capture linter warnings, so it elaborates the command it is attached to as if it were a top-level command. However, the command elaborator runs linters for _all_ top-level commands, which would include `#guard_msgs` itself, and would cause duplicate and/or uncaptured linter warnings. The top-level command elaborator only runs the linters if `#guard_msgs` is not present.
`[`#guard_msgs`](Interacting-with-Lean/#Lean___guardMsgsCmd) produces when the expected message doesn't match the produced message. By default, ``Lean.guardMsgsCmd : command`
`/-- ... -/ #guard_msgs in cmd` captures the messages generated by the command `cmd` and checks that they match the contents of the docstring.
Basic example:

```
/--
error: Unknown identifier `x`
-/
#guard_msgs in
example : α := x

```

This checks that there is such an error and then consumes the message.
By default, the command captures all messages, but the filter condition can be adjusted. For example, we can select only warnings:

```
/--
warning: declaration uses 'sorry'
-/
#guard_msgs(warning) in
example : α := sorry

```

or only errors

```
#guard_msgs(error) in
example : α := sorry

```

In the previous example, since warnings are not captured there is a warning on `sorry`. We can drop the warning completely with

```
#guard_msgs(error, drop warning) in
example : α := sorry

```

In general, `#guard_msgs` accepts a comma-separated list of configuration clauses in parentheses:

```
#guard_msgs (configElt,*) in cmd

```

By default, the configuration list is `(check all, whitespace := normalized, ordering := exact, positions := false)`.
Message filters select messages by severity:
  * `info`, `warning`, `error`: (non-trace) messages with the given severity level.
  * `trace`: trace messages
  * `all`: all messages.


The filters can be prefixed with the action to take:
  * `check` (the default): capture and check the message
  * `drop`: drop the message
  * `pass`: let the message pass through


If no filter is specified, `check all` is assumed. Otherwise, these filters are processed in left-to-right order, with an implicit `pass all` at the end.
Whitespace handling (after trimming leading and trailing whitespace):
  * `whitespace := exact` requires an exact whitespace match.
  * `whitespace := normalized` converts all newline characters to a space before matching (the default). This allows breaking long lines.
  * `whitespace := lax` collapses whitespace to a single space before matching.


Message ordering:
  * `ordering := exact` uses the exact ordering of the messages (the default).
  * `ordering := sorted` sorts the messages in lexicographic order. This helps with testing commands that are non-deterministic in their ordering.


Position reporting:
  * `positions := true` reports the ranges of all messages relative to the line on which `#guard_msgs` appears.
  * `positions := false` does not report position info.


Substring matching:
  * `substring := true` checks that the docstring appears as a substring of the output (after whitespace normalization). This is useful when you only care about part of the message.
  * `substring := false` (the default) requires exact matching (modulo whitespace normalization).


Stabilizing output: When messages contain autogenerated names (e.g., metavariables like `?m.47`), the output may differ between runs or Lean versions. Use `set_option pp.mvars.anonymous false` to replace anonymous metavariables with `?_` while preserving user-named metavariables like `?a`. Alternatively, `set_option pp.mvars false` replaces all metavariables with `?_`. Similarly, `set_option pp.fvars.anonymous false` replaces loose free variable names like `_fvar.22` with `_fvar._`.
For example, `#guard_msgs (error, drop all) in cmd` means to check errors and drop everything else.
The command elaborator has special support for `#guard_msgs` for linting. The `#guard_msgs` itself wants to capture linter warnings, so it elaborates the command it is attached to as if it were a top-level command. However, the command elaborator runs linters for _all_ top-level commands, which would include `#guard_msgs` itself, and would cause duplicate and/or uncaptured linter warnings. The top-level command elaborator only runs the linters if `#guard_msgs` is not present.
`[`#guard_msgs`](Interacting-with-Lean/#Lean___guardMsgsCmd) shows a line-by-line difference, with a leading `+` used to indicate lines from the produced message and a leading `-` used to indicate lines from the expected message. When messages are large and only differ by a small amount, this can make it easier to notice where they differ. Setting `[guard_msgs.diff](Interacting-with-Lean/#guard_msgs___diff "Documentation for option guard_msgs.diff")` to `false` causes ``Lean.guardMsgsCmd : command`
`/-- ... -/ #guard_msgs in cmd` captures the messages generated by the command `cmd` and checks that they match the contents of the docstring.
Basic example:

```
/--
error: Unknown identifier `x`
-/
#guard_msgs in
example : α := x

```

This checks that there is such an error and then consumes the message.
By default, the command captures all messages, but the filter condition can be adjusted. For example, we can select only warnings:

```
/--
warning: declaration uses 'sorry'
-/
#guard_msgs(warning) in
example : α := sorry

```

or only errors

```
#guard_msgs(error) in
example : α := sorry

```

In the previous example, since warnings are not captured there is a warning on `sorry`. We can drop the warning completely with

```
#guard_msgs(error, drop warning) in
example : α := sorry

```

In general, `#guard_msgs` accepts a comma-separated list of configuration clauses in parentheses:

```
#guard_msgs (configElt,*) in cmd

```

By default, the configuration list is `(check all, whitespace := normalized, ordering := exact, positions := false)`.
Message filters select messages by severity:
  * `info`, `warning`, `error`: (non-trace) messages with the given severity level.
  * `trace`: trace messages
  * `all`: all messages.


The filters can be prefixed with the action to take:
  * `check` (the default): capture and check the message
  * `drop`: drop the message
  * `pass`: let the message pass through


If no filter is specified, `check all` is assumed. Otherwise, these filters are processed in left-to-right order, with an implicit `pass all` at the end.
Whitespace handling (after trimming leading and trailing whitespace):
  * `whitespace := exact` requires an exact whitespace match.
  * `whitespace := normalized` converts all newline characters to a space before matching (the default). This allows breaking long lines.
  * `whitespace := lax` collapses whitespace to a single space before matching.


Message ordering:
  * `ordering := exact` uses the exact ordering of the messages (the default).
  * `ordering := sorted` sorts the messages in lexicographic order. This helps with testing commands that are non-deterministic in their ordering.


Position reporting:
  * `positions := true` reports the ranges of all messages relative to the line on which `#guard_msgs` appears.
  * `positions := false` does not report position info.


Substring matching:
  * `substring := true` checks that the docstring appears as a substring of the output (after whitespace normalization). This is useful when you only care about part of the message.
  * `substring := false` (the default) requires exact matching (modulo whitespace normalization).


Stabilizing output: When messages contain autogenerated names (e.g., metavariables like `?m.47`), the output may differ between runs or Lean versions. Use `set_option pp.mvars.anonymous false` to replace anonymous metavariables with `?_` while preserving user-named metavariables like `?a`. Alternatively, `set_option pp.mvars false` replaces all metavariables with `?_`. Similarly, `set_option pp.fvars.anonymous false` replaces loose free variable names like `_fvar.22` with `_fvar._`.
For example, `#guard_msgs (error, drop all) in cmd` means to check errors and drop everything else.
The command elaborator has special support for `#guard_msgs` for linting. The `#guard_msgs` itself wants to capture linter warnings, so it elaborates the command it is attached to as if it were a top-level command. However, the command elaborator runs linters for _all_ top-level commands, which would include `#guard_msgs` itself, and would cause duplicate and/or uncaptured linter warnings. The top-level command elaborator only runs the linters if `#guard_msgs` is not present.
`[`#guard_msgs`](Interacting-with-Lean/#Lean___guardMsgsCmd) to instead show just the produced message, which can be compared with the expected message in the source file. This can be convenient if the difference between the message is confusing or overwhelming.
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=guard_msgs.diff "Permalink")option
```
guard_msgs.diff
```

Default value: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
When true, show a diff between expected and actual messages if they don't match.
Displaying Differences
The ``Lean.guardMsgsCmd : command`
`[`#guard_msgs`](Interacting-with-Lean/#Lean___guardMsgsCmd) command can be used to test definition of a rose tree `[Tree](Interacting-with-Lean/#Tree-_LPAR_in-Displaying-Differences_RPAR_ "Definition of example")` and a function `[Tree.big](Interacting-with-Lean/#Tree___big-_LPAR_in-Displaying-Differences_RPAR_ "Definition of example")` that creates them:
`inductive Tree (α : Type u) : Type u where   | val : α → [Tree](Interacting-with-Lean/#Tree-_LPAR_in-Displaying-Differences_RPAR_ "Definition of example") α   | branches : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ([Tree](Interacting-with-Lean/#Tree-_LPAR_in-Displaying-Differences_RPAR_ "Definition of example") α) → [Tree](Interacting-with-Lean/#Tree-_LPAR_in-Displaying-Differences_RPAR_ "Definition of example") α  def Tree.big (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Tree](Interacting-with-Lean/#Tree-_LPAR_in-Displaying-Differences_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") :=   [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n < 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [.branches](Interacting-with-Lean/#Tree___branches-_LPAR_in-Displaying-Differences_RPAR_ "Definition of example") [[.val](Interacting-with-Lean/#Tree___val-_LPAR_in-Displaying-Differences_RPAR_ "Definition of example") n, [.val](Interacting-with-Lean/#Tree___val-_LPAR_in-Displaying-Differences_RPAR_ "Definition of example") (n - 1), [.val](Interacting-with-Lean/#Tree___val-_LPAR_in-Displaying-Differences_RPAR_ "Definition of example") n, [.val](Interacting-with-Lean/#Tree___val-_LPAR_in-Displaying-Differences_RPAR_ "Definition of example") (n - 2)]   [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [.branches](Interacting-with-Lean/#Tree___branches-_LPAR_in-Displaying-Differences_RPAR_ "Definition of example") [[.big](Interacting-with-Lean/#Tree___big-_LPAR_in-Displaying-Differences_RPAR_ "Definition of example") (n / 2),  [.big](Interacting-with-Lean/#Tree___big-_LPAR_in-Displaying-Differences_RPAR_ "Definition of example") (n / 3)] `
However, it can be difficult to spot where test failures come from when the output is large:
`set_option [guard_msgs.diff](Interacting-with-Lean/#guard_msgs___diff "Documentation for option guard_msgs.diff") false /-- info: Tree.branches   [Tree.branches      [Tree.branches         [Tree.branches [Tree.val 2, Tree.val 1, Tree.val 2, Tree.val 0],          Tree.branches [Tree.val 1, Tree.val 0, Tree.val 1, Tree.val 0],       Tree.branches [Tree.val 3, Tree.val 2, Tree.val 3, Tree.val 1]],    Tree.branches      [Tree.branches [Tree.val 3, Tree.val 2, Tree.val 3, Tree.val 1],       Tree.branches [Tree.val 2, Tree.val 1, Tree.val 2, Tree.val 0]]] -/ `❌️ Docstring on `#guard_msgs` does not match generated message:  info: Tree.branches   [Tree.branches      [Tree.branches         [Tree.branches [Tree.val 2, Tree.val 1, Tree.val 2, Tree.val 0],          Tree.branches [Tree.val 1, Tree.val 0, Tree.val 1, Tree.val 0]],       Tree.branches [Tree.val 3, Tree.val 2, Tree.val 3, Tree.val 1]],    Tree.branches      [Tree.branches [Tree.val 3, Tree.val 2, Tree.val 3, Tree.val 1],       Tree.branches [Tree.val 2, Tree.val 1, Tree.val 2, Tree.val 0]]]`[#guard_msgs](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax") [in](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax") `Tree.branches   [Tree.branches      [Tree.branches         [Tree.branches [Tree.val 2, Tree.val 1, Tree.val 2, Tree.val 0],          Tree.branches [Tree.val 1, Tree.val 0, Tree.val 1, Tree.val 0]],       Tree.branches [Tree.val 3, Tree.val 2, Tree.val 3, Tree.val 1]],    Tree.branches      [Tree.branches [Tree.val 3, Tree.val 2, Tree.val 3, Tree.val 1],       Tree.branches [Tree.val 2, Tree.val 1, Tree.val 2, Tree.val 0]]]`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Tree.big](Interacting-with-Lean/#Tree___big-_LPAR_in-Displaying-Differences_RPAR_ "Definition of example") 20 `
The evaluation produces:

```
Tree.branches
  [Tree.branches
     [Tree.branches
        [Tree.branches [Tree.val 2, Tree.val 1, Tree.val 2, Tree.val 0],
         Tree.branches [Tree.val 1, Tree.val 0, Tree.val 1, Tree.val 0]],
      Tree.branches [Tree.val 3, Tree.val 2, Tree.val 3, Tree.val 1]],
   Tree.branches
     [Tree.branches [Tree.val 3, Tree.val 2, Tree.val 3, Tree.val 1],
      Tree.branches [Tree.val 2, Tree.val 1, Tree.val 2, Tree.val 0]]]
```

Without `[guard_msgs.diff](Interacting-with-Lean/#guard_msgs___diff "Documentation for option guard_msgs.diff")`, the ``Lean.guardMsgsCmd : command`
`[`#guard_msgs`](Interacting-with-Lean/#Lean___guardMsgsCmd) command reports this error:

```
❌️ Docstring on `#guard_msgs` does not match generated message:

info: Tree.branches
  [Tree.branches
     [Tree.branches
        [Tree.branches [Tree.val 2, Tree.val 1, Tree.val 2, Tree.val 0],
         Tree.branches [Tree.val 1, Tree.val 0, Tree.val 1, Tree.val 0]],
      Tree.branches [Tree.val 3, Tree.val 2, Tree.val 3, Tree.val 1]],
   Tree.branches
     [Tree.branches [Tree.val 3, Tree.val 2, Tree.val 3, Tree.val 1],
      Tree.branches [Tree.val 2, Tree.val 1, Tree.val 2, Tree.val 0]]]
```

Enabling `[guard_msgs.diff](Interacting-with-Lean/#guard_msgs___diff "Documentation for option guard_msgs.diff")` highlights the differences instead, making the error more apparent:
`set_option [guard_msgs.diff](Interacting-with-Lean/#guard_msgs___diff "Documentation for option guard_msgs.diff") true [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") /-- info: Tree.branches   [Tree.branches      [Tree.branches         [Tree.branches [Tree.val 2, Tree.val 1, Tree.val 2, Tree.val 0],          Tree.branches [Tree.val 1, Tree.val 0, Tree.val 1, Tree.val 0,       Tree.branches [Tree.val 3, Tree.val 2, Tree.val 3, Tree.val 1]],    Tree.branches      [Tree.branches [Tree.val 3, Tree.val 2, Tree.val 3, Tree.val 1],       Tree.branches [Tree.val 2, Tree.val 1, Tree.val 2, Tree.val 0]]] -/ `❌️ Docstring on `#guard_msgs` does not match generated message:    info: Tree.branches     [Tree.branches        [Tree.branches           [Tree.branches [Tree.val 2, Tree.val 1, Tree.val 2, Tree.val 0], -          Tree.branches [Tree.val 1, Tree.val 0, Tree.val 1, Tree.val 0, +          Tree.branches [Tree.val 1, Tree.val 0, Tree.val 1, Tree.val 0]],         Tree.branches [Tree.val 3, Tree.val 2, Tree.val 3, Tree.val 1]],      Tree.branches        [Tree.branches [Tree.val 3, Tree.val 2, Tree.val 3, Tree.val 1],         Tree.branches [Tree.val 2, Tree.val 1, Tree.val 2, Tree.val 0]]] `[#guard_msgs](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax") [in](Interacting-with-Lean/#Lean___guardMsgsCmd "Documentation for syntax") `Tree.branches   [Tree.branches      [Tree.branches         [Tree.branches [Tree.val 2, Tree.val 1, Tree.val 2, Tree.val 0],          Tree.branches [Tree.val 1, Tree.val 0, Tree.val 1, Tree.val 0]],       Tree.branches [Tree.val 3, Tree.val 2, Tree.val 3, Tree.val 1]],    Tree.branches      [Tree.branches [Tree.val 3, Tree.val 2, Tree.val 3, Tree.val 1],       Tree.branches [Tree.val 2, Tree.val 1, Tree.val 2, Tree.val 0]]]`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [Tree.big](Interacting-with-Lean/#Tree___big-_LPAR_in-Displaying-Differences_RPAR_ "Definition of example") 20 `
```
❌️ Docstring on `#guard_msgs` does not match generated message:

  info: Tree.branches
    [Tree.branches
       [Tree.branches
          [Tree.branches [Tree.val 2, Tree.val 1, Tree.val 2, Tree.val 0],
-          Tree.branches [Tree.val 1, Tree.val 0, Tree.val 1, Tree.val 0,
+          Tree.branches [Tree.val 1, Tree.val 0, Tree.val 1, Tree.val 0]],
        Tree.branches [Tree.val 3, Tree.val 2, Tree.val 3, Tree.val 1]],
     Tree.branches
       [Tree.branches [Tree.val 3, Tree.val 2, Tree.val 3, Tree.val 1],
        Tree.branches [Tree.val 2, Tree.val 1, Tree.val 2, Tree.val 0]]]

```

[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABAFQE6JQCkI3AyAuNATwAcUIBKQk85CZAdwAtFMAoZZAH2XgEMANjXyAkwjSYUuTj2QAjdPxBRWAZxoAZYKpjJsGLMlzVxBqe3ZhEAMwlYAdHOABzPSBoA5fjGpEzyL10CAF4ZYFt3AB5kAFZkGFZ3R0VlNWQAbXsBYRAAGmQsoTdkAFpkAEZKfMKc6uzisoAmSgBdGURBVRRkpRVEdUynV2x3AHpkZvyCoeLxgGZWoA"\))
##  3.7. Formatted Output[🔗](find/?domain=Verso.Genre.Manual.section&name=format-repr "Permalink")
The `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` type class is used to provide a standard representation for data that can be parsed and evaluated to obtain an equivalent value. This is not a strict correctness criterion: for some types, especially those with embedded propositions, it is impossible to achieve. However, the output produced by a `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instance should be as close as possible to something that can be parsed and evaluated.
In addition to being machine-readable, this representation should be convenient for humans to understand—in particular, lines should not be too long, and nested values should be indented. This is achieved through a two-step process:
  1. The `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instance produces an intermediate document of type `[Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")`, which compactly represents a _set_ of strings that differ with respect to the placement of newlines and indentation.
  2. A rendering process selects the “best” representative from the set, according to criteria such as a desired maximum line length.


In particular, `[Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")` can be built compositionally, so `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instances don't need to take the surrounding indentation context into account.
###  3.7.1. Format[🔗](find/?domain=Verso.Genre.Manual.section&name=Format "Permalink")
A `[Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")`The API described here is an adaptation of Wadler's (Philip Wadler, 2003. [“A Prettier Printer”](https://homepages.inf.ed.ac.uk/wadler/papers/prettier/prettier.pdf). In  _The Fun of Programming, A symposium in honour of Professor Richard Bird's 60th birthday._) It has been modified to be efficient in a strict language and with support for additional features such as metadata tags. is a compact representation of a set of strings. The most important `[Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")` operations are: 

Strings
    
A `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` can be made into a `[Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")` using the `[text](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.text")` constructor. This constructor is registered as a [coercion](Coercions/#coercions) from `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` to `[Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")`, so it is often unnecessary to invoke it explicitly. `[text](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.text") str` represents the singleton set that contains only `str`. If the string contains newline characters (`'\n'`), then they are unconditionally inserted as newlines into the resulting output, regardless of groups. They are, however, indented according to the current indentation level. 

Appending
    
Two `[Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")`s can be appended using the `++` operator from the `[Append](Type-Classes/Basic-Classes/#Append___mk "Documentation for Append") [Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")` instance. 

Groups and Newlines
    
The constructor `[line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line")` represents the set that contains both `"\n" ++ indent` and `" "`, where `indent` is a string with enough spaces to indent the line correctly. Imperatively, it can be thought of as a newline that will be “flattened” to a space if there is sufficient room on the current line. Newlines occur in _groups_ : the nearest enclosing application of the `[group](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.group")` operator determines which group the newline belongs to. By default, either all `[line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line")`s in a group represent `"\n"` or all represent `" "`; groups may also be configured to fill lines, in which case the minimal number of `[line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line")`s in the group represent `"\n"`. Uses of `[line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line")` that do not belong to a group always represent `"\n"`. 

Indentation
    
When a newline is inserted, the output is also indented. `[nest](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.nest") n` increases the indentation of a document by `n` spaces. This is not sufficient to represent all Lean syntax, which sometimes requires that columns align exactly. `[align](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.align")` is a document that ensures that the output string is at the current indentation level, inserting just spaces if possible, or a newline followed by spaces if needed. 

Tagging
    
Lean's interactive features require the ability to associate output with the underlying values that they represent. This allows Lean development environments to present elaborated terms when hovering over terms proof states or error messages, for example. Documents can be _tagged_ with a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` value `n` using `[tag](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.tag") n`; these `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`s should be mapped to the underlying value in a side table.
Widths and Newlines
`[open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Std Format `
The helper `[parenSeq](Interacting-with-Lean/#parenSeq-_LPAR_in-Widths-and-Newlines_RPAR_ "Definition of example")` creates a parenthesized sequence, with grouping and indentation to make it responsive to different output widths.
`def parenSeq (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) : [Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format") :=   [group](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.group") <|     [nest](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.nest") 2 ([text](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.text") "(" ++ [line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line") ++ [joinSep](Interacting-with-Lean/#Std___Format___joinSep "Documentation for Std.Format.joinSep") xs [line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line")) ++     [line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line") ++     ")" `
This document represents a parenthesized sequence of numbers:
`def lst : [Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format") := [parenSeq](Interacting-with-Lean/#parenSeq-_LPAR_in-Widths-and-Newlines_RPAR_ "Definition of example") [nums](Interacting-with-Lean/#lst___nums-_LPAR_in-Widths-and-Newlines_RPAR_ "Definition of example") where nums := [1, 2, 3, 4, 5].[map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map") ([text](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.text") s!"{·}") `
Rendering it with the default line width of 120 characters places the entire sequence on one line:
``( 1 2 3 4 5 ) `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") [lst](Interacting-with-Lean/#lst-_LPAR_in-Widths-and-Newlines_RPAR_ "Definition of example").[pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") `
```
( 1 2 3 4 5 )

```

Because all the `[line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line")`s belong to the same `[group](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.group")`, they will either all be rendered as spaces or all be rendered as newlines. If only 9 characters are available, all of the `[line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line")`s in `[lst](Interacting-with-Lean/#lst-_LPAR_in-Widths-and-Newlines_RPAR_ "Definition of example")` become newlines:
``(   1   2   3   4   5 ) `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([lst](Interacting-with-Lean/#lst-_LPAR_in-Widths-and-Newlines_RPAR_ "Definition of example").[pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") (width := 9)) `
```
(
  1
  2
  3
  4
  5
)

```

This document contains three copies of `[lst](Interacting-with-Lean/#lst-_LPAR_in-Widths-and-Newlines_RPAR_ "Definition of example")` in a further parenthesized sequence:
`def lsts := [parenSeq](Interacting-with-Lean/#parenSeq-_LPAR_in-Widths-and-Newlines_RPAR_ "Definition of example") [[lst](Interacting-with-Lean/#lst-_LPAR_in-Widths-and-Newlines_RPAR_ "Definition of example"), [lst](Interacting-with-Lean/#lst-_LPAR_in-Widths-and-Newlines_RPAR_ "Definition of example"), [lst](Interacting-with-Lean/#lst-_LPAR_in-Widths-and-Newlines_RPAR_ "Definition of example")] `
At the default width, it remains on one line:
``( ( 1 2 3 4 5 ) ( 1 2 3 4 5 ) ( 1 2 3 4 5 ) ) `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") [lsts](Interacting-with-Lean/#lsts-_LPAR_in-Widths-and-Newlines_RPAR_ "Definition of example").[pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") `
```
( ( 1 2 3 4 5 ) ( 1 2 3 4 5 ) ( 1 2 3 4 5 ) )

```

If only 20 characters are available, each occurrence of `[lst](Interacting-with-Lean/#lst-_LPAR_in-Widths-and-Newlines_RPAR_ "Definition of example")` ends up on its own line. This is because converting the outer `[group](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.group")` to newlines is sufficient to keep the string within 20 columns:
``(   ( 1 2 3 4 5 )   ( 1 2 3 4 5 )   ( 1 2 3 4 5 ) ) `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([lsts](Interacting-with-Lean/#lsts-_LPAR_in-Widths-and-Newlines_RPAR_ "Definition of example").[pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") (width := 20)) `
```
(
  ( 1 2 3 4 5 )
  ( 1 2 3 4 5 )
  ( 1 2 3 4 5 )
)

```

If only 10 characters are available, each number must be on its own line:
``(   (     1     2     3     4     5   )   (     1     2     3     4     5   )   (     1     2     3     4     5   ) ) `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([lsts](Interacting-with-Lean/#lsts-_LPAR_in-Widths-and-Newlines_RPAR_ "Definition of example").[pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") (width := 10)) `
```
(
  (
    1
    2
    3
    4
    5
  )
  (
    1
    2
    3
    4
    5
  )
  (
    1
    2
    3
    4
    5
  )
)

```

[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAZRgEwFComApgO0SuAMWhAEMZ1ksAzOMUqXBLARzgAoAPAZzgC44AGWDd4xKGRgBKfkRLl+AXlRw4AcygQArmDgAeAD4rVcHFlFwATBxhZO8AETsHcANSu4AG2Bm3HgFYQPsy6PF4+WDLuxqrevtEmcA5SDpQ0XhYC4pJKdAxMrKZaINyoAO4AFliMRSW5ANoAjAA0Vq0AzK0ALK0ArAC6AHRkuuy29nDcAIQOAN4A7QC+yegAxFgAbqSecACSAPKDYFA+MJ54nqJHjDAwAJ5rm9t7h8en5xyXMNdYt3ccZWAyBgFVyAE4pFI0rQvrw+Io8owcMw2PUvq10RkYP1Hlsdgdru8LqJuD8/rjngS3jgznh2LCyfcAUCQblLAAGSEU/GvE40j70kmM/7sQHA0HwuCNTlSIA"\))
Grouping and Filling
`[open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Std Format `
The helper `[parenSeq](Interacting-with-Lean/#parenSeq-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example")` creates a parenthesized sequence, with each element placed on a new line and indented:
`def parenSeq (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) : [Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format") :=   [nest](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.nest") 2 ([text](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.text") "(" ++ [line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line") ++ [joinSep](Interacting-with-Lean/#Std___Format___joinSep "Documentation for Std.Format.joinSep") xs [line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line")) ++   [line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line") ++   ")" `
`[nums](Interacting-with-Lean/#nums-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example")` contains the numbers one through twenty, as a list of formats:
`def nums : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format") :=   [Nat.fold](Basic-Types/Natural-Numbers/#Nat___fold "Documentation for Nat.fold") 20 (init := []) fun i _ ys =>     [text](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.text") s!"{20 - i}" :: ys ```[Std.Format.text "1",  Std.Format.text "2",  Std.Format.text "3",  Std.Format.text "4",  Std.Format.text "5",  Std.Format.text "6",  Std.Format.text "7",  Std.Format.text "8",  Std.Format.text "9",  Std.Format.text "10",  Std.Format.text "11",  Std.Format.text "12",  Std.Format.text "13",  Std.Format.text "14",  Std.Format.text "15",  Std.Format.text "16",  Std.Format.text "17",  Std.Format.text "18",  Std.Format.text "19",  Std.Format.text "20"]`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [nums](Interacting-with-Lean/#nums-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example") `
Because `[parenSeq](Interacting-with-Lean/#parenSeq-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example")` does not introduce any groups, the resulting document is rendered on a single line:
``(   1   2   3   4   5   6   7   8   9   10   11   12   13   14   15   16   17   18   19   20 ) `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") ([parenSeq](Interacting-with-Lean/#parenSeq-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example") [nums](Interacting-with-Lean/#nums-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example"))) `
This can be fixed by grouping them. `[grouped](Interacting-with-Lean/#grouped-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example")` does so with `[group](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.group")`, while `[filled](Interacting-with-Lean/#filled-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example")` does so with `[fill](Interacting-with-Lean/#Std___Format___fill "Documentation for Std.Format.fill")`.
`def grouped := [group](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.group") ([parenSeq](Interacting-with-Lean/#parenSeq-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example") [nums](Interacting-with-Lean/#nums-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example")) def filled := [fill](Interacting-with-Lean/#Std___Format___fill "Documentation for Std.Format.fill") ([parenSeq](Interacting-with-Lean/#parenSeq-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example") [nums](Interacting-with-Lean/#nums-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example")) `
Both grouping operators cause uses of `[line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line")` to render as spaces. Given sufficient space, both render on a single line:
``( 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ) `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") [grouped](Interacting-with-Lean/#grouped-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example")) `
```
( 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 )

```
``( 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ) `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") [filled](Interacting-with-Lean/#filled-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example")) `
```
( 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 )

```

However, difference become apparent when there is not sufficient space on a single line. Unless _all_ newlines in a `[group](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.group")` can be spaces, none can:
``(   1   2   3   4   5   6   7   8   9   10   11   12   13   14   15   16   17   18   19   20 ) `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") (width := 30) [grouped](Interacting-with-Lean/#grouped-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example")) `
```
(
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  16
  17
  18
  19
  20
)

```

Using `[fill](Interacting-with-Lean/#Std___Format___fill "Documentation for Std.Format.fill")`, on the other hand, only inserts newlines as required to avoid being two wide:
``( 1 2 3 4 5 6 7 8 9 10 11 12   13 14 15 16 17 18 19 20 ) `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") (width := 30) [filled](Interacting-with-Lean/#filled-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example")) `
```
( 1 2 3 4 5 6 7 8 9 10 11 12
  13 14 15 16 17 18 19 20 )

```

The behavior of `[fill](Interacting-with-Lean/#Std___Format___fill "Documentation for Std.Format.fill")` can be seen clearly with longer sequences:
``( 1 2 3 4 5 6 7 8 9 10 11 12   13 14 15 16 17 18 19 20 1 2   3 4 5 6 7 8 9 10 11 12 13 14   15 16 17 18 19 20 1 2 3 4 5   6 7 8 9 10 11 12 13 14 15 16   17 18 19 20 1 2 3 4 5 6 7 8   9 10 11 12 13 14 15 16 17 18   19 20 ) `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") <| [pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") (width := 30) ([fill](Interacting-with-Lean/#Std___Format___fill "Documentation for Std.Format.fill") ([parenSeq](Interacting-with-Lean/#parenSeq-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example") ([nums](Interacting-with-Lean/#nums-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example") ++ [nums](Interacting-with-Lean/#nums-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example") ++ [nums](Interacting-with-Lean/#nums-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example") ++ [nums](Interacting-with-Lean/#nums-_LPAR_in-Grouping-and-Filling_RPAR_ "Definition of example")))) `
```
( 1 2 3 4 5 6 7 8 9 10 11 12
  13 14 15 16 17 18 19 20 1 2
  3 4 5 6 7 8 9 10 11 12 13 14
  15 16 17 18 19 20 1 2 3 4 5
  6 7 8 9 10 11 12 13 14 15 16
  17 18 19 20 1 2 3 4 5 6 7 8
  9 10 11 12 13 14 15 16 17 18
  19 20 )

```

[Live ↪](javascript:openLiveLink\("PYBwpgdgBAygLgEygMWAJwLYEM4ChcJgBmUIWakMYAjlABQAeAzlAFxQAyAlk3CutjgBKNv0w42AXlxQoEMLygAmenDAM+AIjqaoAaj1QANl3n7DAK2CmqIKM2OmwIgzMdnXszUM35CJCABXDBZ2bkVUcT5WaVkAORwAOiJgIyQlAAZ6Uy5oySgAbQBdESJA6C4oAH0oAE8WSQA+N1k1DSgmAEJNAG9MqABaKC4AX11Wdnr8AGIwADcsIzlgphn5xagASQB5RJA0UzgjaDp9sDg4WvoyCggqWiCQoSE/YigAczRgQPAkGI+vj9ruRKDRlk8CG8iFwjEYwH98tDYcDbvdwUwXrhZgsljs9gcIEcTmcLldPt9fpjsRs8ftDsdrhRSVAkXCEFT1rjdnTCQzTkzLvQAO5cBBwAAWUigAGYMiJyT94RycVtuQSiYzzoK6CKxZL/rLSjC2cqaWr6dAADwAHzcJO1uolUsN9FZKNBtDojxYBnR5j9vu9zyEQA"\))
Newline Characters in Strings
Including a newline character in a string causes the rendering process to unconditionally insert a newline. These newlines do, however, respect the current indentation level.
The document `[str](Interacting-with-Lean/#str-_LPAR_in-Newline-Characters-in-Strings_RPAR_ "Definition of example")` consists of an embedded string with two newlines:
`[open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Std Format  def str : [Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format") := [text](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.text") "abc\nxyz\n123" `
Printing the string both with and without grouping results in the newlines being used:
``abc xyz 123 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") [str](Interacting-with-Lean/#str-_LPAR_in-Newline-Characters-in-Strings_RPAR_ "Definition of example").[pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") `
```
abc
xyz
123

```
``abc xyz 123 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([group](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.group") [str](Interacting-with-Lean/#str-_LPAR_in-Newline-Characters-in-Strings_RPAR_ "Definition of example")).[pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") `
```
abc
xyz
123

```

Because the string does not terminate with a newline, the last line of the first string is on the same line as the first line of the second string:
``abc xyz 123abc xyz 123 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([str](Interacting-with-Lean/#str-_LPAR_in-Newline-Characters-in-Strings_RPAR_ "Definition of example") ++ [str](Interacting-with-Lean/#str-_LPAR_in-Newline-Characters-in-Strings_RPAR_ "Definition of example")).[pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") `
```
abc
xyz
123abc
xyz
123

```

Increasing the indentation level, however, causes all three lines of the string to begin at the same column:
``It is:   abc   xyz   123 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([text](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.text") "It is:" ++ [indentD](Interacting-with-Lean/#Std___Format___indentD "Documentation for Std.Format.indentD") [str](Interacting-with-Lean/#str-_LPAR_in-Newline-Characters-in-Strings_RPAR_ "Definition of example")).[pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") `
```
It is:
  abc
  xyz
  123

```
``It is:  abc         xyz         123 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([nest](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.nest") 8 <| [text](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.text") "It is:" ++ [align](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.align") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") ++ [str](Interacting-with-Lean/#str-_LPAR_in-Newline-Characters-in-Strings_RPAR_ "Definition of example")).[pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") `
```
It is:  abc
        xyz
        123

```

[Live ↪](javascript:openLiveLink\("PYBwpgdgBAygLgEygMWAJwLYEM4ChcJgBmUAznGlAFwrrZzUC8UcYAHgwERYBGAxgB0IbAJ4AvIQEYATAGZOQA"\))
####  3.7.1.1. Documents[🔗](find/?domain=Verso.Genre.Manual.section&name=format-api "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.group "Permalink")inductive type
```


Std.Format : Type


Std.Format : Type


```

A representation of a set of strings, in which the placement of newlines and indentation differ.
Given a specific line width, specified in columns, the string that uses the fewest lines can be selected.
The pretty-printing algorithm is based on Wadler's paper [_A Prettier Printer_](https://homepages.inf.ed.ac.uk/wadler/papers/prettier/prettier.pdf).
#  Constructors

```
nil : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")
```

The empty format.

```
line : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")
```

A position where a newline may be inserted if the current group does not fit within the allotted column width.

```
align (force : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")
```

`[align](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.align")` tells the formatter to pad with spaces to the current indentation level, or else add a newline if we are already at or past the indent.
If `force` is true, then it will pad to the indent even if it is in a flattened group.
Example:

```
open Std Format in
#eval IO.println (nest 2 <| "." ++ align ++ "a" ++ line ++ "b")

```
`. a   b`

```
text : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")
```

A node containing a plain string.
If the string contains newlines, the formatter emits them and then indents to the current level.

```
nest (indent : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")) (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")
```

`[nest](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.nest") indent f` increases the current indentation level by `indent` while rendering `f`.
Example:
`[open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Std Format [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") def fmtList (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) : [Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format") :=   let f := [joinSep](Interacting-with-Lean/#Std___Format___joinSep "Documentation for Std.Format.joinSep") l  (", " ++ [Format.line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line"))   [group](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.group") ([nest](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.nest") 1 <| "[" ++ f ++ "]") `
This will be written all on one line, but if the text is too large, the formatter will put in linebreaks after the commas and indent later lines by 1.

```
append : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format") → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format") → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")
```

Concatenation of two `[Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")`s.

```
group :
  [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format") →
    (behavior :
        [optParam](Terms/Function-Application/#optParam "Documentation for optParam") [Std.Format.FlattenBehavior](Interacting-with-Lean/#Std___Format___FlattenBehavior___allOrNone "Documentation for Std.Format.FlattenBehavior")
          [Std.Format.FlattenBehavior.allOrNone](Interacting-with-Lean/#Std___Format___FlattenBehavior___allOrNone "Documentation for Std.Format.FlattenBehavior.allOrNone")) →
      [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")
```

Creates a new flattening group for the given inner `[Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")`.

```
tag : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format") → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")
```

Used for associating auxiliary information (e.g. `Expr`s) with `[Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")` objects.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.FlattenBehavior.allOrNone "Permalink")inductive type
```


Std.Format.FlattenBehavior : Type


Std.Format.FlattenBehavior : Type


```

Determines how groups should have linebreaks inserted when the text would overfill its remaining space.
  * `allOrNone` will make a linebreak on every `Format.line` in the group or none of them.
`[1,  2,  3]`
  * `fill` will only make linebreaks on as few `Format.line`s as possible:
`[1, 2,  3]`


#  Constructors

```
allOrNone : [Std.Format.FlattenBehavior](Interacting-with-Lean/#Std___Format___FlattenBehavior___allOrNone "Documentation for Std.Format.FlattenBehavior")
```

Either all `[Format.line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line")`s in the group will be newlines, or all of them will be spaces.

```
fill : [Std.Format.FlattenBehavior](Interacting-with-Lean/#Std___Format___FlattenBehavior___allOrNone "Documentation for Std.Format.FlattenBehavior")
```

As few `[Format.line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line")`s in the group as possible will be newlines.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.fill "Permalink")def
```


Std.Format.fill (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


Std.Format.fill (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) :
  [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


```

Creates a group in which as few `Format.line`s as possible are rendered as newlines.
This is an alias for `Format.group`, with `FlattenBehavior` set to `fill`.
####  3.7.1.2. Empty Documents[🔗](find/?domain=Verso.Genre.Manual.section&name=format-empty "Permalink")
The empty string does not have a single unique representative in `[Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")`. All of the following represent the empty string:
  * `[.nil](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.nil")`
  * `[.text](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.text") ""`
  * `.text "" ++ .nil`
  * `.nil ++ .text ""`


Use `[Std.Format.isEmpty](Interacting-with-Lean/#Std___Format___isEmpty "Documentation for Std.Format.isEmpty")` to check whether a document contains zero characters, and `[Std.Format.isNil](Interacting-with-Lean/#Std___Format___isNil "Documentation for Std.Format.isNil")` to specifically check whether it is the constructor `[Std.Format.nil](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.nil")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.isEmpty "Permalink")def
```


Std.Format.isEmpty : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.Format.isEmpty : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the given format contains no characters.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.isNil "Permalink")def
```


Std.Format.isNil : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.Format.isNil : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a `Format` is the constructor `Format.nil`.
This does not check whether the resulting rendered strings are always empty. To do that, use `Format.isEmpty`.
####  3.7.1.3. Sequences[🔗](find/?domain=Verso.Genre.Manual.section&name=format-join "Permalink")
The operators in this section are useful when there is some kind of repeated content, such as the elements of a list. This is typically done by including `[line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line")` in their separator parameters, using a [bracketing operator](Interacting-with-Lean/#format-brackets)
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.join "Permalink")def
```


Std.Format.join (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


Std.Format.join (xs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) :
  [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


```

Concatenates a list of `Format`s with `++`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.joinSep "Permalink")def
```


Std.Format.joinSep.{u} {α : Type u} [[Std.ToFormat](Interacting-with-Lean/#Std___ToFormat___mk "Documentation for Std.ToFormat") α] :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format") → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


Std.Format.joinSep.{u} {α : Type u}
  [[Std.ToFormat](Interacting-with-Lean/#Std___ToFormat___mk "Documentation for Std.ToFormat") α] :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format") → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


```

Intercalates the given list with the given `sep` format.
The list items are formatting using `ToFormat.format`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.prefixJoin "Permalink")def
```


Std.Format.prefixJoin.{u} {α : Type u} [[Std.ToFormat](Interacting-with-Lean/#Std___ToFormat___mk "Documentation for Std.ToFormat") α]
  (pre : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


Std.Format.prefixJoin.{u} {α : Type u}
  [[Std.ToFormat](Interacting-with-Lean/#Std___ToFormat___mk "Documentation for Std.ToFormat") α] (pre : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


```

Concatenates the given list after prepending `pre` to each element.
The list items are formatting using `ToFormat.format`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.joinSuffix "Permalink")def
```


Std.Format.joinSuffix.{u} {α : Type u} [[Std.ToFormat](Interacting-with-Lean/#Std___ToFormat___mk "Documentation for Std.ToFormat") α] :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format") → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


Std.Format.joinSuffix.{u} {α : Type u}
  [[Std.ToFormat](Interacting-with-Lean/#Std___ToFormat___mk "Documentation for Std.ToFormat") α] :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format") → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


```

Concatenates the given list after appending the given suffix to each element.
The list items are formatting using `ToFormat.format`.
####  3.7.1.4. Indentation[🔗](find/?domain=Verso.Genre.Manual.section&name=format-indent "Permalink")
These operators make it easier to achieve a consistent indentation style on top of `[Std.Format.nest](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.nest")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.nestD "Permalink")def
```


Std.Format.nestD (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


Std.Format.nestD (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) :
  [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


```

Increases the indentation level by the default amount.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.defIndent "Permalink")def
```


Std.Format.defIndent : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Std.Format.defIndent : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The default indentation level, which is two spaces.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.indentD "Permalink")def
```


Std.Format.indentD (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


Std.Format.indentD (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) :
  [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


```

Insert a newline and then `f`, all nested by the default indent amount.
####  3.7.1.5. Brackets and Parentheses[🔗](find/?domain=Verso.Genre.Manual.section&name=format-brackets "Permalink")
These operators make it easier to achieve a consistent parenthesization style.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.bracket "Permalink")def
```


Std.Format.bracket (l : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) (r : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


Std.Format.bracket (l : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) (r : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


```

Creates a format `l ++ f ++ r` with a flattening group, nesting the contents by the length of `l`.
The group's `FlattenBehavior` is `allOrNone`; for `fill` use `[Std.Format.bracketFill](Interacting-with-Lean/#Std___Format___bracketFill "Documentation for Std.Format.bracketFill")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.sbracket "Permalink")def
```


Std.Format.sbracket (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


Std.Format.sbracket (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) :
  [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


```

Creates the format `"[" ++ f ++ "]"` with a flattening group, nesting by one space.
`sbracket` is short for “square bracket”.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.paren "Permalink")def
```


Std.Format.paren (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


Std.Format.paren (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) :
  [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


```

Creates the format `"(" ++ f ++ ")"` with a flattening group, nesting by one space.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.bracketFill "Permalink")def
```


Std.Format.bracketFill (l : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) (r : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


Std.Format.bracketFill (l : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) (r : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


```

Creates a format `l ++ f ++ r` with a flattening group, nesting the contents by the length of `l`.
The group's `FlattenBehavior` is `fill`; for `allOrNone` use `[Std.Format.bracketFill](Interacting-with-Lean/#Std___Format___bracketFill "Documentation for Std.Format.bracketFill")`.
####  3.7.1.6. Rendering[🔗](find/?domain=Verso.Genre.Manual.section&name=format-render "Permalink")
The `ToString [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")` instance invokes `[Std.Format.pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty")` with its default arguments.
There are two ways to render a document:
  * Use `[pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty")` to construct a `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`. The entire string must be constructed up front before any can be sent to a user.
  * Use `[prettyM](Interacting-with-Lean/#Std___Format___prettyM "Documentation for Std.Format.prettyM")` to incrementally emit the `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`, using effects in some `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad")`. As soon as each line is rendered, it is emitted. This is suitable for streaming output.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.pretty "Permalink")def
```


Std.Format.pretty (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) (width : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := [Std.Format.defWidth](Interacting-with-Lean/#Std___Format___defWidth "Documentation for Std.Format.defWidth"))
  (indent column : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


Std.Format.pretty (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format"))
  (width : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := [Std.Format.defWidth](Interacting-with-Lean/#Std___Format___defWidth "Documentation for Std.Format.defWidth"))
  (indent column : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Renders a `Format` to a string.
  * `width`: the total width
  * `indent`: the initial indentation to use for wrapped lines (subsequent wrapping may increase the indentation)
  * `column`: begin the first line wrap `column` characters earlier than usual (this is useful when the output String will be printed starting at `column`)


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.defWidth "Permalink")def
```


Std.Format.defWidth : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Std.Format.defWidth : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The default width of the targeted output, which is 120 columns.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.prettyM "Permalink")def
```


Std.Format.prettyM {m : Type → Type} (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) (w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (indent : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[Std.Format.MonadPrettyFormat](Interacting-with-Lean/#Std___Format___MonadPrettyFormat___mk "Documentation for Std.Format.MonadPrettyFormat") m] :
  m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


Std.Format.prettyM {m : Type → Type}
  (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) (w : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (indent : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[Std.Format.MonadPrettyFormat](Interacting-with-Lean/#Std___Format___MonadPrettyFormat___mk "Documentation for Std.Format.MonadPrettyFormat") m] :
  m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Renders a `Format` using effects in the monad `m`, using the methods of `MonadPrettyFormat`.
Each line is emitted as soon as it is rendered, rather than waiting for the entire document to be rendered.
  * `w`: the total width
  * `indent`: the initial indentation to use for wrapped lines (subsequent wrapping may increase the indentation)


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.Format.MonadPrettyFormat.currColumn "Permalink")type class
```


Std.Format.MonadPrettyFormat (m : Type → Type) : Type


Std.Format.MonadPrettyFormat
  (m : Type → Type) : Type


```

A monad that can be used to incrementally render `Format` objects.
#  Instance Constructor

```
[Std.Format.MonadPrettyFormat.mk](Interacting-with-Lean/#Std___Format___MonadPrettyFormat___mk "Documentation for Std.Format.MonadPrettyFormat.mk")
```

#  Methods

```
pushOutput : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")
```

Emits the string `s`.

```
pushNewline : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")
```

Emits a newline followed by `indent` columns of indentation.

```
currColumn : m [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

Gets the current column at which the next string will be emitted.

```
startTag : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")
```

Starts a region tagged with `tag`.

```
endTags : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → m [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")
```

Exits the scope of `count` opened tags.
####  3.7.1.7. The `ToFormat` Class[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Interacting-with-Lean--Formatted-Output--Format--The--ToFormat--Class "Permalink")
The `[Std.ToFormat](Interacting-with-Lean/#Std___ToFormat___mk "Documentation for Std.ToFormat")` class is used to provide a standard means to format a value, with no expectation that this formatting be valid Lean syntax. These instances are used in error messages and by some of the [sequence concatenation operators](Interacting-with-Lean/#format-join).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ToFormat.mk "Permalink")type class
```


Std.ToFormat.{u} (α : Type u) : Type u


Std.ToFormat.{u} (α : Type u) : Type u


```

Specifies a “user-facing” way to convert from the type `α` to a `Format` object. There is no expectation that the resulting string is valid code.
The `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` class is similar, but the expectation is that instances produce valid Lean code.
#  Instance Constructor

```
[Std.ToFormat.mk](Interacting-with-Lean/#Std___ToFormat___mk "Documentation for Std.ToFormat.mk").{u}
```

#  Methods

```
format : α → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")
```

Converts a value to a `Format` object, with no expectation that the resulting string is valid code.
###  3.7.2. `Repr`[🔗](find/?domain=Verso.Genre.Manual.section&name=repr "Permalink")
A `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instance describes how to represent a value as a `[Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")`. Because they should emit valid Lean syntax, these instances need to take [precedence](Notations-and-Macros/Custom-Operators/#--tech-term-precedence) into account. Inserting the maximal number of parentheses would work, but it makes it more difficult for humans to read the resulting output.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Repr.mk "Permalink")type class
```


Repr.{u} (α : Type u) : Type u


Repr.{u} (α : Type u) : Type u


```

The standard way of turning values of some type into `Format`.
When rendered this `Format` should be as close as possible to something that can be parsed as the input value.
#  Instance Constructor

```
[Repr.mk](Interacting-with-Lean/#Repr___mk "Documentation for Repr.mk").{u}
```

#  Methods

```
reprPrec : α → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")
```

Turn a value of type `α` into a `Format` at a given precedence. The precedence value can be used to avoid parentheses if they are not necessary.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=repr "Permalink")def
```


repr.{u_1} {α : Type u_1} [[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") α] (a : α) : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


repr.{u_1} {α : Type u_1} [[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") α]
  (a : α) : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


```

Turns `a` into a `Format` using its `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instance. The precedence level is initially set to 0.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=reprStr "Permalink")def
```


reprStr.{u_1} {α : Type u_1} [[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") α] (a : α) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


reprStr.{u_1} {α : Type u_1} [[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") α]
  (a : α) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Turns `a` into a `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` using its `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instance, rendering the `Format` at the default width of 120 columns.
The precedence level is initially set to 0.
Maximal Parentheses
The type `[NatOrInt](Interacting-with-Lean/#NatOrInt-_LPAR_in-Maximal-Parentheses_RPAR_ "Definition of example")` can contain a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` or an `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`:
`inductive NatOrInt where   | nat : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [NatOrInt](Interacting-with-Lean/#NatOrInt-_LPAR_in-Maximal-Parentheses_RPAR_ "Definition of example")   | int : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [NatOrInt](Interacting-with-Lean/#NatOrInt-_LPAR_in-Maximal-Parentheses_RPAR_ "Definition of example") `
This `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") [NatOrInt](Interacting-with-Lean/#NatOrInt-_LPAR_in-Maximal-Parentheses_RPAR_ "Definition of example")` instance ensures that the output is valid Lean syntax by inserting many parentheses:
`instance : [Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") [NatOrInt](Interacting-with-Lean/#NatOrInt-_LPAR_in-Maximal-Parentheses_RPAR_ "Definition of example") where   [reprPrec](Interacting-with-Lean/#Repr___mk "Documentation for Repr.reprPrec") x _ :=     [.nestD](Interacting-with-Lean/#Std___Format___nestD "Documentation for Std.Format.nestD") <| [.group](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.group") <|       [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") x [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")       | [.nat](Interacting-with-Lean/#NatOrInt___nat-_LPAR_in-Maximal-Parentheses_RPAR_ "Definition of example") n =>           [.text](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.text") "(" ++ "NatOrInt.nat" ++ [.line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line") ++ "(" ++ [repr](Interacting-with-Lean/#repr-next "Documentation for repr") n ++ "))"       | [.int](Interacting-with-Lean/#NatOrInt___int-_LPAR_in-Maximal-Parentheses_RPAR_ "Definition of example") i =>           [.text](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.text") "(" ++ "NatOrInt.int" ++ [.line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line") ++ "(" ++ [repr](Interacting-with-Lean/#repr-next "Documentation for repr") i ++ "))" `
Whether it contains a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, a non-negative `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`, or a negative `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`, the result can be parsed:
`[open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") NatOrInt [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") `(NatOrInt.nat (3)) (NatOrInt.int (5)) (NatOrInt.int (-5)) `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") <| [repr](Interacting-with-Lean/#repr-next "Documentation for repr") <| [nat](Interacting-with-Lean/#NatOrInt___nat-_LPAR_in-Maximal-Parentheses_RPAR_ "Definition of example") 3 [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") <| [repr](Interacting-with-Lean/#repr-next "Documentation for repr") <| [int](Interacting-with-Lean/#NatOrInt___int-_LPAR_in-Maximal-Parentheses_RPAR_ "Definition of example") 5 [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") <| [repr](Interacting-with-Lean/#repr-next "Documentation for repr") <| [int](Interacting-with-Lean/#NatOrInt___int-_LPAR_in-Maximal-Parentheses_RPAR_ "Definition of example") (-5) `
```
(NatOrInt.nat (3))
(NatOrInt.int (5))
(NatOrInt.int (-5))

```

However, `([NatOrInt.nat](Interacting-with-Lean/#NatOrInt___nat-_LPAR_in-Maximal-Parentheses_RPAR_ "Definition of example") (3))` is not particularly idiomatic Lean, and redundant parentheses can make it difficult to read large expressions.
[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABAOQIYwPICcCSIMyA7gBaI6IBQyyAPsiJsgFxrOBJhO9voTfclBE2BIlww9RVKqADOMdCCgo2AJUQAHHN1yiS5Sv0paACpSjIAHsgD6rALz9aAOhCJ5AEWQAeBs4DmOAD2EBo+dE60yAC2mFCkViTAMKSRtH5MRCDI9gB8aVEuMIiWRABEABRlyADUNchlErqErpjVdcjOADagKB2V7fXG2tn9AJRjZQV+QoI5+YWLncWlDVW19Y2YzTDOQoOdPW4bawfDc+OT0kEaiNlNvESgVADEiPDoXchgQfx4WM4tEIutlfMhzmDMsgAMx/AFAwgg8LgzTaMGzACscMBOGBoIYEIYswqAFoMWMgA"\))
The method `[Repr.reprPrec](Interacting-with-Lean/#Repr___mk "Documentation for Repr.reprPrec")` has the following signature:
`[Repr.reprPrec](Interacting-with-Lean/#Repr___mk "Documentation for Repr.reprPrec").{u} {α : Type u} [[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") α] : α → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")`
The first explicit parameter is the value to be represented, while the second is the [precedence](Notations-and-Macros/Custom-Operators/#--tech-term-precedence) of the context in which it occurs. This precedence can be used to decide whether to insert parentheses: if the precedence of the syntax being produced by the instance is greater than that of its context, parentheses are necessary.
####  3.7.2.1. How To Write a `Repr` Instance[🔗](find/?domain=Verso.Genre.Manual.section&name=repr-instance-howto "Permalink")
Lean can produce an appropriate `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instance for most types automatically using [instance deriving](Type-Classes/Deriving-Instances/#deriving-instances). In some cases, however, it's necessary to write an instance by hand:
When writing a custom `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instance, please follow these conventions: 

Precedence
    
Check precedence, adding parentheses as needed, and pass the correct precedence to the `[reprPrec](Interacting-with-Lean/#Repr___mk "Documentation for Repr.reprPrec")` instances of embedded data. Each instance is responsible for surrounding itself in parentheses if needed; instances should generally not parenthesize recursive calls to `[reprPrec](Interacting-with-Lean/#Repr___mk "Documentation for Repr.reprPrec")`.
Function application has the maximum precedence, `max_prec`. The helpers `[Repr.addAppParen](Interacting-with-Lean/#Repr___addAppParen "Documentation for Repr.addAppParen")` and `[reprArg](Interacting-with-Lean/#reprArg "Documentation for reprArg")` respectively insert parentheses around applications when needed and pass the appropriate precedence to function arguments. 

Fully-Qualified Names
    
A `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instance does have access to the set of open namespaces in a given position. All names of constants in the environment should be fully qualified to remove ambiguity. 

Default Nesting
    
Nested data should be indented using `[nestD](Interacting-with-Lean/#Std___Format___nestD "Documentation for Std.Format.nestD")` to ensure consistent indentation across instances. 

Grouping and Line Breaks
    
The output of every `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instance that includes line breaks should be surrounded in a `[group](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.group")`. Furthermore, if the resulting code contains notional expressions that are nested, a `[group](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.group")` should be inserted around each nested level. Line breaks should usually be inserted in the following positions:
  * Between a constructor and each of its arguments
  * After `:=`
  * After `,`
  * Between the opening and closing braces of [structure instance](The-Type-System/Inductive-Types/#--tech-term-structure-instance) notation and its contents
  * After, but not before, an infix operator



Parentheses and Brackets
    
Parentheses and brackets should be inserted using `[Std.Format.bracket](Interacting-with-Lean/#Std___Format___bracket "Documentation for Std.Format.bracket")` or its specializations `[Std.Format.paren](Interacting-with-Lean/#Std___Format___paren "Documentation for Std.Format.paren")` for parentheses and `[Std.Format.sbracket](Interacting-with-Lean/#Std___Format___sbracket "Documentation for Std.Format.sbracket")` for square brackets. These operators align the contents of the parenthesized or bracketed expression in the same way that Lean's do. Trailing parentheses and brackets should not be placed on their own line, but rather stay with their contents.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Repr.addAppParen "Permalink")def
```


Repr.addAppParen (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")) (prec : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


Repr.addAppParen (f : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format"))
  (prec : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


```

Adds parentheses to `f` if the precedence `prec` from the context is at least that of function application.
Together with `[reprArg](Interacting-with-Lean/#reprArg "Documentation for reprArg")`, this can be used to correctly parenthesize function application syntax.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=reprArg "Permalink")def
```


reprArg.{u_1} {α : Type u_1} [[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") α] (a : α) : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


reprArg.{u_1} {α : Type u_1} [[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") α]
  (a : α) : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


```

Turns `a` into a `Format` using its `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instance, with the precedence level set to that of function application.
Together with `[Repr.addAppParen](Interacting-with-Lean/#Repr___addAppParen "Documentation for Repr.addAppParen")`, this can be used to correctly parenthesize function application syntax.
Inductive Types with Constructors
The inductive type `[N.NatOrInt](Interacting-with-Lean/#N___NatOrInt-_LPAR_in-Inductive-Types-with-Constructors_RPAR_ "Definition of example")` can contain a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` or an `[Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")`:
`[namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") N  inductive NatOrInt where   | nat : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [NatOrInt](Interacting-with-Lean/#N___NatOrInt-_LPAR_in-Inductive-Types-with-Constructors_RPAR_ "Definition of example")   | int : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int") → [NatOrInt](Interacting-with-Lean/#N___NatOrInt-_LPAR_in-Inductive-Types-with-Constructors_RPAR_ "Definition of example")  `
The `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") [NatOrInt](Interacting-with-Lean/#N___NatOrInt-_LPAR_in-Inductive-Types-with-Constructors_RPAR_ "Definition of example")` instance adheres to the conventions:
  * The right-hand side is a function application, so it uses `[Repr.addAppParen](Interacting-with-Lean/#Repr___addAppParen "Documentation for Repr.addAppParen")` to add parentheses if necessary.
  * Parentheses are wrapped around the entire body with no additional `[line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line")`s.
  * The entire function application is grouped, and it is nested the default amount.
  * The function is separated from its parameters by a use of `[line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line")`; this newline will usually be a space because the `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` and `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` instances are unlikely to produce long output.
  * Recursive calls to `[reprPrec](Interacting-with-Lean/#Repr___mk "Documentation for Repr.reprPrec")` pass `max_prec` because they are in function parameter positions, and function application has the highest precedence.

`instance : [Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") [NatOrInt](Interacting-with-Lean/#N___NatOrInt-_LPAR_in-Inductive-Types-with-Constructors_RPAR_ "Definition of example") where   [reprPrec](Interacting-with-Lean/#Repr___mk "Documentation for Repr.reprPrec")     | [.nat](Interacting-with-Lean/#N___NatOrInt___nat-_LPAR_in-Inductive-Types-with-Constructors_RPAR_ "Definition of example") n =>       [Repr.addAppParen](Interacting-with-Lean/#Repr___addAppParen "Documentation for Repr.addAppParen") <|         [.group](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.group") <| [.nestD](Interacting-with-Lean/#Std___Format___nestD "Documentation for Std.Format.nestD") <|           "N.NatOrInt.nat" ++ [.line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line") ++ [reprPrec](Interacting-with-Lean/#Repr___mk "Documentation for Repr.reprPrec") n max_prec     | [.int](Interacting-with-Lean/#N___NatOrInt___int-_LPAR_in-Inductive-Types-with-Constructors_RPAR_ "Definition of example") i =>       [Repr.addAppParen](Interacting-with-Lean/#Repr___addAppParen "Documentation for Repr.addAppParen") <|         [.group](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.group") <| [.nestD](Interacting-with-Lean/#Std___Format___nestD "Documentation for Std.Format.nestD") <|           "N.NatOrInt.int" ++ [.line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line") ++ [reprPrec](Interacting-with-Lean/#Repr___mk "Documentation for Repr.reprPrec") i max_prec ```N.NatOrInt.nat 5 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([repr](Interacting-with-Lean/#repr-next "Documentation for repr") ([NatOrInt.nat](Interacting-with-Lean/#N___NatOrInt___nat-_LPAR_in-Inductive-Types-with-Constructors_RPAR_ "Definition of example") 5)) `
```
N.NatOrInt.nat 5

```
``N.NatOrInt.int 5 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([repr](Interacting-with-Lean/#repr-next "Documentation for repr") ([NatOrInt.int](Interacting-with-Lean/#N___NatOrInt___int-_LPAR_in-Inductive-Types-with-Constructors_RPAR_ "Definition of example") 5)) `
```
N.NatOrInt.int 5

```
``N.NatOrInt.int (-5) `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([repr](Interacting-with-Lean/#repr-next "Documentation for repr") ([NatOrInt.int](Interacting-with-Lean/#N___NatOrInt___int-_LPAR_in-Inductive-Types-with-Constructors_RPAR_ "Definition of example") (-5))) `
```
N.NatOrInt.int (-5)

```
``some (N.NatOrInt.int (-5)) `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([repr](Interacting-with-Lean/#repr-next "Documentation for repr") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ([NatOrInt.int](Interacting-with-Lean/#N___NatOrInt___int-_LPAR_in-Inductive-Types-with-Constructors_RPAR_ "Definition of example") (-5)))) `
```
some (N.NatOrInt.int (-5))

```
``[N.NatOrInt.nat 0,  N.NatOrInt.nat 1,  N.NatOrInt.nat 2,  N.NatOrInt.nat 3,  N.NatOrInt.nat 4,  N.NatOrInt.nat 5,  N.NatOrInt.nat 6,  N.NatOrInt.nat 7,  N.NatOrInt.nat 8,  N.NatOrInt.nat 9] `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([repr](Interacting-with-Lean/#repr-next "Documentation for repr") <| ([List.range](Basic-Types/Linked-Lists/#List___range "Documentation for List.range") 10).[map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map") ([NatOrInt.nat](Interacting-with-Lean/#N___NatOrInt___nat-_LPAR_in-Inductive-Types-with-Constructors_RPAR_ "Definition of example"))) `
```
[N.NatOrInt.nat 0,
 N.NatOrInt.nat 1,
 N.NatOrInt.nat 2,
 N.NatOrInt.nat 3,
 N.NatOrInt.nat 4,
 N.NatOrInt.nat 5,
 N.NatOrInt.nat 6,
 N.NatOrInt.nat 7,
 N.NatOrInt.nat 8,
 N.NatOrInt.nat 9]

```
``[N.NatOrInt.nat    0,  N.NatOrInt.nat    1,  N.NatOrInt.nat    2,  N.NatOrInt.nat    3,  N.NatOrInt.nat    4,  N.NatOrInt.nat    5,  N.NatOrInt.nat    6,  N.NatOrInt.nat    7,  N.NatOrInt.nat    8,  N.NatOrInt.nat    9] `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") <| [Std.Format.pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") (width := 3) <| [repr](Interacting-with-Lean/#repr-next "Documentation for repr") <| ([List.range](Basic-Types/Linked-Lists/#List___range "Documentation for List.range") 10).[map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map") [NatOrInt.nat](Interacting-with-Lean/#N___NatOrInt___nat-_LPAR_in-Inductive-Types-with-Constructors_RPAR_ "Definition of example") `
```
[N.NatOrInt.nat
   0,
 N.NatOrInt.nat
   1,
 N.NatOrInt.nat
   2,
 N.NatOrInt.nat
   3,
 N.NatOrInt.nat
   4,
 N.NatOrInt.nat
   5,
 N.NatOrInt.nat
   6,
 N.NatOrInt.nat
   7,
 N.NatOrInt.nat
   8,
 N.NatOrInt.nat
   9]

```

[Live ↪](javascript:openLiveLink\("HYQwtgpgzgDiDGEAEA5AUGglsAJgV3gBdMA3ZFEQgeQCcBJYQpAdwAsIaI0kkAfJUEwBcqSkkBJhKOr1G3PkmzCkDJpIrSVGbFEIhgiJCIBKEGDSm0VLdpzmczABU7w5PfgDpBApAF4AfK48SCZm7iA4OACCMDAOIJzASAA8vIFBSO4A5jQA9ngwyR7A0IQAIoVp6UgARCju6paMnpTVSADUbRkANtjIHUj2NE4Q8N5gIAAeAPpmI4Eeigq+AVXBpjRhEdGx8RCJKZU8Wbn5hRnFOuUHq+m19ZSNhO6Krf3uPcXtnYPDo5hI42msxcaAAxBASCAusoqO4zIouokABSDJBIhoyJ5eACsAEpcRhwZDoXRYfDGIi0aj0Q9Mc9GEg8QSwRCoTC4TQEcjqRiVPSmEiALRM5lEtmkjlcqnrNFQHKQNG8pqLIUi0WsklkzkU7kylJogAymB07hoekyyAAjAAGXHucYFGkaJqCfGEjXs8mESnXJAAZUIOHcADEcjRxk9ZoRCABPNHMTA4QisQw+JAAZlxFXSqP1SKNJrNwAtSBtdodFjpgiAA"\))
Infix Syntax
This example demonstrates the use of precedences to encode a left-associative pretty printer. The type `[AddExpr](Interacting-with-Lean/#AddExpr-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example")` represents expressions with constants and addition:
`inductive AddExpr where   | nat : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [AddExpr](Interacting-with-Lean/#AddExpr-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example")   | add : [AddExpr](Interacting-with-Lean/#AddExpr-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example") → [AddExpr](Interacting-with-Lean/#AddExpr-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example") → [AddExpr](Interacting-with-Lean/#AddExpr-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example") `
The `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat")` and `[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add")` instances provide a more convenient syntax for `[AddExpr](Interacting-with-Lean/#AddExpr-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example")`:
`instance : [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") [AddExpr](Interacting-with-Lean/#AddExpr-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example") n where   [ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") := [.nat](Interacting-with-Lean/#AddExpr___nat-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example") n  instance : [Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") [AddExpr](Interacting-with-Lean/#AddExpr-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example") where   [add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add.add") := [.add](Interacting-with-Lean/#AddExpr___add-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example") `
The `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") [AddExpr](Interacting-with-Lean/#AddExpr-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example")` instance should insert only the necessary parentheses. Lean's addition operator is left-associative, with precedence 65, so the recursive call to the left uses precedence 64 and the operator itself is parenthesized if the current context has precedence greater than or equal to 65:
`protected def AddExpr.reprPrec : [AddExpr](Interacting-with-Lean/#AddExpr-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")   | [.nat](Interacting-with-Lean/#AddExpr___nat-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example") n, p  =>     [Repr.reprPrec](Interacting-with-Lean/#Repr___mk "Documentation for Repr.reprPrec") n p   | [.add](Interacting-with-Lean/#AddExpr___add-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example") e1 e2, p =>     let out : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format") :=       [.nestD](Interacting-with-Lean/#Std___Format___nestD "Documentation for Std.Format.nestD") <| [.group](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.group") <|         [AddExpr.reprPrec](Interacting-with-Lean/#AddExpr___reprPrec-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example") e1 64 ++ " " ++ "+" ++ [.line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line") ++         [AddExpr.reprPrec](Interacting-with-Lean/#AddExpr___reprPrec-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example") e2 65     [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") p ≥ 65 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") out.[paren](Interacting-with-Lean/#Std___Format___paren "Documentation for Std.Format.paren") [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") out  instance : [Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") [AddExpr](Interacting-with-Lean/#AddExpr-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example") := ⟨[AddExpr.reprPrec](Interacting-with-Lean/#AddExpr___reprPrec-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example")⟩ `
Regardless of the input's parenthesization, this instance inserts only the necessary parentheses:
``2 + 3 + 4 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([repr](Interacting-with-Lean/#repr-next "Documentation for repr") (((2 + 3) + 4) : [AddExpr](Interacting-with-Lean/#AddExpr-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example"))) `
```
2 + 3 + 4

```
``2 + 3 + 4 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([repr](Interacting-with-Lean/#repr-next "Documentation for repr") ((2 + 3 + 4) : [AddExpr](Interacting-with-Lean/#AddExpr-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example"))) `
```
2 + 3 + 4

```
``2 + (3 + 4) `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([repr](Interacting-with-Lean/#repr-next "Documentation for repr") ((2 + (3 + 4)) : [AddExpr](Interacting-with-Lean/#AddExpr-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example"))) `
```
2 + (3 + 4)

```
``[2 + (3 + 4), 2 + 3 + 4] `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") ([repr](Interacting-with-Lean/#repr-next "Documentation for repr") ([2 + (3 + 4), (2 + 3) + 4] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [AddExpr](Interacting-with-Lean/#AddExpr-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example"))) `
```
[2 + (3 + 4), 2 + 3 + 4]

```

The uses of `[group](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.group")`, `[nestD](Interacting-with-Lean/#Std___Format___nestD "Documentation for Std.Format.nestD")`, and `[line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line")` in the implementation lead to the expected newlines and indentation in a narrow context:
``[2 +    (3 +       4),  2 +      3 +    4] `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") ([2 + (3 + 4), (2 + 3) + 4] : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [AddExpr](Interacting-with-Lean/#AddExpr-_LPAR_in-Infix-Syntax_RPAR_ "Definition of example")) |> [repr](Interacting-with-Lean/#repr-next "Documentation for repr") |>.[pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") (width := 0) |> [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") `
```
[2 +
   (3 +
      4),
 2 +
     3 +
   4]

```

[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABAQTGAogDwA4CdkB3AC0X0QChlkAfZEAQxmQC5kA5Z5QJMI0McBanWSMMbfljyE+6KQV6TB+SpVABnGIxBQU7APIAzLiznKGxMhWEB7Y91YBeZADomLEKo1adeyUulLcioaMTA2Zxcw1QIbGERYRHCwREMAghcKAgAFCigJM0C+E0UAZRgwFwAxG3wAW2ZhejduEAAaZFwaRwA+YRoAJUQMrPxchItcJtcw5EQARjmAJg6u3v7kABtEFhsIFnZyypr6h0cNmjdETQARZAAeZoBzfD2ux4uadPxM4bG8uaLABsABZkABqcHIABEMIhUOh4NhkNcm1AKEhnxohRGf3G+UQS2QQIArBtgGkuoBTImJJOQMDIIGQexgLlwjAoTMQm3UKBZXhAmm0ugkQwUOMITmQgAvyCW/HJ5QCX5KoAMSIeCMTbIACS+jZ+FAME2TIAFKNkCbLUSoQBmACUEOQIId7AldrtqvVmp1eoIhuNFvNVsdNsdzoKAmk7s9Gq1uv1/tNQZN1otoahzpd32jlDVsZ9CZARqTfwtAG1Uyb0067R0UyGHRmALoSAAywE02Y9ua9WpNFcdVbDtYtqftYZb7HbnbdTR6yFGc/1OxgAE8LURgGAGRFkAAGD00Wjz+N+ovGoA"\))
####  3.7.2.2. Atomic Types[🔗](find/?domain=Verso.Genre.Manual.section&name=ReprAtom "Permalink")
When the elements of a list are sufficiently small, it can be both difficult to read and wasteful of space to render the list with one element per line. To improve readability, `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List")` has two `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instances: one that uses `[Std.Format.bracket](Interacting-with-Lean/#Std___Format___bracket "Documentation for Std.Format.bracket")` for its contents, and one that uses `[Std.Format.bracketFill](Interacting-with-Lean/#Std___Format___bracketFill "Documentation for Std.Format.bracketFill")`. The latter is defined after the former and is thus selected when possible; however, it requires an instance of the empty type class `[ReprAtom](Interacting-with-Lean/#ReprAtom___mk "Documentation for ReprAtom")`.
If the `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` instance for a type never generates spaces or newlines, then it should have a `[ReprAtom](Interacting-with-Lean/#ReprAtom___mk "Documentation for ReprAtom")` instance. Lean has `[ReprAtom](Interacting-with-Lean/#ReprAtom___mk "Documentation for ReprAtom")` instances for types such as `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`, `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")`, `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, `[Char](Basic-Types/Characters/#Char___mk "Documentation for Char")`, and `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ReprAtom "Permalink")type class
```


ReprAtom.{u} (α : Type u) : Type


ReprAtom.{u} (α : Type u) : Type


```

Auxiliary class for marking types that should be considered atomic by `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")` methods. We use it at `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") ([List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)` to decide whether `bracketFill` should be used or not.
#  Instance Constructor

```
[ReprAtom.mk](Interacting-with-Lean/#ReprAtom___mk "Documentation for ReprAtom.mk").{u}
```

Atomic Types and `Repr`
All constructors of the inductive type `[ABC](Interacting-with-Lean/#ABC-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example")` are without parameters:
`inductive ABC where   | a   | b   | c deriving [Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") `
The derived `[Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr") [ABC](Interacting-with-Lean/#ABC-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example")` instance is used to display lists:
`def abc : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [ABC](Interacting-with-Lean/#ABC-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example") := [[.a](Interacting-with-Lean/#ABC___a-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example"), [.b](Interacting-with-Lean/#ABC___b-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example"), [.c](Interacting-with-Lean/#ABC___c-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example")]  def abcs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [ABC](Interacting-with-Lean/#ABC-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example") := [abc](Interacting-with-Lean/#abc-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example") ++ [abc](Interacting-with-Lean/#abc-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example") ++ [abc](Interacting-with-Lean/#abc-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example")  `[ABC.a,  ABC.b,  ABC.c,  ABC.a,  ABC.b,  ABC.c,  ABC.a,  ABC.b,  ABC.c] `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") (([repr](Interacting-with-Lean/#repr-next "Documentation for repr") [abcs](Interacting-with-Lean/#abcs-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example")).[pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") (width := 14)) `
Because of the narrow width, line breaks are inserted:

```
[ABC.a,
 ABC.b,
 ABC.c,
 ABC.a,
 ABC.b,
 ABC.c,
 ABC.a,
 ABC.b,
 ABC.c]

```

However, converting the list to a `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` leads to a differently-formatted result.
`def ABC.toNat : [ABC](Interacting-with-Lean/#ABC-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   | [.a](Interacting-with-Lean/#ABC___a-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example") => 0   | [.b](Interacting-with-Lean/#ABC___b-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example") => 1   | [.c](Interacting-with-Lean/#ABC___c-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example") => 2  `[0, 1, 2, 0,  1, 2, 0, 1,  2]`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.print](IO/Console-Output/#IO___print "Documentation for IO.print") (([repr](Interacting-with-Lean/#repr-next "Documentation for repr") ([abcs](Interacting-with-Lean/#abcs-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example").[map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map") [ABC.toNat](Interacting-with-Lean/#ABC___toNat-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example"))).[pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") (width := 14)) `
There are far fewer line breaks:

```
[0, 1, 2, 0,
 1, 2, 0, 1,
 2]
```

This is because of the existence of a `[ReprAtom](Interacting-with-Lean/#ReprAtom___mk "Documentation for ReprAtom") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` instance. Adding one for `[ABC](Interacting-with-Lean/#ABC-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example")` leads to similar behavior:
`instance : [ReprAtom](Interacting-with-Lean/#ReprAtom___mk "Documentation for ReprAtom") [ABC](Interacting-with-Lean/#ABC-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example") := ⟨⟩  `[ABC.a, ABC.b,  ABC.c, ABC.a,  ABC.b, ABC.c,  ABC.a, ABC.b,  ABC.c] `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") (([repr](Interacting-with-Lean/#repr-next "Documentation for repr") [abcs](Interacting-with-Lean/#abcs-_LPAR_in-Atomic-Types-and--Repr_RPAR_ "Definition of example")).[pretty](Interacting-with-Lean/#Std___Format___pretty "Documentation for Std.Format.pretty") (width := 14)) `
```
[ABC.a, ABC.b,
 ABC.c, ABC.a,
 ABC.b, ABC.c,
 ABC.a, ABC.b,
 ABC.c]

```

[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABAQQEIGFkHcAWiATogFDLIA+yAhmZcgEZ1VQlhEKgDmyASogAdCJNogBmNBlGQAuZABlgAZxhossgLzIA2gDpqAGmS6GR3VAC6I9hOpSlshctUZsMrXekBqL5O+/PEQBiRHhqABtkAEkAeV0hUBhwkGQAClTiIT8lAEp44hgYAE80nGAwGDxNZABGABYcnJFQFWoQKBQ5fiFUGAB7AFs1Ny1AC/JAS/Jg0IjouISQJJT0zMJsvKFEQpLUsoqq91qGnKA"\))
[←2. Elaboration and Compilation](Elaboration-and-Compilation/#The-Lean-Language-Reference--Elaboration-and-Compilation "2. Elaboration and Compilation")[4. The Type System→](The-Type-System/#type-system "4. The Type System")

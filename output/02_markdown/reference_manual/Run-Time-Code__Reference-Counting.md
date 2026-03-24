[←12.1. Boxing](Run-Time-Code/Boxing/#boxing "12.1. Boxing")[12.3. Multi-Threaded Execution→](Run-Time-Code/Multi-Threaded-Execution/#The-Lean-Language-Reference--Run-Time-Code--Multi-Threaded-Execution "12.3. Multi-Threaded Execution")
#  12.2. Reference Counting[🔗](find/?domain=Verso.Genre.Manual.section&name=reference-counting "Permalink")
Lean uses _reference counting_ for memory management. Each allocated object maintains a count of how many other objects refer to it. When a new reference is added, the count is incremented, and when a reference is dropped, the count is decremented. When a reference count reaches zero, the object is no longer reachable and can play no part in the further execution of the program. It is deallocated and all of its references to other objects are dropped, which may trigger further deallocations.
Reference counting provides a number of benefits: 

Reuse of Memory
    
If an object's reference count drops to zero just as another of the same size is to be allocated, then the original object's memory can be safely reused for the new object. As a result, many common data-structure traversals (such as `[List.map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map")`) do not need to allocate memory when there is exactly one reference to the data structure to be traversed. 

Opportunistic In-Place Updates
    
Primitive types, such as [strings](Basic-Types/Strings/#String) and [arrays](Basic-Types/Arrays/#Array), may provide operations that copy shared data but modify unshared data in-place. As long as they hold the only reference to the value being modified, many operations on these primitive types will modify it rather than copy it. This can lead to substantial performance benefits. Carefully-written `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")` code avoids the performance overhead of immutable data structures while maintaining the ease of reasoning provided by pure functions. 

Predictability
    
Reference counts are decremented at predictable times. As a result, reference-counted objects can be used to manage other resources, such as file handles. In Lean, a `[Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")` does not need to be explicitly closed because it is closed immediately when it is no longer accessible. 

Simpler FFI
    
Objects managed with reference counting don't need to be relocated as part of reclaiming unused memory. This greatly simplifies interaction with code written in other languages, such as C.
The traditional drawbacks of reference counting include the performance overhead due to updating reference counts along with the inability to recognize and deallocate cyclic data. The former drawback is minimized by an analysis based on _borrowing_ that allows many reference count updates to be elided. Nevertheless, multi-threaded code requires that reference count updates are synchronized between threads, which also imposes a substantial overhead. To reduce this overhead, Lean values are partitioned into those which are reachable from multiple threads and those which are not. Single-threaded reference counts can be updated much faster than multi-threaded reference counts, and many values are accessed only on a single thread. Together, these techniques greatly reduce the performance overhead of reference counting. Because the verifiable fragment of Lean cannot create cyclic data, the Lean runtime does not have a technique to detect it. Ullrich and de Moura (2019)Sebastian Ullrich and Leonardo de Moura, 2019. [“Counting Immutable Beans: Reference Counting Optimized for Purely Functional Programming”](https://arxiv.org/abs/1908.05647). In  _Proceedings of the 31st Symposium on Implementation and Application of Functional Languages (IFL 2019)._ provide more details on the implementation of reference counting in Lean.
##  12.2.1. Observing Uniqueness[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Run-Time-Code--Reference-Counting--Observing-Uniqueness "Permalink")
Ensuring that arrays and strings are uniquely referenced is key to writing fast code in Lean. The primitive `[dbgTraceIfShared](Run-Time-Code/Reference-Counting/#dbgTraceIfShared "Documentation for dbgTraceIfShared")` can be used to check whether a data structure is aliased. When called, it returns its argument unchanged, printing the provided trace message if the argument's reference count is greater than one.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=dbgTraceIfShared "Permalink")def
```


dbgTraceIfShared.{u} {α : Type u} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (a : α) : α


dbgTraceIfShared.{u} {α : Type u}
  (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (a : α) : α


```

Display the given message if `a` is shared, that is, RC(a) > 1
Due to the specifics of how ``Lean.Parser.Command.eval : command`
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
`[`#eval`](Interacting-with-Lean/#Lean___Parser___Command___eval) is implemented, using `[dbgTraceIfShared](Run-Time-Code/Reference-Counting/#dbgTraceIfShared "Documentation for dbgTraceIfShared")` with ``Lean.Parser.Command.eval : command`
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
`[`#eval`](Interacting-with-Lean/#Lean___Parser___Command___eval) can be misleading. Instead, it should be used in code that's explicitly compiled and run.
Observing Uniqueness
This program reads a line of input from the user, printing it after replacing its first character with a space. Replacing characters in a string uses an in-place update if the string is not shared and the characters are both contained in the 7-bit ASCII subset of Unicode. The `[dbgTraceIfShared](Run-Time-Code/Reference-Counting/#dbgTraceIfShared "Documentation for dbgTraceIfShared")` call does nothing, indicating that the string will indeed be updated in place rather than copied.
`def process (str : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (h : str.[startPos](Basic-Types/Strings/#String___startPos "Documentation for String.startPos") ≠ str.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") (([dbgTraceIfShared](Run-Time-Code/Reference-Counting/#dbgTraceIfShared "Documentation for dbgTraceIfShared") "String update" str).[startPos](Basic-Types/Strings/#String___startPos "Documentation for String.startPos").[set](Basic-Types/Strings/#String___Pos___set "Documentation for String.Pos.set") ' ' h)  def main : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let line := (← (← [IO.getStdin](IO/Files___-File-Handles___-and-Streams/#IO___getStdin "Documentation for IO.getStdin")).[getLine](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream.getLine")).[trimAscii](Basic-Types/Strings/#String___trimAscii "Documentation for String.trimAscii").[copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")   if h : line.[startPos](Basic-Types/Strings/#String___startPos "Documentation for String.startPos") ≠ line.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos") then     process line h `
When run with this input:
`stdin``Here is input.`
the program emits:
`stdout`` ere is input.`
with an empty standard error output:
`stderr``<empty>`
This version of the program retains a reference to the original string, which necessitates copying the string in the call to `String.set`. This fact is visible in its standard error output.
`def process (str : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (h : str.[startPos](Basic-Types/Strings/#String___startPos "Documentation for String.startPos") ≠ str.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") (([dbgTraceIfShared](Run-Time-Code/Reference-Counting/#dbgTraceIfShared "Documentation for dbgTraceIfShared") "String update" str).[startPos](Basic-Types/Strings/#String___startPos "Documentation for String.startPos").[set](Basic-Types/Strings/#String___Pos___set "Documentation for String.Pos.set") ' ' h)  def main : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let line := (← (← [IO.getStdin](IO/Files___-File-Handles___-and-Streams/#IO___getStdin "Documentation for IO.getStdin")).[getLine](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream.getLine")).[trimAscii](Basic-Types/Strings/#String___trimAscii "Documentation for String.trimAscii").[copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")   if h : line.[startPos](Basic-Types/Strings/#String___startPos "Documentation for String.startPos") ≠ line.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos") then     process line h   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "Original input:"   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") line `
When run with this input:
`stdin``Here is input.`
the program emits:
`stdout`` ere is input.``Original input:``Here is input.`
In its standard error, the message passed to `[dbgTraceIfShared](Run-Time-Code/Reference-Counting/#dbgTraceIfShared "Documentation for dbgTraceIfShared")` is visible.
`stderr``shared RC String update`
##  12.2.2. Compiler IR[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Run-Time-Code--Reference-Counting--Compiler-IR "Permalink")
The compiler option `[trace.compiler.ir.result](Run-Time-Code/Reference-Counting/#trace___compiler___ir___result "Documentation for option trace.compiler.ir.result")` can be used to inspect the compiler's intermediate representation (IR) for a function. In this intermediate representation, reference counting, allocation, and reuse are explicit:
  * The `isShared` operator checks whether a reference count is `1`.
  * `ctor_``nnn` allocates the `nnn`th constructor of a type.
  * `proj_``nnn` retrieves the `nnn`th field from a constructor value.
  * `set ``xxx`﻿`[``nnn`﻿`]` mutates the `nnn`th field of the constructor in `xxx`.
  * `ret ``xxx` returns the value in `xxx`.


The specifics of reference count manipulations can depend on the results of optimization passes such as inlining. While the vast majority of Lean code doesn't require this kind of attention to achieve good performance, knowing how to diagnose unique reference issues can be very important when writing performance-critical code.
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=trace.compiler.ir.result "Permalink")option
```
trace.compiler.ir.result
```

Default value: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
enable/disable tracing for the given module and submodules
Reference Counts in IR
Compiler IR can be used to observe when reference counts are incremented, which can help diagnose situations when a value is expected to have a unique incoming reference, but is in fact shared. Here, `[process](Run-Time-Code/Reference-Counting/#process-_LPAR_in-Reference-Counts-in-IR_RPAR_ "Definition of example")` and `[process'](Run-Time-Code/Reference-Counting/#process___-_LPAR_in-Reference-Counts-in-IR_RPAR_ "Definition of example")` each take a string as a parameter and modify it with `String.set`, returning a pair of strings. While `[process](Run-Time-Code/Reference-Counting/#process-_LPAR_in-Reference-Counts-in-IR_RPAR_ "Definition of example")` returns a constant string as the second element of the pair, `[process'](Run-Time-Code/Reference-Counting/#process___-_LPAR_in-Reference-Counts-in-IR_RPAR_ "Definition of example")` returns the original string.
`set_option [trace.compiler.ir.result](Run-Time-Code/Reference-Counting/#trace___compiler___ir___result "Documentation for option trace.compiler.ir.result") true ``def `[Compiler.IR] [result]     def process._closed_0 : obj :=       let x_1 : obj := "";       ret x_1     def process (x_1 : obj) : obj :=       let x_2 : tagged := 0;       let x_3 : u32 := 32;       let x_4 : obj := String.set x_1 x_2 x_3;       let x_5 : obj := process._closed_0;       let x_6 : obj := ctor_0[Prod.mk] x_4 x_5;       ret x_6`process (str : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") × [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := (str.``String.set` has been deprecated: Use `[String.Pos.Raw.set](Basic-Types/Strings/#String___Pos___Raw___set "Documentation for String.Pos.Raw.set")` instead  Note: The updated constant is in a different namespace. Dot notation may need to be changed (e.g., from `x.set` to `[String.Pos.Raw.set](Basic-Types/Strings/#String___Pos___Raw___set "Documentation for String.Pos.Raw.set") x`).`set 0 ' ', "") ``def `[Compiler.IR] [result]     def process' (x_1 : obj) : obj :=       let x_2 : tagged := 0;       let x_3 : u32 := 32;       inc x_1;       let x_4 : obj := String.set x_1 x_2 x_3;       let x_5 : obj := ctor_0[Prod.mk] x_4 x_1;       ret x_5`process' (str : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") × [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"):= (str.``String.set` has been deprecated: Use `[String.Pos.Raw.set](Basic-Types/Strings/#String___Pos___Raw___set "Documentation for String.Pos.Raw.set")` instead  Note: The updated constant is in a different namespace. Dot notation may need to be changed (e.g., from `x.set` to `[String.Pos.Raw.set](Basic-Types/Strings/#String___Pos___Raw___set "Documentation for String.Pos.Raw.set") x`).`set 0 ' ', str) `
The IR for `[process](Run-Time-Code/Reference-Counting/#process-_LPAR_in-Reference-Counts-in-IR_RPAR_ "Definition of example")` includes no `inc` or `dec` instructions. If the incoming string `x_1` is a unique reference, then it is still a unique reference when passed to `String.set`, which can then use in-place modification:

```
[Compiler.IR] [result]
    def process._closed_0 : obj :=
      let x_1 : obj := "";
      ret x_1
    def process (x_1 : obj) : obj :=
      let x_2 : tagged := 0;
      let x_3 : u32 := 32;
      let x_4 : obj := String.set x_1 x_2 x_3;
      let x_5 : obj := process._closed_0;
      let x_6 : obj := ctor_0[Prod.mk] x_4 x_5;
      ret x_6
```

The IR for `[process'](Run-Time-Code/Reference-Counting/#process___-_LPAR_in-Reference-Counts-in-IR_RPAR_ "Definition of example")`, on the other hand, increments the reference count of the string just before calling `String.set`. Thus, the modified string `x_4` is a copy, regardless of whether the original reference to `x_1` is unique:

```
[Compiler.IR] [result]
    def process' (x_1 : obj) : obj :=
      let x_2 : tagged := 0;
      let x_3 : u32 := 32;
      inc x_1;
      let x_4 : obj := String.set x_1 x_2 x_3;
      let x_5 : obj := ctor_0[Prod.mk] x_4 x_1;
      ret x_5
```

[Live ↪](javascript:openLiveLink\("M4UwLg+g9gDmCWUB2ACMAnAhgYxAOmygFsZ4AbEdPeK9EYAVzLDXQZACgOATEAMxQx0UXMGAoAFMAwoAXCgDKGeEgDmASjmLlalAHXt6FarkBeDiknSqoFgAYUAcicAaFACJ36rrwFCR9MDOUjLySkZqmmE6JgbhxrLmliE24CgOzo5u1upAA"\))
Memory Reuse in IR
The function `[discardElems](Run-Time-Code/Reference-Counting/#discardElems-_LPAR_in-Memory-Reuse-in-IR_RPAR_ "Definition of example")` is a simplified version of `[List.map](Basic-Types/Linked-Lists/#List___map "Documentation for List.map")` that replaces every element in a list with `()`. Inspecting its intermediate representation demonstrates that it will reuse the list's memory when its reference is unique.
`set_option [trace.compiler.ir.result](Run-Time-Code/Reference-Counting/#trace___compiler___ir___result "Documentation for option trace.compiler.ir.result") true  def `[Compiler.IR] [result]     def discardElems._redArg (x_1 : tobj) : tobj :=       case x_1 : tobj of       List.nil →         let x_2 : tagged := ctor_0[List.nil];         ret x_2       List.cons →         let x_3 : u8 := isShared x_1;         case x_3 : u8 of         Bool.false →           let x_4 : tobj := proj[1] x_1;           let x_5 : tobj := proj[0] x_1;           dec x_5;           let x_6 : tagged := ctor_0[PUnit.unit];           let x_7 : tobj := discardElems._redArg x_4;           set x_1[1] := x_7;           set x_1[0] := x_6;           ret x_1         Bool.true →           let x_8 : tobj := proj[1] x_1;           inc x_8;           dec x_1;           let x_9 : tagged := ctor_0[PUnit.unit];           let x_10 : tobj := discardElems._redArg x_8;           let x_11 : obj := ctor_1[List.cons] x_9 x_10;           ret x_11[Compiler.IR] [result]     def discardElems (x_1 : ◾) (x_2 : tobj) : tobj :=       let x_3 : tobj := discardElems._redArg x_2;       ret x_3`discardElems : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α → [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") | [] => [] | x :: xs => () :: [discardElems](Run-Time-Code/Reference-Counting/#discardElems-_LPAR_in-Memory-Reuse-in-IR_RPAR_ "Definition of example") xs `
This emits the following IR:

```
[Compiler.IR] [result]
    def discardElems._redArg (x_1 : tobj) : tobj :=
      case x_1 : tobj of
      List.nil →
        let x_2 : tagged := ctor_0[List.nil];
        ret x_2
      List.cons →
        let x_3 : u8 := isShared x_1;
        case x_3 : u8 of
        Bool.false →
          let x_4 : tobj := proj[1] x_1;
          let x_5 : tobj := proj[0] x_1;
          dec x_5;
          let x_6 : tagged := ctor_0[PUnit.unit];
          let x_7 : tobj := discardElems._redArg x_4;
          set x_1[1] := x_7;
          set x_1[0] := x_6;
          ret x_1
        Bool.true →
          let x_8 : tobj := proj[1] x_1;
          inc x_8;
          dec x_1;
          let x_9 : tagged := ctor_0[PUnit.unit];
          let x_10 : tobj := discardElems._redArg x_8;
          let x_11 : obj := ctor_1[List.cons] x_9 x_10;
          ret x_11[Compiler.IR] [result]
    def discardElems (x_1 : ◾) (x_2 : tobj) : tobj :=
      let x_3 : tobj := discardElems._redArg x_2;
      ret x_3
```

In the IR, the `[List.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")` case explicitly checks whether the argument value is shared (i.e. whether its reference count is greater than one). If the reference is unique, the reference count of the discarded list element `x_5` is decremented and the constructor value is reused. If it is shared, a new `[List.cons](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons")` is allocated in `x_11` for the result.
[Live ↪](javascript:openLiveLink\("M4UwLg+g9gDmCWUB2ACMAnAhgYxAOmygFsZ4AbEdPeK9EYAVzLDXQZACgOATEAMxTd4wbJnTcAohSLAUALhQAZYS0CNwCkBJhEpUoAqknhgOKFAB8UAbQC6KALwA+S1eNmUAD3kK3shygAUAJSegsKi4lIgMu7AQA"\))
[←12.1. Boxing](Run-Time-Code/Boxing/#boxing "12.1. Boxing")[12.3. Multi-Threaded Execution→](Run-Time-Code/Multi-Threaded-Execution/#The-Lean-Language-Reference--Run-Time-Code--Multi-Threaded-Execution "12.3. Multi-Threaded Execution")

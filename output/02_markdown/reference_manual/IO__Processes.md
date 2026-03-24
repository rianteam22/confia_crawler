[←21.8. Timing](IO/Timing/#io-timing "21.8. Timing")[21.10. Random Numbers→](IO/Random-Numbers/#The-Lean-Language-Reference--IO--Random-Numbers "21.10. Random Numbers")
#  21.9. Processes[🔗](find/?domain=Verso.Genre.Manual.section&name=io-processes "Permalink")
##  21.9.1. Current Process[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Processes--Current-Process "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Process.getCurrentDir "Permalink")opaque
```


IO.Process.getCurrentDir : [IO](IO/Logical-Model/#IO "Documentation for IO") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


IO.Process.getCurrentDir :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Returns the current working directory of the calling process.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Process.setCurrentDir "Permalink")opaque
```


IO.Process.setCurrentDir (path : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.Process.setCurrentDir
  (path : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Sets the current working directory of the calling process.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Process.exit "Permalink")opaque
```


IO.Process.exit {α : Type} : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → [IO](IO/Logical-Model/#IO "Documentation for IO") α


IO.Process.exit {α : Type} : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → [IO](IO/Logical-Model/#IO "Documentation for IO") α


```

Terminates the current process with the provided exit code. `0` indicates success, all other values indicate failure.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Process.getPID "Permalink")opaque
```


IO.Process.getPID : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


IO.Process.getPID : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Returns the process ID of the calling process.
##  21.9.2. Running Processes[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Processes--Running-Processes "Permalink")
There are three primary ways to run other programs from Lean:
  1. `[IO.Process.run](IO/Processes/#IO___Process___run "Documentation for IO.Process.run")` synchronously executes another program, returning its standard output as a string. It throws an error if the process exits with an error code other than `0`.
  2. `[IO.Process.output](IO/Processes/#IO___Process___output "Documentation for IO.Process.output")` synchronously executes another program with an empty standard input, capturing its standard output, standard error, and exit code. No error is thrown if the process terminates unsuccessfully.
  3. `[IO.Process.spawn](IO/Processes/#IO___Process___spawn "Documentation for IO.Process.spawn")` starts another program asynchronously and returns a data structure that can be used to access the process's standard input, output, and error streams.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Process.run "Permalink")def
```


IO.Process.run (args : [IO.Process.SpawnArgs](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs"))
  (input? : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


IO.Process.run
  (args : [IO.Process.SpawnArgs](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs"))
  (input? : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Runs a process to completion, blocking until it terminates. The child process is run with a null standard input or the specified input if provided, If the child process terminates successfully with exit code 0, its standard output is returned. An exception is thrown if it terminates with any other exit code.
The specifications of standard input, output, and error handles in `args` are ignored.
Running a Program
When run, this program concatenates its own source code with itself twice using the Unix tool `cat`.
`-- Main.lean begins here def main : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let src2 ← [IO.Process.run](IO/Processes/#IO___Process___run "Documentation for IO.Process.run") {[cmd](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs.cmd") := "cat", [args](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs.args") := #["Main.lean", "Main.lean"]}   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") src2 -- Main.lean ends here `
Its output is:
`stdout``-- Main.lean begins here``def main : IO Unit := do``  let src2 ← IO.Process.run {cmd := "cat", args := #["Main.lean", "Main.lean"]}``  IO.println src2``-- Main.lean ends here``-- Main.lean begins here``def main : IO Unit := do``  let src2 ← IO.Process.run {cmd := "cat", args := #["Main.lean", "Main.lean"]}``  IO.println src2``-- Main.lean ends here`
Running a Program on a File
This program uses the Unix utility `grep` as a filter to find four-digit palindromes. It creates a file that contains all numbers from `0` through `9999`, and then invokes `grep` on it, reading the result from its standard output.
`def main : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   -- Feed the input to the subprocess   [IO.FS.withFile](IO/Files___-File-Handles___-and-Streams/#IO___FS___withFile "Documentation for IO.FS.withFile") "numbers.txt" [.write](IO/Files___-File-Handles___-and-Streams/#IO___FS___Mode___read "Documentation for IO.FS.Mode.write") fun h =>     for i in [0:10000] do       h.[putStrLn](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___putStrLn "Documentation for IO.FS.Handle.putStrLn") (toString i)    let palindromes ← [IO.Process.run](IO/Processes/#IO___Process___run "Documentation for IO.Process.run") {     [cmd](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs.cmd") := "grep",     [args](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs.args") := #[r#"^\([0-9]\)\([0-9]\)\2\1$"#, "numbers.txt"]   }    let count := palindromes.[trimAscii](Basic-Types/Strings/#String___trimAscii "Documentation for String.trimAscii").[split](Basic-Types/Strings/#String___Slice___split "Documentation for String.Slice.split") "\n" |>.[length](Iterators/Consuming-Iterators/#Std___Iter___length "Documentation for Std.Iter.length")    [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"There are {count} four-digit palindromes." `
Its output is:
`stdout``There are 90 four-digit palindromes.`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Process.output "Permalink")def
```


IO.Process.output (args : [IO.Process.SpawnArgs](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs"))
  (input? : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [IO.Process.Output](IO/Processes/#IO___Process___Output___mk "Documentation for IO.Process.Output")


IO.Process.output
  (args : [IO.Process.SpawnArgs](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs"))
  (input? : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [IO.Process.Output](IO/Processes/#IO___Process___Output___mk "Documentation for IO.Process.Output")


```

Runs a process to completion and captures its output and exit code. The child process is run with a null standard input or the specified input if provided, and the current process blocks until it has run to completion.
The specifications of standard input, output, and error handles in `args` are ignored.
Checking Exit Codes
When run, this program first invokes `cat` on a nonexistent file and displays the resulting error code. It then concatenates its own source code with itself twice using the Unix tool `cat`.
`-- Main.lean begins here def main : [IO](IO/Logical-Model/#IO "Documentation for IO") [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let src1 ← [IO.Process.output](IO/Processes/#IO___Process___output "Documentation for IO.Process.output") {[cmd](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs.cmd") := "cat", [args](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs.args") := #["Nonexistent.lean"]}   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Exit code from failed process: {src1.[exitCode](IO/Processes/#IO___Process___Output___mk "Documentation for IO.Process.Output.exitCode")}"    let src2 ← [IO.Process.output](IO/Processes/#IO___Process___output "Documentation for IO.Process.output") {[cmd](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs.cmd") := "cat", [args](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs.args") := #["Main.lean", "Main.lean"]}   if src2.[exitCode](IO/Processes/#IO___Process___Output___mk "Documentation for IO.Process.Output.exitCode") == 0 then     [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") src2.[stdout](IO/Processes/#IO___Process___Output___mk "Documentation for IO.Process.Output.stdout")   else     [IO.eprintln](IO/Console-Output/#IO___eprintln "Documentation for IO.eprintln") "Concatenation failed"     return 1    return 0 -- Main.lean ends here `
Its output is:
`stdout``Exit code from failed process: 1``-- Main.lean begins here``def main : IO UInt32 := do``  let src1 ← IO.Process.output {cmd := "cat", args := #["Nonexistent.lean"]}``  IO.println s!"Exit code from failed process: {src1.exitCode}"````  let src2 ← IO.Process.output {cmd := "cat", args := #["Main.lean", "Main.lean"]}``  if src2.exitCode == 0 then``    IO.println src2.stdout``  else``    IO.eprintln "Concatenation failed"``    return 1````  return 0``-- Main.lean ends here``-- Main.lean begins here``def main : IO UInt32 := do``  let src1 ← IO.Process.output {cmd := "cat", args := #["Nonexistent.lean"]}``  IO.println s!"Exit code from failed process: {src1.exitCode}"````  let src2 ← IO.Process.output {cmd := "cat", args := #["Main.lean", "Main.lean"]}``  if src2.exitCode == 0 then``    IO.println src2.stdout``  else``    IO.eprintln "Concatenation failed"``    return 1````  return 0``-- Main.lean ends here```
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Process.spawn "Permalink")opaque
```


IO.Process.spawn (args : [IO.Process.SpawnArgs](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") ([IO.Process.Child](IO/Processes/#IO___Process___Child___stdin "Documentation for IO.Process.Child") args.[toStdioConfig](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs.toStdioConfig"))


IO.Process.spawn
  (args : [IO.Process.SpawnArgs](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") ([IO.Process.Child](IO/Processes/#IO___Process___Child___stdin "Documentation for IO.Process.Child") args.[toStdioConfig](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs.toStdioConfig"))


```

Starts a child process with the provided configuration. The child process is spawned using operating system primitives, and it can be written in any language.
The child process runs in parallel with the parent.
If the child process's standard input is a pipe, use `[IO.Process.Child.takeStdin](IO/Processes/#IO___Process___Child___takeStdin "Documentation for IO.Process.Child.takeStdin")` to make it possible to close the child's standard input before the process terminates, which provides the child with an end-of-file marker.
Asynchronous Subprocesses
This program uses the Unix utility `grep` as a filter to find four-digit palindromes. It feeds all numbers from `0` through `9999` to the `grep` process and then reads its result. This code is only correct when `grep` is sufficiently fast and when the output pipe is large enough to contain all 90 four-digit palindromes.
`def main : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let grep ← [IO.Process.spawn](IO/Processes/#IO___Process___spawn "Documentation for IO.Process.spawn") {     [cmd](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs.cmd") := "grep",     [args](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs.args") := #[r#"^\([0-9]\)\([0-9]\)\2\1$"#],     [stdin](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stdin") := [.piped](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio.piped"),     [stdout](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stdout") := [.piped](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio.piped"),     [stderr](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stderr") := [.null](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio.null")   }    -- Feed the input to the subprocess   for i in [0:10000] do     grep.[stdin](IO/Processes/#IO___Process___Child___stdin "Documentation for IO.Process.Child.stdin").[putStrLn](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___putStrLn "Documentation for IO.FS.Handle.putStrLn") (toString i)    -- Consume its output, after waiting 100ms for grep to process the data.   [IO.sleep](IO/Timing/#IO___sleep "Documentation for IO.sleep") 100   let count := (← grep.[stdout](IO/Processes/#IO___Process___Child___stdin "Documentation for IO.Process.Child.stdout").[readToEnd](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___readToEnd "Documentation for IO.FS.Handle.readToEnd")).[trimAscii](Basic-Types/Strings/#String___trimAscii "Documentation for String.trimAscii").[split](Basic-Types/Strings/#String___Slice___split "Documentation for String.Slice.split") "\n" |>.[length](Iterators/Consuming-Iterators/#Std___Iter___length "Documentation for Std.Iter.length")    [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"There are {count} four-digit palindromes." `
Its output is:
`stdout``There are 90 four-digit palindromes.`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Process.SpawnArgs.mk "Permalink")structure
```


IO.Process.SpawnArgs : Type


IO.Process.SpawnArgs : Type


```

Configuration for a child process to be spawned.
Use `[IO.Process.spawn](IO/Processes/#IO___Process___spawn "Documentation for IO.Process.spawn")` to start the child process. `[IO.Process.output](IO/Processes/#IO___Process___output "Documentation for IO.Process.output")` and `[IO.Process.run](IO/Processes/#IO___Process___run "Documentation for IO.Process.run")` can be used when the child process should be run to completion, with its output and/or error code captured.
#  Constructor

```
[IO.Process.SpawnArgs.mk](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs.mk")
```

#  Extends
  * `[IO.Process.StdioConfig](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig")`


#  Fields

```
stdin : [IO.Process.Stdio](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio")
```

Inherited from 
  1. `[IO.Process.StdioConfig](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig")`



```
stdout : [IO.Process.Stdio](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio")
```

Inherited from 
  1. `[IO.Process.StdioConfig](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig")`



```
stderr : [IO.Process.Stdio](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio")
```

Inherited from 
  1. `[IO.Process.StdioConfig](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig")`



```
cmd : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

Command name.

```
args : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

Arguments for the command.

```
cwd : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")
```

The child process's working directory. Inherited from the parent current process if `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.

```
env : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")
```

Add or remove environment variables for the child process.
The child process inherits the parent's environment, as modified by `env`. Keys in the array are the names of environment variables. A `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, causes the entry to be removed from the environment, and `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` sets the variable to the new value, adding it if necessary. Variables are processed from left to right.

```
inheritEnv : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

Inherit environment variables from the spawning process.

```
setsid : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

Starts the child process in a new session and process group using `setsid`. Currently a no-op on non-POSIX platforms.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Process.StdioConfig.stdout "Permalink")structure
```


IO.Process.StdioConfig : Type


IO.Process.StdioConfig : Type


```

Configuration for the standard input, output, and error handles of a child process.
#  Constructor

```
[IO.Process.StdioConfig.mk](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.mk")
```

#  Fields

```
stdin : [IO.Process.Stdio](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio")
```

Configuration for the process' stdin handle.

```
stdout : [IO.Process.Stdio](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio")
```

Configuration for the process' stdout handle.

```
stderr : [IO.Process.Stdio](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio")
```

Configuration for the process' stderr handle.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Process.Stdio "Permalink")inductive type
```


IO.Process.Stdio : Type


IO.Process.Stdio : Type


```

Whether the standard input, output, and error handles of a child process should be attached to pipes, inherited from the parent, or null.
If the stream is a pipe, then the parent process can use it to communicate with the child.
#  Constructors

```
piped : [IO.Process.Stdio](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio")
```

The stream should be attached to a pipe.

```
inherit : [IO.Process.Stdio](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio")
```

The stream should be inherited from the parent process.

```
null : [IO.Process.Stdio](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio")
```

The stream should be empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Process.Stdio.toHandleType "Permalink")def
```


IO.Process.Stdio.toHandleType : [IO.Process.Stdio](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio") → Type


IO.Process.Stdio.toHandleType :
  [IO.Process.Stdio](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio") → Type


```

The type of handles that can be used to communicate with a child process on its standard input, output, or error streams.
For `[IO.Process.Stdio.piped](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio.piped")`, this type is `[IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")`. Otherwise, it is `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")`, because no communication is possible.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Process.Child "Permalink")structure
```


IO.Process.Child (cfg : [IO.Process.StdioConfig](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig")) : Type


IO.Process.Child
  (cfg : [IO.Process.StdioConfig](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig")) : Type


```

A child process that was spawned with configuration `cfg`.
The configuration determines whether the child process's standard input, standard output, and standard error are `[IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")`s or `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")`.
#  Fields

```
stdin : cfg.[stdin](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stdin").[toHandleType](IO/Processes/#IO___Process___Stdio___toHandleType "Documentation for IO.Process.Stdio.toHandleType")
```

The child process's standard input handle, if it was configured as `[IO.Process.Stdio.piped](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio.piped")`, or `()` otherwise.

```
stdout : cfg.[stdout](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stdout").[toHandleType](IO/Processes/#IO___Process___Stdio___toHandleType "Documentation for IO.Process.Stdio.toHandleType")
```

The child process's standard output handle, if it was configured as `[IO.Process.Stdio.piped](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio.piped")`, or `()` otherwise.

```
stderr : cfg.[stderr](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stderr").[toHandleType](IO/Processes/#IO___Process___Stdio___toHandleType "Documentation for IO.Process.Stdio.toHandleType")
```

The child process's standard error handle, if it was configured as `[IO.Process.Stdio.piped](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio.piped")`, or `()` otherwise.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Process.Child.wait "Permalink")opaque
```


IO.Process.Child.wait {cfg : [IO.Process.StdioConfig](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig")} :
  [IO.Process.Child](IO/Processes/#IO___Process___Child___stdin "Documentation for IO.Process.Child") cfg → [IO](IO/Logical-Model/#IO "Documentation for IO") [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


IO.Process.Child.wait
  {cfg : [IO.Process.StdioConfig](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig")} :
  [IO.Process.Child](IO/Processes/#IO___Process___Child___stdin "Documentation for IO.Process.Child") cfg → [IO](IO/Logical-Model/#IO "Documentation for IO") [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Blocks until the child process has exited and returns its exit code.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Process.Child.tryWait "Permalink")opaque
```


IO.Process.Child.tryWait {cfg : [IO.Process.StdioConfig](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig")} :
  [IO.Process.Child](IO/Processes/#IO___Process___Child___stdin "Documentation for IO.Process.Child") cfg → [IO](IO/Logical-Model/#IO "Documentation for IO") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32"))


IO.Process.Child.tryWait
  {cfg : [IO.Process.StdioConfig](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig")} :
  [IO.Process.Child](IO/Processes/#IO___Process___Child___stdin "Documentation for IO.Process.Child") cfg →
    [IO](IO/Logical-Model/#IO "Documentation for IO") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32"))


```

Checks whether the child has exited. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the process has not exited, or its exit code if it has.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Process.Child.kill "Permalink")opaque
```


IO.Process.Child.kill {cfg : [IO.Process.StdioConfig](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig")} :
  [IO.Process.Child](IO/Processes/#IO___Process___Child___stdin "Documentation for IO.Process.Child") cfg → [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.Process.Child.kill
  {cfg : [IO.Process.StdioConfig](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig")} :
  [IO.Process.Child](IO/Processes/#IO___Process___Child___stdin "Documentation for IO.Process.Child") cfg → [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Terminates the child process using the `SIGTERM` signal or a platform analogue.
If the process was started using `SpawnArgs.setsid`, terminates the entire process group instead.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Process.Child.takeStdin "Permalink")opaque
```


IO.Process.Child.takeStdin {cfg : [IO.Process.StdioConfig](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig")} :
  [IO.Process.Child](IO/Processes/#IO___Process___Child___stdin "Documentation for IO.Process.Child") cfg →
    [IO](IO/Logical-Model/#IO "Documentation for IO")
      [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")cfg.[stdin](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stdin").[toHandleType](IO/Processes/#IO___Process___Stdio___toHandleType "Documentation for IO.Process.Stdio.toHandleType") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")
        [IO.Process.Child](IO/Processes/#IO___Process___Child___stdin "Documentation for IO.Process.Child")
          [{](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.mk") [stdin](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stdin") [:=](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.mk") [IO.Process.Stdio.null](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio.null")[,](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.mk") [stdout](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stdout") [:=](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.mk") cfg.[stdout](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stdout")[,](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.mk")
            [stderr](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stderr") [:=](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.mk") cfg.[stderr](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stderr") [}](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.mk")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


IO.Process.Child.takeStdin
  {cfg : [IO.Process.StdioConfig](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig")} :
  [IO.Process.Child](IO/Processes/#IO___Process___Child___stdin "Documentation for IO.Process.Child") cfg →
    [IO](IO/Logical-Model/#IO "Documentation for IO")
      [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")cfg.[stdin](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stdin").[toHandleType](IO/Processes/#IO___Process___Stdio___toHandleType "Documentation for IO.Process.Stdio.toHandleType") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")
        [IO.Process.Child](IO/Processes/#IO___Process___Child___stdin "Documentation for IO.Process.Child")
          [{](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.mk")
            [stdin](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stdin") [:=](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.mk")
              [IO.Process.Stdio.null](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio.null")[,](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.mk")
            [stdout](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stdout") [:=](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.mk") cfg.[stdout](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stdout")[,](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.mk")
            [stderr](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stderr") [:=](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.mk") cfg.[stderr](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stderr") [}](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.mk")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Extracts the `stdin` field from a `Child` object, allowing the handle to be closed while maintaining a reference to the child process.
File handles are closed when the last reference to them is dropped. Closing the child's standard input causes an end-of-file marker. Because the `Child` object has a reference to the standard input, this operation is necessary in order to close the stream while the process is running (e.g. to extract its exit code after calling `Child.wait`). Many processes do not terminate until their standard input is exhausted.
Closing a Subprocess's Standard Input
This program uses the Unix utility `grep` as a filter to find four-digit palindromes, ensuring that the subprocess terminates successfully. It feeds all numbers from `0` through `9999` to the `grep` process, then closes the process's standard input, which causes it to terminate. After checking `grep`'s exit code, the program extracts its result.
`def main : [IO](IO/Logical-Model/#IO "Documentation for IO") [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let grep ← do     let (stdin, child) ← (← [IO.Process.spawn](IO/Processes/#IO___Process___spawn "Documentation for IO.Process.spawn") {       [cmd](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs.cmd") := "grep",       [args](IO/Processes/#IO___Process___SpawnArgs___mk "Documentation for IO.Process.SpawnArgs.args") := #[r#"^\([0-9]\)\([0-9]\)\2\1$"#],       [stdin](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stdin") := [.piped](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio.piped"),       [stdout](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stdout") := [.piped](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio.piped"),       [stderr](IO/Processes/#IO___Process___StdioConfig___mk "Documentation for IO.Process.StdioConfig.stderr") := [.null](IO/Processes/#IO___Process___Stdio___piped "Documentation for IO.Process.Stdio.null")     }).[takeStdin](IO/Processes/#IO___Process___Child___takeStdin "Documentation for IO.Process.Child.takeStdin")      -- Feed the input to the subprocess     for i in [0:10000] do       stdin.[putStrLn](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___putStrLn "Documentation for IO.FS.Handle.putStrLn") (toString i)      -- Return the child without its stdin handle.     -- This closes the handle, because there are     -- no more references to it.     [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") child    -- Wait for grep to terminate   if (← grep.[wait](IO/Processes/#IO___Process___Child___wait "Documentation for IO.Process.Child.wait")) != 0 then     [IO.eprintln](IO/Console-Output/#IO___eprintln "Documentation for IO.eprintln") s!"grep terminated unsuccessfully"     return 1    -- Consume its output   let count := (← grep.[stdout](IO/Processes/#IO___Process___Child___stdin "Documentation for IO.Process.Child.stdout").[readToEnd](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___readToEnd "Documentation for IO.FS.Handle.readToEnd")).[trimAscii](Basic-Types/Strings/#String___trimAscii "Documentation for String.trimAscii").[split](Basic-Types/Strings/#String___Slice___split "Documentation for String.Slice.split") "\n" |>.[length](Iterators/Consuming-Iterators/#Std___Iter___length "Documentation for Std.Iter.length")    [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"There are {count} four-digit palindromes."   return 0 `
Its output is:
`stdout``There are 90 four-digit palindromes.`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Process.Output.stdout "Permalink")structure
```


IO.Process.Output : Type


IO.Process.Output : Type


```

The result of running a process to completion.
#  Constructor

```
[IO.Process.Output.mk](IO/Processes/#IO___Process___Output___mk "Documentation for IO.Process.Output.mk")
```

#  Fields

```
exitCode : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")
```

The process's exit code.

```
stdout : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

Everything that was written to the process's standard output.

```
stderr : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

Everything that was written to the process's standard error.
[←21.8. Timing](IO/Timing/#io-timing "21.8. Timing")[21.10. Random Numbers→](IO/Random-Numbers/#The-Lean-Language-Reference--IO--Random-Numbers "21.10. Random Numbers")

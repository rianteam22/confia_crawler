[←21.2. Control Structures](IO/Control-Structures/#io-monad-control "21.2. Control Structures")[21.4. Mutable References→](IO/Mutable-References/#The-Lean-Language-Reference--IO--Mutable-References "21.4. Mutable References")
#  21.3. Console Output[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Console-Output "Permalink")
Lean includes convenience functions for writing to [standard output](IO/Files___-File-Handles___-and-Streams/#--tech-term-standard-output) and [standard error](IO/Files___-File-Handles___-and-Streams/#--tech-term-standard-error). All make use of `ToString` instances, and the varieties whose names end in `-ln` add a newline after the output. These convenience functions only expose a part of the functionality available [using the standard I/O streams](IO/Files___-File-Handles___-and-Streams/#stdio). In particular, to read a line from standard input, use a combination of `[IO.getStdin](IO/Files___-File-Handles___-and-Streams/#IO___getStdin "Documentation for IO.getStdin")` and `[IO.FS.Stream.getLine](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream.getLine")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.print "Permalink")def
```


IO.print.{u_1} {α : Type u_1} [ToString α] (s : α) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.print.{u_1} {α : Type u_1} [ToString α]
  (s : α) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Converts `s` to a string using its `ToString α` instance, and prints it to the current standard output (as determined by `[IO.getStdout](IO/Files___-File-Handles___-and-Streams/#IO___getStdout "Documentation for IO.getStdout")`).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.println "Permalink")def
```


IO.println.{u_1} {α : Type u_1} [ToString α] (s : α) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.println.{u_1} {α : Type u_1}
  [ToString α] (s : α) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Converts `s` to a string using its `ToString α` instance, and prints it with a trailing newline to the current standard output (as determined by `[IO.getStdout](IO/Files___-File-Handles___-and-Streams/#IO___getStdout "Documentation for IO.getStdout")`).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.eprint "Permalink")def
```


IO.eprint.{u_1} {α : Type u_1} [ToString α] (s : α) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.eprint.{u_1} {α : Type u_1}
  [ToString α] (s : α) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Converts `s` to a string using its `ToString α` instance, and prints it to the current standard error (as determined by `[IO.getStderr](IO/Files___-File-Handles___-and-Streams/#IO___getStderr "Documentation for IO.getStderr")`).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.eprintln "Permalink")def
```


IO.eprintln.{u_1} {α : Type u_1} [ToString α] (s : α) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.eprintln.{u_1} {α : Type u_1}
  [ToString α] (s : α) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Converts `s` to a string using its `ToString α` instance, and prints it with a trailing newline to the current standard error (as determined by `[IO.getStderr](IO/Files___-File-Handles___-and-Streams/#IO___getStderr "Documentation for IO.getStderr")`).
Printing
This program demonstrates all four convenience functions for console I/O.
`def main : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   [IO.print](IO/Console-Output/#IO___print "Documentation for IO.print") "This is the "   [IO.print](IO/Console-Output/#IO___print "Documentation for IO.print") "Lean"   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") " language reference."   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "Thank you for reading it!"   [IO.eprint](IO/Console-Output/#IO___eprint "Documentation for IO.eprint") "Please report any "   [IO.eprint](IO/Console-Output/#IO___eprint "Documentation for IO.eprint") "errors"   [IO.eprintln](IO/Console-Output/#IO___eprintln "Documentation for IO.eprintln") " so they can be corrected." `
It outputs the following to the standard output:
`stdout``This is the Lean language reference.``Thank you for reading it!`
and the following to the standard error:
`stderr``Please report any errors so they can be corrected.`
[←21.2. Control Structures](IO/Control-Structures/#io-monad-control "21.2. Control Structures")[21.4. Mutable References→](IO/Mutable-References/#The-Lean-Language-Reference--IO--Mutable-References "21.4. Mutable References")

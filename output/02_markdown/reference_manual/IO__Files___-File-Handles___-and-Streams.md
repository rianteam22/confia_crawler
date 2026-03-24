[←21.4. Mutable References](IO/Mutable-References/#The-Lean-Language-Reference--IO--Mutable-References "21.4. Mutable References")[21.6. System and Platform Information→](IO/System-and-Platform-Information/#platform-info "21.6. System and Platform Information")
#  21.5. Files, File Handles, and Streams[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Files___-File-Handles___-and-Streams "Permalink")
Lean provides a consistent filesystem API on all supported platforms. These are the key concepts: 

Files 
    
Files are an abstraction provided by operating systems that provide random access to persistently-stored data, organized hierarchically into directories. 

Directories 
    
Directories, also known as _folders_ , may contain files or other directories. Fundamentally, a directory maps names to the files and/or directories that it contains. 

File Handles 
    
File handles (`[Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")`) are abstract references to files that have been opened for reading and/or writing. A file handle maintains a mode that determines whether reading and/or writing are allowed, along with a cursor that points at a specific location in the file. Reading from or writing to a file handle advances the cursor. File handles may be buffered, which means that reading from a file handle may not return the current contents of the persistent data, and writing to a file handle may not modify them immediately. 

Paths
    
Files are primarily accessed via _paths_ (`[System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")`). A path is a sequence of directory names, potentially terminated by a file name. They are represented by strings in which separator characters The current platform's separator characters are listed in `[System.FilePath.pathSeparators](IO/Files___-File-Handles___-and-Streams/#System___FilePath___pathSeparators "Documentation for System.FilePath.pathSeparators")`. delimit the names.
The details of paths are platform-specific. Absolute paths begin in a _root directory_ ; some operating systems have a single root, while others may have multiple root directories. Relative paths do not begin in a root directory and require that some other directory be taken as a starting point. In addition to directories, paths may contain the special directory names `.`, which refers to the directory in which it is found, and `..`, which refers to prior directory in the path.
Filenames, and thus paths, may end in one or more _extensions_ that identify the file's type. Extensions are delimited by the character `[System.FilePath.extSeparator](IO/Files___-File-Handles___-and-Streams/#System___FilePath___extSeparator "Documentation for System.FilePath.extSeparator")`. On some platforms, executable files have a special extension (`[System.FilePath.exeExtension](IO/Files___-File-Handles___-and-Streams/#System___FilePath___exeExtension "Documentation for System.FilePath.exeExtension")`). 

Streams 
    
Streams are a higher-level abstraction over files, both providing additional functionality and hiding some details of files. While [file handles](IO/Files___-File-Handles___-and-Streams/#--tech-term-File-Handles) are essentially a thin wrapper around the operating system's representation, streams are implemented in Lean as a structure called `[IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")`. Because streams are implemented in Lean, user code can create additional streams, which can be used seamlessly together with those provided in the standard library.
##  21.5.1. Low-Level File API[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Files___-File-Handles___-and-Streams--Low-Level-File-API "Permalink")
At the lowest level, files are explicitly opened using `[Handle.mk](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___mk "Documentation for IO.FS.Handle.mk")`. When the last reference to the handle object is dropped, the file is closed. There is no explicit way to close a file handle other than by ensuring that there are no references to it.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Handle "Permalink")opaque
```


IO.FS.Handle : Type


IO.FS.Handle : Type


```

A reference to an opened file.
File handles wrap the underlying operating system's file descriptors. There is no explicit operation to close a file: when the last reference to a file handle is dropped, the file is closed automatically.
Handles have an associated read/write cursor that determines where reads and writes occur in the file.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Handle.mk "Permalink")opaque
```


IO.FS.Handle.mk (fn : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) (mode : [IO.FS.Mode](IO/Files___-File-Handles___-and-Streams/#IO___FS___Mode___read "Documentation for IO.FS.Mode")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")


IO.FS.Handle.mk (fn : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath"))
  (mode : [IO.FS.Mode](IO/Files___-File-Handles___-and-Streams/#IO___FS___Mode___read "Documentation for IO.FS.Mode")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")


```

Opens the file at `fn` with the given `mode`.
An exception is thrown if the file cannot be opened.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Mode.write "Permalink")inductive type
```


IO.FS.Mode : Type


IO.FS.Mode : Type


```

Whether a file should be opened for reading, writing, creation and writing, or appending.
At the operating system level, this translates to the mode of a file handle (i.e., a set of `[open](Tactic-Proofs/The-Tactic-Language/#open "Documentation for tactic")` flags and an `fdopen` mode).
None of the modes represented by this datatype translate line endings (i.e. `O_BINARY` on Windows). Furthermore, they are not inherited across process creation (i.e. `O_NOINHERIT` on Windows and `O_CLOEXEC` elsewhere).
**Operating System Specifics:**
  * Windows: [`_open`](https://learn.microsoft.com/en-us/cpp/c-runtime-library/reference/open-wopen?view=msvc-170), [`_fdopen`](https://learn.microsoft.com/en-us/cpp/c-runtime-library/reference/fdopen-wfdopen?view=msvc-170)
  * Linux: [``](https://linux.die.net/man/2/open)`[open](Tactic-Proofs/The-Tactic-Language/#open "Documentation for tactic")`, [`fdopen`](https://linux.die.net/man/3/fdopen)


#  Constructors

```
read : [IO.FS.Mode](IO/Files___-File-Handles___-and-Streams/#IO___FS___Mode___read "Documentation for IO.FS.Mode")
```

The file should be opened for reading.
The read/write cursor is positioned at the beginning of the file. It is an error if the file does not exist.
  * `[open](Tactic-Proofs/The-Tactic-Language/#open "Documentation for tactic")` flags: `O_RDONLY`
  * `fdopen` mode: `r`



```
write : [IO.FS.Mode](IO/Files___-File-Handles___-and-Streams/#IO___FS___Mode___read "Documentation for IO.FS.Mode")
```

The file should be opened for writing.
If the file already exists, it is truncated to zero length. Otherwise, a new file is created. The read/write cursor is positioned at the beginning of the file.
  * `[open](Tactic-Proofs/The-Tactic-Language/#open "Documentation for tactic")` flags: `O_WRONLY | O_CREAT | O_TRUNC`
  * `fdopen` mode: `w`



```
writeNew : [IO.FS.Mode](IO/Files___-File-Handles___-and-Streams/#IO___FS___Mode___read "Documentation for IO.FS.Mode")
```

A new file should be created for writing.
It is an error if the file already exists. A new file is created, with the read/write cursor positioned at the start.
  * `[open](Tactic-Proofs/The-Tactic-Language/#open "Documentation for tactic")` flags: `O_WRONLY | O_CREAT | O_TRUNC | O_EXCL`
  * `fdopen` mode: `w`



```
readWrite : [IO.FS.Mode](IO/Files___-File-Handles___-and-Streams/#IO___FS___Mode___read "Documentation for IO.FS.Mode")
```

The file should be opened for both reading and writing.
It is an error if the file does not already exist. The read/write cursor is positioned at the start of the file.
  * `[open](Tactic-Proofs/The-Tactic-Language/#open "Documentation for tactic")` flags: `O_RDWR`
  * `fdopen` mode: `r+`



```
append : [IO.FS.Mode](IO/Files___-File-Handles___-and-Streams/#IO___FS___Mode___read "Documentation for IO.FS.Mode")
```

The file should be opened for writing.
If the file does not already exist, it is created. If the file already exists, it is opened, and the read/write cursor is positioned at the end of the file.
  * `[open](Tactic-Proofs/The-Tactic-Language/#open "Documentation for tactic")` flags: `O_WRONLY | O_CREAT | O_APPEND`
  * `fdopen` mode: `a`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Handle.read "Permalink")opaque
```


IO.FS.Handle.read (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) (bytes : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


IO.FS.Handle.read (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle"))
  (bytes : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


```

Reads up to the given number of bytes from the handle. If the returned array is empty, an end-of-file marker (EOF) has been reached.
Encountering an EOF does not close a handle. Subsequent reads may block and return more data.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Handle.readToEnd "Permalink")def
```


IO.FS.Handle.readToEnd (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


IO.FS.Handle.readToEnd
  (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Reads the entire remaining contents of the file handle as a UTF-8-encoded string. An exception is thrown if the contents are not valid UTF-8.
The underlying file is not automatically closed, and subsequent reads from the handle may block and/or return data.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Handle.readBinToEnd "Permalink")def
```


IO.FS.Handle.readBinToEnd (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


IO.FS.Handle.readBinToEnd
  (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


```

Reads the entire remaining contents of the file handle until an end-of-file marker (EOF) is encountered.
The underlying file is not automatically closed upon encountering an EOF, and subsequent reads from the handle may block and/or return data.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Handle.readBinToEndInto "Permalink")def
```


IO.FS.Handle.readBinToEndInto (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) (buf : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


IO.FS.Handle.readBinToEndInto
  (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) (buf : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


```

Reads the entire remaining contents of the file handle until an end-of-file marker (EOF) is encountered.
The underlying file is not automatically closed upon encountering an EOF, and subsequent reads from the handle may block and/or return data.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Handle.getLine "Permalink")opaque
```


IO.FS.Handle.getLine (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


IO.FS.Handle.getLine (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Reads UTF-8-encoded text up to and including the next line break from the handle. If the returned string is empty, an end-of-file marker (EOF) has been reached.
Encountering an EOF does not close a handle. Subsequent reads may block and return more data.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Handle.write "Permalink")opaque
```


IO.FS.Handle.write (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) (buffer : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.FS.Handle.write (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle"))
  (buffer : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Writes the provided bytes to the handle.
Writing to a handle is typically buffered, and may not immediately modify the file on disk. Use `[IO.FS.Handle.flush](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___flush "Documentation for IO.FS.Handle.flush")` to write changes to buffers to the associated device.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Handle.putStr "Permalink")opaque
```


IO.FS.Handle.putStr (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.FS.Handle.putStr (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle"))
  (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Writes the provided string to the file handle using the UTF-8 encoding.
Writing to a handle is typically buffered, and may not immediately modify the file on disk. Use `[IO.FS.Handle.flush](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___flush "Documentation for IO.FS.Handle.flush")` to write changes to buffers to the associated device.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Handle.putStrLn "Permalink")def
```


IO.FS.Handle.putStrLn (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.FS.Handle.putStrLn (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle"))
  (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Writes the contents of the string to the handle, followed by a newline. Uses UTF-8.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Handle.flush "Permalink")opaque
```


IO.FS.Handle.flush (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.FS.Handle.flush (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Flushes the output buffer associated with the handle, writing any unwritten data to the associated output device.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Handle.rewind "Permalink")opaque
```


IO.FS.Handle.rewind (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.FS.Handle.rewind (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Rewinds the read/write cursor to the beginning of the handle's file.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Handle.truncate "Permalink")opaque
```


IO.FS.Handle.truncate (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.FS.Handle.truncate (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Truncates the handle to its read/write cursor.
This operation does not automatically flush output buffers, so the contents of the output device may not reflect the change immediately. This does not usually lead to problems because the read/write cursor includes buffered writes. However, buffered writes followed by `[IO.FS.Handle.rewind](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___rewind "Documentation for IO.FS.Handle.rewind")`, then `[IO.FS.Handle.truncate](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___truncate "Documentation for IO.FS.Handle.truncate")`, and then closing the file may lead to a non-empty file. If unsure, call `[IO.FS.Handle.flush](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___flush "Documentation for IO.FS.Handle.flush")` before truncating.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Handle.isTty "Permalink")opaque
```


IO.FS.Handle.isTty (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


IO.FS.Handle.isTty (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if a handle refers to a Windows console or a Unix terminal.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Handle.lock "Permalink")opaque
```


IO.FS.Handle.lock (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) (exclusive : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.FS.Handle.lock (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle"))
  (exclusive : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Acquires an exclusive or shared lock on the handle. Blocks to wait for the lock if necessary.
Acquiring an exclusive lock while already possessing a shared lock will **not** reliably succeed: it works on Unix-like systems but not on Windows.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Handle.tryLock "Permalink")opaque
```


IO.FS.Handle.tryLock (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) (exclusive : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


IO.FS.Handle.tryLock (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle"))
  (exclusive : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Tries to acquire an exclusive or shared lock on the handle and returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if successful. Will not block if the lock cannot be acquired, but instead returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
Acquiring an exclusive lock while already possessing a shared lock will **not** reliably succeed: it works on Unix-like systems but not on Windows.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Handle.unlock "Permalink")opaque
```


IO.FS.Handle.unlock (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.FS.Handle.unlock (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Releases any previously-acquired lock on the handle. Succeeds even if no lock has been acquired.
One File, Multiple Handles
This program has two handles to the same file. Because file I/O may be buffered independently for each handle, `[Handle.flush](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___flush "Documentation for IO.FS.Handle.flush")` should be called when the buffers need to be synchronized with the file's actual contents. Here, the two handles proceed in lock-step through the file, with one of them a single byte ahead of the other. The first handle is used to count the number of occurrences of `'A'`, while the second is used to replace each `'A'` with `'!'`. The second handle is opened in `[readWrite](IO/Files___-File-Handles___-and-Streams/#IO___FS___Mode___read "Documentation for IO.FS.Mode.readWrite")` mode rather than `[write](IO/Files___-File-Handles___-and-Streams/#IO___FS___Mode___read "Documentation for IO.FS.Mode.write")` mode because opening an existing file in `[write](IO/Files___-File-Handles___-and-Streams/#IO___FS___Mode___read "Documentation for IO.FS.Mode.write")` mode replaces it with an empty file. In this case, the buffers don't need to be flushed during execution because modifications occur only to parts of the file that will not be read again, but the write handle should be flushed after the loop has completed.
`[open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") IO.FS ([Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle"))  def main : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Starting contents: '{(← [IO.FS.readFile](IO/Files___-File-Handles___-and-Streams/#IO___FS___readFile "Documentation for IO.FS.readFile") "data").[trimAscii](Basic-Types/Strings/#String___trimAscii "Documentation for String.trimAscii")}'"    let h ← [Handle.mk](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___mk "Documentation for IO.FS.Handle.mk") "data" [.read](IO/Files___-File-Handles___-and-Streams/#IO___FS___Mode___read "Documentation for IO.FS.Mode.read")   let h' ← [Handle.mk](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___mk "Documentation for IO.FS.Handle.mk") "data" [.readWrite](IO/Files___-File-Handles___-and-Streams/#IO___FS___Mode___read "Documentation for IO.FS.Mode.readWrite")   h'.[rewind](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___rewind "Documentation for IO.FS.Handle.rewind")    let mut count := 0   let mut buf : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray") ← h.[read](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___read "Documentation for IO.FS.Handle.read") 1   while ok : buf.[size](Basic-Types/Byte-Arrays/#ByteArray___size "Documentation for ByteArray.size") = 1 do     if [Char.ofUInt8](Basic-Types/Characters/#Char___ofUInt8 "Documentation for Char.ofUInt8") buf[0] == 'A' then       count := count + 1       h'.[write](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___write "Documentation for IO.FS.Handle.write") ([ByteArray.empty](Basic-Types/Byte-Arrays/#ByteArray___empty "Documentation for ByteArray.empty").[push](Basic-Types/Byte-Arrays/#ByteArray___push "Documentation for ByteArray.push") '!'.[toUInt8](Basic-Types/Characters/#Char___toUInt8 "Documentation for Char.toUInt8"))     else       h'.[write](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___write "Documentation for IO.FS.Handle.write") buf     buf ← h.[read](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___read "Documentation for IO.FS.Handle.read") 1    h'.[flush](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle___flush "Documentation for IO.FS.Handle.flush")    [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Count: {count}"   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Contents: '{(← [IO.FS.readFile](IO/Files___-File-Handles___-and-Streams/#IO___FS___readFile "Documentation for IO.FS.readFile") "data").[trimAscii](Basic-Types/Strings/#String___trimAscii "Documentation for String.trimAscii")}'" `
When run on this file:
Input: `data``AABAABCDAB`
the program outputs:
`stdout``Starting contents: 'AABAABCDAB'``Count: 5``Contents: '!!B!!BCD!B'`
Afterwards, the file contains:
Output: `data``!!B!!BCD!B`
##  21.5.2. Streams[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Files___-File-Handles___-and-Streams--Streams "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Stream.mk "Permalink")structure
```


IO.FS.Stream : Type


IO.FS.Stream : Type


```

A pure-Lean abstraction of POSIX streams. These streams may represent an underlying POSIX stream or be implemented by Lean code.
Because standard input, standard output, and standard error are all `[IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")`s that can be overridden, Lean code may capture and redirect input and output.
#  Constructor

```
[IO.FS.Stream.mk](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream.mk")
```

#  Fields

```
flush : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")
```

Flushes the stream's output buffers.

```
read : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize") → [IO](IO/Logical-Model/#IO "Documentation for IO") [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")
```

Reads up to the given number of bytes from the stream.
If the returned array is empty, an end-of-file marker (EOF) has been reached. An EOF does not actually close a stream, so further reads may block and return more data.

```
write : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray") → [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")
```

Writes the provided bytes to the stream.
If the stream represents a physical output device such as a file on disk, then the results may be buffered. Call `FS.Stream.flush` to synchronize their contents.

```
getLine : [IO](IO/Logical-Model/#IO "Documentation for IO") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

Reads text up to and including the next newline from the stream.
If the returned string is empty, an end-of-file marker (EOF) has been reached. An EOF does not actually close a stream, so further reads may block and return more data.

```
putStr : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")
```

Writes the provided string to the stream.

```
isTty : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if a stream refers to a Windows console or Unix terminal.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Stream.ofBuffer "Permalink")def
```


IO.FS.Stream.ofBuffer (r : [IO.Ref](IO/Mutable-References/#IO___Ref "Documentation for IO.Ref") [IO.FS.Stream.Buffer](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___Buffer___mk "Documentation for IO.FS.Stream.Buffer")) : [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")


IO.FS.Stream.ofBuffer
  (r : [IO.Ref](IO/Mutable-References/#IO___Ref "Documentation for IO.Ref") [IO.FS.Stream.Buffer](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___Buffer___mk "Documentation for IO.FS.Stream.Buffer")) :
  [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")


```

Creates a stream from a mutable reference to a buffer.
The resulting stream simulates a file, mutating the contents of the reference in response to writes and reading from it in response to reads. These streams can be used with `[IO.withStdin](IO/Files___-File-Handles___-and-Streams/#IO___withStdin "Documentation for IO.withStdin")`, `[IO.setStdin](IO/Files___-File-Handles___-and-Streams/#IO___setStdin "Documentation for IO.setStdin")`, and the corresponding operators for standard output and standard error to redirect input and output.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Stream.ofHandle "Permalink")def
```


IO.FS.Stream.ofHandle (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) : [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")


IO.FS.Stream.ofHandle (h : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle")) :
  [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")


```

Creates a Lean stream from a file handle. Each stream operation is implemented by the corresponding file handle operation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Stream.putStrLn "Permalink")def
```


IO.FS.Stream.putStrLn (strm : [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")) (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.FS.Stream.putStrLn
  (strm : [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")) (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Writes the contents of the string to the stream, followed by a newline.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Stream.Buffer "Permalink")structure
```


IO.FS.Stream.Buffer : Type


IO.FS.Stream.Buffer : Type


```

A byte buffer that can simulate a file in memory.
Use `[IO.FS.Stream.ofBuffer](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___ofBuffer "Documentation for IO.FS.Stream.ofBuffer")` to create a stream from a buffer.
#  Constructor

```
[IO.FS.Stream.Buffer.mk](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___Buffer___mk "Documentation for IO.FS.Stream.Buffer.mk")
```

#  Fields

```
data : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")
```

The contents of the buffer.

```
pos : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

The read/write cursor's position in the buffer.
##  21.5.3. Paths[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Files___-File-Handles___-and-Streams--Paths "Permalink")
Paths are represented by strings. Different platforms have different conventions for paths: some use slashes (`/`) as directory separators, others use backslashes (`\`). Some are case-sensitive, others are not. Different Unicode encodings and normal forms may be used to represent filenames, and some platforms consider filenames to be byte sequences rather than strings. A string that represents an [absolute path](IO/Files___-File-Handles___-and-Streams/#--tech-term-Absolute-paths) on one system may not even be a valid path on another system.
To write Lean code that is as compatible as possible with multiple systems, it can be helpful to use Lean's path manipulation primitives instead of raw string manipulation. Helpers such as `[System.FilePath.join](IO/Files___-File-Handles___-and-Streams/#System___FilePath___join "Documentation for System.FilePath.join")` take platform-specific rules for absolute paths into account, `[System.FilePath.pathSeparator](IO/Files___-File-Handles___-and-Streams/#System___FilePath___pathSeparator "Documentation for System.FilePath.pathSeparator")` contains the appropriate path separator for the current platform, and `[System.FilePath.exeExtension](IO/Files___-File-Handles___-and-Streams/#System___FilePath___exeExtension "Documentation for System.FilePath.exeExtension")` contains any necessary extension for executable files. Avoid hard-coding these rules.
There is an instance of the `[Div](Type-Classes/Basic-Classes/#Div___mk "Documentation for Div")` type class for `[FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")` which allows the slash operator to be used to concatenate paths.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath "Permalink")structure
```


System.FilePath : Type


System.FilePath : Type


```

A path on the file system.
Paths consist of a sequence of directories followed by the name of a file or directory. They are delimited by a platform-dependent separator character (see `[System.FilePath.pathSeparator](IO/Files___-File-Handles___-and-Streams/#System___FilePath___pathSeparator "Documentation for System.FilePath.pathSeparator")`).
#  Constructor

```
[System.FilePath.mk](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath.mk")
```

#  Fields

```
toString : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

The string representation of the path.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.mkFilePath "Permalink")def
```


System.mkFilePath (parts : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


System.mkFilePath (parts : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Constructs a path from a list of file names by interspersing them with the current platform's path separator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.join "Permalink")def
```


System.FilePath.join (p sub : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


System.FilePath.join
  (p sub : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) :
  [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Appends two paths, taking absolute paths into account. This operation is also accessible via the `/` operator.
If `sub` is an absolute path, then `p` is discarded and `sub` is returned. If `sub` is a relative path, then it is attached to `p` with the platform-specific path separator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.normalize "Permalink")def
```


System.FilePath.normalize (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


System.FilePath.normalize
  (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Normalizes a path, returning an equivalent path that may better follow platform conventions.
In particular:
  * On Windows, drive letters are made uppercase.
  * On platforms that support multiple path separators (that is, where `[System.FilePath.pathSeparators](IO/Files___-File-Handles___-and-Streams/#System___FilePath___pathSeparators "Documentation for System.FilePath.pathSeparators")` has length greater than one), alternative path separators are replaced with the preferred path separator.


There is no guarantee that two equivalent paths normalize to the same path.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.isAbsolute "Permalink")def
```


System.FilePath.isAbsolute (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


System.FilePath.isAbsolute
  (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

An absolute path starts at the root directory or a drive letter. Accessing files through an absolute path does not depend on the current working directory.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.isRelative "Permalink")def
```


System.FilePath.isRelative (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


System.FilePath.isRelative
  (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

A relative path is one that depends on the current working directory for interpretation. Relative paths do not start with the root directory or a drive letter.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.parent "Permalink")def
```


System.FilePath.parent (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


System.FilePath.parent
  (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Returns the parent directory of a path, if there is one.
If the path is that of the root directory or the root of a drive letter, `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` is returned. Otherwise, the path's parent directory is returned.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.components "Permalink")def
```


System.FilePath.components (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


System.FilePath.components
  (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Splits a path into a list of individual file names at the platform-specific path separator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.fileName "Permalink")def
```


System.FilePath.fileName (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


System.FilePath.fileName
  (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Extracts the last element of a path if it is a file or directory name.
Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the last entry is a special name (such as `[.](Tactic-Proofs/The-Tactic-Language/#___ "Documentation for tactic")` or `..`) or if the path is the root directory.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.fileStem "Permalink")def
```


System.FilePath.fileStem (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


System.FilePath.fileStem
  (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Extracts the stem (non-extension) part of `p.[fileName](IO/Files___-File-Handles___-and-Streams/#System___FilePath___fileName "Documentation for System.FilePath.fileName")`.
If the filename contains multiple extensions, then only the last one is removed. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if there is no file name at the end of the path.
Examples:
  * `("app.exe" : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")).[fileStem](IO/Files___-File-Handles___-and-Streams/#System___FilePath___fileStem "Documentation for System.FilePath.fileStem") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "app"`
  * `("file.tar.gz" : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")).[fileStem](IO/Files___-File-Handles___-and-Streams/#System___FilePath___fileStem "Documentation for System.FilePath.fileStem") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "file.tar"`
  * `("files/" : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")).[fileStem](IO/Files___-File-Handles___-and-Streams/#System___FilePath___fileStem "Documentation for System.FilePath.fileStem") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `("files/picture.jpg" : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")).[fileStem](IO/Files___-File-Handles___-and-Streams/#System___FilePath___fileStem "Documentation for System.FilePath.fileStem") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "picture"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.extension "Permalink")def
```


System.FilePath.extension (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


System.FilePath.extension
  (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Extracts the extension part of `p.[fileName](IO/Files___-File-Handles___-and-Streams/#System___FilePath___fileName "Documentation for System.FilePath.fileName")`.
If the filename contains multiple extensions, then only the last one is extracted. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if there is no file name at the end of the path.
Examples:
  * `("app.exe" : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")).[extension](IO/Files___-File-Handles___-and-Streams/#System___FilePath___extension "Documentation for System.FilePath.extension") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "exe"`
  * `("file.tar.gz" : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")).[extension](IO/Files___-File-Handles___-and-Streams/#System___FilePath___extension "Documentation for System.FilePath.extension") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "gz"`
  * `("files/" : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")).[extension](IO/Files___-File-Handles___-and-Streams/#System___FilePath___extension "Documentation for System.FilePath.extension") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `("files/picture.jpg" : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")).[extension](IO/Files___-File-Handles___-and-Streams/#System___FilePath___extension "Documentation for System.FilePath.extension") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "jpg"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.addExtension "Permalink")def
```


System.FilePath.addExtension (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) (ext : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


System.FilePath.addExtension
  (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) (ext : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Appends the extension `ext` to a path `p`.
`ext` should not have leading `[.](Tactic-Proofs/The-Tactic-Language/#___ "Documentation for tactic")`, as this function adds one. If `ext` is the empty string, no `[.](Tactic-Proofs/The-Tactic-Language/#___ "Documentation for tactic")` is added.
Unlike `[System.FilePath.withExtension](IO/Files___-File-Handles___-and-Streams/#System___FilePath___withExtension "Documentation for System.FilePath.withExtension")`, this does not remove any existing extension.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.withExtension "Permalink")def
```


System.FilePath.withExtension (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) (ext : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


System.FilePath.withExtension
  (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) (ext : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Replaces the current extension in a path `p` with `ext`, adding it if there is no extension. If the path has multiple file extensions, only the last one is replaced. If the path has no filename, or if `ext` is the empty string, then the filename is returned unmodified.
`ext` should not have a leading `[.](Tactic-Proofs/The-Tactic-Language/#___ "Documentation for tactic")`, as this function adds one.
Examples:
  * `("files/picture.jpeg" : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")).[withExtension](IO/Files___-File-Handles___-and-Streams/#System___FilePath___withExtension "Documentation for System.FilePath.withExtension") "jpg" = ⟨"files/picture.jpg"⟩`
  * `("files/" : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")).[withExtension](IO/Files___-File-Handles___-and-Streams/#System___FilePath___withExtension "Documentation for System.FilePath.withExtension") "zip" = ⟨"files/"⟩`
  * `("files" : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")).[withExtension](IO/Files___-File-Handles___-and-Streams/#System___FilePath___withExtension "Documentation for System.FilePath.withExtension") "zip" = ⟨"files.zip"⟩`
  * `("files/archive.tar.gz" : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")).[withExtension](IO/Files___-File-Handles___-and-Streams/#System___FilePath___withExtension "Documentation for System.FilePath.withExtension") "xz" = ⟨"files.tar.xz"⟩`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.withFileName "Permalink")def
```


System.FilePath.withFileName (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) (fname : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


System.FilePath.withFileName
  (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) (fname : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Replaces the file name at the end of the path `p` with `fname`, placing `fname` in the parent directory of `p`.
If `p` has no parent directory, then `fname` is returned unmodified.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.pathSeparator "Permalink")def
```


System.FilePath.pathSeparator : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


System.FilePath.pathSeparator : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

The character that separates directories.
On platforms that support multiple separators, `[System.FilePath.pathSeparator](IO/Files___-File-Handles___-and-Streams/#System___FilePath___pathSeparator "Documentation for System.FilePath.pathSeparator")` is the “ideal” one expected by users on the platform. `[System.FilePath.pathSeparators](IO/Files___-File-Handles___-and-Streams/#System___FilePath___pathSeparators "Documentation for System.FilePath.pathSeparators")` lists all supported separators.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.pathSeparators "Permalink")def
```


System.FilePath.pathSeparators : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


System.FilePath.pathSeparators : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

The list of all path separator characters supported on the current platform.
On platforms that support multiple separators, `[System.FilePath.pathSeparator](IO/Files___-File-Handles___-and-Streams/#System___FilePath___pathSeparator "Documentation for System.FilePath.pathSeparator")` is the “ideal” one expected by users on the platform.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.extSeparator "Permalink")def
```


System.FilePath.extSeparator : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


System.FilePath.extSeparator : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

The character that separates file extensions from file names.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.exeExtension "Permalink")def
```


System.FilePath.exeExtension : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


System.FilePath.exeExtension : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

The file extension expected for executable binaries on the current platform, or `""` if there is no such extension.
##  21.5.4. Interacting with the Filesystem[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Files___-File-Handles___-and-Streams--Interacting-with-the-Filesystem "Permalink")
Some operations on paths consult the filesystem.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.Metadata.modified "Permalink")structure
```


IO.FS.Metadata : Type


IO.FS.Metadata : Type


```

File metadata.
The metadata for a file can be accessed with `[System.FilePath.metadata](IO/Files___-File-Handles___-and-Streams/#System___FilePath___metadata "Documentation for System.FilePath.metadata")`/ `[System.FilePath.symlinkMetadata](IO/Files___-File-Handles___-and-Streams/#System___FilePath___symlinkMetadata "Documentation for System.FilePath.symlinkMetadata")`.
#  Constructor

```
[IO.FS.Metadata.mk](IO/Files___-File-Handles___-and-Streams/#IO___FS___Metadata___mk "Documentation for IO.FS.Metadata.mk")
```

#  Fields

```
accessed : IO.FS.SystemTime
```

File access time.

```
modified : IO.FS.SystemTime
```

File modification time.

```
byteSize : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")
```

The size of the file in bytes.

```
type : IO.FS.FileType
```

Whether the file is an ordinary file, a directory, a symbolic link, or some other kind of file.

```
numLinks : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")
```

The number of hard links to the file.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.metadata "Permalink")opaque
```


System.FilePath.metadata : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath") → [IO](IO/Logical-Model/#IO "Documentation for IO") [IO.FS.Metadata](IO/Files___-File-Handles___-and-Streams/#IO___FS___Metadata___mk "Documentation for IO.FS.Metadata")


System.FilePath.metadata :
  [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath") → [IO](IO/Logical-Model/#IO "Documentation for IO") [IO.FS.Metadata](IO/Files___-File-Handles___-and-Streams/#IO___FS___Metadata___mk "Documentation for IO.FS.Metadata")


```

Returns metadata for the indicated file, following symlinks. Throws an exception if the file does not exist or the metadata cannot be accessed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.symlinkMetadata "Permalink")opaque
```


System.FilePath.symlinkMetadata : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath") → [IO](IO/Logical-Model/#IO "Documentation for IO") [IO.FS.Metadata](IO/Files___-File-Handles___-and-Streams/#IO___FS___Metadata___mk "Documentation for IO.FS.Metadata")


System.FilePath.symlinkMetadata :
  [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath") → [IO](IO/Logical-Model/#IO "Documentation for IO") [IO.FS.Metadata](IO/Files___-File-Handles___-and-Streams/#IO___FS___Metadata___mk "Documentation for IO.FS.Metadata")


```

Returns metadata for the indicated file without following symlinks. Throws an exception if the file does not exist or the metadata cannot be accessed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.pathExists "Permalink")def
```


System.FilePath.pathExists (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


System.FilePath.pathExists
  (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the indicated path points to a file that exists. This function will traverse symlinks.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.isDir "Permalink")def
```


System.FilePath.isDir (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


System.FilePath.isDir
  (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the indicated path can be read and is a directory. This function will traverse symlinks.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.DirEntry "Permalink")structure
```


IO.FS.DirEntry : Type


IO.FS.DirEntry : Type


```

An entry in a directory on a filesystem.
#  Constructor

```
[IO.FS.DirEntry.mk](IO/Files___-File-Handles___-and-Streams/#IO___FS___DirEntry___mk "Documentation for IO.FS.DirEntry.mk")
```

#  Fields

```
root : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")
```

The directory in which the entry is found.

```
fileName : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

The name of the entry.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.DirEntry.path "Permalink")def
```


IO.FS.DirEntry.path (entry : [IO.FS.DirEntry](IO/Files___-File-Handles___-and-Streams/#IO___FS___DirEntry___mk "Documentation for IO.FS.DirEntry")) : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


IO.FS.DirEntry.path
  (entry : [IO.FS.DirEntry](IO/Files___-File-Handles___-and-Streams/#IO___FS___DirEntry___mk "Documentation for IO.FS.DirEntry")) :
  [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

The path of the file indicated by the directory entry.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.readDir "Permalink")opaque
```


System.FilePath.readDir : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath") → [IO](IO/Logical-Model/#IO "Documentation for IO") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [IO.FS.DirEntry](IO/Files___-File-Handles___-and-Streams/#IO___FS___DirEntry___mk "Documentation for IO.FS.DirEntry"))


System.FilePath.readDir :
  [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath") →
    [IO](IO/Logical-Model/#IO "Documentation for IO") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [IO.FS.DirEntry](IO/Files___-File-Handles___-and-Streams/#IO___FS___DirEntry___mk "Documentation for IO.FS.DirEntry"))


```

Returns the contents of the indicated directory. Throws an exception if the file does not exist or is not a directory.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.FilePath.walkDir "Permalink")def
```


System.FilePath.walkDir (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath"))
  (enter : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath") → [IO](IO/Logical-Model/#IO "Documentation for IO") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := fun x => [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath"))


System.FilePath.walkDir
  (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath"))
  (enter : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath") → [IO](IO/Logical-Model/#IO "Documentation for IO") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") :=
    fun x => [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath"))


```

Traverses a filesystem starting at the path `p` and exploring directories that satisfy `enter`, returning the paths visited.
The traversal is a preorder traversal, in which parent directories occur prior to any of their children. Symbolic links are followed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.AccessRight.mk "Permalink")structure
```


IO.AccessRight : Type


IO.AccessRight : Type


```

POSIX-style file permissions.
The `FileRight` structure describes these permissions for a file's owner, members of its designated group, and all others.
#  Constructor

```
[IO.AccessRight.mk](IO/Files___-File-Handles___-and-Streams/#IO___AccessRight___mk "Documentation for IO.AccessRight.mk")
```

#  Fields

```
read : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

The file can be read.

```
write : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

The file can be written to.

```
execution : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

The file can be executed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.AccessRight.flags "Permalink")def
```


IO.AccessRight.flags (acc : [IO.AccessRight](IO/Files___-File-Handles___-and-Streams/#IO___AccessRight___mk "Documentation for IO.AccessRight")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


IO.AccessRight.flags
  (acc : [IO.AccessRight](IO/Files___-File-Handles___-and-Streams/#IO___AccessRight___mk "Documentation for IO.AccessRight")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Converts individual POSIX-style file permissions to their conventional three-bit representation.
This is the bitwise `[or](Basic-Types/Booleans/#Bool___or "Documentation for Bool.or")` of the following:
  * If the file can be read, `0x4`, otherwise `0`.
  * If the file can be written, `0x2`, otherwise `0`.
  * If the file can be executed, `0x1`, otherwise `0`.


Examples:
  * `{read := true : AccessRight}.flags = 4`
  * `{read := true, write := true : AccessRight}.flags = 6`
  * `{read := true, execution := true : AccessRight}.flags = 5`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FileRight.other "Permalink")structure
```


IO.FileRight : Type


IO.FileRight : Type


```

POSIX-style file permissions that describe access rights for a file's owner, members of its assigned group, and all others.
#  Constructor

```
[IO.FileRight.mk](IO/Files___-File-Handles___-and-Streams/#IO___FileRight___mk "Documentation for IO.FileRight.mk")
```

#  Fields

```
user : [IO.AccessRight](IO/Files___-File-Handles___-and-Streams/#IO___AccessRight___mk "Documentation for IO.AccessRight")
```

The owner's permissions to access the file.

```
group : [IO.AccessRight](IO/Files___-File-Handles___-and-Streams/#IO___AccessRight___mk "Documentation for IO.AccessRight")
```

The assigned group's permissions to access the file.

```
other : [IO.AccessRight](IO/Files___-File-Handles___-and-Streams/#IO___AccessRight___mk "Documentation for IO.AccessRight")
```

The permissions that all others have to access the file.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FileRight.flags "Permalink")def
```


IO.FileRight.flags (acc : [IO.FileRight](IO/Files___-File-Handles___-and-Streams/#IO___FileRight___mk "Documentation for IO.FileRight")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


IO.FileRight.flags (acc : [IO.FileRight](IO/Files___-File-Handles___-and-Streams/#IO___FileRight___mk "Documentation for IO.FileRight")) :
  [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Converts POSIX-style file permissions to their numeric representation, with three bits each for the owner's permissions, the group's permissions, and others' permissions.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.setAccessRights "Permalink")def
```


IO.setAccessRights (filename : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) (mode : [IO.FileRight](IO/Files___-File-Handles___-and-Streams/#IO___FileRight___mk "Documentation for IO.FileRight")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.setAccessRights
  (filename : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath"))
  (mode : [IO.FileRight](IO/Files___-File-Handles___-and-Streams/#IO___FileRight___mk "Documentation for IO.FileRight")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Sets the POSIX-style permissions for a file.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.removeFile "Permalink")opaque
```


IO.FS.removeFile (fname : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.FS.removeFile
  (fname : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Removes (deletes) a file from the filesystem.
To remove a directory, use `[IO.FS.removeDir](IO/Files___-File-Handles___-and-Streams/#IO___FS___removeDir "Documentation for IO.FS.removeDir")` or `[IO.FS.removeDirAll](IO/Files___-File-Handles___-and-Streams/#IO___FS___removeDirAll "Documentation for IO.FS.removeDirAll")` instead.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.rename "Permalink")opaque
```


IO.FS.rename (old new : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.FS.rename (old new : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Moves a file or directory `old` to the new location `new`.
This function coincides with the [POSIX ``](https://pubs.opengroup.org/onlinepubs/9699919799/functions/rename.html)`[rename](Tactic-Proofs/The-Tactic-Language/#rename "Documentation for tactic")` function.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.removeDir "Permalink")opaque
```


IO.FS.removeDir : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath") → [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.FS.removeDir :
  [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath") → [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Removes (deletes) a directory.
Removing a directory fails if the directory is not empty. Use `[IO.FS.removeDirAll](IO/Files___-File-Handles___-and-Streams/#IO___FS___removeDirAll "Documentation for IO.FS.removeDirAll")` to remove directories along with their contents.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.lines "Permalink")def
```


IO.FS.lines (fname : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [IO](IO/Logical-Model/#IO "Documentation for IO") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))


IO.FS.lines (fname : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))


```

Returns the contents of a UTF-8-encoded text file as an array of lines.
Newline markers are not included in the lines.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.withTempFile "Permalink")def
```


IO.FS.withTempFile.{u_1} {m : Type → Type u_1} {α : Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[MonadFinally](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally") m] [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [IO](IO/Logical-Model/#IO "Documentation for IO") m]
  (f : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle") → [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath") → m α) : m α


IO.FS.withTempFile.{u_1}
  {m : Type → Type u_1} {α : Type}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[MonadFinally](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally") m]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [IO](IO/Logical-Model/#IO "Documentation for IO") m]
  (f :
    [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle") →
      [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath") → m α) :
  m α


```

Creates a temporary file in the most secure manner possible and calls `f` with both a `Handle` to the already-opened file and its path. Afterwards, the temporary file is deleted.
There are no race conditions in the file’s creation. The file is readable and writable only by the creating user ID. Additionally on UNIX style platforms the file is executable by nobody.
Use `[IO.FS.createTempFile](IO/Files___-File-Handles___-and-Streams/#IO___FS___createTempFile "Documentation for IO.FS.createTempFile")` to avoid the automatic deletion of the temporary file.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.withTempDir "Permalink")def
```


IO.FS.withTempDir.{u_1} {m : Type → Type u_1} {α : Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[MonadFinally](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally") m] [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [IO](IO/Logical-Model/#IO "Documentation for IO") m] (f : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath") → m α) : m α


IO.FS.withTempDir.{u_1}
  {m : Type → Type u_1} {α : Type}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[MonadFinally](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally") m]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [IO](IO/Logical-Model/#IO "Documentation for IO") m]
  (f : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath") → m α) : m α


```

Creates a temporary directory in the most secure manner possible, providing its path to an `[IO](IO/Logical-Model/#IO "Documentation for IO")` action. Afterwards, all files in the temporary directory are recursively deleted, regardless of how or when they were created.
There are no race conditions in the directory’s creation. The directory is readable and writable only by the creating user ID. Use `[IO.FS.createTempDir](IO/Files___-File-Handles___-and-Streams/#IO___FS___createTempDir "Documentation for IO.FS.createTempDir")` to avoid the automatic deletion of the directory's contents.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.createDirAll "Permalink")opaque
```


IO.FS.createDirAll (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.FS.createDirAll (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Creates a directory at the specified path, creating all missing parents as directories.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.writeBinFile "Permalink")def
```


IO.FS.writeBinFile (fname : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) (content : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.FS.writeBinFile
  (fname : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath"))
  (content : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Write the provided bytes to a binary file at the specified path.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.withFile "Permalink")def
```


IO.FS.withFile {α : Type} (fn : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) (mode : [IO.FS.Mode](IO/Files___-File-Handles___-and-Streams/#IO___FS___Mode___read "Documentation for IO.FS.Mode"))
  (f : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle") → [IO](IO/Logical-Model/#IO "Documentation for IO") α) : [IO](IO/Logical-Model/#IO "Documentation for IO") α


IO.FS.withFile {α : Type}
  (fn : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath"))
  (mode : [IO.FS.Mode](IO/Files___-File-Handles___-and-Streams/#IO___FS___Mode___read "Documentation for IO.FS.Mode"))
  (f : [IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle") → [IO](IO/Logical-Model/#IO "Documentation for IO") α) : [IO](IO/Logical-Model/#IO "Documentation for IO") α


```

Opens the file `fn` with the specified `mode` and passes the resulting file handle to `f`.
The file handle is closed when the last reference to it is dropped. If references escape `f`, then the file remains open even after `[IO.FS.withFile](IO/Files___-File-Handles___-and-Streams/#IO___FS___withFile "Documentation for IO.FS.withFile")` has finished.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.removeDirAll "Permalink")opaque
```


IO.FS.removeDirAll (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.FS.removeDirAll (p : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Fully remove given directory by deleting all contained files and directories in an unspecified order. Symlinks are deleted but not followed. Fails if any contained entry cannot be deleted or was newly created during execution.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.createTempFile "Permalink")opaque
```


IO.FS.createTempFile : [IO](IO/Logical-Model/#IO "Documentation for IO") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")[IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


IO.FS.createTempFile :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")[IO.FS.Handle](IO/Files___-File-Handles___-and-Streams/#IO___FS___Handle "Documentation for IO.FS.Handle") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Creates a temporary file in the most secure manner possible, returning both a `Handle` to the already-opened file and its path.
There are no race conditions in the file’s creation. The file is readable and writable only by the creating user ID. Additionally on UNIX style platforms the file is executable by nobody.
It is the caller's job to remove the file after use. Use `withTempFile` to ensure that the temporary file is removed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.createTempDir "Permalink")opaque
```


IO.FS.createTempDir : [IO](IO/Logical-Model/#IO "Documentation for IO") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


IO.FS.createTempDir : [IO](IO/Logical-Model/#IO "Documentation for IO") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Creates a temporary directory in the most secure manner possible, returning the new directory's path. There are no race conditions in the directory’s creation. The directory is readable and writable only by the creating user ID.
It is the caller's job to remove the directory after use. Use `withTempDir` to ensure that the temporary directory is removed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.readFile "Permalink")def
```


IO.FS.readFile (fname : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


IO.FS.readFile (fname : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Reads the entire contents of the UTF-8-encoded file at the given path as a `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`.
An exception is thrown if the contents of the file are not valid UTF-8. This is in addition to exceptions that may always be thrown as a result of failing to read files.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.realPath "Permalink")opaque
```


IO.FS.realPath (fname : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


IO.FS.realPath (fname : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Resolves a path to an absolute path that contains no '.', '..', or symbolic links.
This function coincides with the [POSIX `realpath` function](https://pubs.opengroup.org/onlinepubs/9699919799/functions/realpath.html).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.writeFile "Permalink")def
```


IO.FS.writeFile (fname : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) (content : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.FS.writeFile (fname : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath"))
  (content : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Write contents of a string to a file at the specified path using UTF-8 encoding.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.readBinFile "Permalink")def
```


IO.FS.readBinFile (fname : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


IO.FS.readBinFile
  (fname : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")) : [IO](IO/Logical-Model/#IO "Documentation for IO") [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


```

Reads the entire contents of the binary file at the given path as an array of bytes.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.createDir "Permalink")opaque
```


IO.FS.createDir : [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath") → [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.FS.createDir :
  [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath") → [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Creates a directory at the specified path. The parent directory must already exist.
Throws an exception if the directory cannot be created.
##  21.5.5. Standard I/O[🔗](find/?domain=Verso.Genre.Manual.section&name=stdio "Permalink")
On operating systems that are derived from or inspired by Unix, _standard input_ , _standard output_ , and _standard error_ are the names of three streams that are available in each process. Generally, programs are expected to read from standard input, write ordinary output to the standard output, and error messages to the standard error. By default, standard input receives input from the console, while standard output and standard error output to the console, but all three are often redirected to or from pipes or files.
Rather than providing direct access to the operating system's standard I/O facilities, Lean wraps them in `[Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")`s. Additionally, the `[IO](IO/Logical-Model/#IO "Documentation for IO")` monad contains special support for replacing or locally overriding them. This extra level of indirection makes it possible to redirect input and output within a Lean program.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.getStdin "Permalink")opaque
```


IO.getStdin : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")


IO.getStdin : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")


```

Returns the current thread's standard input stream.
Use `[IO.setStdin](IO/Files___-File-Handles___-and-Streams/#IO___setStdin "Documentation for IO.setStdin")` to replace the current thread's standard input stream.
Reading from Standard Input
In this example, `[IO.getStdin](IO/Files___-File-Handles___-and-Streams/#IO___getStdin "Documentation for IO.getStdin")` and `[IO.getStdout](IO/Files___-File-Handles___-and-Streams/#IO___getStdout "Documentation for IO.getStdout")` are used to get the current standard input and output, respectively. These can be read from and written to.
`def main : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let stdin ← [IO.getStdin](IO/Files___-File-Handles___-and-Streams/#IO___getStdin "Documentation for IO.getStdin")   let stdout ← [IO.getStdout](IO/Files___-File-Handles___-and-Streams/#IO___getStdout "Documentation for IO.getStdout")   stdout.[putStrLn](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___putStrLn "Documentation for IO.FS.Stream.putStrLn") "Who is it?"   let name ← stdin.[getLine](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream.getLine")   stdout.[putStr](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream.putStr") "Hello, "   stdout.[putStrLn](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___putStrLn "Documentation for IO.FS.Stream.putStrLn") name `
With this standard input:
`stdin``Lean user`
the standard output is:
`stdout``Who is it?``Hello, Lean user`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.setStdin "Permalink")opaque
```


IO.setStdin : [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream") → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")


IO.setStdin :
  [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream") → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")


```

Replaces the standard input stream of the current thread and returns its previous value.
Use `[IO.getStdin](IO/Files___-File-Handles___-and-Streams/#IO___getStdin "Documentation for IO.getStdin")` to get the current standard input stream.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.withStdin "Permalink")def
```


IO.withStdin.{u_1} {m : Type → Type u_1} {α : Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[MonadFinally](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally") m] [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") m] (h : [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")) (x : m α) :
  m α


IO.withStdin.{u_1} {m : Type → Type u_1}
  {α : Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[MonadFinally](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally") m]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") m] (h : [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream"))
  (x : m α) : m α


```

Runs an action with the specified stream `h` as standard input, restoring the original standard input stream afterwards.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.getStdout "Permalink")opaque
```


IO.getStdout : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")


IO.getStdout : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")


```

Returns the current thread's standard output stream.
Use `[IO.setStdout](IO/Files___-File-Handles___-and-Streams/#IO___setStdout "Documentation for IO.setStdout")` to replace the current thread's standard output stream.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.setStdout "Permalink")opaque
```


IO.setStdout : [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream") → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")


IO.setStdout :
  [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream") → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")


```

Replaces the standard output stream of the current thread and returns its previous value.
Use `[IO.getStdout](IO/Files___-File-Handles___-and-Streams/#IO___getStdout "Documentation for IO.getStdout")` to get the current standard output stream.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.withStdout "Permalink")def
```


IO.withStdout.{u_1} {m : Type → Type u_1} {α : Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[MonadFinally](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally") m] [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") m] (h : [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")) (x : m α) :
  m α


IO.withStdout.{u_1} {m : Type → Type u_1}
  {α : Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[MonadFinally](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally") m]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") m] (h : [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream"))
  (x : m α) : m α


```

Runs an action with the specified stream `h` as standard output, restoring the original standard output stream afterwards.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.getStderr "Permalink")opaque
```


IO.getStderr : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")


IO.getStderr : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")


```

Returns the current thread's standard error stream.
Use `[IO.setStderr](IO/Files___-File-Handles___-and-Streams/#IO___setStderr "Documentation for IO.setStderr")` to replace the current thread's standard error stream.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.setStderr "Permalink")opaque
```


IO.setStderr : [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream") → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")


IO.setStderr :
  [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream") → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")


```

Replaces the standard error stream of the current thread and returns its previous value.
Use `[IO.getStderr](IO/Files___-File-Handles___-and-Streams/#IO___getStderr "Documentation for IO.getStderr")` to get the current standard error stream.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.withStderr "Permalink")def
```


IO.withStderr.{u_1} {m : Type → Type u_1} {α : Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  [[MonadFinally](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally") m] [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") m] (h : [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream")) (x : m α) :
  m α


IO.withStderr.{u_1} {m : Type → Type u_1}
  {α : Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[MonadFinally](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally") m]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") m] (h : [IO.FS.Stream](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream"))
  (x : m α) : m α


```

Runs an action with the specified stream `h` as standard error, restoring the original standard error stream afterwards.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.FS.withIsolatedStreams "Permalink")def
```


IO.FS.withIsolatedStreams.{u_1} {m : Type → Type u_1} {α : Type}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[MonadFinally](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally") m] [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") m] (x : m α)
  (isolateStderr : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : m [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") α[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


IO.FS.withIsolatedStreams.{u_1}
  {m : Type → Type u_1} {α : Type}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] [[MonadFinally](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadFinally___mk "Documentation for MonadFinally") m]
  [[MonadLiftT](Functors___-Monads-and--do--Notation/Lifting-Monads/#MonadLiftT___mk "Documentation for MonadLiftT") [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") m] (x : m α)
  (isolateStderr : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) :
  m [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") α[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Runs an action with `stdin` emptied and `stdout` and `stderr` captured into a `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`. If `isolateStderr` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, only `stdout` is captured.
Redirecting Standard I/O to Strings
The `[countdown](IO/Files___-File-Handles___-and-Streams/#countdown-_LPAR_in-Redirecting-Standard-I___O-to-Strings_RPAR_ "Definition of example")` function counts down from a specified number, writing its progress to standard output. Using `IO.FS.withIsolatedStreams`, this output can be redirected to a string.
`def countdown : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")   | 0 =>     [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "Blastoff!"   | n + 1 => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")     [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"{n + 1}"     [countdown](IO/Files___-File-Handles___-and-Streams/#countdown-_LPAR_in-Redirecting-Standard-I___O-to-Strings_RPAR_ "Definition of example") n  def runCountdown : [IO](IO/Logical-Model/#IO "Documentation for IO") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   let (output, ()) ← [IO.FS.withIsolatedStreams](IO/Files___-File-Handles___-and-Streams/#IO___FS___withIsolatedStreams "Documentation for IO.FS.withIsolatedStreams") ([countdown](IO/Files___-File-Handles___-and-Streams/#countdown-_LPAR_in-Redirecting-Standard-I___O-to-Strings_RPAR_ "Definition of example") 10)   return output  `"10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nBlastoff!\n"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [runCountdown](IO/Files___-File-Handles___-and-Streams/#runCountdown-_LPAR_in-Redirecting-Standard-I___O-to-Strings_RPAR_ "Definition of example") `
Running `[countdown](IO/Files___-File-Handles___-and-Streams/#countdown-_LPAR_in-Redirecting-Standard-I___O-to-Strings_RPAR_ "Definition of example")` yields a string that contains the output:

```
"10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nBlastoff!\n"
```

[Live ↪](javascript:openLiveLink\("CYUwZgBAxg9grgOwC7BgdwRAXBAcgQyQkCTCCASQHkIBVBASyQCgIIAfCABggF4A+ZluQoA6AA4AnOsgA2mAEQAhafgDOSGGDABCOQPaYA1BACMPXhFQCWlMZJmYVOgN6GTAX12Do8ZKgwQERkZQSHFEAGEfFHRMHEoIAGUkOwBzbG4LGAFpECIACngkUTgkABoIPIBKSohABMIhYQAxBOE0BgALMhUYZSQQYCTxEHwAWxUK2ERo/2MOSoEhpDhxTELipkYAYhAAN3xpCDCESKm/BCA"\))
##  21.5.6. Files and Directories[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Files___-File-Handles___-and-Streams--Files-and-Directories "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.currentDir "Permalink")opaque
```


IO.currentDir : [IO](IO/Logical-Model/#IO "Documentation for IO") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


IO.currentDir : [IO](IO/Logical-Model/#IO "Documentation for IO") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Returns the current working directory of the executing process.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.appPath "Permalink")opaque
```


IO.appPath : [IO](IO/Logical-Model/#IO "Documentation for IO") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


IO.appPath : [IO](IO/Logical-Model/#IO "Documentation for IO") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Returns the file name of the currently-running executable.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.appDir "Permalink")def
```


IO.appDir : [IO](IO/Logical-Model/#IO "Documentation for IO") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


IO.appDir : [IO](IO/Logical-Model/#IO "Documentation for IO") [System.FilePath](IO/Files___-File-Handles___-and-Streams/#System___FilePath___mk "Documentation for System.FilePath")


```

Returns the directory that the current executable is located in.
[←21.4. Mutable References](IO/Mutable-References/#The-Lean-Language-Reference--IO--Mutable-References "21.4. Mutable References")[21.6. System and Platform Information→](IO/System-and-Platform-Information/#platform-info "21.6. System and Platform Information")

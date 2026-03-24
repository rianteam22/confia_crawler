[←21. IO](IO/#io "21. IO")[21.2. Control Structures→](IO/Control-Structures/#io-monad-control "21.2. Control Structures")
#  21.1. Logical Model[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--IO--Logical-Model "Permalink")
Conceptually, Lean distinguishes evaluation or reduction of terms from _execution_ of side effects. Term reduction is specified by rules such as [β](The-Type-System/#--tech-term-___) and [δ](The-Type-System/#--tech-term-___-next), which may occur anywhere at any time. Side effects, which must be executed in the correct order, are abstractly described in Lean's logic. When programs are run, the Lean runtime system is responsible for actually carrying out the described effects.
The type `[IO](IO/Logical-Model/#IO "Documentation for IO") α` is a description of a process that, by performing side effects, should either return a value of type `α` or throw an error. It can be thought of as a [state monad](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#--tech-term-State-monads) in which the state is the entire world. Just as a value of type `[StateM](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#StateM "Documentation for StateM") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` computes a `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` while having the ability to mutate a natural number, a value of type `[IO](IO/Logical-Model/#IO "Documentation for IO") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` computes a `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` while potentially changing the world. Error handling is accomplished by layering an appropriate exception monad transformer on top of this.
Because the entire world can't be represented in memory, the actual implementation uses an abstract token that stands for its state. The Lean runtime system is responsible for providing the initial token when the program is run, and each primitive action accepts a token that represents the world and returns another when finished. This ensures that effects occur in the proper order, and it clearly separates the execution of side effects from the reduction semantics of Lean terms.
Non-termination via general recursion is treated separately from the effects described by `[IO](IO/Logical-Model/#IO "Documentation for IO")`. Programs that may not terminate due to infinite loops must be defined as [`partial`](Definitions/Recursive-Definitions/#partial-unsafe) functions. From the logical perspective, they are treated as arbitrary constants; `[IO](IO/Logical-Model/#IO "Documentation for IO")` is not needed.
A very important property of `[IO](IO/Logical-Model/#IO "Documentation for IO")` is that there is no way for values to “escape”. Without using one of a few clearly-marked unsafe operators, programs have no way to extract a pure `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` from an `[IO](IO/Logical-Model/#IO "Documentation for IO") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`. This ensures that the correct ordering of side effects is preserved, and it ensures that programs that have side effects are clearly marked as such.
##  21.1.1. The `IO`, `EIO` and `BaseIO` Monads[🔗](find/?domain=Verso.Genre.Manual.section&name=io-monad "Permalink")
There are two monads that are typically used for programs that interact with the real world:
  * Actions in `[IO](IO/Logical-Model/#IO "Documentation for IO")` may throw exceptions of type `[IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")` or modify the world.
  * Actions in `[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` can't throw exceptions, but they can modify the world.


The distinction makes it possible to tell whether exceptions are possible by looking at an action's type signature. `[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` actions are automatically promoted to `[IO](IO/Logical-Model/#IO "Documentation for IO")` as necessary.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BaseIO "Permalink")def
```


BaseIO (α : Type) : Type


BaseIO (α : Type) : Type


```

An `[IO](IO/Logical-Model/#IO "Documentation for IO")` monad that cannot throw exceptions.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO "Permalink")def
```


IO : Type → Type


IO : Type → Type


```

A monad that supports arbitrary side effects and throwing exceptions of type `[IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")`.
`[IO](IO/Logical-Model/#IO "Documentation for IO")` is an instance of `[EIO](IO/Logical-Model/#EIO "Documentation for EIO")`, in which the type of errors is a parameter. In particular, `[IO](IO/Logical-Model/#IO "Documentation for IO")` is defined as `[EIO](IO/Logical-Model/#EIO "Documentation for EIO") [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")`. In some circumstances, such as bindings to non-Lean libraries, it can be convenient to use `[EIO](IO/Logical-Model/#EIO "Documentation for EIO")` with a custom error type, which ensures that errors are handled at the boundaries between these and other `[IO](IO/Logical-Model/#IO "Documentation for IO")` actions.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EIO "Permalink")def
```


EIO (ε α : Type) : Type


EIO (ε α : Type) : Type


```

A monad that can have side effects on the external world or throw exceptions of type `ε`.
`[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` is a version of this monad that cannot throw exceptions. `[IO](IO/Logical-Model/#IO "Documentation for IO")` sets the exception type to `[IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.lazyPure "Permalink")def
```


IO.lazyPure {α : Type} (fn : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → α) : [IO](IO/Logical-Model/#IO "Documentation for IO") α


IO.lazyPure {α : Type} (fn : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → α) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") α


```

Creates an IO action that will invoke `fn` if and when it is executed, returning the result.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BaseIO.toIO "Permalink")def
```


BaseIO.toIO {α : Type} (act : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") α) : [IO](IO/Logical-Model/#IO "Documentation for IO") α


BaseIO.toIO {α : Type} (act : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") α) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") α


```

Runs a `[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` action, which cannot throw an exception, as an `[IO](IO/Logical-Model/#IO "Documentation for IO")` action.
This function is usually used implicitly via [automatic monadic lifting](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=lifting-monads) rather than being called explicitly.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=BaseIO.toEIO "Permalink")def
```


BaseIO.toEIO {α ε : Type} (act : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") α) : [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε α


BaseIO.toEIO {α ε : Type}
  (act : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") α) : [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε α


```

Runs a `[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` action, which cannot throw an exception, in any other `[EIO](IO/Logical-Model/#EIO "Documentation for EIO")` monad.
This function is usually used implicitly via [automatic monadic lifting](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=lifting-monads) rather being than called explicitly.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EIO.toBaseIO "Permalink")def
```


EIO.toBaseIO {ε α : Type} (act : [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε α) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α)


EIO.toBaseIO {ε α : Type}
  (act : [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε α) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α)


```

Converts an `[EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε` action that might throw an exception of type `ε` into an exception-free `[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` action that returns an `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except")` value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EIO.toIO "Permalink")def
```


EIO.toIO {ε α : Type} (f : ε → [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")) (act : [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε α) : [IO](IO/Logical-Model/#IO "Documentation for IO") α


EIO.toIO {ε α : Type} (f : ε → [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error"))
  (act : [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε α) : [IO](IO/Logical-Model/#IO "Documentation for IO") α


```

Converts an `[EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε` action into an `[IO](IO/Logical-Model/#IO "Documentation for IO")` action by translating any exceptions that it throws into `[IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")`s using `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EIO.toIO' "Permalink")def
```


EIO.toIO' {ε α : Type} (act : [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε α) : [IO](IO/Logical-Model/#IO "Documentation for IO") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α)


EIO.toIO' {ε α : Type} (act : [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε α) :
  [IO](IO/Logical-Model/#IO "Documentation for IO") ([Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α)


```

Converts an `[EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε` action that might throw an exception of type `ε` into an exception-free `[IO](IO/Logical-Model/#IO "Documentation for IO")` action that returns an `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except")` value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.toEIO "Permalink")def
```


IO.toEIO {ε α : Type} (f : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") → ε) (act : [IO](IO/Logical-Model/#IO "Documentation for IO") α) : [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε α


IO.toEIO {ε α : Type} (f : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") → ε)
  (act : [IO](IO/Logical-Model/#IO "Documentation for IO") α) : [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε α


```

Runs an `[IO](IO/Logical-Model/#IO "Documentation for IO")` action in some other `[EIO](IO/Logical-Model/#EIO "Documentation for EIO")` monad, using `f` to translate `[IO](IO/Logical-Model/#IO "Documentation for IO")` exceptions.
##  21.1.2. Errors and Error Handling in `IO`[🔗](find/?domain=Verso.Genre.Manual.section&name=io-monad-errors "Permalink")
Error handling in the `[IO](IO/Logical-Model/#IO "Documentation for IO")` monad uses the same facilities as any other [exception monad](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#--tech-term-Exception-monads). In particular, throwing and catching exceptions uses the methods of the `[MonadExceptOf](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExceptOf___mk "Documentation for MonadExceptOf")` [type class](Type-Classes/#--tech-term-type-class). The exceptions thrown in `[IO](IO/Logical-Model/#IO "Documentation for IO")` have the type `[IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")`. The constructors of this type represent the low-level errors that occur on most operating systems, such as files not existing. The most-used constructor is `[userError](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error.userError")`, which covers all other cases and includes a string that describes the problem.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Error.resourceExhausted "Permalink")inductive type
```


IO.Error : Type


IO.Error : Type


```

Exceptions that may be thrown in the `[IO](IO/Logical-Model/#IO "Documentation for IO")` monad.
Many of the constructors of `[IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")` correspond to POSIX error numbers. In these cases, the documentation string lists POSIX standard error macros that correspond to the error. This list is not necessarily exhaustive, and these constructor includes a field for the underlying error number.
#  Constructors

```
alreadyExists (filename : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (osCode : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32"))
  (details : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")
```

The operation failed because a file already exists.
This corresponds to POSIX errors `EEXIST`, `EINPROGRESS`, and `EISCONN`.

```
otherError (osCode : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) (details : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")
```

Some error not covered by the other constructors of `[IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")` occurred.
This also includes POSIX error `EFAULT`.

```
resourceBusy (osCode : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) (details : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")
```

A necessary resource was busy.
This corresponds to POSIX errors `EADDRINUSE`, `EBUSY`, `EDEADLK`, and `ETXTBSY`.

```
resourceVanished (osCode : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) (details : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")
```

A necessary resource is no longer available.
This corresponds to POSIX errors `ECONNRESET`, `EIDRM`, `ENETDOWN`, `ENETRESET`, `ENOLINK`, and `EPIPE`.

```
unsupportedOperation (osCode : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) (details : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")
```

An operation was not supported.
This corresponds to POSIX errors `EADDRNOTAVAIL`, `EAFNOSUPPORT`, `ENODEV`, `ENOPROTOOPT` `ENOSYS`, `EOPNOTSUPP`, `ERANGE`, `ESPIPE`, and `EXDEV`.

```
hardwareFault (osCode : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) (details : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")
```

The operation failed due to a hardware problem, such as an I/O error.
This corresponds to the POSIX error `[EIO](IO/Logical-Model/#EIO "Documentation for EIO")`.

```
unsatisfiedConstraints (osCode : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32"))
  (details : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")
```

A constraint required by an operation was not satisfied (e.g. a directory was not empty).
This corresponds to the POSIX error `ENOTEMPTY`.

```
illegalOperation (osCode : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) (details : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")
```

An inappropriate I/O control operation was attempted.
This corresponds to the POSIX error `ENOTTY`.

```
protocolError (osCode : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) (details : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")
```

A protocol error occurred.
This corresponds to the POSIX errors `EPROTO`, `EPROTONOSUPPORT`, and `EPROTOTYPE`.

```
timeExpired (osCode : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) (details : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")
```

An operation timed out.
This corresponds to the POSIX errors `ETIME`, and `ETIMEDOUT`.

```
interrupted (filename : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (osCode : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32"))
  (details : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")
```

The operation was interrupted.
This corresponds to the POSIX error `EINTR`.

```
noFileOrDirectory (filename : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (osCode : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32"))
  (details : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")
```

No such file or directory.
This corresponds to the POSIX error `ENOENT`.

```
invalidArgument (filename : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (osCode : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32"))
  (details : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")
```

An argument to an I/O operation was invalid.
This corresponds to the POSIX errors `ELOOP`, `ENAMETOOLONG`, `EDESTADDRREQ`, `EILSEQ`, `EINVAL`, `EDOM`, `EBADF` `ENOEXEC`, `ENOSTR`, `ENOTCONN`, and `ENOTSOCK`.

```
permissionDenied (filename : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (osCode : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) (details : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")
```

An operation failed due to insufficient permissions.
This corresponds to the POSIX errors `EACCES`, `EROFS`, `ECONNABORTED`, `EFBIG`, and `EPERM`.

```
resourceExhausted (filename : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (osCode : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) (details : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")
```

A resource was exhausted.
This corresponds to the POSIX errors `EMFILE`, `ENFILE`, `ENOSPC`, `E2BIG`, `EAGAIN`, `EMLINK`, `EMSGSIZE`, `ENOBUFS`, `ENOLCK`, `ENOMEM`, and `ENOSR`.

```
inappropriateType (filename : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (osCode : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) (details : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")
```

An argument was the wrong type (e.g. a directory when a file was required).
This corresponds to the POSIX errors `EISDIR`, `EBADMSG`, and `ENOTDIR`.

```
noSuchThing (filename : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (osCode : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32"))
  (details : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")
```

A required resource does not exist.
This corresponds to the POSIX errors `ENXIO`, `EHOSTUNREACH`, `ENETUNREACH`, `ECHILD`, `ECONNREFUSED`, `ENODATA`, `ENOMSG`, and `ESRCH`.

```
unexpectedEof : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")
```

An unexpected end-of-file marker was encountered.

```
userError (msg : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")
```

Some other error occurred.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.Error.toString "Permalink")def
```


IO.Error.toString : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


IO.Error.toString : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Converts an `[IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")` to a descriptive string.
`[IO.Error.userError](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error.userError")` is converted to its embedded message. The other constructors are converted in a way that preserves structured information, such as error codes and filenames, that can help diagnose the issue.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.ofExcept "Permalink")def
```


IO.ofExcept.{u_1} {ε : Type u_1} {α : Type} [ToString ε]
  (e : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α) : [IO](IO/Logical-Model/#IO "Documentation for IO") α


IO.ofExcept.{u_1} {ε : Type u_1}
  {α : Type} [ToString ε]
  (e : [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε α) : [IO](IO/Logical-Model/#IO "Documentation for IO") α


```

Converts an `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε` action into an `[IO](IO/Logical-Model/#IO "Documentation for IO")` action.
If the `[Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") ε` action throws an exception, then the exception type's `ToString` instance is used to convert it into an `[IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")`, which is thrown. Otherwise, the value is returned.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=EIO.catchExceptions "Permalink")def
```


EIO.catchExceptions {ε α : Type} (act : [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε α) (h : ε → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") α) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") α


EIO.catchExceptions {ε α : Type}
  (act : [EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε α) (h : ε → [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") α) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") α


```

Handles any exception that might be thrown by an `[EIO](IO/Logical-Model/#EIO "Documentation for EIO") ε` action, transforming it into an exception-free `[BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO")` action.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.userError "Permalink")def
```


IO.userError (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")


IO.userError (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")


```

Constructs an `[IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")` from a string.
`[IO.Error](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error")` is the type of exceptions thrown by the `[IO](IO/Logical-Model/#IO "Documentation for IO")` monad.
Throwing and Catching Errors
This program repeatedly demands a password, using exceptions for control flow. The syntax used for exceptions is available in all exception monads, not just `[IO](IO/Logical-Model/#IO "Documentation for IO")`. When an incorrect password is provided, an exception is thrown, which is caught by the loop that repeats the password check. A correct password allows control to proceed past the check, terminating the loop, and any other exceptions are re-thrown.
`def accessControl : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "What is the password?"   let password ← (← [IO.getStdin](IO/Files___-File-Handles___-and-Streams/#IO___getStdin "Documentation for IO.getStdin")).[getLine](IO/Files___-File-Handles___-and-Streams/#IO___FS___Stream___mk "Documentation for IO.FS.Stream.getLine")   if password.[trimAscii](Basic-Types/Strings/#String___trimAscii "Documentation for String.trimAscii").[copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy") != "secret" then     [throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") ([.userError](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error.userError") "Incorrect password")   else return  def repeatAccessControl : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   repeat     try       [accessControl](IO/Logical-Model/#accessControl-_LPAR_in-Throwing-and-Catching-Errors_RPAR_ "Definition of example")       break     catch       | [.userError](IO/Logical-Model/#IO___Error___alreadyExists "Documentation for IO.Error.userError") "Incorrect password" =>         continue       | other =>         [throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") other  def main : [IO](IO/Logical-Model/#IO "Documentation for IO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") := [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")   [repeatAccessControl](IO/Logical-Model/#repeatAccessControl-_LPAR_in-Throwing-and-Catching-Errors_RPAR_ "Definition of example")   [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") "Access granted!" `
When run with this input:
`stdin``publicinfo``secondtry``secret`
the program emits:
`stdout``What is the password?``What is the password?``What is the password?``Access granted!`
[←21. IO](IO/#io "21. IO")[21.2. Control Structures→](IO/Control-Structures/#io-monad-control "21.2. Control Structures")

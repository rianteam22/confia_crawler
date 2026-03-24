[←21.5. Files, File Handles, and Streams](IO/Files___-File-Handles___-and-Streams/#The-Lean-Language-Reference--IO--Files___-File-Handles___-and-Streams "21.5. Files, File Handles, and Streams")[21.7. Environment Variables→](IO/Environment-Variables/#io-monad-getenv "21.7. Environment Variables")
#  21.6. System and Platform Information[🔗](find/?domain=Verso.Genre.Manual.section&name=platform-info "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.Platform.numBits "Permalink")def
```


System.Platform.numBits : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


System.Platform.numBits : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The word size of the current platform, which may be 64 or 32 bits.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.Platform.target "Permalink")def
```


System.Platform.target : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


System.Platform.target : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

The LLVM target triple of the current platform. Empty if missing when Lean was compiled.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.Platform.isWindows "Permalink")def
```


System.Platform.isWindows : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


System.Platform.isWindows : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Is the current platform Windows?
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.Platform.isOSX "Permalink")def
```


System.Platform.isOSX : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


System.Platform.isOSX : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Is the current platform macOS?
[🔗](find/?domain=Verso.Genre.Manual.doc&name=System.Platform.isEmscripten "Permalink")def
```


System.Platform.isEmscripten : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


System.Platform.isEmscripten : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Is the current platform [Emscripten](https://emscripten.org/)?
[←21.5. Files, File Handles, and Streams](IO/Files___-File-Handles___-and-Streams/#The-Lean-Language-Reference--IO--Files___-File-Handles___-and-Streams "21.5. Files, File Handles, and Streams")[21.7. Environment Variables→](IO/Environment-Variables/#io-monad-getenv "21.7. Environment Variables")

[←21.6. System and Platform Information](IO/System-and-Platform-Information/#platform-info "21.6. System and Platform Information")[21.8. Timing→](IO/Timing/#io-timing "21.8. Timing")
#  21.7. Environment Variables[🔗](find/?domain=Verso.Genre.Manual.section&name=io-monad-getenv "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.getEnv "Permalink")opaque
```


IO.getEnv (var : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))


IO.getEnv (var : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))


```

Returns the value of the environment variable `var`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if it is not present in the environment.
[←21.6. System and Platform Information](IO/System-and-Platform-Information/#platform-info "21.6. System and Platform Information")[21.8. Timing→](IO/Timing/#io-timing "21.8. Timing")

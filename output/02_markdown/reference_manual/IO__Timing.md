[←21.7. Environment Variables](IO/Environment-Variables/#io-monad-getenv "21.7. Environment Variables")[21.9. Processes→](IO/Processes/#io-processes "21.9. Processes")
#  21.8. Timing[🔗](find/?domain=Verso.Genre.Manual.section&name=io-timing "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.sleep "Permalink")opaque
```


IO.sleep (ms : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.sleep (ms : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Pauses execution for the specified number of milliseconds.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.monoNanosNow "Permalink")opaque
```


IO.monoNanosNow : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


IO.monoNanosNow : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Monotonically increasing time since an unspecified past point in nanoseconds. There is no relation to wall clock time.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.monoMsNow "Permalink")opaque
```


IO.monoMsNow : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


IO.monoMsNow : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Monotonically increasing time since an unspecified past point in milliseconds. There is no relation to wall clock time.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.getNumHeartbeats "Permalink")opaque
```


IO.getNumHeartbeats : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


IO.getNumHeartbeats : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the number of _heartbeats_ that have occurred during the current thread's execution. The heartbeat count is the number of "small" memory allocations performed in a thread.
Heartbeats used to implement timeouts that are more deterministic across different hardware.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=IO.addHeartbeats "Permalink")def
```


IO.addHeartbeats (count : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


IO.addHeartbeats (count : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [BaseIO](IO/Logical-Model/#BaseIO "Documentation for BaseIO") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Adjusts the heartbeat counter of the current thread by the given amount. This can be useful to give allocation-avoiding code additional “weight” and is also used to adjust the counter after resuming from a snapshot.
Heartbeats are a means of implementing “deterministic” timeouts. The heartbeat counter is the number of “small” memory allocations performed on the current execution thread.
[←21.7. Environment Variables](IO/Environment-Variables/#io-monad-getenv "21.7. Environment Variables")[21.9. Processes→](IO/Processes/#io-processes "21.9. Processes")

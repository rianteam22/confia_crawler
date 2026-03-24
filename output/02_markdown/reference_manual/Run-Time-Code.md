[←11.5. Implementation Details](Coercions/Implementation-Details/#coercion-impl-details "11.5. Implementation Details")[12.1. Boxing→](Run-Time-Code/Boxing/#boxing "12.1. Boxing")
#  12. Run-Time Code[🔗](find/?domain=Verso.Genre.Manual.section&name=runtime "Permalink")
Compiled Lean code uses services provided by the Lean runtime. The runtime contains efficient, low-level primitives that bridge the gap between the Lean language and the supported platforms. These services include: 

Memory management
    
Lean does not require programmers to manually manage memory. Space is allocated when needed to store a value, and values that can no longer be reached (and are thus irrelevant) are deallocated. In particular, Lean uses [reference counting](Run-Time-Code/Reference-Counting/#--tech-term-reference-counting), where each allocated object maintains a count of incoming references. The compiler emits calls to memory management routines that allocate memory and modify reference counts, and these routines are provided by the runtime, along with the data structures that represent Lean values in compiled code. 

Multiple Threads
    
The `[Task](IO/Tasks-and-Threads/#Task "Documentation for Task")` API provides the ability to write parallel and concurrent code. The runtime is responsible for scheduling Lean tasks across operating-system threads. 

Primitive operators
    
Many built-in types, including `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")`, `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`, and fixed-width integers, have special representations for reasons of efficiency. The runtime provides implementations of these types' primitive operators that take advantage of these optimized representations.
There are many primitive operators. They are described in their respective sections under [Basic Types](Basic-Types/#basic-types).
  1. [12.1. Boxing](Run-Time-Code/Boxing/#boxing)
  2. [12.2. Reference Counting](Run-Time-Code/Reference-Counting/#reference-counting)
  3. [12.3. Multi-Threaded Execution](Run-Time-Code/Multi-Threaded-Execution/#The-Lean-Language-Reference--Run-Time-Code--Multi-Threaded-Execution)
  4. [12.4. Foreign Function Interface](Run-Time-Code/Foreign-Function-Interface/#ffi)

[←11.5. Implementation Details](Coercions/Implementation-Details/#coercion-impl-details "11.5. Implementation Details")[12.1. Boxing→](Run-Time-Code/Boxing/#boxing "12.1. Boxing")

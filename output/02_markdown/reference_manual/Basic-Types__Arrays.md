[←20.15. Linked Lists](Basic-Types/Linked-Lists/#List "20.15. Linked Lists")[20.17. Byte Arrays→](Basic-Types/Byte-Arrays/#ByteArray "20.17. Byte Arrays")
#  20.16. Arrays[🔗](find/?domain=Verso.Genre.Manual.section&name=Array "Permalink")
The `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")` type represents sequences of elements, addressable by their position in the sequence. Arrays are specially supported by Lean:
  * They have a _logical model_ that specifies their behavior in terms of lists of elements, which specifies the meaning of each operation on arrays.
  * They have an optimized run-time representation in compiled code as [dynamic arrays](Basic-Types/Arrays/#--tech-term-dynamic-arrays), and the Lean runtime specially optimizes array operations.
  * There is [array literal syntax](Basic-Types/Arrays/#array-syntax) for writing arrays.


Arrays can be vastly more efficient than lists or other sequences in compiled code. In part, this is because they offer good locality: because all the elements of the sequence are next to each other in memory, the processor's caches can be used efficiently. Even more importantly, if there is only a single reference to an array, operations that might otherwise copy or allocate a data structure can be implemented via mutation. Lean code that uses an array in such a way that there's only ever one unique reference (that is, uses it _linearly_) avoids the performance overhead of persistent data structures while still being as convenient to write, read, and prove things about as ordinary pure functional programs.
##  20.16.1. Logical Model[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--Logical-Model "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array "Permalink")structure
```


Array.{u} (α : Type u) : Type u


Array.{u} (α : Type u) : Type u


```

`[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α` is the type of [dynamic arrays](https://en.wikipedia.org/wiki/Dynamic_array) with elements from `α`. This type has special support in the runtime.
Arrays perform best when unshared. As long as there is never more than one reference to an array, all updates will be performed _destructively_. This results in performance comparable to mutable arrays in imperative programming languages.
An array has a size and a capacity. The size is the number of elements present in the array, while the capacity is the amount of memory currently allocated for elements. The size is accessible via `[Array.size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")`, but the capacity is not observable from Lean code. `[Array.emptyWithCapacity](Basic-Types/Arrays/#Array___emptyWithCapacity "Documentation for Array.emptyWithCapacity") n` creates an array which is equal to `#[]`, but internally allocates an array of capacity `n`. When the size exceeds the capacity, allocation is required to grow the array.
From the point of view of proofs, `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α` is just a wrapper around `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α`.
#  Constructor

```
[Array.mk](Basic-Types/Arrays/#Array___mk "Documentation for Array.mk").{u}
```

Converts a `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` into an `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α`.
The function `[List.toArray](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")` is preferred.
At runtime, this constructor is overridden by `[List.toArrayImpl](Basic-Types/Linked-Lists/#List___toArrayImpl "Documentation for List.toArrayImpl")` and is `O(n)` in the length of the list.
#  Fields

```
toList : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α
```

Converts an `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α` into a `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` that contains the same elements in the same order.
At runtime, this is implemented by `Array.toListImpl` and is `O(n)` in the length of the array.
The logical model of arrays is a structure that contains a single field, which is a list of elements. This is convenient when specifying and proving properties of array-processing functions at a low level.
##  20.16.2. Run-Time Representation[🔗](find/?domain=Verso.Genre.Manual.section&name=array-runtime "Permalink")
Lean's arrays are _dynamic arrays_ , which are blocks of continuous memory with a defined capacity, not all of which is typically in use. As long as the number of elements in the array is less than the capacity, new items can be added to the end without reallocating or moving the data. Adding items to an array that has no extra space results in a reallocation that doubles the capacity. The amortized overhead scales linearly with the size of the array. The values in the array are represented as described in the [section on the foreign function interface](The-Type-System/Inductive-Types/#inductive-types-ffi).
Memory layout of arrays
After the object header, an array contains: 

size
    
The number of objects currently stored in the array 

capacity
    
The number of objects that fit in the memory allocated for the array 

data
    
The values in the array
Many array functions in the Lean runtime check whether they have exclusive access to their argument by consulting the reference count in the object header. If they do, and the array's capacity is sufficient, then the existing array can be mutated rather than allocating fresh memory. Otherwise, a new array must be allocated.
###  20.16.2.1. Performance Notes[🔗](find/?domain=Verso.Genre.Manual.section&name=array-performance "Permalink")
Despite the fact that they appear to be an ordinary constructor and projection, `[Array.mk](Basic-Types/Arrays/#Array___mk "Documentation for Array.mk")` and `Array.toList` take **time linear in the size of the array** in compiled code. This is because converting between linked lists and packed arrays must necessarily visit each element.
Mutable arrays can be used to write very efficient code. However, they are a poor persistent data structure. Updating a shared array rules out mutation, and requires time linear in the size of the array. When using arrays in performance-critical code, it's important to ensure that they are used [linearly](Basic-Types/Arrays/#--tech-term-linearly).
##  20.16.3. Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=array-syntax "Permalink")
Array literals allow arrays to be written directly in code. They may be used in expression or pattern contexts.
syntaxArray Literals
Array literals begin with `#[` and contain a comma-separated sequence of terms, terminating with `]`.

```
term ::= ...
    | 


Syntax for Array α. 


Conventions for notations in identifiers:




  * 

The recommended spelling of #[] in identifiers is empty.




  * 

The recommended spelling of #[x] in identifiers is singleton.






#[term,*]
```

Array Literals
Array literals may be used as expressions or as patterns.
`def oneTwoThree : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := #[1, 2, 3]  `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") [oneTwoThree](Basic-Types/Arrays/#oneTwoThree-_LPAR_in-Array-Literals_RPAR_ "Definition of example") [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") | #[x, y, z] => [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ((x + z) / y) | _ => [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") `
[Live ↪](javascript:openLiveLink\("CYUwZgBA9gdiAqB3K8AWAnEIIC4IEF10BDATwgDliAXXAXggGIBtARgBoIAmTgZgF0AUIMYgAbsQA2giBAC2NAMapocJCgxYIiAJbVUMiAB8mzAB6dSnAF78IdAHwQAzlDnYAFB7MQA1BGsASggAeghSQMMTAH17JxhYECA"\))
Additionally, [sub-arrays](Basic-Types/Arrays/#subarray) may be extracted using the following syntax:
syntaxSub-Arrays
A start index followed by a colon constructs a sub-array that contains the values from the start index onwards (inclusive):

```
term ::= ...
    | 


A subarray with the provided lower bound that extends to the rest of the array. 


term[term :]
```

Providing start and end indices constructs a sub-array that contains the values from the start index (inclusive) to the end index (exclusive):

```
term ::= ...
    | 


A subarray with the provided bounds.


term[term : term]
```

Sub-Array Syntax
The array `[ten](Basic-Types/Arrays/#ten-_LPAR_in-Sub-Array-Syntax_RPAR_ "Definition of example")` contains the first ten natural numbers.
`def ten : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") :=   [.range](Basic-Types/Arrays/#Array___range "Documentation for Array.range") 10 `
A sub-array that represents the second half of `[ten](Basic-Types/Arrays/#ten-_LPAR_in-Sub-Array-Syntax_RPAR_ "Definition of example")` can be constructed using the sub-array syntax:
``#[5, 6, 7, 8, 9].toSubarray`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [ten](Basic-Types/Arrays/#ten-_LPAR_in-Sub-Array-Syntax_RPAR_ "Definition of example")[5:] `
```
#[5, 6, 7, 8, 9].toSubarray
```

Similarly, sub-array that contains two through five can be constructed by providing a stopping point:
``#[2, 3, 4, 5].toSubarray`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [ten](Basic-Types/Arrays/#ten-_LPAR_in-Sub-Array-Syntax_RPAR_ "Definition of example")[2:6] `
```
#[2, 3, 4, 5].toSubarray
```

Because sub-arrays merely store the start and end indices of interest in the underlying array, the array itself can be recovered:
``[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [ten](Basic-Types/Arrays/#ten-_LPAR_in-Sub-Array-Syntax_RPAR_ "Definition of example")[2:6].[array](Basic-Types/Arrays/#Subarray___array "Documentation for Subarray.array") == [ten](Basic-Types/Arrays/#ten-_LPAR_in-Sub-Array-Syntax_RPAR_ "Definition of example") `
```
[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")
```

[Live ↪](javascript:openLiveLink\("CYUwZgBALiB2EC4IEEBOqCGBPCA5DUiAvAFAQQB0msA5iBAIwAMJJAxCAG4YA20cAbQCsCALqsO3PjFgCATAgBs49l179ZC5RQzpsEIkQ1A"\))
##  20.16.4. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=array-api "Permalink")
###  20.16.4.1. Constructing Arrays[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--API-Reference--Constructing-Arrays "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.empty "Permalink")def
```


Array.empty.{u} {α : Type u} : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.empty.{u} {α : Type u} : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Constructs a new empty array with initial capacity `0`.
Use `[Array.emptyWithCapacity](Basic-Types/Arrays/#Array___emptyWithCapacity "Documentation for Array.emptyWithCapacity")` to create an array with a greater initial capacity.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.emptyWithCapacity "Permalink")def
```


Array.emptyWithCapacity.{u} {α : Type u} (c : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.emptyWithCapacity.{u} {α : Type u}
  (c : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Constructs a new empty array with initial capacity `c`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.singleton "Permalink")def
```


Array.singleton.{u} {α : Type u} (v : α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.singleton.{u} {α : Type u} (v : α) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Constructs a single-element array that contains `v`.
Examples:
  * `[Array.singleton](Basic-Types/Arrays/#Array___singleton "Documentation for Array.singleton") 5 = #[5]`
  * `[Array.singleton](Basic-Types/Arrays/#Array___singleton "Documentation for Array.singleton") "one" = #["one"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.range "Permalink")def
```


Array.range (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Array.range (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Constructs an array that contains all the numbers from `0` to `n`, exclusive.
Examples:
  * `Array.range 5 := #[0, 1, 2, 3, 4]`
  * `Array.range 0 := #[]`
  * `Array.range 1 := #[0]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.range' "Permalink")def
```


Array.range' (start size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (step : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 1) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Array.range' (start size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (step : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 1) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Constructs an array of numbers of size `size`, starting at `start` and increasing by `step` at each element.
In other words, `[Array.range'](Basic-Types/Arrays/#Array___range___ "Documentation for Array.range'") start size step` is `#[start, start+step, ..., start+(len-1)*step]`.
Examples:
  * `[Array.range'](Basic-Types/Arrays/#Array___range___ "Documentation for Array.range'") 0 3 (step := 1) = #[0, 1, 2]`
  * `[Array.range'](Basic-Types/Arrays/#Array___range___ "Documentation for Array.range'") 0 3 (step := 2) = #[0, 2, 4]`
  * `[Array.range'](Basic-Types/Arrays/#Array___range___ "Documentation for Array.range'") 0 4 (step := 2) = #[0, 2, 4, 6]`
  * `[Array.range'](Basic-Types/Arrays/#Array___range___ "Documentation for Array.range'") 3 4 (step := 2) = #[3, 5, 7, 9]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.finRange "Permalink")def
```


Array.finRange (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n)


Array.finRange (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n)


```

Returns an array of all elements of `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n` in order, starting at `0`.
Examples:
  * `[Array.finRange](Basic-Types/Arrays/#Array___finRange "Documentation for Array.finRange") 0 = (#[] : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 0))`
  * `[Array.finRange](Basic-Types/Arrays/#Array___finRange "Documentation for Array.finRange") 2 = (#[0, 1] : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 2))`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.ofFn "Permalink")def
```


Array.ofFn.{u} {α : Type u} {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} (f : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.ofFn.{u} {α : Type u} {n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")}
  (f : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") n → α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Creates an array by applying `f` to each potential index in order, starting at `0`.
Examples:
  * `[Array.ofFn](Basic-Types/Arrays/#Array___ofFn "Documentation for Array.ofFn") (n := 3) toString = #["0", "1", "2"]`
  * `[Array.ofFn](Basic-Types/Arrays/#Array___ofFn "Documentation for Array.ofFn") (fun i => #["red", "green", "blue"].get i.val i.isLt) = #["red", "green", "blue"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.replicate "Permalink")def
```


Array.replicate.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (v : α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.replicate.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (v : α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Creates an array that contains `n` repetitions of `v`.
The corresponding `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List")` function is `[List.replicate](Basic-Types/Linked-Lists/#List___replicate "Documentation for List.replicate")`.
Examples:
  * `[Array.replicate](Basic-Types/Arrays/#Array___replicate "Documentation for Array.replicate") 2 [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") = #[[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true"), [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")]`
  * `[Array.replicate](Basic-Types/Arrays/#Array___replicate "Documentation for Array.replicate") 3 () = #[(), (), ()]`
  * `[Array.replicate](Basic-Types/Arrays/#Array___replicate "Documentation for Array.replicate") 0 "anything" = #[]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.append "Permalink")def
```


Array.append.{u} {α : Type u} (as bs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.append.{u} {α : Type u}
  (as bs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Appends two arrays. Normally used via the `++` operator.
Appending arrays takes time proportional to the length of the second array.
Examples:
  * `#[1, 2, 3] ++ #[4, 5] = #[1, 2, 3, 4, 5]`.
  * `#[] ++ #[4, 5] = #[4, 5]`.
  * `#[1, 2, 3] ++ #[] = #[1, 2, 3]`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.appendList "Permalink")def
```


Array.appendList.{u} {α : Type u} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.appendList.{u} {α : Type u}
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (bs : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Appends an array and a list.
Takes time proportional to the length of the list..
Examples:
  * `#[1, 2, 3].[appendList](Basic-Types/Arrays/#Array___appendList "Documentation for Array.appendList") [4, 5] = #[1, 2, 3, 4, 5]`.
  * `#[].[appendList](Basic-Types/Arrays/#Array___appendList "Documentation for Array.appendList") [4, 5] = #[4, 5]`.
  * `#[1, 2, 3].[appendList](Basic-Types/Arrays/#Array___appendList "Documentation for Array.appendList") [] = #[1, 2, 3]`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.leftpad "Permalink")def
```


Array.leftpad.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.leftpad.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (a : α) (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Pads `xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α` on the left with repeated occurrences of `a : α` until it is of size `n`. If `xs` already has at least `n` elements, it is returned unmodified.
Examples:
  * `#[1, 2, 3].[leftpad](Basic-Types/Arrays/#Array___leftpad "Documentation for Array.leftpad") 5 0 = #[0, 0, 1, 2, 3]`
  * `#["red", "green", "blue"].[leftpad](Basic-Types/Arrays/#Array___leftpad "Documentation for Array.leftpad") 4 "blank" = #["blank", "red", "green", "blue"]`
  * `#["red", "green", "blue"].[leftpad](Basic-Types/Arrays/#Array___leftpad "Documentation for Array.leftpad") 3 "blank" = #["red", "green", "blue"]`
  * `#["red", "green", "blue"].[leftpad](Basic-Types/Arrays/#Array___leftpad "Documentation for Array.leftpad") 1 "blank" = #["red", "green", "blue"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.rightpad "Permalink")def
```


Array.rightpad.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.rightpad.{u} {α : Type u} (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (a : α) (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Pads `xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α` on the right with repeated occurrences of `a : α` until it is of length `n`. If `l` already has at least `n` elements, it is returned unmodified.
Examples:
  * `#[1, 2, 3].[rightpad](Basic-Types/Arrays/#Array___rightpad "Documentation for Array.rightpad") 5 0 = #[1, 2, 3, 0, 0]`
  * `#["red", "green", "blue"].[rightpad](Basic-Types/Arrays/#Array___rightpad "Documentation for Array.rightpad") 4 "blank" = #["red", "green", "blue", "blank"]`
  * `#["red", "green", "blue"].[rightpad](Basic-Types/Arrays/#Array___rightpad "Documentation for Array.rightpad") 3 "blank" = #["red", "green", "blue"]`
  * `#["red", "green", "blue"].[rightpad](Basic-Types/Arrays/#Array___rightpad "Documentation for Array.rightpad") 1 "blank" = #["red", "green", "blue"]`


###  20.16.4.2. Size[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--API-Reference--Size "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.size "Permalink")def
```


Array.size.{u} {α : Type u} (a : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Array.size.{u} {α : Type u}
  (a : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Gets the number of elements stored in an array.
This is a cached value, so it is `O(1)` to access. The space allocated for an array, referred to as its _capacity_ , is at least as large as its size, but may be larger. The capacity of an array is an internal detail that's not observable by Lean code.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.usize "Permalink")def
```


Array.usize.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


Array.usize.{u} {α : Type u}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Returns the size of the array as a platform-native unsigned integer.
This is a low-level version of `[Array.size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")` that directly queries the runtime system's representation of arrays. While this is not provable, `[Array.usize](Basic-Types/Arrays/#Array___usize "Documentation for Array.usize")` always returns the exact size of the array since the implementation only supports arrays of size less than `[USize.size](Basic-Types/Fixed-Precision-Integers/#USize___size "Documentation for USize.size")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.isEmpty "Permalink")def
```


Array.isEmpty.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Array.isEmpty.{u} {α : Type u}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether an array is empty.
An array is empty if its size is `0`.
Examples:
  * `(#[] : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")).[isEmpty](Basic-Types/Arrays/#Array___isEmpty "Documentation for Array.isEmpty") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `#[1, 2].[isEmpty](Basic-Types/Arrays/#Array___isEmpty "Documentation for Array.isEmpty") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `#[()].[isEmpty](Basic-Types/Arrays/#Array___isEmpty "Documentation for Array.isEmpty") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


###  20.16.4.3. Lookups[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--API-Reference--Lookups "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.extract "Permalink")def
```


Array.extract.{u_1} {α : Type u_1} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.extract.{u_1} {α : Type u_1}
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Returns the slice of `as` from indices `start` to `stop` (exclusive). The resulting array has size `([min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min.min") stop as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) - start`.
If `start` is greater or equal to `stop`, the result is empty. If `stop` is greater than the size of `as`, the size is used instead.
Examples:
  * `#[0, 1, 2, 3, 4].[extract](Basic-Types/Arrays/#Array___extract "Documentation for Array.extract") 1 3 = #[1, 2]`
  * `#[0, 1, 2, 3, 4].[extract](Basic-Types/Arrays/#Array___extract "Documentation for Array.extract") 1 30 = #[1, 2, 3, 4]`
  * `#[0, 1, 2, 3, 4].[extract](Basic-Types/Arrays/#Array___extract "Documentation for Array.extract") 0 0 = #[]`
  * `#[0, 1, 2, 3, 4].[extract](Basic-Types/Arrays/#Array___extract "Documentation for Array.extract") 2 1 = #[]`
  * `#[0, 1, 2, 3, 4].[extract](Basic-Types/Arrays/#Array___extract "Documentation for Array.extract") 2 2 = #[]`
  * `#[0, 1, 2, 3, 4].[extract](Basic-Types/Arrays/#Array___extract "Documentation for Array.extract") 2 3 = #[2]`
  * `#[0, 1, 2, 3, 4].[extract](Basic-Types/Arrays/#Array___extract "Documentation for Array.extract") 2 4 = #[2, 3]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.getD "Permalink")def
```


Array.getD.{u_1} {α : Type u_1} (a : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (v₀ : α) : α


Array.getD.{u_1} {α : Type u_1}
  (a : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (v₀ : α) : α


```

Returns the element at the provided index, counting from `0`. Returns the fallback value `v₀` if the index is out of bounds.
To return an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` depending on whether the index is in bounds, use `a[i]?`. To panic if the index is out of bounds, use `a[i]!`.
Examples:
  * `#["spring", "summer", "fall", "winter"].[getD](Basic-Types/Arrays/#Array___getD "Documentation for Array.getD") 2 "never" = "fall"`
  * `#["spring", "summer", "fall", "winter"].[getD](Basic-Types/Arrays/#Array___getD "Documentation for Array.getD") 0 "never" = "spring"`
  * `#["spring", "summer", "fall", "winter"].[getD](Basic-Types/Arrays/#Array___getD "Documentation for Array.getD") 4 "never" = "never"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.uget "Permalink")def
```


Array.uget.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize"))
  (h : i.[toNat](Basic-Types/Fixed-Precision-Integers/#USize___toNat "Documentation for USize.toNat") [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : α


Array.uget.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (i : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) (h : i.[toNat](Basic-Types/Fixed-Precision-Integers/#USize___toNat "Documentation for USize.toNat") [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : α


```

Low-level indexing operator which is as fast as a C array read.
This avoids overhead due to unboxing a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` used as an index.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.back "Permalink")def
```


Array.back.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (h : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") := by get_elem_tactic) : α


Array.back.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (h : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") := by
    get_elem_tactic) :
  α


```

Returns the last element of an array, given a proof that the array is not empty.
See `[Array.back!](Basic-Types/Arrays/#Array___back___-next "Documentation for Array.back!")` for the version that panics if the array is empty, or `[Array.back?](Basic-Types/Arrays/#Array___back___ "Documentation for Array.back?")` for the version that returns an option.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.back? "Permalink")def
```


Array.back?.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Array.back?.{u} {α : Type u}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Returns the last element of an array, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the array is empty.
See `[Array.back!](Basic-Types/Arrays/#Array___back___-next "Documentation for Array.back!")` for the version that panics if the array is empty, or `[Array.back](Basic-Types/Arrays/#Array___back "Documentation for Array.back")` for the version that requires a proof the array is non-empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.back! "Permalink")def
```


Array.back!.{u} {α : Type u} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : α


Array.back!.{u} {α : Type u} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : α


```

Returns the last element of an array, or panics if the array is empty.
Safer alternatives include `[Array.back](Basic-Types/Arrays/#Array___back "Documentation for Array.back")`, which requires a proof the array is non-empty, and `[Array.back?](Basic-Types/Arrays/#Array___back___ "Documentation for Array.back?")`, which returns an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.getMax? "Permalink")def
```


Array.getMax?.{u} {α : Type u} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (lt : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Array.getMax?.{u} {α : Type u}
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (lt : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Returns the largest element of the array, as determined by the comparison `lt`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the array is empty.
Examples:
  * `(#[] : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")).[getMax?](Basic-Types/Arrays/#Array___getMax___ "Documentation for Array.getMax?") (· < ·) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `#["red", "green", "blue"].[getMax?](Basic-Types/Arrays/#Array___getMax___ "Documentation for Array.getMax?") (·.[length](Basic-Types/Strings/#String___length "Documentation for String.length") < ·.[length](Basic-Types/Strings/#String___length "Documentation for String.length")) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "green"`
  * `#["red", "green", "blue"].[getMax?](Basic-Types/Arrays/#Array___getMax___ "Documentation for Array.getMax?") (· < ·) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "red"`


###  20.16.4.4. Queries[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--API-Reference--Queries "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.count "Permalink")def
```


Array.count.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (a : α) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Array.count.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (a : α) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Counts the number of times an element occurs in an array.
Examples:
  * `#[1, 1, 2, 3, 5].[count](Basic-Types/Arrays/#Array___count "Documentation for Array.count") 1 = 2`
  * `#[1, 1, 2, 3, 5].[count](Basic-Types/Arrays/#Array___count "Documentation for Array.count") 5 = 1`
  * `#[1, 1, 2, 3, 5].[count](Basic-Types/Arrays/#Array___count "Documentation for Array.count") 4 = 0`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.countP "Permalink")def
```


Array.countP.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Array.countP.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Counts the number of elements in the array `as` that satisfy the Boolean predicate `p`.
Examples:
  * `#[1, 2, 3, 4, 5].[countP](Basic-Types/Arrays/#Array___countP "Documentation for Array.countP") (· % 2 == 0) = 2`
  * `#[1, 2, 3, 4, 5].[countP](Basic-Types/Arrays/#Array___countP "Documentation for Array.countP") (· < 5) = 4`
  * `#[1, 2, 3, 4, 5].[countP](Basic-Types/Arrays/#Array___countP "Documentation for Array.countP") (· > 5) = 0`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.idxOf "Permalink")def
```


Array.idxOf.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (a : α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Array.idxOf.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (a : α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the index of the first element equal to `a`, or the size of the array if no element is equal to `a`.
Examples:
  * `#["carrot", "potato", "broccoli"].[idxOf](Basic-Types/Arrays/#Array___idxOf "Documentation for Array.idxOf") "carrot" = 0`
  * `#["carrot", "potato", "broccoli"].[idxOf](Basic-Types/Arrays/#Array___idxOf "Documentation for Array.idxOf") "broccoli" = 2`
  * `#["carrot", "potato", "broccoli"].[idxOf](Basic-Types/Arrays/#Array___idxOf "Documentation for Array.idxOf") "tomato" = 3`
  * `#["carrot", "potato", "broccoli"].[idxOf](Basic-Types/Arrays/#Array___idxOf "Documentation for Array.idxOf") "anything else" = 3`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.idxOf? "Permalink")def
```


Array.idxOf?.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (v : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Array.idxOf?.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (v : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the index of the first element equal to `a`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no element is equal to `a`.
Examples:
  * `#["carrot", "potato", "broccoli"].[idxOf?](Basic-Types/Arrays/#Array___idxOf___ "Documentation for Array.idxOf?") "carrot" = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 0`
  * `#["carrot", "potato", "broccoli"].[idxOf?](Basic-Types/Arrays/#Array___idxOf___ "Documentation for Array.idxOf?") "broccoli" = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2`
  * `#["carrot", "potato", "broccoli"].[idxOf?](Basic-Types/Arrays/#Array___idxOf___ "Documentation for Array.idxOf?") "tomato" = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `#["carrot", "potato", "broccoli"].[idxOf?](Basic-Types/Arrays/#Array___idxOf___ "Documentation for Array.idxOf?") "anything else" = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.finIdxOf? "Permalink")def
```


Array.finIdxOf?.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (v : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size"))


Array.finIdxOf?.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (v : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size"))


```

Returns the index of the first element equal to `a`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no element is equal to `a`. The index is returned as a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")`, which guarantees that it is in bounds.
Examples:
  * `#["carrot", "potato", "broccoli"].[finIdxOf?](Basic-Types/Arrays/#Array___finIdxOf___ "Documentation for Array.finIdxOf?") "carrot" = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 0`
  * `#["carrot", "potato", "broccoli"].[finIdxOf?](Basic-Types/Arrays/#Array___finIdxOf___ "Documentation for Array.finIdxOf?") "broccoli" = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2`
  * `#["carrot", "potato", "broccoli"].[finIdxOf?](Basic-Types/Arrays/#Array___finIdxOf___ "Documentation for Array.finIdxOf?") "tomato" = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `#["carrot", "potato", "broccoli"].[finIdxOf?](Basic-Types/Arrays/#Array___finIdxOf___ "Documentation for Array.finIdxOf?") "anything else" = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


###  20.16.4.5. Conversions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--API-Reference--Conversions "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.toList "Permalink")def
```


Array.toList.{u} {α : Type u} (self : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


Array.toList.{u} {α : Type u}
  (self : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Converts an `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α` into a `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` that contains the same elements in the same order.
At runtime, this is implemented by `Array.toListImpl` and is `O(n)` in the length of the array.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.toListRev "Permalink")def
```


Array.toListRev.{u_1} {α : Type u_1} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


Array.toListRev.{u_1} {α : Type u_1}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Converts an array to a list that contains the same elements in the opposite order.
This is equivalent to, but more efficient than, `Array.toList ∘ List.reverse`.
Examples:
  * `#[1, 2, 3].[toListRev](Basic-Types/Arrays/#Array___toListRev "Documentation for Array.toListRev") = [3, 2, 1]`
  * `#["blue", "yellow"].[toListRev](Basic-Types/Arrays/#Array___toListRev "Documentation for Array.toListRev") = ["yellow", "blue"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.toListAppend "Permalink")def
```


Array.toListAppend.{u} {α : Type u} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


Array.toListAppend.{u} {α : Type u}
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Prepends an array to a list. The elements of the array are at the beginning of the resulting list.
Equivalent to `as.toList ++ l`.
Examples:
  * `#[1, 2].[toListAppend](Basic-Types/Arrays/#Array___toListAppend "Documentation for Array.toListAppend") [3, 4] = [1, 2, 3, 4]`
  * `#[1, 2].[toListAppend](Basic-Types/Arrays/#Array___toListAppend "Documentation for Array.toListAppend") [] = [1, 2]`
  * `#[].[toListAppend](Basic-Types/Arrays/#Array___toListAppend "Documentation for Array.toListAppend") [3, 4, 5] = [3, 4, 5]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.toVector "Permalink")def
```


Array.toVector.{u_1} {α : Type u_1} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : Vector α xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")


Array.toVector.{u_1} {α : Type u_1}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : Vector α xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")


```

Converts an array to a vector. The resulting vector's size is the array's size.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.toSubarray "Permalink")def
```


Array.toSubarray.{u} {α : Type u} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α


Array.toSubarray.{u} {α : Type u}
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α


```

Returns a subarray of an array, with the given bounds.
If `start` or `stop` are not valid bounds for a subarray, then they are clamped to array's size. Additionally, the starting index is clamped to the ending index.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.ofSubarray "Permalink")def
```


Array.ofSubarray.{u} {α : Type u} (s : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.ofSubarray.{u} {α : Type u}
  (s : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Allocates a new array that contains the contents of the subarray.
###  20.16.4.6. Modification[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--API-Reference--Modification "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.push "Permalink")def
```


Array.push.{u} {α : Type u} (a : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (v : α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.push.{u} {α : Type u} (a : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (v : α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Adds an element to the end of an array. The resulting array's size is one greater than the input array. If there are no other references to the array, then it is modified in-place.
This takes amortized `O(1)` time because `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α` is represented by a dynamic array.
Examples:
  * `#[].[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") "apple" = #["apple"]`
  * `#["apple"].[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") "orange" = #["apple", "orange"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.pop "Permalink")def
```


Array.pop.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.pop.{u} {α : Type u}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Removes the last element of an array. If the array is empty, then it is returned unmodified. The modification is performed in-place when the reference to the array is unique.
Examples:
  * `#[1, 2, 3].[pop](Basic-Types/Arrays/#Array___pop "Documentation for Array.pop") = #[1, 2]`
  * `#["orange", "yellow"].[pop](Basic-Types/Arrays/#Array___pop "Documentation for Array.pop") = #["orange"]`
  * `(#[] : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")).[pop](Basic-Types/Arrays/#Array___pop "Documentation for Array.pop") = #[]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.popWhile "Permalink")def
```


Array.popWhile.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.popWhile.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Removes all the elements that satisfy a predicate from the end of an array.
The longest contiguous sequence of elements that all satisfy the predicate is removed.
Examples:
  * `#[0, 1, 2, 3, 4].[popWhile](Basic-Types/Arrays/#Array___popWhile "Documentation for Array.popWhile") (· > 2) = #[0, 1, 2]`
  * `#[3, 2, 3, 4].[popWhile](Basic-Types/Arrays/#Array___popWhile "Documentation for Array.popWhile") (· > 2) = #[3, 2]`
  * `(#[] : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")).[popWhile](Basic-Types/Arrays/#Array___popWhile "Documentation for Array.popWhile") (· > 2) = #[]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.erase "Permalink")def
```


Array.erase.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (a : α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.erase.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (a : α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Removes the first occurrence of a specified element from an array, or does nothing if it is not present.
This function takes worst-case `O(n)` time because it back-shifts all later elements.
Examples:
  * `#[1, 2, 3].[erase](Basic-Types/Arrays/#Array___erase "Documentation for Array.erase") 2 = #[1, 3]`
  * `#[1, 2, 3].[erase](Basic-Types/Arrays/#Array___erase "Documentation for Array.erase") 5 = #[1, 2, 3]`
  * `#[1, 2, 3, 2, 1].[erase](Basic-Types/Arrays/#Array___erase "Documentation for Array.erase") 2 = #[1, 3, 2, 1]`
  * `(#[] : List Nat).erase 2 = #[]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.eraseP "Permalink")def
```


Array.eraseP.{u} {α : Type u} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.eraseP.{u} {α : Type u}
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Removes the first element that satisfies the predicate `p`. If no element satisfies `p`, the array is returned unmodified.
This function takes worst-case `O(n)` time because it back-shifts all later elements.
Examples:
  * `#["red", "green", "", "blue"].[eraseP](Basic-Types/Arrays/#Array___eraseP "Documentation for Array.eraseP") (·.[isEmpty](Basic-Types/Strings/#String___isEmpty "Documentation for String.isEmpty")) = #["red", "green", "blue"]`
  * `#["red", "green", "", "blue", ""].[eraseP](Basic-Types/Arrays/#Array___eraseP "Documentation for Array.eraseP") (·.[isEmpty](Basic-Types/Strings/#String___isEmpty "Documentation for String.isEmpty")) = #["red", "green", "blue", ""]`
  * `#["red", "green", "blue"].[eraseP](Basic-Types/Arrays/#Array___eraseP "Documentation for Array.eraseP") (·.[length](Basic-Types/Strings/#String___length "Documentation for String.length") % 2 == 0) = #["red", "green"]`
  * `#["red", "green", "blue"].[eraseP](Basic-Types/Arrays/#Array___eraseP "Documentation for Array.eraseP") (fun _ => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) = #["green", "blue"]`
  * `(#[] : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")).[eraseP](Basic-Types/Arrays/#Array___eraseP "Documentation for Array.eraseP") (fun _ => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) = #[]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.eraseIdx "Permalink")def
```


Array.eraseIdx.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (h : i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") := by get_elem_tactic) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.eraseIdx.{u} {α : Type u}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (h : i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") := by
    get_elem_tactic) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Removes the element at a given index from an array without a run-time bounds check.
This function takes worst-case `O(n)` time because it back-shifts all elements at positions greater than `i`.
Examples:
  * `#["apple", "pear", "orange"].[eraseIdx](Basic-Types/Arrays/#Array___eraseIdx "Documentation for Array.eraseIdx") 0 = #["pear", "orange"]`
  * `#["apple", "pear", "orange"].[eraseIdx](Basic-Types/Arrays/#Array___eraseIdx "Documentation for Array.eraseIdx") 1 = #["apple", "orange"]`
  * `#["apple", "pear", "orange"].[eraseIdx](Basic-Types/Arrays/#Array___eraseIdx "Documentation for Array.eraseIdx") 2 = #["apple", "pear"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.eraseIdx! "Permalink")def
```


Array.eraseIdx!.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.eraseIdx!.{u} {α : Type u}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Removes the element at a given index from an array. Panics if the index is out of bounds.
This function takes worst-case `O(n)` time because it back-shifts all elements at positions greater than `i`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.eraseIdxIfInBounds "Permalink")def
```


Array.eraseIdxIfInBounds.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.eraseIdxIfInBounds.{u} {α : Type u}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Removes the element at a given index from an array. Does nothing if the index is out of bounds.
This function takes worst-case `O(n)` time because it back-shifts all elements at positions greater than `i`.
Examples:
  * `#["apple", "pear", "orange"].[eraseIdxIfInBounds](Basic-Types/Arrays/#Array___eraseIdxIfInBounds "Documentation for Array.eraseIdxIfInBounds") 0 = #["pear", "orange"]`
  * `#["apple", "pear", "orange"].[eraseIdxIfInBounds](Basic-Types/Arrays/#Array___eraseIdxIfInBounds "Documentation for Array.eraseIdxIfInBounds") 1 = #["apple", "orange"]`
  * `#["apple", "pear", "orange"].[eraseIdxIfInBounds](Basic-Types/Arrays/#Array___eraseIdxIfInBounds "Documentation for Array.eraseIdxIfInBounds") 2 = #["apple", "pear"]`
  * `#["apple", "pear", "orange"].[eraseIdxIfInBounds](Basic-Types/Arrays/#Array___eraseIdxIfInBounds "Documentation for Array.eraseIdxIfInBounds") 3 = #["apple", "pear", "orange"]`
  * `#["apple", "pear", "orange"].[eraseIdxIfInBounds](Basic-Types/Arrays/#Array___eraseIdxIfInBounds "Documentation for Array.eraseIdxIfInBounds") 5 = #["apple", "pear", "orange"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.eraseReps "Permalink")def
```


Array.eraseReps.{u_1} {α : Type u_1} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.eraseReps.{u_1} {α : Type u_1}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Erases repeated elements, keeping the first element of each run.
`O(|as|)`.
Example:
  * `#[1, 3, 2, 2, 2, 3, 3, 5].[eraseReps](Basic-Types/Arrays/#Array___eraseReps "Documentation for Array.eraseReps") = #[1, 3, 2, 3, 5]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.swap "Permalink")def
```


Array.swap.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i j : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (hi : i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") := by get_elem_tactic)
  (hj : j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") := by get_elem_tactic) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.swap.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (i j : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (hi : i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") := by get_elem_tactic)
  (hj : j [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") := by
    get_elem_tactic) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Swaps two elements of an array. The modification is performed in-place when the reference to the array is unique.
Examples:
  * `#["red", "green", "blue", "brown"].[swap](Basic-Types/Arrays/#Array___swap "Documentation for Array.swap") 0 3 = #["brown", "green", "blue", "red"]`
  * `#["red", "green", "blue", "brown"].[swap](Basic-Types/Arrays/#Array___swap "Documentation for Array.swap") 0 2 = #["blue", "green", "red", "brown"]`
  * `#["red", "green", "blue", "brown"].[swap](Basic-Types/Arrays/#Array___swap "Documentation for Array.swap") 1 2 = #["red", "blue", "green", "brown"]`
  * `#["red", "green", "blue", "brown"].[swap](Basic-Types/Arrays/#Array___swap "Documentation for Array.swap") 3 0 = #["brown", "green", "blue", "red"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.swapIfInBounds "Permalink")def
```


Array.swapIfInBounds.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i j : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.swapIfInBounds.{u} {α : Type u}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i j : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Swaps two elements of an array, returning the array unchanged if either index is out of bounds. The modification is performed in-place when the reference to the array is unique.
Examples:
  * `#["red", "green", "blue", "brown"].[swapIfInBounds](Basic-Types/Arrays/#Array___swapIfInBounds "Documentation for Array.swapIfInBounds") 0 3 = #["brown", "green", "blue", "red"]`
  * `#["red", "green", "blue", "brown"].[swapIfInBounds](Basic-Types/Arrays/#Array___swapIfInBounds "Documentation for Array.swapIfInBounds") 0 2 = #["blue", "green", "red", "brown"]`
  * `#["red", "green", "blue", "brown"].[swapIfInBounds](Basic-Types/Arrays/#Array___swapIfInBounds "Documentation for Array.swapIfInBounds") 1 2 = #["red", "blue", "green", "brown"]`
  * `#["red", "green", "blue", "brown"].[swapIfInBounds](Basic-Types/Arrays/#Array___swapIfInBounds "Documentation for Array.swapIfInBounds") 0 4 = #["red", "green", "blue", "brown"]`
  * `#["red", "green", "blue", "brown"].[swapIfInBounds](Basic-Types/Arrays/#Array___swapIfInBounds "Documentation for Array.swapIfInBounds") 9 2 = #["red", "green", "blue", "brown"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.swapAt "Permalink")def
```


Array.swapAt.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (v : α)
  (hi : i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") := by get_elem_tactic) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.swapAt.{u} {α : Type u}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (v : α)
  (hi : i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") := by
    get_elem_tactic) :
  α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Swaps a new element with the element at the given index.
Returns the value formerly found at `i`, paired with an array in which the value at `i` has been replaced with `v`.
Examples:
  * `#["spinach", "broccoli", "carrot"].[swapAt](Basic-Types/Arrays/#Array___swapAt "Documentation for Array.swapAt") 1 "pepper" = ("broccoli", #["spinach", "pepper", "carrot"])`
  * `#["spinach", "broccoli", "carrot"].[swapAt](Basic-Types/Arrays/#Array___swapAt "Documentation for Array.swapAt") 2 "pepper" = ("carrot", #["spinach", "broccoli", "pepper"])`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.swapAt! "Permalink")def
```


Array.swapAt!.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (v : α) :
  α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.swapAt!.{u} {α : Type u}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (v : α) :
  α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Swaps a new element with the element at the given index. Panics if the index is out of bounds.
Returns the value formerly found at `i`, paired with an array in which the value at `i` has been replaced with `v`.
Examples:
  * `#["spinach", "broccoli", "carrot"].[swapAt!](Basic-Types/Arrays/#Array___swapAt___ "Documentation for Array.swapAt!") 1 "pepper" = (#["spinach", "pepper", "carrot"], "broccoli")`
  * `#["spinach", "broccoli", "carrot"].[swapAt!](Basic-Types/Arrays/#Array___swapAt___ "Documentation for Array.swapAt!") 2 "pepper" = (#["spinach", "broccoli", "pepper"], "carrot")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.replace "Permalink")def
```


Array.replace.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (a b : α) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.replace.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (a b : α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Replaces the first occurrence of `a` with `b` in an array. The modification is performed in-place when the reference to the array is unique. Returns the array unmodified when `a` is not present.
Examples:
  * `#[1, 2, 3, 2, 1].[replace](Basic-Types/Arrays/#Array___replace "Documentation for Array.replace") 2 5 = #[1, 5, 3, 2, 1]`
  * `#[1, 2, 3, 2, 1].[replace](Basic-Types/Arrays/#Array___replace "Documentation for Array.replace") 0 5 = #[1, 2, 3, 2, 1]`
  * `#[].[replace](Basic-Types/Arrays/#Array___replace "Documentation for Array.replace") 2 5 = #[]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.set "Permalink")def
```


Array.set.{u_1} {α : Type u_1} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (v : α)
  (h : i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") := by get_elem_tactic) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.set.{u_1} {α : Type u_1}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (v : α)
  (h : i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") := by
    get_elem_tactic) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Replaces the element at a given index in an array.
No bounds check is performed, but the function requires a proof that the index is in bounds. This proof can usually be omitted, and will be synthesized automatically.
The array is modified in-place if there are no other references to it.
Examples:
  * `#[0, 1, 2].[set](Basic-Types/Arrays/#Array___set "Documentation for Array.set") 1 5 = #[0, 5, 2]`
  * `#["orange", "apple"].[set](Basic-Types/Arrays/#Array___set "Documentation for Array.set") 1 "grape" = #["orange", "grape"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.set! "Permalink")def
```


Array.set!.{u_1} {α : Type u_1} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (v : α) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.set!.{u_1} {α : Type u_1}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (v : α) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Set an element in an array, or panic if the index is out of bounds.
This will perform the update destructively provided that `a` has a reference count of 1 when called.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.setIfInBounds "Permalink")def
```


Array.setIfInBounds.{u_1} {α : Type u_1} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (v : α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.setIfInBounds.{u_1} {α : Type u_1}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (v : α) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Replaces the element at the provided index in an array. The array is returned unmodified if the index is out of bounds.
The array is modified in-place if there are no other references to it.
Examples:
  * `#[0, 1, 2].[setIfInBounds](Basic-Types/Arrays/#Array___setIfInBounds "Documentation for Array.setIfInBounds") 1 5 = #[0, 5, 2]`
  * `#["orange", "apple"].[setIfInBounds](Basic-Types/Arrays/#Array___setIfInBounds "Documentation for Array.setIfInBounds") 1 "grape" = #["orange", "grape"]`
  * `#["orange", "apple"].[setIfInBounds](Basic-Types/Arrays/#Array___setIfInBounds "Documentation for Array.setIfInBounds") 5 "grape" = #["orange", "apple"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.uset "Permalink")def
```


Array.uset.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) (v : α)
  (h : i.[toNat](Basic-Types/Fixed-Precision-Integers/#USize___toNat "Documentation for USize.toNat") [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.uset.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (i : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) (v : α)
  (h : i.[toNat](Basic-Types/Fixed-Precision-Integers/#USize___toNat "Documentation for USize.toNat") [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") xs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Low-level modification operator which is as fast as a C array write. The modification is performed in-place when the reference to the array is unique.
This avoids overhead due to unboxing a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` used as an index.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.modify "Permalink")def
```


Array.modify.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : α → α) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.modify.{u} {α : Type u}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : α → α) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Replaces the element at the given index, if it exists, with the result of applying `f` to it. If the index is invalid, the array is returned unmodified.
Examples:
  * `#[1, 2, 3].[modify](Basic-Types/Arrays/#Array___modify "Documentation for Array.modify") 0 (· * 10) = #[10, 2, 3]`
  * `#[1, 2, 3].[modify](Basic-Types/Arrays/#Array___modify "Documentation for Array.modify") 2 (· * 10) = #[1, 2, 30]`
  * `#[1, 2, 3].[modify](Basic-Types/Arrays/#Array___modify "Documentation for Array.modify") 3 (· * 10) = #[1, 2, 3]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.modifyM "Permalink")def
```


Array.modifyM.{u, u_1} {α : Type u} {m : Type u → Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : α → m α) : m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)


Array.modifyM.{u, u_1} {α : Type u}
  {m : Type u → Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : α → m α) :
  m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)


```

Replaces the element at the given index, if it exists, with the result of applying the monadic function `f` to it. If the index is invalid, the array is returned unmodified and `f` is not called.
Examples:
``#[1, 2, 30, 4]``It was 3 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #[1, 2, 3, 4].[modifyM](Basic-Types/Arrays/#Array___modifyM "Documentation for Array.modifyM") 2 fun x => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"It was {x}" return x * 10 ``It was 3``#[1, 2, 30, 4]```#[1, 2, 3, 4]`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #[1, 2, 3, 4].[modifyM](Basic-Types/Arrays/#Array___modifyM "Documentation for Array.modifyM") 6 fun x => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"It was {x}" return x * 10 ``#[1, 2, 3, 4]`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.modifyOp "Permalink")def
```


Array.modifyOp.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (idx : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : α → α) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.modifyOp.{u} {α : Type u}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (idx : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (f : α → α) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Replaces the element at the given index, if it exists, with the result of applying `f` to it. If the index is invalid, the array is returned unmodified.
Examples:
  * `#[1, 2, 3].[modifyOp](Basic-Types/Arrays/#Array___modifyOp "Documentation for Array.modifyOp") 0 (· * 10) = #[10, 2, 3]`
  * `#[1, 2, 3].[modifyOp](Basic-Types/Arrays/#Array___modifyOp "Documentation for Array.modifyOp") 2 (· * 10) = #[1, 2, 30]`
  * `#[1, 2, 3].[modifyOp](Basic-Types/Arrays/#Array___modifyOp "Documentation for Array.modifyOp") 3 (· * 10) = #[1, 2, 3]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.insertIdx "Permalink")def
```


Array.insertIdx.{u} {α : Type u} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) :
  [autoParam](Terms/Function-Application/#autoParam "Documentation for autoParam") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")i [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") Array.insertIdx._auto_1 → [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.insertIdx.{u} {α : Type u}
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) :
  [autoParam](Terms/Function-Application/#autoParam "Documentation for autoParam") [(](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")i [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")[)](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le")
      Array.insertIdx._auto_1 →
    [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Inserts an element into an array at the specified index. If the index is greater than the size of the array, then the array is returned unmodified.
In other words, the new element is inserted into the array `as` after the first `i` elements of `as`.
This function takes worst case `O(n)` time because it has to swap the inserted element into place.
Examples:
  * `#["tues", "thur", "sat"].[insertIdx](Basic-Types/Arrays/#Array___insertIdx "Documentation for Array.insertIdx") 1 "wed" = #["tues", "wed", "thur", "sat"]`
  * `#["tues", "thur", "sat"].[insertIdx](Basic-Types/Arrays/#Array___insertIdx "Documentation for Array.insertIdx") 2 "wed" = #["tues", "thur", "wed", "sat"]`
  * `#["tues", "thur", "sat"].[insertIdx](Basic-Types/Arrays/#Array___insertIdx "Documentation for Array.insertIdx") 3 "wed" = #["tues", "thur", "sat", "wed"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.insertIdx! "Permalink")def
```


Array.insertIdx!.{u} {α : Type u} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.insertIdx!.{u} {α : Type u}
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Inserts an element into an array at the specified index. Panics if the index is greater than the size of the array.
In other words, the new element is inserted into the array `as` after the first `i` elements of `as`.
This function takes worst case `O(n)` time because it has to swap the inserted element into place. `[Array.insertIdx](Basic-Types/Arrays/#Array___insertIdx "Documentation for Array.insertIdx")` and `[Array.insertIdxIfInBounds](Basic-Types/Arrays/#Array___insertIdxIfInBounds "Documentation for Array.insertIdxIfInBounds")` are safer alternatives.
Examples:
  * `#["tues", "thur", "sat"].[insertIdx!](Basic-Types/Arrays/#Array___insertIdx___ "Documentation for Array.insertIdx!") 1 "wed" = #["tues", "wed", "thur", "sat"]`
  * `#["tues", "thur", "sat"].[insertIdx!](Basic-Types/Arrays/#Array___insertIdx___ "Documentation for Array.insertIdx!") 2 "wed" = #["tues", "thur", "wed", "sat"]`
  * `#["tues", "thur", "sat"].[insertIdx!](Basic-Types/Arrays/#Array___insertIdx___ "Documentation for Array.insertIdx!") 3 "wed" = #["tues", "thur", "sat", "wed"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.insertIdxIfInBounds "Permalink")def
```


Array.insertIdxIfInBounds.{u} {α : Type u} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (a : α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.insertIdxIfInBounds.{u} {α : Type u}
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (a : α) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Inserts an element into an array at the specified index. The array is returned unmodified if the index is greater than the size of the array.
In other words, the new element is inserted into the array `as` after the first `i` elements of `as`.
This function takes worst case `O(n)` time because it has to swap the inserted element into place.
Examples:
  * `#["tues", "thur", "sat"].[insertIdxIfInBounds](Basic-Types/Arrays/#Array___insertIdxIfInBounds "Documentation for Array.insertIdxIfInBounds") 1 "wed" = #["tues", "wed", "thur", "sat"]`
  * `#["tues", "thur", "sat"].[insertIdxIfInBounds](Basic-Types/Arrays/#Array___insertIdxIfInBounds "Documentation for Array.insertIdxIfInBounds") 2 "wed" = #["tues", "thur", "wed", "sat"]`
  * `#["tues", "thur", "sat"].[insertIdxIfInBounds](Basic-Types/Arrays/#Array___insertIdxIfInBounds "Documentation for Array.insertIdxIfInBounds") 3 "wed" = #["tues", "thur", "sat", "wed"]`
  * `#["tues", "thur", "sat"].[insertIdxIfInBounds](Basic-Types/Arrays/#Array___insertIdxIfInBounds "Documentation for Array.insertIdxIfInBounds") 4 "wed" = #["tues", "thur", "sat"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.reverse "Permalink")def
```


Array.reverse.{u} {α : Type u} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.reverse.{u} {α : Type u}
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Reverses an array by repeatedly swapping elements.
The original array is modified in place if there are no other references to it.
Examples:
  * `(#[] : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")).[reverse](Basic-Types/Arrays/#Array___reverse "Documentation for Array.reverse") = #[]`
  * `#[0, 1].[reverse](Basic-Types/Arrays/#Array___reverse "Documentation for Array.reverse") = #[1, 0]`
  * `#[0, 1, 2].[reverse](Basic-Types/Arrays/#Array___reverse "Documentation for Array.reverse") = #[2, 1, 0]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.take "Permalink")def
```


Array.take.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.take.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Returns a new array that contains the first `i` elements of `xs`. If `xs` has fewer than `i` elements, the new array contains all the elements of `xs`.
The returned array is always a new array, even if it contains the same elements as the input array.
Examples:
  * `#["red", "green", "blue"].[take](Basic-Types/Arrays/#Array___take "Documentation for Array.take") 1 = #["red"]`
  * `#["red", "green", "blue"].[take](Basic-Types/Arrays/#Array___take "Documentation for Array.take") 2 = #["red", "green"]`
  * `#["red", "green", "blue"].[take](Basic-Types/Arrays/#Array___take "Documentation for Array.take") 5 = #["red", "green", "blue"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.takeWhile "Permalink")def
```


Array.takeWhile.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.takeWhile.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Returns a new array that contains the longest prefix of elements that satisfy the predicate `p` from an array.
Examples:
  * `#[0, 1, 2, 3, 2, 1].[takeWhile](Basic-Types/Arrays/#Array___takeWhile "Documentation for Array.takeWhile") (· < 2) = #[0, 1]`
  * `#[0, 1, 2, 3, 2, 1].[takeWhile](Basic-Types/Arrays/#Array___takeWhile "Documentation for Array.takeWhile") (· < 20) = #[0, 1, 2, 3, 2, 1]`
  * `#[0, 1, 2, 3, 2, 1].[takeWhile](Basic-Types/Arrays/#Array___takeWhile "Documentation for Array.takeWhile") (· < 0) = #[]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.drop "Permalink")def
```


Array.drop.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.drop.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Removes the first `i` elements of `xs`. If `xs` has fewer than `i` elements, the new array is empty.
The returned array is always a new array, even if it contains the same elements as the input array.
Examples:
  * `#["red", "green", "blue"].[drop](Basic-Types/Arrays/#Array___drop "Documentation for Array.drop") 1 = #["green", "blue"]`
  * `#["red", "green", "blue"].[drop](Basic-Types/Arrays/#Array___drop "Documentation for Array.drop") 2 = #["blue"]`
  * `#["red", "green", "blue"].[drop](Basic-Types/Arrays/#Array___drop "Documentation for Array.drop") 5 = #[]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.shrink "Permalink")def
```


Array.shrink.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.shrink.{u} {α : Type u}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Returns the first `n` elements of an array. The resulting array is produced by repeatedly calling `[Array.pop](Basic-Types/Arrays/#Array___pop "Documentation for Array.pop")`. If `n` is greater than the size of the array, it is returned unmodified.
If the reference to the array is unique, then this function uses in-place modification.
Examples:
  * `#[0, 1, 2, 3, 4].[shrink](Basic-Types/Arrays/#Array___shrink "Documentation for Array.shrink") 2 = #[0, 1]`
  * `#[0, 1, 2, 3, 4].[shrink](Basic-Types/Arrays/#Array___shrink "Documentation for Array.shrink") 0 = #[]`
  * `#[0, 1, 2, 3, 4].[shrink](Basic-Types/Arrays/#Array___shrink "Documentation for Array.shrink") 10 = #[0, 1, 2, 3, 4]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.flatten "Permalink")def
```


Array.flatten.{u} {α : Type u} (xss : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.flatten.{u} {α : Type u}
  (xss : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Appends the contents of array of arrays into a single array. The resulting array contains the same elements as the nested arrays in the same order.
Examples:
  * `#[#[5], #[4], #[3, 2]].[flatten](Basic-Types/Arrays/#Array___flatten "Documentation for Array.flatten") = #[5, 4, 3, 2]`
  * `#[#[0, 1], #[], #[2], #[1, 0, 1]].[flatten](Basic-Types/Arrays/#Array___flatten "Documentation for Array.flatten") = #[0, 1, 2, 1, 0, 1]`
  * `(#[] : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")).[flatten](Basic-Types/Arrays/#Array___flatten "Documentation for Array.flatten") = #[]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.getEvenElems "Permalink")def
```


Array.getEvenElems.{u} {α : Type u} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.getEvenElems.{u} {α : Type u}
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Returns a new array that contains the elements at even indices in `as`, starting with the element at index `0`.
Examples:
  * `#[0, 1, 2, 3, 4].[getEvenElems](Basic-Types/Arrays/#Array___getEvenElems "Documentation for Array.getEvenElems") = #[0, 2, 4]`
  * `#[1, 2, 3, 4].[getEvenElems](Basic-Types/Arrays/#Array___getEvenElems "Documentation for Array.getEvenElems") = #[1, 3]`
  * `#["red", "green", "blue"].[getEvenElems](Basic-Types/Arrays/#Array___getEvenElems "Documentation for Array.getEvenElems") = #["red", "blue"]`
  * `(#[] : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")).[getEvenElems](Basic-Types/Arrays/#Array___getEvenElems "Documentation for Array.getEvenElems") = #[]`


###  20.16.4.7. Sorted Arrays[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--API-Reference--Sorted-Arrays "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.qsort "Permalink")def
```


Array.qsort.{u_1} {α : Type u_1} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (lt : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := by exact (· < ·)) (lo : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (hi : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 1) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.qsort.{u_1} {α : Type u_1}
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (lt : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := by exact (· < ·))
  (lo : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (hi : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 1) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

In-place quicksort.
`qsort as lt lo hi` sorts the subarray `as[lo...=hi]` in-place using `lt` to compare elements.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.qsortOrd "Permalink")def
```


Array.qsortOrd.{u_1} {α : Type u_1} [ord : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α] (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.qsortOrd.{u_1} {α : Type u_1}
  [ord : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α] (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Sort an array using `[compare](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord.compare")` to compare elements.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.insertionSort "Permalink")def
```


Array.insertionSort.{u_1} {α : Type u_1} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (lt : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := by exact (· < ·)) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.insertionSort.{u_1} {α : Type u_1}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (lt : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := by
    exact (· < ·)) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Sorts an array using insertion sort.
The optional parameter `lt` specifies an ordering predicate. It defaults to `[LT.lt](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")`, which must be decidable to be used for sorting.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.binInsert "Permalink")def
```


Array.binInsert.{u} {α : Type u} (lt : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (k : α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.binInsert.{u} {α : Type u}
  (lt : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (k : α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Inserts an element into a sorted array such that the resulting array is sorted. If the element is already present in the array, it is not inserted.
The ordering predicate `lt` should be a total order on elements, and the array `as` should be sorted with respect to `lt`.
`[Array.binInsertM](Basic-Types/Arrays/#Array___binInsertM "Documentation for Array.binInsertM")` is a more general operator that provides greater control over the handling of duplicate elements in addition to running in a monad.
Examples:
  * `#[0, 1, 3, 5].[binInsert](Basic-Types/Arrays/#Array___binInsert "Documentation for Array.binInsert") (· < ·) 2 = #[0, 1, 2, 3, 5]`
  * `#[0, 1, 3, 5].[binInsert](Basic-Types/Arrays/#Array___binInsert "Documentation for Array.binInsert") (· < ·) 1 = #[0, 1, 3, 5]`
  * `#[].[binInsert](Basic-Types/Arrays/#Array___binInsert "Documentation for Array.binInsert") (· < ·) 1 = #[1]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.binInsertM "Permalink")def
```


Array.binInsertM.{u, v} {α : Type u} {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (lt : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (merge : α → m α) (add : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → m α)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (k : α) : m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)


Array.binInsertM.{u, v} {α : Type u}
  {m : Type u → Type v} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (lt : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (merge : α → m α)
  (add : [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") → m α) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (k : α) : m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)


```

Inserts an element `k` into a sorted array `as` such that the resulting array is sorted.
The ordering predicate `lt` should be a total order on elements, and the array `as` should be sorted with respect to `lt`.
If an element that `lt` equates to `k` is already present in `as`, then `merge` is applied to the existing element to determine the value of that position in the resulting array. If no element equal to `k` is present, then `add` is used to determine the value to be inserted.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.binSearch "Permalink")def
```


Array.binSearch {α : Type} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (k : α) (lt : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (lo : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) (hi : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 1) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Array.binSearch {α : Type} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (k : α) (lt : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (lo : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (hi : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 1) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Binary search for an element equivalent to `k` in the sorted array `as`. Returns the element from the array, if it is found, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` otherwise.
The array `as` must be sorted according to the comparison operator `lt`, which should be a total order.
The optional parameters `lo` and `hi` determine the region of the array indices to be searched. Both are inclusive, and default to searching the entire array.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.binSearchContains "Permalink")def
```


Array.binSearchContains {α : Type} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (k : α)
  (lt : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (lo : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) (hi : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 1) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Array.binSearchContains {α : Type}
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (k : α)
  (lt : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (lo : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (hi : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") [-](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub.hSub") 1) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Binary search for an element equivalent to `k` in the sorted array `as`. Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the element is found, or `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` otherwise.
The array `as` must be sorted according to the comparison operator `lt`, which should be a total order.
The optional parameters `lo` and `hi` determine the region of the array indices to be searched. Both are inclusive, and default to searching the entire array.
###  20.16.4.8. Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--API-Reference--Iteration "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.iter "Permalink")def
```


Array.iter.{w} {α : Type w} (l : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") α


Array.iter.{w} {α : Type w}
  (l : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") α


```

Returns a finite iterator for the given array. The iterator yields the elements of the array in order and then terminates.
The monadic version of this iterator is `[Array.iterM](Basic-Types/Arrays/#Array___iterM "Documentation for Array.iterM")`.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.iterFromIdx "Permalink")def
```


Array.iterFromIdx.{w} {α : Type w} (l : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (pos : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") α


Array.iterFromIdx.{w} {α : Type w}
  (l : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (pos : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") α


```

Returns a finite iterator for the given array starting at the given index. The iterator yields the elements of the array in order and then terminates.
The monadic version of this iterator is `[Array.iterFromIdxM](Basic-Types/Arrays/#Array___iterFromIdxM "Documentation for Array.iterFromIdxM")`.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.iterM "Permalink")def
```


Array.iterM.{w, w'} {α : Type w} (array : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (m : Type w → Type w') [[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") m] : [Std.IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m α


Array.iterM.{w, w'} {α : Type w}
  (array : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (m : Type w → Type w')
  [[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") m] : [Std.IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m α


```

Returns a finite monadic iterator for the given array. The iterator yields the elements of the array in order and then terminates. There are no side effects.
The pure version of this iterator is `[Array.iter](Basic-Types/Arrays/#Array___iter "Documentation for Array.iter")`.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.iterFromIdxM "Permalink")def
```


Array.iterFromIdxM.{w, w'} {α : Type w} (array : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (m : Type w → Type w') (pos : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) [[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") m] : [Std.IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m α


Array.iterFromIdxM.{w, w'} {α : Type w}
  (array : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (m : Type w → Type w')
  (pos : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) [[Pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure") m] : [Std.IterM](Iterators/Iterator-Definitions/#Std___IterM___mk "Documentation for Std.IterM") m α


```

Returns a finite monadic iterator for the given array starting at the given index. The iterator yields the elements of the array in order and then terminates.
The pure version of this iterator is `[Array.iterFromIdx](Basic-Types/Arrays/#Array___iterFromIdx "Documentation for Array.iterFromIdx")`.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.foldr "Permalink")def
```


Array.foldr.{u, v} {α : Type u} {β : Type v} (f : α → β → β) (init : β)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) : β


Array.foldr.{u, v} {α : Type u}
  {β : Type v} (f : α → β → β) (init : β)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size"))
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) : β


```

Folds a function over an array from the right, accumulating a value starting with `init`. The accumulated value is combined with the each element of the array in reverse order, using `f`.
The optional parameters `start` and `stop` control the region of the array to be folded. Folding proceeds from `start` (exclusive) to `stop` (inclusive), so no folding occurs unless `start > stop`. By default, the entire array is used.
Examples:
  * `#[a, b, c].[foldr](Basic-Types/Arrays/#Array___foldr "Documentation for Array.foldr") f init  = f a (f b (f c init))`
  * `#[1, 2, 3].[foldr](Basic-Types/Arrays/#Array___foldr "Documentation for Array.foldr") (toString · ++ ·) "" = "123"`
  * `#[1, 2, 3].[foldr](Basic-Types/Arrays/#Array___foldr "Documentation for Array.foldr") (s!"({·} {·})") "!" = "(1 (2 (3 !)))"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.foldrM "Permalink")def
```


Array.foldrM.{u, v, w} {α : Type u} {β : Type v} {m : Type v → Type w}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → β → m β) (init : β) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) : m β


Array.foldrM.{u, v, w} {α : Type u}
  {β : Type v} {m : Type v → Type w}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → β → m β) (init : β)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size"))
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) : m β


```

Folds a monadic function over an array from the right, accumulating a value starting with `init`. The accumulated value is combined with the each element of the list in reverse order, using `f`.
The optional parameters `start` and `stop` control the region of the array to be folded. Folding proceeds from `start` (exclusive) to `stop` (inclusive), so no folding occurs unless `start > stop`. By default, the entire array is folded.
Examples:
`example [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → β → m β) :   [Array.foldrM](Basic-Types/Arrays/#Array___foldrM "Documentation for Array.foldrM") (m := m) f x₀ #[a, b, c] = ([do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")     let x₁ ← f c x₀     let x₂ ← f b x₁     let x₃ ← f a x₂     [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x₃)   := bym:Type u_1 → Type u_2α:Type u_3β:Type u_1x₀:βa:αb:αc:αinst✝:[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") mf:α → β → m β⊢ [Array.foldrM](Basic-Types/Arrays/#Array___foldrM "Documentation for Array.foldrM") f x₀ [#[](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")a[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") b[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") c[]](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") do   let x₁ ← f c x₀   let x₂ ← f b x₁   let x₃ ← f a x₂   [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x₃ [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 ``example [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → β → m β) :   [Array.foldrM](Basic-Types/Arrays/#Array___foldrM "Documentation for Array.foldrM") (m := m) f x₀ #[a, b, c] (start := 2) = ([do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")     let x₁ ← f b x₀     let x₂ ← f a x₁     [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x₂)   := bym:Type u_1 → Type u_2α:Type u_3β:Type u_1x₀:βa:αb:αc:αinst✝:[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") mf:α → β → m β⊢ [Array.foldrM](Basic-Types/Arrays/#Array___foldrM "Documentation for Array.foldrM") f x₀ [#[](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")a[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") b[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") c[]](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray") 2 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") do   let x₁ ← f b x₀   let x₂ ← f a x₁   [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x₂ [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 `
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.foldl "Permalink")def
```


Array.foldl.{u, v} {α : Type u} {β : Type v} (f : β → α → β) (init : β)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : β


Array.foldl.{u, v} {α : Type u}
  {β : Type v} (f : β → α → β) (init : β)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : β


```

Folds a function over an array from the left, accumulating a value starting with `init`. The accumulated value is combined with the each element of the array in order, using `f`.
The optional parameters `start` and `stop` control the region of the array to be folded. Folding proceeds from `start` (inclusive) to `stop` (exclusive), so no folding occurs unless `start < stop`. By default, the entire array is used.
Examples:
  * `#[a, b, c].[foldl](Basic-Types/Arrays/#Array___foldl "Documentation for Array.foldl") f z  = f (f (f z a) b) c`
  * `#[1, 2, 3].[foldl](Basic-Types/Arrays/#Array___foldl "Documentation for Array.foldl") (· ++ toString ·) "" = "123"`
  * `#[1, 2, 3].[foldl](Basic-Types/Arrays/#Array___foldl "Documentation for Array.foldl") (s!"({·} {·})") "" = "((( 1) 2) 3)"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.foldlM "Permalink")def
```


Array.foldlM.{u, v, w} {α : Type u} {β : Type v} {m : Type v → Type w}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : β → α → m β) (init : β) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : m β


Array.foldlM.{u, v, w} {α : Type u}
  {β : Type v} {m : Type v → Type w}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : β → α → m β) (init : β)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : m β


```

Folds a monadic function over a list from the left, accumulating a value starting with `init`. The accumulated value is combined with the each element of the list in order, using `f`.
The optional parameters `start` and `stop` control the region of the array to be folded. Folding proceeds from `start` (inclusive) to `stop` (exclusive), so no folding occurs unless `start < stop`. By default, the entire array is folded.
Examples:
`example [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → β → m α) :     [Array.foldlM](Basic-Types/Arrays/#Array___foldlM "Documentation for Array.foldlM") (m := m) f x₀ #[a, b, c] = ([do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")       let x₁ ← f x₀ a       let x₂ ← f x₁ b       let x₃ ← f x₂ c       [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x₃)   := bym:Type u_1 → Type u_2α:Type u_1β:Type u_3x₀:αa:βb:βc:βinst✝:[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") mf:α → β → m α⊢ [Array.foldlM](Basic-Types/Arrays/#Array___foldlM "Documentation for Array.foldlM") f x₀ [#[](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")a[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") b[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") c[]](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") do   let x₁ ← f x₀ a   let x₂ ← f x₁ b   let x₃ ← f x₂ c   [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x₃ [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 ``example [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → β → m α) :     [Array.foldlM](Basic-Types/Arrays/#Array___foldlM "Documentation for Array.foldlM") (m := m) f x₀ #[a, b, c] (start := 1) = ([do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax")       let x₁ ← f x₀ b       let x₂ ← f x₁ c       [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x₂)   := bym:Type u_1 → Type u_2α:Type u_1β:Type u_3x₀:αa:βb:βc:βinst✝:[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") mf:α → β → m α⊢ [Array.foldlM](Basic-Types/Arrays/#Array___foldlM "Documentation for Array.foldlM") f x₀ [#[](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray")a[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") b[,](Basic-Types/Linked-Lists/#List___nil "Documentation for List.cons") c[]](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray") 1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") do   let x₁ ← f x₀ b   let x₂ ← f x₁ c   [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") x₂ [rfl](Tactic-Proofs/Tactic-Reference/#rfl "Documentation for tactic")All goals completed! 🐙 `
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.forM "Permalink")def
```


Array.forM.{u, v, w} {α : Type u} {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


Array.forM.{u, v, w} {α : Type u}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Applies the monadic action `f` to each element of an array, in order.
The optional parameters `start` and `stop` control the region of the array to which `f` should be applied. Iteration proceeds from `start` (inclusive) to `stop` (exclusive), so `f` is not invoked unless `start < stop`. By default, the entire array is used.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.forRevM "Permalink")def
```


Array.forRevM.{u, v, w} {α : Type u} {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size"))
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


Array.forRevM.{u, v, w} {α : Type u}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size"))
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Applies the monadic action `f` to each element of an array from right to left, in reverse order.
The optional parameters `start` and `stop` control the region of the array to which `f` should be applied. Iteration proceeds from `start` (exclusive) to `stop` (inclusive), so no `f` is not invoked unless `start > stop`. By default, the entire array is used.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.firstM "Permalink")def
```


Array.firstM.{u, v, w} {β : Type v} {α : Type u} {m : Type v → Type w}
  [[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative") m] (f : α → m β) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : m β


Array.firstM.{u, v, w} {β : Type v}
  {α : Type u} {m : Type v → Type w}
  [[Alternative](Functors___-Monads-and--do--Notation/#Alternative___mk "Documentation for Alternative") m] (f : α → m β)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : m β


```

Maps `f` over the array and collects the results with `<|>`. The result for the end of the array is `failure`.
Examples:
  * `#[[], [1, 2], [], [2]].[firstM](Basic-Types/Arrays/#Array___firstM "Documentation for Array.firstM") [List.head?](Basic-Types/Linked-Lists/#List___head___ "Documentation for List.head?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 1`
  * `#[[], [], []].[firstM](Basic-Types/Arrays/#Array___firstM "Documentation for Array.firstM") [List.head?](Basic-Types/Linked-Lists/#List___head___ "Documentation for List.head?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `#[].[firstM](Basic-Types/Arrays/#Array___firstM "Documentation for Array.firstM") [List.head?](Basic-Types/Linked-Lists/#List___head___ "Documentation for List.head?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.sum "Permalink")def
```


Array.sum.{u_1} {α : Type u_1} [[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") α] [[Zero](Type-Classes/Basic-Classes/#Zero___mk "Documentation for Zero") α] : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α → α


Array.sum.{u_1} {α : Type u_1} [[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") α]
  [[Zero](Type-Classes/Basic-Classes/#Zero___mk "Documentation for Zero") α] : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α → α


```

Computes the sum of the elements of an array.
Examples:
  * `#[a, b, c].[sum](Basic-Types/Arrays/#Array___sum "Documentation for Array.sum") = a + (b + (c + 0))`
  * `#[1, 2, 5].[sum](Basic-Types/Arrays/#Array___sum "Documentation for Array.sum") = 8`


###  20.16.4.9. Transformation[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--API-Reference--Transformation "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.map "Permalink")def
```


Array.map.{u, v} {α : Type u} {β : Type v} (f : α → β) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


Array.map.{u, v} {α : Type u} {β : Type v}
  (f : α → β) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


```

Applies a function to each element of the array, returning the resulting array of values.
Examples:
  * `#[a, b, c].[map](Basic-Types/Arrays/#Array___map "Documentation for Array.map") f = #[f a, f b, f c]`
  * `#[].[map](Basic-Types/Arrays/#Array___map "Documentation for Array.map") [Nat.succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ") = #[]`
  * `#["one", "two", "three"].[map](Basic-Types/Arrays/#Array___map "Documentation for Array.map") (·.[length](Basic-Types/Strings/#String___length "Documentation for String.length")) = #[3, 3, 5]`
  * `#["one", "two", "three"].[map](Basic-Types/Arrays/#Array___map "Documentation for Array.map") (·.reverse) = #["eno", "owt", "eerht"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.mapMono "Permalink")def
```


Array.mapMono.{u_1} {α : Type u_1} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (f : α → α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.mapMono.{u_1} {α : Type u_1}
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (f : α → α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Applies a function to each element of an array, returning the array of results. The function is monomorphic: it is required to return a value of the same type. The internal implementation uses pointer equality, and does not allocate a new array if the result of each function call is pointer-equal to its argument.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.mapM "Permalink")def
```


Array.mapM.{u, v, w} {α : Type u} {β : Type v} {m : Type v → Type w}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → m β) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β)


Array.mapM.{u, v, w} {α : Type u}
  {β : Type v} {m : Type v → Type w}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → m β) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) :
  m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β)


```

Applies the monadic action `f` to every element in the array, left-to-right, and returns the array of results.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.mapM' "Permalink")def
```


Array.mapM'.{u_1, u_2, u_3} {m : Type u_1 → Type u_2} {α : Type u_3}
  {β : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → m β) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) :
  m [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") bs [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") bs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


Array.mapM'.{u_1, u_2, u_3}
  {m : Type u_1 → Type u_2} {α : Type u_3}
  {β : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → m β)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) :
  m [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") bs [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") bs.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


```

Applies the monadic action `f` to every element in the array, left-to-right, and returns the array of results. Furthermore, the resulting array's type guarantees that it contains the same number of elements as the input array.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.mapMonoM "Permalink")def
```


Array.mapMonoM.{u_1, u_2} {m : Type u_1 → Type u_2} {α : Type u_1}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (f : α → m α) : m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)


Array.mapMonoM.{u_1, u_2}
  {m : Type u_1 → Type u_2} {α : Type u_1}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (f : α → m α) :
  m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)


```

Applies a monadic function to each element of an array, returning the array of results. The function is monomorphic: it is required to return a value of the same type. The internal implementation uses pointer equality, and does not allocate a new array if the result of each function call is pointer-equal to its argument.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.mapIdx "Permalink")def
```


Array.mapIdx.{u, v} {α : Type u} {β : Type v} (f : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → α → β)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


Array.mapIdx.{u, v} {α : Type u}
  {β : Type v} (f : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → α → β)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


```

Applies a function to each element of the array along with the index at which that element is found, returning the array of results.
`[Array.mapFinIdx](Basic-Types/Arrays/#Array___mapFinIdx "Documentation for Array.mapFinIdx")` is a variant that additionally provides the function with a proof that the index is valid.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.mapIdxM "Permalink")def
```


Array.mapIdxM.{u, v, w} {α : Type u} {β : Type v} {m : Type v → Type w}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → α → m β) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β)


Array.mapIdxM.{u, v, w} {α : Type u}
  {β : Type v} {m : Type v → Type w}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → α → m β)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β)


```

Applies the monadic action `f` to every element in the array, along with the element's index, from left to right. Returns the array of results.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.mapFinIdx "Permalink")def
```


Array.mapFinIdx.{u, v} {α : Type u} {β : Type v} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → α → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") → β) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


Array.mapFinIdx.{u, v} {α : Type u}
  {β : Type v} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → α → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") → β) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


```

Applies a function to each element of the array along with the index at which that element is found, returning the array of results. In addition to the index, the function is also provided with a proof that the index is valid.
`[Array.mapIdx](Basic-Types/Arrays/#Array___mapIdx "Documentation for Array.mapIdx")` is a variant that does not provide the function with evidence that the index is valid.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.mapFinIdxM "Permalink")def
```


Array.mapFinIdxM.{u, v, w} {α : Type u} {β : Type v}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (f : (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → α → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") → m β) : m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β)


Array.mapFinIdxM.{u, v, w} {α : Type u}
  {β : Type v} {m : Type v → Type w}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (f :
    (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) → α → i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") → m β) :
  m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β)


```

Applies the monadic action `f` to every element in the array, along with the element's index and a proof that the index is in bounds, from left to right. Returns the array of results.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.flatMap "Permalink")def
```


Array.flatMap.{u, u_1} {α : Type u} {β : Type u_1} (f : α → [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


Array.flatMap.{u, u_1} {α : Type u}
  {β : Type u_1} (f : α → [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


```

Applies a function that returns an array to each element of an array. The resulting arrays are appended.
Examples:
  * `#[2, 3, 2].[flatMap](Basic-Types/Arrays/#Array___flatMap "Documentation for Array.flatMap") [Array.range](Basic-Types/Arrays/#Array___range "Documentation for Array.range") = #[0, 1, 0, 1, 2, 0, 1]`
  * `#[['a', 'b'], ['c', 'd', 'e']].[flatMap](Basic-Types/Arrays/#Array___flatMap "Documentation for Array.flatMap") [List.toArray](Basic-Types/Linked-Lists/#List___toArray "Documentation for List.toArray") = #['a', 'b', 'c', 'd', 'e']`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.flatMapM "Permalink")def
```


Array.flatMapM.{u, u_1, u_2} {α : Type u} {m : Type u_1 → Type u_2}
  {β : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β)) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) :
  m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β)


Array.flatMapM.{u, u_1, u_2} {α : Type u}
  {m : Type u_1 → Type u_2} {β : Type u_1}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β))
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β)


```

Applies a monadic function that returns an array to each element of an array, from left to right. The resulting arrays are appended.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.zip "Permalink")def
```


Array.zip.{u, u_1} {α : Type u} {β : Type u_1} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (bs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


Array.zip.{u, u_1} {α : Type u}
  {β : Type u_1} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (bs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Combines two arrays into an array of pairs in which the first and second components are the corresponding elements of each input array. The resulting array is the length of the shorter of the input arrays.
Examples:
  * `#["Mon", "Tue", "Wed"].[zip](Basic-Types/Arrays/#Array___zip "Documentation for Array.zip") #[1, 2, 3] = #[("Mon", 1), ("Tue", 2), ("Wed", 3)]`
  * `#["Mon", "Tue", "Wed"].[zip](Basic-Types/Arrays/#Array___zip "Documentation for Array.zip") #[1, 2] = #[("Mon", 1), ("Tue", 2)]`
  * `#[x₁, x₂, x₃].[zip](Basic-Types/Arrays/#Array___zip "Documentation for Array.zip") #[y₁, y₂, y₃, y₄] = #[(x₁, y₁), (x₂, y₂), (x₃, y₃)]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.zipWith "Permalink")def
```


Array.zipWith.{u, u_1, u_2} {α : Type u} {β : Type u_1} {γ : Type u_2}
  (f : α → β → γ) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (bs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") γ


Array.zipWith.{u, u_1, u_2} {α : Type u}
  {β : Type u_1} {γ : Type u_2}
  (f : α → β → γ) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (bs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") γ


```

Applies a function to the corresponding elements of two arrays, stopping at the end of the shorter array.
Examples:
  * `#[1, 2].[zipWith](Basic-Types/Arrays/#Array___zipWith "Documentation for Array.zipWith") (· + ·) #[5, 6] = #[6, 8]`
  * `#[1, 2, 3].[zipWith](Basic-Types/Arrays/#Array___zipWith "Documentation for Array.zipWith") (· + ·) #[5, 6, 10] = #[6, 8, 13]`
  * `#[].[zipWith](Basic-Types/Arrays/#Array___zipWith "Documentation for Array.zipWith") (· + ·) #[5, 6] = #[]`
  * `#[x₁, x₂, x₃].[zipWith](Basic-Types/Arrays/#Array___zipWith "Documentation for Array.zipWith") f #[y₁, y₂, y₃, y₄] = #[f x₁ y₁, f x₂ y₂, f x₃ y₃]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.zipWithAll "Permalink")def
```


Array.zipWithAll.{u, u_1, u_2} {α : Type u} {β : Type u_1}
  {γ : Type u_2} (f : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β → γ) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (bs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") γ


Array.zipWithAll.{u, u_1, u_2}
  {α : Type u} {β : Type u_1}
  {γ : Type u_2}
  (f : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β → γ)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (bs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") γ


```

Applies a function to the corresponding elements of both arrays, stopping when there are no more elements in either array. If one array is shorter than the other, the function is passed `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` for the missing elements.
Examples:
  * `#[1, 6].[zipWithAll](Basic-Types/Arrays/#Array___zipWithAll "Documentation for Array.zipWithAll") [min](Type-Classes/Basic-Classes/#Min___mk "Documentation for Min.min") #[5, 2] = #[[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 1, [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2]`
  * `#[1, 2, 3].[zipWithAll](Basic-Types/Arrays/#Array___zipWithAll "Documentation for Array.zipWithAll") [Prod.mk](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.mk") #[5, 6] = #[([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 1, [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5), ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2, [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 6), ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 3, [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none"))]`
  * `#[x₁, x₂].[zipWithAll](Basic-Types/Arrays/#Array___zipWithAll "Documentation for Array.zipWithAll") f #[y] = #[f ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x₁) ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") y), f ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x₂) [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.zipIdx "Permalink")def
```


Array.zipIdx.{u} {α : Type u} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


Array.zipIdx.{u} {α : Type u}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Pairs each element of an array with its index, optionally starting from an index other than `0`.
Examples:
  * `#[a, b, c].[zipIdx](Basic-Types/Arrays/#Array___zipIdx "Documentation for Array.zipIdx") = #[(a, 0), (b, 1), (c, 2)]`
  * `#[a, b, c].[zipIdx](Basic-Types/Arrays/#Array___zipIdx "Documentation for Array.zipIdx") 5 = #[(a, 5), (b, 6), (c, 7)]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.unzip "Permalink")def
```


Array.unzip.{u, u_1} {α : Type u} {β : Type u_1} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


Array.unzip.{u, u_1} {α : Type u}
  {β : Type u_1} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


```

Separates an array of pairs into two arrays that contain the respective first and second components.
Examples:
  * `#[("Monday", 1), ("Tuesday", 2)].[unzip](Basic-Types/Arrays/#Array___unzip "Documentation for Array.unzip") = (#["Monday", "Tuesday"], #[1, 2])`
  * `#[(x₁, y₁), (x₂, y₂), (x₃, y₃)].[unzip](Basic-Types/Arrays/#Array___unzip "Documentation for Array.unzip") = (#[x₁, x₂, x₃], #[y₁, y₂, y₃])`
  * `(#[] : Array (Nat × String)).unzip = ((#[], #[]) : List Nat × List String)`


###  20.16.4.10. Filtering[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--API-Reference--Filtering "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.filter "Permalink")def
```


Array.filter.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.filter.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Returns the array of elements in `as` for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Only elements from `start` (inclusive) to `stop` (exclusive) are considered. Elements outside that range are discarded. By default, the entire array is considered.
Examples:
  * `#[1, 2, 5, 2, 7, 7].[filter](Basic-Types/Arrays/#Array___filter "Documentation for Array.filter") (· > 2) = #[5, 7, 7]`
  * `#[1, 2, 5, 2, 7, 7].[filter](Basic-Types/Arrays/#Array___filter "Documentation for Array.filter") (fun _ => [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) = #[]`
  * `#[1, 2, 5, 2, 7, 7].[filter](Basic-Types/Arrays/#Array___filter "Documentation for Array.filter") (fun _ => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) = #[1, 2, 5, 2, 7, 7]`
  * `#[1, 2, 5, 2, 7, 7].[filter](Basic-Types/Arrays/#Array___filter "Documentation for Array.filter") (· > 2) (start := 3) = #[7, 7]`
  * `#[1, 2, 5, 2, 7, 7].[filter](Basic-Types/Arrays/#Array___filter "Documentation for Array.filter") (fun _ => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) (start := 3) = #[2, 7, 7]`
  * `#[1, 2, 5, 2, 7, 7].[filter](Basic-Types/Arrays/#Array___filter "Documentation for Array.filter") (fun _ => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) (stop := 3) = #[1, 2, 5]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.filterM "Permalink")def
```


Array.filterM.{u_1} {m : Type → Type u_1} {α : Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)


Array.filterM.{u_1} {m : Type → Type u_1}
  {α : Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)


```

Applies the monadic predicate `p` to every element in the array, in order from left to right, and returns the array of elements for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Only elements from `start` (inclusive) to `stop` (exclusive) are considered. Elements outside that range are discarded. By default, the entire array is checked.
Example:
``#[1, 2, 2]``Checking 1 Checking 2 Checking 5 Checking 2 Checking 7 Checking 7 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #[1, 2, 5, 2, 7, 7].[filterM](Basic-Types/Arrays/#Array___filterM "Documentation for Array.filterM") fun x => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Checking {x}" return x < 3 ``Checking 1 Checking 2 Checking 5 Checking 2 Checking 7 Checking 7``#[1, 2, 2]`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.filterRevM "Permalink")def
```


Array.filterRevM.{u_1} {m : Type → Type u_1} {α : Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size"))
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) : m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)


Array.filterRevM.{u_1}
  {m : Type → Type u_1} {α : Type}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size"))
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) : m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)


```

Applies the monadic predicate `p` on every element in the array in reverse order, from right to left, and returns those elements for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`. The elements of the returned list are in the same order as in the input list.
Only elements from `start` (exclusive) to `stop` (inclusive) are considered. Elements outside that range are discarded. Because the array is examined in reverse order, elements are only examined when `start > stop`. By default, the entire array is considered.
Example:
``#[1, 2, 2]``Checking 7 Checking 7 Checking 2 Checking 5 Checking 2 Checking 1 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #[1, 2, 5, 2, 7, 7].[filterRevM](Basic-Types/Arrays/#Array___filterRevM "Documentation for Array.filterRevM") fun x => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Checking {x}" return x < 3 ``Checking 7 Checking 7 Checking 2 Checking 5 Checking 2 Checking 1``#[1, 2, 2]`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.filterMap "Permalink")def
```


Array.filterMap.{u, u_1} {α : Type u} {β : Type u_1} (f : α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


Array.filterMap.{u, u_1} {α : Type u}
  {β : Type u_1} (f : α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


```

Applies a function that returns an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` to each element of an array, collecting the non-`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` values.
Example:
``#[10, 14, 14]`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #[1, 2, 5, 2, 7, 7].[filterMap](Basic-Types/Arrays/#Array___filterMap "Documentation for Array.filterMap") fun x => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x > 2 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (2 * x) [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") ``#[10, 14, 14]`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.filterMapM "Permalink")def
```


Array.filterMapM.{u, u_1, u_2} {α : Type u} {m : Type u_1 → Type u_2}
  {β : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β)


Array.filterMapM.{u, u_1, u_2}
  {α : Type u} {m : Type u_1 → Type u_2}
  {β : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β)


```

Applies a monadic function that returns an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` to each element of an array, collecting the non-`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` values.
Only elements from `start` (inclusive) to `stop` (exclusive) are considered. Elements outside that range are discarded. By default, the entire array is considered.
Example:
``#[10, 14, 14]``Examining 1 Examining 2 Examining 5 Examining 2 Examining 7 Examining 7 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #[1, 2, 5, 2, 7, 7].[filterMapM](Basic-Types/Arrays/#Array___filterMapM "Documentation for Array.filterMapM") fun x => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Examining {x}" if x > 2 then return [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (2 * x) else return [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") ``Examining 1 Examining 2 Examining 5 Examining 2 Examining 7 Examining 7``#[10, 14, 14]`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.filterSepElems "Permalink")def
```


Array.filterSepElems (a : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")) (p : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")


Array.filterSepElems
  (a : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax"))
  (p : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")


```

Filters an array of syntax, treating every other element as a separator rather than an element to test with the predicate `p`. The resulting array contains the tested elements for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, separated by the corresponding separator elements.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.filterSepElemsM "Permalink")def
```


Array.filterSepElemsM {m : Type → Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (a : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax")) (p : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax") → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax"))


Array.filterSepElemsM {m : Type → Type}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (a : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax"))
  (p : [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax") → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  m ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Lean.Syntax](Notations-and-Macros/Defining-New-Syntax/#Lean___Syntax___missing "Documentation for Lean.Syntax"))


```

Filters an array of syntax, treating every other element as a separator rather than an element to test with the monadic predicate `p`. The resulting array contains the tested elements for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, separated by the corresponding separator elements.
###  20.16.4.11. Partitioning[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--API-Reference--Partitioning "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.partition "Permalink")def
```


Array.partition.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.partition.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Returns a pair of arrays that together contain all the elements of `as`. The first array contains those elements for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, and the second contains those for which `p` returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
`as.[partition](Basic-Types/Arrays/#Array___partition "Documentation for Array.partition") p` is equivalent to `(as.[filter](Basic-Types/Arrays/#Array___filter "Documentation for Array.filter") p, as.[filter](Basic-Types/Arrays/#Array___filter "Documentation for Array.filter") ([not](Basic-Types/Booleans/#Bool___not "Documentation for Bool.not") ∘ p))`, but it is more efficient since it only has to do one pass over the array.
Examples:
  * `#[1, 2, 5, 2, 7, 7].[partition](Basic-Types/Arrays/#Array___partition "Documentation for Array.partition") (· > 2) = (#[5, 7, 7], #[1, 2, 2])`
  * `#[1, 2, 5, 2, 7, 7].[partition](Basic-Types/Arrays/#Array___partition "Documentation for Array.partition") (fun _ => [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) = (#[], #[1, 2, 5, 2, 7, 7])`
  * `#[1, 2, 5, 2, 7, 7].[partition](Basic-Types/Arrays/#Array___partition "Documentation for Array.partition") (fun _ => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) = (#[1, 2, 5, 2, 7, 7], #[])`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.groupByKey "Permalink")def
```


Array.groupByKey.{u, v} {α : Type u} {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (key : β → α) (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β)


Array.groupByKey.{u, v} {α : Type u}
  {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (key : β → α) (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β) :
  [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β)


```

Groups the elements of an array `xs` according to the function `key`, returning a hash map in which each group is associated with its key. Groups preserve the relative order of elements in `xs`.
Example:
``Std.HashMap.ofList [(0, #[0, 2, 4, 6]), (1, #[1, 3, 5])]`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #[0, 1, 2, 3, 4, 5, 6].[groupByKey](Basic-Types/Arrays/#Array___groupByKey "Documentation for Array.groupByKey") (· % 2) ``[Std.HashMap.ofList](Basic-Types/Maps-and-Sets/#Std___HashMap___ofList "Documentation for Std.HashMap.ofList") [(0, #[0, 2, 4, 6]), (1, #[1, 3, 5])]`
###  20.16.4.12. Element Predicates[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--API-Reference--Element-Predicates "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.contains "Permalink")def
```


Array.contains.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Array.contains.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether `a` is an element of `as`, using `==` to compare elements.
`[Array.elem](Basic-Types/Arrays/#Array___elem "Documentation for Array.elem")` is a synonym that takes the element before the array.
Examples:
  * `#[1, 4, 2, 3, 3, 7].[contains](Basic-Types/Arrays/#Array___contains "Documentation for Array.contains") 3 = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[Array.contains](Basic-Types/Arrays/#Array___contains "Documentation for Array.contains") #[1, 4, 2, 3, 3, 7] 5 = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.elem "Permalink")def
```


Array.elem.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (a : α) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Array.elem.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (a : α) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether `a` is an element of `as`, using `==` to compare elements.
`[Array.contains](Basic-Types/Arrays/#Array___contains "Documentation for Array.contains")` is a synonym that takes the array before the element.
For verification purposes, `[Array.elem](Basic-Types/Arrays/#Array___elem "Documentation for Array.elem")` is simplified to `[Array.contains](Basic-Types/Arrays/#Array___contains "Documentation for Array.contains")`.
Example:
  * `[Array.elem](Basic-Types/Arrays/#Array___elem "Documentation for Array.elem") 3 #[1, 4, 2, 3, 3, 7] = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[Array.elem](Basic-Types/Arrays/#Array___elem "Documentation for Array.elem") 5 #[1, 4, 2, 3, 3, 7] = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.find? "Permalink")def
```


Array.find?.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Array.find?.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Returns the first element of the array for which the predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such element is found.
Examples:
  * `#[7, 6, 5, 8, 1, 2, 6].[find?](Basic-Types/Arrays/#Array___find___ "Documentation for Array.find?") (· < 5) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 1`
  * `#[7, 6, 5, 8, 1, 2, 6].[find?](Basic-Types/Arrays/#Array___find___ "Documentation for Array.find?") (· < 1) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.findRev? "Permalink")def
```


Array.findRev? {α : Type} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Array.findRev? {α : Type} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Returns the last element of the array for which the predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such element is found.
Examples:
  * `#[7, 6, 5, 8, 1, 2, 6].[findRev?](Basic-Types/Arrays/#Array___findRev___ "Documentation for Array.findRev?") (· < 5) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2`
  * `#[7, 6, 5, 8, 1, 2, 6].[findRev?](Basic-Types/Arrays/#Array___findRev___ "Documentation for Array.findRev?") (· < 1) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.findIdx "Permalink")def
```


Array.findIdx.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Array.findIdx.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the index of the first element for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, or the size of the array if there is no such element.
Examples:
  * `#[7, 6, 5, 8, 1, 2, 6].[findIdx](Basic-Types/Arrays/#Array___findIdx "Documentation for Array.findIdx") (· < 5) = 4`
  * `#[7, 6, 5, 8, 1, 2, 6].[findIdx](Basic-Types/Arrays/#Array___findIdx "Documentation for Array.findIdx") (· < 1) = 7`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.findIdx? "Permalink")def
```


Array.findIdx?.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Array.findIdx?.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the index of the first element for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if there is no such element.
Examples:
  * `#[7, 6, 5, 8, 1, 2, 6].[findIdx](Basic-Types/Arrays/#Array___findIdx "Documentation for Array.findIdx") (· < 5) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 4`
  * `#[7, 6, 5, 8, 1, 2, 6].[findIdx](Basic-Types/Arrays/#Array___findIdx "Documentation for Array.findIdx") (· < 1) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.findIdxM? "Permalink")def
```


Array.findIdxM?.{u, u_1} {α : Type u} {m : Type → Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))


Array.findIdxM?.{u, u_1} {α : Type u}
  {m : Type → Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))


```

Finds the index of the first element of an array for which the monadic predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`. Elements are examined in order from left to right, and the search is terminated when an element that satisfies `p` is found. If no such element exists in the array, then `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` is returned.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.findFinIdx? "Permalink")def
```


Array.findFinIdx?.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size"))


Array.findFinIdx?.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size"))


```

Returns the index of the first element for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if there is no such element. The index is returned as a `[Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin")`, which guarantees that it is in bounds.
Examples:
  * `#[7, 6, 5, 8, 1, 2, 6].[findFinIdx?](Basic-Types/Arrays/#Array___findFinIdx___ "Documentation for Array.findFinIdx?") (· < 5) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (4 : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") 7)`
  * `#[7, 6, 5, 8, 1, 2, 6].[findFinIdx?](Basic-Types/Arrays/#Array___findFinIdx___ "Documentation for Array.findFinIdx?") (· < 1) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.findM? "Permalink")def
```


Array.findM?.{u_1} {m : Type → Type u_1} {α : Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)


Array.findM?.{u_1} {m : Type → Type u_1}
  {α : Type} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)


```

Returns the first element of the array for which the monadic predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such element is found. Elements of the array are checked in order.
The monad `m` is restricted to `Type → Type` to avoid needing to use `[ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` in `p`'s type.
Example:
``some 1``Almost! 6 Almost! 5 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #[7, 6, 5, 8, 1, 2, 6].[findM?](Basic-Types/Arrays/#Array___findM___ "Documentation for Array.findM?") fun i => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") if i < 5 then return [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") if i ≤ 6 then [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Almost! {i}" return [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") ``Almost! 6 Almost! 5``[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 1`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.findRevM? "Permalink")def
```


Array.findRevM?.{w} {α : Type} {m : Type → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)


Array.findRevM?.{w} {α : Type}
  {m : Type → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)


```

Returns the last element of the array for which the monadic predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such element is found. Elements of the array are checked in reverse, from right to left..
The monad `m` is restricted to `Type → Type` to avoid needing to use `[ULift](The-Type-System/Universes/#ULift___up "Documentation for ULift") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` in `p`'s type.
Example:
``some 2``Almost! 5 Almost! 6 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #[7, 5, 8, 1, 2, 6, 5, 8].[findRevM?](Basic-Types/Arrays/#Array___findRevM___ "Documentation for Array.findRevM?") fun i => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") if i < 5 then return [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") if i ≤ 6 then [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Almost! {i}" return [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") ``Almost! 5 Almost! 6``[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 2`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.findSome? "Permalink")def
```


Array.findSome?.{u, v} {α : Type u} {β : Type v} (f : α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


Array.findSome?.{u, v} {α : Type u}
  {β : Type v} (f : α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


```

Returns the first non-`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` result of applying the function `f` to each element of the array, in order. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if `f` returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` for all elements.
Example:
``some 10`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #[7, 6, 5, 8, 1, 2, 6].[findSome?](Basic-Types/Arrays/#Array___findSome___ "Documentation for Array.findSome?") fun i => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") i < 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (i * 10) [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") ``[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 10`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.findSome! "Permalink")def
```


Array.findSome!.{u, v} {α : Type u} {β : Type v} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") β]
  (f : α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β) (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : β


Array.findSome!.{u, v} {α : Type u}
  {β : Type v} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") β]
  (f : α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β) (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : β


```

Returns the first non-`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` result of applying the function `f` to each element of the array, in order. Panics if `f` returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` for all elements.
Example:
``some 10`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #[7, 6, 5, 8, 1, 2, 6].[findSome?](Basic-Types/Arrays/#Array___findSome___ "Documentation for Array.findSome?") fun i => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") i < 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (i * 10) [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") ``[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 10`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.findSomeM? "Permalink")def
```


Array.findSomeM?.{u, v, w} {α : Type u} {β : Type v}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β))
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


Array.findSomeM?.{u, v, w} {α : Type u}
  {β : Type v} {m : Type v → Type w}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β))
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


```

Returns the first non-`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` result of applying the monadic function `f` to each element of the array, in order. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if `f` returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` for all elements.
Example:
``some 10``Almost! 6 Almost! 5 `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #[7, 6, 5, 8, 1, 2, 6].[findSomeM?](Basic-Types/Arrays/#Array___findSomeM___ "Documentation for Array.findSomeM?") fun i => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") if i < 5 then return [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (i * 10) if i ≤ 6 then [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") s!"Almost! {i}" return [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") ``Almost! 6 Almost! 5``[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 10`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.findSomeRev? "Permalink")def
```


Array.findSomeRev?.{u, v} {α : Type u} {β : Type v} (f : α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


Array.findSomeRev?.{u, v} {α : Type u}
  {β : Type v} (f : α → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


```

Returns the first non-`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` result of applying `f` to each element of the array in reverse order, from right to left. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if `f` returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` for all elements of the array.
Examples:
  * `#[7, 6, 5, 8, 1, 2, 6].[findSome?](Basic-Types/Arrays/#Array___findSome___ "Documentation for Array.findSome?") (fun x => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x < 5 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (10 * x) [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 10`
  * `#[7, 6, 5, 8, 1, 2, 6].[findSome?](Basic-Types/Arrays/#Array___findSome___ "Documentation for Array.findSome?") (fun x => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") x < 1 [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (10 * x) [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")) = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.findSomeRevM? "Permalink")def
```


Array.findSomeRevM?.{u, v, w} {α : Type u} {β : Type v}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β))
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


Array.findSomeRevM?.{u, v, w} {α : Type u}
  {β : Type v} {m : Type v → Type w}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β))
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


```

Returns the first non-`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` result of applying the monadic function `f` to each element of the array in reverse order, from right to left. Once a non-`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` result is found, no further elements are checked. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if `f` returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` for all elements of the array.
Examples:
``Except.ok (some (-4))`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #[1, 2, 0, -4, 1].[findSomeRevM?](Basic-Types/Arrays/#Array___findSomeRevM___ "Documentation for Array.findSomeRevM?") (m := [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) fun x => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") if x = 0 then [throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") "Zero!" else if x < 0 then return ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x) else return [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") ``[Except.ok](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.ok") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (-4))```Except.error "Zero!"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #[1, 2, 0, 4, 1].[findSomeRevM?](Basic-Types/Arrays/#Array___findSomeRevM___ "Documentation for Array.findSomeRevM?") (m := [Except](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) fun x => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") if x = 0 then [throw](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#MonadExcept___mk "Documentation for MonadExcept.throw") "Zero!" else if x < 0 then return ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x) else return [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") ``[Except.error](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Except___error "Documentation for Except.error") "Zero!"`
[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=Array.every%E2%86%AAArray.all "Permalink")def
```


Array.all.{u} {α : Type u} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Array.all.{u} {α : Type u} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for every element of `as`.
Short-circuits upon encountering the first `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
The optional parameters `start` and `stop` control the region of the array to be checked. Only the elements with indices from `start` (inclusive) to `stop` (exclusive) are checked. By default, the entire array is checked.
Examples:
  * `#[a, b, c].[all](Basic-Types/Arrays/#Array___all "Documentation for Array.all") p = (p a && (p b && p c))`
  * `#[2, 4, 6].[all](Basic-Types/Arrays/#Array___all "Documentation for Array.all") (· % 2 = 0) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `#[2, 4, 5, 6].[all](Basic-Types/Arrays/#Array___all "Documentation for Array.all") (· % 2 = 0) = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.allM "Permalink")def
```


Array.allM.{u, w} {α : Type u} {m : Type → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Array.allM.{u, w} {α : Type u}
  {m : Type → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the monadic predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for every element of `as`.
Short-circuits upon encountering the first `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`. The elements in `as` are examined in order from left to right.
The optional parameters `start` and `stop` control the region of the array to be checked. Only the elements with indices from `start` (inclusive) to `stop` (exclusive) are checked. By default, the entire array is checked.
[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=Array.some%E2%86%AAArray.any "Permalink")def
```


Array.any.{u} {α : Type u} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Array.any.{u} {α : Type u} (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for any element of `as`.
Short-circuits upon encountering the first `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
The optional parameters `start` and `stop` control the region of the array to be checked. Only the elements with indices from `start` (inclusive) to `stop` (exclusive) are checked. By default, the entire array is checked.
Examples:
  * `#[2, 4, 6].[any](Basic-Types/Arrays/#Array___any "Documentation for Array.any") (· % 2 = 0) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `#[2, 4, 6].[any](Basic-Types/Arrays/#Array___any "Documentation for Array.any") (· % 2 = 1) = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `#[2, 4, 5, 6].[any](Basic-Types/Arrays/#Array___any "Documentation for Array.any") (· % 2 = 0) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `#[2, 4, 5, 6].[any](Basic-Types/Arrays/#Array___any "Documentation for Array.any") (· % 2 = 1) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.anyM "Permalink")def
```


Array.anyM.{u, w} {α : Type u} {m : Type → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Array.anyM.{u, w} {α : Type u}
  {m : Type → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the monadic predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for any element of `as`.
Short-circuits upon encountering the first `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`. The elements in `as` are examined in order from left to right.
The optional parameters `start` and `stop` control the region of the array to be checked. Only the elements with indices from `start` (inclusive) to `stop` (exclusive) are checked. By default, the entire array is checked.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.allDiff "Permalink")def
```


Array.allDiff.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Array.allDiff.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (as : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if no two elements of `as` are equal according to the `==` operator.
Examples:
  * `#["red", "green", "blue"].[allDiff](Basic-Types/Arrays/#Array___allDiff "Documentation for Array.allDiff") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `#["red", "green", "red"].[allDiff](Basic-Types/Arrays/#Array___allDiff "Documentation for Array.allDiff") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `(#[] : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")).[allDiff](Basic-Types/Arrays/#Array___allDiff "Documentation for Array.allDiff") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.isEqv "Permalink")def
```


Array.isEqv.{u} {α : Type u} (xs ys : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (p : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Array.isEqv.{u} {α : Type u}
  (xs ys : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (p : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if `as` and `bs` have the same length and they are pairwise related by `eqv`.
Short-circuits at the first non-related pair of elements.
Examples:
  * `#[1, 2, 3].[isEqv](Basic-Types/Arrays/#Array___isEqv "Documentation for Array.isEqv") #[2, 3, 4] (· < ·) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `#[1, 2, 3].[isEqv](Basic-Types/Arrays/#Array___isEqv "Documentation for Array.isEqv") #[2, 2, 4] (· < ·) = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `#[1, 2, 3].[isEqv](Basic-Types/Arrays/#Array___isEqv "Documentation for Array.isEqv") #[2, 3] (· < ·) = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


###  20.16.4.13. Comparisons[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--API-Reference--Comparisons "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.isPrefixOf "Permalink")def
```


Array.isPrefixOf.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (as bs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Array.isPrefixOf.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (as bs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Return `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if `as` is a prefix of `bs`, or `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` otherwise.
Examples:
  * `#[0, 1, 2].[isPrefixOf](Basic-Types/Arrays/#Array___isPrefixOf "Documentation for Array.isPrefixOf") #[0, 1, 2, 3] = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `#[0, 1, 2].[isPrefixOf](Basic-Types/Arrays/#Array___isPrefixOf "Documentation for Array.isPrefixOf") #[0, 1, 2] = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `#[0, 1, 2].[isPrefixOf](Basic-Types/Arrays/#Array___isPrefixOf "Documentation for Array.isPrefixOf") #[0, 1] = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `#[].[isPrefixOf](Basic-Types/Arrays/#Array___isPrefixOf "Documentation for Array.isPrefixOf") #[0, 1] = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.lex "Permalink")def
```


Array.lex.{u_1} {α : Type u_1} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] (as bs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (lt : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := by exact (· < ·)) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Array.lex.{u_1} {α : Type u_1} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  (as bs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (lt : α → α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := by
    exact (· < ·)) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Compares arrays lexicographically with respect to a comparison `lt` on their elements.
Specifically, `[Array.lex](Basic-Types/Arrays/#Array___lex "Documentation for Array.lex") as bs lt` is true if
  * `bs` is larger than `as` and `as` is pairwise equivalent via `==` to the initial segment of `bs`, or
  * there is an index `i` such that `lt as[i] bs[i]`, and for all `j < i`, `as[j] == bs[j]`.


###  20.16.4.14. Termination Helpers[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--API-Reference--Termination-Helpers "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.attach "Permalink")def
```


Array.attach.{u_1} {α : Type u_1} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x ∈ xs [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


Array.attach.{u_1} {α : Type u_1}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x ∈ xs [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


```

“Attaches” the proof that the elements of `xs` are in fact elements of `xs`, producing a new array with the same elements but in the subtype `{ x // x ∈ xs }`.
`O(1)`.
This function is primarily used to allow definitions by [well-founded recursion](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=well-founded-recursion) that use higher-order functions (such as `[Array.map](Basic-Types/Arrays/#Array___map "Documentation for Array.map")`) to prove that an value taken from a list is smaller than the list. This allows the well-founded recursion mechanism to prove that the function terminates.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.attachWith "Permalink")def
```


Array.attachWith.{u_1} {α : Type u_1} (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (P : α → Prop)
  (H : ∀ (x : α), x ∈ xs → P x) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") P x [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


Array.attachWith.{u_1} {α : Type u_1}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (P : α → Prop)
  (H : ∀ (x : α), x ∈ xs → P x) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") P x [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


```

“Attaches” individual proofs to an array of values that satisfy a predicate `P`, returning an array of elements in the corresponding subtype `{ x // P x }`.
`O(1)`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.unattach "Permalink")def
```


Array.unattach.{u_1} {α : Type u_1} {p : α → Prop}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") p x [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Array.unattach.{u_1} {α : Type u_1}
  {p : α → Prop}
  (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") x [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") p x [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Maps an array of terms in a subtype to the corresponding terms in the type by forgetting that they satisfy the predicate.
This is the inverse of `[Array.attachWith](Basic-Types/Arrays/#Array___attachWith "Documentation for Array.attachWith")` and a synonym for `xs.[map](Basic-Types/Arrays/#Array___map "Documentation for Array.map") (·.val)`.
Mostly this should not be needed by users. It is introduced as an intermediate step by lemmas such as `map_subtype`, and is ideally subsequently simplified away by `unattach_attach`.
This function is usually inserted automatically by Lean as an intermediate step while proving termination. It is rarely used explicitly in code. It is introduced as an intermediate step during the elaboration of definitions by [well-founded recursion](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=well-founded-recursion). If this function is encountered in a proof state, the right approach is usually the tactic `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [Array.unattach, -Array.map_subtype]`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Array.pmap "Permalink")def
```


Array.pmap.{u_1, u_2} {α : Type u_1} {β : Type u_2} {P : α → Prop}
  (f : (a : α) → P a → β) (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) (H : ∀ (a : α), a ∈ xs → P a) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


Array.pmap.{u_1, u_2} {α : Type u_1}
  {β : Type u_2} {P : α → Prop}
  (f : (a : α) → P a → β) (xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (H : ∀ (a : α), a ∈ xs → P a) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


```

Maps a partially defined function (defined on those terms of `α` that satisfy a predicate `P`) over an array `xs : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α`, given a proof that every element of `xs` in fact satisfies `P`.
`[Array.pmap](Basic-Types/Arrays/#Array___pmap "Documentation for Array.pmap")`, named for “partial map,” is the equivalent of `[Array.map](Basic-Types/Arrays/#Array___map "Documentation for Array.map")` for such partial functions.
##  20.16.5. Subarrays[🔗](find/?domain=Verso.Genre.Manual.section&name=subarray "Permalink")
The type `[Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α` is an abbreviations for `Std.Slice α`. This means that, in addition to the operators in this section, [generalized field notation](Terms/Function-Application/#--tech-term-generalized-field-notation) can be used to call functions in the `Std.Slice` namespace, such as `Std.Slice.foldl`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray "Permalink")def
```


Subarray.{u} (α : Type u) : Type u


Subarray.{u} (α : Type u) : Type u


```

A region of some underlying array.
A subarray contains an array together with the start and end indices of a region of interest. Subarrays can be used to avoid copying or allocating space, while being more convenient than tracking the bounds by hand. The region of interest consists of every index that is both greater than or equal to `start` and strictly less than `[stop](Tactic-Proofs/Tactic-Reference/#stop "Documentation for tactic")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.empty "Permalink")def
```


Subarray.empty.{u_1} {α : Type u_1} : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α


Subarray.empty.{u_1} {α : Type u_1} :
  [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α


```

The empty subarray.
This empty subarray is backed by an empty array.
###  20.16.5.1. Array Data[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--Subarrays--Array-Data "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.array "Permalink")def
```


Subarray.array.{u_1} {α : Type u_1} (xs : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Subarray.array.{u_1} {α : Type u_1}
  (xs : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

The underlying array.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.start "Permalink")def
```


Subarray.start.{u_1} {α : Type u_1} (xs : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Subarray.start.{u_1} {α : Type u_1}
  (xs : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The starting index of the region of interest (inclusive).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.stop "Permalink")def
```


Subarray.stop.{u_1} {α : Type u_1} (xs : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Subarray.stop.{u_1} {α : Type u_1}
  (xs : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The ending index of the region of interest (exclusive).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.start_le_stop "Permalink")def
```


Subarray.start_le_stop.{u_1} {α : Type u_1} (xs : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) :
  xs.[start](Basic-Types/Arrays/#Subarray___start "Documentation for Subarray.start") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") xs.[stop](Basic-Types/Arrays/#Subarray___stop "Documentation for Subarray.stop")


Subarray.start_le_stop.{u_1}
  {α : Type u_1} (xs : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) :
  xs.[start](Basic-Types/Arrays/#Subarray___start "Documentation for Subarray.start") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") xs.[stop](Basic-Types/Arrays/#Subarray___stop "Documentation for Subarray.stop")


```

The starting index is no later than the ending index.
The ending index is exclusive. If the starting and ending indices are equal, then the subarray is empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.stop_le_array_size "Permalink")def
```


Subarray.stop_le_array_size.{u_1} {α : Type u_1} (xs : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) :
  xs.[stop](Basic-Types/Arrays/#Subarray___stop "Documentation for Subarray.stop") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") xs.[array](Basic-Types/Arrays/#Subarray___array "Documentation for Subarray.array").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")


Subarray.stop_le_array_size.{u_1}
  {α : Type u_1} (xs : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) :
  xs.[stop](Basic-Types/Arrays/#Subarray___stop "Documentation for Subarray.stop") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") xs.[array](Basic-Types/Arrays/#Subarray___array "Documentation for Subarray.array").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")


```

The stopping index is no later than the end of the array.
The ending index is exclusive. If it is equal to the size of the array, then the last element of the array is in the subarray.
###  20.16.5.2. Resizing[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--Subarrays--Resizing "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.drop "Permalink")def
```


Subarray.drop.{u_1} {α : Type u_1} (arr : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α


Subarray.drop.{u_1} {α : Type u_1}
  (arr : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α


```

Removes the first `i` elements of the subarray. If there are `i` or fewer elements, the resulting subarray is empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.take "Permalink")def
```


Subarray.take.{u_1} {α : Type u_1} (arr : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α


Subarray.take.{u_1} {α : Type u_1}
  (arr : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α


```

Keeps only the first `i` elements of the subarray. If there are `i` or fewer elements, the resulting subarray is empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.popFront "Permalink")def
```


Subarray.popFront.{u_1} {α : Type u_1} (s : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α


Subarray.popFront.{u_1} {α : Type u_1}
  (s : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α


```

Shrinks the subarray by incrementing its starting index if possible, returning it unchanged if not.
Examples:
  * `#[1,2,3].[toSubarray](Basic-Types/Arrays/#Array___toSubarray "Documentation for Array.toSubarray").[popFront](Basic-Types/Arrays/#Subarray___popFront "Documentation for Subarray.popFront").toArray = #[2, 3]`
  * `#[1,2,3].[toSubarray](Basic-Types/Arrays/#Array___toSubarray "Documentation for Array.toSubarray").[popFront](Basic-Types/Arrays/#Subarray___popFront "Documentation for Subarray.popFront").[popFront](Basic-Types/Arrays/#Subarray___popFront "Documentation for Subarray.popFront").toArray = #[3]`
  * `#[1,2,3].[toSubarray](Basic-Types/Arrays/#Array___toSubarray "Documentation for Array.toSubarray").[popFront](Basic-Types/Arrays/#Subarray___popFront "Documentation for Subarray.popFront").[popFront](Basic-Types/Arrays/#Subarray___popFront "Documentation for Subarray.popFront").[popFront](Basic-Types/Arrays/#Subarray___popFront "Documentation for Subarray.popFront").toArray = #[]`
  * `#[1,2,3].[toSubarray](Basic-Types/Arrays/#Array___toSubarray "Documentation for Array.toSubarray").[popFront](Basic-Types/Arrays/#Subarray___popFront "Documentation for Subarray.popFront").[popFront](Basic-Types/Arrays/#Subarray___popFront "Documentation for Subarray.popFront").[popFront](Basic-Types/Arrays/#Subarray___popFront "Documentation for Subarray.popFront").[popFront](Basic-Types/Arrays/#Subarray___popFront "Documentation for Subarray.popFront").toArray = #[]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.split "Permalink")def
```


Subarray.split.{u_1} {α : Type u_1} (s : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α)
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (Std.Slice.size s).[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")) : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α


Subarray.split.{u_1} {α : Type u_1}
  (s : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α)
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (Std.Slice.size s).[succ](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat.succ")) :
  [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α


```

Splits a subarray into two parts, the first of which contains the first `i` elements and the second of which contains the remainder.
###  20.16.5.3. Lookups[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--Subarrays--Lookups "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.get "Permalink")def
```


Subarray.get.{u_1} {α : Type u_1} (s : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α)
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (Std.Slice.size s)) : α


Subarray.get.{u_1} {α : Type u_1}
  (s : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α)
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") (Std.Slice.size s)) : α


```

Extracts an element from the subarray.
The index is relative to the start of the subarray, rather than the underlying array.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.get! "Permalink")def
```


Subarray.get!.{u_1} {α : Type u_1} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (s : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α)
  (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : α


Subarray.get!.{u_1} {α : Type u_1}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (s : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α)
  (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : α


```

Extracts an element from the subarray, or returns a default value when the index is out of bounds.
The index is relative to the start and end of the subarray, rather than the underlying array. The default value is that provided by the `[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α` instance.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.getD "Permalink")def
```


Subarray.getD.{u_1} {α : Type u_1} (s : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (v₀ : α) :
  α


Subarray.getD.{u_1} {α : Type u_1}
  (s : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (v₀ : α) : α


```

Extracts an element from the subarray, or returns a default value `v₀` when the index is out of bounds.
The index is relative to the start and end of the subarray, rather than the underlying array.
###  20.16.5.4. Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--Subarrays--Iteration "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.foldr "Permalink")def
```


Subarray.foldr.{u, v} {α : Type u} {β : Type v} (f : α → β → β)
  (init : β) (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : β


Subarray.foldr.{u, v} {α : Type u}
  {β : Type v} (f : α → β → β) (init : β)
  (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : β


```

Folds an operation from right to left over the elements in a subarray.
An accumulator of type `β` is constructed by starting with `init` and combining each element of the subarray with the current accumulator value in turn, moving from the end to the start.
Examples:
  * `#["red", "green", "blue"].[toSubarray](Basic-Types/Arrays/#Array___toSubarray "Documentation for Array.toSubarray").[foldr](Basic-Types/Arrays/#Subarray___foldr "Documentation for Subarray.foldr") (·.[length](Basic-Types/Strings/#String___length "Documentation for String.length") + ·) 0 = 12`
  * `#["red", "green", "blue"].[toSubarray](Basic-Types/Arrays/#Array___toSubarray "Documentation for Array.toSubarray").[popFront](Basic-Types/Arrays/#Subarray___popFront "Documentation for Subarray.popFront").[foldr](Basic-Types/Arrays/#Subarray___foldr "Documentation for Subarray.foldr") (·.[length](Basic-Types/Strings/#String___length "Documentation for String.length") + ·) 0 = 9`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.foldrM "Permalink")def
```


Subarray.foldrM.{u, v, w} {α : Type u} {β : Type v}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → β → m β) (init : β)
  (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : m β


Subarray.foldrM.{u, v, w} {α : Type u}
  {β : Type v} {m : Type v → Type w}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → β → m β) (init : β)
  (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : m β


```

Folds a monadic operation from right to left over the elements in a subarray.
An accumulator of type `β` is constructed by starting with `init` and monadically combining each element of the subarray with the current accumulator value in turn, moving from the end to the start. The monad in question may permit early termination or repetition.
Examples:
``some "(4)blue (5)green (3)red "`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #["red", "green", "blue"].[toSubarray](Basic-Types/Arrays/#Array___toSubarray "Documentation for Array.toSubarray").[foldrM](Basic-Types/Arrays/#Subarray___foldrM "Documentation for Subarray.foldrM") (init := "") fun x acc => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") let l ← [Option.guard](Basic-Types/Optional-Values/#Option___guard "Documentation for Option.guard") (· ≠ 0) x.[length](Basic-Types/Strings/#String___length "Documentation for String.length") return s!"{acc}({l}){x} " ``[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "(4)blue (5)green (3)red "`
```
#eval #["red", "green", "blue"].toSubarray.foldrM (init := 0) fun x acc => do
  let l ← Option.guard (· ≠ 5) x.length
  return s!"{acc}({l}){x} "

```
`[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.forM "Permalink")def
```


Subarray.forM.{u, v, w} {α : Type u} {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


Subarray.forM.{u, v, w} {α : Type u}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) :
  m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Runs a monadic action on each element of a subarray.
The elements are processed starting at the lowest index and moving up.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.forRevM "Permalink")def
```


Subarray.forRevM.{u, v, w} {α : Type u} {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


Subarray.forRevM.{u, v, w} {α : Type u}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) :
  m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Runs a monadic action on each element of a subarray, in reverse order.
The elements are processed starting at the highest index and moving down.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.forIn "Permalink")def
```


Subarray.forIn.{v, w, u} {α : Type u} {β : Type v} {m : Type v → Type w}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (s : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) (b : β) (f : α → β → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") β)) : m β


Subarray.forIn.{v, w, u} {α : Type u}
  {β : Type v} {m : Type v → Type w}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (s : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) (b : β)
  (f : α → β → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") β)) : m β


```

The implementation of `[ForIn.forIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn.forIn")` for `[Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray")`, which allows it to be used with `for` loops in `do`-notation.
###  20.16.5.5. Element Predicates[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Arrays--Subarrays--Element-Predicates "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.findRev? "Permalink")def
```


Subarray.findRev? {α : Type} (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Subarray.findRev? {α : Type}
  (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Tests each element in a subarray with a Boolean predicate in reverse order, stopping at the first element that satisfies the predicate. The element that satisfies the predicate is returned, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no element satisfies the predicate.
Examples:
  * `#["red", "green", "blue"].[toSubarray](Basic-Types/Arrays/#Array___toSubarray "Documentation for Array.toSubarray").[findRev?](Basic-Types/Arrays/#Subarray___findRev___ "Documentation for Subarray.findRev?") (·.[length](Basic-Types/Strings/#String___length "Documentation for String.length") ≠ 4) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "green"`
  * `#["red", "green", "blue"].[toSubarray](Basic-Types/Arrays/#Array___toSubarray "Documentation for Array.toSubarray").[findRev?](Basic-Types/Arrays/#Subarray___findRev___ "Documentation for Subarray.findRev?") (fun _ => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "blue"`
  * `#["red", "green", "blue"].toSubarray 0 0 |>.findRev? (fun _ => true) = none`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.findRevM? "Permalink")def
```


Subarray.findRevM?.{w} {α : Type} {m : Type → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)


Subarray.findRevM?.{w} {α : Type}
  {m : Type → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)


```

Applies a monadic Boolean predicate to each element in a subarray in reverse order, stopping at the first element that satisfies the predicate. The element that satisfies the predicate is returned, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no element satisfies it.
Example:
``some "green"``blue green `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #["red", "green", "blue"].[toSubarray](Basic-Types/Arrays/#Array___toSubarray "Documentation for Array.toSubarray").[findRevM?](Basic-Types/Arrays/#Subarray___findRevM___ "Documentation for Subarray.findRevM?") fun x => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") x return (x.[length](Basic-Types/Strings/#String___length "Documentation for String.length") = 5) ``blue green``[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.findSomeRevM? "Permalink")def
```


Subarray.findSomeRevM?.{u, v, w} {α : Type u} {β : Type v}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α)
  (f : α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


Subarray.findSomeRevM?.{u, v, w}
  {α : Type u} {β : Type v}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α)
  (f : α → m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)) : m ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β)


```

Applies a monadic function to each element in a subarray in reverse order, stopping at the first element for which the function succeeds by returning a value other than `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`. The succeeding value is returned, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if there is no success.
Example:
``some 5``blue green `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #["red", "green", "blue"].[toSubarray](Basic-Types/Arrays/#Array___toSubarray "Documentation for Array.toSubarray").[findSomeRevM?](Basic-Types/Arrays/#Subarray___findSomeRevM___ "Documentation for Subarray.findSomeRevM?") fun x => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") x return [Option.guard](Basic-Types/Optional-Values/#Option___guard "Documentation for Option.guard") (· = 5) x.[length](Basic-Types/Strings/#String___length "Documentation for String.length") ``blue green``[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5`
[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=Subarray.every%E2%86%AASubarray.all "Permalink")def
```


Subarray.all.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Subarray.all.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether all of the elements in a subarray satisfy a Boolean predicate.
The elements are tested starting at the lowest index and moving up. The search terminates as soon as an element that does not satisfy the predicate is found.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.allM "Permalink")def
```


Subarray.allM.{u, w} {α : Type u} {m : Type → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Subarray.allM.{u, w} {α : Type u}
  {m : Type → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) :
  m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether all of the elements in a subarray satisfy a monadic Boolean predicate.
The elements are tested starting at the lowest index and moving up. The search terminates as soon as an element that does not satisfy the predicate is found.
Example:
``[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")``green blue `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #["red", "green", "blue", "orange"].[toSubarray](Basic-Types/Arrays/#Array___toSubarray "Documentation for Array.toSubarray").[popFront](Basic-Types/Arrays/#Subarray___popFront "Documentation for Subarray.popFront").[allM](Basic-Types/Arrays/#Subarray___allM "Documentation for Subarray.allM") fun x => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") x [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") (x.[length](Basic-Types/Strings/#String___length "Documentation for String.length") == 5) ``green blue``[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=Subarray.some%E2%86%AASubarray.any "Permalink")def
```


Subarray.any.{u} {α : Type u} (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Subarray.any.{u} {α : Type u}
  (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether any of the elements in a subarray satisfy a Boolean predicate.
The elements are tested starting at the lowest index and moving up. The search terminates as soon as an element that satisfies the predicate is found.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Subarray.anyM "Permalink")def
```


Subarray.anyM.{u, w} {α : Type u} {m : Type → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) : m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Subarray.anyM.{u, w} {α : Type u}
  {m : Type → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (p : α → m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (as : [Subarray](Basic-Types/Arrays/#Subarray "Documentation for Subarray") α) :
  m [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether any of the elements in a subarray satisfy a monadic Boolean predicate.
The elements are tested starting at the lowest index and moving up. The search terminates as soon as an element that satisfies the predicate is found.
Example:
``[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")``green blue `[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") #["red", "green", "blue", "orange"].[toSubarray](Basic-Types/Arrays/#Array___toSubarray "Documentation for Array.toSubarray").[popFront](Basic-Types/Arrays/#Subarray___popFront "Documentation for Subarray.popFront").[anyM](Basic-Types/Arrays/#Subarray___anyM "Documentation for Subarray.anyM") fun x => [do](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do "Documentation for syntax") [IO.println](IO/Console-Output/#IO___println "Documentation for IO.println") x [pure](Functors___-Monads-and--do--Notation/#Pure___mk "Documentation for Pure.pure") (x == "blue") ``green blue``[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
##  20.16.6. FFI[🔗](find/?domain=Verso.Genre.Manual.section&name=array-ffi "Permalink")
FFI type
```

```
typedef struct {
    lean_object   m_header;
    size_t        m_size;
    size_t        m_capacity;
    lean_object * m_data[];
} lean_array_object;

```

```

The representation of arrays in C. See [the description of run-time ``](Basic-Types/Arrays/#array-runtime)`[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")`s for more details.
FFI function
```

```
bool lean_is_array(lean_object * o)

```

```

Returns `true` if `o` is an array, or `false` otherwise.
FFI function
```

```
lean_array_object * lean_to_array(lean_object * o)

```

```

Performs a runtime check that `o` is indeed an array. If `o` is not an array, an assertion fails.
[←20.15. Linked Lists](Basic-Types/Linked-Lists/#List "20.15. Linked Lists")[20.17. Byte Arrays→](Basic-Types/Byte-Arrays/#ByteArray "20.17. Byte Arrays")

[←20.16. Arrays](Basic-Types/Arrays/#Array "20.16. Arrays")[20.18. Ranges→](Basic-Types/Ranges/#ranges "20.18. Ranges")
#  20.17. Byte Arrays[🔗](find/?domain=Verso.Genre.Manual.section&name=ByteArray "Permalink")
Byte arrays are a specialized array type that can only contain elements of type `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")`. Due to this restriction, they can use a much more efficient representation, with no pointer indirections. Like other arrays, byte arrays are represented in compiled code as [dynamic arrays](Basic-Types/Arrays/#--tech-term-dynamic-arrays), and the Lean runtime specially optimizes array operations. The operations that modify byte arrays first check the array's [reference count](Run-Time-Code/Reference-Counting/#reference-counting), and if there are no other references to the array, it is modified in place.
There is no literal syntax for byte arrays. `[List.toByteArray](Basic-Types/Linked-Lists/#List___toByteArray "Documentation for List.toByteArray")` can be used to construct an array from a list literal.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.mk "Permalink")structure
```


ByteArray : Type


ByteArray : Type


```

`[ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")` is like `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")`, but with an efficient run-time representation as a packed byte buffer.
#  Constructor

```
[ByteArray.mk](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray.mk")
```

Packs an array of bytes into a `[ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")`.
Converting between `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")` and `[ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")` takes linear time.
#  Fields

```
data : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")
```

The data contained in the byte array.
Converting between `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")` and `[ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")` takes linear time.
##  20.17.1. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Byte-Arrays--API-Reference "Permalink")
###  20.17.1.1. Constructing Byte Arrays[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Byte-Arrays--API-Reference--Constructing-Byte-Arrays "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.empty "Permalink")def
```


ByteArray.empty : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


ByteArray.empty : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


```

Constructs a new empty byte array with initial capacity `0`.
Use `[ByteArray.emptyWithCapacity](Basic-Types/Byte-Arrays/#ByteArray___emptyWithCapacity "Documentation for ByteArray.emptyWithCapacity")` to create an array with a greater initial capacity.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.emptyWithCapacity "Permalink")def
```


ByteArray.emptyWithCapacity (c : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


ByteArray.emptyWithCapacity (c : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


```

Constructs a new empty byte array with initial capacity `c`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.append "Permalink")def
```


ByteArray.append (a b : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


ByteArray.append (a b : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) :
  [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


```

Appends two byte arrays.
In compiled code, calls to `[ByteArray.append](Basic-Types/Byte-Arrays/#ByteArray___append "Documentation for ByteArray.append")` are replaced with the much more efficient `[ByteArray.fastAppend](Basic-Types/Byte-Arrays/#ByteArray___fastAppend "Documentation for ByteArray.fastAppend")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.fastAppend "Permalink")def
```


ByteArray.fastAppend (a b : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


ByteArray.fastAppend (a b : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) :
  [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


```

Appends two byte arrays using fast array primitives instead of converting them into lists and back.
In compiled code, this function replaces calls to `[ByteArray.append](Basic-Types/Byte-Arrays/#ByteArray___append "Documentation for ByteArray.append")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.copySlice "Permalink")def
```


ByteArray.copySlice (src : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (srcOff : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (dest : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray"))
  (destOff len : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (exact : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


ByteArray.copySlice (src : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray"))
  (srcOff : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (dest : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray"))
  (destOff len : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (exact : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") := [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


```

Copies the slice at `[srcOff, srcOff + len)` in `src` to `[destOff, destOff + len)` in `dest`, growing `dest` if necessary. If `exact` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, the capacity will be doubled when grown.
###  20.17.1.2. Size[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Byte-Arrays--API-Reference--Size "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.size "Permalink")def
```


ByteArray.size : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


ByteArray.size : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the number of bytes in the byte array.
This is the number of bytes actually in the array, as distinct from its capacity, which is the amount of memory presently allocated for the array.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.usize "Permalink")def
```


ByteArray.usize (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


ByteArray.usize (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")


```

Retrieves the size of the array as a platform-specific fixed-width integer.
Because `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")` is big enough to address all memory on every platform that Lean supports, there are in practice no `[ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")`s that have more elements that `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")` can count.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.isEmpty "Permalink")def
```


ByteArray.isEmpty (s : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


ByteArray.isEmpty (s : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` when `s` contains zero bytes.
###  20.17.1.3. Lookups[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Byte-Arrays--API-Reference--Lookups "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.get "Permalink")def
```


ByteArray.get (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (h : i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") a.[size](Basic-Types/Byte-Arrays/#ByteArray___size "Documentation for ByteArray.size") := by get_elem_tactic) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


ByteArray.get (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (h : i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") a.[size](Basic-Types/Byte-Arrays/#ByteArray___size "Documentation for ByteArray.size") := by get_elem_tactic) :
  [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Retrieves the byte at the indicated index. Callers must prove that the index is in bounds.
Use `uget` for a more efficient alternative or `get!` for a variant that panics if the index is out of bounds.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.uget "Permalink")def
```


ByteArray.uget (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (i : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize"))
  (h : i.[toNat](Basic-Types/Fixed-Precision-Integers/#USize___toNat "Documentation for USize.toNat") [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") a.[size](Basic-Types/Byte-Arrays/#ByteArray___size "Documentation for ByteArray.size") := by get_elem_tactic) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


ByteArray.uget (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (i : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize"))
  (h : i.[toNat](Basic-Types/Fixed-Precision-Integers/#USize___toNat "Documentation for USize.toNat") [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") a.[size](Basic-Types/Byte-Arrays/#ByteArray___size "Documentation for ByteArray.size") := by
    get_elem_tactic) :
  [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Retrieves the byte at the indicated index. Callers must prove that the index is in bounds. The index is represented by a platform-specific fixed-width integer (either 32 or 64 bits).
Because `[USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")` is big enough to address all memory on every platform that Lean supports, there are in practice no `[ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")`s for which `uget` cannot retrieve all elements.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.get! "Permalink")def
```


ByteArray.get! : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


ByteArray.get! : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Retrieves the byte at the indicated index. Panics if the index is out of bounds.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.extract "Permalink")def
```


ByteArray.extract (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (b e : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


ByteArray.extract (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray"))
  (b e : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


```

Copies the bytes with indices `b` (inclusive) to `e` (exclusive) to a new `[ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")`.
###  20.17.1.4. Conversions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Byte-Arrays--API-Reference--Conversions "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.toList "Permalink")def
```


ByteArray.toList (bs : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


ByteArray.toList (bs : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Converts a packed array of bytes to a linked list.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.toUInt64BE! "Permalink")def
```


ByteArray.toUInt64BE! (bs : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


ByteArray.toUInt64BE! (bs : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) :
  [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Interprets a `[ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")` of size 8 as a big-endian `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`.
Panics if the array's size is not 8.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.toUInt64LE! "Permalink")def
```


ByteArray.toUInt64LE! (bs : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


ByteArray.toUInt64LE! (bs : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) :
  [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Interprets a `[ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")` of size 8 as a little-endian `[UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")`.
Panics if the array's size is not 8.
####  20.17.1.4.1. UTF-8[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Byte-Arrays--API-Reference--Conversions--UTF-8 "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.utf8Decode? "Permalink")def
```


ByteArray.utf8Decode? (b : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))


ByteArray.utf8Decode? (b : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))


```

Decodes a sequence of characters from their UTF-8 representation. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the bytes are not a sequence of Unicode scalar values.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.utf8DecodeChar? "Permalink")def
```


ByteArray.utf8DecodeChar? (bytes : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


ByteArray.utf8DecodeChar?
  (bytes : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Decodes and returns the `[Char](Basic-Types/Characters/#Char___mk "Documentation for Char")` whose UTF-8 encoding begins at `i` in `bytes`.
Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if `i` is not the start of a valid UTF-8 encoding of a character.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.utf8DecodeChar "Permalink")def
```


ByteArray.utf8DecodeChar (bytes : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (h : (bytes.[utf8DecodeChar?](Basic-Types/Byte-Arrays/#ByteArray___utf8DecodeChar___ "Documentation for ByteArray.utf8DecodeChar?") i).[isSome](Basic-Types/Optional-Values/#Option___isSome "Documentation for Option.isSome") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


ByteArray.utf8DecodeChar
  (bytes : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (h :
    (bytes.[utf8DecodeChar?](Basic-Types/Byte-Arrays/#ByteArray___utf8DecodeChar___ "Documentation for ByteArray.utf8DecodeChar?") i).[isSome](Basic-Types/Optional-Values/#Option___isSome "Documentation for Option.isSome") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")
      [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) :
  [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Decodes and returns the `[Char](Basic-Types/Characters/#Char___mk "Documentation for Char")` whose UTF-8 encoding begins at `i` in `bytes`.
This function requires a proof that there is, in fact, a valid `[Char](Basic-Types/Characters/#Char___mk "Documentation for Char")` at `i`. `utf8DecodeChar?` is an alternative function that returns `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")` instead of requiring a proof ahead of time.
###  20.17.1.5. Modification[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Byte-Arrays--API-Reference--Modification "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.push "Permalink")def
```


ByteArray.push : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray") → [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


ByteArray.push :
  [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray") → [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


```

Adds an element to the end of an array. The resulting array's size is one greater than the input array. If there are no other references to the array, then it is modified in-place.
This takes amortized `O(1)` time because `[ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")` is represented by a dynamic array.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.set "Permalink")def
```


ByteArray.set (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → (h : [autoParam](Terms/Function-Application/#autoParam "Documentation for autoParam") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") a.[size](Basic-Types/Byte-Arrays/#ByteArray___size "Documentation for ByteArray.size")[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") ByteArray.set._auto_1) → [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


ByteArray.set (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") →
    (h :
        [autoParam](Terms/Function-Application/#autoParam "Documentation for autoParam") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")i [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") a.[size](Basic-Types/Byte-Arrays/#ByteArray___size "Documentation for ByteArray.size")[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")
          ByteArray.set._auto_1) →
      [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


```

Replaces the byte at the given index.
No bounds check is performed, but the function requires a proof that the index is in bounds. This proof can usually be omitted, and will be synthesized automatically.
The array is modified in-place if there are no other references to it.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.uset "Permalink")def
```


ByteArray.uset (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (i : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) :
  [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") →
    (h : [autoParam](Terms/Function-Application/#autoParam "Documentation for autoParam") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")i.[toNat](Basic-Types/Fixed-Precision-Integers/#USize___toNat "Documentation for USize.toNat") [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") a.[size](Basic-Types/Byte-Arrays/#ByteArray___size "Documentation for ByteArray.size")[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") ByteArray.uset._auto_1) →
      [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


ByteArray.uset (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray"))
  (i : [USize](Basic-Types/Fixed-Precision-Integers/#USize___ofBitVec "Documentation for USize")) :
  [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") →
    (h :
        [autoParam](Terms/Function-Application/#autoParam "Documentation for autoParam") [(](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")i.[toNat](Basic-Types/Fixed-Precision-Integers/#USize___toNat "Documentation for USize.toNat") [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") a.[size](Basic-Types/Byte-Arrays/#ByteArray___size "Documentation for ByteArray.size")[)](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt")
          ByteArray.uset._auto_1) →
      [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


```

Replaces the byte at the given index.
No bounds check is performed, but the function requires a proof that the index is in bounds. This proof can usually be omitted, and will be synthesized automatically.
The array is modified in-place if there are no other references to it.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.set! "Permalink")def
```


ByteArray.set! : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


ByteArray.set! :
  [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


```

Replaces the byte at the given index.
The array is modified in-place if there are no other references to it.
If the index is out of bounds, the array is returned unmodified.
###  20.17.1.6. Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Byte-Arrays--API-Reference--Iteration "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.foldl "Permalink")def
```


ByteArray.foldl.{v} {β : Type v} (f : β → [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → β) (init : β)
  (as : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Byte-Arrays/#ByteArray___size "Documentation for ByteArray.size")) : β


ByteArray.foldl.{v} {β : Type v}
  (f : β → [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → β) (init : β)
  (as : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Byte-Arrays/#ByteArray___size "Documentation for ByteArray.size")) : β


```

A left fold on `[ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")` that iterates over an array from low to high indices, computing a running value.
Each element of the array is combined with the value from the prior elements using a function `f`. The initial value `init` is the starting value before any elements have been processed.
`[ByteArray.foldlM](Basic-Types/Byte-Arrays/#ByteArray___foldlM "Documentation for ByteArray.foldlM")` is a monadic variant of this function.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.foldlM "Permalink")def
```


ByteArray.foldlM.{v, w} {β : Type v} {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : β → [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → m β) (init : β) (as : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Byte-Arrays/#ByteArray___size "Documentation for ByteArray.size")) : m β


ByteArray.foldlM.{v, w} {β : Type v}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : β → [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → m β) (init : β)
  (as : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Byte-Arrays/#ByteArray___size "Documentation for ByteArray.size")) : m β


```

A monadic left fold on `[ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")` that iterates over an array from low to high indices, computing a running value.
Each element of the array is combined with the value from the prior elements using a monadic function `f`. The initial value `init` is the starting value before any elements have been processed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.forIn "Permalink")def
```


ByteArray.forIn.{v, w} {β : Type v} {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (as : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (b : β) (f : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → β → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") β)) : m β


ByteArray.forIn.{v, w} {β : Type v}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (as : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (b : β)
  (f : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → β → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") β)) : m β


```

The reference implementation of `[ForIn.forIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn.forIn")` for `[ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")`.
In compiled code, this is replaced by the more efficient `ByteArray.forInUnsafe`.
###  20.17.1.7. Iterators[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Byte-Arrays--API-Reference--Iterators "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.iter "Permalink")def
```


ByteArray.iter (arr : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) : [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")


ByteArray.iter (arr : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) :
  [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")


```

Creates an iterator at the beginning of an array.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.Iterator "Permalink")structure
```


ByteArray.Iterator : Type


ByteArray.Iterator : Type


```

Iterator over the bytes (`[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")`) of a `[ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")`.
Typically created by `arr.iter`, where `arr` is a `[ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")`.
An iterator is _valid_ if the position `i` is _valid_ for the array `arr`, meaning `0 ≤ i ≤ arr.size`
Most operations on iterators return arbitrary values if the iterator is not valid. The functions in the `[ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")` API should rule out the creation of invalid iterators, with two exceptions:
  * `Iterator.next iter` is invalid if `iter` is already at the end of the array (`iter.atEnd` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`)
  * `Iterator.forward iter n`/`Iterator.nextn iter n` is invalid if `n` is strictly greater than the number of remaining bytes.


#  Constructor

```
[ByteArray.Iterator.mk](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator.mk")
```

#  Fields

```
array : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")
```

The array the iterator is for.

```
idx : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

The current position.
This position is not necessarily valid for the array, for instance if one keeps calling `Iterator.next` when `Iterator.atEnd` is true. If the position is not valid, then the current byte is `([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8"))`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.Iterator.pos "Permalink")def
```


ByteArray.Iterator.pos (self : [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


ByteArray.Iterator.pos
  (self : [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The current position.
This position is not necessarily valid for the array, for instance if one keeps calling `Iterator.next` when `Iterator.atEnd` is true. If the position is not valid, then the current byte is `([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8"))`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.Iterator.atEnd "Permalink")def
```


ByteArray.Iterator.atEnd : [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


ByteArray.Iterator.atEnd :
  [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

True if the iterator is past the array's last byte.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.Iterator.hasNext "Permalink")def
```


ByteArray.Iterator.hasNext : [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


ByteArray.Iterator.hasNext :
  [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

True if the iterator is valid; that is, it is not past the array's last byte.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.Iterator.hasPrev "Permalink")def
```


ByteArray.Iterator.hasPrev : [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


ByteArray.Iterator.hasPrev :
  [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

True if the position is not zero.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.Iterator.curr "Permalink")def
```


ByteArray.Iterator.curr : [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") → [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


ByteArray.Iterator.curr :
  [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") → [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

The byte at the current position.
On an invalid position, returns `([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8"))`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.Iterator.curr' "Permalink")def
```


ByteArray.Iterator.curr' (it : [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator"))
  (h : it.[hasNext](Basic-Types/Byte-Arrays/#ByteArray___Iterator___hasNext "Documentation for ByteArray.Iterator.hasNext") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


ByteArray.Iterator.curr'
  (it : [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator"))
  (h : it.[hasNext](Basic-Types/Byte-Arrays/#ByteArray___Iterator___hasNext "Documentation for ByteArray.Iterator.hasNext") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

The byte at the current position. -
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.Iterator.next "Permalink")def
```


ByteArray.Iterator.next : [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") → [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")


ByteArray.Iterator.next :
  [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") → [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")


```

Moves the iterator's position forward by one byte, unconditionally.
It is only valid to call this function if the iterator is not at the end of the array, **i.e.** `Iterator.atEnd` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`; otherwise, the resulting iterator will be invalid.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.Iterator.next' "Permalink")def
```


ByteArray.Iterator.next' (it : [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator"))
  (_h : it.[hasNext](Basic-Types/Byte-Arrays/#ByteArray___Iterator___hasNext "Documentation for ByteArray.Iterator.hasNext") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")


ByteArray.Iterator.next'
  (it : [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator"))
  (_h : it.[hasNext](Basic-Types/Byte-Arrays/#ByteArray___Iterator___hasNext "Documentation for ByteArray.Iterator.hasNext") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) :
  [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")


```

Moves the iterator's position forward by one byte. -
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.Iterator.forward "Permalink")def
```


ByteArray.Iterator.forward :
  [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")


ByteArray.Iterator.forward :
  [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") →
    [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")


```

Moves the iterator's position several bytes forward.
The resulting iterator is only valid if the number of bytes to skip is less than or equal to the number of bytes left in the iterator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.Iterator.nextn "Permalink")def
```


ByteArray.Iterator.nextn : [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")


ByteArray.Iterator.nextn :
  [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") →
    [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")


```

Moves the iterator's position several bytes forward.
The resulting iterator is only valid if the number of bytes to skip is less than or equal to the number of bytes left in the iterator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.Iterator.prev "Permalink")def
```


ByteArray.Iterator.prev : [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") → [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")


ByteArray.Iterator.prev :
  [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") → [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")


```

Decreases the iterator's position.
If the position is zero, this function is the identity.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.Iterator.prevn "Permalink")def
```


ByteArray.Iterator.prevn : [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")


ByteArray.Iterator.prevn :
  [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") →
    [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")


```

Moves the iterator's position several bytes back.
If asked to go back more bytes than available, stops at the beginning of the array.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.Iterator.remainingBytes "Permalink")def
```


ByteArray.Iterator.remainingBytes : [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


ByteArray.Iterator.remainingBytes :
  [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of bytes remaining in the iterator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.Iterator.toEnd "Permalink")def
```


ByteArray.Iterator.toEnd : [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") → [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")


ByteArray.Iterator.toEnd :
  [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator") → [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")


```

Moves the iterator's position to the end of the array.
Given `i : [ByteArray.Iterator](Basic-Types/Byte-Arrays/#ByteArray___Iterator___mk "Documentation for ByteArray.Iterator")`, note that `i.[toEnd](Basic-Types/Byte-Arrays/#ByteArray___Iterator___toEnd "Documentation for ByteArray.Iterator.toEnd").[atEnd](Basic-Types/Byte-Arrays/#ByteArray___Iterator___atEnd "Documentation for ByteArray.Iterator.atEnd")` is always `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
###  20.17.1.8. Slices[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Byte-Arrays--API-Reference--Slices "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.toByteSlice "Permalink")def
```


ByteArray.toByteSlice (as : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Byte-Arrays/#ByteArray___size "Documentation for ByteArray.size")) : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")


ByteArray.toByteSlice (as : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray"))
  (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := as.[size](Basic-Types/Byte-Arrays/#ByteArray___size "Documentation for ByteArray.size")) : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")


```

Returns a byte slice of a byte array, with the given bounds.
If `start` or `stop` are not valid bounds for a byte slice, then they are clamped to byte array's size. Additionally, the starting index is clamped to the ending index.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteSlice "Permalink")def
```


ByteSlice : Type


ByteSlice : Type


```

A region of some underlying byte array.
A byte slice contains a byte array together with the start and end indices of a region of interest. Byte slices can be used to avoid copying or allocating space, while being more convenient than tracking the bounds by hand. The region of interest consists of every index that is both greater than or equal to `start` and strictly less than `[stop](Tactic-Proofs/Tactic-Reference/#stop "Documentation for tactic")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteSlice.beq "Permalink")def
```


ByteSlice.beq (a b : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


ByteSlice.beq (a b : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Comparison function
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteSlice.byteArray "Permalink")def
```


ByteSlice.byteArray (xs : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


ByteSlice.byteArray (xs : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) :
  [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


```

The underlying byte array.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteSlice.contains "Permalink")def
```


ByteSlice.contains (s : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) (byte : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


ByteSlice.contains (s : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice"))
  (byte : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks if the byte slice contains a specific byte value.
Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if any byte in the slice equals the given value, `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` otherwise.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteSlice.empty "Permalink")def
```


ByteSlice.empty : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")


ByteSlice.empty : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")


```

The empty byte slice.
This empty byte slice is backed by an empty byte array.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteSlice.foldr "Permalink")def
```


ByteSlice.foldr.{v} {β : Type v} (f : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → β → β) (init : β)
  (as : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) : β


ByteSlice.foldr.{v} {β : Type v}
  (f : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → β → β) (init : β)
  (as : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) : β


```

Folds an operation from right to left over the bytes in a byte slice.
An accumulator of type `β` is constructed by starting with `init` and combining each byte of the byte slice with the current accumulator value in turn, moving from the end to the start.
Examples:
  * `([ByteArray.mk](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray.mk") #[1, 2, 3]).[toByteSlice](Basic-Types/Byte-Arrays/#ByteArray___toByteSlice "Documentation for ByteArray.toByteSlice").[foldr](Basic-Types/Byte-Arrays/#ByteSlice___foldr "Documentation for ByteSlice.foldr") (·.[toNat](Basic-Types/Fixed-Precision-Integers/#UInt8___toNat "Documentation for UInt8.toNat") + ·) 0 = 6`
  * `([ByteArray.mk](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray.mk") #[1, 2, 3]).toByteSlice.popFront.foldr (·.toNat + ·) 0 = 5`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteSlice.foldrM "Permalink")def
```


ByteSlice.foldrM.{v, w} {β : Type v} {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → β → m β) (init : β) (as : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) : m β


ByteSlice.foldrM.{v, w} {β : Type v}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → β → m β) (init : β)
  (as : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) : m β


```

Folds a monadic operation from right to left over the bytes in a byte slice.
An accumulator of type `β` is constructed by starting with `init` and monadically combining each byte of the byte slice with the current accumulator value in turn, moving from the end to the start. The monad in question may permit early termination or repetition.
Examples:

```
#eval (ByteArray.mk #[1, 2, 3]).toByteSlice.foldrM (init := 0) fun x acc =>
  some x.toNat + acc

```
`[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 6`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteSlice.forM "Permalink")def
```


ByteSlice.forM.{v, w} {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) (as : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


ByteSlice.forM.{v, w}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) (as : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) :
  m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Runs a monadic action on each byte of a byte slice.
The bytes are processed starting at the lowest index and moving up.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteSlice.get "Permalink")def
```


ByteSlice.get (s : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") s.[size](Basic-Types/Byte-Arrays/#ByteSlice___size "Documentation for ByteSlice.size")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


ByteSlice.get (s : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice"))
  (i : [Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") s.[size](Basic-Types/Byte-Arrays/#ByteSlice___size "Documentation for ByteSlice.size")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Extracts a byte from the byte slice.
The index is relative to the start of the byte slice, rather than the underlying byte array.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteSlice.get! "Permalink")def
```


ByteSlice.get! (s : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


ByteSlice.get! (s : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Extracts a byte from the byte slice, or returns a default value when the index is out of bounds.
The index is relative to the start and end of the byte slice, rather than the underlying byte array. The default value is 0.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteSlice.getD "Permalink")def
```


ByteSlice.getD (s : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (v₀ : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


ByteSlice.getD (s : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (v₀ : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Extracts a byte from the byte slice, or returns a default value `v₀` when the index is out of bounds.
The index is relative to the start and end of the byte slice, rather than the underlying byte array.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteSlice.ofByteArray "Permalink")def
```


ByteSlice.ofByteArray (ba : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")


ByteSlice.ofByteArray (ba : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) :
  [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")


```

Creates a new ByteSlice of a ByteArray
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteSlice.size "Permalink")def
```


ByteSlice.size (s : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


ByteSlice.size (s : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Computes the size of the byte slice.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteSlice.slice "Permalink")def
```


ByteSlice.slice (s : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := s.[size](Basic-Types/Byte-Arrays/#ByteSlice___size "Documentation for ByteSlice.size")) : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")


ByteSlice.slice (s : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice"))
  (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0)
  (stop : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := s.[size](Basic-Types/Byte-Arrays/#ByteSlice___size "Documentation for ByteSlice.size")) : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")


```

Creates a sub-slice of the byte slice with the given bounds.
If `start` or `stop` are not valid bounds for a sub-slice, then they are clamped to the slice's size. Additionally, the starting index is clamped to the ending index.
The indices are relative to the current slice, not the underlying byte array.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteSlice.start "Permalink")def
```


ByteSlice.start (xs : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


ByteSlice.start (xs : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The starting index of the region of interest (inclusive).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteSlice.stop "Permalink")def
```


ByteSlice.stop (xs : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


ByteSlice.stop (xs : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The ending index of the region of interest (exclusive).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteSlice.toByteArray "Permalink")def
```


ByteSlice.toByteArray (s : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


ByteSlice.toByteArray (s : [ByteSlice](Basic-Types/Byte-Arrays/#ByteSlice "Documentation for ByteSlice")) :
  [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


```

Converts a byte slice back to a byte array by copying the relevant portion.
###  20.17.1.9. Element Predicates[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Byte-Arrays--API-Reference--Element-Predicates "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.findIdx? "Permalink")def
```


ByteArray.findIdx? (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (p : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


ByteArray.findIdx? (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray"))
  (p : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Finds the index of the first byte in `a` for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`. If no byte in `a` satisfies `p`, then the result is `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
The variant `findFinIdx?` additionally returns a proof that the found index is in bounds.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=ByteArray.findFinIdx? "Permalink")def
```


ByteArray.findFinIdx? (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (p : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") a.[size](Basic-Types/Byte-Arrays/#ByteArray___size "Documentation for ByteArray.size"))


ByteArray.findFinIdx? (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray"))
  (p : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (start : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 0) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") ([Fin](Basic-Types/Finite-Natural-Numbers/#Fin___mk "Documentation for Fin") a.[size](Basic-Types/Byte-Arrays/#ByteArray___size "Documentation for ByteArray.size"))


```

Finds the index of the first byte in `a` for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`. If no byte in `a` satisfies `p`, then the result is `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
The index is returned along with a proof that it is a valid index in the array.
[←20.16. Arrays](Basic-Types/Arrays/#Array "20.16. Arrays")[20.18. Ranges→](Basic-Types/Ranges/#ranges "20.18. Ranges")

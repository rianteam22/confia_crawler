[←20.7. Characters](Basic-Types/Characters/#Char "20.7. Characters")[20.9. The Unit Type→](Basic-Types/The-Unit-Type/#The-Lean-Language-Reference--Basic-Types--The-Unit-Type "20.9. The Unit Type")
#  20.8. Strings[🔗](find/?domain=Verso.Genre.Manual.section&name=String "Permalink")
Strings represent Unicode text. Strings are specially supported by Lean:
  * They have a _logical model_ that specifies their behavior in terms of `[ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")`s that contain UTF-8 scalar values.
  * In compiled code, they have a run-time representation that additionally includes a cached length, measured as the number of scalar values. The Lean runtime provides optimized implementations of string operations.
  * There is [string literal syntax](Basic-Types/Strings/#string-syntax) for writing strings.


UTF-8 is a variable-width encoding. A character may be encoded as a one, two, three, or four byte code unit. The fact that strings are UTF-8-encoded byte arrays is visible in the API:
  * There is no operation to project a particular character out of the string, as this would be a performance trap. [Use an iterator](Basic-Types/Strings/#string-iterators) in a loop instead of a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`.
  * Strings are indexed by `[String.Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")`, which internally records _byte counts_ rather than _character counts_ , and thus takes constant time. `[String.Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")` includes a proof that the byte count in fact points at the beginning of a UTF-8 code unit. Aside from `0`, these should not be constructed directly, but rather updated using `String.next` and `String.prev`.


##  20.8.1. Logical Model[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--Logical-Model "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String "Permalink")structure
```


String : Type


String : Type


```

A string is a sequence of Unicode scalar values.
At runtime, strings are represented by [dynamic arrays](https://en.wikipedia.org/wiki/Dynamic_array) of bytes using the UTF-8 encoding. Both the size in bytes (`[String.utf8ByteSize](Basic-Types/Strings/#String___utf8ByteSize "Documentation for String.utf8ByteSize")`) and in characters (`[String.length](Basic-Types/Strings/#String___length "Documentation for String.length")`) are cached and take constant time. Many operations on strings perform in-place modifications when the reference to the string is unique.
#  Constructor

```
[String.ofByteArray](Basic-Types/Strings/#String___ofByteArray "Documentation for String.ofByteArray")
```

#  Fields

```
toByteArray : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")
```

The bytes of the UTF-8 encoding of the string. Since strings have a special representation in the runtime, this function actually takes linear time and space at runtime. For efficient access to the string's bytes, use `[String.utf8ByteSize](Basic-Types/Strings/#String___utf8ByteSize "Documentation for String.utf8ByteSize")` and `[String.getUTF8Byte](Basic-Types/Strings/#String___getUTF8Byte "Documentation for String.getUTF8Byte")`.

```
isValidUTF8 : self.[toByteArray](Basic-Types/Strings/#String___ofByteArray "Documentation for String.toByteArray").IsValidUTF8
```

The bytes of the string form valid UTF-8.
The logical model of strings in Lean is a structure that contains two fields:
  * `[String.toByteArray](Basic-Types/Strings/#String___ofByteArray "Documentation for String.toByteArray")` is a `[ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")`, which contains the UTF-8 encoding of the string.
  * `[String.isValidUTF8](Basic-Types/Strings/#String___ofByteArray "Documentation for String.isValidUTF8")` is a proof that the bytes are in fact a valid UTF-8 encoding of a string.


This model allows operations on byte arrays to be used to specify and prove properties about string operations at a low level while still building on the theory of byte arrays. At the same time, it is close enough to the real run-time representation to avoid impedance mismatches between the logical model and the operations that make sense in the run-time representation.
###  20.8.1.1. Backwards Compatibility[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--Logical-Model--Backwards-Compatibility "Permalink")
In prior versions of Lean, the logical model of strings was a structure that contained a list of characters. This model is still useful. It is still accessible using `[String.ofList](Basic-Types/Strings/#String___ofList "Documentation for String.ofList")`, which converts a list of characters into a `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`, and `String.toList`, which converts a `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` into a list of characters.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.ofList "Permalink")def
```


String.ofList (data : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.ofList (data : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Creates a string that contains the characters in a list, in order.
Examples:
  * `[String.ofList](Basic-Types/Strings/#String___ofList "Documentation for String.ofList") ['L', '∃', '∀', 'N'] = "L∃∀N"`
  * `[String.ofList](Basic-Types/Strings/#String___ofList "Documentation for String.ofList") [] = ""`
  * `[String.ofList](Basic-Types/Strings/#String___ofList "Documentation for String.ofList") ['a', 'a', 'a'] = "aaa"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.toList "Permalink")def
```


String.toList (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.toList (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Converts a string to a list of characters.
Since strings are represented as dynamic arrays of bytes containing the string encoded using UTF-8, this operation takes time and space linear in the length of the string.
Examples:
  * `"abc".toList = ['a', 'b', 'c']`
  * `"".toList = []`
  * `"\n".toList = ['\n']`


##  20.8.2. Run-Time Representation[🔗](find/?domain=Verso.Genre.Manual.section&name=string-runtime "Permalink")
Memory layout of strings
Strings are represented as [dynamic arrays](Basic-Types/Arrays/#--tech-term-dynamic-arrays) of bytes, encoded in UTF-8. After the object header, a string contains: 

byte count
    
The number of bytes that currently contain valid string data 

capacity
    
The number of bytes presently allocated for the string 

length
    
The length of the encoded string, which may be shorter than the byte count due to UTF-8 multi-byte characters 

data
    
The actual character data in the string, null-terminated
Many string functions in the Lean runtime check whether they have exclusive access to their argument by consulting the reference count in the object header. If they do, and the string's capacity is sufficient, then the existing string can be mutated rather than allocating fresh memory. Otherwise, a new string must be allocated.
###  20.8.2.1. Performance Notes[🔗](find/?domain=Verso.Genre.Manual.section&name=string-performance "Permalink")
Despite the fact that they appear to be an ordinary constructor and projection, `[String.ofByteArray](Basic-Types/Strings/#String___ofByteArray "Documentation for String.ofByteArray")` and `[String.toByteArray](Basic-Types/Strings/#String___ofByteArray "Documentation for String.toByteArray")` take **time linear in the length of the string**. This is because byte arrays and strings do not have an identical representation, so the contents of the byte array must be copied to a new object.
##  20.8.3. Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=string-syntax "Permalink")
Lean has three kinds of string literals: ordinary string literals, interpolated string literals, and raw string literals.
###  20.8.3.1. String Literals[🔗](find/?domain=Verso.Genre.Manual.section&name=string-literals "Permalink")
String literals begin and end with a double-quote character `"`.  Between these characters, they may contain any other character, including newlines, which are included literally (with the caveat that all newlines in a Lean source file are interpreted as `'\n'`, regardless of file encoding and platform). Special characters that cannot otherwise be written in string literals may be escaped with a backslash, so `"\"Quotes\""` is a string literal that begins and ends with double quotes. The following forms of escape sequences are accepted: 

`\r`, `\n`, `\t`, `\\`, `\"`, `\'` 
    
These escape sequences have the usual meaning, mapping to `CR`, `LF`, tab, backslash, double quote, and single quote, respectively. 

`\xNN` 
    
When `NN` is a sequence of two hexadecimal digits, this escape denotes the character whose Unicode code point is indicated by the two-digit hexadecimal code. 

`\uNNNN` 
    
When `NN` is a sequence of two hexadecimal digits, this escape denotes the character whose Unicode code point is indicated by the four-digit hexadecimal code.
String literals may contain _gaps_. A gap is indicated by an escaped newline, with no intervening characters between the escaping backslash and the newline. In this case, the string denoted by the literal is missing the newline and all leading whitespace from the next line. String gaps may not precede lines that contain only whitespace.
Here, `str1` and `str2` are the same string:
`def str1 := "String with \              a gap" def str2 := "String with a gap"  example : [str1](Basic-Types/Strings/#str1 "Definition of example") = [str2](Basic-Types/Strings/#str2 "Definition of example") := [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
If the line following the gap is empty, the string is rejected:

```
def str3 := "String with \unexpected additional newline in string gap 
             a gap"
```

The parser error is:

```
<example>:2:0-3:0: unexpected additional newline in string gap
```

###  20.8.3.2. Interpolated Strings[🔗](find/?domain=Verso.Genre.Manual.section&name=string-interpolation "Permalink")
Preceding a string literal with `s!` causes it to be processed as an _interpolated string_ , in which regions of the string surrounded by `{` and `}` characters are parsed and interpreted as Lean expressions. Interpolated strings are interpreted by appending the string that precedes the interpolation, the expression (with an added call to `toString` surrounding it), and the string that follows the interpolation.
For example:
`example :     s!"1 + 1 = {1 + 1}\n" =     "1 + 1 = " ++ toString (1 + 1) ++ "\n" :=   [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
Preceding a literal with `m!` causes the interpolation to result in an instance of `MessageData`, the compiler's internal data structure for messages to be shown to users.
###  20.8.3.3. Raw String Literals[🔗](find/?domain=Verso.Genre.Manual.section&name=raw-string-literals "Permalink")
In raw string literals,  there are no escape sequences or gaps, and each character denotes itself exactly. Raw string literals are preceded by `r`, followed by zero or more hash characters (`#`) and a double quote `"`. The string literal is completed at a double quote that is followed by _the same number_ of hash characters. For example, they can be used to avoid the need to double-escape certain characters:
`example : r"\t" = "\\t" := [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `"Write backslash in a string using '\\\\\\\\'"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") r"Write backslash in a string using '\\\\\\\'" `
The `#eval` yields:

```
"Write backslash in a string using '\\\\\\\\'"
```

Including hash marks allows the strings to contain unescaped quotes:
`example :     r#"This is "literally" quoted"# =     "This is \"literally\" quoted" :=   [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
Adding sufficiently many hash marks allows any raw literal to be written literally:
`example :     r##"This is r#"literally"# quoted"## =     "This is r#\"literally\"# quoted" :=   [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
##  20.8.4. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=string-api "Permalink")
###  20.8.4.1. Constructing[🔗](find/?domain=Verso.Genre.Manual.section&name=string-api-build "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.singleton "Permalink")def
```


String.singleton (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.singleton (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Returns a new string that contains only the character `c`.
Because strings are encoded in UTF-8, the resulting string may take multiple bytes.
Examples:
  * `[String.singleton](Basic-Types/Strings/#String___singleton "Documentation for String.singleton") 'L' = "L"`
  * `[String.singleton](Basic-Types/Strings/#String___singleton "Documentation for String.singleton") ' ' = " "`
  * `[String.singleton](Basic-Types/Strings/#String___singleton "Documentation for String.singleton") '"' = "\""`
  * `[String.singleton](Basic-Types/Strings/#String___singleton "Documentation for String.singleton") '𝒫' = "𝒫"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.append "Permalink")def
```


String.append (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (t : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.append (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (t : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Appends two strings. Usually accessed via the `++` operator.
The internal implementation will perform destructive updates if the string is not shared.
Examples:
  * `"abc".[append](Basic-Types/Strings/#String___append "Documentation for String.append") "def" = "abcdef"`
  * `"abc" ++ "def" = "abcdef"`
  * `"" ++ "" = ""`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.join "Permalink")def
```


String.join (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.join (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Appends all the strings in a list of strings, in order.
Use `[String.intercalate](Basic-Types/Strings/#String___intercalate "Documentation for String.intercalate")` to place a separator string between the strings in a list.
Examples:
  * `[String.join](Basic-Types/Strings/#String___join "Documentation for String.join") ["gr", "ee", "n"] = "green"`
  * `[String.join](Basic-Types/Strings/#String___join "Documentation for String.join") ["b", "", "l", "", "ue"] = "blue"`
  * `[String.join](Basic-Types/Strings/#String___join "Documentation for String.join") [] = ""`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.intercalate "Permalink")def
```


String.intercalate (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.intercalate (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Appends the strings in a list of strings, placing the separator `s` between each pair.
Examples:
  * `", ".[intercalate](Basic-Types/Strings/#String___intercalate "Documentation for String.intercalate") ["red", "green", "blue"] = "red, green, blue"`
  * `" and ".[intercalate](Basic-Types/Strings/#String___intercalate "Documentation for String.intercalate") ["tea", "coffee"] = "tea and coffee"`
  * `" | ".[intercalate](Basic-Types/Strings/#String___intercalate "Documentation for String.intercalate") ["M", "", "N"] = "M |  | N"`


###  20.8.4.2. Conversions[🔗](find/?domain=Verso.Genre.Manual.section&name=string-api-convert "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.toList "Permalink")def
```


String.toList (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.toList (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Converts a string to a list of characters.
Since strings are represented as dynamic arrays of bytes containing the string encoded using UTF-8, this operation takes time and space linear in the length of the string.
Examples:
  * `"abc".toList = ['a', 'b', 'c']`
  * `"".toList = []`
  * `"\n".toList = ['\n']`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.isNat "Permalink")def
```


String.isNat (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.isNat (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the string can be interpreted as the decimal representation of a natural number.
A slice can be interpreted as a decimal natural number if it is not empty and all the characters in it are digits.
Use `toNat?` or `toNat!` to convert such a slice to a natural number.
Examples:
  * `"".[isNat](Basic-Types/Strings/#String___isNat "Documentation for String.isNat") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"0".[isNat](Basic-Types/Strings/#String___isNat "Documentation for String.isNat") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"5".[isNat](Basic-Types/Strings/#String___isNat "Documentation for String.isNat") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"05".[isNat](Basic-Types/Strings/#String___isNat "Documentation for String.isNat") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"587".[isNat](Basic-Types/Strings/#String___isNat "Documentation for String.isNat") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"-587".[isNat](Basic-Types/Strings/#String___isNat "Documentation for String.isNat") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `" 5".[isNat](Basic-Types/Strings/#String___isNat "Documentation for String.isNat") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"2+3".[isNat](Basic-Types/Strings/#String___isNat "Documentation for String.isNat") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"0xff".[isNat](Basic-Types/Strings/#String___isNat "Documentation for String.isNat") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.toNat? "Permalink")def
```


String.toNat? (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


String.toNat? (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Interprets a string as the decimal representation of a natural number, returning it. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the slice does not contain a decimal natural number.
A slice can be interpreted as a decimal natural number if it is not empty and all the characters in it are digits.
Use `isNat` to check whether `toNat?` would return `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")`. `toNat!` is an alternative that panics instead of returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` when the slice is not a natural number.
Examples:
  * `"".[toNat?](Basic-Types/Strings/#String___toNat___ "Documentation for String.toNat?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `"0".[toNat?](Basic-Types/Strings/#String___toNat___ "Documentation for String.toNat?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 0`
  * `"5".[toNat?](Basic-Types/Strings/#String___toNat___ "Documentation for String.toNat?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5`
  * `"587".[toNat?](Basic-Types/Strings/#String___toNat___ "Documentation for String.toNat?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 587`
  * `"-587".[toNat?](Basic-Types/Strings/#String___toNat___ "Documentation for String.toNat?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `" 5".[toNat?](Basic-Types/Strings/#String___toNat___ "Documentation for String.toNat?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `"2+3".[toNat?](Basic-Types/Strings/#String___toNat___ "Documentation for String.toNat?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `"0xff".[toNat?](Basic-Types/Strings/#String___toNat___ "Documentation for String.toNat?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.toNat! "Permalink")def
```


String.toNat! (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


String.toNat! (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Interprets a string as the decimal representation of a natural number, returning it. Panics if the slice does not contain a decimal natural number.
A slice can be interpreted as a decimal natural number if it is not empty and all the characters in it are digits.
Use `isNat` to check whether `toNat!` would return a value. `toNat?` is a safer alternative that returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` instead of panicking when the string is not a natural number.
Examples:
  * `"0".[toNat!](Basic-Types/Strings/#String___toNat___-next "Documentation for String.toNat!") = 0`
  * `"5".[toNat!](Basic-Types/Strings/#String___toNat___-next "Documentation for String.toNat!") = 5`
  * `"587".[toNat!](Basic-Types/Strings/#String___toNat___-next "Documentation for String.toNat!") = 587`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.isInt "Permalink")def
```


String.isInt (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.isInt (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the string can be interpreted as the decimal representation of an integer.
A string can be interpreted as a decimal integer if it only consists of at least one decimal digit and optionally `-` in front. Leading `+` characters are not allowed.
Use `[String.toInt?](Basic-Types/Strings/#String___toInt___ "Documentation for String.toInt?")` or `[String.toInt!](Basic-Types/Strings/#String___toInt___-next "Documentation for String.toInt!")` to convert such a string to an integer.
Examples:
  * `"".[isInt](Basic-Types/Strings/#String___isInt "Documentation for String.isInt") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"-".[isInt](Basic-Types/Strings/#String___isInt "Documentation for String.isInt") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"0".[isInt](Basic-Types/Strings/#String___isInt "Documentation for String.isInt") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"-0".[isInt](Basic-Types/Strings/#String___isInt "Documentation for String.isInt") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"5".[isInt](Basic-Types/Strings/#String___isInt "Documentation for String.isInt") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"587".[isInt](Basic-Types/Strings/#String___isInt "Documentation for String.isInt") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"-587".[isInt](Basic-Types/Strings/#String___isInt "Documentation for String.isInt") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"+587".[isInt](Basic-Types/Strings/#String___isInt "Documentation for String.isInt") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `" 5".[isInt](Basic-Types/Strings/#String___isInt "Documentation for String.isInt") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"2-3".[isInt](Basic-Types/Strings/#String___isInt "Documentation for String.isInt") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"0xff".[isInt](Basic-Types/Strings/#String___isInt "Documentation for String.isInt") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.toInt? "Permalink")def
```


String.toInt? (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


String.toInt? (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Interprets a string as the decimal representation of an integer, returning it. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the string does not contain a decimal integer.
A string can be interpreted as a decimal integer if it only consists of at least one decimal digit and optionally `-` in front. Leading `+` characters are not allowed.
Use `[String.isInt](Basic-Types/Strings/#String___isInt "Documentation for String.isInt")` to check whether `[String.toInt?](Basic-Types/Strings/#String___toInt___ "Documentation for String.toInt?")` would return `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")`. `[String.toInt!](Basic-Types/Strings/#String___toInt___-next "Documentation for String.toInt!")` is an alternative that panics instead of returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` when the string is not an integer.
Examples:
  * `"".[toInt?](Basic-Types/Strings/#String___toInt___ "Documentation for String.toInt?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `"-".[toInt?](Basic-Types/Strings/#String___toInt___ "Documentation for String.toInt?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `"0".[toInt?](Basic-Types/Strings/#String___toInt___ "Documentation for String.toInt?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 0`
  * `"5".[toInt?](Basic-Types/Strings/#String___toInt___ "Documentation for String.toInt?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5`
  * `"-5".[toInt?](Basic-Types/Strings/#String___toInt___ "Documentation for String.toInt?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (-5)`
  * `"587".[toInt?](Basic-Types/Strings/#String___toInt___ "Documentation for String.toInt?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 587`
  * `"-587".[toInt?](Basic-Types/Strings/#String___toInt___ "Documentation for String.toInt?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") (-587)`
  * `" 5".[toInt?](Basic-Types/Strings/#String___toInt___ "Documentation for String.toInt?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `"2-3".[toInt?](Basic-Types/Strings/#String___toInt___ "Documentation for String.toInt?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `"0xff".[toInt?](Basic-Types/Strings/#String___toInt___ "Documentation for String.toInt?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.toInt! "Permalink")def
```


String.toInt! (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


String.toInt! (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")


```

Interprets a string as the decimal representation of an integer, returning it. Panics if the string does not contain a decimal integer.
A string can be interpreted as a decimal integer if it only consists of at least one decimal digit and optionally `-` in front. Leading `+` characters are not allowed.
Use `[String.isInt](Basic-Types/Strings/#String___isInt "Documentation for String.isInt")` to check whether `[String.toInt!](Basic-Types/Strings/#String___toInt___-next "Documentation for String.toInt!")` would return a value. `[String.toInt?](Basic-Types/Strings/#String___toInt___ "Documentation for String.toInt?")` is a safer alternative that returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` instead of panicking when the string is not an integer.
Examples:
  * `"0".[toInt!](Basic-Types/Strings/#String___toInt___-next "Documentation for String.toInt!") = 0`
  * `"5".[toInt!](Basic-Types/Strings/#String___toInt___-next "Documentation for String.toInt!") = 5`
  * `"587".[toInt!](Basic-Types/Strings/#String___toInt___-next "Documentation for String.toInt!") = 587`
  * `"-587".[toInt!](Basic-Types/Strings/#String___toInt___-next "Documentation for String.toInt!") = -587`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.toFormat "Permalink")def
```


String.toFormat (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


String.toFormat (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Std.Format](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format")


```

Converts a string to a pretty-printer document, replacing newlines in the string with `[Std.Format.line](Interacting-with-Lean/#Std___Format___nil "Documentation for Std.Format.line")`.
###  20.8.4.3. Properties[🔗](find/?domain=Verso.Genre.Manual.section&name=string-api-props "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.isEmpty "Permalink")def
```


String.isEmpty (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.isEmpty (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a string is empty.
Empty strings are equal to `""` and have length and end position `0`.
Examples:
  * `"".[isEmpty](Basic-Types/Strings/#String___isEmpty "Documentation for String.isEmpty") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"empty".[isEmpty](Basic-Types/Strings/#String___isEmpty "Documentation for String.isEmpty") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `" ".[isEmpty](Basic-Types/Strings/#String___isEmpty "Documentation for String.isEmpty") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.length "Permalink")def
```


String.length (b : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


String.length (b : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the length of a string in Unicode code points.
Examples:
  * `"".[length](Basic-Types/Strings/#String___length "Documentation for String.length") = 0`
  * `"abc".[length](Basic-Types/Strings/#String___length "Documentation for String.length") = 3`
  * `"L∃∀N".[length](Basic-Types/Strings/#String___length "Documentation for String.length") = 4`


###  20.8.4.4. Positions[🔗](find/?domain=Verso.Genre.Manual.section&name=string-api-valid-pos "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.isValid "Permalink")structure
```


String.Pos (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : Type


String.Pos (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : Type


```

A `Pos s` is a byte offset in `s` together with a proof that this position is at a UTF-8 character boundary.
#  Constructor

```
[String.Pos.mk](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos.mk")
```

#  Fields

```
offset : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")
```

The underlying byte offset of the `Pos`.

```
isValid : String.Pos.Raw.IsValid s self.[offset](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos.offset")
```

The proof that `offset` is valid for the string `s`.
####  20.8.4.4.1. In Strings[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Positions--In-Strings "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.startPos "Permalink")def
```


String.startPos (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


String.startPos (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


```

The start position of `s`, as an `s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.endPos "Permalink")def
```


String.endPos (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


String.endPos (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


```

The past-the-end position of `s`, as an `s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.pos "Permalink")def
```


String.pos (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (off : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (h : String.Pos.Raw.IsValid s off) : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


String.pos (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (off : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (h : String.Pos.Raw.IsValid s off) :
  s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


```

Constructs a valid position on `s` from a position and a proof that it is valid.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.pos? "Permalink")def
```


String.pos? (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (off : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


String.pos? (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (off : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


```

Constructs a valid position on `s` from a position, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the position is not valid.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.pos! "Permalink")def
```


String.pos! (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (off : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


String.pos! (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (off : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


```

Constructs a valid position `s` from a position, panicking if the position is not valid.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.extract "Permalink")def
```


String.extract {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (b e : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.extract {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}
  (b e : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Copies a region of a string to a new string.
The region of `s` from `b` (inclusive) to `e` (exclusive) is copied to a newly-allocated `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`.
If `b`'s offset is greater than or equal to that of `e`, then the resulting string is `""`.
If possible, prefer `String.slice`, which avoids the allocation.
####  20.8.4.4.2. Lookups[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Positions--Lookups "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.get "Permalink")def
```


String.Pos.get {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) (h : pos ≠ s.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.Pos.get {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos"))
  (h : pos ≠ s.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Returns the character at the position `pos` of a string, taking a proof that `p` is not the past-the-end position.
This function is overridden with an efficient implementation in runtime code.
Examples:
  * `("abc".[pos](Basic-Types/Strings/#String___pos "Documentation for String.pos") ⟨1⟩ (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic"))).[get](Basic-Types/Strings/#String___Pos___get "Documentation for String.Pos.get") (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")) = 'b'`
  * `("L∃∀N".[pos](Basic-Types/Strings/#String___pos "Documentation for String.pos") ⟨1⟩ (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic"))).[get](Basic-Types/Strings/#String___Pos___get "Documentation for String.Pos.get") (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")) = '∃'`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.get! "Permalink")def
```


String.Pos.get! {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.Pos.get! {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Returns the character at the position `pos` of a string, or panics if the position is the past-the-end position.
This function is overridden with an efficient implementation in runtime code.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.get? "Permalink")def
```


String.Pos.get? {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.Pos.get? {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Returns the character at the position `pos` of a string, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the position is the past-the-end position.
This function is overridden with an efficient implementation in runtime code.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.set "Permalink")def
```


String.Pos.set {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (p : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) (hp : p ≠ s.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")) :
  [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.Pos.set {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (p : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos"))
  (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) (hp : p ≠ s.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Replaces the character at a specified position in a string with a new character.
If both the replacement character and the replaced character are 7-bit ASCII characters and the string is not shared, then it is updated in-place and not copied.
Examples:
  * `("abc".[pos](Basic-Types/Strings/#String___pos "Documentation for String.pos") ⟨1⟩ (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic"))).[set](Basic-Types/Strings/#String___Pos___set "Documentation for String.Pos.set") 'B' (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")) = "aBc"`
  * `("L∃∀N".[pos](Basic-Types/Strings/#String___pos "Documentation for String.pos") ⟨4⟩ (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic"))).[set](Basic-Types/Strings/#String___Pos___set "Documentation for String.Pos.set") 'X' (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")) = "L∃XN"`


####  20.8.4.4.3. Modifications[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Positions--Modifications "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.modify "Permalink")def
```


String.Pos.modify {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (p : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) (f : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))
  (hp : p ≠ s.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.Pos.modify {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (p : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos"))
  (f : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) (hp : p ≠ s.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")) :
  [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Replaces the character at position `p` in the string `s` with the result of applying `f` to that character.
If both the replacement character and the replaced character are 7-bit ASCII characters and the string is not shared, then it is updated in-place and not copied.
Examples:
  * `("abc".[pos](Basic-Types/Strings/#String___pos "Documentation for String.pos") ⟨1⟩ (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic"))).[modify](Basic-Types/Strings/#String___Pos___modify "Documentation for String.Pos.modify") [Char.toUpper](Basic-Types/Characters/#Char___toUpper "Documentation for Char.toUpper") (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")) = "aBc"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.byte "Permalink")def
```


String.Pos.byte {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) (h : pos ≠ s.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


String.Pos.byte {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos"))
  (h : pos ≠ s.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Returns the byte at the position `pos` of a string.
####  20.8.4.4.4. Adjustment[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Positions--Adjustment "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.prev "Permalink")def
```


String.Pos.prev {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) (h : pos ≠ s.[startPos](Basic-Types/Strings/#String___startPos "Documentation for String.startPos")) :
  s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


String.Pos.prev {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos"))
  (h : pos ≠ s.[startPos](Basic-Types/Strings/#String___startPos "Documentation for String.startPos")) : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


```

Returns the previous valid position before the given position, given a proof that the position is not the start position, which guarantees that such a position exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.prev! "Permalink")def
```


String.Pos.prev! {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


String.Pos.prev! {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


```

Returns the previous valid position before the given position, or panics if the position is the start position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.prev? "Permalink")def
```


String.Pos.prev? {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


String.Pos.prev? {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


```

Returns the previous valid position before the given position, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the position is the start position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.next "Permalink")def
```


String.Pos.next {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) (h : pos ≠ s.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")) : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


String.Pos.next {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos"))
  (h : pos ≠ s.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")) : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


```

Advances a valid position on a string to the next valid position, given a proof that the position is not the past-the-end position, which guarantees that such a position exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.next! "Permalink")def
```


String.Pos.next! {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


String.Pos.next! {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


```

Advances a valid position on a string to the next valid position, or panics if the given position is the past-the-end position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.next? "Permalink")def
```


String.Pos.next? {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


String.Pos.next? {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


```

Advances a valid position on a string to the next valid position, or returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the given position is the past-the-end position.
####  20.8.4.4.5. Other Strings[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Positions--Other-Strings "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.cast "Permalink")def
```


String.Pos.cast {s t : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) (h : s [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t) : t.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


String.Pos.cast {s t : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) (h : s [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t) : t.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


```

Constructs a valid position on `t` from a valid position on `s` and a proof that `s = t`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.ofCopy "Permalink")def
```


String.Pos.ofCopy {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} (pos : s.[copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy").[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Pos.ofCopy {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")}
  (pos : s.[copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy").[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Given a slice `s` and a position on `s.[copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")`, obtain the corresponding position on `s`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.toSetOfLE "Permalink")def
```


String.Pos.toSetOfLE {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (q p : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))
  (hp : p ≠ s.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")) (hpq : q [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") p) : (p.[set](Basic-Types/Strings/#String___Pos___set "Documentation for String.Pos.set") c hp).[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


String.Pos.toSetOfLE {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}
  (q p : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))
  (hp : p ≠ s.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")) (hpq : q [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") p) :
  (p.[set](Basic-Types/Strings/#String___Pos___set "Documentation for String.Pos.set") c hp).[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


```

Given a valid position in a string, obtain the corresponding position after setting a character on that string, provided that the position was before the changed position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.toModifyOfLE "Permalink")def
```


String.Pos.toModifyOfLE {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (q p : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) (f : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))
  (hp : p ≠ s.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")) (hpq : q [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") p) : (p.[modify](Basic-Types/Strings/#String___Pos___modify "Documentation for String.Pos.modify") f hp).[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


String.Pos.toModifyOfLE {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}
  (q p : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) (f : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))
  (hp : p ≠ s.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")) (hpq : q [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") p) :
  (p.[modify](Basic-Types/Strings/#String___Pos___modify "Documentation for String.Pos.modify") f hp).[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


```

Given a valid position in a string, obtain the corresponding position after modifying a character in that string, provided that the position was before the changed position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.toSlice "Permalink")def
```


String.Pos.toSlice {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")} (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : s.[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Pos.toSlice {s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : s.[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Turns a valid position on the string `s` into a valid position on the slice `s.[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`.
###  20.8.4.5. Raw Positions[🔗](find/?domain=Verso.Genre.Manual.section&name=string-api-pos "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.byteIdx "Permalink")structure
```


String.Pos.Raw : Type


String.Pos.Raw : Type


```

A byte position in a `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`, according to its UTF-8 encoding.
Character positions (counting the Unicode code points rather than bytes) are represented by plain `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`s. Indexing a `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` by a `[String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")` takes constant time, while character positions need to be translated internally to byte positions, which takes linear time.
A byte position `p` is _valid_ for a string `s` if `0 ≤ p ≤ s.rawEndPos` and `p` lies on a UTF-8 character boundary, see `[String.Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos").IsValid`.
There is another type, `[String.Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")`, which bundles the validity predicate. Using `[String.Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")` instead of `[String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")` is recommended because it will lead to less error handling and fewer edge cases.
#  Constructor

```
[String.Pos.Raw.mk](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw.mk")
```

#  Fields

```
byteIdx : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

Get the underlying byte index of a `[String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")`
####  20.8.4.5.1. Byte Position[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Raw-Positions--Byte-Position "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.offsetOfPos "Permalink")def
```


String.Pos.Raw.offsetOfPos (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pos : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


String.Pos.Raw.offsetOfPos (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (pos : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the character index that corresponds to the provided position (i.e. UTF-8 byte index) in a string.
If the position is at the end of the string, then the string's length in characters is returned. If the position is invalid due to pointing at the middle of a UTF-8 byte sequence, then the character index of the next character after the position is returned.
Examples:
  * `"L∃∀N".offsetOfPos ⟨0⟩ = 0`
  * `"L∃∀N".offsetOfPos ⟨1⟩ = 1`
  * `"L∃∀N".offsetOfPos ⟨2⟩ = 2`
  * `"L∃∀N".offsetOfPos ⟨4⟩ = 2`
  * `"L∃∀N".offsetOfPos ⟨5⟩ = 3`
  * `"L∃∀N".offsetOfPos ⟨50⟩ = 4`


####  20.8.4.5.2. Validity[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Raw-Positions--Validity "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.isValid "Permalink")def
```


String.Pos.Raw.isValid (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.Pos.Raw.isValid (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if `p` is a valid UTF-8 position in the string `s`.
This means that `p ≤ s.[rawEndPos](Basic-Types/Strings/#String___rawEndPos "Documentation for String.rawEndPos")` and `p` lies on a UTF-8 character boundary. At runtime, this operation takes constant time.
Examples:
  * `[String.Pos.isValid](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos.isValid") "abc" ⟨0⟩ = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[String.Pos.isValid](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos.isValid") "abc" ⟨1⟩ = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[String.Pos.isValid](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos.isValid") "abc" ⟨3⟩ = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[String.Pos.isValid](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos.isValid") "abc" ⟨4⟩ = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `[String.Pos.isValid](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos.isValid") "𝒫(A)" ⟨0⟩ = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `[String.Pos.isValid](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos.isValid") "𝒫(A)" ⟨1⟩ = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `[String.Pos.isValid](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos.isValid") "𝒫(A)" ⟨2⟩ = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `[String.Pos.isValid](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos.isValid") "𝒫(A)" ⟨3⟩ = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `[String.Pos.isValid](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos.isValid") "𝒫(A)" ⟨4⟩ = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.isValidForSlice "Permalink")def
```


String.Pos.Raw.isValidForSlice (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.Pos.Raw.isValidForSlice
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice"))
  (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Efficiently checks whether a position is at a UTF-8 character boundary of the slice `s`.
####  20.8.4.5.3. Boundaries[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Raw-Positions--Boundaries "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.rawEndPos "Permalink")def
```


String.rawEndPos (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


String.rawEndPos (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

A UTF-8 byte position that points at the end of a string, just after the last character.
  * `"abc".[rawEndPos](Basic-Types/Strings/#String___rawEndPos "Documentation for String.rawEndPos") = ⟨3⟩`
  * `"L∃∀N".[rawEndPos](Basic-Types/Strings/#String___rawEndPos "Documentation for String.rawEndPos") = ⟨8⟩`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.atEnd "Permalink")def
```


String.Pos.Raw.atEnd : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.Pos.Raw.atEnd :
  [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if a specified byte position is greater than or equal to the position which points to the end of a string. Otherwise, returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
Examples:
  * `(0 |> "abc".next |> "abc".next |> "abc".atEnd) = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `(0 |> "abc".next |> "abc".next |> "abc".next |> "abc".next |> "abc".atEnd) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `(0 |> "L∃∀N".next |> "L∃∀N".next |> "L∃∀N".next |> "L∃∀N".atEnd) = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `(0 |> "L∃∀N".next |> "L∃∀N".next |> "L∃∀N".next |> "L∃∀N".next |> "L∃∀N".atEnd) = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"abc".atEnd ⟨4⟩ = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"L∃∀N".atEnd ⟨7⟩ = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"L∃∀N".atEnd ⟨8⟩ = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


####  20.8.4.5.4. Comparisons[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Raw-Positions--Comparisons "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.min "Permalink")def
```


String.Pos.Raw.min (p₁ p₂ : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


String.Pos.Raw.min
  (p₁ p₂ : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) :
  [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

Returns either `p₁` or `p₂`, whichever has the least byte index.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.byteDistance "Permalink")def
```


String.Pos.Raw.byteDistance (lo hi : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


String.Pos.Raw.byteDistance
  (lo hi : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the size of the byte slice delineated by the positions `lo` and `hi`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.substrEq "Permalink")def
```


String.Pos.Raw.substrEq (s1 : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pos1 : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (s2 : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pos2 : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) (sz : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.Pos.Raw.substrEq (s1 : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (pos1 : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) (s2 : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (pos2 : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) (sz : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether substrings of two strings are equal. Substrings are indicated by their starting positions and a size in _UTF-8 bytes_. Returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` if the indicated substring does not exist in either string.
This is a legacy function. The recommended alternative is to construct slices representing the strings to be compared and use the `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` instance of `[String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")`.
####  20.8.4.5.5. Adjustment[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Raw-Positions--Adjustment "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.prev "Permalink")def
```


String.Pos.Raw.prev : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


String.Pos.Raw.prev :
  [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

Returns the position in a string before a specified position, `p`. If `p = ⟨0⟩`, returns `0`. If `p` is greater than `rawEndPos`, returns the position one byte before `p`. Otherwise, if `p` occurs in the middle of a multi-byte character, returns the beginning position of that character.
For example, `"L∃∀N".prev ⟨3⟩` is `⟨1⟩`, since byte 3 occurs in the middle of the multi-byte character `'∃'` that starts at byte 1.
This is a legacy function. The recommended alternative is `[String.Pos.prev](Basic-Types/Strings/#String___Pos___prev "Documentation for String.Pos.prev")` or one of its variants like `[String.Pos.prev?](Basic-Types/Strings/#String___Pos___prev___-next "Documentation for String.Pos.prev?")`, combined with `[String.pos](Basic-Types/Strings/#String___pos "Documentation for String.pos")` or another means of obtaining a `[String.Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")`.
Examples:
  * `"abc".get ("abc".[rawEndPos](Basic-Types/Strings/#String___rawEndPos "Documentation for String.rawEndPos") |> "abc".prev) = 'c'`
  * `"L∃∀N".get ("L∃∀N".[rawEndPos](Basic-Types/Strings/#String___rawEndPos "Documentation for String.rawEndPos") |> "L∃∀N".prev |> "L∃∀N".prev |> "L∃∀N".prev) = '∃'`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.next "Permalink")def
```


String.Pos.Raw.next (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


String.Pos.Raw.next (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

Returns the next position in a string after position `p`. If `p` is not a valid position or `p = s.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")`, returns the position one byte after `p`.
A run-time bounds check is performed to determine whether `p` is at the end of the string. If a bounds check has already been performed, use `String.next'` to avoid a repeated check.
This is a legacy function. The recommended alternative is `[String.Pos.next](Basic-Types/Strings/#String___Pos___next "Documentation for String.Pos.next")` or one of its variants like `[String.Pos.next?](Basic-Types/Strings/#String___Pos___next___-next "Documentation for String.Pos.next?")`, combined with `[String.pos](Basic-Types/Strings/#String___pos "Documentation for String.pos")` or another means of obtaining a `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String").ValisPos`.
Some examples of edge cases:
  * `"abc".next ⟨3⟩ = ⟨4⟩`, since `3 = "abc".[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")`
  * `"L∃∀N".next ⟨2⟩ = ⟨3⟩`, since `2` points into the middle of a multi-byte UTF-8 character


Examples:
  * `"abc".get ("abc".next 0) = 'b'`
  * `"L∃∀N".get (0 |> "L∃∀N".next |> "L∃∀N".next) = '∀'`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.next' "Permalink")def
```


String.Pos.Raw.next' (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (h : [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[String.Pos.Raw.atEnd](Basic-Types/Strings/#String___Pos___Raw___atEnd "Documentation for String.Pos.Raw.atEnd") s p [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


String.Pos.Raw.next' (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (h : [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[String.Pos.Raw.atEnd](Basic-Types/Strings/#String___Pos___Raw___atEnd "Documentation for String.Pos.Raw.atEnd") s p [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) :
  [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

Returns the next position in a string after position `p`. The result is unspecified if `p` is not a valid position.
Requires evidence, `h`, that `p` is within bounds. No run-time bounds check is performed, as in `String.next`.
A typical pattern combines `String.next'` with a dependent `[if](Tactic-Proofs/The-Tactic-Language/#if "Documentation for tactic")`-expression to avoid the overhead of an additional bounds check. For example:

```
def next? (s : String) (p : String.Pos) : Option Char :=
  if h : s.atEnd p then none else s.get (s.next' p h)

```

This is a legacy function. The recommended alternative is `[String.Pos.next](Basic-Types/Strings/#String___Pos___next "Documentation for String.Pos.next")`, combined with `[String.pos](Basic-Types/Strings/#String___pos "Documentation for String.pos")` or another means of obtaining a `[String.Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")`.
Example:
  * `let abc := "abc"; abc.get (abc.next' 0 (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic"))) = 'b'`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.nextUntil "Permalink")def
```


String.Pos.Raw.nextUntil (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (p : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (i : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


String.Pos.Raw.nextUntil (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (p : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (i : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) :
  [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

Repeatedly increments a position in a string, as if by `[String.Pos.Raw.next](Basic-Types/Strings/#String___Pos___Raw___next "Documentation for String.Pos.Raw.next")`, while the predicate `p` returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` for the character at the position. Stops incrementing at the end of the string or when `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for the current character.
Examples:
  * `let s := "   a  "; (Pos.Raw.nextUntil s Char.isWhitespace 0).get s = ' '`
  * `let s := "   a  "; (Pos.Raw.nextUntil s Char.isAlpha 0).get s = 'a'`
  * `let s := "a  "; (Pos.Raw.nextUntil s Char.isWhitespace 0).get s = ' '`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.nextWhile "Permalink")def
```


String.Pos.Raw.nextWhile (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (p : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (i : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


String.Pos.Raw.nextWhile (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (p : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (i : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) :
  [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

Repeatedly increments a position in a string, as if by `[String.Pos.Raw.next](Basic-Types/Strings/#String___Pos___Raw___next "Documentation for String.Pos.Raw.next")`, while the predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for the character at the position. Stops incrementing at the end of the string or when `p` returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` for the current character.
Examples:
  * `let s := "   a  "; ((0 : Pos.Raw).nextWhile s Char.isWhitespace).get s = 'a'`
  * `let s := "a  "; ((0 : Pos.Raw).nextWhile s Char.isWhitespace).get s = 'a'`
  * `let s := "ba  "; (Pos.Raw.nextWhile s Char.isWhitespace 0).get s = 'b'`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.inc "Permalink")def
```


String.Pos.Raw.inc (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


String.Pos.Raw.inc (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) :
  [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

Increases the byte offset of the position by `1`. Not to be confused with `Pos.next`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.increaseBy "Permalink")def
```


String.Pos.Raw.increaseBy (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


String.Pos.Raw.increaseBy
  (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

Advances `p` by `n` bytes. This is not an `[HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd")` instance because it should be a relatively rare operation, so we use a name to make accidental use less likely. To add the size of a character `c` or string `s` to a raw position `p`, you can use `p + c` resp. `p + s`.
This should be seen as an "advance" or "skip".
See also `Pos.Raw.offsetBy`, which turns relative positions into absolute positions.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.offsetBy "Permalink")def
```


String.Pos.Raw.offsetBy (p offset : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


String.Pos.Raw.offsetBy
  (p offset : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) :
  [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

Offsets `p` by `offset` on the left. This is not an `[HAdd](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd")` instance because it should be a relatively rare operation, so we use a name to make accidental use less likely. To offset a position by the size of a character character `c` or string `s`, you can use `c + p` resp. `s + p`.
This should be seen as an operation that converts relative positions into absolute positions.
See also `Pos.Raw.increaseBy`, which is an "advancing" operation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.dec "Permalink")def
```


String.Pos.Raw.dec (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


String.Pos.Raw.dec (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) :
  [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

Decreases the byte offset of the position by `1`. Not to be confused with `Pos.prev`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.decreaseBy "Permalink")def
```


String.Pos.Raw.decreaseBy (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


String.Pos.Raw.decreaseBy
  (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

Move the position `p` back by `n` bytes. This is not an `[HSub](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub")` instance because it should be a relatively rare operation, so we use a name to make accidental use less likely. To remove the size of a character `c` or string `s` from a raw position `p`, you can use `p - c` resp. `p - s`.
This should be seen as the inverse of an "advance" or "skip".
See also `Pos.Raw.unoffsetBy`, which turns absolute positions into relative positions.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.unoffsetBy "Permalink")def
```


String.Pos.Raw.unoffsetBy (p offset : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


String.Pos.Raw.unoffsetBy
  (p offset : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) :
  [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

Decreases `p` by `offset`. This is not an `[HSub](Type-Classes/Basic-Classes/#HSub___mk "Documentation for HSub")` instance because it should be a relatively rare operation, so we use a name to make accidental use less likely. To unoffset a position by the size of a character `c` or string `s`, you can use `p - c` resp. `p - s`.
This should be seen as an operation that converts absolute positions into relative positions.
See also `Pos.Raw.decreaseBy`, which is an "unadvancing" operation.
####  20.8.4.5.6. String Lookups[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Raw-Positions--String-Lookups "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.extract "Permalink")def
```


String.Pos.Raw.extract :
  [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.Pos.Raw.extract :
  [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") →
    [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") →
      [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Creates a new string that consists of the region of the input string delimited by the two positions.
The result is `""` if the start position is greater than or equal to the end position or if the start position is at the end of the string. If either position is invalid (that is, if either points at the middle of a multi-byte UTF-8 character) then the result is unspecified.
This is a legacy function. The recommended alternative is `String.Pos.extract`, but usually it is even better to operate on `[String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")` instead and call `[String.Slice.copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")` (only) if required.
Examples:
  * `"red green blue".[extract](Basic-Types/Strings/#String___extract "Documentation for String.extract") ⟨0⟩ ⟨3⟩ = "red"`
  * `"red green blue".[extract](Basic-Types/Strings/#String___extract "Documentation for String.extract") ⟨3⟩ ⟨0⟩ = ""`
  * `"red green blue".[extract](Basic-Types/Strings/#String___extract "Documentation for String.extract") ⟨0⟩ ⟨100⟩ = "red green blue"`
  * `"red green blue".[extract](Basic-Types/Strings/#String___extract "Documentation for String.extract") ⟨4⟩ ⟨100⟩ = "green blue"`
  * `"L∃∀N".[extract](Basic-Types/Strings/#String___extract "Documentation for String.extract") ⟨1⟩ ⟨2⟩ = "∃∀N"`
  * `"L∃∀N".[extract](Basic-Types/Strings/#String___extract "Documentation for String.extract") ⟨2⟩ ⟨100⟩ = ""`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.get "Permalink")def
```


String.Pos.Raw.get (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.Pos.Raw.get (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Returns the character at position `p` of a string. If `p` is not a valid position, returns the fallback value `([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))`, which is `'A'`, but does not panic.
This function is overridden with an efficient implementation in runtime code. See `String.Pos.Raw.utf8GetAux` for the reference implementation.
This is a legacy function. The recommended alternative is `[String.Pos.get](Basic-Types/Strings/#String___Pos___get "Documentation for String.Pos.get")`, combined with `[String.pos](Basic-Types/Strings/#String___pos "Documentation for String.pos")` or another means of obtaining a `[String.Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")`.
Examples:
  * `"abc".get ⟨1⟩ = 'b'`
  * `"abc".get ⟨3⟩ = ([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))` because byte `3` is at the end of the string.
  * `"L∃∀N".get ⟨2⟩ = ([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))` because byte `2` is in the middle of `'∃'`.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.get! "Permalink")def
```


String.Pos.Raw.get! (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.Pos.Raw.get! (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Returns the character at position `p` of a string. Panics if `p` is not a valid position.
See `[String.pos?](Basic-Types/Strings/#String___pos___ "Documentation for String.pos?")` and `[String.Pos.get](Basic-Types/Strings/#String___Pos___get "Documentation for String.Pos.get")` for a safer alternative.
This function is overridden with an efficient implementation in runtime code. See `String.utf8GetAux` for the reference implementation.
This is a legacy function. The recommended alternative is `[String.Pos.get](Basic-Types/Strings/#String___Pos___get "Documentation for String.Pos.get")`, combined with `[String.pos!](Basic-Types/Strings/#String___pos___-next "Documentation for String.pos!")` or another means of obtaining a `[String.Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")`.
Examples
  * `"abc".get! ⟨1⟩ = 'b'`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.get' "Permalink")def
```


String.Pos.Raw.get' (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (h : [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[String.Pos.Raw.atEnd](Basic-Types/Strings/#String___Pos___Raw___atEnd "Documentation for String.Pos.Raw.atEnd") s p [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.Pos.Raw.get' (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (h : [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[String.Pos.Raw.atEnd](Basic-Types/Strings/#String___Pos___Raw___atEnd "Documentation for String.Pos.Raw.atEnd") s p [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) :
  [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Returns the character at position `p` of a string. Returns `([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))`, which is `'A'`, if `p` is not a valid position.
Requires evidence, `h`, that `p` is within bounds instead of performing a run-time bounds check as in `String.get`.
A typical pattern combines `get'` with a dependent `[if](Tactic-Proofs/The-Tactic-Language/#if "Documentation for tactic")`-expression to avoid the overhead of an additional bounds check. For example:

```
def getInBounds? (s : String) (p : String.Pos) : Option Char :=
  if h : s.atEnd p then none else some (s.get' p h)

```

Even with evidence of `¬ s.atEnd p`, `p` may be invalid if a byte index points into the middle of a multi-byte UTF-8 character. For example, `"L∃∀N".get' ⟨2⟩ (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")) = ([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))`.
This is a legacy function. The recommended alternative is `[String.Pos.get](Basic-Types/Strings/#String___Pos___get "Documentation for String.Pos.get")`, combined with `[String.pos](Basic-Types/Strings/#String___pos "Documentation for String.pos")` or another means of obtaining a `[String.Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")`.
Examples:
  * `"abc".get' 0 (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")) = 'a'`
  * `let lean := "L∃∀N"; lean.get' (0 |> lean.next |> lean.next) (by [decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")) = '∀'`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.get? "Permalink")def
```


String.Pos.Raw.get? : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.Pos.Raw.get? :
  [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Returns the character at position `p` of a string. If `p` is not a valid position, returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
This function is overridden with an efficient implementation in runtime code. See `String.utf8GetAux?` for the reference implementation.
This is a legacy function. The recommended alternative is `[String.Pos.get](Basic-Types/Strings/#String___Pos___get "Documentation for String.Pos.get")`, combined with `[String.pos?](Basic-Types/Strings/#String___pos___ "Documentation for String.pos?")` or another means of obtaining a `[String.Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")`.
Examples:
  * `"abc".get? ⟨1⟩ = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 'b'`
  * `"abc".get? ⟨3⟩ = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `"L∃∀N".get? ⟨1⟩ = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") '∃'`
  * `"L∃∀N".get? ⟨2⟩ = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


####  20.8.4.5.7. String Modifications[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Raw-Positions--String-Modifications "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.set "Permalink")def
```


String.Pos.Raw.set : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.Pos.Raw.set :
  [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Replaces the character at a specified position in a string with a new character. If the position is invalid, the string is returned unchanged.
If both the replacement character and the replaced character are 7-bit ASCII characters and the string is not shared, then it is updated in-place and not copied.
This is a legacy function. The recommended alternative is `[String.Pos.set](Basic-Types/Strings/#String___Pos___set "Documentation for String.Pos.set")`, combined with `[String.pos](Basic-Types/Strings/#String___pos "Documentation for String.pos")` or another means of obtaining a `[String.Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")`.
Examples:
  * `"abc".set ⟨1⟩ 'B' = "aBc"`
  * `"abc".set ⟨3⟩ 'D' = "abc"`
  * `"L∃∀N".set ⟨4⟩ 'X' = "L∃XN"`
  * `"L∃∀N".set ⟨2⟩ 'X' = "L∃∀N"` because `'∃'` is a multi-byte character, so the byte index `2` is an invalid position.


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Pos.Raw.modify "Permalink")def
```


String.Pos.Raw.modify (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (i : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (f : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.Pos.Raw.modify (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (i : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) (f : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) :
  [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Replaces the character at position `p` in the string `s` with the result of applying `f` to that character. If `p` is an invalid position, the string is returned unchanged.
If both the replacement character and the replaced character are 7-bit ASCII characters and the string is not shared, then it is updated in-place and not copied.
This is a legacy function. The recommended alternative is `[String.Pos.set](Basic-Types/Strings/#String___Pos___set "Documentation for String.Pos.set")`, combined with `[String.pos](Basic-Types/Strings/#String___pos "Documentation for String.pos")` or another means of obtaining a `[String.Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")`.
Examples:
  * `"abc".modify ⟨1⟩ [Char.toUpper](Basic-Types/Characters/#Char___toUpper "Documentation for Char.toUpper") = "aBc"`
  * `"abc".modify ⟨3⟩ [Char.toUpper](Basic-Types/Characters/#Char___toUpper "Documentation for Char.toUpper") = "abc"`


###  20.8.4.6. Lookups and Modifications[🔗](find/?domain=Verso.Genre.Manual.section&name=string-api-lookup "Permalink")
Operations that select a sub-region of a string (for example, a prefix or suffix of it) return a [slice](Basic-Types/Strings/#string-api-slice) into the original string rather than allocating a new string. Use `[String.Slice.copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")` to convert the slice into a new string.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.take "Permalink")def
```


String.take (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.take (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Returns a `[String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")` that contains the first `n` characters (Unicode code points) of `s`.
If `n` is greater than `s.[length](Basic-Types/Strings/#String___length "Documentation for String.length")`, returns `s.[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`.
This is a cheap operation because it does not allocate a new string to hold the result. To convert the result into a string, use `[String.Slice.copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")`.
Examples:
  * `"red green blue".[take](Basic-Types/Strings/#String___take "Documentation for String.take") 3 == "red".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[take](Basic-Types/Strings/#String___take "Documentation for String.take") 1 == "r".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[take](Basic-Types/Strings/#String___take "Documentation for String.take") 0 == "".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[take](Basic-Types/Strings/#String___take "Documentation for String.take") 100 == "red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"مرحبا بالعالم".[take](Basic-Types/Strings/#String___take "Documentation for String.take") 5 == "مرحبا".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.takeWhile "Permalink")def
```


String.takeWhile {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern") pat] : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.takeWhile {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern")
      pat] :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Creates a string slice that contains the longest prefix of `s` in which `pat` matched (potentially repeatedly).
This is a cheap operation because it does not allocate a new string to hold the result. To convert the result into a string, use `[String.Slice.copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")`.
This function is generic over all currently supported patterns.
Examples:
  * `"red green blue".[takeWhile](Basic-Types/Strings/#String___takeWhile "Documentation for String.takeWhile") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") == "red".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[takeWhile](Basic-Types/Strings/#String___takeWhile "Documentation for String.takeWhile") 'r' == "r".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red red green blue".[takeWhile](Basic-Types/Strings/#String___takeWhile "Documentation for String.takeWhile") "red " == "red red ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[takeWhile](Basic-Types/Strings/#String___takeWhile "Documentation for String.takeWhile") (fun (_ : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) == "red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.takeEnd "Permalink")def
```


String.takeEnd (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.takeEnd (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Returns a `[String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")` that contains the last `n` characters (Unicode code points) of `s`.
If `n` is greater than `s.[length](Basic-Types/Strings/#String___length "Documentation for String.length")`, returns `s.[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`.
This is a cheap operation because it does not allocate a new string to hold the result. To convert the result into a string, use `[String.Slice.copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")`.
Examples:
  * `"red green blue".[takeEnd](Basic-Types/Strings/#String___takeEnd "Documentation for String.takeEnd") 4 == "blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[takeEnd](Basic-Types/Strings/#String___takeEnd "Documentation for String.takeEnd") 1 == "e".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[takeEnd](Basic-Types/Strings/#String___takeEnd "Documentation for String.takeEnd") 0 == "".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[takeEnd](Basic-Types/Strings/#String___takeEnd "Documentation for String.takeEnd") 100 == "red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"مرحبا بالعالم".[takeEnd](Basic-Types/Strings/#String___takeEnd "Documentation for String.takeEnd") 5 == "لعالم".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.takeEndWhile "Permalink")def
```


String.takeEndWhile {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern") pat] : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.takeEndWhile {ρ : Type}
  (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern")
      pat] :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Creates a string slice that contains the longest suffix of `s` in which `pat` matched (potentially repeatedly).
This is a cheap operation because it does not allocate a new string to hold the result. To convert the result into a string, use `[String.Slice.copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")`.
This function is generic over all currently supported patterns.
Examples:
  * `"red green blue".[takeEndWhile](Basic-Types/Strings/#String___takeEndWhile "Documentation for String.takeEndWhile") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") == "blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[takeEndWhile](Basic-Types/Strings/#String___takeEndWhile "Documentation for String.takeEndWhile") 'e' == "e".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[takeEndWhile](Basic-Types/Strings/#String___takeEndWhile "Documentation for String.takeEndWhile") (fun (_ : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) == "red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.drop "Permalink")def
```


String.drop (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.drop (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Returns a `[String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")` obtained by removing the specified number of characters (Unicode code points) from the start of the string.
If `n` is greater than `s.[length](Basic-Types/Strings/#String___length "Documentation for String.length")`, returns an empty slice.
This is a cheap operation because it does not allocate a new string to hold the result. To convert the result into a string, use `[String.Slice.copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")`.
Examples:
  * `"red green blue".[drop](Basic-Types/Strings/#String___drop "Documentation for String.drop") 4 == "green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[drop](Basic-Types/Strings/#String___drop "Documentation for String.drop") 10 == "blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[drop](Basic-Types/Strings/#String___drop "Documentation for String.drop") 50 == "".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"مرحبا بالعالم".[drop](Basic-Types/Strings/#String___drop "Documentation for String.drop") 3 == "با بالعالم".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.dropWhile "Permalink")def
```


String.dropWhile {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern") pat] : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.dropWhile {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern")
      pat] :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Creates a string slice by removing the longest prefix from `s` in which `pat` matched (potentially repeatedly).
This is a cheap operation because it does not allocate a new string to hold the result. To convert the result into a string, use `[String.Slice.copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")`.
This function is generic over all currently supported patterns.
Examples:
  * `"red green blue".[dropWhile](Basic-Types/Strings/#String___dropWhile "Documentation for String.dropWhile") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") == " green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[dropWhile](Basic-Types/Strings/#String___dropWhile "Documentation for String.dropWhile") 'r' == "ed green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red red green blue".[dropWhile](Basic-Types/Strings/#String___dropWhile "Documentation for String.dropWhile") "red " == "green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[dropWhile](Basic-Types/Strings/#String___dropWhile "Documentation for String.dropWhile") (fun (_ : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) == "".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.dropEnd "Permalink")def
```


String.dropEnd (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.dropEnd (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Returns a `[String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")` obtained by removing the specified number of characters (Unicode code points) from the end of the string.
If `n` is greater than `s.[length](Basic-Types/Strings/#String___length "Documentation for String.length")`, returns an empty slice.
This is a cheap operation because it does not allocate a new string to hold the result. To convert the result into a string, use `[String.Slice.copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")`.
Examples:
  * `"red green blue".[dropEnd](Basic-Types/Strings/#String___dropEnd "Documentation for String.dropEnd") 5 == "red green".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[dropEnd](Basic-Types/Strings/#String___dropEnd "Documentation for String.dropEnd") 11 == "red".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[dropEnd](Basic-Types/Strings/#String___dropEnd "Documentation for String.dropEnd") 50 == "".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"مرحبا بالعالم".[dropEnd](Basic-Types/Strings/#String___dropEnd "Documentation for String.dropEnd") 3 == "مرحبا بالع".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.dropEndWhile "Permalink")def
```


String.dropEndWhile {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern") pat] : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.dropEndWhile {ρ : Type}
  (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern")
      pat] :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Creates a new string by removing the longest suffix from `s` in which `pat` matches (potentially repeatedly).
This is a cheap operation because it does not allocate a new string to hold the result. To convert the result into a string, use `[String.Slice.copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")`.
This function is generic over all currently supported patterns.
Examples:
  * `"red green blue".[dropEndWhile](Basic-Types/Strings/#String___dropEndWhile "Documentation for String.dropEndWhile") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") == "red green ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[dropEndWhile](Basic-Types/Strings/#String___dropEndWhile "Documentation for String.dropEndWhile") 'e' == "red green blu".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[dropEndWhile](Basic-Types/Strings/#String___dropEndWhile "Documentation for String.dropEndWhile") (fun (_ : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) == "".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.dropPrefix? "Permalink")def
```


String.dropPrefix? {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern") pat] : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.dropPrefix? {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern")
      pat] :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

If `pat` matches a prefix of `s`, returns the remainder. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` otherwise.
Use `[String.dropPrefix](Basic-Types/Strings/#String___dropPrefix "Documentation for String.dropPrefix")` to return the slice unchanged when `pat` does not match a prefix.
This is a cheap operation because it does not allocate a new string to hold the result. To convert the result into a string, use `[String.Slice.copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")`.
This function is generic over all currently supported patterns.
Examples:
  * `"red green blue".[dropPrefix?](Basic-Types/Strings/#String___dropPrefix___ "Documentation for String.dropPrefix?") "red " == [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[dropPrefix?](Basic-Types/Strings/#String___dropPrefix___ "Documentation for String.dropPrefix?") "reed " == [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `"red green blue".[dropPrefix?](Basic-Types/Strings/#String___dropPrefix___ "Documentation for String.dropPrefix?") 'r' == [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "ed green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[dropPrefix?](Basic-Types/Strings/#String___dropPrefix___ "Documentation for String.dropPrefix?") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") == [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "ed green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.dropPrefix "Permalink")def
```


String.dropPrefix {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern") pat] : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.dropPrefix {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern")
      pat] :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

If `pat` matches a prefix of `s`, returns the remainder. Returns `s` unmodified otherwise.
Use `[String.dropPrefix?](Basic-Types/Strings/#String___dropPrefix___ "Documentation for String.dropPrefix?")` to return `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` when `pat` does not match a prefix.
This is a cheap operation because it does not allocate a new string to hold the result. To convert the result into a string, use `[String.Slice.copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")`.
This function is generic over all currently supported patterns.
Examples:
  * `"red green blue".[dropPrefix](Basic-Types/Strings/#String___dropPrefix "Documentation for String.dropPrefix") "red " == "green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[dropPrefix](Basic-Types/Strings/#String___dropPrefix "Documentation for String.dropPrefix") "reed " == "red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[dropPrefix](Basic-Types/Strings/#String___dropPrefix "Documentation for String.dropPrefix") 'r' == "ed green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[dropPrefix](Basic-Types/Strings/#String___dropPrefix "Documentation for String.dropPrefix") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") == "ed green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.dropSuffix? "Permalink")def
```


String.dropSuffix? {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern") pat] : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.dropSuffix? {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern")
      pat] :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

If `pat` matches a suffix of `s`, returns the remainder. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` otherwise.
Use `[String.dropSuffix](Basic-Types/Strings/#String___dropSuffix "Documentation for String.dropSuffix")` to return the slice unchanged when `pat` does not match a prefix.
This is a cheap operation because it does not allocate a new string to hold the result. To convert the result into a string, use `[String.Slice.copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")`.
This function is generic over all currently supported patterns.
Examples:
  * `"red green blue".[dropSuffix?](Basic-Types/Strings/#String___dropSuffix___ "Documentation for String.dropSuffix?") " blue" == [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "red green".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[dropSuffix?](Basic-Types/Strings/#String___dropSuffix___ "Documentation for String.dropSuffix?") "bluu " == [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `"red green blue".[dropSuffix?](Basic-Types/Strings/#String___dropSuffix___ "Documentation for String.dropSuffix?") 'e' == [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "red green blu".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[dropSuffix?](Basic-Types/Strings/#String___dropSuffix___ "Documentation for String.dropSuffix?") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") == [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "red green blu".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.dropSuffix "Permalink")def
```


String.dropSuffix {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern") pat] : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.dropSuffix {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern")
      pat] :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

If `pat` matches a suffix of `s`, returns the remainder. Returns `s` unmodified otherwise.
Use `[String.dropSuffix?](Basic-Types/Strings/#String___dropSuffix___ "Documentation for String.dropSuffix?")` to return `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` when `pat` does not match a prefix.
This is a cheap operation because it does not allocate a new string to hold the result. To convert the result into a string, use `[String.Slice.copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")`.
This function is generic over all currently supported patterns.
Examples:
  * `"red green blue".[dropSuffix](Basic-Types/Strings/#String___dropSuffix "Documentation for String.dropSuffix") " blue" == "red green".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[dropSuffix](Basic-Types/Strings/#String___dropSuffix "Documentation for String.dropSuffix") "bluu " == "red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[dropSuffix](Basic-Types/Strings/#String___dropSuffix "Documentation for String.dropSuffix") 'e' == "red green blu".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[dropSuffix](Basic-Types/Strings/#String___dropSuffix "Documentation for String.dropSuffix") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") == "red green blu".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.trimAscii "Permalink")def
```


String.trimAscii (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.trimAscii (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Removes leading and trailing whitespace from a string.
“Whitespace” is defined as characters for which `[Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace")` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Examples:
  * `"abc".[trimAscii](Basic-Types/Strings/#String___trimAscii "Documentation for String.trimAscii") == "abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"   abc".[trimAscii](Basic-Types/Strings/#String___trimAscii "Documentation for String.trimAscii") == "abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"abc \t  ".[trimAscii](Basic-Types/Strings/#String___trimAscii "Documentation for String.trimAscii") == "abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"  abc   ".[trimAscii](Basic-Types/Strings/#String___trimAscii "Documentation for String.trimAscii") == "abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"abc\ndef\n".[trimAscii](Basic-Types/Strings/#String___trimAscii "Documentation for String.trimAscii") == "abc\ndef".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.trimAsciiStart "Permalink")def
```


String.trimAsciiStart (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.trimAsciiStart (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Removes leading whitespace from a string by returning a slice whose start position is the first non-whitespace character, or the end position if there is no non-whitespace character.
“Whitespace” is defined as characters for which `[Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace")` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Examples:
  * `"abc".[trimAsciiStart](Basic-Types/Strings/#String___trimAsciiStart "Documentation for String.trimAsciiStart") == "abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"   abc".[trimAsciiStart](Basic-Types/Strings/#String___trimAsciiStart "Documentation for String.trimAsciiStart") == "abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"abc \t  ".[trimAsciiStart](Basic-Types/Strings/#String___trimAsciiStart "Documentation for String.trimAsciiStart") == "abc \t  ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"  abc   ".[trimAsciiStart](Basic-Types/Strings/#String___trimAsciiStart "Documentation for String.trimAsciiStart") == "abc   ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"abc\ndef\n".[trimAsciiStart](Basic-Types/Strings/#String___trimAsciiStart "Documentation for String.trimAsciiStart") == "abc\ndef\n".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.trimAsciiEnd "Permalink")def
```


String.trimAsciiEnd (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.trimAsciiEnd (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Removes trailing whitespace from a string by returning a slice whose end position is the last non-whitespace character, or the start position if there is no non-whitespace character.
“Whitespace” is defined as characters for which `[Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace")` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Examples:
  * `"abc".[trimAsciiEnd](Basic-Types/Strings/#String___trimAsciiEnd "Documentation for String.trimAsciiEnd") == "abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"   abc".[trimAsciiEnd](Basic-Types/Strings/#String___trimAsciiEnd "Documentation for String.trimAsciiEnd") == "   abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"abc \t  ".[trimAsciiEnd](Basic-Types/Strings/#String___trimAsciiEnd "Documentation for String.trimAsciiEnd") == "abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"  abc   ".[trimAsciiEnd](Basic-Types/Strings/#String___trimAsciiEnd "Documentation for String.trimAsciiEnd") == "  abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"abc\ndef\n".[trimAsciiEnd](Basic-Types/Strings/#String___trimAsciiEnd "Documentation for String.trimAsciiEnd") == "abc\ndef".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.removeLeadingSpaces "Permalink")def
```


String.removeLeadingSpaces (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.removeLeadingSpaces (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Consistently de-indents the lines in a string, removing the same amount of leading whitespace from each line such that the least-indented line has no leading whitespace.
The number of leading whitespace characters to remove from each line is determined by counting the number of leading space (`' '`) and tab (`'\t'`) characters on lines after the first line that also contain non-whitespace characters. No distinction is made between tab and space characters; both count equally.
The least number of leading whitespace characters found is then removed from the beginning of each line. The first line's leading whitespace is not counted when determining how far to de-indent the string, but leading whitespace is removed from it.
Examples:
  * `"Here:\n  fun x =>\n    x + 1".[removeLeadingSpaces](Basic-Types/Strings/#String___removeLeadingSpaces "Documentation for String.removeLeadingSpaces") = "Here:\nfun x =>\n  x + 1"`
  * `"Here:\n\t\tfun x =>\n\t  \tx + 1".[removeLeadingSpaces](Basic-Types/Strings/#String___removeLeadingSpaces "Documentation for String.removeLeadingSpaces") = "Here:\nfun x =>\n \tx + 1"`
  * `"Here:\n\t\tfun x =>\n \n\t  \tx + 1".[removeLeadingSpaces](Basic-Types/Strings/#String___removeLeadingSpaces "Documentation for String.removeLeadingSpaces") = "Here:\nfun x =>\n\n \tx + 1"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.front "Permalink")def
```


String.front (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.front (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Returns the first character in `s`. If `s = ""`, returns `([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))`.
Examples:
  * `"abc".[front](Basic-Types/Strings/#String___front "Documentation for String.front") = 'a'`
  * `"".[front](Basic-Types/Strings/#String___front "Documentation for String.front") = ([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.back "Permalink")def
```


String.back (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.back (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Returns the last character in `s`. If `s = ""`, returns `([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))`.
Examples:
  * `"abc".[back](Basic-Types/Strings/#String___back "Documentation for String.back") = 'c'`
  * `"".[back](Basic-Types/Strings/#String___back "Documentation for String.back") = ([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.find "Permalink")def
```


String.find {ρ : Type} {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") (String.Slice.Pattern.SearchStep s)]
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) → [Std.IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (pattern : ρ) [[String.Slice.Pattern.ToForwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToForwardSearcher___mk "Documentation for String.Slice.Pattern.ToForwardSearcher") pattern σ] :
  s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


String.find {ρ : Type}
  {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")
        (String.Slice.Pattern.SearchStep
          s)]
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pattern : ρ)
  [[String.Slice.Pattern.ToForwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToForwardSearcher___mk "Documentation for String.Slice.Pattern.ToForwardSearcher")
      pattern σ] :
  s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


```

Finds the position of the first match of the pattern `pattern` in a slice `s`. If there is no match `s.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")` is returned.
This function is generic over all currently supported patterns.
Examples:
  * `("coffee tea water".find [Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace")).[get!](Basic-Types/Strings/#String___Pos___get___ "Documentation for String.Pos.get!") == ' '`
  * `"tea".find (fun (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) => c == 'X') == "tea".[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")`
  * `("coffee tea water".find "tea").[get!](Basic-Types/Strings/#String___Pos___get___ "Documentation for String.Pos.get!") == 't'`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.revFind? "Permalink")def
```


String.revFind? {ρ : Type} {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") (String.Slice.Pattern.SearchStep s)]
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) → [Std.IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (pattern : ρ) [[String.Slice.Pattern.ToBackwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToBackwardSearcher___mk "Documentation for String.Slice.Pattern.ToBackwardSearcher") pattern σ] :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


String.revFind? {ρ : Type}
  {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")
        (String.Slice.Pattern.SearchStep
          s)]
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pattern : ρ)
  [[String.Slice.Pattern.ToBackwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToBackwardSearcher___mk "Documentation for String.Slice.Pattern.ToBackwardSearcher")
      pattern σ] :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


```

Finds the position of the first match of the pattern `pattern` in a string, starting from the end of the slice and traversing towards the start. If there is no match `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` is returned.
This function is generic over all currently supported patterns except `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`/`[String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")`.
Examples:
  * `("coffee tea water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[revFind?](Basic-Types/Strings/#String___Slice___revFind___ "Documentation for String.Slice.revFind?") [Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace")).[map](Basic-Types/Optional-Values/#Option___map "Documentation for Option.map") (·.[get!](Basic-Types/Strings/#String___Slice___Pos___get___ "Documentation for String.Slice.Pos.get!")) == [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ' '`
  * `"tea".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[revFind?](Basic-Types/Strings/#String___Slice___revFind___ "Documentation for String.Slice.revFind?") (fun (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) => c == 'X') == [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=String.some%E2%86%AAString.contains "Permalink")def
```


String.contains {ρ : Type} {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") (String.Slice.Pattern.SearchStep s)]
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) → [Std.IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (pat : ρ) [[String.Slice.Pattern.ToForwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToForwardSearcher___mk "Documentation for String.Slice.Pattern.ToForwardSearcher") pat σ] : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.contains {ρ : Type}
  {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")
        (String.Slice.Pattern.SearchStep
          s)]
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pat : ρ)
  [[String.Slice.Pattern.ToForwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToForwardSearcher___mk "Documentation for String.Slice.Pattern.ToForwardSearcher")
      pat σ] :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a string has a match of the pattern `pat` anywhere.
This function is generic over all currently supported patterns.
Examples:
  * `"coffee tea water".[contains](Basic-Types/Strings/#String___contains "Documentation for String.contains") [Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"tea".[contains](Basic-Types/Strings/#String___contains "Documentation for String.contains") (fun (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) => c == 'X') = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"coffee tea water".[contains](Basic-Types/Strings/#String___contains "Documentation for String.contains") "tea" = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.replace "Permalink")def
```


String.replace.{u_1} {ρ : Type} {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") (String.Slice.Pattern.SearchStep s)]
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) → [Std.IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] {α : Type u_1}
  [String.ToSlice α] (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pattern : ρ)
  [[String.Slice.Pattern.ToForwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToForwardSearcher___mk "Documentation for String.Slice.Pattern.ToForwardSearcher") pattern σ] (replacement : α) :
  [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.replace.{u_1} {ρ : Type}
  {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")
        (String.Slice.Pattern.SearchStep
          s)]
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  {α : Type u_1} [String.ToSlice α]
  (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pattern : ρ)
  [[String.Slice.Pattern.ToForwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToForwardSearcher___mk "Documentation for String.Slice.Pattern.ToForwardSearcher")
      pattern σ]
  (replacement : α) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Constructs a new string obtained by replacing all occurrences of `pattern` with `replacement` in `s`.
This function is generic over all currently supported patterns. The replacement may be a `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` or a `[String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")`.
Examples:
  * `"red green blue".[replace](Basic-Types/Strings/#String___replace "Documentation for String.replace") 'e' "" = "rd grn blu"`
  * `"red green blue".[replace](Basic-Types/Strings/#String___replace "Documentation for String.replace") (fun c => c == 'u' || c == 'e') "" = "rd grn bl"`
  * `"red green blue".[replace](Basic-Types/Strings/#String___replace "Documentation for String.replace") "e" "" = "rd grn blu"`
  * `"red green blue".[replace](Basic-Types/Strings/#String___replace "Documentation for String.replace") "ee" "E" = "red grEn blue"`
  * `"red green blue".[replace](Basic-Types/Strings/#String___replace "Documentation for String.replace") "e" "E" = "rEd grEEn bluE"`
  * `"aaaaa".[replace](Basic-Types/Strings/#String___replace "Documentation for String.replace") "aa" "b" = "bba"`
  * `"abc".[replace](Basic-Types/Strings/#String___replace "Documentation for String.replace") "" "k" = "kakbkck"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.find "Permalink")def
```


String.find {ρ : Type} {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") (String.Slice.Pattern.SearchStep s)]
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) → [Std.IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (pattern : ρ) [[String.Slice.Pattern.ToForwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToForwardSearcher___mk "Documentation for String.Slice.Pattern.ToForwardSearcher") pattern σ] :
  s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


String.find {ρ : Type}
  {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")
        (String.Slice.Pattern.SearchStep
          s)]
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pattern : ρ)
  [[String.Slice.Pattern.ToForwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToForwardSearcher___mk "Documentation for String.Slice.Pattern.ToForwardSearcher")
      pattern σ] :
  s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


```

Finds the position of the first match of the pattern `pattern` in a slice `s`. If there is no match `s.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")` is returned.
This function is generic over all currently supported patterns.
Examples:
  * `("coffee tea water".find [Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace")).[get!](Basic-Types/Strings/#String___Pos___get___ "Documentation for String.Pos.get!") == ' '`
  * `"tea".find (fun (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) => c == 'X') == "tea".[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")`
  * `("coffee tea water".find "tea").[get!](Basic-Types/Strings/#String___Pos___get___ "Documentation for String.Pos.get!") == 't'`


###  20.8.4.7. Folds and Aggregation[🔗](find/?domain=Verso.Genre.Manual.section&name=string-api-fold "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.map "Permalink")def
```


String.map (f : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.map (f : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))
  (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Applies the function `f` to every character in a string, returning a string that contains the resulting characters.
Examples:
  * `"abc123".[map](Basic-Types/Strings/#String___map "Documentation for String.map") [Char.toUpper](Basic-Types/Characters/#Char___toUpper "Documentation for Char.toUpper") = "ABC123"`
  * `"".[map](Basic-Types/Strings/#String___map "Documentation for String.map") [Char.toUpper](Basic-Types/Characters/#Char___toUpper "Documentation for Char.toUpper") = ""`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.foldl "Permalink")def
```


String.foldl.{u} {α : Type u} (f : α → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → α) (init : α)
  (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : α


String.foldl.{u} {α : Type u}
  (f : α → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → α) (init : α)
  (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : α


```

Folds a function over a string from the start, accumulating a value starting with `init`. The accumulated value is combined with each character in order, using `f`.
Examples:
  * `"coffee tea water".[foldl](Basic-Types/Strings/#String___foldl "Documentation for String.foldl") (fun n c => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") c.[isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace") [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n + 1 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n) 0 = 2`
  * `"coffee tea and water".[foldl](Basic-Types/Strings/#String___foldl "Documentation for String.foldl") (fun n c => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") c.[isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace") [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n + 1 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n) 0 = 3`
  * `"coffee tea water".[foldl](Basic-Types/Strings/#String___foldl "Documentation for String.foldl") (·.[push](Basic-Types/Strings/#String___push "Documentation for String.push") ·) "" = "coffee tea water"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.foldr "Permalink")def
```


String.foldr.{u} {α : Type u} (f : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → α → α) (init : α)
  (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : α


String.foldr.{u} {α : Type u}
  (f : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → α → α) (init : α)
  (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : α


```

Folds a function over a string from the right, accumulating a value starting with `init`. The accumulated value is combined with each character in reverse order, using `f`.
Examples:
  * `"coffee tea water".[foldr](Basic-Types/Strings/#String___foldr "Documentation for String.foldr") (fun c n => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") c.[isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace") [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n + 1 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n) 0 = 2`
  * `"coffee tea and water".[foldr](Basic-Types/Strings/#String___foldr "Documentation for String.foldr") (fun c n => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") c.[isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace") [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n + 1 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n) 0 = 3`
  * `"coffee tea water".[foldr](Basic-Types/Strings/#String___foldr "Documentation for String.foldr") (fun c s => s.[push](Basic-Types/Strings/#String___push "Documentation for String.push") c) "" = "retaw aet eeffoc"`


[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=String.every%E2%86%AAString.all "Permalink")def
```


String.all {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern") pat] : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.all {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern")
      pat] :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a slice only consists of matches of the pattern `pat`.
Short-circuits at the first pattern mis-match.
This function is generic over all currently supported patterns.
Examples:
  * `"brown".[all](Basic-Types/Strings/#String___all "Documentation for String.all") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"brown and orange".[all](Basic-Types/Strings/#String___all "Documentation for String.all") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"aaaaaa".[all](Basic-Types/Strings/#String___all "Documentation for String.all") 'a' = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"aaaaaa".[all](Basic-Types/Strings/#String___all "Documentation for String.all") "aa" = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"aaaaaaa".[all](Basic-Types/Strings/#String___all "Documentation for String.all") "aa" = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.any "Permalink")def
```


String.any {ρ : Type} {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") (String.Slice.Pattern.SearchStep s)]
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) → [Std.IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (pat : ρ) [[String.Slice.Pattern.ToForwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToForwardSearcher___mk "Documentation for String.Slice.Pattern.ToForwardSearcher") pat σ] : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.any {ρ : Type}
  {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")
        (String.Slice.Pattern.SearchStep
          s)]
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pat : ρ)
  [[String.Slice.Pattern.ToForwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToForwardSearcher___mk "Documentation for String.Slice.Pattern.ToForwardSearcher")
      pat σ] :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a string has a match of the pattern `pat` anywhere.
This function is generic over all currently supported patterns.
Examples:
  * `"coffee tea water".[contains](Basic-Types/Strings/#String___contains "Documentation for String.contains") [Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"tea".[contains](Basic-Types/Strings/#String___contains "Documentation for String.contains") (fun (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) => c == 'X') = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"coffee tea water".[contains](Basic-Types/Strings/#String___contains "Documentation for String.contains") "tea" = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


###  20.8.4.8. Comparisons[🔗](find/?domain=Verso.Genre.Manual.section&name=string-api-compare "Permalink")
The `[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` instance is defined by the lexicographic ordering on strings based on the `[LT](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")` instance. Logically, this is modeled by the lexicographic ordering on the lists that model strings, so `List.Lex` defines the order. It is decidable, and the decision procedure is overridden at runtime with efficient code that takes advantage of the run-time representation of strings.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.le "Permalink")def
```


String.le (a b : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : Prop


String.le (a b : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : Prop


```

Non-strict inequality on strings, typically used via the `≤` operator.
`a ≤ b` is defined to mean `¬ b < a`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.firstDiffPos "Permalink")def
```


String.firstDiffPos (a b : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


String.firstDiffPos (a b : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

Returns the first position where the two strings differ.
If one string is a prefix of the other, then the returned position is the end position of the shorter string. If the strings are identical, then their end position is returned.
Examples:
  * `"tea".[firstDiffPos](Basic-Types/Strings/#String___firstDiffPos "Documentation for String.firstDiffPos") "ten" = ⟨2⟩`
  * `"tea".[firstDiffPos](Basic-Types/Strings/#String___firstDiffPos "Documentation for String.firstDiffPos") "tea" = ⟨3⟩`
  * `"tea".[firstDiffPos](Basic-Types/Strings/#String___firstDiffPos "Documentation for String.firstDiffPos") "teas" = ⟨3⟩`
  * `"teas".[firstDiffPos](Basic-Types/Strings/#String___firstDiffPos "Documentation for String.firstDiffPos") "tea" = ⟨3⟩`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.isPrefixOf "Permalink")def
```


String.isPrefixOf (p s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.isPrefixOf (p s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the second string (`s`) begins with a prefix (`p`).
This function is generic over all currently supported patterns.
`[String.startsWith](Basic-Types/Strings/#String___startsWith "Documentation for String.startsWith")` is a version that takes the potential prefix after the string.
Examples:
  * `"red".[isPrefixOf](Basic-Types/Strings/#String___isPrefixOf "Documentation for String.isPrefixOf") "red green blue" = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"green".[isPrefixOf](Basic-Types/Strings/#String___isPrefixOf "Documentation for String.isPrefixOf") "red green blue" = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"".[isPrefixOf](Basic-Types/Strings/#String___isPrefixOf "Documentation for String.isPrefixOf") "red green blue" = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.startsWith "Permalink")def
```


String.startsWith {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern") pat] : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.startsWith {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern")
      pat] :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the first string (`s`) begins with the pattern (`pat`).
`[String.isPrefixOf](Basic-Types/Strings/#String___isPrefixOf "Documentation for String.isPrefixOf")` is a version that takes the potential prefix before the string.
Examples:
  * `"red green blue".[startsWith](Basic-Types/Strings/#String___startsWith "Documentation for String.startsWith") "red" = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"red green blue".[startsWith](Basic-Types/Strings/#String___startsWith "Documentation for String.startsWith") "green" = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"red green blue".[startsWith](Basic-Types/Strings/#String___startsWith "Documentation for String.startsWith") "" = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"red green blue".[startsWith](Basic-Types/Strings/#String___startsWith "Documentation for String.startsWith") 'r' = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"red green blue".[startsWith](Basic-Types/Strings/#String___startsWith "Documentation for String.startsWith") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.endsWith "Permalink")def
```


String.endsWith {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern") pat] : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.endsWith {ρ : Type} (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern")
      pat] :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the string (`s`) ends with the pattern (`pat`).
This function is generic over all currently supported patterns.
Examples:
  * `"red green blue".[endsWith](Basic-Types/Strings/#String___endsWith "Documentation for String.endsWith") "blue" = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"red green blue".[endsWith](Basic-Types/Strings/#String___endsWith "Documentation for String.endsWith") "green" = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"red green blue".[endsWith](Basic-Types/Strings/#String___endsWith "Documentation for String.endsWith") "" = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"red green blue".[endsWith](Basic-Types/Strings/#String___endsWith "Documentation for String.endsWith") 'e' = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"red green blue".[endsWith](Basic-Types/Strings/#String___endsWith "Documentation for String.endsWith") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.decEq "Permalink")def
```


String.decEq (s₁ s₂ : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")s₁ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") s₂[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


String.decEq (s₁ s₂ : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")s₁ [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") s₂[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")


```

Decides whether two strings are equal. Normally used via the `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` instance and the `=` operator.
At runtime, this function is overridden with an efficient native implementation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.hash "Permalink")opaque
```


String.hash (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


String.hash (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [UInt64](Basic-Types/Fixed-Precision-Integers/#UInt64___ofBitVec "Documentation for UInt64")


```

Computes a hash for strings.
###  20.8.4.9. Manipulation[🔗](find/?domain=Verso.Genre.Manual.section&name=string-api-modify "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.splitToList "Permalink")def
```


String.splitToList (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (p : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.splitToList (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (p : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Splits a string at each character for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
The characters that satisfy `p` are not included in any of the resulting strings. If multiple characters in a row satisfy `p`, then the resulting list will contain empty strings.
This is a legacy function. Use `String.split` instead.
Examples:
  * `"coffee tea water".split (·.isWhitespace) = ["coffee", "tea", "water"]`
  * `"coffee  tea  water".split (·.isWhitespace) = ["coffee", "", "tea", "", "water"]`
  * `"fun x =>\n  x + 1\n".split (· == '\n') = ["fun x =>", "  x + 1", ""]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.splitOn "Permalink")def
```


String.splitOn (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (sep : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := " ") : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.splitOn (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (sep : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := " ") : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Splits a string `s` on occurrences of the separator string `sep`. The default separator is `" "`.
When `sep` is empty, the result is `[s]`. When `sep` occurs in overlapping patterns, the first match is taken. There will always be exactly `n+1` elements in the returned list if there were `n` non-overlapping matches of `sep` in the string. The separators are not included in the returned substrings.
This is a legacy function. Use `String.split` instead.
Examples:
  * `"here is some text ".[splitOn](Basic-Types/Strings/#String___splitOn "Documentation for String.splitOn") = ["here", "is", "some", "text", ""]`
  * `"here is some text ".[splitOn](Basic-Types/Strings/#String___splitOn "Documentation for String.splitOn") "some" = ["here is ", " text "]`
  * `"here is some text ".[splitOn](Basic-Types/Strings/#String___splitOn "Documentation for String.splitOn") "" = ["here is some text "]`
  * `"ababacabac".[splitOn](Basic-Types/Strings/#String___splitOn "Documentation for String.splitOn") "aba" = ["", "bac", "c"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.push "Permalink")def
```


String.push : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.push : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Adds a character to the end of a string.
The internal implementation uses dynamic arrays and will perform destructive updates if the string is not shared.
Examples:
  * `"abc".[push](Basic-Types/Strings/#String___push "Documentation for String.push") 'd' = "abcd"`
  * `"".[push](Basic-Types/Strings/#String___push "Documentation for String.push") 'a' = "a"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.pushn "Permalink")def
```


String.pushn (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.pushn (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Adds multiple repetitions of a character to the end of a string.
Returns `s`, with `n` repetitions of `c` at the end. Internally, the implementation repeatedly calls `[String.push](Basic-Types/Strings/#String___push "Documentation for String.push")`, so the string is modified in-place if there is a unique reference to it.
Examples:
  * `"indeed".[pushn](Basic-Types/Strings/#String___pushn "Documentation for String.pushn") '!' 2 = "indeed!!"`
  * `"indeed".[pushn](Basic-Types/Strings/#String___pushn "Documentation for String.pushn") '!' 0 = "indeed"`
  * `"".[pushn](Basic-Types/Strings/#String___pushn "Documentation for String.pushn") ' ' 4 = "    "`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.capitalize "Permalink")def
```


String.capitalize (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.capitalize (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Replaces the first character in `s` with the result of applying `[Char.toUpper](Basic-Types/Characters/#Char___toUpper "Documentation for Char.toUpper")` to it. Returns the empty string if the string is empty.
`[Char.toUpper](Basic-Types/Characters/#Char___toUpper "Documentation for Char.toUpper")` has no effect on characters outside of the range `'a'`–`'z'`.
Examples:
  * `"orange".[capitalize](Basic-Types/Strings/#String___capitalize "Documentation for String.capitalize") = "Orange"`
  * `"ORANGE".[capitalize](Basic-Types/Strings/#String___capitalize "Documentation for String.capitalize") = "ORANGE"`
  * `"".[capitalize](Basic-Types/Strings/#String___capitalize "Documentation for String.capitalize") = ""`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.decapitalize "Permalink")def
```


String.decapitalize (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.decapitalize (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Replaces the first character in `s` with the result of applying `[Char.toLower](Basic-Types/Characters/#Char___toLower "Documentation for Char.toLower")` to it. Returns the empty string if the string is empty.
`[Char.toLower](Basic-Types/Characters/#Char___toLower "Documentation for Char.toLower")` has no effect on characters outside of the range `'A'`–`'Z'`.
Examples:
  * `"Orange".[decapitalize](Basic-Types/Strings/#String___decapitalize "Documentation for String.decapitalize") = "orange"`
  * `"ORANGE".[decapitalize](Basic-Types/Strings/#String___decapitalize "Documentation for String.decapitalize") = "oRANGE"`
  * `"".[decapitalize](Basic-Types/Strings/#String___decapitalize "Documentation for String.decapitalize") = ""`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.toUpper "Permalink")def
```


String.toUpper (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.toUpper (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Replaces each character in `s` with the result of applying `[Char.toUpper](Basic-Types/Characters/#Char___toUpper "Documentation for Char.toUpper")` to it.
`[Char.toUpper](Basic-Types/Characters/#Char___toUpper "Documentation for Char.toUpper")` has no effect on characters outside of the range `'a'`–`'z'`.
Examples:
  * `"orange".[toUpper](Basic-Types/Strings/#String___toUpper "Documentation for String.toUpper") = "ORANGE"`
  * `"abc123".[toUpper](Basic-Types/Strings/#String___toUpper "Documentation for String.toUpper") = "ABC123"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.toLower "Permalink")def
```


String.toLower (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.toLower (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Replaces each character in `s` with the result of applying `[Char.toLower](Basic-Types/Characters/#Char___toLower "Documentation for Char.toLower")` to it.
`[Char.toLower](Basic-Types/Characters/#Char___toLower "Documentation for Char.toLower")` has no effect on characters outside of the range `'A'`–`'Z'`.
Examples:
  * `"ORANGE".[toLower](Basic-Types/Strings/#String___toLower "Documentation for String.toLower") = "orange"`
  * `"Orange".[toLower](Basic-Types/Strings/#String___toLower "Documentation for String.toLower") = "orange"`
  * `"ABc123".[toLower](Basic-Types/Strings/#String___toLower "Documentation for String.toLower") = "abc123"`


###  20.8.4.10. Legacy Iterators[🔗](find/?domain=Verso.Genre.Manual.section&name=string-iterators "Permalink")
For backwards compatibility, Lean includes legacy string iterators. Fundamentally, a `[String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")` is a pair of a string and a valid position in the string. Iterators provide functions for getting the current character (`[curr](Basic-Types/Strings/#String___Legacy___Iterator___curr "Documentation for String.Legacy.Iterator.curr")`), replacing the current character (`[setCurr](Basic-Types/Strings/#String___Legacy___Iterator___setCurr "Documentation for String.Legacy.Iterator.setCurr")`), checking whether the iterator can move to the left or the right (`[hasPrev](Basic-Types/Strings/#String___Legacy___Iterator___hasPrev "Documentation for String.Legacy.Iterator.hasPrev")` and `[hasNext](Basic-Types/Strings/#String___Legacy___Iterator___hasNext "Documentation for String.Legacy.Iterator.hasNext")`, respectively), and moving the iterator (`[prev](Basic-Types/Strings/#String___Legacy___Iterator___prev "Documentation for String.Legacy.Iterator.prev")` and `[next](Basic-Types/Strings/#String___Legacy___Iterator___next "Documentation for String.Legacy.Iterator.next")`, respectively). Clients are responsible for checking whether they've reached the beginning or end of the string; otherwise, the iterator ensures that its position always points at a character. However, `[String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")` does not include proofs of these well-formedness conditions, which can make it more difficult to use in verified code.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.mk "Permalink")structure
```


String.Legacy.Iterator : Type


String.Legacy.Iterator : Type


```

An iterator over the characters (Unicode code points) in a `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`. Typically created by `String.iter`.
This is a no-longer-supported legacy API that will be removed in a future release. You should use `[String.Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")` instead, which is similar, but safer. To iterate over a string `s`, start with `p : s.startPos`, advance it using `p.next`, access the current character using `p.get` and check if the position is at the end using `p = s.endPos` or `p.IsAtEnd`.
String iterators pair a string with a valid byte index. This allows efficient character-by-character processing of strings while avoiding the need to manually ensure that byte indices are used with the correct strings.
An iterator is _valid_ if the position `i` is _valid_ for the string `s`, meaning `0 ≤ i ≤ s.rawEndPos` and `i` lies on a UTF8 byte boundary. If `i = s.rawEndPos`, the iterator is at the end of the string.
Most operations on iterators return unspecified values if the iterator is not valid. The functions in the `String.Iterator` API rule out the creation of invalid iterators, with two exceptions:
  * `Iterator.next iter` is invalid if `iter` is already at the end of the string (`iter.atEnd` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), and
  * `Iterator.forward iter n`/`Iterator.nextn iter n` is invalid if `n` is strictly greater than the number of remaining characters.


#  Constructor

```
[String.Legacy.Iterator.mk](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator.mk")
```

#  Fields

```
s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

The string being iterated over.

```
i : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")
```

The current UTF-8 byte position in the string `s`.
This position is not guaranteed to be valid for the string. If the position is not valid, then the current character is `([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))`, similar to `String.get` on an invalid position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.iter "Permalink")def
```


String.Legacy.iter (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


String.Legacy.iter (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


```

Creates an iterator at the beginning of the string.
This is a no-longer-supported legacy API that will be removed in a future release. You should use `[String.Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")` instead, which is similar, but safer. To iterate over a string `s`, start with `p : s.startPos`, advance it using `p.next`, access the current character using `p.get` and check if the position is at the end using `p = s.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")` or `p.IsAtEnd`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.mkIterator "Permalink")def
```


String.Legacy.mkIterator (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


String.Legacy.mkIterator (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


```

Creates an iterator at the beginning of the string.
This is a no-longer-supported legacy API that will be removed in a future release. You should use `[String.Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")` instead, which is similar, but safer. To iterate over a string `s`, start with `p : s.startPos`, advance it using `p.next`, access the current character using `p.get` and check if the position is at the end using `p = s.[endPos](Basic-Types/Strings/#String___endPos "Documentation for String.endPos")` or `p.IsAtEnd`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.curr "Permalink")def
```


String.Legacy.Iterator.curr : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.Legacy.Iterator.curr :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Gets the character at the iterator's current position.
This is a no-longer-supported legacy API that will be removed in a future release. You should use `[String.Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")` instead, which is similar, but safer. To iterate over a string `s`, start with `p : s.startPos`, advance it using `p.next`, access the current character using `p.get` and check if the position is at the end using `p = s.endPos` or `p.IsAtEnd`.
A run-time bounds check is performed. Use `String.Iterator.curr'` to avoid redundant bounds checks.
If the position is invalid, returns `([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.curr' "Permalink")def
```


String.Legacy.Iterator.curr' (it : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator"))
  (h : it.[hasNext](Basic-Types/Strings/#String___Legacy___Iterator___hasNext "Documentation for String.Legacy.Iterator.hasNext") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.Legacy.Iterator.curr'
  (it : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator"))
  (h : it.[hasNext](Basic-Types/Strings/#String___Legacy___Iterator___hasNext "Documentation for String.Legacy.Iterator.hasNext") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Gets the character at the iterator's current position.
The proof of `it.[hasNext](Basic-Types/Strings/#String___Legacy___Iterator___hasNext "Documentation for String.Legacy.Iterator.hasNext")` ensures that there is, in fact, a character at the current position. This function is faster that `String.Iterator.curr` due to avoiding a run-time bounds check.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.hasNext "Permalink")def
```


String.Legacy.Iterator.hasNext : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.Legacy.Iterator.hasNext :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the iterator is at or before the string's last character.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.next "Permalink")def
```


String.Legacy.Iterator.next :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


String.Legacy.Iterator.next :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") →
    [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


```

Moves the iterator's position forward by one character, unconditionally.
This is a no-longer-supported legacy API that will be removed in a future release. You should use `[String.Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")` instead, which is similar, but safer. To iterate over a string `s`, start with `p : s.startPos`, advance it using `p.next`, access the current character using `p.get` and check if the position is at the end using `p = s.endPos` or `p.IsAtEnd`.
It is only valid to call this function if the iterator is not at the end of the string (i.e. if `Iterator.atEnd` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`); otherwise, the resulting iterator will be invalid.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.next' "Permalink")def
```


String.Legacy.Iterator.next' (it : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator"))
  (h : it.[hasNext](Basic-Types/Strings/#String___Legacy___Iterator___hasNext "Documentation for String.Legacy.Iterator.hasNext") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


String.Legacy.Iterator.next'
  (it : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator"))
  (h : it.[hasNext](Basic-Types/Strings/#String___Legacy___Iterator___hasNext "Documentation for String.Legacy.Iterator.hasNext") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


```

Moves the iterator's position forward by one character, unconditionally.
The proof of `it.[hasNext](Basic-Types/Strings/#String___Legacy___Iterator___hasNext "Documentation for String.Legacy.Iterator.hasNext")` ensures that there is, in fact, a position that's one character forwards. This function is faster that `String.Iterator.next` due to avoiding a run-time bounds check.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.forward "Permalink")def
```


String.Legacy.Iterator.forward :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


String.Legacy.Iterator.forward :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") →
    [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


```

Moves the iterator's position forward by the specified number of characters.
The resulting iterator is only valid if the number of characters to skip is less than or equal to the number of characters left in the iterator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.nextn "Permalink")def
```


String.Legacy.Iterator.nextn :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


String.Legacy.Iterator.nextn :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") →
    [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


```

Moves the iterator's position forward by the specified number of characters.
The resulting iterator is only valid if the number of characters to skip is less than or equal to the number of characters left in the iterator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.hasPrev "Permalink")def
```


String.Legacy.Iterator.hasPrev : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.Legacy.Iterator.hasPrev :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the iterator is after the beginning of the string.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.prev "Permalink")def
```


String.Legacy.Iterator.prev :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


String.Legacy.Iterator.prev :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") →
    [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


```

Moves the iterator's position backward by one character, unconditionally.
The position is not changed if the iterator is at the beginning of the string.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.prevn "Permalink")def
```


String.Legacy.Iterator.prevn :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


String.Legacy.Iterator.prevn :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") →
    [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


```

Moves the iterator's position back by the specified number of characters, stopping at the beginning of the string.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.atEnd "Permalink")def
```


String.Legacy.Iterator.atEnd : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.Legacy.Iterator.atEnd :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the iterator is past its string's last character.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.toEnd "Permalink")def
```


String.Legacy.Iterator.toEnd :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


String.Legacy.Iterator.toEnd :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") →
    [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


```

Moves the iterator's position to the end of the string, just past the last character.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.setCurr "Permalink")def
```


String.Legacy.Iterator.setCurr :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


String.Legacy.Iterator.setCurr :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") →
    [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


```

Replaces the current character in the string.
Does nothing if the iterator is at the end of the string. If both the replacement character and the replaced character are 7-bit ASCII characters and the string is not shared, then it is updated in-place and not copied.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.find "Permalink")def
```


String.Legacy.Iterator.find (it : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator"))
  (p : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


String.Legacy.Iterator.find
  (it : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator"))
  (p : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


```

Moves the iterator forward until the Boolean predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for the iterator's current character or until the end of the string is reached. Does nothing if the current character already satisfies `p`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.foldUntil "Permalink")def
```


String.Legacy.Iterator.foldUntil.{u_1} {α : Type u_1}
  (it : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")) (init : α) (f : α → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) :
  α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


String.Legacy.Iterator.foldUntil.{u_1}
  {α : Type u_1}
  (it : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")) (init : α)
  (f : α → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) :
  α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


```

Iterates over a string, updating a state at each character using the provided function `f`, until `f` returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`. Begins with the state `init`. Returns the state and character for which `f` returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.extract "Permalink")def
```


String.Legacy.Iterator.extract :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.Legacy.Iterator.extract :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") →
    [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Extracts the substring between the positions of two iterators. The first iterator's position is the start of the substring, and the second iterator's position is the end.
Returns the empty string if the iterators are for different strings, or if the position of the first iterator is past the position of the second iterator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.remainingToString "Permalink")def
```


String.Legacy.Iterator.remainingToString :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.Legacy.Iterator.remainingToString :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

The remaining characters in an iterator, as a string.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.remainingBytes "Permalink")def
```


String.Legacy.Iterator.remainingBytes : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


String.Legacy.Iterator.remainingBytes :
  [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of UTF-8 bytes remaining in the iterator.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.pos "Permalink")def
```


String.Legacy.Iterator.pos (self : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")) :
  [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


String.Legacy.Iterator.pos
  (self : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")) :
  [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

The current UTF-8 byte position in the string `s`.
This position is not guaranteed to be valid for the string. If the position is not valid, then the current character is `([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))`, similar to `String.get` on an invalid position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Legacy.Iterator.toString "Permalink")def
```


String.Legacy.Iterator.toString (self : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.Legacy.Iterator.toString
  (self : [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

The string being iterated over.
###  20.8.4.11. String Slices[🔗](find/?domain=Verso.Genre.Manual.section&name=string-api-slice "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.mk "Permalink")structure
```


String.Slice : Type


String.Slice : Type


```

A region or slice of some underlying string.
A slice consists of a string together with the start and end byte positions of a region of interest. Actually extracting a substring requires copying and memory allocation, while many slices of the same underlying string may exist with very little overhead. While this could be achieved by tracking the bounds by hand, the slice API is much more convenient.
`[String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")` bundles proofs to ensure that the start and end positions always delineate a valid string. For this reason, it should be preferred over `[Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")`.
#  Constructor

```
[String.Slice.mk](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice.mk")
```

#  Fields

```
str : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

The underlying strings.

```
startInclusive : self.[str](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice.str").[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")
```

The byte position of the start of the string slice.

```
endExclusive : self.[str](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice.str").[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")
```

The byte position of the end of the string slice.

```
startInclusive_le_endExclusive : self.[startInclusive](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice.startInclusive") [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") self.[endExclusive](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice.endExclusive")
```

The slice is not degenerate (but it may be empty).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.toSlice "Permalink")def
```


String.toSlice (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.toSlice (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Returns a slice that contains the entire string.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.sliceFrom "Permalink")def
```


String.sliceFrom (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (p : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.sliceFrom (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (p : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

The slice from `p` (inclusive) up to the end of `s`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.sliceTo "Permalink")def
```


String.sliceTo (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (p : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.sliceTo (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (p : s.[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")) :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

The slice from the beginning of `s` up to `p` (exclusive).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pos.offset "Permalink")structure
```


String.Slice.Pos (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : Type


String.Slice.Pos (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : Type


```

A `Slice.Pos s` is a byte offset in `s` together with a proof that this position is at a UTF-8 character boundary.
#  Constructor

```
[String.Slice.Pos.mk](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos.mk")
```

#  Fields

```
offset : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")
```

The underlying byte offset of the `Slice.Pos`.

```
isValidForSlice : String.Pos.Raw.IsValidForSlice s self.[offset](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos.offset")
```

The proof that `offset` is valid for the string slice `s`.
####  20.8.4.11.1. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--String-Slices--API-Reference "Permalink")
#####  20.8.4.11.1.1. Copying[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--String-Slices--API-Reference--Copying "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.copy "Permalink")def
```


String.Slice.copy (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.Slice.copy (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Creates a `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` from a `[String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")` by copying the bytes.
#####  20.8.4.11.1.2. Size[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--String-Slices--API-Reference--Size "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.isEmpty "Permalink")def
```


String.Slice.isEmpty (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.Slice.isEmpty (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a slice is empty.
Empty slices have {name}`utf8ByteSize` {lean}`0`.
Examples:
  * {lean}`"".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[isEmpty](Basic-Types/Strings/#String___Slice___isEmpty "Documentation for String.Slice.isEmpty") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * {lean}`" ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[isEmpty](Basic-Types/Strings/#String___Slice___isEmpty "Documentation for String.Slice.isEmpty") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.utf8ByteSize "Permalink")def
```


String.Slice.utf8ByteSize (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


String.Slice.utf8ByteSize
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of bytes of the UTF-8 encoding of the string slice.
#####  20.8.4.11.1.3. Boundaries[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--String-Slices--API-Reference--Boundaries "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.pos "Permalink")def
```


String.Slice.pos (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (off : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (h : String.Pos.Raw.IsValidForSlice s off) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.pos (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice"))
  (off : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (h :
    String.Pos.Raw.IsValidForSlice s
      off) :
  s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Constructs a valid position on `s` from a position and a proof that it is valid.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.pos! "Permalink")def
```


String.Slice.pos! (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (off : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.pos! (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice"))
  (off : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Constructs a valid position `s` from a position, panicking if the position is not valid.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.pos? "Permalink")def
```


String.Slice.pos? (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (off : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.pos? (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice"))
  (off : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Constructs a valid position on `s` from a position, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the position is not valid.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.startPos "Permalink")def
```


String.Slice.startPos (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.startPos (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

The start position of `s`, as an `s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.endPos "Permalink")def
```


String.Slice.endPos (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.endPos (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

The past-the-end position of `s`, as an `s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.rawEndPos "Permalink")def
```


String.Slice.rawEndPos (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


String.Slice.rawEndPos
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

The end position of a slice, as a `Pos.Raw`.
######  20.8.4.11.1.3.1. Adjustment[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--String-Slices--API-Reference--Boundaries--Adjustment "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.sliceFrom "Permalink")def
```


String.Slice.sliceFrom (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.sliceFrom (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice"))
  (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Given a slice and a valid position within the slice, obtain a new slice on the same underlying string by replacing the start of the slice with the given position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.sliceTo "Permalink")def
```


String.Slice.sliceTo (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.sliceTo (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice"))
  (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Given a slice and a valid position within the slice, obtain a new slice on the same underlying string by replacing the end of the slice with the given position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.slice "Permalink")def
```


String.Slice.slice (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (newStart newEnd : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos"))
  (h : newStart [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") newEnd) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.slice (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice"))
  (newStart newEnd : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos"))
  (h : newStart [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") newEnd) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Given a slice and two valid positions within the slice, obtain a new slice on the same underlying string formed by the new bounds.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.slice! "Permalink")def
```


String.Slice.slice! (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (newStart newEnd : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.slice! (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice"))
  (newStart newEnd : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Given a slice and two valid positions within the slice, obtain a new slice on the same underlying string formed by the new bounds, or panic if the given end is strictly less than the given start.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.drop "Permalink")def
```


String.Slice.drop (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.drop (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice"))
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Removes the specified number of characters (Unicode code points) from the start of the slice.
If `n` is greater than the amount of characters in `s`, returns an empty slice.
Examples:
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[drop](Basic-Types/Strings/#String___Slice___drop "Documentation for String.Slice.drop") 4 == "green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[drop](Basic-Types/Strings/#String___Slice___drop "Documentation for String.Slice.drop") 10 == "blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[drop](Basic-Types/Strings/#String___Slice___drop "Documentation for String.Slice.drop") 50 == "".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.dropEnd "Permalink")def
```


String.Slice.dropEnd (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.dropEnd (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice"))
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Removes the specified number of characters (Unicode code points) from the end of the slice.
If `n` is greater than the amount of characters in `s`, returns an empty slice.
Examples:
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropEnd](Basic-Types/Strings/#String___Slice___dropEnd "Documentation for String.Slice.dropEnd") 5 == "red green".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropEnd](Basic-Types/Strings/#String___Slice___dropEnd "Documentation for String.Slice.dropEnd") 11 == "red".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropEnd](Basic-Types/Strings/#String___Slice___dropEnd "Documentation for String.Slice.dropEnd") 50 == "".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.dropEndWhile "Permalink")def
```


String.Slice.dropEndWhile {ρ : Type} (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern") pat] : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.dropEndWhile {ρ : Type}
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern")
      pat] :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Creates a new slice that contains the longest suffix of `s` for which `pat` matched (potentially repeatedly).
Examples:
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropEndWhile](Basic-Types/Strings/#String___Slice___dropEndWhile "Documentation for String.Slice.dropEndWhile") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") == "red green ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropEndWhile](Basic-Types/Strings/#String___Slice___dropEndWhile "Documentation for String.Slice.dropEndWhile") 'e' == "red green blu".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropEndWhile](Basic-Types/Strings/#String___Slice___dropEndWhile "Documentation for String.Slice.dropEndWhile") (fun (_ : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) == "".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.dropPrefix "Permalink")def
```


String.Slice.dropPrefix {ρ : Type} (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern") pat] : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.dropPrefix {ρ : Type}
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern")
      pat] :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

If `pat` matches a prefix of `s`, returns the remainder. Returns `s` unmodified otherwise.
Use `[String.Slice.dropPrefix?](Basic-Types/Strings/#String___Slice___dropPrefix___ "Documentation for String.Slice.dropPrefix?")` to return `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` when `pat` does not match a prefix.
This function is generic over all currently supported patterns.
Examples:
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropPrefix](Basic-Types/Strings/#String___Slice___dropPrefix "Documentation for String.Slice.dropPrefix") "red " == "green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropPrefix](Basic-Types/Strings/#String___Slice___dropPrefix "Documentation for String.Slice.dropPrefix") "reed " == "red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropPrefix](Basic-Types/Strings/#String___Slice___dropPrefix "Documentation for String.Slice.dropPrefix") 'r' == "ed green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropPrefix](Basic-Types/Strings/#String___Slice___dropPrefix "Documentation for String.Slice.dropPrefix") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") == "ed green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.dropPrefix? "Permalink")def
```


String.Slice.dropPrefix? {ρ : Type} (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern") pat] : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.dropPrefix? {ρ : Type}
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern")
      pat] :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

If `pat` matches a prefix of `s`, returns the remainder. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` otherwise.
Use `[String.Slice.dropPrefix](Basic-Types/Strings/#String___Slice___dropPrefix "Documentation for String.Slice.dropPrefix")` to return the slice unchanged when `pat` does not match a prefix.
This function is generic over all currently supported patterns.
Examples:
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropPrefix?](Basic-Types/Strings/#String___Slice___dropPrefix___ "Documentation for String.Slice.dropPrefix?") "red " == [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropPrefix?](Basic-Types/Strings/#String___Slice___dropPrefix___ "Documentation for String.Slice.dropPrefix?") "reed " == [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropPrefix?](Basic-Types/Strings/#String___Slice___dropPrefix___ "Documentation for String.Slice.dropPrefix?") 'r' == [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "ed green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropPrefix?](Basic-Types/Strings/#String___Slice___dropPrefix___ "Documentation for String.Slice.dropPrefix?") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") == [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "ed green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.dropSuffix "Permalink")def
```


String.Slice.dropSuffix {ρ : Type} (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern") pat] : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.dropSuffix {ρ : Type}
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern")
      pat] :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

If `pat` matches a suffix of `s`, returns the remainder. Returns `s` unmodified otherwise.
Use `[String.Slice.dropSuffix?](Basic-Types/Strings/#String___Slice___dropSuffix___ "Documentation for String.Slice.dropSuffix?")` to return `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` when `pat` does not match a prefix.
This function is generic over all currently supported patterns.
Examples:
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropSuffix](Basic-Types/Strings/#String___Slice___dropSuffix "Documentation for String.Slice.dropSuffix") " blue" == "red green".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropSuffix](Basic-Types/Strings/#String___Slice___dropSuffix "Documentation for String.Slice.dropSuffix") "bluu " == "red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropSuffix](Basic-Types/Strings/#String___Slice___dropSuffix "Documentation for String.Slice.dropSuffix") 'e' == "red green blu".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropSuffix](Basic-Types/Strings/#String___Slice___dropSuffix "Documentation for String.Slice.dropSuffix") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") == "red green blu".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.dropSuffix? "Permalink")def
```


String.Slice.dropSuffix? {ρ : Type} (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern") pat] : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.dropSuffix? {ρ : Type}
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern")
      pat] :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

If `pat` matches a suffix of `s`, returns the remainder. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` otherwise.
Use `[String.Slice.dropSuffix](Basic-Types/Strings/#String___Slice___dropSuffix "Documentation for String.Slice.dropSuffix")` to return the slice unchanged when `pat` does not match a prefix.
This function is generic over all currently supported patterns.
Examples:
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropSuffix?](Basic-Types/Strings/#String___Slice___dropSuffix___ "Documentation for String.Slice.dropSuffix?") " blue" == [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "red green".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropSuffix?](Basic-Types/Strings/#String___Slice___dropSuffix___ "Documentation for String.Slice.dropSuffix?") "bluu " == [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropSuffix?](Basic-Types/Strings/#String___Slice___dropSuffix___ "Documentation for String.Slice.dropSuffix?") 'e' == [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "red green blu".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropSuffix?](Basic-Types/Strings/#String___Slice___dropSuffix___ "Documentation for String.Slice.dropSuffix?") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") == [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") "red green blu".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.dropWhile "Permalink")def
```


String.Slice.dropWhile {ρ : Type} (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern") pat] : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.dropWhile {ρ : Type}
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern")
      pat] :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Creates a new slice that contains the longest prefix of `s` for which `pat` matched (potentially repeatedly).
Examples:
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropWhile](Basic-Types/Strings/#String___Slice___dropWhile "Documentation for String.Slice.dropWhile") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") == " green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropWhile](Basic-Types/Strings/#String___Slice___dropWhile "Documentation for String.Slice.dropWhile") 'r' == "ed green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropWhile](Basic-Types/Strings/#String___Slice___dropWhile "Documentation for String.Slice.dropWhile") "red " == "green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[dropWhile](Basic-Types/Strings/#String___Slice___dropWhile "Documentation for String.Slice.dropWhile") (fun (_ : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) == "".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.take "Permalink")def
```


String.Slice.take (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.take (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice"))
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Creates a new slice that contains the first `n` characters (Unicode code points) of `s`.
If `n` is greater than the amount of characters in `s`, returns `s`.
Examples:
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[take](Basic-Types/Strings/#String___Slice___take "Documentation for String.Slice.take") 3 == "red".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[take](Basic-Types/Strings/#String___Slice___take "Documentation for String.Slice.take") 1 == "r".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[take](Basic-Types/Strings/#String___Slice___take "Documentation for String.Slice.take") 0 == "".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[take](Basic-Types/Strings/#String___Slice___take "Documentation for String.Slice.take") 100 == "red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.takeEnd "Permalink")def
```


String.Slice.takeEnd (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.takeEnd (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice"))
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Creates a new slice that contains the last `n` characters (Unicode code points) of `s`.
If `n` is greater than the amount of characters in `s`, returns `s`.
Examples:
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[takeEnd](Basic-Types/Strings/#String___Slice___takeEnd "Documentation for String.Slice.takeEnd") 4 == "blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[takeEnd](Basic-Types/Strings/#String___Slice___takeEnd "Documentation for String.Slice.takeEnd") 1 == "e".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[takeEnd](Basic-Types/Strings/#String___Slice___takeEnd "Documentation for String.Slice.takeEnd") 0 == "".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[takeEnd](Basic-Types/Strings/#String___Slice___takeEnd "Documentation for String.Slice.takeEnd") 100 == "red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.takeEndWhile "Permalink")def
```


String.Slice.takeEndWhile {ρ : Type} (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern") pat] : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.takeEndWhile {ρ : Type}
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern")
      pat] :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Creates a new slice that contains the suffix prefix of `s` for which `pat` matched (potentially repeatedly).
This function is generic over all currently supported patterns.
Examples:
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[takeEndWhile](Basic-Types/Strings/#String___Slice___takeEndWhile "Documentation for String.Slice.takeEndWhile") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") == "blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[takeEndWhile](Basic-Types/Strings/#String___Slice___takeEndWhile "Documentation for String.Slice.takeEndWhile") 'e' == "e".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[takeEndWhile](Basic-Types/Strings/#String___Slice___takeEndWhile "Documentation for String.Slice.takeEndWhile") (fun (_ : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) == "red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.takeWhile "Permalink")def
```


String.Slice.takeWhile {ρ : Type} (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern") pat] : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.takeWhile {ρ : Type}
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern")
      pat] :
  [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Creates a new slice that contains the longest prefix of `s` for which `pat` matched (potentially repeatedly).
This function is generic over all currently supported patterns.
Examples:
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[takeWhile](Basic-Types/Strings/#String___Slice___takeWhile "Documentation for String.Slice.takeWhile") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") == "red".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[takeWhile](Basic-Types/Strings/#String___Slice___takeWhile "Documentation for String.Slice.takeWhile") 'r' == "r".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[takeWhile](Basic-Types/Strings/#String___Slice___takeWhile "Documentation for String.Slice.takeWhile") "red " == "red red ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[takeWhile](Basic-Types/Strings/#String___Slice___takeWhile "Documentation for String.Slice.takeWhile") (fun (_ : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) => [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) == "red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


#####  20.8.4.11.1.4. Characters[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--String-Slices--API-Reference--Characters "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.front "Permalink")def
```


String.Slice.front (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.Slice.front (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Returns the first character in `s`. If `s` is empty, returns `([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))`.
Examples:
  * `"abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[front](Basic-Types/Strings/#String___Slice___front "Documentation for String.Slice.front") = 'a'`
  * `"".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[front](Basic-Types/Strings/#String___Slice___front "Documentation for String.Slice.front") = ([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.front? "Permalink")def
```


String.Slice.front? (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.Slice.front? (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Returns the first character in `s`. If `s` is empty, returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
Examples:
  * `"abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[front?](Basic-Types/Strings/#String___Slice___front___ "Documentation for String.Slice.front?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 'a'`
  * `"".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[front?](Basic-Types/Strings/#String___Slice___front___ "Documentation for String.Slice.front?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.back "Permalink")def
```


String.Slice.back (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.Slice.back (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Returns the last character in `s`. If `s` is empty, returns `([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))`.
Examples:
  * `"abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[back](Basic-Types/Strings/#String___Slice___back "Documentation for String.Slice.back") = 'c'`
  * `"".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[back](Basic-Types/Strings/#String___Slice___back "Documentation for String.Slice.back") = ([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.back? "Permalink")def
```


String.Slice.back? (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.Slice.back? (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Returns the last character in `s`. If `s` is empty, returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
Examples:
  * `"abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[back?](Basic-Types/Strings/#String___Slice___back___ "Documentation for String.Slice.back?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 'c'`
  * `"".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[back?](Basic-Types/Strings/#String___Slice___back___ "Documentation for String.Slice.back?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


#####  20.8.4.11.1.5. Bytes[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--String-Slices--API-Reference--Bytes "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.getUTF8Byte "Permalink")def
```


String.Slice.getUTF8Byte (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (h : p [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") s.[rawEndPos](Basic-Types/Strings/#String___Slice___rawEndPos "Documentation for String.Slice.rawEndPos")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


String.Slice.getUTF8Byte
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (h : p [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") s.[rawEndPos](Basic-Types/Strings/#String___Slice___rawEndPos "Documentation for String.Slice.rawEndPos")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Accesses the indicated byte in the UTF-8 encoding of a string slice.
At runtime, this function is implemented by efficient, constant-time code.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.getUTF8Byte! "Permalink")def
```


String.Slice.getUTF8Byte! (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) :
  [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


String.Slice.getUTF8Byte!
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice"))
  (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Accesses the indicated byte in the UTF-8 encoding of the string slice, or panics if the position is out-of-bounds.
#####  20.8.4.11.1.6. Positions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--String-Slices--API-Reference--Positions "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.posGE "Permalink")def
```


String.Slice.posGE (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (offset : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (h : offset [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") s.[rawEndPos](Basic-Types/Strings/#String___Slice___rawEndPos "Documentation for String.Slice.rawEndPos")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.posGE (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice"))
  (offset : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (h : offset [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") s.[rawEndPos](Basic-Types/Strings/#String___Slice___rawEndPos "Documentation for String.Slice.rawEndPos")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Obtains the smallest valid position that is greater than or equal to the given byte position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.posGT "Permalink")def
```


String.Slice.posGT (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (offset : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (h : offset [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") s.[rawEndPos](Basic-Types/Strings/#String___Slice___rawEndPos "Documentation for String.Slice.rawEndPos")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.posGT (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice"))
  (offset : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (h : offset [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") s.[rawEndPos](Basic-Types/Strings/#String___Slice___rawEndPos "Documentation for String.Slice.rawEndPos")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Obtains the smallest valid position that is strictly greater than the given byte position.
#####  20.8.4.11.1.7. Searching[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--String-Slices--API-Reference--Searching "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=String.Slice.some%E2%86%AAString.Slice.contains "Permalink")def
```


String.Slice.contains {ρ : Type} {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") (String.Slice.Pattern.SearchStep s)]
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) → [Std.IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice"))
  (pat : ρ) [[String.Slice.Pattern.ToForwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToForwardSearcher___mk "Documentation for String.Slice.Pattern.ToForwardSearcher") pat σ] : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.Slice.contains {ρ : Type}
  {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")
        (String.Slice.Pattern.SearchStep
          s)]
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ToForwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToForwardSearcher___mk "Documentation for String.Slice.Pattern.ToForwardSearcher")
      pat σ] :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a slice has a match of the pattern `pat` anywhere.
This function is generic over all currently supported patterns.
Examples:
  * `"coffee tea water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[contains](Basic-Types/Strings/#String___Slice___contains "Documentation for String.Slice.contains") [Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"tea".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[contains](Basic-Types/Strings/#String___Slice___contains "Documentation for String.Slice.contains") (fun (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) => c == 'X') = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"coffee tea water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[contains](Basic-Types/Strings/#String___Slice___contains "Documentation for String.Slice.contains") "tea" = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.startsWith "Permalink")def
```


String.Slice.startsWith {ρ : Type} (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern") pat] : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.Slice.startsWith {ρ : Type}
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern")
      pat] :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the slice (`s`) begins with the pattern (`pat`).
This function is generic over all currently supported patterns.
Examples:
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[startsWith](Basic-Types/Strings/#String___Slice___startsWith "Documentation for String.Slice.startsWith") "red" = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[startsWith](Basic-Types/Strings/#String___Slice___startsWith "Documentation for String.Slice.startsWith") "green" = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[startsWith](Basic-Types/Strings/#String___Slice___startsWith "Documentation for String.Slice.startsWith") "" = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[startsWith](Basic-Types/Strings/#String___Slice___startsWith "Documentation for String.Slice.startsWith") 'r' = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[startsWith](Basic-Types/Strings/#String___Slice___startsWith "Documentation for String.Slice.startsWith") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.endsWith "Permalink")def
```


String.Slice.endsWith {ρ : Type} (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern") pat] : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.Slice.endsWith {ρ : Type}
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.BackwardPattern](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern")
      pat] :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the slice (`s`) ends with the pattern (`pat`).
This function is generic over all currently supported patterns.
Examples:
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[endsWith](Basic-Types/Strings/#String___Slice___endsWith "Documentation for String.Slice.endsWith") "blue" = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[endsWith](Basic-Types/Strings/#String___Slice___endsWith "Documentation for String.Slice.endsWith") "green" = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[endsWith](Basic-Types/Strings/#String___Slice___endsWith "Documentation for String.Slice.endsWith") "" = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[endsWith](Basic-Types/Strings/#String___Slice___endsWith "Documentation for String.Slice.endsWith") 'e' = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"red green blue".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[endsWith](Basic-Types/Strings/#String___Slice___endsWith "Documentation for String.Slice.endsWith") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.all "Permalink")def
```


String.Slice.all {ρ : Type} (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern") pat] : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.Slice.all {ρ : Type}
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ForwardPattern](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern")
      pat] :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a slice only consists of matches of the pattern `pat`.
Short-circuits at the first pattern mis-match.
This function is generic over all currently supported patterns.
Examples:
  * `"brown".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[all](Basic-Types/Strings/#String___Slice___all "Documentation for String.Slice.all") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"brown and orange".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[all](Basic-Types/Strings/#String___Slice___all "Documentation for String.Slice.all") [Char.isLower](Basic-Types/Characters/#Char___isLower "Documentation for Char.isLower") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"aaaaaa".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[all](Basic-Types/Strings/#String___Slice___all "Documentation for String.Slice.all") 'a' = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"aaaaaa".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[all](Basic-Types/Strings/#String___Slice___all "Documentation for String.Slice.all") "aa" = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"aaaaaaa".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[all](Basic-Types/Strings/#String___Slice___all "Documentation for String.Slice.all") "aa" = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.find? "Permalink")def
```


String.Slice.find? {ρ : Type} {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") (String.Slice.Pattern.SearchStep s)]
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) → [Std.IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice"))
  (pat : ρ) [[String.Slice.Pattern.ToForwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToForwardSearcher___mk "Documentation for String.Slice.Pattern.ToForwardSearcher") pat σ] :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.find? {ρ : Type}
  {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")
        (String.Slice.Pattern.SearchStep
          s)]
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ToForwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToForwardSearcher___mk "Documentation for String.Slice.Pattern.ToForwardSearcher")
      pat σ] :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Finds the position of the first match of the pattern `pat` in a slice `s`. If there is no match `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` is returned.
This function is generic over all currently supported patterns.
Examples:
  * `("coffee tea water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[find?](Basic-Types/Strings/#String___Slice___find___ "Documentation for String.Slice.find?") [Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace")).[map](Basic-Types/Optional-Values/#Option___map "Documentation for Option.map") (·.[get!](Basic-Types/Strings/#String___Slice___Pos___get___ "Documentation for String.Slice.Pos.get!")) == [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ' '`
  * `"tea".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[find?](Basic-Types/Strings/#String___Slice___find___ "Documentation for String.Slice.find?") (fun (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) => c == 'X') == [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `("coffee tea water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[find?](Basic-Types/Strings/#String___Slice___find___ "Documentation for String.Slice.find?") "tea").[map](Basic-Types/Optional-Values/#Option___map "Documentation for Option.map") (·.[get!](Basic-Types/Strings/#String___Slice___Pos___get___ "Documentation for String.Slice.Pos.get!")) == [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 't'`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.revFind? "Permalink")def
```


String.Slice.revFind? {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") (String.Slice.Pattern.SearchStep s)]
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) → [Std.IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")] {ρ : Type}
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ToBackwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToBackwardSearcher___mk "Documentation for String.Slice.Pattern.ToBackwardSearcher") pat σ] : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.revFind?
  {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")
        (String.Slice.Pattern.SearchStep
          s)]
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.IteratorLoop](Iterators/Iterator-Definitions/#Std___IteratorLoop___mk "Documentation for Std.IteratorLoop") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")]
  {ρ : Type} (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ToBackwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToBackwardSearcher___mk "Documentation for String.Slice.Pattern.ToBackwardSearcher")
      pat σ] :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Finds the position of the first match of the pattern `pat` in a slice, starting from the end of the slice and traversing towards the start. If there is no match `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` is returned.
This function is generic over all currently supported patterns except `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`/`[String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")`.
Examples:
  * `("coffee tea water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[revFind?](Basic-Types/Strings/#String___Slice___revFind___ "Documentation for String.Slice.revFind?") [Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace")).[map](Basic-Types/Optional-Values/#Option___map "Documentation for Option.map") (·.[get!](Basic-Types/Strings/#String___Slice___Pos___get___ "Documentation for String.Slice.Pos.get!")) == [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ' '`
  * `"tea".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[revFind?](Basic-Types/Strings/#String___Slice___revFind___ "Documentation for String.Slice.revFind?") (fun (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) => c == 'X') == [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


#####  20.8.4.11.1.8. Manipulation[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--String-Slices--API-Reference--Manipulation "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.split "Permalink")def
```


String.Slice.split {ρ : Type} {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") (String.Slice.Pattern.SearchStep s)]
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ToForwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToForwardSearcher___mk "Documentation for String.Slice.Pattern.ToForwardSearcher") pat σ] : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.split {ρ : Type}
  {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  [(s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) →
      [Std.Iterator](Iterators/Iterator-Definitions/#Std___Iterator___mk "Documentation for Std.Iterator") (σ s) [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id")
        (String.Slice.Pattern.SearchStep
          s)]
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ToForwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToForwardSearcher___mk "Documentation for String.Slice.Pattern.ToForwardSearcher")
      pat σ] :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Splits a slice at each subslice that matches the pattern `pat`.
The subslices that matched the pattern are not included in any of the resulting subslices. If multiple subslices in a row match the pattern, the resulting list will contain empty strings.
This function is generic over all currently supported patterns.
Examples:
  * `("coffee tea water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[split](Basic-Types/Strings/#String___Slice___split "Documentation for String.Slice.split") [Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace")).toStringList == ["coffee", "tea", "water"]`
  * `("coffee tea water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[split](Basic-Types/Strings/#String___Slice___split "Documentation for String.Slice.split") ' ').toStringList == ["coffee", "tea", "water"]`
  * `("coffee tea water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[split](Basic-Types/Strings/#String___Slice___split "Documentation for String.Slice.split") " tea ").toStringList == ["coffee", "water"]`
  * `("ababababa".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[split](Basic-Types/Strings/#String___Slice___split "Documentation for String.Slice.split") "aba").toStringList == ["coffee", "water"]`
  * `("baaab".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[split](Basic-Types/Strings/#String___Slice___split "Documentation for String.Slice.split") "aa").toStringList == ["b", "ab"]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.splitInclusive "Permalink")def
```


String.Slice.splitInclusive {ρ : Type} {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ToForwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToForwardSearcher___mk "Documentation for String.Slice.Pattern.ToForwardSearcher") pat σ] : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.splitInclusive {ρ : Type}
  {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type}
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ToForwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToForwardSearcher___mk "Documentation for String.Slice.Pattern.ToForwardSearcher")
      pat σ] :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Splits a slice at each subslice that matches the pattern `pat`. Unlike `[split](Tactic-Proofs/Tactic-Reference/#split "Documentation for tactic")` the matched subslices are included at the end of each subslice.
This function is generic over all currently supported patterns.
Examples:
  * `("coffee tea water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[splitInclusive](Basic-Types/Strings/#String___Slice___splitInclusive "Documentation for String.Slice.splitInclusive") [Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace")).[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList") == ["coffee ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice"), "tea ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice"), "water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")]`
  * `("coffee tea water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[splitInclusive](Basic-Types/Strings/#String___Slice___splitInclusive "Documentation for String.Slice.splitInclusive") ' ').[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList") == ["coffee ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice"), "tea ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice"), "water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")]`
  * `("coffee tea water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[splitInclusive](Basic-Types/Strings/#String___Slice___splitInclusive "Documentation for String.Slice.splitInclusive") " tea ").[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList") == ["coffee tea ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice"), "water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")]`
  * `("baaab".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[splitInclusive](Basic-Types/Strings/#String___Slice___splitInclusive "Documentation for String.Slice.splitInclusive") "aa").[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList") == ["baa".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice"), "ab".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.lines "Permalink")def
```


String.Slice.lines (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.lines (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Creates an iterator over all lines in `s` with the line ending characters `\r\n` or `\n` being stripped.
Examples:
  * `"foo\r\nbar\n\nbaz\n".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[lines](Basic-Types/Strings/#String___Slice___lines "Documentation for String.Slice.lines").[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList")  == ["foo".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice"), "bar".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice"), "".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice"), "baz".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")]`
  * `"foo\r\nbar\n\nbaz".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[lines](Basic-Types/Strings/#String___Slice___lines "Documentation for String.Slice.lines").[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList")  == ["foo".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice"), "bar".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice"), "".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice"), "baz".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")]`
  * `"foo\r\nbar\n\nbaz\r".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[lines](Basic-Types/Strings/#String___Slice___lines "Documentation for String.Slice.lines").[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList")  == ["foo".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice"), "bar".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice"), "".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice"), "baz\r".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.trimAscii "Permalink")def
```


String.Slice.trimAscii (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.trimAscii
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Removes leading and trailing whitespace from a slice.
“Whitespace” is defined as characters for which `[Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace")` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Examples:
  * `"abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[trimAscii](Basic-Types/Strings/#String___Slice___trimAscii "Documentation for String.Slice.trimAscii") == "abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"   abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[trimAscii](Basic-Types/Strings/#String___Slice___trimAscii "Documentation for String.Slice.trimAscii") == "abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"abc \t  ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[trimAscii](Basic-Types/Strings/#String___Slice___trimAscii "Documentation for String.Slice.trimAscii") == "abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"  abc   ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[trimAscii](Basic-Types/Strings/#String___Slice___trimAscii "Documentation for String.Slice.trimAscii") == "abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"abc\ndef\n".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[trimAscii](Basic-Types/Strings/#String___Slice___trimAscii "Documentation for String.Slice.trimAscii") == "abc\ndef".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.trimAsciiEnd "Permalink")def
```


String.Slice.trimAsciiEnd (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.trimAsciiEnd
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Removes trailing whitespace from a slice by moving its end position to the last non-whitespace character, or to its start position if there is no non-whitespace character.
“Whitespace” is defined as characters for which `[Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace")` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Examples:
  * `"abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[trimAsciiEnd](Basic-Types/Strings/#String___Slice___trimAsciiEnd "Documentation for String.Slice.trimAsciiEnd") == "abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"   abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[trimAsciiEnd](Basic-Types/Strings/#String___Slice___trimAsciiEnd "Documentation for String.Slice.trimAsciiEnd") == "   abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"abc \t  ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[trimAsciiEnd](Basic-Types/Strings/#String___Slice___trimAsciiEnd "Documentation for String.Slice.trimAsciiEnd") == "abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"  abc   ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[trimAsciiEnd](Basic-Types/Strings/#String___Slice___trimAsciiEnd "Documentation for String.Slice.trimAsciiEnd") == "  abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"abc\ndef\n".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[trimAsciiEnd](Basic-Types/Strings/#String___Slice___trimAsciiEnd "Documentation for String.Slice.trimAsciiEnd") == "abc\ndef".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.trimAsciiStart "Permalink")def
```


String.Slice.trimAsciiStart (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.trimAsciiStart
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Removes leading whitespace from a slice by moving its start position to the first non-whitespace character, or to its end position if there is no non-whitespace character.
“Whitespace” is defined as characters for which `[Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace")` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Examples:
  * `"abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[trimAsciiStart](Basic-Types/Strings/#String___Slice___trimAsciiStart "Documentation for String.Slice.trimAsciiStart") == "abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"   abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[trimAsciiStart](Basic-Types/Strings/#String___Slice___trimAsciiStart "Documentation for String.Slice.trimAsciiStart") == "abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"abc \t  ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[trimAsciiStart](Basic-Types/Strings/#String___Slice___trimAsciiStart "Documentation for String.Slice.trimAsciiStart") == "abc \t  ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"  abc   ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[trimAsciiStart](Basic-Types/Strings/#String___Slice___trimAsciiStart "Documentation for String.Slice.trimAsciiStart") == "abc   ".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`
  * `"abc\ndef\n".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[trimAsciiStart](Basic-Types/Strings/#String___Slice___trimAsciiStart "Documentation for String.Slice.trimAsciiStart") == "abc\ndef\n".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")`


#####  20.8.4.11.1.9. Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--String-Slices--API-Reference--Iteration "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.chars "Permalink")def
```


String.Slice.chars (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.Slice.chars (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Creates an iterator over all characters (Unicode code points) in `s`.
Examples:
  * `"abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[chars](Basic-Types/Strings/#String___Slice___chars "Documentation for String.Slice.chars").[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList") = ['a', 'b', 'c']`
  * `"ab∀c".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[chars](Basic-Types/Strings/#String___Slice___chars "Documentation for String.Slice.chars").[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList") = ['a', 'b', '∀', 'c']`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.revChars "Permalink")def
```


String.Slice.revChars (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.Slice.revChars (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Creates an iterator over all characters (Unicode code points) in `s`, starting from the end of the slice and iterating towards the start.
Example:
  * `"abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[revChars](Basic-Types/Strings/#String___Slice___revChars "Documentation for String.Slice.revChars").[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList") = ['c', 'b', 'a']`
  * `"ab∀c".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[revChars](Basic-Types/Strings/#String___Slice___revChars "Documentation for String.Slice.revChars").[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList") = ['c', '∀', 'b', 'a']`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.positions "Permalink")def
```


String.Slice.positions (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") p [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") p ≠ s.[endPos](Basic-Types/Strings/#String___Slice___endPos "Documentation for String.Slice.endPos") [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


String.Slice.positions
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") p [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") p ≠ s.[endPos](Basic-Types/Strings/#String___Slice___endPos "Documentation for String.Slice.endPos") [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


```

Creates an iterator over all valid positions within {name}`s`.
Examples:
  * {lean}`("abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[positions](Basic-Types/Strings/#String___Slice___positions "Documentation for String.Slice.positions").[map](Iterators/Iterator-Combinators/#Std___Iter___map "Documentation for Std.Iter.map") (fun ⟨p, h⟩ => p.[get](Basic-Types/Strings/#String___Slice___Pos___get "Documentation for String.Slice.Pos.get") h) |>.[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList")) = ['a', 'b', 'c']`
  * {lean}`("abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[positions](Basic-Types/Strings/#String___Slice___positions "Documentation for String.Slice.positions").[map](Iterators/Iterator-Combinators/#Std___Iter___map "Documentation for Std.Iter.map") (·.[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").[offset](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos.offset").[byteIdx](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw.byteIdx")) |>.[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList")) = [0, 1, 2]`
  * {lean}`("ab∀c".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[positions](Basic-Types/Strings/#String___Slice___positions "Documentation for String.Slice.positions").[map](Iterators/Iterator-Combinators/#Std___Iter___map "Documentation for Std.Iter.map") (fun ⟨p, h⟩ => p.[get](Basic-Types/Strings/#String___Slice___Pos___get "Documentation for String.Slice.Pos.get") h) |>.[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList")) = ['a', 'b', '∀', 'c']`
  * {lean}`("ab∀c".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[positions](Basic-Types/Strings/#String___Slice___positions "Documentation for String.Slice.positions").[map](Iterators/Iterator-Combinators/#Std___Iter___map "Documentation for Std.Iter.map") (·.[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").[offset](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos.offset").[byteIdx](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw.byteIdx")) |>.[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList")) = [0, 1, 2, 5]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.revPositions "Permalink")def
```


String.Slice.revPositions (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") p [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") p ≠ s.[endPos](Basic-Types/Strings/#String___Slice___endPos "Documentation for String.Slice.endPos") [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


String.Slice.revPositions
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [{](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") p [//](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype") p ≠ s.[endPos](Basic-Types/Strings/#String___Slice___endPos "Documentation for String.Slice.endPos") [}](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype")


```

Creates an iterator over all valid positions within {name}`s`, starting from the last valid position and iterating towards the first one.
Examples
  * {lean}`("abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[revPositions](Basic-Types/Strings/#String___Slice___revPositions "Documentation for String.Slice.revPositions").[map](Iterators/Iterator-Combinators/#Std___Iter___map "Documentation for Std.Iter.map") (fun ⟨p, h⟩ => p.[get](Basic-Types/Strings/#String___Slice___Pos___get "Documentation for String.Slice.Pos.get") h) |>.[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList")) = ['c', 'b', 'a']`
  * {lean}`("abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[revPositions](Basic-Types/Strings/#String___Slice___revPositions "Documentation for String.Slice.revPositions").[map](Iterators/Iterator-Combinators/#Std___Iter___map "Documentation for Std.Iter.map") (·.[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").[offset](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos.offset").[byteIdx](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw.byteIdx")) |>.[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList")) = [2, 1, 0]`
  * {lean}`("ab∀c".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[revPositions](Basic-Types/Strings/#String___Slice___revPositions "Documentation for String.Slice.revPositions").[map](Iterators/Iterator-Combinators/#Std___Iter___map "Documentation for Std.Iter.map") (fun ⟨p, h⟩ => p.[get](Basic-Types/Strings/#String___Slice___Pos___get "Documentation for String.Slice.Pos.get") h) |>.[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList")) = ['c', '∀', 'b', 'a']`
  * {lean}`("ab∀c".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[revPositions](Basic-Types/Strings/#String___Slice___revPositions "Documentation for String.Slice.revPositions").[map](Iterators/Iterator-Combinators/#Std___Iter___map "Documentation for Std.Iter.map") (·.[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").[offset](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos.offset").[byteIdx](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw.byteIdx")) |>.[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList")) = [5, 2, 1, 0]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.bytes "Permalink")def
```


String.Slice.bytes (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


String.Slice.bytes (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Creates an iterator over all bytes in {name}`s`.
Examples:
  * {lean}`"abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[bytes](Basic-Types/Strings/#String___Slice___bytes "Documentation for String.Slice.bytes").[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList") = [97, 98, 99]`
  * {lean}`"ab∀c".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[bytes](Basic-Types/Strings/#String___Slice___bytes "Documentation for String.Slice.bytes").[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList") = [97, 98, 226, 136, 128, 99]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.revBytes "Permalink")def
```


String.Slice.revBytes (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


String.Slice.revBytes (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Creates an iterator over all bytes in {name}`s`, starting from the last one and iterating towards the first one.
Examples:
  * {lean}`"abc".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[revBytes](Basic-Types/Strings/#String___Slice___revBytes "Documentation for String.Slice.revBytes").[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList") = [99, 98, 97]`
  * {lean}`"ab∀c".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[revBytes](Basic-Types/Strings/#String___Slice___revBytes "Documentation for String.Slice.revBytes").[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList") = [99, 128, 136, 226, 98, 97]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.revSplit "Permalink")def
```


String.Slice.revSplit {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type} {ρ : Type}
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ToBackwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToBackwardSearcher___mk "Documentation for String.Slice.Pattern.ToBackwardSearcher") pat σ] :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


String.Slice.revSplit
  {σ : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type} {ρ : Type}
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) (pat : ρ)
  [[String.Slice.Pattern.ToBackwardSearcher](Basic-Types/Strings/#String___Slice___Pattern___ToBackwardSearcher___mk "Documentation for String.Slice.Pattern.ToBackwardSearcher")
      pat σ] :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")


```

Splits a slice at each subslice that matches the pattern `pat`, starting from the end of the slice and traversing towards the start.
The subslices that matched the pattern are not included in any of the resulting subslices. If multiple subslices in a row match the pattern, the resulting list will contain empty slices.
This function is generic over all currently supported patterns except `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`/`[String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")`.
Examples:
  * `("coffee tea water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[revSplit](Basic-Types/Strings/#String___Slice___revSplit "Documentation for String.Slice.revSplit") [Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace")).[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList") == ["water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice"), "tea".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice"), "coffee".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")]`
  * `("coffee tea water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[revSplit](Basic-Types/Strings/#String___Slice___revSplit "Documentation for String.Slice.revSplit") ' ').[toList](Iterators/Consuming-Iterators/#Std___Iter___toList "Documentation for Std.Iter.toList") == ["water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice"), "tea".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice"), "coffee".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice")]`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.foldl "Permalink")def
```


String.Slice.foldl.{u} {α : Type u} (f : α → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → α) (init : α)
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : α


String.Slice.foldl.{u} {α : Type u}
  (f : α → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → α) (init : α)
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : α


```

Folds a function over a slice from the start, accumulating a value starting with `init`. The accumulated value is combined with each character in order, using `f`.
Examples:
  * `"coffee tea water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[foldl](Basic-Types/Strings/#String___Slice___foldl "Documentation for String.Slice.foldl") (fun n c => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") c.[isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace") [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n + 1 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n) 0 = 2`
  * `"coffee tea and water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[foldl](Basic-Types/Strings/#String___Slice___foldl "Documentation for String.Slice.foldl") (fun n c => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") c.[isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace") [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n + 1 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n) 0 = 3`
  * `"coffee tea water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[foldl](Basic-Types/Strings/#String___Slice___foldl "Documentation for String.Slice.foldl") (·.[push](Basic-Types/Strings/#String___push "Documentation for String.push") ·) "" = "coffee tea water"`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.foldr "Permalink")def
```


String.Slice.foldr.{u} {α : Type u} (f : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → α → α) (init : α)
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : α


String.Slice.foldr.{u} {α : Type u}
  (f : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → α → α) (init : α)
  (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : α


```

Folds a function over a slice from the end, accumulating a value starting with `init`. The accumulated value is combined with each character in reverse order, using `f`.
Examples:
  * `"coffee tea water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[foldr](Basic-Types/Strings/#String___Slice___foldr "Documentation for String.Slice.foldr") (fun c n => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") c.[isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace") [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n + 1 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n) 0 = 2`
  * `"coffee tea and water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[foldr](Basic-Types/Strings/#String___Slice___foldr "Documentation for String.Slice.foldr") (fun c n => [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") c.[isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace") [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n + 1 [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") n) 0 = 3`
  * `"coffee tea water".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[foldr](Basic-Types/Strings/#String___Slice___foldr "Documentation for String.Slice.foldr") (fun c s => s.[push](Basic-Types/Strings/#String___push "Documentation for String.push") c) "" = "retaw aet eeffoc"`


#####  20.8.4.11.1.10. Conversions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--String-Slices--API-Reference--Conversions "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.isNat "Permalink")def
```


String.Slice.isNat (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.Slice.isNat (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the slice can be interpreted as the decimal representation of a natural number.
A slice can be interpreted as a decimal natural number if it is not empty and all the characters in it are digits. Underscores (`_`) are allowed as digit separators for readability, but cannot appear at the start, at the end, or consecutively.
Use `toNat?` or `toNat!` to convert such a slice to a natural number.
Examples:
  * `"".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[isNat](Basic-Types/Strings/#String___Slice___isNat "Documentation for String.Slice.isNat") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"0".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[isNat](Basic-Types/Strings/#String___Slice___isNat "Documentation for String.Slice.isNat") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"5".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[isNat](Basic-Types/Strings/#String___Slice___isNat "Documentation for String.Slice.isNat") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"05".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[isNat](Basic-Types/Strings/#String___Slice___isNat "Documentation for String.Slice.isNat") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"587".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[isNat](Basic-Types/Strings/#String___Slice___isNat "Documentation for String.Slice.isNat") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"1_000".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[isNat](Basic-Types/Strings/#String___Slice___isNat "Documentation for String.Slice.isNat") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"100_000_000".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[isNat](Basic-Types/Strings/#String___Slice___isNat "Documentation for String.Slice.isNat") = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
  * `"-587".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[isNat](Basic-Types/Strings/#String___Slice___isNat "Documentation for String.Slice.isNat") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `" 5".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[isNat](Basic-Types/Strings/#String___Slice___isNat "Documentation for String.Slice.isNat") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"2+3".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[isNat](Basic-Types/Strings/#String___Slice___isNat "Documentation for String.Slice.isNat") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"0xff".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[isNat](Basic-Types/Strings/#String___Slice___isNat "Documentation for String.Slice.isNat") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"_123".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[isNat](Basic-Types/Strings/#String___Slice___isNat "Documentation for String.Slice.isNat") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"123_".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[isNat](Basic-Types/Strings/#String___Slice___isNat "Documentation for String.Slice.isNat") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
  * `"12__34".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[isNat](Basic-Types/Strings/#String___Slice___isNat "Documentation for String.Slice.isNat") = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.toNat! "Permalink")def
```


String.Slice.toNat! (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


String.Slice.toNat! (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Interprets a slice as the decimal representation of a natural number, returning it. Panics if the slice does not contain a decimal natural number.
A slice can be interpreted as a decimal natural number if it is not empty and all the characters in it are digits. Underscores (`_`) are allowed as digit separators and are ignored during parsing.
Use `isNat` to check whether `toNat!` would return a value. `toNat?` is a safer alternative that returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` instead of panicking when the string is not a natural number.
Examples:
  * `"0".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[toNat!](Basic-Types/Strings/#String___Slice___toNat___ "Documentation for String.Slice.toNat!") = 0`
  * `"5".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[toNat!](Basic-Types/Strings/#String___Slice___toNat___ "Documentation for String.Slice.toNat!") = 5`
  * `"587".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[toNat!](Basic-Types/Strings/#String___Slice___toNat___ "Documentation for String.Slice.toNat!") = 587`
  * `"1_000".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[toNat!](Basic-Types/Strings/#String___Slice___toNat___ "Documentation for String.Slice.toNat!") = 1000`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.toNat? "Permalink")def
```


String.Slice.toNat? (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


String.Slice.toNat? (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Interprets a slice as the decimal representation of a natural number, returning it. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the slice does not contain a decimal natural number.
A slice can be interpreted as a decimal natural number if it is not empty and all the characters in it are digits. Underscores (`_`) are allowed as digit separators and are ignored during parsing.
Use `isNat` to check whether `toNat?` would return `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")`. `toNat!` is an alternative that panics instead of returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` when the slice is not a natural number.
Examples:
  * `"".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[toNat?](Basic-Types/Strings/#String___Slice___toNat___-next "Documentation for String.Slice.toNat?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `"0".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[toNat?](Basic-Types/Strings/#String___Slice___toNat___-next "Documentation for String.Slice.toNat?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 0`
  * `"5".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[toNat?](Basic-Types/Strings/#String___Slice___toNat___-next "Documentation for String.Slice.toNat?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 5`
  * `"587".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[toNat?](Basic-Types/Strings/#String___Slice___toNat___-next "Documentation for String.Slice.toNat?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 587`
  * `"1_000".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[toNat?](Basic-Types/Strings/#String___Slice___toNat___-next "Documentation for String.Slice.toNat?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 1000`
  * `"100_000_000".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[toNat?](Basic-Types/Strings/#String___Slice___toNat___-next "Documentation for String.Slice.toNat?") = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") 100000000`
  * `"-587".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[toNat?](Basic-Types/Strings/#String___Slice___toNat___-next "Documentation for String.Slice.toNat?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `" 5".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[toNat?](Basic-Types/Strings/#String___Slice___toNat___-next "Documentation for String.Slice.toNat?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `"2+3".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[toNat?](Basic-Types/Strings/#String___Slice___toNat___-next "Documentation for String.Slice.toNat?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`
  * `"0xff".[toSlice](Basic-Types/Strings/#String___toSlice "Documentation for String.toSlice").[toNat?](Basic-Types/Strings/#String___Slice___toNat___-next "Documentation for String.Slice.toNat?") = [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`


#####  20.8.4.11.1.11. Equality[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--String-Slices--API-Reference--Equality "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.beq "Permalink")def
```


String.Slice.beq (s1 s2 : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.Slice.beq (s1 s2 : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether `s1` and `s2` represent the same string, even if they are slices of different base strings or different slices within the same string.
The implementation is an efficient equivalent of `s1.[copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy") == s2.[copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy")`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.eqIgnoreAsciiCase "Permalink")def
```


String.Slice.eqIgnoreAsciiCase (s1 s2 : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


String.Slice.eqIgnoreAsciiCase
  (s1 s2 : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether `s1 == s2` if ASCII upper/lowercase are ignored.
####  20.8.4.11.2. Patterns[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--String-Slices--Patterns "Permalink")
String slices feature generalized search patterns. Rather than being defined to work only for characters or for strings, many operations on slices accept arbitrary patterns. New types can be made into patterns by defining instances of the classes in this section. The Lean standard library provides instances that allow the following types to be used for both forward and backward searching:  
|  Pattern Type  |  Meaning  |  
| --- | --- |  
|  `[Char](Basic-Types/Characters/#Char___mk "Documentation for Char")`  |  Matches the provided character   |  
|  `[Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`  |  Matches any character that satisfies the predicate  |  
|  `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`  |  Matches occurrences of the given string  |  
|  `[String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")`  |  Matches occurrences of the string represented by the slice  |  
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pattern.ToForwardSearcher.toSearcher "Permalink")type class
```


String.Slice.Pattern.ToForwardSearcher {ρ : Type} (pat : ρ)
  (σ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") ([String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type)) : Type


String.Slice.Pattern.ToForwardSearcher
  {ρ : Type} (pat : ρ)
  (σ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") ([String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type)) :
  Type


```

Provides a conversion from a pattern to an iterator of `SearchStep` that searches for matches of the pattern from the start towards the end of a `Slice`.
While these operations can be implemented on top of `ForwardPattern`, some patterns allow for more efficient implementations. For example, a searcher for `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` patterns derived from the `ForwardPattern` instance on strings would try to match the pattern at every position in the string, but more efficient string matching routines are known. Indeed, the Lean standard library uses the Knuth-Morris-Pratt algorithm. See the module `Init.Data.String.Pattern.String` for the implementation.
This class can be used to provide such an efficient implementation. If there is no need to specialize in this fashion, then `ToForwardSearcher.defaultImplementation` can be used to automatically derive an instance.
#  Instance Constructor

```
[String.Slice.Pattern.ToForwardSearcher.mk](Basic-Types/Strings/#String___Slice___Pattern___ToForwardSearcher___mk "Documentation for String.Slice.Pattern.ToForwardSearcher.mk")
```

#  Methods

```
toSearcher : (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) → [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") (String.Slice.Pattern.SearchStep s)
```

Builds an iterator of `SearchStep` corresponding to matches of `pat` along the slice `s`. The `SearchStep`s returned by this iterator must contain ranges that are adjacent, non-overlapping and cover all of `s`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pattern.ForwardPattern.mk "Permalink")type class
```


String.Slice.Pattern.ForwardPattern {ρ : Type} (pat : ρ) : Type


String.Slice.Pattern.ForwardPattern
  {ρ : Type} (pat : ρ) : Type


```

Provides simple pattern matching capabilities from the start of a `Slice`.
#  Instance Constructor

```
[String.Slice.Pattern.ForwardPattern.mk](Basic-Types/Strings/#String___Slice___Pattern___ForwardPattern___mk "Documentation for String.Slice.Pattern.ForwardPattern.mk")
```

#  Methods

```
dropPrefix? : (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")
```

Checks whether the slice starts with the pattern. If it does, the slice is returned with the prefix removed; otherwise the result is `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.

```
dropPrefixOfNonempty? : (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) → s.[isEmpty](Basic-Types/Strings/#String___Slice___isEmpty "Documentation for String.Slice.isEmpty") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")
```

Checks whether the slice starts with the pattern. If it does, the slice is returned with the prefix removed; otherwise the result is `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.

```
startsWith : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

Checks whether the slice starts with the pattern.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pattern.ToBackwardSearcher.mk "Permalink")type class
```


String.Slice.Pattern.ToBackwardSearcher {ρ : Type} (pat : ρ)
  (σ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") ([String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type)) : Type


String.Slice.Pattern.ToBackwardSearcher
  {ρ : Type} (pat : ρ)
  (σ : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") ([String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → Type)) :
  Type


```

Provides a conversion from a pattern to an iterator of `SearchStep` searching for matches of the pattern from the end towards the start of a `Slice`.
While these operations can be implemented on top of `BackwardPattern`, some patterns allow for more efficient implementations. For example, a searcher for `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` patterns derived from the `BackwardPattern` instance on strings would try to match the pattern at every position in the string, but more efficient string matching routines are known. Indeed, the Lean standard library uses the Knuth-Morris-Pratt algorithm. See the module `Init.Data.String.Pattern.String` for the implementation.
This class can be used to provide such an efficient implementation. If there is no need to specialize in this fashion, then `ToBackwardSearcher.defaultImplementation` can be used to automatically derive an instance.
#  Instance Constructor

```
[String.Slice.Pattern.ToBackwardSearcher.mk](Basic-Types/Strings/#String___Slice___Pattern___ToBackwardSearcher___mk "Documentation for String.Slice.Pattern.ToBackwardSearcher.mk")
```

#  Methods

```
toSearcher : (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) → [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") (String.Slice.Pattern.SearchStep s)
```

Build an iterator of `SearchStep` corresponding to matches of `pat` along the slice `s`. The `SearchStep`s returned by this iterator must contain ranges that are adjacent, non-overlapping and cover all of `s`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pattern.BackwardPattern.mk "Permalink")type class
```


String.Slice.Pattern.BackwardPattern {ρ : Type} (pat : ρ) : Type


String.Slice.Pattern.BackwardPattern
  {ρ : Type} (pat : ρ) : Type


```

Provides simple pattern matching capabilities from the end of a `Slice`.
#  Instance Constructor

```
[String.Slice.Pattern.BackwardPattern.mk](Basic-Types/Strings/#String___Slice___Pattern___BackwardPattern___mk "Documentation for String.Slice.Pattern.BackwardPattern.mk")
```

#  Methods

```
dropSuffix? : (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")
```

Checks whether the slice ends with the pattern. If it does, the slice is returned with the suffix removed; otherwise the result is `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.

```
dropSuffixOfNonempty? : (s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")) → s.[isEmpty](Basic-Types/Strings/#String___Slice___isEmpty "Documentation for String.Slice.isEmpty") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")
```

Checks whether the slice ends with the pattern. If it does, the slice is returned with the suffix removed; otherwise the result is `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.

```
endsWith : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

Checks whether the slice ends with the pattern.
####  20.8.4.11.3. Positions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--String-Slices--Positions "Permalink")
#####  20.8.4.11.3.1. Lookups[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--String-Slices--Positions--Lookups "Permalink")
Because they retain a reference to the slice from which they were drawn, slice positions allow individual characters or bytes to be looked up.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pos.byte "Permalink")def
```


String.Slice.Pos.byte {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos"))
  (h : pos ≠ s.[endPos](Basic-Types/Strings/#String___Slice___endPos "Documentation for String.Slice.endPos")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


String.Slice.Pos.byte {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) (h : pos ≠ s.[endPos](Basic-Types/Strings/#String___Slice___endPos "Documentation for String.Slice.endPos")) :
  [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Returns the byte at a position in a slice that is not the end position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pos.get "Permalink")def
```


String.Slice.Pos.get {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos"))
  (h : pos ≠ s.[endPos](Basic-Types/Strings/#String___Slice___endPos "Documentation for String.Slice.endPos")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.Slice.Pos.get {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) (h : pos ≠ s.[endPos](Basic-Types/Strings/#String___Slice___endPos "Documentation for String.Slice.endPos")) :
  [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Obtains the character at the given position in the string.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pos.get! "Permalink")def
```


String.Slice.Pos.get! {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.Slice.Pos.get! {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Returns the byte at the given position in the string, or panics if the position is the end position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pos.get? "Permalink")def
```


String.Slice.Pos.get? {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


String.Slice.Pos.get? {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Returns the byte at the given position in the string, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the position is the end position.
#####  20.8.4.11.3.2. Incrementing and Decrementing[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--String-Slices--Positions--Incrementing-and-Decrementing "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pos.prev "Permalink")def
```


String.Slice.Pos.prev {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos"))
  (h : pos ≠ s.[startPos](Basic-Types/Strings/#String___Slice___startPos "Documentation for String.Slice.startPos")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.Pos.prev {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) (h : pos ≠ s.[startPos](Basic-Types/Strings/#String___Slice___startPos "Documentation for String.Slice.startPos")) :
  s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Returns the previous valid position before the given position, given a proof that the position is not the start position, which guarantees that such a position exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pos.prev! "Permalink")def
```


String.Slice.Pos.prev! {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.Pos.prev! {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Returns the previous valid position before the given position, or panics if the position is the start position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pos.prev? "Permalink")def
```


String.Slice.Pos.prev? {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.Pos.prev? {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Returns the previous valid position before the given position, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the position is the start position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pos.prevn "Permalink")def
```


String.Slice.Pos.prevn {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} (p : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.Pos.prevn {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")}
  (p : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Iterates `p.[prev](Basic-Types/Strings/#String___Slice___Pos___prev "Documentation for String.Slice.Pos.prev")` `n` times.
If this would move `p` past the start of `s`, the result is `s.[endPos](Basic-Types/Strings/#String___Slice___endPos "Documentation for String.Slice.endPos")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pos.next "Permalink")def
```


String.Slice.Pos.next {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos"))
  (h : pos ≠ s.[endPos](Basic-Types/Strings/#String___Slice___endPos "Documentation for String.Slice.endPos")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.Pos.next {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) (h : pos ≠ s.[endPos](Basic-Types/Strings/#String___Slice___endPos "Documentation for String.Slice.endPos")) :
  s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Advances a valid position on a slice to the next valid position, given a proof that the position is not the past-the-end position, which guarantees that such a position exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pos.next! "Permalink")def
```


String.Slice.Pos.next! {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.Pos.next! {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Advances a valid position on a slice to the next valid position, or panics if the given position is the past-the-end position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pos.next? "Permalink")def
```


String.Slice.Pos.next? {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.Pos.next? {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Advances a valid position on a slice to the next valid position, or returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the given position is the past-the-end position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pos.nextn "Permalink")def
```


String.Slice.Pos.nextn {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} (p : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.Pos.nextn {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")}
  (p : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Advances the position `p` `n` times.
If this would move `p` past the end of `s`, the result is `s.[endPos](Basic-Types/Strings/#String___Slice___endPos "Documentation for String.Slice.endPos")`.
#####  20.8.4.11.3.3. Other Strings or Slices[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--String-Slices--Positions--Other-Strings-or-Slices "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pos.cast "Permalink")def
```


String.Slice.Pos.cast {s t : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) (h : s [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t) :
  t.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.Pos.cast {s t : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) (h : s [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t) : t.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Constructs a valid position on `t` from a valid position on `s` and a proof that `s = t`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pos.ofSlice "Permalink")def
```


String.Slice.Pos.ofSlice {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} {p₀ p₁ : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")}
  {h : p₀ [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") p₁} (pos : (s.[slice](Basic-Types/Strings/#String___Slice___slice "Documentation for String.Slice.slice") p₀ p₁ h).[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.Pos.ofSlice
  {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} {p₀ p₁ : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")}
  {h : p₀ [≤](Type-Classes/Basic-Classes/#LE___mk "Documentation for LE.le") p₁}
  (pos : (s.[slice](Basic-Types/Strings/#String___Slice___slice "Documentation for String.Slice.slice") p₀ p₁ h).[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Given a position in `s.[slice](Basic-Types/Strings/#String___Slice___slice "Documentation for String.Slice.slice") p₀ p₁ h`, obtain the corresponding position in `s`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pos.str "Permalink")def
```


String.Slice.Pos.str {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : s.[str](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice.str").[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


String.Slice.Pos.str {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : s.[str](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice.str").[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


```

Given a valid position on a slice `s`, obtains the corresponding valid position on the underlying string `s.[str](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice.str")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pos.copy "Permalink")def
```


String.Slice.Pos.copy {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : s.[copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy").[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


String.Slice.Pos.copy {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")}
  (pos : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : s.[copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy").[Pos](Basic-Types/Strings/#String___Pos___mk "Documentation for String.Pos")


```

Given a slice `s` and a position on `s`, obtain the corresponding position on `s.[copy](Basic-Types/Strings/#String___Slice___copy "Documentation for String.Slice.copy").`
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pos.ofSliceFrom "Permalink")def
```


String.Slice.Pos.ofSliceFrom {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} {p₀ : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")}
  (pos : (s.[sliceFrom](Basic-Types/Strings/#String___Slice___sliceFrom "Documentation for String.Slice.sliceFrom") p₀).[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.Pos.ofSliceFrom
  {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} {p₀ : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")}
  (pos : (s.[sliceFrom](Basic-Types/Strings/#String___Slice___sliceFrom "Documentation for String.Slice.sliceFrom") p₀).[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Given a position in `s.[sliceFrom](Basic-Types/Strings/#String___Slice___sliceFrom "Documentation for String.Slice.sliceFrom") p₀`, obtain the corresponding position in `s`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.Slice.Pos.ofSliceTo "Permalink")def
```


String.Slice.Pos.ofSliceTo {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} {p₀ : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")}
  (pos : (s.[sliceTo](Basic-Types/Strings/#String___Slice___sliceTo "Documentation for String.Slice.sliceTo") p₀).[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


String.Slice.Pos.ofSliceTo
  {s : [String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")} {p₀ : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")}
  (pos : (s.[sliceTo](Basic-Types/Strings/#String___Slice___sliceTo "Documentation for String.Slice.sliceTo") p₀).[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")) : s.[Pos](Basic-Types/Strings/#String___Slice___Pos___mk "Documentation for String.Slice.Pos")


```

Given a position in `s.[sliceTo](Basic-Types/Strings/#String___Slice___sliceTo "Documentation for String.Slice.sliceTo") p₀`, obtain the corresponding position in `s`.
###  20.8.4.12. Raw Substrings[🔗](find/?domain=Verso.Genre.Manual.section&name=string-api-substring "Permalink")
Raw substrings are a low-level type that groups a string together with byte positions that delimit a region in the string. Most code should use [slices](Basic-Types/Strings/#string-api-slice) instead, because they are safer and more convenient.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.toRawSubstring "Permalink")def
```


String.toRawSubstring (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


String.toRawSubstring (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

Converts a `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` into a `Substring` that denotes the entire string.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.toRawSubstring' "Permalink")def
```


String.toRawSubstring' (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


String.toRawSubstring' (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

Converts a `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` into a `Substring` that denotes the entire string.
This is a version of `[String.toRawSubstring](Basic-Types/Strings/#String___toRawSubstring "Documentation for String.toRawSubstring")` that doesn't have an `@[inline]` annotation.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.mk "Permalink")structure
```


Substring.Raw : Type


Substring.Raw : Type


```

A region or slice of some underlying string.
A substring contains a string together with the start and end byte positions of a region of interest. Actually extracting a substring requires copying and memory allocation, while many substrings of the same underlying string may exist with very little overhead, and they are more convenient than tracking the bounds by hand.
Using its constructor explicitly, it is possible to construct a `Substring` in which one or both of the positions is invalid for the string. Many operations will return unexpected or confusing results if the start and stop positions are not valid. For this reason, `Substring` will be deprecated in favor of `[String.Slice](Basic-Types/Strings/#String___Slice___mk "Documentation for String.Slice")`, which always represents a valid substring.
#  Constructor

```
[Substring.Raw.mk](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw.mk")
```

#  Fields

```
str : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")
```

The underlying string.

```
startPos : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")
```

The byte position of the start of the string slice.

```
stopPos : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")
```

The byte position of the end of the string slice.
####  20.8.4.12.1. Properties[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Raw-Substrings--Properties "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.isEmpty "Permalink")def
```


Substring.Raw.isEmpty (ss : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Substring.Raw.isEmpty
  (ss : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a substring is empty.
A substring is empty if its start and end positions are the same.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.bsize "Permalink")def
```


Substring.Raw.bsize : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Substring.Raw.bsize : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of bytes used by the string's UTF-8 encoding.
####  20.8.4.12.2. Positions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Raw-Substrings--Positions "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.atEnd "Permalink")def
```


Substring.Raw.atEnd : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Substring.Raw.atEnd :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a position in a substring is precisely equal to its ending position.
The position is understood relative to the substring's starting position, rather than the underlying string's starting position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.posOf "Permalink")def
```


Substring.Raw.posOf (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


Substring.Raw.posOf (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw"))
  (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

Returns the substring-relative position of the first occurrence of `c` in `s`, or `s.[bsize](Basic-Types/Strings/#Substring___Raw___bsize "Documentation for Substring.Raw.bsize")` if `c` doesn't occur.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.next "Permalink")def
```


Substring.Raw.next : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


Substring.Raw.next :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") →
    [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

Returns the next position in a substring after the given position. If the position is at the end of the substring, it is returned unmodified.
Both the input position and the returned position are interpreted relative to the substring's start position, not the underlying string.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.nextn "Permalink")def
```


Substring.Raw.nextn :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


Substring.Raw.nextn :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") →
    [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

Returns the position that's the specified number of characters forward from the given position in a substring. If the end position of the substring is reached, it is returned.
Both the input position and the returned position are interpreted relative to the substring's start position, not the underlying string.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.prev "Permalink")def
```


Substring.Raw.prev : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


Substring.Raw.prev :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") →
    [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

Returns the previous position in a substring, just prior to the given position. If the position is at the beginning of the substring, it is returned unmodified.
Both the input position and the returned position are interpreted relative to the substring's start position, not the underlying string.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.prevn "Permalink")def
```


Substring.Raw.prevn :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


Substring.Raw.prevn :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") →
    [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw")


```

Returns the position that's the specified number of characters prior to the given position in a substring. If the start position of the substring is reached, it is returned.
Both the input position and the returned position are interpreted relative to the substring's start position, not the underlying string.
####  20.8.4.12.3. Folds and Aggregation[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Raw-Substrings--Folds-and-Aggregation "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.foldl "Permalink")def
```


Substring.Raw.foldl.{u} {α : Type u} (f : α → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → α) (init : α)
  (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : α


Substring.Raw.foldl.{u} {α : Type u}
  (f : α → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → α) (init : α)
  (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : α


```

Folds a function over a substring from the left, accumulating a value starting with `init`. The accumulated value is combined with each character in order, using `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.foldr "Permalink")def
```


Substring.Raw.foldr.{u} {α : Type u} (f : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → α → α) (init : α)
  (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : α


Substring.Raw.foldr.{u} {α : Type u}
  (f : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → α → α) (init : α)
  (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : α


```

Folds a function over a substring from the right, accumulating a value starting with `init`. The accumulated value is combined with each character in reverse order, using `f`.
[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=Substring.Raw.every%E2%86%AASubstring.Raw.all "Permalink")def
```


Substring.Raw.all (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) (p : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Substring.Raw.all (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw"))
  (p : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the Boolean predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for every character in a substring.
Short-circuits at the first character for which `p` returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
[🔗](find/?domain=Verso.Genre.Manual.doc.suggestion&name=Substring.Raw.some%E2%86%AASubstring.Raw.any "Permalink")def
```


Substring.Raw.any (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) (p : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Substring.Raw.any (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw"))
  (p : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the Boolean predicate `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for any character in a substring.
Short-circuits at the first character for which `p` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
####  20.8.4.12.4. Comparisons[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Raw-Substrings--Comparisons "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.beq "Permalink")def
```


Substring.Raw.beq (ss1 ss2 : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Substring.Raw.beq
  (ss1 ss2 : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether two substrings represent equal strings. Usually accessed via the `==` operator.
Two substrings do not need to have the same underlying string or the same start and end positions; instead, they are equal if they contain the same sequence of characters.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.sameAs "Permalink")def
```


Substring.Raw.sameAs (ss1 ss2 : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Substring.Raw.sameAs
  (ss1 ss2 : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether two substrings have the same position and content.
The two substrings do not need to have the same underlying string for this check to succeed.
####  20.8.4.12.5. Prefix and Suffix[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Raw-Substrings--Prefix-and-Suffix "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.commonPrefix "Permalink")def
```


Substring.Raw.commonPrefix (s t : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


Substring.Raw.commonPrefix
  (s t : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

Returns the longest common prefix of two substrings.
The returned substring uses the same underlying string as `s`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.commonSuffix "Permalink")def
```


Substring.Raw.commonSuffix (s t : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


Substring.Raw.commonSuffix
  (s t : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

Returns the longest common suffix of two substrings.
The returned substring uses the same underlying string as `s`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.dropPrefix? "Permalink")def
```


Substring.Raw.dropPrefix? (s pre : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


Substring.Raw.dropPrefix?
  (s pre : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

If `pre` is a prefix of `s`, returns the remainder. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` otherwise.
The substring `pre` is a prefix of `s` if there exists a `t : Substring` such that `s.[toString](Basic-Types/Strings/#Substring___Raw___toString "Documentation for Substring.Raw.toString") = pre.[toString](Basic-Types/Strings/#Substring___Raw___toString "Documentation for Substring.Raw.toString") ++ t.toString`. If so, the result is the substring of `s` without the prefix.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.dropSuffix? "Permalink")def
```


Substring.Raw.dropSuffix? (s suff : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


Substring.Raw.dropSuffix?
  (s suff : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

If `suff` is a suffix of `s`, returns the remainder. Returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` otherwise.
The substring `suff` is a suffix of `s` if there exists a `t : Substring` such that `s.[toString](Basic-Types/Strings/#Substring___Raw___toString "Documentation for Substring.Raw.toString") = t.toString ++ suff.[toString](Basic-Types/Strings/#Substring___Raw___toString "Documentation for Substring.Raw.toString")`. If so, the result the substring of `s` without the suffix.
####  20.8.4.12.6. Lookups[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Raw-Substrings--Lookups "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.get "Permalink")def
```


Substring.Raw.get : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


Substring.Raw.get :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Returns the character at the given position in the substring.
The position is relative to the substring, rather than the underlying string, and no bounds checking is performed with respect to the substring's end position. If the relative position is not a valid position in the underlying string, the fallback value `([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))`, which is `'A'`, is returned. Does not panic.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.contains "Permalink")def
```


Substring.Raw.contains (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Substring.Raw.contains (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw"))
  (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether a substring contains the specified character.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.front "Permalink")def
```


Substring.Raw.front (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


Substring.Raw.front (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) :
  [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Returns the first character in the substring.
If the substring is empty, but the substring's start position is a valid position in the underlying string, then the character at the start position is returned. If the substring's start position is not a valid position in the string, the fallback value `([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char"))`, which is `'A'`, is returned. Does not panic.
####  20.8.4.12.7. Modifications[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Raw-Substrings--Modifications "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.drop "Permalink")def
```


Substring.Raw.drop : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


Substring.Raw.drop :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

Removes the specified number of characters (Unicode code points) from the beginning of a substring by advancing its start position.
If the substring's end position is reached, the start position is not advanced past it.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.dropWhile "Permalink")def
```


Substring.Raw.dropWhile : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → ([Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


Substring.Raw.dropWhile :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") →
    ([Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

Removes the longest prefix of a substring in which a Boolean predicate returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for all characters by moving the substring's start position. The start position is moved to the position of the first character for which the predicate returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, or to the substring's end position if the predicate always returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.dropRight "Permalink")def
```


Substring.Raw.dropRight : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


Substring.Raw.dropRight :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

Removes the specified number of characters (Unicode code points) from the end of a substring by moving its end position towards its start position.
If the substring's start position is reached, the end position is not retracted past it.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.dropRightWhile "Permalink")def
```


Substring.Raw.dropRightWhile :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → ([Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


Substring.Raw.dropRightWhile :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") →
    ([Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

Removes the longest suffix of a substring in which a Boolean predicate returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for all characters by moving the substring's end position. The end position is moved just after the position of the last character for which the predicate returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, or to the substring's start position if the predicate always returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.take "Permalink")def
```


Substring.Raw.take : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


Substring.Raw.take :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

Retains only the specified number of characters (Unicode code points) at the beginning of a substring, by moving its end position towards its start position.
If the substring's start position is reached, the end position is not retracted past it.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.takeWhile "Permalink")def
```


Substring.Raw.takeWhile : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → ([Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


Substring.Raw.takeWhile :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") →
    ([Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

Retains only the longest prefix of a substring in which a Boolean predicate returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for all characters by moving the substring's end position towards its start position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.takeRight "Permalink")def
```


Substring.Raw.takeRight : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


Substring.Raw.takeRight :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

Retains only the specified number of characters (Unicode code points) at the end of a substring, by moving its start position towards its end position.
If the substring's end position is reached, the start position is not advanced past it.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.takeRightWhile "Permalink")def
```


Substring.Raw.takeRightWhile :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → ([Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


Substring.Raw.takeRightWhile :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") →
    ([Char](Basic-Types/Characters/#Char___mk "Documentation for Char") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

Retains only the longest suffix of a substring in which a Boolean predicate returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` for all characters by moving the substring's start position towards its end position.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.extract "Permalink")def
```


Substring.Raw.extract :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


Substring.Raw.extract :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") →
    [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") →
      [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw") → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

Returns the region of the substring delimited by the provided start and stop positions, as a substring. The positions are interpreted with respect to the substring's start position, rather than the underlying string.
If the resulting substring is empty, then the resulting substring is a substring of the empty string `""`. Otherwise, the underlying string is that of the input substring with the beginning and end positions adjusted.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.trim "Permalink")def
```


Substring.Raw.trim : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


Substring.Raw.trim :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

Removes leading and trailing whitespace from a substring by first moving its start position to the first non-whitespace character, and then moving its end position to the last non-whitespace character.
If the substring consists only of whitespace, then the resulting substring's start position is moved to its end position.
“Whitespace” is defined as characters for which `[Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace")` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Examples:
  * `" red green blue ".[toRawSubstring](Basic-Types/Strings/#String___toRawSubstring "Documentation for String.toRawSubstring").[trim](Basic-Types/Strings/#Substring___Raw___trim "Documentation for Substring.Raw.trim").[toString](Basic-Types/Strings/#Substring___Raw___toString "Documentation for Substring.Raw.toString") = "red green blue"`
  * `" red green blue ".[toRawSubstring](Basic-Types/Strings/#String___toRawSubstring "Documentation for String.toRawSubstring").[trim](Basic-Types/Strings/#Substring___Raw___trim "Documentation for Substring.Raw.trim").[startPos](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw.startPos") = ⟨1⟩`
  * `" red green blue ".[toRawSubstring](Basic-Types/Strings/#String___toRawSubstring "Documentation for String.toRawSubstring").[trim](Basic-Types/Strings/#Substring___Raw___trim "Documentation for Substring.Raw.trim").[stopPos](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw.stopPos") = ⟨15⟩`
  * `"     ".[toRawSubstring](Basic-Types/Strings/#String___toRawSubstring "Documentation for String.toRawSubstring").[trim](Basic-Types/Strings/#Substring___Raw___trim "Documentation for Substring.Raw.trim").[startPos](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw.startPos") = ⟨5⟩`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.trimLeft "Permalink")def
```


Substring.Raw.trimLeft (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


Substring.Raw.trimLeft
  (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

Removes leading whitespace from a substring by moving its start position to the first non-whitespace character, or to its end position if there is no non-whitespace character.
“Whitespace” is defined as characters for which `[Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace")` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.trimRight "Permalink")def
```


Substring.Raw.trimRight (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


Substring.Raw.trimRight
  (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

Removes trailing whitespace from a substring by moving its end position to the last non-whitespace character, or to its start position if there is no non-whitespace character.
“Whitespace” is defined as characters for which `[Char.isWhitespace](Basic-Types/Characters/#Char___isWhitespace "Documentation for Char.isWhitespace")` returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.splitOn "Permalink")def
```


Substring.Raw.splitOn (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) (sep : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := " ") :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


Substring.Raw.splitOn (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw"))
  (sep : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := " ") :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

Splits a substring `s` on occurrences of the separator string `sep`. The default separator is `" "`.
When `sep` is empty, the result is `[s]`. When `sep` occurs in overlapping patterns, the first match is taken. There will always be exactly `n+1` elements in the returned list if there were `n` non-overlapping matches of `sep` in the string. The separators are not included in the returned substrings, which are all substrings of `s`'s string.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.repair "Permalink")def
```


Substring.Raw.repair : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


Substring.Raw.repair :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")


```

Given a `Substring`, returns another one which has valid endpoints and represents the same substring according to `Substring.toString`. (Note, the substring may still be inverted, i.e. beginning greater than end.)
####  20.8.4.12.8. Conversions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Strings--API-Reference--Raw-Substrings--Conversions "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.toString "Permalink")def
```


Substring.Raw.toString : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


Substring.Raw.toString :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

{} Copies the region of the underlying string pointed to by a substring into a fresh string.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.isNat "Permalink")def
```


Substring.Raw.isNat (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Substring.Raw.isNat (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Checks whether the substring can be interpreted as the decimal representation of a natural number.
A substring can be interpreted as a decimal natural number if it is not empty and all the characters in it are digits. Underscores ({lit}`_`) are allowed as digit separators for readability, but cannot appear at the start, at the end, or consecutively.
Use `Substring.toNat?` to convert such a substring to a natural number.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.toNat? "Permalink")def
```


Substring.Raw.toNat? (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Substring.Raw.toNat? (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Checks whether the substring can be interpreted as the decimal representation of a natural number, returning the number if it can.
A substring can be interpreted as a decimal natural number if it is not empty and all the characters in it are digits. Underscores ({lit}`_`) are allowed as digit separators and are ignored during parsing.
Use `Substring.isNat` to check whether the substring is such a substring.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.toLegacyIterator "Permalink")def
```


Substring.Raw.toLegacyIterator : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


Substring.Raw.toLegacyIterator :
  [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw") → [String.Legacy.Iterator](Basic-Types/Strings/#String___Legacy___Iterator___mk "Documentation for String.Legacy.Iterator")


```

Returns an iterator into the underlying string, at the substring's starting position. The ending position is discarded, so the iterator alone cannot be used to determine whether its current position is within the original substring.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Substring.Raw.toName "Permalink")def
```


Substring.Raw.toName (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) : Lean.Name


Substring.Raw.toName (s : [Substring.Raw](Basic-Types/Strings/#Substring___Raw___mk "Documentation for Substring.Raw")) :
  Lean.Name


```

Converts a substring to the Lean compiler's representation of names. The resulting name is hierarchical, and the string is split at the dots (`'.'`).
`"a.b".[toRawSubstring](Basic-Types/Strings/#String___toRawSubstring "Documentation for String.toRawSubstring").[toName](Basic-Types/Strings/#Substring___Raw___toName "Documentation for Substring.Raw.toName")` is the name `a.b`, not `«a.b»`. For the latter, use `Name.mkSimple ∘ [Substring.Raw.toString](Basic-Types/Strings/#Substring___Raw___toString "Documentation for Substring.Raw.toString")`. -- TODO: deprecate old name
###  20.8.4.13. Metaprogramming[🔗](find/?domain=Verso.Genre.Manual.section&name=string-api-meta "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.toName "Permalink")def
```


String.toName (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : Lean.Name


String.toName (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : Lean.Name


```

Converts a string to the Lean compiler's representation of names. The resulting name is hierarchical, and the string is split at the dots (`'.'`).
`"a.b".[toName](Basic-Types/Strings/#String___toName "Documentation for String.toName")` is the name `a.b`, not `«a.b»`. For the latter, use `Name.mkSimple`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.quote "Permalink")def
```


String.quote (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.quote (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Converts a string to its corresponding Lean string literal syntax. Double quotes are added to each end, and internal characters are escaped as needed.
Examples:
  * `"abc".[quote](Basic-Types/Strings/#String___quote "Documentation for String.quote") = "\"abc\""`
  * `"\"".[quote](Basic-Types/Strings/#String___quote "Documentation for String.quote") = "\"\\\"\""`


###  20.8.4.14. Encodings[🔗](find/?domain=Verso.Genre.Manual.section&name=string-api-encoding "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.getUTF8Byte "Permalink")def
```


String.getUTF8Byte (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (h : p [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") s.[rawEndPos](Basic-Types/Strings/#String___rawEndPos "Documentation for String.rawEndPos")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


String.getUTF8Byte (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String"))
  (p : [String.Pos.Raw](Basic-Types/Strings/#String___Pos___Raw___mk "Documentation for String.Pos.Raw"))
  (h : p [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") s.[rawEndPos](Basic-Types/Strings/#String___rawEndPos "Documentation for String.rawEndPos")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Accesses the indicated byte in the UTF-8 encoding of a string.
At runtime, this function is implemented by efficient, constant-time code.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.utf8ByteSize "Permalink")def
```


String.utf8ByteSize (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


String.utf8ByteSize (s : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of bytes used by the string's UTF-8 encoding.
At runtime, this function takes constant time because the byte length of strings is cached.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.utf8EncodeChar "Permalink")def
```


String.utf8EncodeChar (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


String.utf8EncodeChar (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Returns the sequence of bytes in a character's UTF-8 encoding.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.fromUTF8 "Permalink")def
```


String.fromUTF8 (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) (h : a.IsValidUTF8) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.fromUTF8 (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray"))
  (h : a.IsValidUTF8) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Decodes an array of bytes that encode a string as [UTF-8](https://en.wikipedia.org/wiki/UTF-8) into the corresponding string.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.fromUTF8? "Permalink")def
```


String.fromUTF8? (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.fromUTF8? (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Decodes an array of bytes that encode a string as [UTF-8](https://en.wikipedia.org/wiki/UTF-8) into the corresponding string, or returns `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the array is not a valid UTF-8 encoding of a string.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.fromUTF8! "Permalink")def
```


String.fromUTF8! (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.fromUTF8! (a : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Decodes an array of bytes that encode a string as [UTF-8](https://en.wikipedia.org/wiki/UTF-8) into the corresponding string, or panics if the array is not a valid UTF-8 encoding of a string.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.toUTF8 "Permalink")def
```


String.toUTF8 (a : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


String.toUTF8 (a : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [ByteArray](Basic-Types/Byte-Arrays/#ByteArray___mk "Documentation for ByteArray")


```

Encodes a string in UTF-8 as an array of bytes.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=String.crlfToLf "Permalink")def
```


String.crlfToLf (text : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


String.crlfToLf (text : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Replaces each `\r\n` with `\n` to normalize line endings, but does not validate that there are no isolated `\r` characters.
This is an optimized version of `[String.replace](Basic-Types/Strings/#String___replace "Documentation for String.replace") text "\r\n" "\n"`.
##  20.8.5. FFI[🔗](find/?domain=Verso.Genre.Manual.section&name=string-ffi "Permalink")
FFI type
```

```
typedef struct {
    lean_object m_header;
    /* byte length including '\0' terminator */
    size_t      m_size;
    size_t      m_capacity;
    /* UTF8 length */
    size_t      m_length;
    char        m_data[0];
} lean_string_object;

```

```

The representation of strings in C. See [the description of run-time ``](Basic-Types/Strings/#string-runtime)`[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`s for more details.
FFI function
```

```
bool lean_is_string(lean_object * o)

```

```

Returns `true` if `o` is a string, or `false` otherwise.
FFI function
```

```
lean_string_object * lean_to_string(lean_object * o)

```

```

Performs a runtime check that `o` is indeed a string. If `o` is not a string, an assertion fails.
[←20.7. Characters](Basic-Types/Characters/#Char "20.7. Characters")[20.9. The Unit Type→](Basic-Types/The-Unit-Type/#The-Lean-Language-Reference--Basic-Types--The-Unit-Type "20.9. The Unit Type")

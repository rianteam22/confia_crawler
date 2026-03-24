[←20.6. Floating-Point Numbers](Basic-Types/Floating-Point-Numbers/#Float "20.6. Floating-Point Numbers")[20.8. Strings→](Basic-Types/Strings/#String "20.8. Strings")
#  20.7. Characters[🔗](find/?domain=Verso.Genre.Manual.section&name=Char "Permalink")
Characters are represented by the type `[Char](Basic-Types/Characters/#Char___mk "Documentation for Char")`, which may be any Unicode [scalar value](http://www.unicode.org/glossary/#unicode_scalar_value). While [strings](Basic-Types/Strings/#String) are UTF-8-encoded arrays of bytes, characters are represented by full 32-bit values. Lean provides special [syntax](Basic-Types/Characters/#char-syntax) for character literals.
##  20.7.1. Logical Model[🔗](find/?domain=Verso.Genre.Manual.section&name=char-model "Permalink")
From the perspective of Lean's logic, characters consist of a 32-bit unsigned integer paired with a proof that it is a valid Unicode scalar value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.mk "Permalink")structure
```


Char : Type


Char : Type


```

Characters are Unicode [scalar values](http://www.unicode.org/glossary/#unicode_scalar_value).
#  Constructor

```
[Char.mk](Basic-Types/Characters/#Char___mk "Documentation for Char.mk")
```

#  Fields

```
val : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")
```

The underlying Unicode scalar value as a `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")`.

```
valid : self.[val](Basic-Types/Characters/#Char___mk "Documentation for Char.val").[isValidChar](Basic-Types/Fixed-Precision-Integers/#UInt32___isValidChar "Documentation for UInt32.isValidChar")
```

The value must be a legal scalar value.
##  20.7.2. Run-Time Representation[🔗](find/?domain=Verso.Genre.Manual.section&name=char-runtime "Permalink")
As a [trivial wrapper](The-Type-System/Inductive-Types/#inductive-types-trivial-wrappers), characters are represented identically to `[UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")`. In particular, characters are represented as 32-bit immediate values in monomorphic contexts. In other words, a field of a constructor or structure of type `[Char](Basic-Types/Characters/#Char___mk "Documentation for Char")` does not require indirection to access. In polymorphic contexts, characters are [boxed](Run-Time-Code/Boxing/#--tech-term-Boxed).
##  20.7.3. Syntax[🔗](find/?domain=Verso.Genre.Manual.section&name=char-syntax "Permalink")
Character literals consist of a single character or an escape sequence enclosed in single quotes (`'`, Unicode `'APOSTROPHE' (U+0027)`). Between these single quotes, the character literal may contain character other that `'`, including newlines, which are included literally (with the caveat that all newlines in a Lean source file are interpreted as `'\n'`, regardless of file encoding and platform). Special characters may be escaped with a backslash, so `'\''` is a character literal that contains a single quote. The following forms of escape sequences are accepted: 

`\r`, `\n`, `\t`, `\\`, `\"`, `\'` 
    
These escape sequences have the usual meaning, mapping to `CR`, `LF`, tab, backslash, double quote, and single quote, respectively. 

`\xNN` 
    
When `NN` is a sequence of two hexadecimal digits, this escape denotes the character whose Unicode code point is indicated by the two-digit hexadecimal code. 

`\uNNNN` 
    
When `NN` is a sequence of two hexadecimal digits, this escape denotes the character whose Unicode code point is indicated by the four-digit hexadecimal code.
##  20.7.4. API Reference[🔗](find/?domain=Verso.Genre.Manual.section&name=char-api "Permalink")
###  20.7.4.1. Conversions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Characters--API-Reference--Conversions "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.ofNat "Permalink")def
```


Char.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


Char.ofNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Converts a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` into a `[Char](Basic-Types/Characters/#Char___mk "Documentation for Char")`. If the `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` does not encode a valid Unicode scalar value, `'\0'` is returned instead.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.toNat "Permalink")def
```


Char.toNat (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Char.toNat (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The character's Unicode code point as a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.isValidCharNat "Permalink")def
```


Char.isValidCharNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : Prop


Char.isValidCharNat (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : Prop


```

True for natural numbers that are valid [Unicode scalar values](https://www.unicode.org/glossary/#unicode_scalar_value).
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.ofUInt8 "Permalink")def
```


Char.ofUInt8 (n : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


Char.ofUInt8 (n : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Converts an 8-bit unsigned integer into a character.
The integer's value is interpreted as a Unicode code point.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.toUInt8 "Permalink")def
```


Char.toUInt8 (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


Char.toUInt8 (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")


```

Converts a character into a `[UInt8](Basic-Types/Fixed-Precision-Integers/#UInt8___ofBitVec "Documentation for UInt8")` that contains its code point.
If the code point is larger than 255, it is truncated (reduced modulo 256).
There are two ways to convert a character to a string. `[Char.toString](Basic-Types/Characters/#Char___toString "Documentation for Char.toString")` converts a character to a singleton string that consists of only that character, while `[Char.quote](Basic-Types/Characters/#Char___quote "Documentation for Char.quote")` converts the character to a string representation of the corresponding character literal.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.toString "Permalink")def
```


Char.toString (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


Char.toString (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Constructs a singleton string that contains only the provided character.
Examples:
  * `'L'.[toString](Basic-Types/Characters/#Char___toString "Documentation for Char.toString") = "L"`
  * `'"'.[toString](Basic-Types/Characters/#Char___toString "Documentation for Char.toString") = "\""`


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.quote "Permalink")def
```


Char.quote (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


Char.quote (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")


```

Quotes the character to its representation as a character literal, surrounded by single quotes and escaped as necessary.
Examples:
  * `'L'.[quote](Basic-Types/Characters/#Char___quote "Documentation for Char.quote") = "'L'"`
  * `'"'.[quote](Basic-Types/Characters/#Char___quote "Documentation for Char.quote") = "'\\\"'"`


From Characters to Strings
`[Char.toString](Basic-Types/Characters/#Char___toString "Documentation for Char.toString")` produces a string that contains only the character in question:
``"e"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") 'e'.[toString](Basic-Types/Characters/#Char___toString "Documentation for Char.toString") `
```
"e"
```
``"e"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") '\x65'.[toString](Basic-Types/Characters/#Char___toString "Documentation for Char.toString") `
```
"e"
```
``"\""`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") '"'.[toString](Basic-Types/Characters/#Char___toString "Documentation for Char.toString") `
```
"\""
```

`[Char.quote](Basic-Types/Characters/#Char___quote "Documentation for Char.quote")` produces a string that contains a character literal, suitably escaped:
``"'e'"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") 'e'.[quote](Basic-Types/Characters/#Char___quote "Documentation for Char.quote") `
```
"'e'"
```
``"'e'"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") '\x65'.[quote](Basic-Types/Characters/#Char___quote "Documentation for Char.quote") `
```
"'e'"
```
``"'\\\"'"`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") '"'.[quote](Basic-Types/Characters/#Char___quote "Documentation for Char.quote") `
```
"'\\\"'"
```

[Live ↪](javascript:openLiveLink\("MQUwbghgNgBA5COA6ALgewMooE4EsB2A5gFDGiSxwA6AHgGwCsy6WeRp508ARM5jgRJlwXBMgCOAVzQoQHEZVqMJ02fIo8VMkEA"\))
###  20.7.4.2. Character Classes[🔗](find/?domain=Verso.Genre.Manual.section&name=char-api-classes "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.isAlpha "Permalink")def
```


Char.isAlpha (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Char.isAlpha (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the character is an ASCII letter.
The ASCII letters are the following: `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.isAlphanum "Permalink")def
```


Char.isAlphanum (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Char.isAlphanum (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the character is an ASCII letter or digit.
The ASCII letters are the following: `ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`. The ASCII digits are the following: `0123456789`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.isDigit "Permalink")def
```


Char.isDigit (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Char.isDigit (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the character is an ASCII digit.
The ASCII digits are the following: `0123456789`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.isLower "Permalink")def
```


Char.isLower (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Char.isLower (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the character is a lowercase ASCII letter.
The lowercase ASCII letters are the following: `abcdefghijklmnopqrstuvwxyz`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.isUpper "Permalink")def
```


Char.isUpper (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Char.isUpper (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the character is a uppercase ASCII letter.
The uppercase ASCII letters are the following: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.isWhitespace "Permalink")def
```


Char.isWhitespace (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Char.isWhitespace (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the character is a space `(' ', U+0020)`, a tab `('\t', U+0009)`, a carriage return `('\r', U+000D)`, or a newline `('\n', U+000A)`.
###  20.7.4.3. Case Conversion[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Characters--API-Reference--Case-Conversion "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.toUpper "Permalink")def
```


Char.toUpper (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


Char.toUpper (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Converts a lowercase ASCII letter to the corresponding uppercase letter. Letters outside the ASCII alphabet are returned unchanged.
The lowercase ASCII letters are the following: `abcdefghijklmnopqrstuvwxyz`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.toLower "Permalink")def
```


Char.toLower (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


Char.toLower (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")


```

Converts an uppercase ASCII letter to the corresponding lowercase letter. Letters outside the ASCII alphabet are returned unchanged.
The uppercase ASCII letters are the following: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`.
###  20.7.4.4. Comparisons[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Characters--API-Reference--Comparisons "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.le "Permalink")def
```


Char.le (a b : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : Prop


Char.le (a b : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : Prop


```

One character is less than or equal to another if its code point is less than or equal to the other's.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.lt "Permalink")def
```


Char.lt (a b : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : Prop


Char.lt (a b : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : Prop


```

One character is less than another if its code point is strictly less than the other's.
###  20.7.4.5. Unicode[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Characters--API-Reference--Unicode "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.utf8Size "Permalink")def
```


Char.utf8Size (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Char.utf8Size (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the number of bytes required to encode this `[Char](Basic-Types/Characters/#Char___mk "Documentation for Char")` in UTF-8.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Char.utf16Size "Permalink")def
```


Char.utf16Size (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


Char.utf16Size (c : [Char](Basic-Types/Characters/#Char___mk "Documentation for Char")) : [UInt32](Basic-Types/Fixed-Precision-Integers/#UInt32___ofBitVec "Documentation for UInt32")


```

Returns the number of bytes required to encode this `[Char](Basic-Types/Characters/#Char___mk "Documentation for Char")` in UTF-16.
[←20.6. Floating-Point Numbers](Basic-Types/Floating-Point-Numbers/#Float "20.6. Floating-Point Numbers")[20.8. Strings→](Basic-Types/Strings/#String "20.8. Strings")

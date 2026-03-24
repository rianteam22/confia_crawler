[←20.18. Ranges](Basic-Types/Ranges/#ranges "20.18. Ranges")[20.20. Subtypes→](Basic-Types/Subtypes/#Subtype "20.20. Subtypes")
#  20.19. Maps and Sets[🔗](find/?domain=Verso.Genre.Manual.section&name=maps "Permalink")
A _map_ is a data structure that associates keys with values. They are also referred to as _dictionaries_ , _associative arrays_ , or simply as hash tables.
In Lean, maps may have the following properties: 

Representation
    
The in-memory representation of a map may be either a tree or a hash table. Tree-based representations are better when the [reference](Run-Time-Code/Reference-Counting/#reference-counting) to the data structure is shared, because hash tables are based on [arrays](Basic-Types/Arrays/#Array). Arrays are copied in full on modification when the reference is not unique, while only the path from the root of the tree to the modified nodes must be copied on modification of a tree. Hash tables, on the other hand, can be more efficient when references are not shared, because non-shared arrays can be modified in constant time. Furthermore, tree-based maps store data in order and thus support ordered traversals of the data. 

Extensionality
    
Maps can be viewed as partial functions from keys to values. _Extensional maps_ are maps for which propositional equality matches this interpretation. This can be convenient for reasoning, but it also rules out some useful operations that would be able to distinguish between them. In general, extensional maps should be used only when needed for verification. 

Dependent or Not
    
A _dependent map_ is one in which the type of each value is determined by its corresponding key, rather than being constant. Dependent maps have more expressive power, but are also more difficult to use. They impose more requirements on their users. For example, many operations on `[DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap")` require `[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq")` instances rather than `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")`.  
|  Map  |  Representation  |  Extensional?  |  Dependent?  |  
| --- | --- | --- | --- |  
|  `[TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap")`  |  Tree  |  No  |  No  |  
|  `[DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap")`  |  Tree  |  No  |  Yes  |  
|  `[HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap")`  |  Hash Table  |  No  |  No  |  
|  `[DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap")`  |  Hash Table  |  No  |  Yes  |  
|  `[ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap")`  |  Hash Table  |  Yes  |  No  |  
|  `[ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap")`  |  Hash Table  |  Yes  |  Yes  |  
A map can always be used as a set by setting its type of values to `[Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")`. The following set types are provided:
  * `[Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet")` is a set based on hash tables. Its performance characteristics are like those of `[Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap")`: it is based on arrays and can be efficiently updated, but only when not shared.
  * `[Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet")` is a set based on balanced trees. Its performance characteristics are like those of `[Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap")`.
  * `[Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet")` is an extensional hash set type that matches the mathematical notion of finite sets: two sets are equal if they contain the same elements.


##  20.19.1. Library Design[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Library-Design "Permalink")
All the basic operations on maps and sets are fully verified. They are proven correct with respect to simpler models implemented with lists. At the same time, maps and sets have predictable performance.
Some types include additional operations that are not yet fully verified. These operations are useful, and not all programs need full verification. Examples include `[HashMap.partition](Basic-Types/Maps-and-Sets/#Std___HashMap___partition "Documentation for Std.HashMap.partition")` and `[TreeMap.filterMap](Basic-Types/Maps-and-Sets/#Std___TreeMap___filterMap "Documentation for Std.TreeMap.filterMap")`.
###  20.19.1.1. Fused Operations[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Library-Design--Fused-Operations "Permalink")
It is common to modify a table based on its pre-existing contents. To avoid having to traverse a data structure twice, many query/modification pairs are provided in “fused” variants that perform a query while modifying a map or set. In some cases, the result of the query affects the modification.
For example, `[Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap")` provides `[containsThenInsert](Basic-Types/Maps-and-Sets/#Std___HashMap___containsThenInsert "Documentation for Std.HashMap.containsThenInsert")`, which inserts a key-value pair into a map while signalling whether it was previously found, and `[containsThenInsertIfNew](Basic-Types/Maps-and-Sets/#Std___HashMap___containsThenInsertIfNew "Documentation for Std.HashMap.containsThenInsertIfNew")`, which inserts the new mapping only if it was not previously present. The `[alter](Basic-Types/Maps-and-Sets/#Std___HashMap___alter "Documentation for Std.HashMap.alter")` function modifies the value for a given key without having to search for the key multiple times; the alternation is performed by a function in which missing values are represented by `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`.
###  20.19.1.2. Raw Data and Invariants[🔗](find/?domain=Verso.Genre.Manual.section&name=raw-data "Permalink")
Both hash-based and tree-based maps rely on certain internal well-formedness invariants, such as that trees are balanced and ordered. In Lean's standard library, these data structures are represented as a pair of the underlying data with a proof that it is well formed. This fact is mostly an internal implementation detail; however, it is relevant to users in one situation: this representation prevents them from being used in [nested inductive types](The-Type-System/Inductive-Types/#--tech-term-Nested-inductive-types).
To enable their use in nested inductive types, the standard library provides “raw” variants of each container along with separate “unbundled” versions of their invariants. These use the following naming convention:
  * `T.Raw` is the version of type `T` without its invariants. For example, `[Std.HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw")` is a version of `[Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap")` without the embedded proofs.
  * `T.Raw.WF` is the corresponding well-formedness predicate. For example, `[Std.HashMap.Raw.WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")` asserts that a `[Std.HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw")` is well-formed.
  * Each operation on `T`, called `T.f`, has a corresponding operation on `T.Raw` called `T.Raw.f`. For example, `Std.HashMap.Raw.insert` is the version of `[Std.HashMap.insert](Basic-Types/Maps-and-Sets/#Std___HashMap___insert "Documentation for Std.HashMap.insert")` to be used with raw hash maps.
  * Each operation `T.Raw.f` has an associated well-formedness lemma `T.Raw.WF.f`. For example, `Std.HashMap.Raw.WF.insert` asserts that inserting a new key-value pair into a well-formed raw hash map results in a well-formed raw hash map.


Because the vast majority of use cases do not require them, not all lemmas about raw types are imported by default with the data structures. It is usually necessary to import `Std.Data.T.RawLemmas` (where `T` is the data structure in question).
A nested inductive type that occurs inside a map or set should be defined in three stages:
  1. First, define a raw version of the nested inductive type that uses the raw version of the map or set type. Define any necessary operations.
  2. Next, define an inductive predicate that asserts that all maps or sets in the raw nested type are well formed. Show that the operations on the raw type preserve well-formedness.
  3. Construct an appropriate interface to the nested inductive type by defining an API that proves well-formedness properties as needed, hiding them from users.

Nested Inductive Types with `Std.HashMap`
This example requires that `Std.Data.HashMap.RawLemmas` is imported. To keep the code shorter, the `Std` namespace is opened:
`[open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Std `
The map of an adventure game may consist of a series of rooms, connected by passages. Each room has a description, and each passage faces in a particular direction. This can be represented as a recursive structure.
``(kernel) application type mismatch   [DHashMap.Raw.WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF") inner argument has type   _nested.Std.DHashMap.Raw_3 but function has type   (DHashMap.Raw String fun x => Maze) → Prop`structure Maze where description : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") passages : [HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") Maze `
This definition is rejected:

```
(kernel) application type mismatch
  [DHashMap.Raw.WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF") inner
argument has type
  _nested.Std.DHashMap.Raw_3
but function has type
  (DHashMap.Raw String fun x => Maze) → Prop
```

Making this work requires separating the well-formedness predicates from the structure. The first step is to redefine the type without embedded hash map invariants:
`structure RawMaze where   description : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")   passages : [Std.HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") `
The most basic raw maze has no passages:
`def RawMaze.base (description : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") where   [description](Basic-Types/Maps-and-Sets/#RawMaze___description-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := description   [passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := ∅ `
A passage to a further maze can be added to a raw maze using `[RawMaze.insert](Basic-Types/Maps-and-Sets/#RawMaze___insert-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")`:
`def RawMaze.insert (maze : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example"))     (direction : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (next : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")) : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") :=   { maze with     [passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := maze.[passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example").insert direction next   } `
The second step is to define a well-formedness predicate for `[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")` that ensures that each included hash map is well-formed. If the `[passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")` field itself is well-formed, and all raw mazes included in it are well-formed, then a raw maze is well-formed.
`inductive RawMaze.WF : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") → Prop   | mk {description passages} :     (∀ (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) v, passages[dir]? = [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → [WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") v) →     passages.[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF") →     [WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") { [description](Basic-Types/Maps-and-Sets/#RawMaze___description-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example"), [passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := passages } `
Base mazes are well-formed, and inserting a passage to a well-formed maze into some other well-formed maze produces a well-formed maze:
`theorem RawMaze.base_wf (description : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :     [RawMaze.WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") ([.base](Basic-Types/Maps-and-Sets/#RawMaze___base-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") description) := bydescription:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")⊢ ([base](Basic-Types/Maps-and-Sets/#RawMaze___base-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") description).[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")   [constructor](Tactic-Proofs/Tactic-Reference/#constructor "Documentation for tactic")adescription:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")⊢ ∀ (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")), ∅[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")adescription:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")⊢ ∅.[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")   .adescription:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")⊢ ∀ (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")), ∅[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") v hadescription:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")v:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")h:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")⊢ ∅[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")v[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") h → h.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") h'adescription:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")v:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")h:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")h':∅[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")v[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") h⊢ h.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")     [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [Std.HashMap.Raw.getElem?_empty] at *All goals completed! 🐙   .adescription:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")⊢ ∅.[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF") [exact](Tactic-Proofs/Tactic-Reference/#exact "Documentation for tactic") HashMap.Raw.WF.emptyAll goals completed! 🐙  def RawMaze.insert_wf (maze : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")) :     [WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") maze → [WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") next → [WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") (maze.[insert](Basic-Types/Maps-and-Sets/#RawMaze___insert-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") dir next) := bynext:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")maze:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")⊢ maze.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") → next.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") → (maze.[insert](Basic-Types/Maps-and-Sets/#RawMaze___insert-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") dir next).[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")   [let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic") ⟨desc, passages⟩ := mazenext:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")maze:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")desc:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")passages:[HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")⊢ { [description](Basic-Types/Maps-and-Sets/#RawMaze___description-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := desc, [passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := passages }.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") →   next.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") → ({ [description](Basic-Types/Maps-and-Sets/#RawMaze___description-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := desc, [passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := passages }.[insert](Basic-Types/Maps-and-Sets/#RawMaze___insert-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") dir next).[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")   [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") ⟨wfMore, wfPassages⟩ wfNextnext:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")maze:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")desc:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")passages:[HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfMore:∀ (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")), passages[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfPassages:passages.[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")wfNext:next.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")⊢ ({ [description](Basic-Types/Maps-and-Sets/#RawMaze___description-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := desc, [passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := passages }.[insert](Basic-Types/Maps-and-Sets/#RawMaze___insert-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") dir next).[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")   [constructor](Tactic-Proofs/Tactic-Reference/#constructor "Documentation for tactic")anext:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")maze:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")desc:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")passages:[HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfMore:∀ (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")), passages[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfPassages:passages.[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")wfNext:next.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")⊢ ∀ (dir_1 : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")),   ({ [description](Basic-Types/Maps-and-Sets/#RawMaze___description-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := desc, [passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := passages }.[passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example").insert dir next)[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir_1[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")anext:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")maze:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")desc:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")passages:[HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfMore:∀ (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")), passages[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfPassages:passages.[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")wfNext:next.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")⊢ ({ [description](Basic-Types/Maps-and-Sets/#RawMaze___description-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := desc, [passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := passages }.[passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example").insert dir next).[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")   .anext:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")maze:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")desc:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")passages:[HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfMore:∀ (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")), passages[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfPassages:passages.[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")wfNext:next.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")⊢ ∀ (dir_1 : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")),   ({ [description](Basic-Types/Maps-and-Sets/#RawMaze___description-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := desc, [passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := passages }.[passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example").insert dir next)[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir_1[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") dir' vanext:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")maze:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")desc:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")passages:[HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfMore:∀ (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")), passages[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfPassages:passages.[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")wfNext:next.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir':[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")v:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")⊢ ({ [description](Basic-Types/Maps-and-Sets/#RawMaze___description-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := desc, [passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := passages }.[passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example").insert dir next)[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir'[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")     [rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic") [HashMap.Raw.getElem?_insert wfPassages]anext:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")maze:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")desc:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")passages:[HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfMore:∀ (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")), passages[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfPassages:passages.[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")wfNext:next.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir':[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")v:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")⊢ (if [(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")dir [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") dir'[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true") then [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") next else passages[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir'[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")) [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")     [split](Tactic-Proofs/Tactic-Reference/#split "Documentation for tactic")a.isTruenext:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")maze:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")desc:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")passages:[HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfMore:∀ (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")), passages[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfPassages:passages.[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")wfNext:next.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir':[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")v:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")h✝:[(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")dir [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") dir'[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")⊢ [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") next [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")a.isFalsenext:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")maze:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")desc:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")passages:[HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfMore:∀ (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")), passages[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfPassages:passages.[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")wfNext:next.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir':[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")v:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")h✝:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")dir [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") dir'[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")⊢ passages[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir'[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") <;>a.isTruenext:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")maze:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")desc:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")passages:[HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfMore:∀ (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")), passages[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfPassages:passages.[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")wfNext:next.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir':[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")v:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")h✝:[(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")dir [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") dir'[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")⊢ [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") next [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")a.isFalsenext:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")maze:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")desc:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")passages:[HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfMore:∀ (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")), passages[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfPassages:passages.[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")wfNext:next.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir':[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")v:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")h✝:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")dir [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") dir'[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")⊢ passages[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir'[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") [intros](Tactic-Proofs/Tactic-Reference/#intros "Documentation for tactic")a.isFalsenext:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")maze:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")desc:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")passages:[HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfMore:∀ (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")), passages[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfPassages:passages.[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")wfNext:next.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir':[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")v:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")h✝:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")dir [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") dir'[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")a✝:passages[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir'[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v⊢ v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") <;>a.isTruenext:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")maze:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")desc:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")passages:[HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfMore:∀ (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")), passages[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfPassages:passages.[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")wfNext:next.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir':[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")v:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")h✝:[(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")dir [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") dir'[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")a✝:[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") next [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v⊢ v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")a.isFalsenext:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")maze:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")desc:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")passages:[HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfMore:∀ (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")), passages[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfPassages:passages.[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")wfNext:next.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir':[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")v:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")h✝:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[(](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")dir [==](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") dir'[)](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")a✝:passages[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir'[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v⊢ v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") [simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic") [wfMore dir']All goals completed! 🐙   .anext:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")dir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")maze:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")desc:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")passages:[HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfMore:∀ (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")), passages[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfPassages:passages.[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")wfNext:next.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")⊢ ({ [description](Basic-Types/Maps-and-Sets/#RawMaze___description-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := desc, [passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := passages }.[passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example").insert dir next).[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF") [simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic") [HashMap.Raw.WF.insert]All goals completed! 🐙 `
Finally, a more friendly interface can be defined that frees users from worrying about well-formedness. A `Maze` bundles up a `[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")` with a proof that it is well-formed:
`structure Maze where   raw : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")   wf : raw.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") `
The `[base](Basic-Types/Maps-and-Sets/#Maze___base-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")` and `[insert](Basic-Types/Maps-and-Sets/#Maze___insert-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")` operators take care of the well-formedness proof obligations:
`def Maze.base (description : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : Maze where   [raw](Basic-Types/Maps-and-Sets/#Maze___raw-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := [.base](Basic-Types/Maps-and-Sets/#RawMaze___base-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") description   [wf](Basic-Types/Maps-and-Sets/#Maze___wf-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := bydescription:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")⊢ ([RawMaze.base](Basic-Types/Maps-and-Sets/#RawMaze___base-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") description).[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") [apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") [RawMaze.base_wf](Basic-Types/Maps-and-Sets/#RawMaze___base_wf-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")All goals completed! 🐙  def Maze.insert (maze : Maze)     (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (next : Maze) : Maze where   [raw](Basic-Types/Maps-and-Sets/#Maze___raw-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := maze.[raw](Basic-Types/Maps-and-Sets/#Maze___raw-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example").[insert](Basic-Types/Maps-and-Sets/#RawMaze___insert-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") dir next.[raw](Basic-Types/Maps-and-Sets/#Maze___raw-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")   [wf](Basic-Types/Maps-and-Sets/#Maze___wf-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := [RawMaze.insert_wf](Basic-Types/Maps-and-Sets/#RawMaze___insert_wf-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") maze.[raw](Basic-Types/Maps-and-Sets/#Maze___raw-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") maze.[wf](Basic-Types/Maps-and-Sets/#Maze___wf-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") next.[wf](Basic-Types/Maps-and-Sets/#Maze___wf-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") `
Users of the `Maze` API may either check the description of the current maze or attempt to go in a direction to a new maze:
`def Maze.description (maze : Maze) : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") :=   maze.[raw](Basic-Types/Maps-and-Sets/#Maze___raw-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example").[description](Basic-Types/Maps-and-Sets/#RawMaze___description-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")  def Maze.go? (maze : Maze) (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") Maze :=   [match](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax") h : maze.[raw](Basic-Types/Maps-and-Sets/#Maze___raw-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example").[passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")[dir]? [with](Terms/Pattern-Matching/#Lean___Parser___Term___match "Documentation for syntax")   | [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none") => [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")   | [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") m' =>     Maze.mk m' <| bymaze:Mazedir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")m':[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")h:maze.[raw](Basic-Types/Maps-and-Sets/#Maze___raw-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example").[passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") m'⊢ m'.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")       [let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic") ⟨r, wf⟩ := mazemaze:Mazedir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")m':[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")r:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wf:r.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")h:{ [raw](Basic-Types/Maps-and-Sets/#Maze___raw-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := r, [wf](Basic-Types/Maps-and-Sets/#Maze___wf-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := wf }.[raw](Basic-Types/Maps-and-Sets/#Maze___raw-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example").[passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") m'⊢ m'.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")       [let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic") ⟨wfAll, _⟩ := wfmaze:Mazedir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")m':[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")r:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wf:r.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")description✝:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")passages✝:[HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfAll:∀ (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")), passages✝[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")a✝:passages✝.[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")h:{ [raw](Basic-Types/Maps-and-Sets/#Maze___raw-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := { [description](Basic-Types/Maps-and-Sets/#RawMaze___description-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := description✝, [passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := passages✝ }, [wf](Basic-Types/Maps-and-Sets/#Maze___wf-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := ⋯ }.[raw](Basic-Types/Maps-and-Sets/#Maze___raw-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example").[passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") m'⊢ m'.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")       [apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") wfAll diramaze:Mazedir:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")m':[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")r:[RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wf:r.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")description✝:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")passages✝:[HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")wfAll:∀ (dir : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (v : [RawMaze](Basic-Types/Maps-and-Sets/#RawMaze-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")), passages✝[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v → v.[WF](Basic-Types/Maps-and-Sets/#RawMaze___WF-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")a✝:passages✝.[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")h:{ [raw](Basic-Types/Maps-and-Sets/#Maze___raw-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := { [description](Basic-Types/Maps-and-Sets/#RawMaze___description-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := description✝, [passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := passages✝ }, [wf](Basic-Types/Maps-and-Sets/#Maze___wf-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example") := ⋯ }.[raw](Basic-Types/Maps-and-Sets/#Maze___raw-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example").[passages](Basic-Types/Maps-and-Sets/#RawMaze___passages-_LPAR_in-Nested-Inductive-Types-with--Std___HashMap_RPAR_ "Definition of example")[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") m'⊢ passages✝[[](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")dir[]](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?")[?](Type-Classes/Basic-Classes/#GetElem______mk "Documentation for GetElem?.getElem?") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") m'       [apply](Tactic-Proofs/Tactic-Reference/#apply "Documentation for tactic") hAll goals completed! 🐙 `
[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAZRgEwFComApgO0S9AZxigFcBjGUqLOAJQEMB3AWQYC9amALLG1OHGRZC5KMDAxgEPAC584nAHMBcMA0KEGSkXHlJkAOgASG7mzCHGTBcGX1mbTumEAzB6w5ZDAIw20ACmFRcUlpOVtlAEo9DycuXn5BYLEJKRk9AF4hEVSwmVV1TW1dWWzAUCIXLHdreMM7Qj54AJAvWNqvKNVBIOAaSnDYpEUlGICcLAAPeHkOzhjZxzay1QBvOFbOOCZgGG5utQ0tHUIsja9DIuORepxG2CE+rAGMienVAF90O2QKKQA3WhzbwAdQAYu0lltAEmEcAAClBMKoAD4bADWcFWKVC6TwVxKhA+egOAUAAERwXpQIYkOyjOD/AA0h2KJwA2sg+gBdAD8cGyhAgIFo/zgsPB9Ji0IO+JOhnFUsEgnF62xaXCTJlpWymtOX1Qeyw0CwIDiFz8jQA+kx3EFcjjBvoadFiYrTZw5RCAr5/DkQmqZAtsj4AJ6qcgyYhkSjQVSGOB2EgQelwbgpgDkB0IoDAcFZBhMZgsVmYhh0MAAogAbY3ci3GyTBzlwBjwABUsbgUwYlDgpkI5gYlmsHsM9ZgodQbjd3gaTStNs2tEWnnmLsV4sXorg4re8DFnsXt3u8A5VN3gbgIdU1fggAvyFIao4EwCX5GdF6oE4i4LfrSwjUzrThJ8Tlfa0ADkphgMMIxIP4Y0EONPyTU803pA4oBsVk+wHIcSzLKsawtWcHkA4CRE5TMwErXY4AAHgAbgAPnjHBE1OBjmKzcALQYStK1zX8jUeKA0wohC4C4sAeL43NsKLYdwSPJoKNQSM/moWh4m2RIsFUKBmEhFddMEa1Yn0pgPSqdw6nNQJVXyCJhlpBY4C0ng+GMuBzLOb1Gl9PJcVUUyykvYNmzAKiwuBXysHnKzXIuYjmk3eR4i6V1KWpEYxl3WI0rytp3KSLyDJCw9zKUh5TzgXdDHMoL3BC6Kkvnc53W8w9TNq614rqezcQpFKEtXR0RiyVRypLfrwl6i4lAgXkWmWYasDGarRuc2IAHkHJW8bBFaGByFTVN5EmiydXZLleR2PYURqmRaEyZicEe+6BSFDZUOeg46hADEQFQ2jUSvV1BBvb8oAA1xXzKrwDnBrA72tABBPimQtWHsh6sHwsi7ZXDR/jTwRvHKzC7ggA"\))
###  20.19.1.3. Suitable Operators for Uniqueness[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Library-Design--Suitable-Operators-for-Uniqueness "Permalink")
Care should be taken when working with data structures to ensure that as many references are unique as possible, which enables Lean to use destructive mutation behind the scenes while maintaining a pure functional interface. The map and set library provides operators that can be used to maintain uniqueness of references. In particular, when possible, operations such as `[alter](Basic-Types/Maps-and-Sets/#Std___HashMap___alter "Documentation for Std.HashMap.alter")` or `[modify](Basic-Types/Maps-and-Sets/#Std___HashMap___modify "Documentation for Std.HashMap.modify")` should be preferred over explicitly retrieving a value, modifying it, and reinserting it. These operations avoid creating a second reference to the value during modification.
Modifying Values in Maps
`[open](Namespaces-and-Sections/#Lean___Parser___Command___open "Documentation for syntax") Std `
The function `[addAlias](Basic-Types/Maps-and-Sets/#addAlias-_LPAR_in-Modifying-Values-in-Maps_RPAR_ "Definition of example")` is used to track aliases of a string in some data set. One way to add an alias is to first look up the existing aliases, defaulting to the empty array, then insert the new alias, and finally save the resulting array in the map:
`def addAlias (aliases : [HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")))     (key value : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :     [HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :=   let prior := aliases.[getD](Basic-Types/Maps-and-Sets/#Std___HashMap___getD "Documentation for Std.HashMap.getD") key #[]   aliases.[insert](Basic-Types/Maps-and-Sets/#Std___HashMap___insert "Documentation for Std.HashMap.insert") key (prior.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") value) `
This implementation has poor performance characteristics. Because the map retains a reference to the prior values, the array must be copied rather than mutated. A better implementation explicitly erases the prior value from the map before modifying it:
`def addAlias' (aliases : [HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")))     (key value : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :     [HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :=   let prior := aliases.[getD](Basic-Types/Maps-and-Sets/#Std___HashMap___getD "Documentation for Std.HashMap.getD") key #[]   let aliases := aliases.[erase](Basic-Types/Maps-and-Sets/#Std___HashMap___erase "Documentation for Std.HashMap.erase") key   aliases.[insert](Basic-Types/Maps-and-Sets/#Std___HashMap___insert "Documentation for Std.HashMap.insert") key (prior.[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") value) `
Using `[HashMap.alter](Basic-Types/Maps-and-Sets/#Std___HashMap___alter "Documentation for Std.HashMap.alter")` is even better. It removes the need to explicitly delete and re-insert the value:
`def addAlias'' (aliases : [HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")))     (key value : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :     [HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) :=   aliases.[alter](Basic-Types/Maps-and-Sets/#Std___HashMap___alter "Documentation for Std.HashMap.alter") key fun prior? =>     [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ((prior?.[getD](Basic-Types/Optional-Values/#Option___getD "Documentation for Option.getD") #[]).[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") value) `
[Live ↪](javascript:openLiveLink\("JYWwDg9gTgLgBAZRgEwFComApgO0S9ZLAMzgENlkBBAG2DIGc4AKMuxrJgLjgAlGAFgFkyYfFGA4A5iypQoZAJ7jJUgJRrUcbSwDWWZQDc2AVyxweSCdLUWtO/g2GiV02fKWv1FgLz2aWPBgEtC+5OwMnAB0UoEAInD6ygDEANoAuvZs9JEMUZKRsIkGLMHA0FFgJk5wxjRmmqhEpBTUEQDkLNkc3HyCImJWqu4KykM2mjp6JXVmFl62XPbajs6DMNYyzHKjC77+gXBloVw+4TnRsTAJSXBpmdoB8N25YS/RWAqRxYpZEdEFT7wW7MY5QSrVAS1UxYRrNciUWg5dqdVj/XqrAZeEaecbqSY6Zi3WbmSwbVSLZZ9JxYvE4sbkmz7bTvPJsGCfH5wYgmPBggD8cB8AD4qQwICBzMxQSEoPyYvE7hk1BCaiS1EA"\))
##  20.19.2. Hash Maps[🔗](find/?domain=Verso.Genre.Manual.section&name=HashMap "Permalink")
The declarations in this section should be imported using `import Std.HashMap`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap "Permalink")structure
```


Std.HashMap.{u, v} (α : Type u) (β : Type v) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] :
  Type (max u v)


Std.HashMap.{u, v} (α : Type u)
  (β : Type v) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] :
  Type (max u v)


```

Hash maps.
This is a simple separate-chaining hash table. The data of the hash map consists of a cached size and an array of buckets, where each bucket is a linked list of key-value pairs. The number of buckets is always a power of two. The hash map doubles its size upon inserting an element such that the number of elements is more than 75% of the number of buckets.
The hash table is backed by an `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")`. Users should make sure that the hash map is used linearly to avoid expensive copies.
The hash map uses `==` (provided by the `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` typeclass) to compare keys and `[hash](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable.hash")` (provided by the `[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable")` typeclass) to hash them. To ensure that the operations behave as expected, `==` should be an equivalence relation and `a == b` should imply `hash a = hash b` (see also the `[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq")` and `[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable")` typeclasses). Both of these conditions are automatic if the BEq instance is lawful, i.e., if `a == b` implies `a = b`.
These hash maps contain a bundled well-formedness invariant, which means that they cannot be used in nested inductive types. For these use cases, `Std.Data.HashMap.Raw` and `Std.Data.HashMap.Raw.WF` unbundle the invariant from the hash map. When in doubt, prefer `HashMap` over `HashMap.Raw`.
Dependent hash maps, in which keys may occur in their values' types, are available as `Std.Data.DHashMap`.
###  20.19.2.1. Creation[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Hash-Maps--Creation "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.emptyWithCapacity "Permalink")def
```


Std.HashMap.emptyWithCapacity.{u, v} {α : Type u} {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (capacity : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 8) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


Std.HashMap.emptyWithCapacity.{u, v}
  {α : Type u} {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (capacity : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 8) :
  [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


```

Creates a new empty hash map. The optional parameter `capacity` can be supplied to presize the map so that it can hold the given number of mappings without reallocating. It is also possible to use the empty collection notations `∅` and `{}` to create an empty hash map with the default capacity.
###  20.19.2.2. Properties[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Hash-Maps--Properties "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.size "Permalink")def
```


Std.HashMap.size.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Std.HashMap.size.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of mappings present in the hash map
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.isEmpty "Permalink")def
```


Std.HashMap.isEmpty.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.HashMap.isEmpty.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the hash map contains no mappings.
Note that if your `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` instance is not reflexive or your `[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable")` instance is not lawful, then it is possible that this function returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` even though is not possible to get anything out of the hash map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.Equiv.inner "Permalink")structure
```


Std.HashMap.Equiv.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m₁ m₂ : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : Prop


Std.HashMap.Equiv.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m₁ m₂ : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : Prop


```

Two hash maps are equivalent in the sense of `Equiv` iff all the keys and values are equal.
#  Constructor

```
[Std.HashMap.Equiv.mk](Basic-Types/Maps-and-Sets/#Std___HashMap___Equiv___mk "Documentation for Std.HashMap.Equiv.mk").{u, v}
```

#  Fields

```
inner : m₁.inner.[Equiv](Basic-Types/Maps-and-Sets/#Std___DHashMap___Equiv___mk "Documentation for Std.DHashMap.Equiv") m₂.inner
```

Internal implementation detail of the hash map
syntaxEquivalence
The relation `[HashMap.Equiv](Basic-Types/Maps-and-Sets/#Std___HashMap___Equiv___mk "Documentation for Std.HashMap.Equiv")` can also be written with an infix operator, which is scoped to its namespace:

```
term ::= ...
    | 


Two hash maps are equivalent in the sense of Equiv iff
all the keys and values are equal.


term ~m term
```

###  20.19.2.3. Queries[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Hash-Maps--Queries "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.contains "Permalink")def
```


Std.HashMap.contains.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.HashMap.contains.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β)
  (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if there is a mapping for the given key. There is also a `Prop`-valued version of this: `a ∈ m` is equivalent to `m.[contains](Basic-Types/Maps-and-Sets/#Std___HashMap___contains "Documentation for Std.HashMap.contains") a = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Observe that this is different behavior than for lists: for lists, `∈` uses `=` and `contains` uses `==` for comparisons, while for hash maps, both use `==`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.get "Permalink")def
```


Std.HashMap.get.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a : α) (h : a ∈ m) : β


Std.HashMap.get.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β)
  (a : α) (h : a ∈ m) : β


```

The notation `m[a]` or `m[a]'h` is preferred over calling this function directly.
Retrieves the mapping for the given key. Ensures that such a mapping exists by requiring a proof of `a ∈ m`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.get! "Permalink")def
```


Std.HashMap.get!.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") β] (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a : α) : β


Std.HashMap.get!.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") β]
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a : α) : β


```

The notation `m[a]!` is preferred over calling this function directly.
Tries to retrieve the mapping for the given key, panicking if no such mapping is present.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.get? "Permalink")def
```


Std.HashMap.get?.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


Std.HashMap.get?.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β)
  (a : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


```

The notation `m[a]?` is preferred over calling this function directly.
Tries to retrieve the mapping for the given key, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such mapping is present.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.getD "Permalink")def
```


Std.HashMap.getD.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a : α) (fallback : β) : β


Std.HashMap.getD.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β)
  (a : α) (fallback : β) : β


```

Tries to retrieve the mapping for the given key, returning `fallback` if no such mapping is present.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.getKey "Permalink")def
```


Std.HashMap.getKey.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a : α) (h : a ∈ m) : α


Std.HashMap.getKey.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β)
  (a : α) (h : a ∈ m) : α


```

Retrieves the key from the mapping that matches `a`. Ensures that such a mapping exists by requiring a proof of `a ∈ m`. The result is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.getKey! "Permalink")def
```


Std.HashMap.getKey!.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a : α) : α


Std.HashMap.getKey!.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a : α) : α


```

Checks if a mapping for the given key exists and returns the key if it does, otherwise panics. If no panic occurs the result is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.getKey? "Permalink")def
```


Std.HashMap.getKey?.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.HashMap.getKey?.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β)
  (a : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Checks if a mapping for the given key exists and returns the key if it does, otherwise `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`. The result in the `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` case is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.getKeyD "Permalink")def
```


Std.HashMap.getKeyD.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a fallback : α) : α


Std.HashMap.getKeyD.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β)
  (a fallback : α) : α


```

Checks if a mapping for the given key exists and returns the key if it does, otherwise `fallback`. If a mapping exists the result is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.keys "Permalink")def
```


Std.HashMap.keys.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


Std.HashMap.keys.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Returns a list of all keys present in the hash map in some order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.keysArray "Permalink")def
```


Std.HashMap.keysArray.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Std.HashMap.keysArray.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Returns an array of all keys present in the hash map in some order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.values "Permalink")def
```


Std.HashMap.values.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


Std.HashMap.values.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


```

Returns a list of all values present in the hash map in some order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.valuesArray "Permalink")def
```


Std.HashMap.valuesArray.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


Std.HashMap.valuesArray.{u, v}
  {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


```

Returns an array of all values present in the hash map in some order.
###  20.19.2.4. Modification[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Hash-Maps--Modification "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.alter "Permalink")def
```


Std.HashMap.alter.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a : α)
  (f : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


Std.HashMap.alter.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β)
  (a : α) (f : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β) :
  [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


```

Modifies in place the value associated with a given key, allowing creating new values and deleting values via an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` valued replacement function.
This function ensures that the value is used linearly.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.modify "Permalink")def
```


Std.HashMap.modify.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a : α) (f : β → β) :
  [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


Std.HashMap.modify.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β)
  (a : α) (f : β → β) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


```

Modifies in place the value associated with a given key.
This function ensures that the value is used linearly.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.containsThenInsert "Permalink")def
```


Std.HashMap.containsThenInsert.{u, v} {α : Type u} {β : Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a : α)
  (b : β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


Std.HashMap.containsThenInsert.{u, v}
  {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β)
  (a : α) (b : β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


```

Checks whether a key is present in a map, and unconditionally inserts a value for the key.
Equivalent to (but potentially faster than) calling `contains` followed by `insert`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.containsThenInsertIfNew "Permalink")def
```


Std.HashMap.containsThenInsertIfNew.{u, v} {α : Type u} {β : Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a : α)
  (b : β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


Std.HashMap.containsThenInsertIfNew.{u, v}
  {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β)
  (a : α) (b : β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


```

Checks whether a key is present in a map and inserts a value for the key if it was not found.
If the returned `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, then the returned map is unaltered. If the `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, then the returned map has a new value inserted.
Equivalent to (but potentially faster than) calling `contains` followed by `insertIfNew`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.erase "Permalink")def
```


Std.HashMap.erase.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a : α) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


Std.HashMap.erase.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β)
  (a : α) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


```

Removes the mapping for the given key if it exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.filter "Permalink")def
```


Std.HashMap.filter.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (f : α → β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) :
  [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


Std.HashMap.filter.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (f : α → β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


```

Removes all mappings of the hash map for which the given function returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.filterMap "Permalink")def
```


Std.HashMap.filterMap.{u, v, w} {α : Type u} {β : Type v} {γ : Type w}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (f : α → β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ) (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) :
  [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α γ


Std.HashMap.filterMap.{u, v, w}
  {α : Type u} {β : Type v} {γ : Type w}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (f : α → β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ)
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α γ


```

Updates the values of the hash map by applying the given function to all mappings, keeping only those mappings where the function returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.insert "Permalink")def
```


Std.HashMap.insert.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a : α) (b : β) :
  [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


Std.HashMap.insert.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β)
  (a : α) (b : β) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


```

Inserts the given mapping into the map. If there is already a mapping for the given key, then both key and value will be replaced.
Note: this replacement behavior is true for `HashMap`, `DHashMap`, `HashMap.Raw` and `DHashMap.Raw`. The `insert` function on `HashSet` and `HashSet.Raw` behaves differently: it will return the set unchanged if a matching key is already present.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.insertIfNew "Permalink")def
```


Std.HashMap.insertIfNew.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a : α) (b : β) :
  [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


Std.HashMap.insertIfNew.{u, v}
  {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β)
  (a : α) (b : β) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


```

If there is no mapping for the given key, inserts the given mapping into the map. Otherwise, returns the map unaltered.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.getThenInsertIfNew? "Permalink")def
```


Std.HashMap.getThenInsertIfNew?.{u, v} {α : Type u} {β : Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (a : α)
  (b : β) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


Std.HashMap.getThenInsertIfNew?.{u, v}
  {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β)
  (a : α) (b : β) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


```

Checks whether a key is present in a map, returning the associated value, and inserts a value for the key if it was not found.
If the returned value is `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v`, then the returned map is unaltered. If it is `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, then the returned map has a new value inserted.
Equivalent to (but potentially faster than) calling `get?` followed by `insertIfNew`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.insertMany "Permalink")def
```


Std.HashMap.insertMany.{u, v, w} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} {ρ : Type w} [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")]
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (l : ρ) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


Std.HashMap.insertMany.{u, v, w}
  {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} {ρ : Type w}
  [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")]
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) (l : ρ) :
  [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


```

Inserts multiple mappings into the hash map by iterating over the given collection and calling `insert`. If the same key appears multiple times, the last occurrence takes precedence.
Note: this precedence behavior is true for `HashMap`, `DHashMap`, `HashMap.Raw` and `DHashMap.Raw`. The `insertMany` function on `HashSet` and `HashSet.Raw` behaves differently: it will prefer the first appearance.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.insertManyIfNewUnit "Permalink")def
```


Std.HashMap.insertManyIfNewUnit.{u, w} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} {ρ : Type w} [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ α]
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")) (l : ρ) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


Std.HashMap.insertManyIfNewUnit.{u, w}
  {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} {ρ : Type w}
  [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ α] (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit"))
  (l : ρ) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Inserts multiple keys with the value `()` into the hash map by iterating over the given collection and calling `insertIfNew`. If the same key appears multiple times, the first occurrence takes precedence.
This is mainly useful to implement `HashSet.insertMany`, so if you are considering using this, `HashSet` or `HashSet.Raw` might be a better fit for you.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.partition "Permalink")def
```


Std.HashMap.partition.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (f : α → β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) :
  [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


Std.HashMap.partition.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (f : α → β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) :
  [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


```

Partition a hash map into two hash map based on a predicate.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.union "Permalink")def
```


Std.HashMap.union.{u, v} {α : Type u} {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m₁ m₂ : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


Std.HashMap.union.{u, v} {α : Type u}
  {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m₁ m₂ : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) :
  [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


```

Computes the union of the given hash maps. If a key appears in both maps, the entry contained in the second argument will appear in the result.
This function always merges the smaller map into the larger map, so the expected runtime is `O(min(m₁.size, m₂.size))`.
###  20.19.2.5. Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Hash-Maps--Iteration "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.iter "Permalink")def
```


Std.HashMap.iter.{u, v} {α : Type u} {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


Std.HashMap.iter.{u, v} {α : Type u}
  {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Returns a finite iterator over the entries of a hash map. The iterator yields the elements of the map in order and then terminates.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.keysIter "Permalink")def
```


Std.HashMap.keysIter.{u} {α β : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") α


Std.HashMap.keysIter.{u} {α β : Type u}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") α


```

Returns a finite iterator over the entries of a hash map. The iterator yields the elements of the map in order and then terminates.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.valuesIter "Permalink")def
```


Std.HashMap.valuesIter.{u} {α β : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


Std.HashMap.valuesIter.{u} {α β : Type u}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


```

Returns a finite iterator over the entries of a hash map. The iterator yields the elements of the map in order and then terminates.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.map "Permalink")def
```


Std.HashMap.map.{u, v, w} {α : Type u} {β : Type v} {γ : Type w} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (f : α → β → γ) (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α γ


Std.HashMap.map.{u, v, w} {α : Type u}
  {β : Type v} {γ : Type w} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (f : α → β → γ)
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α γ


```

Updates the values of the hash map by applying the given function to all mappings.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.fold "Permalink")def
```


Std.HashMap.fold.{u, v, w} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} {γ : Type w} (f : γ → α → β → γ) (init : γ)
  (b : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : γ


Std.HashMap.fold.{u, v, w} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} {γ : Type w}
  (f : γ → α → β → γ) (init : γ)
  (b : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : γ


```

Folds the given function over the mappings in the hash map in some order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.foldM "Permalink")def
```


Std.HashMap.foldM.{u, v, w, w'} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {γ : Type w}
  (f : γ → α → β → m γ) (init : γ) (b : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : m γ


Std.HashMap.foldM.{u, v, w, w'}
  {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {γ : Type w} (f : γ → α → β → m γ)
  (init : γ) (b : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : m γ


```

Monadically computes a value by folding the given function over the mappings in the hash map in some order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.forIn "Permalink")def
```


Std.HashMap.forIn.{u, v, w, w'} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {γ : Type w}
  (f : α → β → γ → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") γ)) (init : γ) (b : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) :
  m γ


Std.HashMap.forIn.{u, v, w, w'}
  {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {γ : Type w}
  (f : α → β → γ → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") γ))
  (init : γ) (b : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : m γ


```

Support for the `for` loop construct in `do` blocks.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.forM "Permalink")def
```


Std.HashMap.forM.{u, v, w, w'} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → β → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) (b : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


Std.HashMap.forM.{u, v, w, w'}
  {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → β → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit"))
  (b : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Carries out a monadic action on each mapping in the hash map in some order.
###  20.19.2.6. Conversion[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Hash-Maps--Conversion "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.ofList "Permalink")def
```


Std.HashMap.ofList.{u, v} {α : Type u} {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


Std.HashMap.ofList.{u, v} {α : Type u}
  {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β


```

Creates a hash map from a list of mappings. If the same key appears multiple times, the last occurrence takes precedence.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.toArray "Permalink")def
```


Std.HashMap.toArray.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


Std.HashMap.toArray.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Transforms the hash map into an array of mappings in some order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.toList "Permalink")def
```


Std.HashMap.toList.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


Std.HashMap.toList.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Transforms the hash map into a list of mappings in some order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.unitOfArray "Permalink")def
```


Std.HashMap.unitOfArray.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (l : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


Std.HashMap.unitOfArray.{u} {α : Type u}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (l : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) :
  [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Creates a hash map from an array of keys, associating the value `()` with each key.
This is mainly useful to implement `HashSet.ofArray`, so if you are considering using this, `HashSet` or `HashSet.Raw` might be a better fit for you.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.unitOfList "Permalink")def
```


Std.HashMap.unitOfList.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


Std.HashMap.unitOfList.{u} {α : Type u}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Creates a hash map from a list of keys, associating the value `()` with each key.
This is mainly useful to implement `HashSet.ofList`, so if you are considering using this, `HashSet` or `HashSet.Raw` might be a better fit for you.
###  20.19.2.7. Unbundled Variants[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Hash-Maps--Unbundled-Variants "Permalink")
Unbundled maps separate well-formedness proofs from data. This is primarily useful when defining [nested inductive types](Basic-Types/Maps-and-Sets/#raw-data). To use these variants, import the modules `Std.HashMap.Raw` and `Std.HashMap.RawLemmas`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.Raw.inner "Permalink")structure
```


Std.HashMap.Raw.{u, v} (α : Type u) (β : Type v) : Type (max u v)


Std.HashMap.Raw.{u, v} (α : Type u)
  (β : Type v) : Type (max u v)


```

Hash maps without a bundled well-formedness invariant, suitable for use in nested inductive types. The well-formedness invariant is called `Raw.WF`. When in doubt, prefer `HashMap` over `HashMap.Raw`. Lemmas about the operations on `Std.Data.HashMap.Raw` are available in the module `Std.Data.HashMap.RawLemmas`.
This is a simple separate-chaining hash table. The data of the hash map consists of a cached size and an array of buckets, where each bucket is a linked list of key-value pairs. The number of buckets is always a power of two. The hash map doubles its size upon inserting an element such that the number of elements is more than 75% of the number of buckets.
The hash table is backed by an `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")`. Users should make sure that the hash map is used linearly to avoid expensive copies.
The hash map uses `==` (provided by the `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` typeclass) to compare keys and `[hash](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable.hash")` (provided by the `[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable")` typeclass) to hash them. To ensure that the operations behave as expected, `==` should be an equivalence relation and `a == b` should imply `hash a = hash b` (see also the `[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq")` and `[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable")` typeclasses). Both of these conditions are automatic if the BEq instance is lawful, i.e., if `a == b` implies `a = b`.
Dependent hash maps, in which keys may occur in their values' types, are available as `Std.Data.Raw.DHashMap`.
#  Constructor

```
[Std.HashMap.Raw.mk](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw.mk").{u, v}
```

#  Fields

```
inner : [Std.DHashMap.Raw](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw") α fun x => β
```

Internal implementation detail of the hash map
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashMap.Raw.WF.out "Permalink")structure
```


Std.HashMap.Raw.WF.{u, v} {α : Type u} {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m : [Std.HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") α β) : Prop


Std.HashMap.Raw.WF.{u, v} {α : Type u}
  {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m : [Std.HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") α β) : Prop


```

Well-formedness predicate for hash maps. Users of `HashMap` will not need to interact with this. Users of `HashMap.Raw` will need to provide proofs of `WF` to lemmas and should use lemmas `WF.empty` and `WF.insert` (which are always named exactly like the operations they are about) to show that map operations preserve well-formedness.
#  Constructor

```
[Std.HashMap.Raw.WF.mk](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF.mk").{u, v}
```

#  Fields

```
out : m.[inner](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw.inner").[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF")
```

Internal implementation detail of the hash map
##  20.19.3. Dependent Hash Maps[🔗](find/?domain=Verso.Genre.Manual.section&name=DHashMap "Permalink")
The declarations in this section should be imported using `import Std.DHashMap`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap "Permalink")structure
```


Std.DHashMap.{u, v} (α : Type u) (β : α → Type v) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] :
  Type (max u v)


Std.DHashMap.{u, v} (α : Type u)
  (β : α → Type v) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] :
  Type (max u v)


```

Dependent hash maps.
This is a simple separate-chaining hash table. The data of the hash map consists of a cached size and an array of buckets, where each bucket is a linked list of key-value pairs. The number of buckets is always a power of two. The hash map doubles its size upon inserting an element such that the number of elements is more than 75% of the number of buckets.
The hash table is backed by an `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")`. Users should make sure that the hash map is used linearly to avoid expensive copies.
The hash map uses `==` (provided by the `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` typeclass) to compare keys and `[hash](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable.hash")` (provided by the `[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable")` typeclass) to hash them. To ensure that the operations behave as expected, `==` should be an equivalence relation and `a == b` should imply `hash a = hash b` (see also the `[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq")` and `[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable")` typeclasses). Both of these conditions are automatic if the BEq instance is lawful, i.e., if `a == b` implies `a = b`.
These hash maps contain a bundled well-formedness invariant, which means that they cannot be used in nested inductive types. For these use cases, `[Std.DHashMap.Raw](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw")` and `[Std.DHashMap.Raw.WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF")` unbundle the invariant from the hash map. When in doubt, prefer `DHashMap` over `DHashMap.Raw`.
For a variant that is more convenient for use in proofs because of extensionalities, see `[Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap")` which is defined in the module `Std.Data.ExtDHashMap`.
###  20.19.3.1. Creation[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Dependent-Hash-Maps--Creation "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.emptyWithCapacity "Permalink")def
```


Std.DHashMap.emptyWithCapacity.{u, v} {α : Type u} {β : α → Type v}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (capacity : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 8) : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


Std.DHashMap.emptyWithCapacity.{u, v}
  {α : Type u} {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (capacity : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 8) :
  [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


```

Creates a new empty hash map. The optional parameter `capacity` can be supplied to presize the map so that it can hold the given number of mappings without reallocating. It is also possible to use the empty collection notations `∅` and `{}` to create an empty hash map with the default capacity.
###  20.19.3.2. Properties[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Dependent-Hash-Maps--Properties "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.size "Permalink")def
```


Std.DHashMap.size.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Std.DHashMap.size.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of mappings present in the hash map
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.isEmpty "Permalink")def
```


Std.DHashMap.isEmpty.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.DHashMap.isEmpty.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the hash map contains no mappings.
Note that if your `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` instance is not reflexive or your `[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable")` instance is not lawful, then it is possible that this function returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` even though is not possible to get anything out of the hash map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.Equiv "Permalink")structure
```


Std.DHashMap.Equiv.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m₁ m₂ : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : Prop


Std.DHashMap.Equiv.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m₁ m₂ : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : Prop


```

Two hash maps are equivalent in the sense of `Equiv` iff all the keys and values are equal.
#  Constructor

```
[Std.DHashMap.Equiv.mk](Basic-Types/Maps-and-Sets/#Std___DHashMap___Equiv___mk "Documentation for Std.DHashMap.Equiv.mk").{u, v}
```

#  Fields

```
inner : m₁.inner.Equiv m₂.inner
```

Internal implementation detail of the hash map
syntaxEquivalence
The relation `[DHashMap.Equiv](Basic-Types/Maps-and-Sets/#Std___DHashMap___Equiv___mk "Documentation for Std.DHashMap.Equiv")` can also be written with an infix operator, which is scoped to its namespace:

```
term ::= ...
    | 


Two hash maps are equivalent in the sense of Equiv iff
all the keys and values are equal.


term ~m term
```

###  20.19.3.3. Queries[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Dependent-Hash-Maps--Queries "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.contains "Permalink")def
```


Std.DHashMap.contains.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.DHashMap.contains.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if there is a mapping for the given key. There is also a `Prop`-valued version of this: `a ∈ m` is equivalent to `m.[contains](Basic-Types/Maps-and-Sets/#Std___DHashMap___contains "Documentation for Std.DHashMap.contains") a = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Observe that this is different behavior than for lists: for lists, `∈` uses `=` and `contains` uses `==` for comparisons, while for hash maps, both use `==`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.get "Permalink")def
```


Std.DHashMap.get.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α] (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α)
  (h : a ∈ m) : β a


Std.DHashMap.get.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α]
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α)
  (h : a ∈ m) : β a


```

Retrieves the mapping for the given key. Ensures that such a mapping exists by requiring a proof of `a ∈ m`.
Uses the `[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq")` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.get! "Permalink")def
```


Std.DHashMap.get!.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α] (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α)
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") (β a)] : β a


Std.DHashMap.get!.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α]
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α)
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") (β a)] : β a


```

Tries to retrieve the mapping for the given key, panicking if no such mapping is present.
Uses the `[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq")` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.get? "Permalink")def
```


Std.DHashMap.get?.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α] (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a)


Std.DHashMap.get?.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α]
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a)


```

Tries to retrieve the mapping for the given key, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such mapping is present.
Uses the `[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq")` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.getD "Permalink")def
```


Std.DHashMap.getD.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α] (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α)
  (fallback : β a) : β a


Std.DHashMap.getD.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α]
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α)
  (fallback : β a) : β a


```

Tries to retrieve the mapping for the given key, returning `fallback` if no such mapping is present.
Uses the `[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq")` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.getKey "Permalink")def
```


Std.DHashMap.getKey.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α) (h : a ∈ m) : α


Std.DHashMap.getKey.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α)
  (h : a ∈ m) : α


```

Retrieves the key from the mapping that matches `a`. Ensures that such a mapping exists by requiring a proof of `a ∈ m`. The result is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.getKey! "Permalink")def
```


Std.DHashMap.getKey!.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α) : α


Std.DHashMap.getKey!.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α) : α


```

Checks if a mapping for the given key exists and returns the key if it does, otherwise panics. If no panic occurs the result is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.getKey? "Permalink")def
```


Std.DHashMap.getKey?.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.DHashMap.getKey?.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Checks if a mapping for the given key exists and returns the key if it does, otherwise `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`. The result in the `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` case is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.getKeyD "Permalink")def
```


Std.DHashMap.getKeyD.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a fallback : α) : α


Std.DHashMap.getKeyD.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β)
  (a fallback : α) : α


```

Checks if a mapping for the given key exists and returns the key if it does, otherwise `fallback`. If a mapping exists the result is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.keys "Permalink")def
```


Std.DHashMap.keys.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


Std.DHashMap.keys.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Returns a list of all keys present in the hash map in some order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.keysArray "Permalink")def
```


Std.DHashMap.keysArray.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Std.DHashMap.keysArray.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Returns an array of all keys present in the hash map in some order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.values "Permalink")def
```


Std.DHashMap.values.{u, v} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  {β : Type v} (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α fun x => β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


Std.DHashMap.values.{u, v} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  {β : Type v}
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α fun x => β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


```

Returns a list of all values present in the hash map in some order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.valuesArray "Permalink")def
```


Std.DHashMap.valuesArray.{u, v} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} {β : Type v} (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α fun x => β) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


Std.DHashMap.valuesArray.{u, v}
  {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} {β : Type v}
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α fun x => β) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


```

Returns an array of all values present in the hash map in some order.
###  20.19.3.4. Modification[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Dependent-Hash-Maps--Modification "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.alter "Permalink")def
```


Std.DHashMap.alter.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α] (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α)
  (f : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a) → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a)) : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


Std.DHashMap.alter.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α]
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α)
  (f : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a) → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a)) :
  [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


```

Modifies in place the value associated with a given key, allowing creating new values and deleting values via an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` valued replacement function.
This function ensures that the value is used linearly.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.modify "Permalink")def
```


Std.DHashMap.modify.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α] (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α)
  (f : β a → β a) : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


Std.DHashMap.modify.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α]
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α)
  (f : β a → β a) : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


```

Modifies in place the value associated with a given key.
This function ensures that the value is used linearly.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.containsThenInsert "Permalink")def
```


Std.DHashMap.containsThenInsert.{u, v} {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α)
  (b : β a) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


Std.DHashMap.containsThenInsert.{u, v}
  {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α)
  (b : β a) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


```

Checks whether a key is present in a map, and unconditionally inserts a value for the key.
Equivalent to (but potentially faster than) calling `contains` followed by `insert`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.containsThenInsertIfNew "Permalink")def
```


Std.DHashMap.containsThenInsertIfNew.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α) (b : β a) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


Std.DHashMap.containsThenInsertIfNew.{u,
    v}
  {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α)
  (b : β a) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


```

Checks whether a key is present in a map and inserts a value for the key if it was not found.
If the returned `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, then the returned map is unaltered. If the `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, then the returned map has a new value inserted.
Equivalent to (but potentially faster than) calling `contains` followed by `insertIfNew`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.erase "Permalink")def
```


Std.DHashMap.erase.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α) : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


Std.DHashMap.erase.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α) :
  [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


```

Removes the mapping for the given key if it exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.filter "Permalink")def
```


Std.DHashMap.filter.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (f : (a : α) → β a → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) :
  [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


Std.DHashMap.filter.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (f : (a : α) → β a → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) :
  [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


```

Removes all mappings of the hash map for which the given function returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.filterMap "Permalink")def
```


Std.DHashMap.filterMap.{u, v, w} {α : Type u} {β : α → Type v}
  {δ : α → Type w} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (f : (a : α) → β a → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (δ a)) (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) :
  [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α δ


Std.DHashMap.filterMap.{u, v, w}
  {α : Type u} {β : α → Type v}
  {δ : α → Type w} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (f : (a : α) → β a → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (δ a))
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) :
  [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α δ


```

Updates the values of the hash map by applying the given function to all mappings, keeping only those mappings where the function returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.insert "Permalink")def
```


Std.DHashMap.insert.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α) (b : β a) :
  [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


Std.DHashMap.insert.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α)
  (b : β a) : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


```

Inserts the given mapping into the map. If there is already a mapping for the given key, then both key and value will be replaced.
Note: this replacement behavior is true for `HashMap`, `DHashMap`, `HashMap.Raw` and `DHashMap.Raw`. The `insert` function on `HashSet` and `HashSet.Raw` behaves differently: it will return the set unchanged if a matching key is already present.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.insertIfNew "Permalink")def
```


Std.DHashMap.insertIfNew.{u, v} {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α)
  (b : β a) : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


Std.DHashMap.insertIfNew.{u, v}
  {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (a : α)
  (b : β a) : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


```

If there is no mapping for the given key, inserts the given mapping into the map. Otherwise, returns the map unaltered.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.getThenInsertIfNew? "Permalink")def
```


Std.DHashMap.getThenInsertIfNew?.{u, v} {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α] (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β)
  (a : α) (b : β a) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a) [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


Std.DHashMap.getThenInsertIfNew?.{u, v}
  {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α] (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β)
  (a : α) (b : β a) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a) [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


```

Checks whether a key is present in a map, returning the associated value, and inserts a value for the key if it was not found.
If the returned value is `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v`, then the returned map is unaltered. If it is `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, then the returned map has a new value inserted.
Equivalent to (but potentially faster than) calling `get?` followed by `insertIfNew`.
Uses the `[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq")` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.insertMany "Permalink")def
```


Std.DHashMap.insertMany.{u, v, w} {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} {ρ : Type w}
  [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ ((a : α) × β a)] (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (l : ρ) :
  [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


Std.DHashMap.insertMany.{u, v, w}
  {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  {ρ : Type w}
  [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ ((a : α) × β a)]
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) (l : ρ) :
  [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


```

Inserts multiple mappings into the hash map by iterating over the given collection and calling `insert`. If the same key appears multiple times, the last occurrence takes precedence.
Note: this precedence behavior is true for `HashMap`, `DHashMap`, `HashMap.Raw` and `DHashMap.Raw`. The `insertMany` function on `HashSet` and `HashSet.Raw` behaves differently: it will prefer the first appearance.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.partition "Permalink")def
```


Std.DHashMap.partition.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (f : (a : α) → β a → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) :
  [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


Std.DHashMap.partition.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (f : (a : α) → β a → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) :
  [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


```

Partition a hash map into two hash map based on a predicate.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.union "Permalink")def
```


Std.DHashMap.union.{u, v} {α : Type u} {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (m₁ m₂ : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


Std.DHashMap.union.{u, v} {α : Type u}
  {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m₁ m₂ : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) :
  [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


```

Computes the union of the given hash maps. If a key appears in both maps, the entry contained in the second argument will appear in the result.
This function always merges the smaller map into the larger map, so the expected runtime is `O(min(m₁.size, m₂.size))`.
###  20.19.3.5. Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Dependent-Hash-Maps--Iteration "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.iter "Permalink")def
```


Std.DHashMap.iter.{u, v} {α : Type u} {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") ((a : α) × β a)


Std.DHashMap.iter.{u, v} {α : Type u}
  {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") ((a : α) × β a)


```

Returns a finite iterator over the entries of a dependent hash map. The iterator yields the elements of the map in order and then terminates.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.keysIter "Permalink")def
```


Std.DHashMap.keysIter.{u} {α : Type u} {β : α → Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") α


Std.DHashMap.keysIter.{u} {α : Type u}
  {β : α → Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") α


```

Returns a finite iterator over the keys of a dependent hash map. The iterator yields the keys in order and then terminates.
The key and value types must live in the same universe.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.valuesIter "Permalink")def
```


Std.DHashMap.valuesIter.{u} {α β : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α fun x => β) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


Std.DHashMap.valuesIter.{u} {α β : Type u}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α fun x => β) :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


```

Returns a finite iterator over the values of a hash map. The iterator yields the values in order and then terminates.
The key and value types must live in the same universe.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.map "Permalink")def
```


Std.DHashMap.map.{u, v, w} {α : Type u} {β : α → Type v}
  {δ : α → Type w} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (f : (a : α) → β a → δ a)
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α δ


Std.DHashMap.map.{u, v, w} {α : Type u}
  {β : α → Type v} {δ : α → Type w}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (f : (a : α) → β a → δ a)
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) :
  [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α δ


```

Updates the values of the hash map by applying the given function to all mappings.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.fold "Permalink")def
```


Std.DHashMap.fold.{u, v, w} {α : Type u} {β : α → Type v} {δ : Type w}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (f : δ → (a : α) → β a → δ) (init : δ)
  (b : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : δ


Std.DHashMap.fold.{u, v, w} {α : Type u}
  {β : α → Type v} {δ : Type w}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (f : δ → (a : α) → β a → δ) (init : δ)
  (b : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : δ


```

Folds the given function over the mappings in the hash map in some order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.foldM "Permalink")def
```


Std.DHashMap.foldM.{u, v, w, w'} {α : Type u} {β : α → Type v}
  {δ : Type w} {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (f : δ → (a : α) → β a → m δ) (init : δ)
  (b : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : m δ


Std.DHashMap.foldM.{u, v, w, w'}
  {α : Type u} {β : α → Type v}
  {δ : Type w} {m : Type w → Type w'}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (f : δ → (a : α) → β a → m δ) (init : δ)
  (b : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : m δ


```

Monadically computes a value by folding the given function over the mappings in the hash map in some order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.forIn "Permalink")def
```


Std.DHashMap.forIn.{u, v, w, w'} {α : Type u} {β : α → Type v}
  {δ : Type w} {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (f : (a : α) → β a → δ → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") δ))
  (init : δ) (b : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : m δ


Std.DHashMap.forIn.{u, v, w, w'}
  {α : Type u} {β : α → Type v}
  {δ : Type w} {m : Type w → Type w'}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (f :
    (a : α) → β a → δ → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") δ))
  (init : δ) (b : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : m δ


```

Support for the `for` loop construct in `do` blocks.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.forM "Permalink")def
```


Std.DHashMap.forM.{u, v, w, w'} {α : Type u} {β : α → Type v}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (f : (a : α) → β a → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) (b : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


Std.DHashMap.forM.{u, v, w, w'}
  {α : Type u} {β : α → Type v}
  {m : Type w → Type w'} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (f : (a : α) → β a → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit"))
  (b : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Carries out a monadic action on each mapping in the hash map in some order.
###  20.19.3.6. Conversion[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Dependent-Hash-Maps--Conversion "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.ofList "Permalink")def
```


Std.DHashMap.ofList.{u, v} {α : Type u} {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ((a : α) × β a)) : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


Std.DHashMap.ofList.{u, v} {α : Type u}
  {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ((a : α) × β a)) :
  [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β


```

Creates a hash map from a list of mappings. If the same key appears multiple times, the last occurrence takes precedence.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.toArray "Permalink")def
```


Std.DHashMap.toArray.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ((a : α) × β a)


Std.DHashMap.toArray.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ((a : α) × β a)


```

Transforms the hash map into an array of mappings in some order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.toList "Permalink")def
```


Std.DHashMap.toList.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ((a : α) × β a)


Std.DHashMap.toList.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.DHashMap](Basic-Types/Maps-and-Sets/#Std___DHashMap "Documentation for Std.DHashMap") α β) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ((a : α) × β a)


```

Transforms the hash map into a list of mappings in some order.
###  20.19.3.7. Unbundled Variants[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Dependent-Hash-Maps--Unbundled-Variants "Permalink")
Unbundled maps separate well-formedness proofs from data. This is primarily useful when defining [nested inductive types](Basic-Types/Maps-and-Sets/#raw-data). To use these variants, import the modules `Std.DHashMap.Raw` and `Std.DHashMap.RawLemmas`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.Raw "Permalink")structure
```


Std.DHashMap.Raw.{u, v} (α : Type u) (β : α → Type v) : Type (max u v)


Std.DHashMap.Raw.{u, v} (α : Type u)
  (β : α → Type v) : Type (max u v)


```

Dependent hash maps without a bundled well-formedness invariant, suitable for use in nested inductive types. The well-formedness invariant is called `Raw.WF`. When in doubt, prefer `DHashMap` over `DHashMap.Raw`. Lemmas about the operations on `Std.Data.DHashMap.Raw` are available in the module `Std.Data.DHashMap.RawLemmas`.
The hash table is backed by an `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")`. Users should make sure that the hash map is used linearly to avoid expensive copies.
This is a simple separate-chaining hash table. The data of the hash map consists of a cached size and an array of buckets, where each bucket is a linked list of key-value pairs. The number of buckets is always a power of two. The hash map doubles its size upon inserting an element such that the number of elements is more than 75% of the number of buckets.
The hash map uses `==` (provided by the `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` typeclass) to compare keys and `[hash](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable.hash")` (provided by the `[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable")` typeclass) to hash them. To ensure that the operations behave as expected, `==` should be an equivalence relation and `a == b` should imply `hash a = hash b` (see also the `[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq")` and `[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable")` typeclasses). Both of these conditions are automatic if the BEq instance is lawful, i.e., if `a == b` implies `a = b`.
#  Constructor

```
[Std.DHashMap.Raw.mk](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw.mk").{u, v}
```

#  Fields

```
size : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

The number of mappings present in the hash map

```
buckets : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") (Std.DHashMap.Internal.AssocList α β)
```

Internal implementation detail of the hash map
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DHashMap.Raw.WF.containsThenInsertIfNew%E2%82%80 "Permalink")inductive predicate
```


Std.DHashMap.Raw.WF.{u, v} {α : Type u} {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] : [Std.DHashMap.Raw](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw") α β → Prop


Std.DHashMap.Raw.WF.{u, v} {α : Type u}
  {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] :
  [Std.DHashMap.Raw](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw") α β → Prop


```

Well-formedness predicate for hash maps. Users of `DHashMap` will not need to interact with this. Users of `DHashMap.Raw` will need to provide proofs of `WF` to lemmas and should use lemmas like `WF.empty` and `WF.insert` (which are always named exactly like the operations they are about) to show that map operations preserve well-formedness. The constructors of this type are internal implementation details and should not be accessed by users.
#  Constructors

```
wf.{u, v} {α : Type u} {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  {m : [Std.DHashMap.Raw](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw") α β} :
  0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") m.[buckets](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw.buckets").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") →
    (∀ [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α],
        Std.DHashMap.Internal.Raw.WFImp m) →
      m.[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF")
```

Internal implementation detail of the hash map

```
emptyWithCapacity₀.{u, v} {α : Type u} {β : α → Type v}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] {c : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")} :
  (Std.DHashMap.Internal.Raw₀.emptyWithCapacity c).[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF")
```

Internal implementation detail of the hash map

```
insert₀.{u, v} {α : Type u} {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] {m : [Std.DHashMap.Raw](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw") α β}
  {h : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") m.[buckets](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw.buckets").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")} {a : α} {b : β a} :
  m.[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF") →
    (Std.DHashMap.Internal.Raw₀.insert [⟨](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk")m[,](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") h[⟩](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") a b).[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF")
```

Internal implementation detail of the hash map

```
containsThenInsert₀.{u, v} {α : Type u} {β : α → Type v}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] {m : [Std.DHashMap.Raw](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw") α β}
  {h : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") m.[buckets](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw.buckets").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")} {a : α} {b : β a} :
  m.[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF") →
    (Std.DHashMap.Internal.Raw₀.containsThenInsert [⟨](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk")m[,](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") h[⟩](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") a
            b).[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd").[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF")
```

Internal implementation detail of the hash map

```
containsThenInsertIfNew₀.{u, v} {α : Type u}
  {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  {m : [Std.DHashMap.Raw](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw") α β} {h : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") m.[buckets](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw.buckets").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")}
  {a : α} {b : β a} :
  m.[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF") →
    (Std.DHashMap.Internal.Raw₀.containsThenInsertIfNew
            [⟨](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk")m[,](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") h[⟩](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") a b).[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd").[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF")
```

Internal implementation detail of the hash map

```
erase₀.{u, v} {α : Type u} {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] {m : [Std.DHashMap.Raw](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw") α β}
  {h : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") m.[buckets](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw.buckets").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")} {a : α} :
  m.[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF") → (Std.DHashMap.Internal.Raw₀.erase [⟨](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk")m[,](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") h[⟩](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") a).[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF")
```

Internal implementation detail of the hash map

```
insertIfNew₀.{u, v} {α : Type u} {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] {m : [Std.DHashMap.Raw](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw") α β}
  {h : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") m.[buckets](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw.buckets").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")} {a : α} {b : β a} :
  m.[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF") →
    (Std.DHashMap.Internal.Raw₀.insertIfNew [⟨](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk")m[,](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") h[⟩](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") a
          b).[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF")
```

Internal implementation detail of the hash map

```
getThenInsertIfNew?₀.{u, v} {α : Type u} {β : α → Type v}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α]
  {m : [Std.DHashMap.Raw](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw") α β} {h : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") m.[buckets](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw.buckets").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")}
  {a : α} {b : β a} :
  m.[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF") →
    (Std.DHashMap.Internal.Raw₀.getThenInsertIfNew? [⟨](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk")m[,](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") h[⟩](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") a
            b).[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd").[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF")
```

Internal implementation detail of the hash map

```
filter₀.{u, v} {α : Type u} {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] {m : [Std.DHashMap.Raw](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw") α β}
  {h : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") m.[buckets](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw.buckets").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")} {f : (a : α) → β a → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")} :
  m.[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF") → (Std.DHashMap.Internal.Raw₀.filter f [⟨](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk")m[,](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") h[⟩](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk")).[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF")
```

Internal implementation detail of the hash map

```
constGetThenInsertIfNew?₀.{u, v} {α : Type u} {β : Type v}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] {m : [Std.DHashMap.Raw](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw") α fun x => β}
  {h : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") m.[buckets](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw.buckets").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")} {a : α} {b : β} :
  m.[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF") →
    (Std.DHashMap.Internal.Raw₀.Const.getThenInsertIfNew?
            [⟨](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk")m[,](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") h[⟩](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") a b).[snd](Basic-Types/Tuples/#Prod___mk "Documentation for Prod.snd").[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF")
```

Internal implementation detail of the hash map

```
modify₀.{u, v} {α : Type u} {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α] {m : [Std.DHashMap.Raw](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw") α β}
  {h : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") m.[buckets](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw.buckets").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")} {a : α} {f : β a → β a} :
  m.[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF") →
    (Std.DHashMap.Internal.Raw₀.modify [⟨](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk")m[,](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") h[⟩](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") a f).[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF")
```

Internal implementation detail of the hash map

```
constModify₀.{u, v} {α : Type u} {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] {m : [Std.DHashMap.Raw](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw") α fun x => β}
  {h : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") m.[buckets](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw.buckets").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")} {a : α} {f : β → β} :
  m.[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF") →
    (Std.DHashMap.Internal.Raw₀.Const.modify [⟨](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk")m[,](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") h[⟩](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") a
          f).[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF")
```

Internal implementation detail of the hash map

```
alter₀.{u, v} {α : Type u} {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α] {m : [Std.DHashMap.Raw](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw") α β}
  {h : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") m.[buckets](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw.buckets").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")} {a : α}
  {f : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a) → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a)} :
  m.[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF") →
    (Std.DHashMap.Internal.Raw₀.alter [⟨](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk")m[,](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") h[⟩](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") a f).[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF")
```

Internal implementation detail of the hash map

```
constAlter₀.{u, v} {α : Type u} {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] {m : [Std.DHashMap.Raw](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw") α fun x => β}
  {h : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") m.[buckets](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw.buckets").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")} {a : α}
  {f : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β} :
  m.[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF") →
    (Std.DHashMap.Internal.Raw₀.Const.alter [⟨](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk")m[,](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") h[⟩](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") a
          f).[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF")
```

Internal implementation detail of the hash map

```
inter₀.{u, v} {α : Type u} {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] {m₁ m₂ : [Std.DHashMap.Raw](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw") α β}
  {h₁ : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") m₁.[buckets](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw.buckets").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")} {h₂ : 0 [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") m₂.[buckets](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw.buckets").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")} :
  m₁.[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF") →
    m₂.[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF") →
      (Std.DHashMap.Internal.Raw₀.inter [⟨](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk")m₁[,](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") h₁[⟩](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk")
            [⟨](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk")m₂[,](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk") h₂[⟩](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.mk")).[val](Basic-Types/Subtypes/#Subtype___mk "Documentation for Subtype.val").[WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF")
```

Internal implementation detail of the hash map
##  20.19.4. Extensional Hash Maps[🔗](find/?domain=Verso.Genre.Manual.section&name=ExtHashMap "Permalink")
The declarations in this section should be imported using `import Std.ExtHashMap`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap "Permalink")structure
```


Std.ExtHashMap.{u, v} (α : Type u) (β : Type v) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] :
  Type (max u v)


Std.ExtHashMap.{u, v} (α : Type u)
  (β : Type v) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] :
  Type (max u v)


```

Hash maps.
This is a simple separate-chaining hash table. The data of the hash map consists of a cached size and an array of buckets, where each bucket is a linked list of key-value pairs. The number of buckets is always a power of two. The hash map doubles its size upon inserting an element such that the number of elements is more than 75% of the number of buckets.
The hash table is backed by an `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")`. Users should make sure that the hash map is used linearly to avoid expensive copies.
The hash map uses `==` (provided by the `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` typeclass) to compare keys and `[hash](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable.hash")` (provided by the `[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable")` typeclass) to hash them. To ensure that the operations behave as expected, `==` should be an equivalence relation and `a == b` should imply `hash a = hash b` (see also the `[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq")` and `[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable")` typeclasses). Both of these conditions are automatic if the BEq instance is lawful, i.e., if `a == b` implies `a = b`.
In contrast to regular hash maps, `[Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap")` offers several extensionality lemmas and therefore has more lemmas about equality of hash maps. This however also makes it lose the ability to iterate freely over hash maps.
These hash maps contain a bundled well-formedness invariant, which means that they cannot be used in nested inductive types. For these use cases, `[Std.HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw")` and `[Std.HashMap.Raw.WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")` unbundle the invariant from the hash map. When in doubt, prefer `HashMap` or `ExtHashMap` over `HashMap.Raw`.
Dependent hash maps, in which keys may occur in their values' types, are available as `[Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap")` in the module `Std.Data.ExtDHashMap`.
###  20.19.4.1. Creation[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Extensional-Hash-Maps--Creation "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.emptyWithCapacity "Permalink")def
```


Std.ExtHashMap.emptyWithCapacity.{u, v} {α : Type u} {β : Type v}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (capacity : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 8) : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


Std.ExtHashMap.emptyWithCapacity.{u, v}
  {α : Type u} {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (capacity : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 8) :
  [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


```

Creates a new empty hash map. The optional parameter `capacity` can be supplied to presize the map so that it can hold the given number of mappings without reallocating. It is also possible to use the empty collection notations `∅` and `{}` to create an empty hash map with the default capacity.
###  20.19.4.2. Properties[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Extensional-Hash-Maps--Properties "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.size "Permalink")def
```


Std.ExtHashMap.size.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Std.ExtHashMap.size.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of mappings present in the hash map
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.isEmpty "Permalink")def
```


Std.ExtHashMap.isEmpty.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.ExtHashMap.isEmpty.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the hash map contains no mappings.
Note that if your `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` instance is not reflexive or your `[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable")` instance is not lawful, then it is possible that this function returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` even though is not possible to get anything out of the hash map.
###  20.19.4.3. Queries[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Extensional-Hash-Maps--Queries "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.contains "Permalink")def
```


Std.ExtHashMap.contains.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.ExtHashMap.contains.{u, v}
  {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if there is a mapping for the given key. There is also a `Prop`-valued version of this: `a ∈ m` is equivalent to `m.[contains](Basic-Types/Maps-and-Sets/#Std___ExtHashMap___contains "Documentation for Std.ExtHashMap.contains") a = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Observe that this is different behavior than for lists: for lists, `∈` uses `=` and `contains` uses `==` for comparisons, while for hash maps, both use `==`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.get "Permalink")def
```


Std.ExtHashMap.get.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) (h : a ∈ m) : β


Std.ExtHashMap.get.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α)
  (h : a ∈ m) : β


```

The notation `m[a]` or `m[a]'h` is preferred over calling this function directly.
Retrieves the mapping for the given key. Ensures that such a mapping exists by requiring a proof of `a ∈ m`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.get! "Permalink")def
```


Std.ExtHashMap.get!.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") β]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) : β


Std.ExtHashMap.get!.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") β]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) : β


```

The notation `m[a]!` is preferred over calling this function directly.
Tries to retrieve the mapping for the given key, panicking if no such mapping is present.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.get? "Permalink")def
```


Std.ExtHashMap.get?.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


Std.ExtHashMap.get?.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


```

The notation `m[a]?` is preferred over calling this function directly.
Tries to retrieve the mapping for the given key, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such mapping is present.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.getD "Permalink")def
```


Std.ExtHashMap.getD.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) (fallback : β) : β


Std.ExtHashMap.getD.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α)
  (fallback : β) : β


```

Tries to retrieve the mapping for the given key, returning `fallback` if no such mapping is present.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.getKey "Permalink")def
```


Std.ExtHashMap.getKey.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) (h : a ∈ m) : α


Std.ExtHashMap.getKey.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α)
  (h : a ∈ m) : α


```

Retrieves the key from the mapping that matches `a`. Ensures that such a mapping exists by requiring a proof of `a ∈ m`. The result is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.getKey! "Permalink")def
```


Std.ExtHashMap.getKey!.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) : α


Std.ExtHashMap.getKey!.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) : α


```

Checks if a mapping for the given key exists and returns the key if it does, otherwise panics. If no panic occurs the result is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.getKey? "Permalink")def
```


Std.ExtHashMap.getKey?.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.ExtHashMap.getKey?.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Checks if a mapping for the given key exists and returns the key if it does, otherwise `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`. The result in the `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` case is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.getKeyD "Permalink")def
```


Std.ExtHashMap.getKeyD.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a fallback : α) : α


Std.ExtHashMap.getKeyD.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β)
  (a fallback : α) : α


```

Checks if a mapping for the given key exists and returns the key if it does, otherwise `fallback`. If a mapping exists the result is guaranteed to be pointer equal to the key in the map.
###  20.19.4.4. Modification[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Extensional-Hash-Maps--Modification "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.alter "Permalink")def
```


Std.ExtHashMap.alter.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) (f : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β) :
  [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


Std.ExtHashMap.alter.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α)
  (f : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β) :
  [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


```

Modifies in place the value associated with a given key, allowing creating new values and deleting values via an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` valued replacement function.
This function ensures that the value is used linearly.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.modify "Permalink")def
```


Std.ExtHashMap.modify.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) (f : β → β) : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


Std.ExtHashMap.modify.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α)
  (f : β → β) : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


```

Modifies in place the value associated with a given key.
This function ensures that the value is used linearly.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.containsThenInsert "Permalink")def
```


Std.ExtHashMap.containsThenInsert.{u, v} {α : Type u} {β : Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) (b : β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


Std.ExtHashMap.containsThenInsert.{u, v}
  {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α)
  (b : β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


```

Checks whether a key is present in a map, and unconditionally inserts a value for the key.
Equivalent to (but potentially faster than) calling `contains` followed by `insert`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.containsThenInsertIfNew "Permalink")def
```


Std.ExtHashMap.containsThenInsertIfNew.{u, v} {α : Type u} {β : Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) (b : β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


Std.ExtHashMap.containsThenInsertIfNew.{u,
    v}
  {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α)
  (b : β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


```

Checks whether a key is present in a map and inserts a value for the key if it was not found.
If the returned `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, then the returned map is unaltered. If the `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, then the returned map has a new value inserted.
Equivalent to (but potentially faster than) calling `contains` followed by `insertIfNew`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.erase "Permalink")def
```


Std.ExtHashMap.erase.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


Std.ExtHashMap.erase.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) :
  [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


```

Removes the mapping for the given key if it exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.filter "Permalink")def
```


Std.ExtHashMap.filter.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] (f : α → β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


Std.ExtHashMap.filter.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] (f : α → β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) :
  [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


```

Removes all mappings of the hash map for which the given function returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.filterMap "Permalink")def
```


Std.ExtHashMap.filterMap.{u, v, w} {α : Type u} {β : Type v}
  {γ : Type w} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] (f : α → β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ) (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) :
  [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α γ


Std.ExtHashMap.filterMap.{u, v, w}
  {α : Type u} {β : Type v} {γ : Type w}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (f : α → β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ)
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) :
  [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α γ


```

Updates the values of the hash map by applying the given function to all mappings, keeping only those mappings where the function returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.insert "Permalink")def
```


Std.ExtHashMap.insert.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) (b : β) : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


Std.ExtHashMap.insert.{u, v} {α : Type u}
  {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α)
  (b : β) : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


```

Inserts the given mapping into the map. If there is already a mapping for the given key, then both key and value will be replaced.
Note: this replacement behavior is true for `HashMap`, `DHashMap`, `HashMap.Raw` and `DHashMap.Raw`. The `insert` function on `HashSet` and `HashSet.Raw` behaves differently: it will return the set unchanged if a matching key is already present.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.insertIfNew "Permalink")def
```


Std.ExtHashMap.insertIfNew.{u, v} {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) (b : β) : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


Std.ExtHashMap.insertIfNew.{u, v}
  {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α)
  (b : β) : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


```

If there is no mapping for the given key, inserts the given mapping into the map. Otherwise, returns the map unaltered.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.getThenInsertIfNew? "Permalink")def
```


Std.ExtHashMap.getThenInsertIfNew?.{u, v} {α : Type u} {β : Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α) (b : β) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


Std.ExtHashMap.getThenInsertIfNew?.{u, v}
  {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (a : α)
  (b : β) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


```

Checks whether a key is present in a map, returning the associated value, and inserts a value for the key if it was not found.
If the returned value is `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v`, then the returned map is unaltered. If it is `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, then the returned map has a new value inserted.
Equivalent to (but potentially faster than) calling `get?` followed by `insertIfNew`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.insertMany "Permalink")def
```


Std.ExtHashMap.insertMany.{u, v, w} {α : Type u} {β : Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  {ρ : Type w} [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")] (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (l : ρ) :
  [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


Std.ExtHashMap.insertMany.{u, v, w}
  {α : Type u} {β : Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] {ρ : Type w}
  [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) (l : ρ) :
  [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


```

Inserts multiple mappings into the hash map by iterating over the given collection and calling `insert`. If the same key appears multiple times, the last occurrence takes precedence.
Note: this precedence behavior is true for `HashMap`, `DHashMap`, `HashMap.Raw` and `DHashMap.Raw`. The `insertMany` function on `HashSet` and `HashSet.Raw` behaves differently: it will prefer the first appearance.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.insertManyIfNewUnit "Permalink")def
```


Std.ExtHashMap.insertManyIfNewUnit.{u, w} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] {ρ : Type w}
  [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ α] (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")) (l : ρ) :
  [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


Std.ExtHashMap.insertManyIfNewUnit.{u, w}
  {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] {ρ : Type w}
  [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ α]
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")) (l : ρ) :
  [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Inserts multiple keys with the value `()` into the hash map by iterating over the given collection and calling `insertIfNew`. If the same key appears multiple times, the first occurrence takes precedence.
This is mainly useful to implement `HashSet.insertMany`, so if you are considering using this, `HashSet` or `HashSet.Raw` might be a better fit for you.
###  20.19.4.5. Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Extensional-Hash-Maps--Iteration "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.map "Permalink")def
```


Std.ExtHashMap.map.{u, v, w} {α : Type u} {β : Type v} {γ : Type w}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (f : α → β → γ) (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α γ


Std.ExtHashMap.map.{u, v, w} {α : Type u}
  {β : Type v} {γ : Type w} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] (f : α → β → γ)
  (m : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β) :
  [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α γ


```

Updates the values of the hash map by applying the given function to all mappings.
###  20.19.4.6. Conversion[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Extensional-Hash-Maps--Conversion "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.ofList "Permalink")def
```


Std.ExtHashMap.ofList.{u, v} {α : Type u} {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")) : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


Std.ExtHashMap.ofList.{u, v} {α : Type u}
  {β : Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")) : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α β


```

Creates a hash map from a list of mappings. If the same key appears multiple times, the last occurrence takes precedence.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.unitOfArray "Permalink")def
```


Std.ExtHashMap.unitOfArray.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (l : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


Std.ExtHashMap.unitOfArray.{u}
  {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (l : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Creates a hash map from an array of keys, associating the value `()` with each key.
This is mainly useful to implement `HashSet.ofArray`, so if you are considering using this, `HashSet` or `HashSet.Raw` might be a better fit for you.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashMap.unitOfList "Permalink")def
```


Std.ExtHashMap.unitOfList.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


Std.ExtHashMap.unitOfList.{u} {α : Type u}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")


```

Creates a hash map from a list of keys, associating the value `()` with each key.
This is mainly useful to implement `HashSet.ofList`, so if you are considering using this, `HashSet` or `HashSet.Raw` might be a better fit for you.
##  20.19.5. Extensional Dependent Hash Maps[🔗](find/?domain=Verso.Genre.Manual.section&name=ExtDHashMap "Permalink")
The declarations in this section should be imported using `import Std.ExtDHashMap`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap "Permalink")structure
```


Std.ExtDHashMap.{u, v} (α : Type u) (β : α → Type v) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] : Type (max u v)


Std.ExtDHashMap.{u, v} (α : Type u)
  (β : α → Type v) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] :
  Type (max u v)


```

Extensional dependent hash maps.
This is a simple separate-chaining hash table. The data of the hash map consists of a cached size and an array of buckets, where each bucket is a linked list of key-value pairs. The number of buckets is always a power of two. The hash map doubles its size upon inserting an element such that the number of elements is more than 75% of the number of buckets.
The hash table is backed by an `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")`. Users should make sure that the hash map is used linearly to avoid expensive copies.
The hash map uses `==` (provided by the `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` typeclass) to compare keys and `[hash](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable.hash")` (provided by the `[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable")` typeclass) to hash them. To ensure that the operations behave as expected, `==` must be an equivalence relation and `a == b` must imply `hash a = hash b` (see also the `[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq")` and `[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable")` typeclasses). Both of these conditions are automatic if the BEq instance is lawful, i.e., if `a == b` implies `a = b`.
In contrast to regular dependent hash maps, `[Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap")` offers several extensionality lemmas and therefore has more lemmas about equality of hash maps. This however also makes it lose the ability to iterate freely over the hash map.
These hash maps contain a bundled well-formedness invariant, which means that they cannot be used in nested inductive types. For these use cases, `[Std.DHashMap.Raw](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___mk "Documentation for Std.DHashMap.Raw")` and `[Std.DHashMap.Raw.WF](Basic-Types/Maps-and-Sets/#Std___DHashMap___Raw___WF___wf "Documentation for Std.DHashMap.Raw.WF")` unbundle the invariant from the hash map. When in doubt, prefer `DHashMap` over `DHashMap.Raw`.
###  20.19.5.1. Creation[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Extensional-Dependent-Hash-Maps--Creation "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.emptyWithCapacity "Permalink")def
```


Std.ExtDHashMap.emptyWithCapacity.{u, v} {α : Type u} {β : α → Type v}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (capacity : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 8) : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


Std.ExtDHashMap.emptyWithCapacity.{u, v}
  {α : Type u} {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (capacity : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 8) :
  [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


```

Creates a new empty hash map. The optional parameter `capacity` can be supplied to presize the map so that it can hold the given number of mappings without reallocating. It is also possible to use the empty collection notations `∅` and `{}` to create an empty hash map with the default capacity.
###  20.19.5.2. Properties[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Extensional-Dependent-Hash-Maps--Properties "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.size "Permalink")def
```


Std.ExtDHashMap.size.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Std.ExtDHashMap.size.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of mappings present in the hash map
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.isEmpty "Permalink")def
```


Std.ExtDHashMap.isEmpty.{u, v} {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.ExtDHashMap.isEmpty.{u, v}
  {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the hash map contains no mappings.
Note that if your `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` instance is not reflexive or your `[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable")` instance is not lawful, then it is possible that this function returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` even though is not possible to get anything out of the hash map.
###  20.19.5.3. Queries[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Extensional-Dependent-Hash-Maps--Queries "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.contains "Permalink")def
```


Std.ExtDHashMap.contains.{u, v} {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.ExtDHashMap.contains.{u, v}
  {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if there is a mapping for the given key. There is also a `Prop`-valued version of this: `a ∈ m` is equivalent to `m.[contains](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap___contains "Documentation for Std.ExtDHashMap.contains") a = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Observe that this is different behavior than for lists: for lists, `∈` uses `=` and `contains` uses `==` for comparisons, while for hash maps, both use `==`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.get "Permalink")def
```


Std.ExtDHashMap.get.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α] (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α)
  (h : a ∈ m) : β a


Std.ExtDHashMap.get.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α)
  (h : a ∈ m) : β a


```

Retrieves the mapping for the given key. Ensures that such a mapping exists by requiring a proof of `a ∈ m`.
Uses the `[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq")` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.get! "Permalink")def
```


Std.ExtDHashMap.get!.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α] (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α)
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") (β a)] : β a


Std.ExtDHashMap.get!.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α)
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") (β a)] : β a


```

Tries to retrieve the mapping for the given key, panicking if no such mapping is present.
Uses the `[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq")` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.get? "Permalink")def
```


Std.ExtDHashMap.get?.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α] (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a)


Std.ExtDHashMap.get?.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a)


```

Tries to retrieve the mapping for the given key, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such mapping is present.
Uses the `[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq")` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.getD "Permalink")def
```


Std.ExtDHashMap.getD.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α] (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α)
  (fallback : β a) : β a


Std.ExtDHashMap.getD.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α)
  (fallback : β a) : β a


```

Tries to retrieve the mapping for the given key, returning `fallback` if no such mapping is present.
Uses the `[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq")` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.getKey "Permalink")def
```


Std.ExtDHashMap.getKey.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α) (h : a ∈ m) : α


Std.ExtDHashMap.getKey.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α)
  (h : a ∈ m) : α


```

Retrieves the key from the mapping that matches `a`. Ensures that such a mapping exists by requiring a proof of `a ∈ m`. The result is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.getKey! "Permalink")def
```


Std.ExtDHashMap.getKey!.{u, v} {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α) : α


Std.ExtDHashMap.getKey!.{u, v}
  {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β)
  (a : α) : α


```

Checks if a mapping for the given key exists and returns the key if it does, otherwise panics. If no panic occurs the result is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.getKey? "Permalink")def
```


Std.ExtDHashMap.getKey?.{u, v} {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.ExtDHashMap.getKey?.{u, v}
  {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Checks if a mapping for the given key exists and returns the key if it does, otherwise `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`. The result in the `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` case is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.getKeyD "Permalink")def
```


Std.ExtDHashMap.getKeyD.{u, v} {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a fallback : α) : α


Std.ExtDHashMap.getKeyD.{u, v}
  {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β)
  (a fallback : α) : α


```

Checks if a mapping for the given key exists and returns the key if it does, otherwise `fallback`. If a mapping exists the result is guaranteed to be pointer equal to the key in the map.
###  20.19.5.4. Modification[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Extensional-Dependent-Hash-Maps--Modification "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.alter "Permalink")def
```


Std.ExtDHashMap.alter.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α] (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α)
  (f : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a) → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a)) : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


Std.ExtDHashMap.alter.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α)
  (f : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a) → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a)) :
  [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


```

Modifies in place the value associated with a given key, allowing creating new values and deleting values via an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` valued replacement function.
This function ensures that the value is used linearly.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.modify "Permalink")def
```


Std.ExtDHashMap.modify.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α] (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α)
  (f : β a → β a) : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


Std.ExtDHashMap.modify.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α)
  (f : β a → β a) : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


```

Modifies in place the value associated with a given key.
This function ensures that the value is used linearly.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.containsThenInsert "Permalink")def
```


Std.ExtDHashMap.containsThenInsert.{u, v} {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α) (b : β a) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


Std.ExtDHashMap.containsThenInsert.{u, v}
  {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α)
  (b : β a) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


```

Checks whether a key is present in a map, and unconditionally inserts a value for the key.
Equivalent to (but potentially faster than) calling `contains` followed by `insert`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.containsThenInsertIfNew "Permalink")def
```


Std.ExtDHashMap.containsThenInsertIfNew.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α) (b : β a) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


Std.ExtDHashMap.containsThenInsertIfNew.{u,
    v}
  {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α)
  (b : β a) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


```

Checks whether a key is present in a map and inserts a value for the key if it was not found.
If the returned `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, then the returned map is unaltered. If the `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, then the returned map has a new value inserted.
Equivalent to (but potentially faster than) calling `contains` followed by `insertIfNew`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.erase "Permalink")def
```


Std.ExtDHashMap.erase.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α) : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


Std.ExtDHashMap.erase.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α) :
  [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


```

Removes the mapping for the given key if it exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.filter "Permalink")def
```


Std.ExtDHashMap.filter.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (f : (a : α) → β a → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) :
  [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


Std.ExtDHashMap.filter.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (f : (a : α) → β a → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) :
  [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


```

Removes all mappings of the hash map for which the given function returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.filterMap "Permalink")def
```


Std.ExtDHashMap.filterMap.{u, v, w} {α : Type u} {β : α → Type v}
  {γ : α → Type w} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] (f : (a : α) → β a → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (γ a))
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α γ


Std.ExtDHashMap.filterMap.{u, v, w}
  {α : Type u} {β : α → Type v}
  {γ : α → Type w} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (f : (a : α) → β a → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (γ a))
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) :
  [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α γ


```

Updates the values of the hash map by applying the given function to all mappings, keeping only those mappings where the function returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.insert "Permalink")def
```


Std.ExtDHashMap.insert.{u, v} {α : Type u} {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α) (b : β a) : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


Std.ExtDHashMap.insert.{u, v} {α : Type u}
  {β : α → Type v} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α)
  (b : β a) : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


```

Inserts the given mapping into the map. If there is already a mapping for the given key, then both key and value will be replaced.
Note: this replacement behavior is true for `HashMap`, `DHashMap`, `HashMap.Raw` and `DHashMap.Raw`. The `insert` function on `HashSet` and `HashSet.Raw` behaves differently: it will return the set unchanged if a matching key is already present.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.insertIfNew "Permalink")def
```


Std.ExtDHashMap.insertIfNew.{u, v} {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α) (b : β a) : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


Std.ExtDHashMap.insertIfNew.{u, v}
  {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α)
  (b : β a) : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


```

If there is no mapping for the given key, inserts the given mapping into the map. Otherwise, returns the map unaltered.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.getThenInsertIfNew? "Permalink")def
```


Std.ExtDHashMap.getThenInsertIfNew?.{u, v} {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (a : α) (b : β a) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a) [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


Std.ExtDHashMap.getThenInsertIfNew?.{u, v}
  {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq") α] (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β)
  (a : α) (b : β a) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a) [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


```

Checks whether a key is present in a map, returning the associated value, and inserts a value for the key if it was not found.
If the returned value is `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v`, then the returned map is unaltered. If it is `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, then the returned map has a new value inserted.
Equivalent to (but potentially faster than) calling `get?` followed by `insertIfNew`.
Uses the `[LawfulBEq](Type-Classes/Basic-Classes/#LawfulBEq___mk "Documentation for LawfulBEq")` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.insertMany "Permalink")def
```


Std.ExtDHashMap.insertMany.{u, v, w} {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  {ρ : Type w} [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ ((a : α) × β a)] (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β)
  (l : ρ) : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


Std.ExtDHashMap.insertMany.{u, v, w}
  {α : Type u} {β : α → Type v}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  {ρ : Type w}
  [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ ((a : α) × β a)]
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) (l : ρ) :
  [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


```

Inserts multiple mappings into the hash map by iterating over the given collection and calling `insert`. If the same key appears multiple times, the last occurrence takes precedence.
Note: this precedence behavior is true for `HashMap`, `DHashMap`, `HashMap.Raw` and `DHashMap.Raw`. The `insertMany` function on `HashSet` and `HashSet.Raw` behaves differently: it will prefer the first appearance.
###  20.19.5.5. Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Extensional-Dependent-Hash-Maps--Iteration "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.map "Permalink")def
```


Std.ExtDHashMap.map.{u, v, w} {α : Type u} {β : α → Type v}
  {γ : α → Type w} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] (f : (a : α) → β a → γ a)
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α γ


Std.ExtDHashMap.map.{u, v, w} {α : Type u}
  {β : α → Type v} {γ : α → Type w}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (f : (a : α) → β a → γ a)
  (m : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β) :
  [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α γ


```

Updates the values of the hash map by applying the given function to all mappings.
###  20.19.5.6. Conversion[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Extensional-Dependent-Hash-Maps--Conversion "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtDHashMap.ofList "Permalink")def
```


Std.ExtDHashMap.ofList.{u, v} {α : Type u} {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ((a : α) × β a)) : [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


Std.ExtDHashMap.ofList.{u, v} {α : Type u}
  {β : α → Type v} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ((a : α) × β a)) :
  [Std.ExtDHashMap](Basic-Types/Maps-and-Sets/#Std___ExtDHashMap "Documentation for Std.ExtDHashMap") α β


```

Creates a hash map from a list of mappings. If the same key appears multiple times, the last occurrence takes precedence.
##  20.19.6. Hash Sets[🔗](find/?domain=Verso.Genre.Manual.section&name=HashSet "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.mk "Permalink")structure
```


Std.HashSet.{u} (α : Type u) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] : Type u


Std.HashSet.{u} (α : Type u) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] : Type u


```

Hash sets.
This is a simple separate-chaining hash table. The data of the hash set consists of a cached size and an array of buckets, where each bucket is a linked list of keys. The number of buckets is always a power of two. The hash set doubles its size upon inserting an element such that the number of elements is more than 75% of the number of buckets.
The hash table is backed by an `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")`. Users should make sure that the hash set is used linearly to avoid expensive copies.
The hash set uses `==` (provided by the `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` typeclass) to compare elements and `[hash](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable.hash")` (provided by the `[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable")` typeclass) to hash them. To ensure that the operations behave as expected, `==` should be an equivalence relation and `a == b` should imply `hash a = hash b` (see also the `[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq")` and `[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable")` typeclasses). Both of these conditions are automatic if the BEq instance is lawful, i.e., if `a == b` implies `a = b`.
These hash sets contain a bundled well-formedness invariant, which means that they cannot be used in nested inductive types. For these use cases, `Std.Data.HashSet.Raw` and `Std.Data.HashSet.Raw.WF` unbundle the invariant from the hash set. When in doubt, prefer `HashSet` over `HashSet.Raw`.
#  Constructor

```
[Std.HashSet.mk](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet.mk").{u}
```

#  Fields

```
inner : [Std.HashMap](Basic-Types/Maps-and-Sets/#Std___HashMap "Documentation for Std.HashMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")
```

Internal implementation detail of the hash set.
###  20.19.6.1. Creation[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Hash-Sets--Creation "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.emptyWithCapacity "Permalink")def
```


Std.HashSet.emptyWithCapacity.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (capacity : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 8) : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


Std.HashSet.emptyWithCapacity.{u}
  {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (capacity : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 8) : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


```

Creates a new empty hash set. The optional parameter `capacity` can be supplied to presize the set so that it can hold the given number of elements without reallocating. It is also possible to use the empty collection notations `∅` and `{}` to create an empty hash set with the default capacity.
###  20.19.6.2. Properties[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Hash-Sets--Properties "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.isEmpty "Permalink")def
```


Std.HashSet.isEmpty.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.HashSet.isEmpty.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the hash set contains no elements.
Note that if your `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` instance is not reflexive or your `[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable")` instance is not lawful, then it is possible that this function returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` even though `m.[contains](Basic-Types/Maps-and-Sets/#Std___HashSet___contains "Documentation for Std.HashSet.contains") a = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` for all `a`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.size "Permalink")def
```


Std.HashSet.size.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Std.HashSet.size.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of elements present in the set
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.Equiv "Permalink")structure
```


Std.HashSet.Equiv.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m₁ m₂ : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : Prop


Std.HashSet.Equiv.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m₁ m₂ : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : Prop


```

Two hash sets are equivalent in the sense of `Equiv` iff all their values are equal.
#  Constructor

```
[Std.HashSet.Equiv.mk](Basic-Types/Maps-and-Sets/#Std___HashSet___Equiv___mk "Documentation for Std.HashSet.Equiv.mk").{u}
```

#  Fields

```
inner : m₁.[inner](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet.inner").[Equiv](Basic-Types/Maps-and-Sets/#Std___HashMap___Equiv___mk "Documentation for Std.HashMap.Equiv") m₂.[inner](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet.inner")
```

Internal implementation detail of the hash map
syntaxEquivalence
The relation `[HashSet.Equiv](Basic-Types/Maps-and-Sets/#Std___HashSet___Equiv___mk "Documentation for Std.HashSet.Equiv")` can also be written with an infix operator, which is scoped to its namespace:

```
term ::= ...
    | 


Two hash maps are equivalent in the sense of Equiv iff
all the keys and values are equal.


term ~m term
```

###  20.19.6.3. Queries[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Hash-Sets--Queries "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.contains "Permalink")def
```


Std.HashSet.contains.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.HashSet.contains.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the given key is present in the set. There is also a `Prop`-valued version of this: `a ∈ m` is equivalent to `m.[contains](Basic-Types/Maps-and-Sets/#Std___HashSet___contains "Documentation for Std.HashSet.contains") a = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Observe that this is different behavior than for lists: for lists, `∈` uses `=` and `contains` use `==` for comparisons, while for hash sets, both use `==`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.get "Permalink")def
```


Std.HashSet.get.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) (a : α) (h : a ∈ m) : α


Std.HashSet.get.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) (a : α)
  (h : a ∈ m) : α


```

Retrieves the key from the set that matches `a`. Ensures that such a key exists by requiring a proof of `a ∈ m`. The result is guaranteed to be pointer equal to the key in the set.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.get! "Permalink")def
```


Std.HashSet.get!.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) (a : α) : α


Std.HashSet.get!.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) (a : α) : α


```

Checks if given key is contained and returns the key if it is, otherwise panics. If no panic occurs the result is guaranteed to be pointer equal to the key in the set.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.get? "Permalink")def
```


Std.HashSet.get?.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) (a : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.HashSet.get?.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) (a : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Checks if given key is contained and returns the key if it is, otherwise `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`. The result in the `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` case is guaranteed to be pointer equal to the key in the set.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.getD "Permalink")def
```


Std.HashSet.getD.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) (a fallback : α) : α


Std.HashSet.getD.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α)
  (a fallback : α) : α


```

Checks if given key is contained and returns the key if it is, otherwise `fallback`. If they key is contained the result is guaranteed to be pointer equal to the key in the set.
###  20.19.6.4. Modification[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Hash-Sets--Modification "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.insert "Permalink")def
```


Std.HashSet.insert.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) (a : α) : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


Std.HashSet.insert.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) (a : α) :
  [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


```

Inserts the given element into the set. If the hash set already contains an element that is equal (with regard to `==`) to the given element, then the hash set is returned unchanged.
Note: this non-replacement behavior is true for `HashSet` and `HashSet.Raw`. The `insert` function on `HashMap`, `DHashMap`, `HashMap.Raw` and `DHashMap.Raw` behaves differently: it will overwrite an existing mapping.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.insertMany "Permalink")def
```


Std.HashSet.insertMany.{u, v} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} {ρ : Type v} [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ α] (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α)
  (l : ρ) : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


Std.HashSet.insertMany.{u, v} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  {ρ : Type v} [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ α]
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) (l : ρ) :
  [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


```

Inserts multiple mappings into the hash set by iterating over the given collection and calling `insert`. If the same key appears multiple times, the first occurrence takes precedence.
Note: this precedence behavior is true for `HashSet` and `HashSet.Raw`. The `insertMany` function on `HashMap`, `DHashMap`, `HashMap.Raw` and `DHashMap.Raw` behaves differently: it will prefer the last appearance.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.erase "Permalink")def
```


Std.HashSet.erase.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) (a : α) : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


Std.HashSet.erase.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) (a : α) :
  [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


```

Removes the element if it exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.filter "Permalink")def
```


Std.HashSet.filter.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (f : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


Std.HashSet.filter.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (f : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) :
  [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


```

Removes all elements from the hash set for which the given function returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.containsThenInsert "Permalink")def
```


Std.HashSet.containsThenInsert.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


Std.HashSet.containsThenInsert.{u}
  {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α)
  (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


```

Checks whether an element is present in a set and inserts the element if it was not found. If the hash set already contains an element that is equal (with regard to `==`) to the given element, then the hash set is returned unchanged.
Equivalent to (but potentially faster than) calling `contains` followed by `insert`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.partition "Permalink")def
```


Std.HashSet.partition.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (f : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


Std.HashSet.partition.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (f : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) :
  [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


```

Partition a hashset into two hashsets based on a predicate.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.union "Permalink")def
```


Std.HashSet.union.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m₁ m₂ : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


Std.HashSet.union.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (m₁ m₂ : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) :
  [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


```

Computes the union of the given hash sets.
This function always merges the smaller set into the larger set, so the expected runtime is `O(min(m₁.size, m₂.size))`.
###  20.19.6.5. Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Hash-Sets--Iteration "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.iter "Permalink")def
```


Std.HashSet.iter.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") α


Std.HashSet.iter.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") α


```

Returns a finite iterator over the elements of a hash set. The iterator yields the elements of the set in order and then terminates.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.all "Permalink")def
```


Std.HashSet.all.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.HashSet.all.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Check if all elements satisfy the predicate, short-circuiting if a predicate fails.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.any "Permalink")def
```


Std.HashSet.any.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.HashSet.any.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Check if any element satisfies the predicate, short-circuiting if a predicate succeeds.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.fold "Permalink")def
```


Std.HashSet.fold.{u, v} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  {β : Type v} (f : β → α → β) (init : β) (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : β


Std.HashSet.fold.{u, v} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  {β : Type v} (f : β → α → β) (init : β)
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : β


```

Folds the given function over the elements of the hash set in some order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.foldM "Permalink")def
```


Std.HashSet.foldM.{u, v, w} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {β : Type v} (f : β → α → m β)
  (init : β) (b : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : m β


Std.HashSet.foldM.{u, v, w} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {β : Type v} (f : β → α → m β)
  (init : β) (b : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : m β


```

Monadically computes a value by folding the given function over the elements in the hash set in some order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.forIn "Permalink")def
```


Std.HashSet.forIn.{u, v, w} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] {β : Type v}
  (f : α → β → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") β)) (init : β) (b : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : m β


Std.HashSet.forIn.{u, v, w} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  {β : Type v}
  (f : α → β → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") β)) (init : β)
  (b : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : m β


```

Support for the `for` loop construct in `do` blocks.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.forM "Permalink")def
```


Std.HashSet.forM.{u, v, w} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit"))
  (b : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


Std.HashSet.forM.{u, v, w} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  {m : Type v → Type w} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) (b : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) :
  m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Carries out a monadic action on each element in the hash set in some order.
###  20.19.6.6. Conversion[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Hash-Sets--Conversion "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.ofList "Permalink")def
```


Std.HashSet.ofList.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


Std.HashSet.ofList.{u} {α : Type u}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


```

Creates a hash set from a list of elements. Note that unlike repeatedly calling `insert`, if the collection contains multiple elements that are equal (with regard to `==`), then the last element in the collection will be present in the returned hash set.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.toList "Permalink")def
```


Std.HashSet.toList.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


Std.HashSet.toList.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Transforms the hash set into a list of elements in some order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.ofArray "Permalink")def
```


Std.HashSet.ofArray.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (l : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


Std.HashSet.ofArray.{u} {α : Type u}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (l : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) :
  [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α


```

Creates a hash set from an array of elements. Note that unlike repeatedly calling `insert`, if the collection contains multiple elements that are equal (with regard to `==`), then the last element in the collection will be present in the returned hash set.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.toArray "Permalink")def
```


Std.HashSet.toArray.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Std.HashSet.toArray.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  (m : [Std.HashSet](Basic-Types/Maps-and-Sets/#Std___HashSet___mk "Documentation for Std.HashSet") α) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Transforms the hash set into an array of elements in some order.
###  20.19.6.7. Unbundled Variants[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Hash-Sets--Unbundled-Variants "Permalink")
Unbundled maps separate well-formedness proofs from data. This is primarily useful when defining [nested inductive types](Basic-Types/Maps-and-Sets/#raw-data). To use these variants, import the modules `Std.HashSet.Raw` and `Std.HashSet.RawLemmas`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.Raw "Permalink")structure
```


Std.HashSet.Raw.{u} (α : Type u) : Type u


Std.HashSet.Raw.{u} (α : Type u) : Type u


```

Hash sets without a bundled well-formedness invariant, suitable for use in nested inductive types. The well-formedness invariant is called `Raw.WF`. When in doubt, prefer `HashSet` over `HashSet.Raw`. Lemmas about the operations on `Std.Data.HashSet.Raw` are available in the module `Std.Data.HashSet.RawLemmas`.
This is a simple separate-chaining hash table. The data of the hash set consists of a cached size and an array of buckets, where each bucket is a linked list of keys. The number of buckets is always a power of two. The hash set doubles its size upon inserting an element such that the number of elements is more than 75% of the number of buckets.
The hash table is backed by an `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")`. Users should make sure that the hash set is used linearly to avoid expensive copies.
The hash set uses `==` (provided by the `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` typeclass) to compare elements and `[hash](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable.hash")` (provided by the `[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable")` typeclass) to hash them. To ensure that the operations behave as expected, `==` should be an equivalence relation and `a == b` should imply `hash a = hash b` (see also the `[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq")` and `[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable")` typeclasses). Both of these conditions are automatic if the BEq instance is lawful, i.e., if `a == b` implies `a = b`.
#  Constructor

```
[Std.HashSet.Raw.mk](Basic-Types/Maps-and-Sets/#Std___HashSet___Raw___mk "Documentation for Std.HashSet.Raw.mk").{u}
```

#  Fields

```
inner : [Std.HashMap.Raw](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___mk "Documentation for Std.HashMap.Raw") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")
```

Internal implementation detail of the hash set.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.HashSet.Raw.WF "Permalink")structure
```


Std.HashSet.Raw.WF.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m : [Std.HashSet.Raw](Basic-Types/Maps-and-Sets/#Std___HashSet___Raw___mk "Documentation for Std.HashSet.Raw") α) : Prop


Std.HashSet.Raw.WF.{u} {α : Type u}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (m : [Std.HashSet.Raw](Basic-Types/Maps-and-Sets/#Std___HashSet___Raw___mk "Documentation for Std.HashSet.Raw") α) : Prop


```

Well-formedness predicate for hash sets. Users of `HashSet` will not need to interact with this. Users of `HashSet.Raw` will need to provide proofs of `WF` to lemmas and should use lemmas like `WF.empty` and `WF.insert` (which are always named exactly like the operations they are about) to show that set operations preserve well-formedness.
#  Constructor

```
[Std.HashSet.Raw.WF.mk](Basic-Types/Maps-and-Sets/#Std___HashSet___Raw___WF___mk "Documentation for Std.HashSet.Raw.WF.mk").{u}
```

#  Fields

```
out : m.[inner](Basic-Types/Maps-and-Sets/#Std___HashSet___Raw___mk "Documentation for Std.HashSet.Raw.inner").[WF](Basic-Types/Maps-and-Sets/#Std___HashMap___Raw___WF___mk "Documentation for Std.HashMap.Raw.WF")
```

Internal implementation detail of the hash set
##  20.19.7. Extensional Hash Sets[🔗](find/?domain=Verso.Genre.Manual.section&name=ExtHashSet "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashSet "Permalink")structure
```


Std.ExtHashSet.{u} (α : Type u) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] : Type u


Std.ExtHashSet.{u} (α : Type u) [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α]
  [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] : Type u


```

Hash sets.
This is a simple separate-chaining hash table. The data of the hash set consists of a cached size and an array of buckets, where each bucket is a linked list of keys. The number of buckets is always a power of two. The hash set doubles its size upon inserting an element such that the number of elements is more than 75% of the number of buckets.
The hash table is backed by an `[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")`. Users should make sure that the hash set is used linearly to avoid expensive copies.
The hash set uses `==` (provided by the `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` typeclass) to compare elements and `[hash](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable.hash")` (provided by the `[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable")` typeclass) to hash them. To ensure that the operations behave as expected, `==` should be an equivalence relation and `a == b` should imply `hash a = hash b` (see also the `[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq")` and `[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable")` typeclasses). Both of these conditions are automatic if the BEq instance is lawful, i.e., if `a == b` implies `a = b`.
In contrast to regular hash sets, `[Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet")` offers several extensionality lemmas and therefore has more lemmas about equality of hash maps. This however also makes it lose the ability to iterate freely over hash sets.
These hash sets contain a bundled well-formedness invariant, which means that they cannot be used in nested inductive types. For these use cases, `[Std.HashSet.Raw](Basic-Types/Maps-and-Sets/#Std___HashSet___Raw___mk "Documentation for Std.HashSet.Raw")` and `[Std.HashSet.Raw.WF](Basic-Types/Maps-and-Sets/#Std___HashSet___Raw___WF___mk "Documentation for Std.HashSet.Raw.WF")` unbundle the invariant from the hash set. When in doubt, prefer `HashSet` or `ExtHashSet` over `HashSet.Raw`.
#  Constructor

```
[Std.ExtHashSet.mk](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet.mk").{u}
```

#  Fields

```
inner : [Std.ExtHashMap](Basic-Types/Maps-and-Sets/#Std___ExtHashMap "Documentation for Std.ExtHashMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")
```

Internal implementation detail of the hash set.
###  20.19.7.1. Creation[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Extensional-Hash-Sets--Creation "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashSet.emptyWithCapacity "Permalink")def
```


Std.ExtHashSet.emptyWithCapacity.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (capacity : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 8) : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α


Std.ExtHashSet.emptyWithCapacity.{u}
  {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (capacity : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") := 8) : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α


```

Creates a new empty hash set. The optional parameter `capacity` can be supplied to presize the set so that it can hold the given number of elements without reallocating. It is also possible to use the empty collection notations `∅` and `{}` to create an empty hash set with the default capacity.
###  20.19.7.2. Properties[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Extensional-Hash-Sets--Properties "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashSet.isEmpty "Permalink")def
```


Std.ExtHashSet.isEmpty.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.ExtHashSet.isEmpty.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the hash set contains no elements.
Note that if your `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` instance is not reflexive or your `[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable")` instance is not lawful, then it is possible that this function returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` even though `m.[contains](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___contains "Documentation for Std.ExtHashSet.contains") a = [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` for all `a`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashSet.size "Permalink")def
```


Std.ExtHashSet.size.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Std.ExtHashSet.size.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

The number of elements present in the set
###  20.19.7.3. Queries[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Extensional-Hash-Sets--Queries "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashSet.contains "Permalink")def
```


Std.ExtHashSet.contains.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.ExtHashSet.contains.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the given key is present in the set. There is also a `Prop`-valued version of this: `a ∈ m` is equivalent to `m.[contains](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___contains "Documentation for Std.ExtHashSet.contains") a = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Observe that this is different behavior than for lists: for lists, `∈` uses `=` and `contains` use `==` for comparisons, while for hash sets, both use `==`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashSet.get "Permalink")def
```


Std.ExtHashSet.get.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α) (a : α)
  (h : a ∈ m) : α


Std.ExtHashSet.get.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α) (a : α)
  (h : a ∈ m) : α


```

Retrieves the key from the set that matches `a`. Ensures that such a key exists by requiring a proof of `a ∈ m`. The result is guaranteed to be pointer equal to the key in the set.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashSet.get! "Permalink")def
```


Std.ExtHashSet.get!.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α)
  (a : α) : α


Std.ExtHashSet.get!.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α)
  (a : α) : α


```

Checks if given key is contained and returns the key if it is, otherwise panics. If no panic occurs the result is guaranteed to be pointer equal to the key in the set.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashSet.get? "Permalink")def
```


Std.ExtHashSet.get?.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α) (a : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.ExtHashSet.get?.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α) (a : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Checks if given key is contained and returns the key if it is, otherwise `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`. The result in the `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` case is guaranteed to be pointer equal to the key in the set.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashSet.getD "Permalink")def
```


Std.ExtHashSet.getD.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α)
  (a fallback : α) : α


Std.ExtHashSet.getD.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α)
  (a fallback : α) : α


```

Checks if given key is contained and returns the key if it is, otherwise `fallback`. If they key is contained the result is guaranteed to be pointer equal to the key in the set.
###  20.19.7.4. Modification[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Extensional-Hash-Sets--Modification "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashSet.insert "Permalink")def
```


Std.ExtHashSet.insert.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α) (a : α) :
  [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α


Std.ExtHashSet.insert.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α) (a : α) :
  [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α


```

Inserts the given element into the set. If the hash set already contains an element that is equal (with regard to `==`) to the given element, then the hash set is returned unchanged.
Note: this non-replacement behavior is true for `ExtHashSet` and `ExtHashSet.Raw`. The `insert` function on `ExtHashMap`, `DExtHashMap`, `ExtHashMap.Raw` and `DExtHashMap.Raw` behaves differently: it will overwrite an existing mapping.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashSet.insertMany "Permalink")def
```


Std.ExtHashSet.insertMany.{u, v} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] {ρ : Type v}
  [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ α] (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α) (l : ρ) : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α


Std.ExtHashSet.insertMany.{u, v}
  {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] {ρ : Type v}
  [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ α] (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α)
  (l : ρ) : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α


```

Inserts multiple mappings into the hash set by iterating over the given collection and calling `insert`. If the same key appears multiple times, the first occurrence takes precedence.
Note: this precedence behavior is true for `ExtHashSet` and `ExtHashSet.Raw`. The `insertMany` function on `ExtHashMap`, `DExtHashMap`, `ExtHashMap.Raw` and `DExtHashMap.Raw` behaves differently: it will prefer the last appearance.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashSet.erase "Permalink")def
```


Std.ExtHashSet.erase.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α) (a : α) :
  [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α


Std.ExtHashSet.erase.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α) (a : α) :
  [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α


```

Removes the element if it exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashSet.filter "Permalink")def
```


Std.ExtHashSet.filter.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α] (f : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α) : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α


Std.ExtHashSet.filter.{u} {α : Type u}
  {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α} {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α}
  [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (f : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α) :
  [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α


```

Removes all elements from the hash set for which the given function returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashSet.containsThenInsert "Permalink")def
```


Std.ExtHashSet.containsThenInsert.{u} {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α] [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α


Std.ExtHashSet.containsThenInsert.{u}
  {α : Type u} {x✝ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α}
  {x✝¹ : [Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α} [[EquivBEq](Type-Classes/Basic-Classes/#EquivBEq___mk "Documentation for EquivBEq") α]
  [[LawfulHashable](Type-Classes/Basic-Classes/#LawfulHashable___mk "Documentation for LawfulHashable") α]
  (m : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α) (a : α) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α


```

Checks whether an element is present in a set and inserts the element if it was not found. If the hash set already contains an element that is equal (with regard to `==`) to the given element, then the hash set is returned unchanged.
Equivalent to (but potentially faster than) calling `contains` followed by `insert`.
###  20.19.7.5. Conversion[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Extensional-Hash-Sets--Conversion "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashSet.ofList "Permalink")def
```


Std.ExtHashSet.ofList.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α


Std.ExtHashSet.ofList.{u} {α : Type u}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α) :
  [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α


```

Creates a hash set from a list of elements. Note that unlike repeatedly calling `insert`, if the collection contains multiple elements that are equal (with regard to `==`), then the last element in the collection will be present in the returned hash set.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.ExtHashSet.ofArray "Permalink")def
```


Std.ExtHashSet.ofArray.{u} {α : Type u} [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α]
  (l : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) : [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α


Std.ExtHashSet.ofArray.{u} {α : Type u}
  [[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") α] [[Hashable](Type-Classes/Basic-Classes/#Hashable___mk "Documentation for Hashable") α] (l : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α) :
  [Std.ExtHashSet](Basic-Types/Maps-and-Sets/#Std___ExtHashSet___mk "Documentation for Std.ExtHashSet") α


```

Creates a hash set from an array of elements. Note that unlike repeatedly calling `insert`, if the collection contains multiple elements that are equal (with regard to `==`), then the last element in the collection will be present in the returned hash set.
##  20.19.8. Tree-Based Maps[🔗](find/?domain=Verso.Genre.Manual.section&name=TreeMap "Permalink")
The declarations in this section should be imported using `import Std.TreeMap`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap "Permalink")structure
```


Std.TreeMap.{u, v} (α : Type u) (β : Type v)
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by exact compare) : Type (max u v)


Std.TreeMap.{u, v} (α : Type u)
  (β : Type v)
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by
    exact compare) :
  Type (max u v)


```

Tree maps.
A tree map stores an assignment of keys to values. It depends on a comparator function that defines an ordering on the keys and provides efficient order-dependent queries, such as retrieval of the minimum or maximum.
To ensure that the operations behave as expected, the comparator function `cmp` should satisfy certain laws that ensure a consistent ordering:
  * If `a` is less than (or equal) to `b`, then `b` is greater than (or equal) to `a` and vice versa (see the `OrientedCmp` typeclass).
  * If `a` is less than or equal to `b` and `b` is, in turn, less than or equal to `c`, then `a` is less than or equal to `c` (see the `TransCmp` typeclass).


Keys for which `cmp a b = [Ordering.eq](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.eq")` are considered the same, i.e., there can be only one entry with key either `a` or `b` in a tree map. Looking up either `a` or `b` always yields the same entry, if any is present.
To avoid expensive copies, users should make sure that the tree map is used linearly.
Internally, the tree maps are represented as size-bounded trees, a type of self-balancing binary search tree with efficient order statistic lookups.
For use in proofs, the type `Std.ExtTreeMap` of extensional tree maps should be preferred. This type comes with several extensionality lemmas and provides the same functions but requires a `TransCmp` instance to work with.
These tree maps contain a bundled well-formedness invariant, which means that they cannot be used in nested inductive types. For these use cases, `[Std.TreeMap.Raw](Basic-Types/Maps-and-Sets/#Std___TreeMap___Raw___mk "Documentation for Std.TreeMap.Raw")` and `[Std.TreeMap.Raw.WF](Basic-Types/Maps-and-Sets/#Std___TreeMap___Raw___WF___mk "Documentation for Std.TreeMap.Raw.WF")` unbundle the invariant from the tree map. When in doubt, prefer `TreeMap` over `TreeMap.Raw`.
###  20.19.8.1. Creation[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Tree-Based-Maps--Creation "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.empty "Permalink")def
```


Std.TreeMap.empty.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


Std.TreeMap.empty.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} :
  [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


```

Creates a new empty tree map. It is also possible and recommended to use the empty collection notations `∅` and `{}` to create an empty tree map. `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` replaces `empty` with `∅`.
###  20.19.8.2. Properties[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Tree-Based-Maps--Properties "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.size "Permalink")def
```


Std.TreeMap.size.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Std.TreeMap.size.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the number of mappings present in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.isEmpty "Permalink")def
```


Std.TreeMap.isEmpty.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.TreeMap.isEmpty.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the tree map contains no mappings.
###  20.19.8.3. Queries[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Tree-Based-Maps--Queries "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.contains "Permalink")def
```


Std.TreeMap.contains.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (l : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.TreeMap.contains.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (l : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if there is a mapping for the given key `a` or a key that is equal to `a` according to the comparator `cmp`. There is also a `Prop`-valued version of this: `a ∈ t` is equivalent to `t.contains a = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Observe that this is different behavior than for lists: for lists, `∈` uses `=` and `contains` uses `==` for equality checks, while for tree maps, both use the given comparator `cmp`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.get "Permalink")def
```


Std.TreeMap.get.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α)
  (h : a ∈ t) : β


Std.TreeMap.get.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α)
  (h : a ∈ t) : β


```

Given a proof that a mapping for the given key is present, retrieves the mapping for the given key.
Uses the `LawfulEqCmp` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.get! "Permalink")def
```


Std.TreeMap.get!.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") β] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (a : α) : β


Std.TreeMap.get!.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") β] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (a : α) : β


```

Tries to retrieve the mapping for the given key, panicking if no such mapping is present.
Uses the `LawfulEqCmp` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.get? "Permalink")def
```


Std.TreeMap.get?.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


Std.TreeMap.get?.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β


```

Tries to retrieve the mapping for the given key, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such mapping is present.
Uses the `LawfulEqCmp` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getD "Permalink")def
```


Std.TreeMap.getD.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α)
  (fallback : β) : β


Std.TreeMap.getD.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α)
  (fallback : β) : β


```

Tries to retrieve the mapping for the given key, returning `fallback` if no such mapping is present.
Uses the `LawfulEqCmp` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKey "Permalink")def
```


Std.TreeMap.getKey.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α)
  (h : a ∈ t) : α


Std.TreeMap.getKey.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α)
  (h : a ∈ t) : α


```

Retrieves the key from the mapping that matches `a`. Ensures that such a mapping exists by requiring a proof of `a ∈ m`. The result is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKey! "Permalink")def
```


Std.TreeMap.getKey!.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (a : α) : α


Std.TreeMap.getKey!.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (a : α) : α


```

Checks if a mapping for the given key exists and returns the key if it does, otherwise panics. If no panic occurs the result is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKey? "Permalink")def
```


Std.TreeMap.getKey?.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.TreeMap.getKey?.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Checks if a mapping for the given key exists and returns the key if it does, otherwise `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`. The result in the `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` case is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKeyD "Permalink")def
```


Std.TreeMap.getKeyD.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a fallback : α) :
  α


Std.TreeMap.getKeyD.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (a fallback : α) : α


```

Checks if a mapping for the given key exists and returns the key if it does, otherwise `fallback`. If a mapping exists the result is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.keys "Permalink")def
```


Std.TreeMap.keys.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


Std.TreeMap.keys.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Returns a list of all keys present in the tree map in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.keysArray "Permalink")def
```


Std.TreeMap.keysArray.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Std.TreeMap.keysArray.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Returns an array of all keys present in the tree map in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.values "Permalink")def
```


Std.TreeMap.values.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


Std.TreeMap.values.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


```

Returns a list of all values present in the tree map in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.valuesArray "Permalink")def
```


Std.TreeMap.valuesArray.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


Std.TreeMap.valuesArray.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


```

Returns an array of all values present in the tree map in ascending order.
####  20.19.8.3.1. Ordering-Based Queries[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Tree-Based-Maps--Queries--Ordering-Based-Queries "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.entryAtIdx "Permalink")def
```


Std.TreeMap.entryAtIdx.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (h : n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") t.[size](Basic-Types/Maps-and-Sets/#Std___TreeMap___size "Documentation for Std.TreeMap.size")) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.entryAtIdx.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (h : n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") t.[size](Basic-Types/Maps-and-Sets/#Std___TreeMap___size "Documentation for Std.TreeMap.size")) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Returns the key-value pair with the `n`-th smallest key.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.entryAtIdx! "Permalink")def
```


Std.TreeMap.entryAtIdx!.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.entryAtIdx!.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Returns the key-value pair with the `n`-th smallest key, or panics if `n` is at least `t.[size](Basic-Types/Maps-and-Sets/#Std___TreeMap___size "Documentation for Std.TreeMap.size")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.entryAtIdx? "Permalink")def
```


Std.TreeMap.entryAtIdx?.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


Std.TreeMap.entryAtIdx?.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Returns the key-value pair with the `n`-th smallest key, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if `n` is at least `t.[size](Basic-Types/Maps-and-Sets/#Std___TreeMap___size "Documentation for Std.TreeMap.size")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.entryAtIdxD "Permalink")def
```


Std.TreeMap.entryAtIdxD.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (fallback : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.entryAtIdxD.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (fallback : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Returns the key-value pair with the `n`-th smallest key, or `fallback` if `n` is at least `t.[size](Basic-Types/Maps-and-Sets/#Std___TreeMap___size "Documentation for Std.TreeMap.size")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getEntryGE "Permalink")def
```


Std.TreeMap.getEntryGE.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [Std.TransCmp cmp] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) (h : [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") (cmp a k).[isGE](Type-Classes/Basic-Classes/#Ordering___isGE "Documentation for Ordering.isGE") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.getEntryGE.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.TransCmp cmp]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α)
  (h :
    [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") (cmp a k).[isGE](Type-Classes/Basic-Classes/#Ordering___isGE "Documentation for Ordering.isGE") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) :
  α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Given a proof that such a mapping exists, retrieves the key-value pair with the smallest key that is greater than or equal to the given key.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getEntryGE! "Permalink")def
```


Std.TreeMap.getEntryGE!.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.getEntryGE!.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) :
  α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Tries to retrieve the key-value pair with the smallest key that is greater than or equal to the given key, panicking if no such pair exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getEntryGE? "Permalink")def
```


Std.TreeMap.getEntryGE?.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


Std.TreeMap.getEntryGE?.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Tries to retrieve the key-value pair with the smallest key that is greater than or equal to the given key, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such pair exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getEntryGED "Permalink")def
```


Std.TreeMap.getEntryGED.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α)
  (fallback : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.getEntryGED.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α)
  (fallback : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Tries to retrieve the key-value pair with the smallest key that is greater than or equal to the given key, returning `fallback` if no such pair exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getEntryGT "Permalink")def
```


Std.TreeMap.getEntryGT.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [Std.TransCmp cmp] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) (h : [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") cmp a k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Ordering.gt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.gt")) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.getEntryGT.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.TransCmp cmp]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α)
  (h :
    [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") cmp a k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Ordering.gt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.gt")) :
  α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Given a proof that such a mapping exists, retrieves the key-value pair with the smallest key that is greater than the given key.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getEntryGT! "Permalink")def
```


Std.TreeMap.getEntryGT!.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.getEntryGT!.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) :
  α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Tries to retrieve the key-value pair with the smallest key that is greater than the given key, panicking if no such pair exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getEntryGT? "Permalink")def
```


Std.TreeMap.getEntryGT?.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


Std.TreeMap.getEntryGT?.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Tries to retrieve the key-value pair with the smallest key that is greater than the given key, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such pair exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getEntryGTD "Permalink")def
```


Std.TreeMap.getEntryGTD.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α)
  (fallback : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.getEntryGTD.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α)
  (fallback : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Tries to retrieve the key-value pair with the smallest key that is greater than the given key, returning `fallback` if no such pair exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getEntryLE "Permalink")def
```


Std.TreeMap.getEntryLE.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [Std.TransCmp cmp] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) (h : [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") (cmp a k).[isLE](Type-Classes/Basic-Classes/#Ordering___isLE "Documentation for Ordering.isLE") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.getEntryLE.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.TransCmp cmp]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α)
  (h :
    [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") (cmp a k).[isLE](Type-Classes/Basic-Classes/#Ordering___isLE "Documentation for Ordering.isLE") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) :
  α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Given a proof that such a mapping exists, retrieves the key-value pair with the largest key that is less than or equal to the given key.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getEntryLE! "Permalink")def
```


Std.TreeMap.getEntryLE!.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.getEntryLE!.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) :
  α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Tries to retrieve the key-value pair with the largest key that is less than or equal to the given key, panicking if no such pair exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getEntryLE? "Permalink")def
```


Std.TreeMap.getEntryLE?.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


Std.TreeMap.getEntryLE?.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Tries to retrieve the key-value pair with the largest key that is less than or equal to the given key, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such pair exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getEntryLED "Permalink")def
```


Std.TreeMap.getEntryLED.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α)
  (fallback : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.getEntryLED.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α)
  (fallback : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Tries to retrieve the key-value pair with the largest key that is less than or equal to the given key, returning `fallback` if no such pair exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getEntryLT "Permalink")def
```


Std.TreeMap.getEntryLT.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [Std.TransCmp cmp] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) (h : [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") cmp a k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Ordering.lt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.lt")) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.getEntryLT.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.TransCmp cmp]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α)
  (h :
    [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") cmp a k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Ordering.lt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.lt")) :
  α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Given a proof that such a mapping exists, retrieves the key-value pair with the largest key that is less than the given key.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getEntryLT! "Permalink")def
```


Std.TreeMap.getEntryLT!.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.getEntryLT!.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) :
  α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Tries to retrieve the key-value pair with the largest key that is less than the given key, panicking if no such pair exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getEntryLT? "Permalink")def
```


Std.TreeMap.getEntryLT?.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


Std.TreeMap.getEntryLT?.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Tries to retrieve the key-value pair with the largest key that is less than the given key, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such pair exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getEntryLTD "Permalink")def
```


Std.TreeMap.getEntryLTD.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α)
  (fallback : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.getEntryLTD.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α)
  (fallback : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Tries to retrieve the key-value pair with the largest key that is less than the given key, returning `fallback` if no such pair exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKeyGE "Permalink")def
```


Std.TreeMap.getKeyGE.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [Std.TransCmp cmp] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) (h : [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") (cmp a k).[isGE](Type-Classes/Basic-Classes/#Ordering___isGE "Documentation for Ordering.isGE") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : α


Std.TreeMap.getKeyGE.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.TransCmp cmp]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α)
  (h :
    [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") (cmp a k).[isGE](Type-Classes/Basic-Classes/#Ordering___isGE "Documentation for Ordering.isGE") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) :
  α


```

Given a proof that such a mapping exists, retrieves the smallest key that is greater than or equal to the given key.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKeyGE! "Permalink")def
```


Std.TreeMap.getKeyGE!.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) : α


Std.TreeMap.getKeyGE!.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) : α


```

Tries to retrieve the smallest key that is greater than or equal to the given key, panicking if no such key exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKeyGE? "Permalink")def
```


Std.TreeMap.getKeyGE?.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.TreeMap.getKeyGE?.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Tries to retrieve the smallest key that is greater than or equal to the given key, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such key exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKeyGED "Permalink")def
```


Std.TreeMap.getKeyGED.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k fallback : α) :
  α


Std.TreeMap.getKeyGED.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k fallback : α) : α


```

Tries to retrieve the smallest key that is greater than or equal to the given key, returning `fallback` if no such key exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKeyGT "Permalink")def
```


Std.TreeMap.getKeyGT.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [Std.TransCmp cmp] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) (h : [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") cmp a k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Ordering.gt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.gt")) : α


Std.TreeMap.getKeyGT.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.TransCmp cmp]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α)
  (h :
    [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") cmp a k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Ordering.gt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.gt")) :
  α


```

Given a proof that such a mapping exists, retrieves the smallest key that is greater than the given key.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKeyGT! "Permalink")def
```


Std.TreeMap.getKeyGT!.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) : α


Std.TreeMap.getKeyGT!.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) : α


```

Tries to retrieve the smallest key that is greater than the given key, panicking if no such key exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKeyGT? "Permalink")def
```


Std.TreeMap.getKeyGT?.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.TreeMap.getKeyGT?.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Tries to retrieve the smallest key that is greater than the given key, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such key exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKeyGTD "Permalink")def
```


Std.TreeMap.getKeyGTD.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k fallback : α) :
  α


Std.TreeMap.getKeyGTD.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k fallback : α) : α


```

Tries to retrieve the smallest key that is greater than the given key, returning `fallback` if no such key exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKeyLE "Permalink")def
```


Std.TreeMap.getKeyLE.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [Std.TransCmp cmp] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) (h : [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") (cmp a k).[isLE](Type-Classes/Basic-Classes/#Ordering___isLE "Documentation for Ordering.isLE") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : α


Std.TreeMap.getKeyLE.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.TransCmp cmp]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α)
  (h :
    [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") (cmp a k).[isLE](Type-Classes/Basic-Classes/#Ordering___isLE "Documentation for Ordering.isLE") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) :
  α


```

Given a proof that such a mapping exists, retrieves the largest key that is less than or equal to the given key.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKeyLE! "Permalink")def
```


Std.TreeMap.getKeyLE!.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) : α


Std.TreeMap.getKeyLE!.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) : α


```

Tries to retrieve the largest key that is less than or equal to the given key, panicking if no such key exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKeyLE? "Permalink")def
```


Std.TreeMap.getKeyLE?.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.TreeMap.getKeyLE?.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Tries to retrieve the largest key that is less than or equal to the given key, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such key exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKeyLED "Permalink")def
```


Std.TreeMap.getKeyLED.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k fallback : α) :
  α


Std.TreeMap.getKeyLED.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k fallback : α) : α


```

Tries to retrieve the largest key that is less than or equal to the given key, returning `fallback` if no such key exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKeyLT "Permalink")def
```


Std.TreeMap.getKeyLT.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [Std.TransCmp cmp] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) (h : [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") cmp a k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Ordering.lt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.lt")) : α


Std.TreeMap.getKeyLT.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.TransCmp cmp]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α)
  (h :
    [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") cmp a k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Ordering.lt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.lt")) :
  α


```

Given a proof that such a mapping exists, retrieves the largest key that is less than the given key.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKeyLT! "Permalink")def
```


Std.TreeMap.getKeyLT!.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) : α


Std.TreeMap.getKeyLT!.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k : α) : α


```

Tries to retrieve the largest key that is less than the given key, panicking if no such key exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKeyLT? "Permalink")def
```


Std.TreeMap.getKeyLT?.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.TreeMap.getKeyLT?.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Tries to retrieve the largest key that is less than the given key, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such key exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getKeyLTD "Permalink")def
```


Std.TreeMap.getKeyLTD.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (k fallback : α) :
  α


Std.TreeMap.getKeyLTD.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (k fallback : α) : α


```

Tries to retrieve the largest key that is less than the given key, returning `fallback` if no such key exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.keyAtIdx "Permalink")def
```


Std.TreeMap.keyAtIdx.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (h : n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") t.[size](Basic-Types/Maps-and-Sets/#Std___TreeMap___size "Documentation for Std.TreeMap.size")) : α


Std.TreeMap.keyAtIdx.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (h : n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") t.[size](Basic-Types/Maps-and-Sets/#Std___TreeMap___size "Documentation for Std.TreeMap.size")) : α


```

Returns the `n`-th smallest key.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.keyAtIdx! "Permalink")def
```


Std.TreeMap.keyAtIdx!.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : α


Std.TreeMap.keyAtIdx!.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : α


```

Returns the `n`-th smallest key, or panics if `n` is at least `t.[size](Basic-Types/Maps-and-Sets/#Std___TreeMap___size "Documentation for Std.TreeMap.size")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.keyAtIdx? "Permalink")def
```


Std.TreeMap.keyAtIdx?.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.TreeMap.keyAtIdx?.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Returns the `n`-th smallest key, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if `n` is at least `t.[size](Basic-Types/Maps-and-Sets/#Std___TreeMap___size "Documentation for Std.TreeMap.size")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.keyAtIdxD "Permalink")def
```


Std.TreeMap.keyAtIdxD.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (fallback : α) : α


Std.TreeMap.keyAtIdxD.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (fallback : α) : α


```

Returns the `n`-th smallest key, or `fallback` if `n` is at least `t.[size](Basic-Types/Maps-and-Sets/#Std___TreeMap___size "Documentation for Std.TreeMap.size")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.minEntry "Permalink")def
```


Std.TreeMap.minEntry.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (h : t.[isEmpty](Basic-Types/Maps-and-Sets/#Std___TreeMap___isEmpty "Documentation for Std.TreeMap.isEmpty") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.minEntry.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (h : t.[isEmpty](Basic-Types/Maps-and-Sets/#Std___TreeMap___isEmpty "Documentation for Std.TreeMap.isEmpty") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Given a proof that the tree map is not empty, retrieves the key-value pair with the smallest key.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.minEntry! "Permalink")def
```


Std.TreeMap.minEntry!.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.minEntry!.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Tries to retrieve the key-value pair with the smallest key in the tree map, panicking if the map is empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.minEntry? "Permalink")def
```


Std.TreeMap.minEntry?.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


Std.TreeMap.minEntry?.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Tries to retrieve the key-value pair with the smallest key in the tree map, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the map is empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.minEntryD "Permalink")def
```


Std.TreeMap.minEntryD.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (fallback : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.minEntryD.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (fallback : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Tries to retrieve the key-value pair with the smallest key in the tree map, returning `fallback` if the tree map is empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.minKey "Permalink")def
```


Std.TreeMap.minKey.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (h : t.[isEmpty](Basic-Types/Maps-and-Sets/#Std___TreeMap___isEmpty "Documentation for Std.TreeMap.isEmpty") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : α


Std.TreeMap.minKey.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (h : t.[isEmpty](Basic-Types/Maps-and-Sets/#Std___TreeMap___isEmpty "Documentation for Std.TreeMap.isEmpty") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : α


```

Given a proof that the tree map is not empty, retrieves the smallest key.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.minKey! "Permalink")def
```


Std.TreeMap.minKey!.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : α


Std.TreeMap.minKey!.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : α


```

Tries to retrieve the smallest key in the tree map, panicking if the map is empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.minKey? "Permalink")def
```


Std.TreeMap.minKey?.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.TreeMap.minKey?.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Tries to retrieve the smallest key in the tree map, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the map is empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.minKeyD "Permalink")def
```


Std.TreeMap.minKeyD.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (fallback : α) : α


Std.TreeMap.minKeyD.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (fallback : α) : α


```

Tries to retrieve the smallest key in the tree map, returning `fallback` if the tree map is empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.maxEntry "Permalink")def
```


Std.TreeMap.maxEntry.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (h : t.[isEmpty](Basic-Types/Maps-and-Sets/#Std___TreeMap___isEmpty "Documentation for Std.TreeMap.isEmpty") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.maxEntry.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (h : t.[isEmpty](Basic-Types/Maps-and-Sets/#Std___TreeMap___isEmpty "Documentation for Std.TreeMap.isEmpty") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Given a proof that the tree map is not empty, retrieves the key-value pair with the largest key.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.maxEntry! "Permalink")def
```


Std.TreeMap.maxEntry!.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.maxEntry!.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Tries to retrieve the key-value pair with the largest key in the tree map, panicking if the map is empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.maxEntry? "Permalink")def
```


Std.TreeMap.maxEntry?.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


Std.TreeMap.maxEntry?.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Tries to retrieve the key-value pair with the largest key in the tree map, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the map is empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.maxEntryD "Permalink")def
```


Std.TreeMap.maxEntryD.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (fallback : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


Std.TreeMap.maxEntryD.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (fallback : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β) : α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β


```

Tries to retrieve the key-value pair with the largest key in the tree map, returning `fallback` if the tree map is empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.maxKey "Permalink")def
```


Std.TreeMap.maxKey.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (h : t.[isEmpty](Basic-Types/Maps-and-Sets/#Std___TreeMap___isEmpty "Documentation for Std.TreeMap.isEmpty") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : α


Std.TreeMap.maxKey.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (h : t.[isEmpty](Basic-Types/Maps-and-Sets/#Std___TreeMap___isEmpty "Documentation for Std.TreeMap.isEmpty") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : α


```

Given a proof that the tree map is not empty, retrieves the largest key.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.maxKey! "Permalink")def
```


Std.TreeMap.maxKey!.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : α


Std.TreeMap.maxKey!.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : α


```

Tries to retrieve the largest key in the tree map, panicking if the map is empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.maxKey? "Permalink")def
```


Std.TreeMap.maxKey?.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.TreeMap.maxKey?.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Tries to retrieve the largest key in the tree map, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the map is empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.maxKeyD "Permalink")def
```


Std.TreeMap.maxKeyD.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (fallback : α) : α


Std.TreeMap.maxKeyD.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (fallback : α) : α


```

Tries to retrieve the largest key in the tree map, returning `fallback` if the tree map is empty.
###  20.19.8.4. Modification[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Tree-Based-Maps--Modification "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.alter "Permalink")def
```


Std.TreeMap.alter.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α)
  (f : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β) : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


Std.TreeMap.alter.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α)
  (f : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β) :
  [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


```

Modifies in place the value associated with a given key, allowing creating new values and deleting values via an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` valued replacement function.
This function ensures that the value is used linearly.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.modify "Permalink")def
```


Std.TreeMap.modify.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α)
  (f : β → β) : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


Std.TreeMap.modify.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α)
  (f : β → β) : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


```

Modifies in place the value associated with a given key.
This function ensures that the value is used linearly.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.containsThenInsert "Permalink")def
```


Std.TreeMap.containsThenInsert.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α) (b : β) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


Std.TreeMap.containsThenInsert.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α)
  (b : β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


```

Checks whether a key is present in a map and unconditionally inserts a value for the key.
Equivalent to (but potentially faster than) calling `contains` followed by `insert`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.containsThenInsertIfNew "Permalink")def
```


Std.TreeMap.containsThenInsertIfNew.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α) (b : β) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


Std.TreeMap.containsThenInsertIfNew.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α)
  (b : β) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


```

Checks whether a key is present in a map and inserts a value for the key if it was not found. If the returned `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, then the returned map is unaltered. If the `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, then the returned map has a new value inserted.
Equivalent to (but potentially faster than) calling `contains` followed by `insertIfNew`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.erase "Permalink")def
```


Std.TreeMap.erase.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α) :
  [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


Std.TreeMap.erase.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α) :
  [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


```

Removes the mapping for the given key if it exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.eraseMany "Permalink")def
```


Std.TreeMap.eraseMany.{u, v, u_1} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {ρ : Type u_1} [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ α]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (l : ρ) : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


Std.TreeMap.eraseMany.{u, v, u_1}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {ρ : Type u_1}
  [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ α] (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (l : ρ) : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


```

Erases multiple mappings from the tree map by iterating over the given collection and calling `erase`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.filter "Permalink")def
```


Std.TreeMap.filter.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (f : α → β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (m : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


Std.TreeMap.filter.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (f : α → β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (m : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) :
  [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


```

Removes all mappings of the map for which the given function returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.filterMap "Permalink")def
```


Std.TreeMap.filterMap.{u, v, w} {α : Type u} {β : Type v} {γ : Type w}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (f : α → β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ)
  (m : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α γ cmp


Std.TreeMap.filterMap.{u, v, w}
  {α : Type u} {β : Type v} {γ : Type w}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (f : α → β → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") γ)
  (m : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) :
  [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α γ cmp


```

Updates the values of the map by applying the given function to all mappings, keeping only those mappings where the function returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.insert "Permalink")def
```


Std.TreeMap.insert.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (l : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α) (b : β) :
  [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


Std.TreeMap.insert.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (l : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α)
  (b : β) : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


```

Inserts the given mapping into the map. If there is already a mapping for the given key, then both key and value will be replaced.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.insertIfNew "Permalink")def
```


Std.TreeMap.insertIfNew.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α) (b : β) :
  [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


Std.TreeMap.insertIfNew.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α)
  (b : β) : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


```

If there is no mapping for the given key, inserts the given mapping into the map. Otherwise, returns the map unaltered.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.getThenInsertIfNew? "Permalink")def
```


Std.TreeMap.getThenInsertIfNew?.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α) (b : β) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


Std.TreeMap.getThenInsertIfNew?.{u, v}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (a : α)
  (b : β) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") β [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


```

Checks whether a key is present in a map, returning the associated value, and inserts a value for the key if it was not found.
If the returned value is `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v`, then the returned map is unaltered. If it is `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, then the returned map has a new value inserted.
Equivalent to (but potentially faster than) calling `get?` followed by `insertIfNew`.
Uses the `LawfulEqCmp` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.insertMany "Permalink")def
```


Std.TreeMap.insertMany.{u, v, u_1} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {ρ : Type u_1} [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (l : ρ) : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


Std.TreeMap.insertMany.{u, v, u_1}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {ρ : Type u_1}
  [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) (l : ρ) :
  [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


```

Inserts multiple mappings into the tree map by iterating over the given collection and calling `insert`. If the same key appears multiple times, the last occurrence takes precedence.
Note: this precedence behavior is true for `TreeMap`, `DTreeMap`, `TreeMap.Raw` and `DTreeMap.Raw`. The `insertMany` function on `TreeSet` and `TreeSet.Raw` behaves differently: it will prefer the first appearance.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.insertManyIfNewUnit "Permalink")def
```


Std.TreeMap.insertManyIfNewUnit.{u, u_1} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {ρ : Type u_1} [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ α]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") cmp) (l : ρ) : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") cmp


Std.TreeMap.insertManyIfNewUnit.{u, u_1}
  {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {ρ : Type u_1} [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ α]
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") cmp) (l : ρ) :
  [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") cmp


```

Inserts multiple elements into the tree map by iterating over the given collection and calling `insertIfNew`. If the same key appears multiple times, the first occurrence takes precedence.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.mergeWith "Permalink")def
```


Std.TreeMap.mergeWith.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (mergeFn : α → β → β → β)
  (t₁ t₂ : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


Std.TreeMap.mergeWith.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (mergeFn : α → β → β → β)
  (t₁ t₂ : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) :
  [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


```

Returns a map that contains all mappings of `t₁` and `t₂`. In case that both maps contain the same key `k` with respect to `cmp`, the provided function is used to determine the new value from the respective values in `t₁` and `t₂`.
This function ensures that `t₁` is used linearly. It also uses the individual values in `t₁` linearly if the merge function uses the second argument (i.e. the first of type `β a`) linearly. Hence, as long as `t₁` is unshared, the performance characteristics follow the following imperative description: Iterate over all mappings in `t₂`, inserting them into `t₁` if `t₁` does not contain a conflicting mapping yet. If `t₁` does contain a conflicting mapping, use the given merge function to merge the mapping in `t₂` into the mapping in `t₁`. Then return `t₁`.
Hence, the runtime of this method scales logarithmically in the size of `t₁` and linearly in the size of `t₂` as long as `t₁` is unshared.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.partition "Permalink")def
```


Std.TreeMap.partition.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (f : α → β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


Std.TreeMap.partition.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (f : α → β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) :
  [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")
    [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


```

Partitions a tree map into two tree maps based on a predicate.
###  20.19.8.5. Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Tree-Based-Maps--Iteration "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.iter "Permalink")def
```


Std.TreeMap.iter.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (m : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


Std.TreeMap.iter.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (m : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Returns a finite iterator over the entries of a tree map. The iterator yields the elements of the map in order and then terminates.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.keysIter "Permalink")def
```


Std.TreeMap.keysIter.{u} {α β : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (m : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") α


Std.TreeMap.keysIter.{u} {α β : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (m : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") α


```

Returns a finite iterator over the keys of a tree map. The iterator yields the keys in order and then terminates.
The key and value types must live in the same universe.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.valuesIter "Permalink")def
```


Std.TreeMap.valuesIter.{u} {α β : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (m : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


Std.TreeMap.valuesIter.{u} {α β : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (m : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


```

Returns a finite iterator over the values of a tree map. The iterator yields the values in order and then terminates.
The key and value types must live in the same universe.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.map "Permalink")def
```


Std.TreeMap.map.{u, v, w} {α : Type u} {β : Type v} {γ : Type w}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (f : α → β → γ) (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) :
  [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α γ cmp


Std.TreeMap.map.{u, v, w} {α : Type u}
  {β : Type v} {γ : Type w}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (f : α → β → γ)
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) :
  [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α γ cmp


```

Updates the values of the map by applying the given function to all mappings.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.all "Permalink")def
```


Std.TreeMap.all.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (p : α → β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.TreeMap.all.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (p : α → β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Check if all elements satisfy the predicate, short-circuiting if a predicate fails.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.any "Permalink")def
```


Std.TreeMap.any.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (p : α → β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.TreeMap.any.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp)
  (p : α → β → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Check if any element satisfies the predicate, short-circuiting if a predicate fails.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.foldl "Permalink")def
```


Std.TreeMap.foldl.{u, v, w} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {δ : Type w} (f : δ → α → β → δ) (init : δ)
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : δ


Std.TreeMap.foldl.{u, v, w} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {δ : Type w} (f : δ → α → β → δ)
  (init : δ) (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : δ


```

Folds the given function over the mappings in the map in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.foldlM "Permalink")def
```


Std.TreeMap.foldlM.{u, v, w, w₂} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {δ : Type w} {m : Type w → Type w₂} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : δ → α → β → m δ) (init : δ) (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : m δ


Std.TreeMap.foldlM.{u, v, w, w₂}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {δ : Type w}
  {m : Type w → Type w₂} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : δ → α → β → m δ) (init : δ)
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : m δ


```

Folds the given monadic function over the mappings in the map in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.foldr "Permalink")def
```


Std.TreeMap.foldr.{u, v, w} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {δ : Type w} (f : α → β → δ → δ) (init : δ)
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : δ


Std.TreeMap.foldr.{u, v, w} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {δ : Type w} (f : α → β → δ → δ)
  (init : δ) (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : δ


```

Folds the given function over the mappings in the map in descending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.foldrM "Permalink")def
```


Std.TreeMap.foldrM.{u, v, w, w₂} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {δ : Type w} {m : Type w → Type w₂} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → β → δ → m δ) (init : δ) (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : m δ


Std.TreeMap.foldrM.{u, v, w, w₂}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {δ : Type w}
  {m : Type w → Type w₂} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → β → δ → m δ) (init : δ)
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : m δ


```

Folds the given monadic function over the mappings in the map in descending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.forIn "Permalink")def
```


Std.TreeMap.forIn.{u, v, w, w₂} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {δ : Type w} {m : Type w → Type w₂} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → β → δ → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") δ)) (init : δ)
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : m δ


Std.TreeMap.forIn.{u, v, w, w₂}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {δ : Type w}
  {m : Type w → Type w₂} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → β → δ → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") δ))
  (init : δ) (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) :
  m δ


```

Support for the `for` loop construct in `do` blocks. Iteration happens in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.forM "Permalink")def
```


Std.TreeMap.forM.{u, v, w, w₂} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {m : Type w → Type w₂} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → β → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


Std.TreeMap.forM.{u, v, w, w₂}
  {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {m : Type w → Type w₂} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → β → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit"))
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Carries out a monadic action on each mapping in the tree map in ascending order.
###  20.19.8.6. Conversion[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Tree-Based-Maps--Conversion "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.ofList "Permalink")def
```


Std.TreeMap.ofList.{u, v} {α : Type u} {β : Type v} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod"))
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by exact compare) : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


Std.TreeMap.ofList.{u, v} {α : Type u}
  {β : Type v} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod"))
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by
    exact compare) :
  [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


```

Transforms a list of mappings into a tree map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.toList "Permalink")def
```


Std.TreeMap.toList.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


Std.TreeMap.toList.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Transforms the tree map into a list of mappings in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.ofArray "Permalink")def
```


Std.TreeMap.ofArray.{u, v} {α : Type u} {β : Type v} (a : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod"))
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by exact compare) : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


Std.TreeMap.ofArray.{u, v} {α : Type u}
  {β : Type v} (a : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod"))
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by
    exact compare) :
  [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp


```

Transforms a list of mappings into a tree map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.toArray "Permalink")def
```


Std.TreeMap.toArray.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


Std.TreeMap.toArray.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α β cmp) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")α [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") β[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")


```

Transforms the tree map into a list of mappings in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.unitOfArray "Permalink")def
```


Std.TreeMap.unitOfArray.{u} {α : Type u} (a : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by exact compare) : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") cmp


Std.TreeMap.unitOfArray.{u} {α : Type u}
  (a : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by
    exact compare) :
  [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") cmp


```

Transforms an array of keys into a tree map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.unitOfList "Permalink")def
```


Std.TreeMap.unitOfList.{u} {α : Type u} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by exact compare) : [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") cmp


Std.TreeMap.unitOfList.{u} {α : Type u}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by
    exact compare) :
  [Std.TreeMap](Basic-Types/Maps-and-Sets/#Std___TreeMap "Documentation for Std.TreeMap") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") cmp


```

Transforms a list of keys into a tree map.
####  20.19.8.6.1. Unbundled Variants[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Tree-Based-Maps--Conversion--Unbundled-Variants "Permalink")
Unbundled maps separate well-formedness proofs from data. This is primarily useful when defining [nested inductive types](Basic-Types/Maps-and-Sets/#raw-data). To use these variants, import the module `Std.TreeMap.Raw`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.Raw "Permalink")structure
```


Std.TreeMap.Raw.{u, v} (α : Type u) (β : Type v)
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by exact compare) : Type (max u v)


Std.TreeMap.Raw.{u, v} (α : Type u)
  (β : Type v)
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by
    exact compare) :
  Type (max u v)


```

Tree maps without a bundled well-formedness invariant, suitable for use in nested inductive types. The well-formedness invariant is called `Raw.WF`. When in doubt, prefer `TreeMap` over `TreeMap.Raw`. Lemmas about the operations on `[Std.TreeMap.Raw](Basic-Types/Maps-and-Sets/#Std___TreeMap___Raw___mk "Documentation for Std.TreeMap.Raw")` are available in the module `Std.Data.TreeMap.Raw.Lemmas`.
A tree map stores an assignment of keys to values. It depends on a comparator function that defines an ordering on the keys and provides efficient order-dependent queries, such as retrieval of the minimum or maximum.
To ensure that the operations behave as expected, the comparator function `cmp` should satisfy certain laws that ensure a consistent ordering:
  * If `a` is less than (or equal) to `b`, then `b` is greater than (or equal) to `a` and vice versa (see the `OrientedCmp` typeclass).
  * If `a` is less than or equal to `b` and `b` is, in turn, less than or equal to `c`, then `a` is less than or equal to `c` (see the `TransCmp` typeclass).


Keys for which `cmp a b = [Ordering.eq](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.eq")` are considered the same, i.e., there can be only one entry with key either `a` or `b` in a tree map. Looking up either `a` or `b` always yields the same entry, if any is present.
To avoid expensive copies, users should make sure that the tree map is used linearly.
Internally, the tree maps are represented as size-bounded trees, a type of self-balancing binary search tree with efficient order statistic lookups.
#  Constructor

```
[Std.TreeMap.Raw.mk](Basic-Types/Maps-and-Sets/#Std___TreeMap___Raw___mk "Documentation for Std.TreeMap.Raw.mk").{u, v}
```

#  Fields

```
inner : [Std.DTreeMap.Raw](Basic-Types/Maps-and-Sets/#Std___DTreeMap___Raw___mk "Documentation for Std.DTreeMap.Raw") α (fun x => β) cmp
```

Internal implementation detail of the tree map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeMap.Raw.WF.mk "Permalink")structure
```


Std.TreeMap.Raw.WF.{u, v} {α : Type u} {β : Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.TreeMap.Raw](Basic-Types/Maps-and-Sets/#Std___TreeMap___Raw___mk "Documentation for Std.TreeMap.Raw") α β cmp) : Prop


Std.TreeMap.Raw.WF.{u, v} {α : Type u}
  {β : Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeMap.Raw](Basic-Types/Maps-and-Sets/#Std___TreeMap___Raw___mk "Documentation for Std.TreeMap.Raw") α β cmp) : Prop


```

Well-formedness predicate for tree maps. Users of `TreeMap` will not need to interact with this. Users of `TreeMap.Raw` will need to provide proofs of `WF` to lemmas and should use lemmas like `WF.empty` and `WF.insert` (which are always named exactly like the operations they are about) to show that map operations preserve well-formedness. The constructors of this type are internal implementation details and should not be accessed by users.
#  Constructor

```
[Std.TreeMap.Raw.WF.mk](Basic-Types/Maps-and-Sets/#Std___TreeMap___Raw___WF___mk "Documentation for Std.TreeMap.Raw.WF.mk").{u, v}
```

#  Fields

```
out : t.[inner](Basic-Types/Maps-and-Sets/#Std___TreeMap___Raw___mk "Documentation for Std.TreeMap.Raw.inner").[WF](Basic-Types/Maps-and-Sets/#Std___DTreeMap___Raw___WF___mk "Documentation for Std.DTreeMap.Raw.WF")
```

Internal implementation detail of the tree map.
##  20.19.9. Dependent Tree-Based Maps[🔗](find/?domain=Verso.Genre.Manual.section&name=DTreeMap "Permalink")
The declarations in this section should be imported using `import Std.DTreeMap`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap "Permalink")structure
```


Std.DTreeMap.{u, v} (α : Type u) (β : α → Type v)
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by exact compare) : Type (max u v)


Std.DTreeMap.{u, v} (α : Type u)
  (β : α → Type v)
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by
    exact compare) :
  Type (max u v)


```

Dependent tree maps.
A tree map stores an assignment of keys to values. It depends on a comparator function that defines an ordering on the keys and provides efficient order-dependent queries, such as retrieval of the minimum or maximum.
To ensure that the operations behave as expected, the comparator function `cmp` should satisfy certain laws that ensure a consistent ordering:
  * If `a` is less than (or equal) to `b`, then `b` is greater than (or equal) to `a` and vice versa (see the `OrientedCmp` typeclass).
  * If `a` is less than or equal to `b` and `b` is, in turn, less than or equal to `c`, then `a` is less than or equal to `c` (see the `TransCmp` typeclass).


Keys for which `cmp a b = [Ordering.eq](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.eq")` are considered the same, i.e., there can be only one entry with key either `a` or `b` in a tree map. Looking up either `a` or `b` always yields the same entry, if any is present. The `get` operations of the _dependent_ tree map additionally require a `LawfulEqCmp` instance to ensure that `cmp a b = [.eq](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.eq")` always implies `a = b`, so that their respective value types are equal.
To avoid expensive copies, users should make sure that the tree map is used linearly.
Internally, the tree maps are represented as size-bounded trees, a type of self-balancing binary search tree with efficient order statistic lookups.
For use in proofs, the type `Std.ExtDTreeMap` of extensional dependent tree maps should be preferred. This type comes with several extensionality lemmas and provides the same functions but requires a `TransCmp` instance to work with.
These tree maps contain a bundled well-formedness invariant, which means that they cannot be used in nested inductive types. For these use cases, `[Std.DTreeMap.Raw](Basic-Types/Maps-and-Sets/#Std___DTreeMap___Raw___mk "Documentation for Std.DTreeMap.Raw")` and `[Std.DTreeMap.Raw.WF](Basic-Types/Maps-and-Sets/#Std___DTreeMap___Raw___WF___mk "Documentation for Std.DTreeMap.Raw.WF")` unbundle the invariant from the tree map. When in doubt, prefer `DTreeMap` over `DTreeMap.Raw`.
###  20.19.9.1. Creation[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Dependent-Tree-Based-Maps--Creation "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.empty "Permalink")def
```


Std.DTreeMap.empty.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


Std.DTreeMap.empty.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} :
  [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


```

Creates a new empty tree map. It is also possible and recommended to use the empty collection notations `∅` and `{}` to create an empty tree map. `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` replaces `empty` with `∅`.
###  20.19.9.2. Properties[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Dependent-Tree-Based-Maps--Properties "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.size "Permalink")def
```


Std.DTreeMap.size.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Std.DTreeMap.size.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the number of mappings present in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.isEmpty "Permalink")def
```


Std.DTreeMap.isEmpty.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.DTreeMap.isEmpty.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the tree map contains no mappings.
###  20.19.9.3. Queries[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Dependent-Tree-Based-Maps--Queries "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.contains "Permalink")def
```


Std.DTreeMap.contains.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.DTreeMap.contains.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if there is a mapping for the given key `a` or a key that is equal to `a` according to the comparator `cmp`. There is also a `Prop`-valued version of this: `a ∈ t` is equivalent to `t.[contains](Basic-Types/Maps-and-Sets/#Std___DTreeMap___contains "Documentation for Std.DTreeMap.contains") a = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Observe that this is different behavior than for lists: for lists, `∈` uses `=` and `contains` uses `==` for equality checks, while for tree maps, both use the given comparator `cmp`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.get "Permalink")def
```


Std.DTreeMap.get.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [Std.LawfulEqCmp cmp]
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α) (h : a ∈ t) : β a


Std.DTreeMap.get.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.LawfulEqCmp cmp]
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α)
  (h : a ∈ t) : β a


```

Given a proof that a mapping for the given key is present, retrieves the mapping for the given key.
Uses the `LawfulEqCmp` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.get! "Permalink")def
```


Std.DTreeMap.get!.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [Std.LawfulEqCmp cmp]
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α) [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") (β a)] : β a


Std.DTreeMap.get!.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.LawfulEqCmp cmp]
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α)
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") (β a)] : β a


```

Tries to retrieve the mapping for the given key, panicking if no such mapping is present.
Uses the `LawfulEqCmp` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.get? "Permalink")def
```


Std.DTreeMap.get?.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [Std.LawfulEqCmp cmp]
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a)


Std.DTreeMap.get?.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.LawfulEqCmp cmp]
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a)


```

Tries to retrieve the mapping for the given key, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such mapping is present.
Uses the `LawfulEqCmp` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.getD "Permalink")def
```


Std.DTreeMap.getD.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [Std.LawfulEqCmp cmp]
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α) (fallback : β a) : β a


Std.DTreeMap.getD.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.LawfulEqCmp cmp]
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α)
  (fallback : β a) : β a


```

Tries to retrieve the mapping for the given key, returning `fallback` if no such mapping is present.
Uses the `LawfulEqCmp` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.getKey "Permalink")def
```


Std.DTreeMap.getKey.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α)
  (h : a ∈ t) : α


Std.DTreeMap.getKey.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α)
  (h : a ∈ t) : α


```

Retrieves the key from the mapping that matches `a`. Ensures that such a mapping exists by requiring a proof of `a ∈ m`. The result is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.getKey! "Permalink")def
```


Std.DTreeMap.getKey!.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp)
  (a : α) : α


Std.DTreeMap.getKey!.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α) : α


```

Checks if a mapping for the given key exists and returns the key if it does, otherwise panics. If no panic occurs the result is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.getKey? "Permalink")def
```


Std.DTreeMap.getKey?.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.DTreeMap.getKey?.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Checks if a mapping for the given key exists and returns the key if it does, otherwise `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`. The result in the `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` case is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.getKeyD "Permalink")def
```


Std.DTreeMap.getKeyD.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a fallback : α) :
  α


Std.DTreeMap.getKeyD.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp)
  (a fallback : α) : α


```

Checks if a mapping for the given key exists and returns the key if it does, otherwise `fallback`. If a mapping exists the result is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.keys "Permalink")def
```


Std.DTreeMap.keys.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


Std.DTreeMap.keys.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Returns a list of all keys present in the tree map in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.keysArray "Permalink")def
```


Std.DTreeMap.keysArray.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Std.DTreeMap.keysArray.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Returns an array of all keys present in the tree map in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.values "Permalink")def
```


Std.DTreeMap.values.{u, v} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {β : Type v} (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α (fun x => β) cmp) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


Std.DTreeMap.values.{u, v} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {β : Type v}
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α (fun x => β) cmp) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") β


```

Returns a list of all values present in the tree map in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.valuesArray "Permalink")def
```


Std.DTreeMap.valuesArray.{u, v} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {β : Type v} (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α (fun x => β) cmp) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


Std.DTreeMap.valuesArray.{u, v}
  {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {β : Type v}
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α (fun x => β) cmp) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") β


```

Returns an array of all values present in the tree map in ascending order.
###  20.19.9.4. Modification[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Dependent-Tree-Based-Maps--Modification "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.alter "Permalink")def
```


Std.DTreeMap.alter.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [Std.LawfulEqCmp cmp]
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α) (f : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a) → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a)) :
  [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


Std.DTreeMap.alter.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.LawfulEqCmp cmp]
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α)
  (f : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a) → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a)) :
  [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


```

Modifies in place the value associated with a given key, allowing creating new values and deleting values via an `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option")` valued replacement function.
This function ensures that the value is used linearly.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.modify "Permalink")def
```


Std.DTreeMap.modify.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [Std.LawfulEqCmp cmp]
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α) (f : β a → β a) :
  [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


Std.DTreeMap.modify.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.LawfulEqCmp cmp]
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α)
  (f : β a → β a) : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


```

Modifies in place the value associated with a given key.
This function ensures that the value is used linearly.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.containsThenInsert "Permalink")def
```


Std.DTreeMap.containsThenInsert.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α)
  (b : β a) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


Std.DTreeMap.containsThenInsert.{u, v}
  {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α)
  (b : β a) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


```

Checks whether a key is present in a map and unconditionally inserts a value for the key.
Equivalent to (but potentially faster than) calling `contains` followed by `insert`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.containsThenInsertIfNew "Permalink")def
```


Std.DTreeMap.containsThenInsertIfNew.{u, v} {α : Type u}
  {β : α → Type v} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp)
  (a : α) (b : β a) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


Std.DTreeMap.containsThenInsertIfNew.{u,
    v}
  {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α)
  (b : β a) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


```

Checks whether a key is present in a map and inserts a value for the key if it was not found. If the returned `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, then the returned map is unaltered. If the `[Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, then the returned map has a new value inserted.
Equivalent to (but potentially faster than) calling `contains` followed by `insertIfNew`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.erase "Permalink")def
```


Std.DTreeMap.erase.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α) :
  [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


Std.DTreeMap.erase.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α) :
  [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


```

Removes the mapping for the given key if it exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.filter "Permalink")def
```


Std.DTreeMap.filter.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (f : (a : α) → β a → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


Std.DTreeMap.filter.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (f : (a : α) → β a → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) :
  [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


```

Removes all mappings of the map for which the given function returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.filterMap "Permalink")def
```


Std.DTreeMap.filterMap.{u, v, w} {α : Type u} {β : α → Type v}
  {γ : α → Type w} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (f : (a : α) → β a → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (γ a)) (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) :
  [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α γ cmp


Std.DTreeMap.filterMap.{u, v, w}
  {α : Type u} {β : α → Type v}
  {γ : α → Type w}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (f : (a : α) → β a → [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (γ a))
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) :
  [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α γ cmp


```

Updates the values of the map by applying the given function to all mappings, keeping only those mappings where the function returns `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` value.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.insert "Permalink")def
```


Std.DTreeMap.insert.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α)
  (b : β a) : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


Std.DTreeMap.insert.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α)
  (b : β a) : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


```

Inserts the given mapping into the map. If there is already a mapping for the given key, then both key and value will be replaced.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.insertIfNew "Permalink")def
```


Std.DTreeMap.insertIfNew.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α)
  (b : β a) : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


Std.DTreeMap.insertIfNew.{u, v}
  {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α)
  (b : β a) : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


```

If there is no mapping for the given key, inserts the given mapping into the map. Otherwise, returns the map unaltered.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.getThenInsertIfNew? "Permalink")def
```


Std.DTreeMap.getThenInsertIfNew?.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [Std.LawfulEqCmp cmp]
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α) (b : β a) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a) [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


Std.DTreeMap.getThenInsertIfNew?.{u, v}
  {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.LawfulEqCmp cmp]
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (a : α)
  (b : β a) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") (β a) [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


```

Checks whether a key is present in a map, returning the associated value, and inserts a value for the key if it was not found.
If the returned value is `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") v`, then the returned map is unaltered. If it is `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, then the returned map has a new value inserted.
Equivalent to (but potentially faster than) calling `get?` followed by `insertIfNew`.
Uses the `LawfulEqCmp` instance to cast the retrieved value to the correct type.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.insertMany "Permalink")def
```


Std.DTreeMap.insertMany.{u, v, u_1} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {ρ : Type u_1} [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ ((a : α) × β a)]
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (l : ρ) : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


Std.DTreeMap.insertMany.{u, v, u_1}
  {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {ρ : Type u_1}
  [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ ((a : α) × β a)]
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) (l : ρ) :
  [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


```

Inserts multiple mappings into the tree map by iterating over the given collection and calling `insert`. If the same key appears multiple times, the last occurrence takes precedence.
Note: this precedence behavior is true for `TreeMap`, `DTreeMap`, `TreeMap.Raw` and `DTreeMap.Raw`. The `insertMany` function on `TreeSet` and `TreeSet.Raw` behaves differently: it will prefer the first appearance.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.partition "Permalink")def
```


Std.DTreeMap.partition.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (f : (a : α) → β a → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) :
  [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


Std.DTreeMap.partition.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (f : (a : α) → β a → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) :
  [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")
    [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


```

Partitions a tree map into two tree maps based on a predicate.
###  20.19.9.5. Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Dependent-Tree-Based-Maps--Iteration "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.iter "Permalink")def
```


Std.DTreeMap.iter.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (m : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") ((a : α) × β a)


Std.DTreeMap.iter.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (m : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") ((a : α) × β a)


```

Returns a finite iterator over the entries of a dependent tree map. The iterator yields the elements of the map in order and then terminates.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.keysIter "Permalink")def
```


Std.DTreeMap.keysIter.{u} {α : Type u} {β : α → Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (m : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") α


Std.DTreeMap.keysIter.{u} {α : Type u}
  {β : α → Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (m : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") α


```

Returns a finite iterator over the keys of a dependent tree map. The iterator yields the keys in order and then terminates.
The key and value types must live in the same universe.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.valuesIter "Permalink")def
```


Std.DTreeMap.valuesIter.{u} {α β : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (m : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α (fun x => β) cmp) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


Std.DTreeMap.valuesIter.{u} {α β : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (m : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α (fun x => β) cmp) :
  [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") β


```

Returns a finite iterator over the values of a tree map. The iterator yields the values in order and then terminates.
The key and value types must live in the same universe.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.map "Permalink")def
```


Std.DTreeMap.map.{u, v, w} {α : Type u} {β : α → Type v}
  {γ : α → Type w} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (f : (a : α) → β a → γ a)
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α γ cmp


Std.DTreeMap.map.{u, v, w} {α : Type u}
  {β : α → Type v} {γ : α → Type w}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (f : (a : α) → β a → γ a)
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) :
  [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α γ cmp


```

Updates the values of the map by applying the given function to all mappings.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.foldl "Permalink")def
```


Std.DTreeMap.foldl.{u, v, w} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {δ : Type w} (f : δ → (a : α) → β a → δ)
  (init : δ) (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) : δ


Std.DTreeMap.foldl.{u, v, w} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {δ : Type w}
  (f : δ → (a : α) → β a → δ) (init : δ)
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) : δ


```

Folds the given function over the mappings in the map in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.foldlM "Permalink")def
```


Std.DTreeMap.foldlM.{u, v, w, w₂} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {δ : Type w} {m : Type w → Type w₂} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : δ → (a : α) → β a → m δ) (init : δ) (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) :
  m δ


Std.DTreeMap.foldlM.{u, v, w, w₂}
  {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {δ : Type w}
  {m : Type w → Type w₂} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : δ → (a : α) → β a → m δ) (init : δ)
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) : m δ


```

Folds the given monadic function over the mappings in the map in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.forIn "Permalink")def
```


Std.DTreeMap.forIn.{u, v, w, w₂} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {δ : Type w} {m : Type w → Type w₂} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : (a : α) → β a → δ → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") δ)) (init : δ)
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) : m δ


Std.DTreeMap.forIn.{u, v, w, w₂}
  {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {δ : Type w}
  {m : Type w → Type w₂} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f :
    (a : α) → β a → δ → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") δ))
  (init : δ) (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) :
  m δ


```

Support for the `for` loop construct in `do` blocks. Iteration happens in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.forM "Permalink")def
```


Std.DTreeMap.forM.{u, v, w, w₂} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {m : Type w → Type w₂} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : (a : α) → β a → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")) (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


Std.DTreeMap.forM.{u, v, w, w₂}
  {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {m : Type w → Type w₂} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : (a : α) → β a → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit"))
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Carries out a monadic action on each mapping in the tree map in ascending order.
###  20.19.9.6. Conversion[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Dependent-Tree-Based-Maps--Conversion "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.ofList "Permalink")def
```


Std.DTreeMap.ofList.{u, v} {α : Type u} {β : α → Type v}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ((a : α) × β a))
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by exact compare) : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


Std.DTreeMap.ofList.{u, v} {α : Type u}
  {β : α → Type v}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ((a : α) × β a))
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by
    exact compare) :
  [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp


```

Transforms a list of mappings into a tree map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.toArray "Permalink")def
```


Std.DTreeMap.toArray.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ((a : α) × β a)


Std.DTreeMap.toArray.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) :
  [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") ((a : α) × β a)


```

Transforms the tree map into a list of mappings in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.toList "Permalink")def
```


Std.DTreeMap.toList.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ((a : α) × β a)


Std.DTreeMap.toList.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.DTreeMap](Basic-Types/Maps-and-Sets/#Std___DTreeMap "Documentation for Std.DTreeMap") α β cmp) :
  [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") ((a : α) × β a)


```

Transforms the tree map into a list of mappings in ascending order.
###  20.19.9.7. Unbundled Variants[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Dependent-Tree-Based-Maps--Unbundled-Variants "Permalink")
Unbundled maps separate well-formedness proofs from data. This is primarily useful when defining [nested inductive types](Basic-Types/Maps-and-Sets/#raw-data). To use these variants, import the module `Std.DTreeMap.Raw`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.Raw.inner "Permalink")structure
```


Std.DTreeMap.Raw.{u, v} (α : Type u) (β : α → Type v)
  (_cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by exact compare) : Type (max u v)


Std.DTreeMap.Raw.{u, v} (α : Type u)
  (β : α → Type v)
  (_cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by
    exact compare) :
  Type (max u v)


```

Dependent tree maps without a bundled well-formedness invariant, suitable for use in nested inductive types. The well-formedness invariant is called `Raw.WF`. When in doubt, prefer `DTreeMap` over `DTreeMap.Raw`. Lemmas about the operations on `[Std.DTreeMap.Raw](Basic-Types/Maps-and-Sets/#Std___DTreeMap___Raw___mk "Documentation for Std.DTreeMap.Raw")` are available in the module `Std.Data.DTreeMap.Raw.Lemmas`.
A tree map stores an assignment of keys to values. It depends on a comparator function that defines an ordering on the keys and provides efficient order-dependent queries, such as retrieval of the minimum or maximum.
To ensure that the operations behave as expected, the comparator function `cmp` should satisfy certain laws that ensure a consistent ordering:
  * If `a` is less than (or equal) to `b`, then `b` is greater than (or equal) to `a` and vice versa (see the `OrientedCmp` typeclass).
  * If `a` is less than or equal to `b` and `b` is, in turn, less than or equal to `c`, then `a` is less than or equal to `c` (see the `TransCmp` typeclass).


Keys for which `cmp a b = [Ordering.eq](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.eq")` are considered the same, i.e., there can be only one entry with key either `a` or `b` in a tree map. Looking up either `a` or `b` always yields the same entry, if any is present. The `get` operations of the _dependent_ tree map additionally require a `LawfulEqCmp` instance to ensure that `cmp a b = .eq` always implies `a = b`, so that their respective value types are equal.
To avoid expensive copies, users should make sure that the tree map is used linearly.
Internally, the tree maps are represented as size-bounded trees, a type of self-balancing binary search tree with efficient order statistic lookups.
#  Constructor

```
[Std.DTreeMap.Raw.mk](Basic-Types/Maps-and-Sets/#Std___DTreeMap___Raw___mk "Documentation for Std.DTreeMap.Raw.mk").{u, v}
```

#  Fields

```
inner : Std.DTreeMap.Internal.Impl α β
```

Internal implementation detail of the tree map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.DTreeMap.Raw.WF.out "Permalink")structure
```


Std.DTreeMap.Raw.WF.{u, v} {α : Type u} {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (t : [Std.DTreeMap.Raw](Basic-Types/Maps-and-Sets/#Std___DTreeMap___Raw___mk "Documentation for Std.DTreeMap.Raw") α β cmp) : Prop


Std.DTreeMap.Raw.WF.{u, v} {α : Type u}
  {β : α → Type v}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.DTreeMap.Raw](Basic-Types/Maps-and-Sets/#Std___DTreeMap___Raw___mk "Documentation for Std.DTreeMap.Raw") α β cmp) : Prop


```

Well-formedness predicate for tree maps. Users of `DTreeMap` will not need to interact with this. Users of `DTreeMap.Raw` will need to provide proofs of `WF` to lemmas and should use lemmas like `WF.empty` and `WF.insert` (which are always named exactly like the operations they are about) to show that map operations preserve well-formedness. The constructors of this type are internal implementation details and should not be accessed by users.
#  Constructor

```
[Std.DTreeMap.Raw.WF.mk](Basic-Types/Maps-and-Sets/#Std___DTreeMap___Raw___WF___mk "Documentation for Std.DTreeMap.Raw.WF.mk").{u, v}
```

#  Fields

```
out : t.[inner](Basic-Types/Maps-and-Sets/#Std___DTreeMap___Raw___mk "Documentation for Std.DTreeMap.Raw.inner").WF
```

Internal implementation detail of the tree map.
##  20.19.10. Tree-Based Sets[🔗](find/?domain=Verso.Genre.Manual.section&name=TreeSet "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet "Permalink")structure
```


Std.TreeSet.{u} (α : Type u)
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by exact compare) : Type u


Std.TreeSet.{u} (α : Type u)
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by
    exact compare) :
  Type u


```

Tree sets.
A tree set stores elements of a certain type in a certain order. It depends on a comparator function that defines an ordering on the keys and provides efficient order-dependent queries, such as retrieval of the minimum or maximum.
To ensure that the operations behave as expected, the comparator function `cmp` should satisfy certain laws that ensure a consistent ordering:
  * If `a` is less than (or equal) to `b`, then `b` is greater than (or equal) to `a` and vice versa (see the `OrientedCmp` typeclass).
  * If `a` is less than or equal to `b` and `b` is, in turn, less than or equal to `c`, then `a` is less than or equal to `c` (see the `TransCmp` typeclass).


Keys for which `cmp a b = [Ordering.eq](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.eq")` are considered the same, i.e., there can be only one of them be contained in a single tree set at the same time.
To avoid expensive copies, users should make sure that the tree set is used linearly.
Internally, the tree sets are represented as size-bounded trees, a type of self-balancing binary search tree with efficient order statistic lookups.
For use in proofs, the type `Std.ExtTreeSet` of extensional tree sets should be preferred. This type comes with several extensionality lemmas and provides the same functions but requires a `TransCmp` instance to work with.
These tree sets contain a bundled well-formedness invariant, which means that they cannot be used in nested inductive types. For these use cases, `[Std.TreeSet.Raw](Basic-Types/Maps-and-Sets/#Std___TreeSet___Raw___mk "Documentation for Std.TreeSet.Raw")` and `[Std.TreeSet.Raw.WF](Basic-Types/Maps-and-Sets/#Std___TreeSet___Raw___WF___mk "Documentation for Std.TreeSet.Raw.WF")` unbundle the invariant from the tree set. When in doubt, prefer `TreeSet` over `TreeSet.Raw`.
###  20.19.10.1. Creation[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Tree-Based-Sets--Creation "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.empty "Permalink")def
```


Std.TreeSet.empty.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} :
  [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


Std.TreeSet.empty.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} :
  [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


```

Creates a new empty tree set. It is also possible and recommended to use the empty collection notations `∅` and `{}` to create an empty tree set. `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` replaces `empty` with `∅`.
###  20.19.10.2. Properties[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Tree-Based-Sets--Properties "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.isEmpty "Permalink")def
```


Std.TreeSet.isEmpty.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.TreeSet.isEmpty.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if the tree set contains no mappings.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.size "Permalink")def
```


Std.TreeSet.size.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


Std.TreeSet.size.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


```

Returns the number of mappings present in the map.
###  20.19.10.3. Queries[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Tree-Based-Sets--Queries "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.contains "Permalink")def
```


Std.TreeSet.contains.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (l : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.TreeSet.contains.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (l : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Returns `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` if `a`, or an element equal to `a` according to the comparator `cmp`, is contained in the set. There is also a `Prop`-valued version of this: `a ∈ t` is equivalent to `t.contains a = [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.
Observe that this is different behavior than for lists: for lists, `∈` uses `=` and `contains` uses `==` for equality checks, while for tree sets, both use the given comparator `cmp`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.get "Permalink")def
```


Std.TreeSet.get.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (a : α) (h : a ∈ t) : α


Std.TreeSet.get.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (a : α)
  (h : a ∈ t) : α


```

Retrieves the key from the set that matches `a`. Ensures that such a key exists by requiring a proof of `a ∈ m`. The result is guaranteed to be pointer equal to the key in the set.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.get! "Permalink")def
```


Std.TreeSet.get!.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (a : α) : α


Std.TreeSet.get!.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (a : α) : α


```

Checks if given key is contained and returns the key if it is, otherwise panics. If no panic occurs the result is guaranteed to be pointer equal to the key in the set.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.get? "Permalink")def
```


Std.TreeSet.get?.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (a : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.TreeSet.get?.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (a : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Checks if given key is contained and returns the key if it is, otherwise `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`. The result in the `[some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some")` case is guaranteed to be pointer equal to the key in the map.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.getD "Permalink")def
```


Std.TreeSet.getD.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (a fallback : α) : α


Std.TreeSet.getD.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp)
  (a fallback : α) : α


```

Checks if given key is contained and returns the key if it is, otherwise `fallback`. If they key is contained the result is guaranteed to be pointer equal to the key in the set.
####  20.19.10.3.1. Ordering-Based Queries[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Tree-Based-Sets--Queries--Ordering-Based-Queries "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.atIdx "Permalink")def
```


Std.TreeSet.atIdx.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (h : n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") t.[size](Basic-Types/Maps-and-Sets/#Std___TreeSet___size "Documentation for Std.TreeSet.size")) : α


Std.TreeSet.atIdx.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (h : n [<](Type-Classes/Basic-Classes/#LT___mk "Documentation for LT.lt") t.[size](Basic-Types/Maps-and-Sets/#Std___TreeSet___size "Documentation for Std.TreeSet.size")) : α


```

Returns the `n`-th smallest element.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.atIdx! "Permalink")def
```


Std.TreeSet.atIdx!.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : α


Std.TreeSet.atIdx!.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : α


```

Returns the `n`-th smallest element, or panics if `n` is at least `t.[size](Basic-Types/Maps-and-Sets/#Std___TreeSet___size "Documentation for Std.TreeSet.size")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.atIdx? "Permalink")def
```


Std.TreeSet.atIdx?.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.TreeSet.atIdx?.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Returns the `n`-th smallest element, or `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if `n` is at least `t.[size](Basic-Types/Maps-and-Sets/#Std___TreeSet___size "Documentation for Std.TreeSet.size")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.atIdxD "Permalink")def
```


Std.TreeSet.atIdxD.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (fallback : α) : α


Std.TreeSet.atIdxD.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (n : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))
  (fallback : α) : α


```

Returns the `n`-th smallest element, or `fallback` if `n` is at least `t.[size](Basic-Types/Maps-and-Sets/#Std___TreeSet___size "Documentation for Std.TreeSet.size")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.getGE "Permalink")def
```


Std.TreeSet.getGE.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.TransCmp cmp] (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α)
  (h : [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") (cmp a k).[isGE](Type-Classes/Basic-Classes/#Ordering___isGE "Documentation for Ordering.isGE") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : α


Std.TreeSet.getGE.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.TransCmp cmp]
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α)
  (h :
    [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") (cmp a k).[isGE](Type-Classes/Basic-Classes/#Ordering___isGE "Documentation for Ordering.isGE") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) :
  α


```

Given a proof that such an element exists, retrieves the smallest element that is greater than or equal to the given element.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.getGE! "Permalink")def
```


Std.TreeSet.getGE!.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α) : α


Std.TreeSet.getGE!.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α) : α


```

Tries to retrieve the smallest element that is greater than or equal to the given element, panicking if no such element exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.getGE? "Permalink")def
```


Std.TreeSet.getGE?.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.TreeSet.getGE?.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Tries to retrieve the smallest element that is greater than or equal to the given element, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such element exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.getGED "Permalink")def
```


Std.TreeSet.getGED.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k fallback : α) : α


Std.TreeSet.getGED.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp)
  (k fallback : α) : α


```

Tries to retrieve the smallest element that is greater than or equal to the given element, returning `fallback` if no such element exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.getGT "Permalink")def
```


Std.TreeSet.getGT.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.TransCmp cmp] (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α)
  (h : [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") cmp a k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Ordering.gt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.gt")) : α


Std.TreeSet.getGT.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.TransCmp cmp]
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α)
  (h :
    [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") cmp a k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Ordering.gt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.gt")) :
  α


```

Given a proof that such an element exists, retrieves the smallest element that is greater than the given element.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.getGT! "Permalink")def
```


Std.TreeSet.getGT!.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α) : α


Std.TreeSet.getGT!.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α) : α


```

Tries to retrieve the smallest element that is greater than the given element, panicking if no such element exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.getGT? "Permalink")def
```


Std.TreeSet.getGT?.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.TreeSet.getGT?.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Tries to retrieve the smallest element that is greater than the given element, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such element exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.getGTD "Permalink")def
```


Std.TreeSet.getGTD.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k fallback : α) : α


Std.TreeSet.getGTD.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp)
  (k fallback : α) : α


```

Tries to retrieve the smallest element that is greater than the given element, returning `fallback` if no such element exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.getLE "Permalink")def
```


Std.TreeSet.getLE.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.TransCmp cmp] (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α)
  (h : [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") (cmp a k).[isLE](Type-Classes/Basic-Classes/#Ordering___isLE "Documentation for Ordering.isLE") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) : α


Std.TreeSet.getLE.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.TransCmp cmp]
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α)
  (h :
    [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") (cmp a k).[isLE](Type-Classes/Basic-Classes/#Ordering___isLE "Documentation for Ordering.isLE") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")) :
  α


```

Given a proof that such an element exists, retrieves the largest element that is less than or equal to the given element.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.getLE! "Permalink")def
```


Std.TreeSet.getLE!.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α) : α


Std.TreeSet.getLE!.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α) : α


```

Tries to retrieve the largest element that is less than or equal to the given element, panicking if no such element exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.getLE? "Permalink")def
```


Std.TreeSet.getLE?.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.TreeSet.getLE?.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Tries to retrieve the largest element that is less than or equal to the given element, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such element exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.getLED "Permalink")def
```


Std.TreeSet.getLED.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k fallback : α) : α


Std.TreeSet.getLED.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp)
  (k fallback : α) : α


```

Tries to retrieve the largest element that is less than or equal to the given element, returning `fallback` if no such element exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.getLT "Permalink")def
```


Std.TreeSet.getLT.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.TransCmp cmp] (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α)
  (h : [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") cmp a k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Ordering.lt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.lt")) : α


Std.TreeSet.getLT.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [Std.TransCmp cmp]
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α)
  (h :
    [∃](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a[,](Basic-Propositions/Quantifiers/#Exists___intro "Documentation for Exists") a ∈ t [∧](Basic-Propositions/Logical-Connectives/#And___intro "Documentation for And") cmp a k [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [Ordering.lt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.lt")) :
  α


```

Given a proof that such an element exists, retrieves the smallest element that is less than the given element.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.getLT! "Permalink")def
```


Std.TreeSet.getLT!.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α] (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α) : α


Std.TreeSet.getLT!.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α) : α


```

Tries to retrieve the smallest element that is less than the given element, panicking if no such element exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.getLT? "Permalink")def
```


Std.TreeSet.getLT?.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.TreeSet.getLT?.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k : α) :
  [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Tries to retrieve the smallest element that is less than the given element, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if no such element exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.getLTD "Permalink")def
```


Std.TreeSet.getLTD.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (k fallback : α) : α


Std.TreeSet.getLTD.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp)
  (k fallback : α) : α


```

Tries to retrieve the smallest element that is less than the given element, returning `fallback` if no such element exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.min "Permalink")def
```


Std.TreeSet.min.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (h : t.[isEmpty](Basic-Types/Maps-and-Sets/#Std___TreeSet___isEmpty "Documentation for Std.TreeSet.isEmpty") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : α


Std.TreeSet.min.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp)
  (h : t.[isEmpty](Basic-Types/Maps-and-Sets/#Std___TreeSet___isEmpty "Documentation for Std.TreeSet.isEmpty") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : α


```

Given a proof that the tree set is not empty, retrieves the smallest element.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.min! "Permalink")def
```


Std.TreeSet.min!.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : α


Std.TreeSet.min!.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : α


```

Tries to retrieve the smallest element of the tree set, panicking if the set is empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.min? "Permalink")def
```


Std.TreeSet.min?.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.TreeSet.min?.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Tries to retrieve the smallest element of the tree set, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the set is empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.minD "Permalink")def
```


Std.TreeSet.minD.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (fallback : α) : α


Std.TreeSet.minD.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (fallback : α) :
  α


```

Tries to retrieve the smallest element of the tree set, returning `fallback` if the tree set is empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.max "Permalink")def
```


Std.TreeSet.max.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (h : t.[isEmpty](Basic-Types/Maps-and-Sets/#Std___TreeSet___isEmpty "Documentation for Std.TreeSet.isEmpty") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : α


Std.TreeSet.max.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp)
  (h : t.[isEmpty](Basic-Types/Maps-and-Sets/#Std___TreeSet___isEmpty "Documentation for Std.TreeSet.isEmpty") [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) : α


```

Given a proof that the tree set is not empty, retrieves the largest element.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.max! "Permalink")def
```


Std.TreeSet.max!.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : α


Std.TreeSet.max!.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} [[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") α]
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : α


```

Tries to retrieve the largest element of the tree set, panicking if the set is empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.max? "Permalink")def
```


Std.TreeSet.max?.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


Std.TreeSet.max?.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α


```

Tries to retrieve the largest element of the tree set, returning `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")` if the set is empty.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.maxD "Permalink")def
```


Std.TreeSet.maxD.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (fallback : α) : α


Std.TreeSet.maxD.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (fallback : α) :
  α


```

Tries to retrieve the largest element of the tree set, returning `fallback` if the tree set is empty.
###  20.19.10.4. Modification[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Tree-Based-Sets--Modification "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.insert "Permalink")def
```


Std.TreeSet.insert.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (l : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (a : α) : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


Std.TreeSet.insert.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (l : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (a : α) :
  [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


```

Inserts the given element into the set. If the tree set already contains an element that is equal (with regard to `cmp`) to the given element, then the tree set is returned unchanged.
Note: this non-replacement behavior is true for `TreeSet` and `TreeSet.Raw`. The `insert` function on `TreeMap`, `DTreeMap`, `TreeMap.Raw` and `DTreeMap.Raw` behaves differently: it will overwrite an existing mapping.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.insertMany "Permalink")def
```


Std.TreeSet.insertMany.{u, u_1} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {ρ : Type u_1} [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ α] (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (l : ρ) :
  [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


Std.TreeSet.insertMany.{u, u_1}
  {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {ρ : Type u_1} [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ α]
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (l : ρ) :
  [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


```

Inserts multiple elements into the tree set by iterating over the given collection and calling `insert`. If the same element (with respect to `cmp`) appears multiple times, the first occurrence takes precedence.
Note: this precedence behavior is true for `TreeSet` and `TreeSet.Raw`. The `insertMany` function on `TreeMap`, `DTreeMap`, `TreeMap.Raw` and `DTreeMap.Raw` behaves differently: it will prefer the last appearance.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.containsThenInsert "Permalink")def
```


Std.TreeSet.containsThenInsert.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (a : α) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


Std.TreeSet.containsThenInsert.{u}
  {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (a : α) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


```

Checks whether an element is present in a set and inserts the element if it was not found. If the tree set already contains an element that is equal (with regard to `cmp` to the given element, then the tree set is returned unchanged.
Equivalent to (but potentially faster than) calling `contains` followed by `insert`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.erase "Permalink")def
```


Std.TreeSet.erase.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (a : α) : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


Std.TreeSet.erase.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (a : α) :
  [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


```

Removes the given key if it exists.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.eraseMany "Permalink")def
```


Std.TreeSet.eraseMany.{u, u_1} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {ρ : Type u_1} [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ α] (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (l : ρ) :
  [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


Std.TreeSet.eraseMany.{u, u_1}
  {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {ρ : Type u_1} [[ForIn](Functors___-Monads-and--do--Notation/Syntax/#ForIn___mk "Documentation for ForIn") [Id](Functors___-Monads-and--do--Notation/Varieties-of-Monads/#Id "Documentation for Id") ρ α]
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (l : ρ) :
  [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


```

Erases multiple items from the tree set by iterating over the given collection and calling erase.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.filter "Permalink")def
```


Std.TreeSet.filter.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (f : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (m : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


Std.TreeSet.filter.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (f : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (m : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) :
  [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


```

Removes all elements from the tree set for which the given function returns `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.merge "Permalink")def
```


Std.TreeSet.merge.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t₁ t₂ : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


Std.TreeSet.merge.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t₁ t₂ : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) :
  [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


```

Returns a set that contains all mappings of `t₁` and `t₂.
This function ensures that `t₁` is used linearly. Hence, as long as `t₁` is unshared, the performance characteristics follow the following imperative description: Iterate over all mappings in `t₂`, inserting them into `t₁`.
Hence, the runtime of this method scales logarithmically in the size of `t₁` and linearly in the size of `t₂` as long as `t₁` is unshared.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.partition "Permalink")def
```


Std.TreeSet.partition.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (f : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) :
  [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


Std.TreeSet.partition.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} (f : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool"))
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) :
  [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


```

Partitions a tree set into two tree sets based on a predicate.
###  20.19.10.5. Iteration[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Tree-Based-Sets--Iteration "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.iter "Permalink")def
```


Std.TreeSet.iter.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (m : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") α


Std.TreeSet.iter.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (m : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : [Std.Iter](Iterators/Iterator-Definitions/#Std___Iter___mk "Documentation for Std.Iter") α


```

Returns a finite iterator over the entries of a tree set. The iterator yields the elements of the set in order and then terminates.
**Termination properties:**
  * `Finite` instance: always
  * `Productive` instance: always


[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.all "Permalink")def
```


Std.TreeSet.all.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.TreeSet.all.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Check if any element satisfies the predicate, short-circuiting if a predicate succeeds.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.any "Permalink")def
```


Std.TreeSet.any.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


Std.TreeSet.any.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) (p : α → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) :
  [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")


```

Check if all elements satisfy the predicate, short-circuiting if a predicate fails.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.foldl "Permalink")def
```


Std.TreeSet.foldl.{u, w} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {δ : Type w} (f : δ → α → δ) (init : δ) (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : δ


Std.TreeSet.foldl.{u, w} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {δ : Type w}
  (f : δ → α → δ) (init : δ)
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : δ


```

Folds the given function over the elements of the tree set in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.foldlM "Permalink")def
```


Std.TreeSet.foldlM.{u, u_1, u_2} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {m : Type u_1 → Type u_2} {δ : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : δ → α → m δ)
  (init : δ) (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : m δ


Std.TreeSet.foldlM.{u, u_1, u_2}
  {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {m : Type u_1 → Type u_2} {δ : Type u_1}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : δ → α → m δ) (init : δ)
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : m δ


```

Monadically computes a value by folding the given function over the elements in the tree set in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.foldr "Permalink")def
```


Std.TreeSet.foldr.{u, w} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {δ : Type w} (f : α → δ → δ) (init : δ) (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : δ


Std.TreeSet.foldr.{u, w} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {δ : Type w}
  (f : α → δ → δ) (init : δ)
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : δ


```

Folds the given function over the elements of the tree set in descending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.foldrM "Permalink")def
```


Std.TreeSet.foldrM.{u, u_1, u_2} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {m : Type u_1 → Type u_2} {δ : Type u_1} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → δ → m δ)
  (init : δ) (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : m δ


Std.TreeSet.foldrM.{u, u_1, u_2}
  {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {m : Type u_1 → Type u_2} {δ : Type u_1}
  [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → δ → m δ) (init : δ)
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : m δ


```

Monadically computes a value by folding the given function over the elements in the tree set in descending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.forIn "Permalink")def
```


Std.TreeSet.forIn.{u, w, w₂} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {δ : Type w} {m : Type w → Type w₂} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → δ → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") δ)) (init : δ) (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : m δ


Std.TreeSet.forIn.{u, w, w₂} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")} {δ : Type w}
  {m : Type w → Type w₂} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → δ → m ([ForInStep](Functors___-Monads-and--do--Notation/Syntax/#ForInStep___done "Documentation for ForInStep") δ)) (init : δ)
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : m δ


```

Support for the `for` loop construct in `do` blocks. The iteration happens in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.forM "Permalink")def
```


Std.TreeSet.forM.{u, w, w₂} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {m : Type w → Type w₂} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m] (f : α → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit"))
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


Std.TreeSet.forM.{u, w, w₂} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  {m : Type w → Type w₂} [[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") m]
  (f : α → m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit"))
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : m [PUnit](Basic-Types/The-Unit-Type/#PUnit___unit "Documentation for PUnit")


```

Carries out a monadic action on each element in the tree set in ascending order.
###  20.19.10.6. Conversion[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Tree-Based-Sets--Conversion "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.toList "Permalink")def
```


Std.TreeSet.toList.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


Std.TreeSet.toList.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α


```

Transforms the tree set into a list of elements in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.ofList "Permalink")def
```


Std.TreeSet.ofList.{u} {α : Type u} (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by exact compare) : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


Std.TreeSet.ofList.{u} {α : Type u}
  (l : [List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α)
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by
    exact compare) :
  [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


```

Transforms a list into a tree set.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.toArray "Permalink")def
```


Std.TreeSet.toArray.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


Std.TreeSet.toArray.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp) : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α


```

Transforms the tree set into an array of elements in ascending order.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.ofArray "Permalink")def
```


Std.TreeSet.ofArray.{u} {α : Type u} (a : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by exact compare) : [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


Std.TreeSet.ofArray.{u} {α : Type u}
  (a : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α)
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by
    exact compare) :
  [Std.TreeSet](Basic-Types/Maps-and-Sets/#Std___TreeSet "Documentation for Std.TreeSet") α cmp


```

Transforms an array into a tree set.
####  20.19.10.6.1. Unbundled Variants[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Basic-Types--Maps-and-Sets--Tree-Based-Sets--Conversion--Unbundled-Variants "Permalink")
Unbundled sets separate well-formedness proofs from data. This is primarily useful when defining [nested inductive types](Basic-Types/Maps-and-Sets/#raw-data). To use these variants, import the module `Std.TreeSet.Raw`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.Raw "Permalink")structure
```


Std.TreeSet.Raw.{u} (α : Type u)
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by exact compare) : Type u


Std.TreeSet.Raw.{u} (α : Type u)
  (cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering") := by
    exact compare) :
  Type u


```

Tree sets without a bundled well-formedness invariant, suitable for use in nested inductive types. The well-formedness invariant is called `Raw.WF`. When in doubt, prefer `TreeSet` over `TreeSet.Raw`. Lemmas about the operations on `[Std.TreeSet.Raw](Basic-Types/Maps-and-Sets/#Std___TreeSet___Raw___mk "Documentation for Std.TreeSet.Raw")` are available in the module `Std.Data.TreeSet.Raw.Lemmas`.
A tree set stores elements of a certain type in a certain order. It depends on a comparator function that defines an ordering on the keys and provides efficient order-dependent queries, such as retrieval of the minimum or maximum.
To ensure that the operations behave as expected, the comparator function `cmp` should satisfy certain laws that ensure a consistent ordering:
  * If `a` is less than (or equal) to `b`, then `b` is greater than (or equal) to `a` and vice versa (see the `OrientedCmp` typeclass).
  * If `a` is less than or equal to `b` and `b` is, in turn, less than or equal to `c`, then `a` is less than or equal to `c` (see the `TransCmp` typeclass).


Keys for which `cmp a b = [Ordering.eq](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.eq")` are considered the same, i.e only one of them can be contained in a single tree set at the same time.
To avoid expensive copies, users should make sure that the tree set is used linearly.
Internally, the tree sets are represented as size-bounded trees, a type of self-balancing binary search tree with efficient order statistic lookups.
#  Constructor

```
[Std.TreeSet.Raw.mk](Basic-Types/Maps-and-Sets/#Std___TreeSet___Raw___mk "Documentation for Std.TreeSet.Raw.mk").{u}
```

#  Fields

```
inner : [Std.TreeMap.Raw](Basic-Types/Maps-and-Sets/#Std___TreeMap___Raw___mk "Documentation for Std.TreeMap.Raw") α [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") cmp
```

Internal implementation detail of the tree set.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Std.TreeSet.Raw.WF.out "Permalink")structure
```


Std.TreeSet.Raw.WF.{u} {α : Type u} {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet.Raw](Basic-Types/Maps-and-Sets/#Std___TreeSet___Raw___mk "Documentation for Std.TreeSet.Raw") α cmp) : Prop


Std.TreeSet.Raw.WF.{u} {α : Type u}
  {cmp : α → α → [Ordering](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering")}
  (t : [Std.TreeSet.Raw](Basic-Types/Maps-and-Sets/#Std___TreeSet___Raw___mk "Documentation for Std.TreeSet.Raw") α cmp) : Prop


```

Well-formedness predicate for tree sets. Users of `TreeSet` will not need to interact with this. Users of `TreeSet.Raw` will need to provide proofs of `WF` to lemmas and should use lemmas like `WF.empty` and `WF.insert` (which are always named exactly like the operations they are about) to show that set operations preserve well-formedness. The constructors of this type are internal implementation details and should not be accessed by users.
#  Constructor

```
[Std.TreeSet.Raw.WF.mk](Basic-Types/Maps-and-Sets/#Std___TreeSet___Raw___WF___mk "Documentation for Std.TreeSet.Raw.WF.mk").{u}
```

#  Fields

```
out : t.[inner](Basic-Types/Maps-and-Sets/#Std___TreeSet___Raw___mk "Documentation for Std.TreeSet.Raw.inner").[WF](Basic-Types/Maps-and-Sets/#Std___TreeMap___Raw___WF___mk "Documentation for Std.TreeMap.Raw.WF")
```

Internal implementation detail of the tree map.
[←20.18. Ranges](Basic-Types/Ranges/#ranges "20.18. Ranges")[20.20. Subtypes→](Basic-Types/Subtypes/#Subtype "20.20. Subtypes")

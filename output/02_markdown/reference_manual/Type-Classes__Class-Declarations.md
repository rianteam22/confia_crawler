[←10. Type Classes](Type-Classes/#type-classes "10. Type Classes")[10.2. Instance Declarations→](Type-Classes/Instance-Declarations/#instance-declarations "10.2. Instance Declarations")
#  10.1. Class Declarations[🔗](find/?domain=Verso.Genre.Manual.section&name=class "Permalink")
Type classes are declared with the ``Lean.Parser.Command.declaration : command```class` keyword.
syntaxType Class Declarations

```
command ::= ...
    | [
declModifiers is the collection of modifiers on a declaration:



  * a doc comment /-- ... -/



  * a list of attributes @[attr1, attr2]



  * a visibility specifier, private or public



  * protected


  * noncomputable


  * unsafe


  * 
partial or nonrec




All modifiers are optional, and have to come in the listed order.
nestedDeclModifiers is the same as declModifiers, but attributes are printed
on the same line as the declaration. It is used for declarations nested inside other syntax,
such as inductive constructors, structure projections, and let rec / where definitions. 
declModifiers](Definitions/Modifiers/#Lean___Parser___Command___declModifiers)
      class 


declId matches foo or foo.{u,v}: an identifier possibly followed by a list of universe names 


declId 


optDeclSig matches the signature of a declaration with optional type: a list of binders and then possibly : type 


bracketedBinder* (: term)?
        (extends (ident : )?term,*)?
        where
        ([
declModifiers is the collection of modifiers on a declaration:



  * a doc comment /-- ... -/



  * a list of attributes @[attr1, attr2]



  * a visibility specifier, private or public



  * protected


  * noncomputable


  * unsafe


  * 
partial or nonrec




All modifiers are optional, and have to come in the listed order.
nestedDeclModifiers is the same as declModifiers, but attributes are printed
on the same line as the declaration. It is used for declarations nested inside other syntax,
such as inductive constructors, structure projections, and let rec / where definitions. 
declModifiers](Definitions/Modifiers/#Lean___Parser___Command___declModifiers) ident ::)?
        structFields
      ([deriving](Type-Classes/Deriving-Instances/#Lean___Parser___Command___optDeriving-next) ident,*)?
```

Declares a new type class.
The ``Lean.Parser.Command.declaration : command```class` declaration creates a new single-constructor inductive type, just as if the ``Lean.Parser.Command.declaration : command```structure` command had been used instead. In fact, the results of the ``Lean.Parser.Command.declaration : command```class` and ``Lean.Parser.Command.declaration : command```structure` commands are almost identical, and features such as default values may be used the same way in both. Please refer to [the documentation for structures](The-Type-System/Inductive-Types/#structures) for more information about default values, inheritance, and other features of structures. The differences between structure and class declarations are: 

Methods instead of fields
    
Instead of creating field projections that take a value of the structure type as an explicit parameter, [methods](Type-Classes/#--tech-term-methods) are created. Each method takes the corresponding instance as an instance-implicit parameter. 

Instance-implicit parent classes
    
The constructor of a class that extends other classes takes its class parents' instances as instance-implicit parameters, rather than explicit parameters. When instances of this class are defined, instance synthesis is used to find the values of inherited fields. Parents that are not classes are still explicit parameters to the underlying constructor. 

Parent projections via instance synthesis
    
Structure field projections make use of [inheritance information](The-Type-System/Inductive-Types/#structure-inheritance) to project parent structure fields from child structure values. Classes instead use instance synthesis: given a child class instance, synthesis will construct the parent; thus, methods are not added to child classes in the same way that projections are added to child structures. 

Registered as class
    
The resulting inductive type is registered as a type class, for which instances may be defined and that may be used as the type of instance-implicit arguments. 

Out and semi-out parameters are considered
    
The `[outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam")` and `[semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam")` [gadgets](Type-Classes/Class-Declarations/#--tech-term-gadgets) have no meaning in structure definitions, but they are used in class definitions to control instance search.
While ``Lean.Parser.Command.declaration : command```deriving` clauses are allowed for class definitions to maintain the parallel between class and structure elaboration, they are not frequently used and should be considered an advanced feature.
No Instances of Non-Classes
Lean rejects instance-implicit parameters of types that are not classes:
`def f [n : `invalid binder annotation, type is not a class instance   [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")  Note: Use the command `set_option checkBinderAnnotations false` to disable the check`[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")] : n = n := rfl `
```
invalid binder annotation, type is not a class instance
  [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")

Note: Use the command `set_option checkBinderAnnotations false` to disable the check
```

Class vs Structure Constructors
A very small algebraic hierarchy can be represented either as structures (`[S.Magma](Type-Classes/Class-Declarations/#S___Magma-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example")`, `[S.Semigroup](Type-Classes/Class-Declarations/#S___Semigroup-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example")`, and `[S.Monoid](Type-Classes/Class-Declarations/#S___Monoid-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example")` below), a mix of structures and classes (`[C1.Monoid](Type-Classes/Class-Declarations/#C1___Monoid-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example")`), or only using classes (`[C2.Magma](Type-Classes/Class-Declarations/#C2___Magma-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example")`, `[C2.Semigroup](Type-Classes/Class-Declarations/#C2___Semigroup-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example")`, and `[C2.Monoid](Type-Classes/Class-Declarations/#C2___Monoid-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example")`):
`[namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") S structure Magma (α : Type u) where   op : α → α → α  structure Semigroup (α : Type u) extends [Magma](Type-Classes/Class-Declarations/#S___Magma-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") α where   op_assoc : ∀ x y z, op (op x y) z = op x (op y z)  structure Monoid (α : Type u) extends [Semigroup](Type-Classes/Class-Declarations/#S___Semigroup-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") α where   ident : α   ident_left : ∀ x, op ident x = x   ident_right : ∀ x, op x ident = x end S  [namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") C1 class Monoid (α : Type u) extends [S.Semigroup](Type-Classes/Class-Declarations/#S___Semigroup-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") α where   ident : α   ident_left : ∀ x, op ident x = x   ident_right : ∀ x, op x ident = x end C1  [namespace](Namespaces-and-Sections/#Lean___Parser___Command___namespace "Documentation for syntax") C2 class Magma (α : Type u) where   op : α → α → α  class Semigroup (α : Type u) extends [Magma](Type-Classes/Class-Declarations/#C2___Magma-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") α where   op_assoc : ∀ x y z, op (op x y) z = op x (op y z)  class Monoid (α : Type u) extends [Semigroup](Type-Classes/Class-Declarations/#C2___Semigroup-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") α where   ident : α   ident_left : ∀ x, op ident x = x   ident_right : ∀ x, op x ident = x end C2 `
`S.Monoid.mk` and `C1.Monoid.mk` have identical signatures, because the parent of the class `[C1.Monoid](Type-Classes/Class-Declarations/#C1___Monoid-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example")` is not itself a class:
`S.Monoid.mk.{u} {α : Type u}   (toSemigroup : [S.Semigroup](Type-Classes/Class-Declarations/#S___Semigroup-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") α)   (ident : α)   (ident_left : ∀ (x : α), toSemigroup.[op](Type-Classes/Class-Declarations/#S___Magma___op-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") ident x = x)   (ident_right : ∀ (x : α), toSemigroup.[op](Type-Classes/Class-Declarations/#S___Magma___op-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") x ident = x) :   [S.Monoid](Type-Classes/Class-Declarations/#S___Monoid-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") α``C1.Monoid.mk.{u} {α : Type u}   (toSemigroup : [S.Semigroup](Type-Classes/Class-Declarations/#S___Semigroup-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") α)   (ident : α)   (ident_left : ∀ (x : α), toSemigroup.[op](Type-Classes/Class-Declarations/#S___Magma___op-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") ident x = x)   (ident_right : ∀ (x : α), toSemigroup.[op](Type-Classes/Class-Declarations/#S___Magma___op-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") x ident = x) :   [C1.Monoid](Type-Classes/Class-Declarations/#C1___Monoid-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") α`
Similarly, because neither `S.Magma` nor `C2.Magma` inherits from another structure or class, their constructors are identical:
`S.Magma.mk.{u} {α : Type u} (op : α → α → α) : [S.Magma](Type-Classes/Class-Declarations/#S___Magma-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") α``C2.Magma.mk.{u} {α : Type u} (op : α → α → α) : [C2.Magma](Type-Classes/Class-Declarations/#C2___Magma-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") α`
`S.Semigroup.mk`, however, takes its parent as an ordinary parameter, while `C2.Semigroup.mk` takes its parent as an instance implicit parameter:
`S.Semigroup.mk.{u} {α : Type u}   (toMagma : [S.Magma](Type-Classes/Class-Declarations/#S___Magma-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") α)   (op_assoc : ∀ (x y z : α),     toMagma.[op](Type-Classes/Class-Declarations/#S___Magma___op-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") (toMagma.[op](Type-Classes/Class-Declarations/#S___Magma___op-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") x y) z = toMagma.[op](Type-Classes/Class-Declarations/#S___Magma___op-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") x (toMagma.[op](Type-Classes/Class-Declarations/#S___Magma___op-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") y z)) :   [S.Semigroup](Type-Classes/Class-Declarations/#S___Semigroup-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") α``C2.Semigroup.mk.{u} {α : Type u} [toMagma : [C2.Magma](Type-Classes/Class-Declarations/#C2___Magma-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") α]   (op_assoc : ∀ (x y z : α),     toMagma.[op](Type-Classes/Class-Declarations/#C2___Magma___op-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") (toMagma.[op](Type-Classes/Class-Declarations/#C2___Magma___op-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") x y) z = toMagma.[op](Type-Classes/Class-Declarations/#C2___Magma___op-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") x (toMagma.[op](Type-Classes/Class-Declarations/#C2___Magma___op-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") y z)) :   [C2.Semigroup](Type-Classes/Class-Declarations/#C2___Semigroup-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") α`
Finally, `C2.Monoid.mk` takes its semigroup parent as an instance implicit parameter. The references to `op` become references to the method `[C2.Magma.op](Type-Classes/Class-Declarations/#C2___Magma___op-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example")`, relying on instance synthesis to recover the implementation from the `[C2.Semigroup](Type-Classes/Class-Declarations/#C2___Semigroup-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example")` instance-implicit parameter via its parent projection:
`C2.Monoid.mk.{u} {α : Type u}   [toSemigroup : [C2.Semigroup](Type-Classes/Class-Declarations/#C2___Semigroup-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") α]   (ident : α)   (ident_left : ∀ (x : α), [C2.Magma.op](Type-Classes/Class-Declarations/#C2___Magma___op-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") ident x = x)   (ident_right : ∀ (x : α), [C2.Magma.op](Type-Classes/Class-Declarations/#C2___Magma___op-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") x ident = x) :   [C2.Monoid](Type-Classes/Class-Declarations/#C2___Monoid-_LPAR_in-Class-vs-Structure-Constructors_RPAR_ "Definition of example") α`
[Live ↪](javascript:openLiveLink\("HYQwtgpgzgDiDGEAEBlAUFALgJwK70122QFkQBzMEJACkEbgJALiQBUBPGZXASiQHcAFhGJokSAPYwmSBoCTCGUnl00GHPkLFUEMAEty2cbin1p7Tkh5IIAD0wRgAEyhIylag0HCIoiTAD6IFBQ4vDSgABESNZIbEgAXgA0vrSSkdG8sUgAvElRNCkxsdwqWHgERKTiwOI6DrQMzGZcvDZ2js4o2noGRgqeImI19pjSygMOQ34ANhAAZsPMEdaJKYPAw1HZ1j6rmH7YegLzSIvLUlE7WZFo9rXoaKCQsAjIAMIAjGjwk4HOJJXVtRMDQ4TSsthu7QAdB1dPpDFIPEJ+kgLsxRijxmsprMjickhcNlcxhN9uRDuFIqdUhdNtdHEh3ioHtA4IgGQAmT7fIIuChUOqmEEWXh9bxiFJoxQKJQqL4/LSw7rGeqsIWWFoQ3luXpIsW+AJBEIUqIFKl5M5pOKXFK5fJxIpc+V/Ko1AXA8zq8FtBVdeE6rzbTFHdE7bFzY1UgmXLbErGk8kLSk5DFDaN02ovdlAA"\))
Parameters to type classes may be marked with _gadgets_ , which are special versions of the identity function that cause the elaborator to treat a value differently. Gadgets never change the _meaning_ of a term, but they may cause it to be treated differently in elaboration-time search procedures. The gadgets `[outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam")` and `[semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam")` affect [instance synthesis](Type-Classes/Instance-Synthesis/#instance-synth), so they are documented in that section.
Whether a type is a class or not has no effect on definitional equality. Two instances of the same class with the same parameters are not necessarily identical and may in fact be very different.
Instances are Not Unique
This implementation of binary heap insertion is buggy:
`structure Heap (α : Type u) where   contents : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α deriving [Repr](Interacting-with-Lean/#Repr___mk "Documentation for Repr")  def Heap.bubbleUp [[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α] (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (xs : [Heap](Type-Classes/Class-Declarations/#Heap-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example") α) : [Heap](Type-Classes/Class-Declarations/#Heap-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example") α :=   [if](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") h : i = 0 [then](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") xs   [else](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") [if](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") h : i ≥ xs.[contents](Type-Classes/Class-Declarations/#Heap___contents-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") [then](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") xs   [else](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax")     let j := i / 2     [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") [Ord.compare](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord.compare") xs.[contents](Type-Classes/Class-Declarations/#Heap___contents-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example")[i] xs.[contents](Type-Classes/Class-Declarations/#Heap___contents-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example")[j] == [.lt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.lt") [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax")       [Heap.bubbleUp](Type-Classes/Class-Declarations/#Heap___bubbleUp-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example") j { xs with [contents](Type-Classes/Class-Declarations/#Heap___contents-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example") := xs.[contents](Type-Classes/Class-Declarations/#Heap___contents-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example").[swap](Basic-Types/Arrays/#Array___swap "Documentation for Array.swap") i j }     [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") xs  def Heap.insert [[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α] (x : α) (xs : [Heap](Type-Classes/Class-Declarations/#Heap-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example") α) : [Heap](Type-Classes/Class-Declarations/#Heap-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example") α :=   let i := xs.[contents](Type-Classes/Class-Declarations/#Heap___contents-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")   {xs with [contents](Type-Classes/Class-Declarations/#Heap___contents-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example") := xs.[contents](Type-Classes/Class-Declarations/#Heap___contents-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example").[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") x}.[bubbleUp](Type-Classes/Class-Declarations/#Heap___bubbleUp-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example") i `
The problem is that a heap constructed with one `[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord")` instance may later be used with another, leading to the breaking of the heap invariant.
One way to correct this is to make the heap type depend on the selected `Ord` instance:
`structure Heap' (α : Type u) [[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α] where   contents : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") α  def Heap'.bubbleUp [inst : [Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α]     (i : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (xs : @[Heap'](Type-Classes/Class-Declarations/#Heap___-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example") α inst) :     @[Heap'](Type-Classes/Class-Declarations/#Heap___-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example") α inst :=   [if](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") h : i = 0 [then](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") xs   [else](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") [if](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") h : i ≥ xs.[contents](Type-Classes/Class-Declarations/#Heap______contents-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size") [then](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") xs   [else](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax")     let j := i / 2     [if](Terms/Conditionals/#termIfThenElse "Documentation for syntax") inst.[compare](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord.compare") xs.[contents](Type-Classes/Class-Declarations/#Heap______contents-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example")[i] xs.[contents](Type-Classes/Class-Declarations/#Heap______contents-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example")[j] == [.lt](Type-Classes/Basic-Classes/#Ordering___lt "Documentation for Ordering.lt") [then](Terms/Conditionals/#termIfThenElse "Documentation for syntax")       [Heap'.bubbleUp](Type-Classes/Class-Declarations/#Heap______bubbleUp-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example") j {xs with [contents](Type-Classes/Class-Declarations/#Heap______contents-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example") := xs.[contents](Type-Classes/Class-Declarations/#Heap______contents-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example").[swap](Basic-Types/Arrays/#Array___swap "Documentation for Array.swap") i j}     [else](Terms/Conditionals/#termIfThenElse "Documentation for syntax") xs  def Heap'.insert [[Ord](Type-Classes/Basic-Classes/#Ord___mk "Documentation for Ord") α] (x : α) (xs : [Heap'](Type-Classes/Class-Declarations/#Heap___-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example") α) : [Heap'](Type-Classes/Class-Declarations/#Heap___-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example") α :=   let i := xs.[contents](Type-Classes/Class-Declarations/#Heap______contents-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example").[size](Basic-Types/Arrays/#Array___size "Documentation for Array.size")   {xs with [contents](Type-Classes/Class-Declarations/#Heap______contents-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example") := xs.[contents](Type-Classes/Class-Declarations/#Heap______contents-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example").[push](Basic-Types/Arrays/#Array___push "Documentation for Array.push") x}.[bubbleUp](Type-Classes/Class-Declarations/#Heap______bubbleUp-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example") i `
In the improved definitions, `[Heap'.bubbleUp](Type-Classes/Class-Declarations/#Heap______bubbleUp-_LPAR_in-Instances-are-Not-Unique_RPAR_ "Definition of example")` is needlessly explicit; the instance does not need to be explicitly named here because Lean would select the indicated instances nonetheless, but it does bring the correctness invariant front and center for readers.
[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgBLwIYAdEApCNwIgLkQBUBPDJCASkQHcALeBAKEUSgHsA7EeH4QogCCYMGlKJczACZMAlgDc5XAOaIASvAxhmM+ADMU6DADoARhDNmANvACqWANoB5MNMkBdHHMEA5NCA02AAeAkSomJI04caShAC8rIhyhvSCPvGIAAyIIIxciKFJ8NbASCmIaUQ+gKZEhcAmnDx8IA3AcgBeSHl89cWl8ElstiCIAFYJyYgA9IgATEPJhq7SjRwAthhoCPVrzfyOcl6he7wHY17xmSbWoz1ci2wRphZWtg7jiADe9XRyeexuGdWpMTk1gW1aJEfBMAL6LEplPp6QzPEzKMpgUYuNyeHDBQS4IKhQTPKKk2L4AiJYbwUY+am7cEtNqdQZsL4k2j/NLM/ighp81omDAQYBpYKw8yWGz2LByXSgSAwOBIZ4AchwVJI5EoNBx7lwXgYTHZgP2IKIIjEEikKKMmHV0recsQhy4oEEK08i2wDMQ/kC+LCiAAAhq4higwRFuHjJr8FGEkkKlUppkcvc+mxEeVUulEHUwUCWSZ2l1cvls4hc4sRp9GT5Zgs2GwKlG1pttkhixbgIdjoKS+dLtdbpW+I8HRgna9ZR8JpyBNyAUKwplexCy1D5eN4a2awNkbJUfH0R6mNjvUb8YTiSGI0SKY64tSkvWGRuh32y2ykku/lXYdLS/U5S1FcVCilOd3nlIA"\))
##  10.1.1. Sum Types as Classes[🔗](find/?domain=Verso.Genre.Manual.section&name=class-inductive "Permalink")
Most type classes follow the paradigm of a set of overloaded methods from which clients may choose freely. This is naturally modeled by a product type, from which the overloaded methods are projections. Some classes, however, are sum types: they require that the recipient of the synthesized instance first check _which_ of the available instance constructors was provided. To account for these classes, a class declaration may consist of an arbitrary [inductive type](The-Type-System/Inductive-Types/#--tech-term-Inductive-types), not just an extended form of structure declaration.
syntaxClass Inductive Type Declarations

```
command ::= ...
    | [
declModifiers is the collection of modifiers on a declaration:



  * a doc comment /-- ... -/



  * a list of attributes @[attr1, attr2]



  * a visibility specifier, private or public



  * protected


  * noncomputable


  * unsafe


  * 
partial or nonrec




All modifiers are optional, and have to come in the listed order.
nestedDeclModifiers is the same as declModifiers, but attributes are printed
on the same line as the declaration. It is used for declarations nested inside other syntax,
such as inductive constructors, structure projections, and let rec / where definitions. 
declModifiers](Definitions/Modifiers/#Lean___Parser___Command___declModifiers)
      class inductive 


declId matches foo or foo.{u,v}: an identifier possibly followed by a list of universe names 


declId [
optDeclSig matches the signature of a declaration with optional type: a list of binders and then possibly : type 
optDeclSig](Definitions/Headers-and-Signatures/#Lean___Parser___Command___optDeclSig) where
        (| [
declModifiers is the collection of modifiers on a declaration:



  * a doc comment /-- ... -/



  * a list of attributes @[attr1, attr2]



  * a visibility specifier, private or public



  * protected


  * noncomputable


  * unsafe


  * 
partial or nonrec




All modifiers are optional, and have to come in the listed order.
nestedDeclModifiers is the same as declModifiers, but attributes are printed
on the same line as the declaration. It is used for declarations nested inside other syntax,
such as inductive constructors, structure projections, and let rec / where definitions. 
declModifiers](Definitions/Modifiers/#Lean___Parser___Command___declModifiers) ident [
optDeclSig matches the signature of a declaration with optional type: a list of binders and then possibly : type 
optDeclSig](Definitions/Headers-and-Signatures/#Lean___Parser___Command___optDeclSig))*
      ([deriving](Type-Classes/Deriving-Instances/#Lean___Parser___Command___optDeriving-next) ident,*)?
```

Class inductive types are just like other inductive types, except they may participate in instance synthesis. The paradigmatic example of a class inductive is `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")`: synthesizing an instance in a context with free variables amounts to synthesizing the decision procedure, but if there are no free variables, then the truth of the proposition can be established by instance synthesis alone (as is done by the `[decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")` tactic).
##  10.1.2. Class Abbreviations[🔗](find/?domain=Verso.Genre.Manual.section&name=class-abbrev "Permalink")
In some cases, many related type classes may co-occur throughout a codebase. Rather than writing all the names repeatedly, it would be possible to define a class that extends all the classes in question, contributing no new methods itself. However, this new class has a disadvantage: its instances must be declared explicitly.
The ``Lean.Parser.Command.classAbbrev : command`
Expands

```
class abbrev C <params> := D_1, ..., D_n

```

into

```
class C <params> extends D_1, ..., D_n
attribute [instance] C.mk

```

``class abbrev` command allows the creation of _class abbreviations_ in which one name is short for a number of other class parameters. Behind the scenes, a class abbreviation is represented by a class that extends all the others. Its constructor is additionally declared to be an instance so the new class can be constructed by instance synthesis alone.
Class Abbreviations
Both `[plusTimes1](Type-Classes/Class-Declarations/#plusTimes1-_LPAR_in-Class-Abbreviations_RPAR_ "Definition of example")` and `[plusTimes2](Type-Classes/Class-Declarations/#plusTimes2-_LPAR_in-Class-Abbreviations_RPAR_ "Definition of example")` require that their parameters' type have `[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add")` and `[Mul](Type-Classes/Basic-Classes/#Mul___mk "Documentation for Mul")` instances:
`class abbrev AddMul (α : Type u) := [Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") α, [Mul](Type-Classes/Basic-Classes/#Mul___mk "Documentation for Mul") α  def plusTimes1 [[AddMul](Type-Classes/Class-Declarations/#AddMul-_LPAR_in-Class-Abbreviations_RPAR_ "Definition of example") α] (x y z : α) := x + y * z  class AddMul' (α : Type u) extends [Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") α, [Mul](Type-Classes/Basic-Classes/#Mul___mk "Documentation for Mul") α  def plusTimes2 [[AddMul'](Type-Classes/Class-Declarations/#AddMul___-_LPAR_in-Class-Abbreviations_RPAR_ "Definition of example") α] (x y z : α) := x + y * z `
Because `[AddMul](Type-Classes/Class-Declarations/#AddMul-_LPAR_in-Class-Abbreviations_RPAR_ "Definition of example")` is a ``Lean.Parser.Command.classAbbrev : command`
``class abbrev`, no additional declarations are necessary to use `[plusTimes1](Type-Classes/Class-Declarations/#plusTimes1-_LPAR_in-Class-Abbreviations_RPAR_ "Definition of example")` with `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`:
``37`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [plusTimes1](Type-Classes/Class-Declarations/#plusTimes1-_LPAR_in-Class-Abbreviations_RPAR_ "Definition of example") 2 5 7 `
```
37
```

However, `[plusTimes2](Type-Classes/Class-Declarations/#plusTimes2-_LPAR_in-Class-Abbreviations_RPAR_ "Definition of example")` fails, because there is no `[AddMul'](Type-Classes/Class-Declarations/#AddMul___-_LPAR_in-Class-Abbreviations_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` instance—no instances whatsoever have yet been declared:
`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") `failed to synthesize instance of type class   [AddMul'](Type-Classes/Class-Declarations/#AddMul___-_LPAR_in-Class-Abbreviations_RPAR_ "Definition of example") ?m.8  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`[plusTimes2](Type-Classes/Class-Declarations/#plusTimes2-_LPAR_in-Class-Abbreviations_RPAR_ "Definition of example") 2 5 7 `
```
failed to synthesize instance of type class
  [AddMul'](Type-Classes/Class-Declarations/#AddMul___-_LPAR_in-Class-Abbreviations_RPAR_ "Definition of example") ?m.8

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```

Declaring a very general instance takes care of the problem for `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` and every other type:
`instance [[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") α] [[Mul](Type-Classes/Basic-Classes/#Mul___mk "Documentation for Mul") α] : [AddMul'](Type-Classes/Class-Declarations/#AddMul___-_LPAR_in-Class-Abbreviations_RPAR_ "Definition of example") α where  `37`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [plusTimes2](Type-Classes/Class-Declarations/#plusTimes2-_LPAR_in-Class-Abbreviations_RPAR_ "Definition of example") 2 5 7 `
```
37
```

[Live ↪](javascript:openLiveLink\("MYGwhgzhAEYEZwE4FMBu0CCATLBZAriNABSCNwNAFzQAqAngA7LT4CUlAvJjtKQDTQEipAFDCsyAGbR6IfBGoBLALbIIARmgBtbHkI8AuiQAe0WtABelHmwqcTAalPQAVBdGhIMHYIDkJclR0jMxsyEYALsgAdlhe3HwCeiJiktKy8sqqAExa3oR+pIbEJmaWVKQ2dtCOZq7mogDEaGBEMnKKKurQOQCs0ADsogpREOFgUcBM2vGGmoIGVnkgBdAA7gAWyCiNza3pHdnd0H39QA"\))
[←10. Type Classes](Type-Classes/#type-classes "10. Type Classes")[10.2. Instance Declarations→](Type-Classes/Instance-Declarations/#instance-declarations "10.2. Instance Declarations")

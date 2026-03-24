[←10.1. Class Declarations](Type-Classes/Class-Declarations/#class "10.1. Class Declarations")[10.3. Instance Synthesis→](Type-Classes/Instance-Synthesis/#instance-synth "10.3. Instance Synthesis")
#  10.2. Instance Declarations[🔗](find/?domain=Verso.Genre.Manual.section&name=instance-declarations "Permalink")
The syntax of instance declarations is almost identical to that of definitions. The only syntactic differences are that the keyword ``Lean.Parser.Command.declaration : command```def` is replaced by ``Lean.Parser.Command.declaration : command```instance` and the name is optional:
syntaxInstance Declarations
Most instances define each method using ``Lean.Parser.Command.declaration : command```where` syntax:

```
instance ::= ...
    | 


attrKind matches ("scoped" <|> "local")?, used before an attribute like @[local simp]. 


instance ((priority := prio))? 


declId matches foo or foo.{u,v}: an identifier possibly followed by a list of universe names 


declId? [
declSig matches the signature of a declaration with required type: a list of binders and then : type 
declSig](Definitions/Headers-and-Signatures/#Lean___Parser___Command___declSig) where
        structInstField*
```

However, type classes are inductive types, so instances can be constructed using any expression with an appropriate type:

```
instance ::= ...
    | 


attrKind matches ("scoped" <|> "local")?, used before an attribute like @[local simp]. 


instance ((priority := prio))? 


declId matches foo or foo.{u,v}: an identifier possibly followed by a list of universe names 


declId? [
declSig matches the signature of a declaration with required type: a list of binders and then : type 
declSig](Definitions/Headers-and-Signatures/#Lean___Parser___Command___declSig) :=
        term


Termination hints are termination_by and decreasing_by, in that order.



```

Instances may also be defined by cases; however, this feature is rarely used outside of `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable")` instances:

```
instance ::= ...
    | 


attrKind matches ("scoped" <|> "local")?, used before an attribute like @[local simp]. 


instance ((priority := prio))? 


declId matches foo or foo.{u,v}: an identifier possibly followed by a list of universe names 


declId? [
declSig matches the signature of a declaration with required type: a list of binders and then : type 
declSig](Definitions/Headers-and-Signatures/#Lean___Parser___Command___declSig)
        (| term => term)*


Termination hints are termination_by and decreasing_by, in that order.



```

Instances defined with explicit terms often consist of either anonymous constructors (``Lean.Parser.Term.anonymousCtor : term`
The _anonymous constructor_ `⟨e, ...⟩` is equivalent to `c e ...` if the expected type is an inductive type with a single constructor `c`. If more terms are given than `c` has parameters, the remaining arguments are turned into a new anonymous constructor application. For example, `⟨a, b, c⟩ : α × (β × γ)` is equivalent to `⟨a, ⟨b, c⟩⟩`.
`[`⟨...⟩`](The-Type-System/Inductive-Types/#Lean___Parser___Term___anonymousCtor)) wrapping method implementations or of invocations of `[inferInstanceAs](Type-Classes/Instance-Synthesis/#inferInstanceAs "Documentation for inferInstanceAs")` on definitionally equal types.
Elaboration of instances is almost identical to the elaboration of ordinary definitions, with the exception of the caveats documented below. If no name is provided, then one is created automatically. It is possible to refer to this generated name directly, but the algorithm used to generate the names has changed in the past and may change in the future. It's better to explicitly name instances that will be referred to directly. After elaboration, the new instance is registered as a candidate for instance search. Adding the attribute `instance` to a name can be used to mark any other defined name as a candidate.
Instance Name Generation
Following these declarations:
`structure NatWrapper where   val : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")  instance : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") [NatWrapper](Type-Classes/Instance-Declarations/#NatWrapper-_LPAR_in-Instance-Name-Generation_RPAR_ "Definition of example") where   [beq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")     | ⟨x⟩, ⟨y⟩ => x == y `
the name `instBEqNatWrapper` refers to the new instance.
[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgHIEMQHUyoA4/mIgO4AWB8AUIogG6oA2iAXCuhRQJYB2oqXUSFgCEAogEdWmbHgLEyCKogBG8MYuoAfRIAvyAB6BL8gA0OgJ77EAXgB8iXZYuITQA"\))
Variations in Instance Definitions
Given this structure type:
`structure NatWrapper where   val : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") `
all of the following ways of defining a `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` instance are equivalent:
`instance : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") [NatWrapper](Type-Classes/Instance-Declarations/#NatWrapper-_LPAR_in-Variations-in-Instance-Definitions_RPAR_ "Definition of example") where   [beq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")     | ⟨x⟩, ⟨y⟩ => x == y  instance : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") [NatWrapper](Type-Classes/Instance-Declarations/#NatWrapper-_LPAR_in-Variations-in-Instance-Definitions_RPAR_ "Definition of example") :=   ⟨fun x y => x.[val](Type-Classes/Instance-Declarations/#NatWrapper___val-_LPAR_in-Variations-in-Instance-Definitions_RPAR_ "Definition of example") == y.[val](Type-Classes/Instance-Declarations/#NatWrapper___val-_LPAR_in-Variations-in-Instance-Definitions_RPAR_ "Definition of example")⟩  instance : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") [NatWrapper](Type-Classes/Instance-Declarations/#NatWrapper-_LPAR_in-Variations-in-Instance-Definitions_RPAR_ "Definition of example") :=   ⟨fun ⟨x⟩ ⟨y⟩ => x == y⟩ `
Aside from introducing different names into the environment, the following are also equivalent:
``Definition `instBeqNatWrapper` of class type must be marked with `@[reducible]` or `@[implicit_reducible]``@[`instance `instBeqNatWrapper` must be marked with `@[reducible]` or `@[implicit_reducible]``[instance](Type-Classes/Instance-Declarations/#Lean___Parser___Attr___instance "Documentation for syntax")] def instBeqNatWrapper : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") [NatWrapper](Type-Classes/Instance-Declarations/#NatWrapper-_LPAR_in-Variations-in-Instance-Definitions_RPAR_ "Definition of example") where [beq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") | ⟨x⟩, ⟨y⟩ => x == y instance : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") [NatWrapper](Type-Classes/Instance-Declarations/#NatWrapper-_LPAR_in-Variations-in-Instance-Definitions_RPAR_ "Definition of example") := ⟨fun x y => x.[val](Type-Classes/Instance-Declarations/#NatWrapper___val-_LPAR_in-Variations-in-Instance-Definitions_RPAR_ "Definition of example") == y.[val](Type-Classes/Instance-Declarations/#NatWrapper___val-_LPAR_in-Variations-in-Instance-Definitions_RPAR_ "Definition of example")⟩ instance : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") [NatWrapper](Type-Classes/Instance-Declarations/#NatWrapper-_LPAR_in-Variations-in-Instance-Definitions_RPAR_ "Definition of example") := ⟨fun ⟨x⟩ ⟨y⟩ => x == y⟩ `
[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgHIEMQHUyoA4/mIgO4AWB8AUIogG6oA2iAXCuhRQJYB2oqXUSFgCEAogEdWmbHgLEyCKogBG8MYuoAfRIAvyAB6BL8gA0OgJ77EAXgB8iXZYuIT7br36DEoiWim58hJhaK2gBmEFy2jpY2ugB0dIwWDiZxDPrOPCB8Aswe4pJYvrIBQaHheubaZlERiY5pFAACANoumW4AuhQAJvDBiK1Cqt4FMv65XugjfnLkiipq1Jo6BsaV5tY1Semu2cJ5w9LTxdQhYREm1bHx9o4p9PWtWe6e+YdFgSelyxVVG3a1ZiAA"\))
##  10.2.1. Recursive Instances[🔗](find/?domain=Verso.Genre.Manual.section&name=recursive-instances "Permalink")
Functions defined in ``Lean.Parser.Command.declaration : command```where` structure definition syntax are not recursive. Because instance declaration is a version of structure definition, type class methods are also not recursive by default. Instances for recursive inductive types are common, however. There is a standard idiom to work around this limitation: define a recursive function independently of the instance, and then refer to it in the instance definition. By convention, these recursive functions have the name of the corresponding method, but are defined in the type's namespace.
Instances are not recursive
Given this definition of `[NatTree](Type-Classes/Instance-Declarations/#NatTree-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example")`:
`inductive NatTree where   | leaf   | branch (left : [NatTree](Type-Classes/Instance-Declarations/#NatTree-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example")) (val : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (right : [NatTree](Type-Classes/Instance-Declarations/#NatTree-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example")) `
the following `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq")` instance fails:
`instance : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") [NatTree](Type-Classes/Instance-Declarations/#NatTree-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example") where   [beq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq")     | [.leaf](Type-Classes/Instance-Declarations/#NatTree___leaf-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example"), [.leaf](Type-Classes/Instance-Declarations/#NatTree___leaf-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example") =>       [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")     | [.branch](Type-Classes/Instance-Declarations/#NatTree___branch-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example") l1 v1 r1, [.branch](Type-Classes/Instance-Declarations/#NatTree___branch-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example") l2 v2 r2 =>       `failed to synthesize instance of type class   [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") [NatTree](Type-Classes/Instance-Declarations/#NatTree-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example")  Hint: Adding the command `deriving instance BEq for NatTree` may allow Lean to derive the missing instance.`l1 == l2 && v1 == v2 && `failed to synthesize instance of type class   [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") [NatTree](Type-Classes/Instance-Declarations/#NatTree-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example")  Hint: Adding the command `deriving instance BEq for NatTree` may allow Lean to derive the missing instance.`r1 == r2 | _, _ => [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") `
with errors in both the left and right recursive calls that read:

```
failed to synthesize instance of type class
  [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") [NatTree](Type-Classes/Instance-Declarations/#NatTree-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example")

Hint: Adding the command `deriving instance BEq for NatTree` may allow Lean to derive the missing instance.
```

Given a suitable recursive function, such as `[NatTree.beq](Type-Classes/Instance-Declarations/#NatTree___beq-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example")`:
`def NatTree.beq : [NatTree](Type-Classes/Instance-Declarations/#NatTree-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example") → [NatTree](Type-Classes/Instance-Declarations/#NatTree-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example") → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")   | [.leaf](Type-Classes/Instance-Declarations/#NatTree___leaf-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example"), [.leaf](Type-Classes/Instance-Declarations/#NatTree___leaf-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example") =>     [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")   | [.branch](Type-Classes/Instance-Declarations/#NatTree___branch-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example") l1 v1 r1, [.branch](Type-Classes/Instance-Declarations/#NatTree___branch-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example") l2 v2 r2 =>     [NatTree.beq](Type-Classes/Instance-Declarations/#NatTree___beq-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example") l1 l2 && v1 == v2 && [NatTree.beq](Type-Classes/Instance-Declarations/#NatTree___beq-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example") r1 r2   | _, _ =>     [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false") `
the instance can be created in a second step:
`instance : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") [NatTree](Type-Classes/Instance-Declarations/#NatTree-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example") where   [beq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq.beq") := [NatTree.beq](Type-Classes/Instance-Declarations/#NatTree___beq-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example") `
or, equivalently, using anonymous constructor syntax:
`instance : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") [NatTree](Type-Classes/Instance-Declarations/#NatTree-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example") := ⟨[NatTree.beq](Type-Classes/Instance-Declarations/#NatTree___beq-_LPAR_in-Instances-are-not-recursive_RPAR_ "Definition of example")⟩ `
[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABAOQIYwCoCdEoHcALRPAKGWQB9kAbRdAMwuuQCMd0QojkAKeoxjIAXGky58ASn7x0tUeJgy+OYAHMiwsRmx5EUsmTCJGSyYgB0bRAEdFui8kBJhOf0vkAIQD232ixpLeiYAGmQghjMAXgA+FkoYHAhEAPCOLh46AEZkeBycLLDrTm5eWgAmXMqcStj4t3xrO2y6SoAyNtycqKiq5A6Gqxt7AuQa1IB9MInkOspKRnkAZxSyUCWYDJQxTwBRe0d3YlIUymHRXsPG4aN1ze5tr33Bi+RAC/IrobtAS/IgA"\))
Furthermore, instances are not available for instance synthesis during their own definitions. They are first marked as being available for instance synthesis after they are defined. Nested inductive types, in which the recursive occurrence of the type occurs as a parameter to some other inductive type, may require an instance to be available to write even the recursive function. The standard idiom to work around this limitation is to create a local instance in a recursively-defined function that includes a reference to the function being defined, taking advantage of the fact that instance synthesis may use every binding in the local context with the right type.
Instances for nested types
In this definition of `[NatRoseTree](Type-Classes/Instance-Declarations/#NatRoseTree-_LPAR_in-Instances-for-nested-types_RPAR_ "Definition of example")`, the type being defined occurs nested under another inductive type constructor (`[Array](Basic-Types/Arrays/#Array___mk "Documentation for Array")`):
`inductive NatRoseTree where   | node (val : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) (children : [Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [NatRoseTree](Type-Classes/Instance-Declarations/#NatRoseTree-_LPAR_in-Instances-for-nested-types_RPAR_ "Definition of example"))  `
Checking the equality of rose trees requires checking equality of arrays. However, instances are not typically available for instance synthesis during their own definitions, so the following definition fails, even though `NatRoseTree.beq` is a recursive function and is in scope in its own definition.
`def NatRoseTree.beq : (tree1 tree2 : [NatRoseTree](Type-Classes/Instance-Declarations/#NatRoseTree-_LPAR_in-Instances-for-nested-types_RPAR_ "Definition of example")) → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")   | [.node](Type-Classes/Instance-Declarations/#NatRoseTree___node-_LPAR_in-Instances-for-nested-types_RPAR_ "Definition of example") val1 children1, [.node](Type-Classes/Instance-Declarations/#NatRoseTree___node-_LPAR_in-Instances-for-nested-types_RPAR_ "Definition of example") val2 children2 =>     val1 == val2 &&     `failed to synthesize instance of type class   [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [NatRoseTree](Type-Classes/Instance-Declarations/#NatRoseTree-_LPAR_in-Instances-for-nested-types_RPAR_ "Definition of example"))  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`children1 == children2 `
```
failed to synthesize instance of type class
  [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") ([Array](Basic-Types/Arrays/#Array___mk "Documentation for Array") [NatRoseTree](Type-Classes/Instance-Declarations/#NatRoseTree-_LPAR_in-Instances-for-nested-types_RPAR_ "Definition of example"))

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```

To solve this, a local `[BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") [NatRoseTree](Type-Classes/Instance-Declarations/#NatRoseTree-_LPAR_in-Instances-for-nested-types_RPAR_ "Definition of example")` instance may be `let`-bound:
`partial def NatRoseTree.beq : (tree1 tree2 : [NatRoseTree](Type-Classes/Instance-Declarations/#NatRoseTree-_LPAR_in-Instances-for-nested-types_RPAR_ "Definition of example")) → [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")   | [.node](Type-Classes/Instance-Declarations/#NatRoseTree___node-_LPAR_in-Instances-for-nested-types_RPAR_ "Definition of example") val1 children1, [.node](Type-Classes/Instance-Declarations/#NatRoseTree___node-_LPAR_in-Instances-for-nested-types_RPAR_ "Definition of example") val2 children2 =>     let _ : [BEq](Type-Classes/Basic-Classes/#BEq___mk "Documentation for BEq") [NatRoseTree](Type-Classes/Instance-Declarations/#NatRoseTree-_LPAR_in-Instances-for-nested-types_RPAR_ "Definition of example") := ⟨NatRoseTree.beq⟩     val1 == val2 &&     children1 == children2 `
The use of array equality on the children finds the let-bound instance during instance synthesis.
[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABAOQIYwEoHsDOiAKgE6IoDuAFoqQFDLIA+yIOYKAFPOgDbIBcaTAEpkHKJWA8wpEAOQBBYsXQBPIdnxFSiYbVoAHdMTi9k7AGYbcBEmQB0AI0QBHeRxg6AjMk9kATPIYmrY6ooBJhMgAQjg4PPRMyPas7MjcPD4SUjKIIF4ANEkpKOmBWdKygQC8AHwJDDyIMMgA+vJRAKJuwTbaZAJVyIAX5D1adohOroCX5PVpvD5Vg6XIAGQrs+U5eciLyJuVQA"\))
##  10.2.2. Instances of `class inductive`s[🔗](find/?domain=Verso.Genre.Manual.section&name=class-inductive-instances "Permalink")
Many instances have function types: any instance that itself recursively invokes instance search is a function, as is any instance with implicit parameters. While most instances only project method implementations from their own instance parameters, instances of class inductive types typically pattern-match one or more of their arguments, allowing the instance to select the appropriate constructor. This is done using ordinary Lean function syntax. Just as with other instances, the function in question is not available for instance synthesis in its own definition.
An instance for a sum class
Because `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") α` is an abbreviation for `(a b : α) → [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") ([Eq](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") a b)`, its arguments can be used directly, as in this example:
`inductive ThreeChoices where   | yes | no | maybe  instance : [DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") [ThreeChoices](Type-Classes/Instance-Declarations/#ThreeChoices-_LPAR_in-An-instance-for-a-sum-class_RPAR_ "Definition of example")   | [.yes](Type-Classes/Instance-Declarations/#ThreeChoices___yes-_LPAR_in-An-instance-for-a-sum-class_RPAR_ "Definition of example"),   [.yes](Type-Classes/Instance-Declarations/#ThreeChoices___yes-_LPAR_in-An-instance-for-a-sum-class_RPAR_ "Definition of example")   =>     [.isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")   | [.no](Type-Classes/Instance-Declarations/#ThreeChoices___no-_LPAR_in-An-instance-for-a-sum-class_RPAR_ "Definition of example"),    [.no](Type-Classes/Instance-Declarations/#ThreeChoices___no-_LPAR_in-An-instance-for-a-sum-class_RPAR_ "Definition of example")    =>     [.isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")   | [.maybe](Type-Classes/Instance-Declarations/#ThreeChoices___maybe-_LPAR_in-An-instance-for-a-sum-class_RPAR_ "Definition of example"), [.maybe](Type-Classes/Instance-Declarations/#ThreeChoices___maybe-_LPAR_in-An-instance-for-a-sum-class_RPAR_ "Definition of example") =>     [.isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")   | [.yes](Type-Classes/Instance-Declarations/#ThreeChoices___yes-_LPAR_in-An-instance-for-a-sum-class_RPAR_ "Definition of example"),   [.maybe](Type-Classes/Instance-Declarations/#ThreeChoices___maybe-_LPAR_in-An-instance-for-a-sum-class_RPAR_ "Definition of example") | [.yes](Type-Classes/Instance-Declarations/#ThreeChoices___yes-_LPAR_in-An-instance-for-a-sum-class_RPAR_ "Definition of example"),   [.no](Type-Classes/Instance-Declarations/#ThreeChoices___no-_LPAR_in-An-instance-for-a-sum-class_RPAR_ "Definition of example")   | [.maybe](Type-Classes/Instance-Declarations/#ThreeChoices___maybe-_LPAR_in-An-instance-for-a-sum-class_RPAR_ "Definition of example"), [.yes](Type-Classes/Instance-Declarations/#ThreeChoices___yes-_LPAR_in-An-instance-for-a-sum-class_RPAR_ "Definition of example")   | [.maybe](Type-Classes/Instance-Declarations/#ThreeChoices___maybe-_LPAR_in-An-instance-for-a-sum-class_RPAR_ "Definition of example"), [.no](Type-Classes/Instance-Declarations/#ThreeChoices___no-_LPAR_in-An-instance-for-a-sum-class_RPAR_ "Definition of example")   | [.no](Type-Classes/Instance-Declarations/#ThreeChoices___no-_LPAR_in-An-instance-for-a-sum-class_RPAR_ "Definition of example"),    [.yes](Type-Classes/Instance-Declarations/#ThreeChoices___yes-_LPAR_in-An-instance-for-a-sum-class_RPAR_ "Definition of example")   | [.no](Type-Classes/Instance-Declarations/#ThreeChoices___no-_LPAR_in-An-instance-for-a-sum-class_RPAR_ "Definition of example"),    [.maybe](Type-Classes/Instance-Declarations/#ThreeChoices___maybe-_LPAR_in-An-instance-for-a-sum-class_RPAR_ "Definition of example") =>     [.isFalse](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isFalse") [nofun](Terms/Pattern-Matching/#Lean___Parser___Term___nofun "Documentation for syntax")  `
[Live ↪](javascript:openLiveLink\("IYDwlg9gtgBIjcAwFwwCoE8AOBTAUDsAdgCYCuAxgC5gBuWqAFgE5ZYDC9EYZWAzjAO70szHDBgAfGGl4SYBCLKjA0AI1z4CPCsALckMACJYyYIsBUAbLAFEAjg2ZsOXXqNkA6aTwA0YmJ5kxAF4APjcxdzAeFEYSOkYAMws3SXd5Xz80hT9Q8P8omLiYROSxVKVVLF93CrUYXL986Nj4pJT/Lwz/WrpUzsz5dprlNWqvP3KRqv9BspmILo7Aj3TG4cr6sLWogDFgCx46eQSSAiA"\))
A recursive instance for a sum class
The type `[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")` represents monomorphic lists of strings:
`inductive StringList where   | nil   | cons (hd : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")) (tl : [StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")) `
In the following attempt at defining a `[DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq")` instance, instance synthesis invoked while elaborating the inner ``termIfThenElse : term`
`[`if`](Terms/Conditionals/#termIfThenElse) fails because the instance is not available for instance synthesis in its own definition:
`instance : [DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") [StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")   | [.nil](Type-Classes/Instance-Declarations/#StringList___nil-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example"), [.nil](Type-Classes/Instance-Declarations/#StringList___nil-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") => [.isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")   | [.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h1 t1, [.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h2 t2 =>     [if](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") h : h1 = h2 [then](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax")       `failed to synthesize instance of type class   [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t2[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`[if](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") h' : t1 = t2 [then](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") [.isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") (byh1:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t1:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")h2:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t2:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")h:h1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") h2h':t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t2⊢ [StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h1 t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h2 t2 [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [*]All goals completed! 🐙) [else](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") [.isFalse](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isFalse") (byh1:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t1:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")h2:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t2:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")h:h1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") h2h':[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t2⊢ [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h1 t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h2 t2 [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") hEqh1:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t1:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")h2:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t2:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")h:h1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") h2h':[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t2hEq:[StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h1 t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h2 t2⊢ [False](Basic-Propositions/Truth/#False "Documentation for False"); [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") hEqreflh1:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t1:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")h:h1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") h1h':[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t1⊢ [False](Basic-Propositions/Truth/#False "Documentation for False"); [trivial](Tactic-Proofs/Tactic-Reference/#trivial "Documentation for tactic")All goals completed! 🐙) [else](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") [.isFalse](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isFalse") (byh1:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t1:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")h2:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t2:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")h:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")h1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") h2⊢ [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h1 t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h2 t2 [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") hEqh1:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t1:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")h2:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t2:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")h:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")h1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") h2hEq:[StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h1 t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h2 t2⊢ [False](Basic-Propositions/Truth/#False "Documentation for False"); [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") hEqreflh1:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t1:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")h:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")h1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") h1⊢ [False](Basic-Propositions/Truth/#False "Documentation for False"); [trivial](Tactic-Proofs/Tactic-Reference/#trivial "Documentation for tactic")All goals completed! 🐙) | [.nil](Type-Classes/Instance-Declarations/#StringList___nil-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example"), [.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") _ _ | [.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") _ _, [.nil](Type-Classes/Instance-Declarations/#StringList___nil-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") => [.isFalse](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isFalse") [nofun](Terms/Pattern-Matching/#Lean___Parser___Term___nofun "Documentation for syntax") `
```
failed to synthesize instance of type class
  [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t2[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```

However, because it is an ordinary Lean function, it can recursively refer to its own explicitly-provided name:
`instance instDecidableEqStringList : [DecidableEq](Type-Classes/Basic-Classes/#DecidableEq "Documentation for DecidableEq") [StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")   | [.nil](Type-Classes/Instance-Declarations/#StringList___nil-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example"), [.nil](Type-Classes/Instance-Declarations/#StringList___nil-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") => [.isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl")   | [.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h1 t1, [.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h2 t2 =>     let _ : [Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") (t1 = t2) :=       [instDecidableEqStringList](Type-Classes/Instance-Declarations/#instDecidableEqStringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") t1 t2     [if](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") h : h1 = h2 [then](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax")       [if](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax") h' : t1 = t2 [then](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax")         [.isTrue](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isTrue") (byh1:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t1:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")h2:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t2:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")x✝:[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t2[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") := [instDecidableEqStringList](Type-Classes/Instance-Declarations/#instDecidableEqStringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") t1 t2h:h1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") h2h':t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t2⊢ [StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h1 t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h2 t2 [simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") [*]All goals completed! 🐙)       [else](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax")         [.isFalse](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isFalse") (byh1:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t1:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")h2:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t2:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")x✝:[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t2[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") := [instDecidableEqStringList](Type-Classes/Instance-Declarations/#instDecidableEqStringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") t1 t2h:h1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") h2h':[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t2⊢ [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h1 t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h2 t2 [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") hEqh1:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t1:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")h2:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t2:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")x✝:[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t2[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") := [instDecidableEqStringList](Type-Classes/Instance-Declarations/#instDecidableEqStringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") t1 t2h:h1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") h2h':[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t2hEq:[StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h1 t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h2 t2⊢ [False](Basic-Propositions/Truth/#False "Documentation for False"); [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") hEqreflh1:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t1:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")h:h1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") h1x✝:[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t1[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") := [instDecidableEqStringList](Type-Classes/Instance-Declarations/#instDecidableEqStringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") t1 t1h':[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t1⊢ [False](Basic-Propositions/Truth/#False "Documentation for False"); [trivial](Tactic-Proofs/Tactic-Reference/#trivial "Documentation for tactic")All goals completed! 🐙)     [else](Terms/Conditionals/#termDepIfThenElse "Documentation for syntax")       [.isFalse](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isFalse") (byh1:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t1:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")h2:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t2:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")x✝:[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t2[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") := [instDecidableEqStringList](Type-Classes/Instance-Declarations/#instDecidableEqStringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") t1 t2h:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")h1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") h2⊢ [¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")[StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h1 t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h2 t2 [intro](Tactic-Proofs/Tactic-Reference/#intro "Documentation for tactic") hEqh1:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t1:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")h2:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t2:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")x✝:[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t2[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") := [instDecidableEqStringList](Type-Classes/Instance-Declarations/#instDecidableEqStringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") t1 t2h:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")h1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") h2hEq:[StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h1 t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") [StringList.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") h2 t2⊢ [False](Basic-Propositions/Truth/#False "Documentation for False"); [cases](Tactic-Proofs/Tactic-Reference/#cases "Documentation for tactic") hEqreflh1:[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")t1:[StringList](Type-Classes/Instance-Declarations/#StringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example")h:[¬](Basic-Propositions/Logical-Connectives/#Not "Documentation for Not")h1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") h1x✝:[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") [(](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq")t1 [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") t1[)](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") := [instDecidableEqStringList](Type-Classes/Instance-Declarations/#instDecidableEqStringList-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") t1 t1⊢ [False](Basic-Propositions/Truth/#False "Documentation for False"); [trivial](Tactic-Proofs/Tactic-Reference/#trivial "Documentation for tactic")All goals completed! 🐙)   | [.nil](Type-Classes/Instance-Declarations/#StringList___nil-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example"), [.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") _ _ | [.cons](Type-Classes/Instance-Declarations/#StringList___cons-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") _ _, [.nil](Type-Classes/Instance-Declarations/#StringList___nil-_LPAR_in-A-recursive-instance-for-a-sum-class_RPAR_ "Definition of example") => [.isFalse](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable.isFalse") [nofun](Terms/Pattern-Matching/#Lean___Parser___Term___nofun "Documentation for syntax") `
[Live ↪](javascript:openLiveLink\("JYOwJgrgxgLsBuBTABAZRgJ1AcwDLAGcZkB3AC0Q0QChlkAfZEYAG1oeSgHsQDkAKMmGQAuNJhwBKATBajxWEHkIxJ1aqCIBDEFBSaYAEURRgYLQCMWiAKIBHdIuVF5x0+au27CnPiLtGADpmFgAaZGDWZABeAD4IwgAVDAgUDAAzNjog7l5kMgBGZBgC8MDcvjIAJmKauPY6a2IAfVcTM0trGSLo2ukRaIa6ZAM3Ds97R18VYqKYKqHgdPz5Qpj8mpgKECG6JfyAcnkS9fni7d3hwKSUlH4LAE9kAmAAWwAHZABtACoAXTUw2GiBYBBoQKB1wIADEtKC7o8RiBMFx8vYANycLRgyoY4pYeDAOGA4Hwy5Q2HwgSI0AotF2TFQbGIXEM/EIIksElBEJlCrIVqtHI8PiCsohGLxClwsFMLjpCAgIA"\))
##  10.2.3. Instance Priorities[🔗](find/?domain=Verso.Genre.Manual.section&name=instance-priorities "Permalink")
Instances may be assigned _priorities_. During instance synthesis, higher-priority instances are preferred; see [the section on instance synthesis](Type-Classes/Instance-Synthesis/#instance-synth) for details of instance synthesis.
syntaxInstance Priorities
Priorities may be numeric:

```
prio ::=
    num
```

If no priority is specified, the default priority that corresponds to 1000 is used:

```
prio ::= ...
    | 


The default priority default = 1000, which is used when no priority is set. 


default
```

Three named priorities are available when numeric values are too fine-grained, corresponding to 100, 500, and 10000 respectively. The ``prioMid : prio`
The standardized "medium" priority `mid = 500`. This is lower than `default`, and higher than `low`.
`[`mid`](Type-Classes/Instance-Declarations/#prioMid) priority is lower than ``prioDefault : prio`
The default priority `default = 1000`, which is used when no priority is set. 
`[`default`](Type-Classes/Instance-Declarations/#prioDefault).

```
prio ::= ...
    | 


The standardized "low" priority low = 100, for things that should be lower than default priority. 


low
```

```
prio ::= ...
    | 


The standardized "medium" priority mid = 500. This is lower than default, and higher than low.


mid
```

```
prio ::= ...
    | 


The standardized "high" priority high = 10000, for things that should be higher than default priority. 


high
```

Finally, priorities can be added and subtracted, so `default + 2` is a valid priority, corresponding to 1002:

```
prio ::= ...
    | 


Parentheses are used for grouping priority expressions. 


(prio)
```

```
prio ::= ...
    | 


Addition of priorities. This is normally used only for offsetting, e.g. default + 1. 


prio + prio
```

```
prio ::= ...
    | 


Subtraction of priorities. This is normally used only for offsetting, e.g. default - 1. 


prio - prio
```

##  10.2.4. Default Instances[🔗](find/?domain=Verso.Genre.Manual.section&name=default-instances "Permalink")
The `default_instance` attribute specifies that an instance [should be used as a fallback in situations where there is not enough information to select it otherwise](Type-Classes/Instance-Synthesis/#default-instance-synth). If no priority is specified, then the default priority `default` is used.
attributeThe `default_instance` Attribute

```
attr ::= ...
    | default_instance prio?
```

Default Instances
A default instance of `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` is used to select `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` for natural number literals in the absence of other type information. It is declared in the Lean standard library with priority 100. Given this representation of even numbers, in which an even number is represented by half of it:
`structure Even where   half : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") `
the following instances allow numeric literals to be used for small `[Even](Introduction/#Even___zero-next "Documentation for Even")` values (a limit on the depth of type class instance search prevents them from being used for arbitrarily large literals):
`instance ofNatEven0 : [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") [Even](Introduction/#Even___zero-next "Documentation for Even") 0 where   [ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") := ⟨0⟩  instance ofNatEvenPlusTwo [[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") [Even](Introduction/#Even___zero-next "Documentation for Even") n] : [OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") [Even](Introduction/#Even___zero-next "Documentation for Even") (n + 2) where   [ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") := ⟨([OfNat.ofNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat.ofNat") n : [Even](Introduction/#Even___zero-next "Documentation for Even")).[half](Type-Classes/Instance-Declarations/#Even___half-_LPAR_in-Default-Instances_RPAR_ "Definition of example") + 1⟩  `{ half := 0 }`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (0 : [Even](Introduction/#Even___zero-next "Documentation for Even")) `{ half := 17 }`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (34 : [Even](Introduction/#Even___zero-next "Documentation for Even")) `{ half := 127 }`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") (254 : [Even](Introduction/#Even___zero-next "Documentation for Even")) `
```
{ half := 0 }
```

```
{ half := 17 }
```

```
{ half := 127 }
```

Specifying them as default instances with a priority greater than or equal to 100 causes them to be used instead of `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`:
`[attribute](Attributes/#Lean___Parser___Command___attribute "Documentation for syntax") [[default_instance](Type-Classes/Instance-Declarations/#Lean___Parser___Attr___default_instance "Documentation for syntax") 100] [ofNatEven0](Type-Classes/Instance-Declarations/#ofNatEven0-_LPAR_in-Default-Instances_RPAR_ "Definition of example") [attribute](Attributes/#Lean___Parser___Command___attribute "Documentation for syntax") [[default_instance](Type-Classes/Instance-Declarations/#Lean___Parser___Attr___default_instance "Documentation for syntax") 100] [ofNatEvenPlusTwo](Type-Classes/Instance-Declarations/#ofNatEvenPlusTwo-_LPAR_in-Default-Instances_RPAR_ "Definition of example") ```{ half := 0 }`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") 0 `{ half := 17 }`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") 34 `
```
{ half := 0 }
```

```
{ half := 17 }
```

Non-even numerals still use the `[OfNat](Terms/Numeric-Literals/#OfNat___mk "Documentation for OfNat") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` instance:
``5`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") 5 `
```
5
```

[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgKIDd4DtEHcAW8EAoRRXAQwBsAzRALkQDkyRDCBLDUMjKJAeypMQaTAAY6iAPKDmKdFnF4C8YogFC6AXkSAL8lGBL8lYcuPfjOHyAChQjAAKtj6IA2tI0isGALoS3sj4gAFFgA1IgATACUOPhEJOqytNo6gX4gAHQJIIhY9B6R6eTUiGEAjIaEAMTwqJRB4nnykVU1dYEAzAAsEvkttRRB4QCs3Y2YzYTM4GwARhAgSM4AJvBUZBAUIAD6xiDcvIiloqI+WR6ikyDTcwsuK2sb27v7SEcnauYe1rYOfKzV/UQFwBdS6/1aAyGQA"\))
##  10.2.5. The Instance Attribute[🔗](find/?domain=Verso.Genre.Manual.section&name=instance-attribute "Permalink")
The `instance` attribute declares a name to be an instance, with the specified priority. Like other attributes, `instance` can be applied globally, locally, or only when the current namespace is opened. The ``Lean.Parser.Command.declaration : command```instance` declaration is a form of definition that automatically applies the `instance` attribute.
attributeThe `instance` Attribute
Declares the definition to which it is applied to be an instance. If no priority is provided, then the default priority `default` is used.

```
attr ::= ...
    | instance prio?
```

[←10.1. Class Declarations](Type-Classes/Class-Declarations/#class "10.1. Class Declarations")[10.3. Instance Synthesis→](Type-Classes/Instance-Synthesis/#instance-synth "10.3. Instance Synthesis")

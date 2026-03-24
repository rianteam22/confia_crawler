[←10.2. Instance Declarations](Type-Classes/Instance-Declarations/#instance-declarations "10.2. Instance Declarations")[10.4. Deriving Instances→](Type-Classes/Deriving-Instances/#deriving-instances "10.4. Deriving Instances")
#  10.3. Instance Synthesis[🔗](find/?domain=Verso.Genre.Manual.section&name=instance-synth "Permalink")
Instance synthesis is a recursive search procedure that either finds an instance for a given type class or fails. In other words, given a type that is registered as a type class, instance synthesis attempts to construct a term with said type. It respects [reducibility](Definitions/Recursive-Definitions/#--tech-term-reducibility): [semireducible](Definitions/Recursive-Definitions/#--tech-term-Semireducible) or [irreducible](Definitions/Recursive-Definitions/#--tech-term-Irreducible) definitions are not unfolded, so instances for a definition are not automatically treated as instances for its unfolding unless it is [reducible](Definitions/Recursive-Definitions/#--tech-term-Reducible). There may be multiple possible instances for a given class; in this case, declared priorities and order of declaration are used as tiebreakers, in that order, with more recent instances taking precedence over earlier ones with the same priority.
This search procedure is efficient in the presence of diamonds and does not loop indefinitely when there are cycles. _Diamonds_ occur when there is more than one route to a given goal, and _cycles_ are situations when two instances each could be solved if the other were solved. Diamonds occur regularly in practice when encoding mathematical concepts using type classes, and Lean's coercion feature naturally leads to cycles, e.g. between finite sets and finite multisets.
Instance synthesis can be tested using the ``Lean.Parser.Command.synth : command``[`#synth`](Interacting-with-Lean/#Lean___Parser___Command___synth) command. Additionally, `[inferInstance](Type-Classes/Instance-Synthesis/#inferInstance "Documentation for inferInstance")` and `[inferInstanceAs](Type-Classes/Instance-Synthesis/#inferInstanceAs "Documentation for inferInstanceAs")` can be used to synthesize an instance in a position where the instance itself is needed.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=inferInstance "Permalink")def
```


inferInstance.{u} {α : Sort u} [i : α] : α


inferInstance.{u} {α : Sort u} [i : α] : α


```

`[inferInstance](Type-Classes/Instance-Synthesis/#inferInstance "Documentation for inferInstance")` synthesizes a value of any target type by typeclass inference. This function has the same type signature as the identity function, but the square brackets on the `[i : α]` argument means that it will attempt to construct this argument by typeclass inference. (This will fail if `α` is not a `class`.) Example:
``inferInstance : Inhabited [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") ([inferInstance](Type-Classes/Instance-Synthesis/#inferInstance "Documentation for inferInstance") : [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) -- Inhabited Nat `Definition `foo` of class type must be marked with `@[reducible]` or `@[implicit_reducible]``def foo : [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") ([Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") × [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) := [inferInstance](Type-Classes/Instance-Synthesis/#inferInstance "Documentation for inferInstance") example : foo.[default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default") = ([default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default"), [default](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited.default")) := [rfl](Basic-Propositions/Propositional-Equality/#rfl-next "Documentation for rfl") `
[🔗](find/?domain=Verso.Genre.Manual.doc&name=inferInstanceAs "Permalink")def
```


inferInstanceAs.{u} (α : Sort u) [i : α] : α


inferInstanceAs.{u} (α : Sort u) [i : α] :
  α


```

`[inferInstanceAs](Type-Classes/Instance-Synthesis/#inferInstanceAs "Documentation for inferInstanceAs") α` synthesizes a value of any target type by typeclass inference. This is just like `[inferInstance](Type-Classes/Instance-Synthesis/#inferInstance "Documentation for inferInstance")` except that `α` is given explicitly instead of being inferred from the target type. It is especially useful when the target type is some `α'` which is definitionally equal to `α`, but the instance we are looking for is only registered for `α` (because typeclass search does not unfold most definitions, but definitional equality does.) Example:
``inferInstanceAs (Inhabited [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) : Inhabited [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [inferInstanceAs](Type-Classes/Instance-Synthesis/#inferInstanceAs "Documentation for inferInstanceAs") ([Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")) -- Inhabited Nat `
##  10.3.1. Instance Search Summary[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Type-Classes--Instance-Synthesis--Instance-Search-Summary "Permalink")
Generally speaking, instance synthesis is a recursive search procedure that may, in general, backtrack arbitrarily. Synthesis may _succeed_ with an instance term, _fail_ if no such term can be found, or get _stuck_ if there is insufficient information. A detailed description of the instance synthesis algorithm is available in Selsam, Ullrich, and de Moura (2020)Daniel Selsam, Sebastian Ullrich, and Leonardo de Moura, 2020. [“Tabled typeclass resolution”](https://arxiv.org/abs/2001.04301). arXiv:2001.04301. An instance search problem is given by a type class applied to concrete arguments; these argument values may or may not be known. Instance search attempts every locally-bound variable whose type is a class, as well as each registered instance, in order of priority and definition. When candidate instances themselves have instance-implicit parameters, they impose further synthesis tasks.
A problem is only attempted when all of the input parameters to the type class are known. When a problem cannot yet be attempted, then that branch is stuck; progress in other subproblems may result in the problem becoming solvable. Output or semi-output parameters may be either known or unknown at the start of instance search. Output parameters are ignored when checking whether an instance matches the problem, while semi-output parameters are considered.
Every candidate solution for a given problem is saved in a table; this prevents infinite regress in case of cycles as well as exponential search overheads in the presence of diamonds (that is, multiple paths by which the same goal can be achieved). A branch of the search fails when any of the following occur:
  * All potential instances have been attempted, and the search space is exhausted.
  * The instance size limit specified by the option `[synthInstance.maxSize](Type-Classes/Instance-Synthesis/#synthInstance___maxSize "Documentation for option synthInstance.maxSize")` is reached.
  * The synthesized value of an output parameter does not match the specified value in the search problem. Failed branches are not retried.


If search would otherwise fail or get stuck, the search process attempts to use matching [default instances](Type-Classes/Instance-Synthesis/#--tech-term-default-instances) in order of priority. For default instances, the input parameters do not need to be fully known, and may be instantiated by the instances parameter values. Default instances may take instance-implicit parameters, which induce further recursive search.
Successful branches in which the problem is fully known (that is, in which there are no unsolved metavariables) are pruned, and further potentially-successful instances are not attempted, because no later instance could cause the previously-succeeding branch to fail.
##  10.3.2. Instance Search Problems[🔗](find/?domain=Verso.Genre.Manual.section&name=instance-search "Permalink")
Instance search occurs during the elaboration of (potentially nullary) function applications. Some of the implicit parameters' values are forced by others; for instance, an implicit type parameter may be solved using the type of a later value argument that is explicitly provided. Implicit parameters may also be solved using information from the expected type at that point in the program. The search for instance implicit arguments may make use of the implicit argument values that have been found, and may additionally solve others.
Instance synthesis begins with the type of the instance-implicit parameter. This type must be the application of a type class to zero or more arguments; these argument values may be known or unknown when search begins. If an argument to a class is unknown, the search process will not instantiate it unless the corresponding parameter is [marked as an output parameter](Type-Classes/Instance-Synthesis/#class-output-parameters), explicitly making it an output of the instance synthesis routine.
Search may succeed, fail, or get stuck; a stuck search may occur when an unknown argument value becoming known might enable progress to be made. Stuck searches may be re-invoked when the elaborator has discovered one of the previously-unknown implicit arguments. If this does not occur, stuck searches become failures.
Tracing Instance Search
Setting the `trace.Meta.synthInstance` option to `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` causes Lean to emit a trace of the process for synthesizing an instance of a type class. This trace can be used to understand how instance synthesis succeeds and why it fails.
Here, we can see the steps Lean takes to conclude that there exists an element of the type `([Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ⊕ [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty"))` (specifically the element `[Sum.inl](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inl") 0`): Clicking a `▶` symbol expands that branch of the trace, and clicking the `▼` collapses an expanded branch.
`set_option pp.explicit true [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") set_option trace.Meta.synthInstance true [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") `[Meta.synthInstance] ✅️ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty"))
 
  * [Meta.synthInstance] new goal [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty"))
    * [Meta.synthInstance.instances] #[@instNonemptyOfInhabited, @instNonemptyOfMonad, @Sum.nonemptyLeft, @Sum.nonemptyRight]
 
  * [Meta.synthInstance] ✅️ apply @Sum.nonemptyRight to [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")) 
    * [Meta.synthInstance.tryResolve] ✅️ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")) ≟ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty"))
 
    * [Meta.synthInstance] new goal [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")
      * [Meta.synthInstance.instances] #[@instNonemptyOfInhabited, @instNonemptyOfMonad]
 
 
  * [Meta.synthInstance] ❌️ apply @instNonemptyOfMonad to [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")
    * [Meta.synthInstance.tryResolve] ❌️ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") ≟ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") (?m.5 ?m.6)
 
  * [Meta.synthInstance] ✅️ apply @instNonemptyOfInhabited to [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") 
    * [Meta.synthInstance.tryResolve] ✅️ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") ≟ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")
 
    * [Meta.synthInstance] new goal [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")
      * [Meta.synthInstance.instances] #[@instInhabitedOfMonad, @Lake.inhabitedOfNilTrace, @instInhabitedOfApplicative_manual]
 
 
  * [Meta.synthInstance] ❌️ apply @instInhabitedOfApplicative_manual to [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")
    * [Meta.synthInstance.tryResolve] ❌️ [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") ≟ [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") (?m.8 ?m.7)
 
  * [Meta.synthInstance] ✅️ apply @Lake.inhabitedOfNilTrace to [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") 
    * [Meta.synthInstance.tryResolve] ✅️ [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") ≟ [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")
 
    * [Meta.synthInstance] no instances for Lake.NilTrace [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")
      * [Meta.synthInstance.instances] #[]
 
 
  * [Meta.synthInstance] ❌️ apply @instInhabitedOfMonad to [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")
    * [Meta.synthInstance.tryResolve] ❌️ [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") ≟ [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") (?m.8 ?m.7)
 
  * [Meta.synthInstance] ✅️ apply @Sum.nonemptyLeft to [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")) 
    * [Meta.synthInstance.tryResolve] ✅️ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")) ≟ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty"))
 
    * [Meta.synthInstance] new goal [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
      * [Meta.synthInstance.instances] #[@instNonemptyOfInhabited, @instNonemptyOfMonad]
 
 
  * [Meta.synthInstance] ❌️ apply @instNonemptyOfMonad to [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
    * [Meta.synthInstance.tryResolve] ❌️ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ≟ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") (?m.5 ?m.6)
 
  * [Meta.synthInstance] ✅️ apply @instNonemptyOfInhabited to [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") 
    * [Meta.synthInstance.tryResolve] ✅️ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ≟ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
 
    * [Meta.synthInstance] new goal [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
      * [Meta.synthInstance.instances] #[@instInhabitedOfMonad, @Lake.inhabitedOfNilTrace, @instInhabitedOfApplicative_manual, instInhabitedNat]
 
 
  * [Meta.synthInstance] ✅️ apply instInhabitedNat to [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") 
    * [Meta.synthInstance.tryResolve] ✅️ [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ≟ [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
 
    * [Meta.synthInstance.answer] ✅️ [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
 
 
  * [Meta.synthInstance.resume] propagating [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") to subgoal [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") of [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") 
    * [Meta.synthInstance.resume] size: 1
 
    * [Meta.synthInstance.answer] ✅️ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
 
 
  * [Meta.synthInstance.resume] propagating [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") to subgoal [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") of [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")) 
    * [Meta.synthInstance.resume] size: 2
 
    * [Meta.synthInstance.answer] ✅️ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty"))
 
 
  * [Meta.synthInstance] result @Sum.nonemptyLeft [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") (@instNonemptyOfInhabited [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") instInhabitedNat)
 
``@Sum.nonemptyLeft [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") (@instNonemptyOfInhabited [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") instInhabitedNat)`[#synth](Interacting-with-Lean/#Lean___Parser___Command___synth "Documentation for syntax") [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ⊕ [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")) `
```
[Meta.synthInstance] ✅️ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty"))


  * [Meta.synthInstance] new goal [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty"))
    * [Meta.synthInstance.instances] #[@instNonemptyOfInhabited, @instNonemptyOfMonad, @Sum.nonemptyLeft, @Sum.nonemptyRight]


  * [Meta.synthInstance] ✅️ apply @Sum.nonemptyRight to [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty"))

    * [Meta.synthInstance.tryResolve] ✅️ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")) ≟ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty"))


    * [Meta.synthInstance] new goal [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")
      * [Meta.synthInstance.instances] #[@instNonemptyOfInhabited, @instNonemptyOfMonad]




  * [Meta.synthInstance] ❌️ apply @instNonemptyOfMonad to [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")
    * [Meta.synthInstance.tryResolve] ❌️ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") ≟ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") (?m.5 ?m.6)


  * [Meta.synthInstance] ✅️ apply @instNonemptyOfInhabited to [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")

    * [Meta.synthInstance.tryResolve] ✅️ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") ≟ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")


    * [Meta.synthInstance] new goal [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")
      * [Meta.synthInstance.instances] #[@instInhabitedOfMonad, @Lake.inhabitedOfNilTrace, @instInhabitedOfApplicative_manual]




  * [Meta.synthInstance] ❌️ apply @instInhabitedOfApplicative_manual to [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")
    * [Meta.synthInstance.tryResolve] ❌️ [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") ≟ [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") (?m.8 ?m.7)


  * [Meta.synthInstance] ✅️ apply @Lake.inhabitedOfNilTrace to [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")

    * [Meta.synthInstance.tryResolve] ✅️ [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") ≟ [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")


    * [Meta.synthInstance] no instances for Lake.NilTrace [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")
      * [Meta.synthInstance.instances] #[]




  * [Meta.synthInstance] ❌️ apply @instInhabitedOfMonad to [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")
    * [Meta.synthInstance.tryResolve] ❌️ [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") ≟ [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") (?m.8 ?m.7)


  * [Meta.synthInstance] ✅️ apply @Sum.nonemptyLeft to [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty"))

    * [Meta.synthInstance.tryResolve] ✅️ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")) ≟ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty"))


    * [Meta.synthInstance] new goal [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
      * [Meta.synthInstance.instances] #[@instNonemptyOfInhabited, @instNonemptyOfMonad]




  * [Meta.synthInstance] ❌️ apply @instNonemptyOfMonad to [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
    * [Meta.synthInstance.tryResolve] ❌️ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ≟ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") (?m.5 ?m.6)


  * [Meta.synthInstance] ✅️ apply @instNonemptyOfInhabited to [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")

    * [Meta.synthInstance.tryResolve] ✅️ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ≟ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


    * [Meta.synthInstance] new goal [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
      * [Meta.synthInstance.instances] #[@instInhabitedOfMonad, @Lake.inhabitedOfNilTrace, @instInhabitedOfApplicative_manual, instInhabitedNat]




  * [Meta.synthInstance] ✅️ apply instInhabitedNat to [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")

    * [Meta.synthInstance.tryResolve] ✅️ [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ≟ [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")


    * [Meta.synthInstance.answer] ✅️ [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")




  * [Meta.synthInstance.resume] propagating [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") to subgoal [Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") of [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")

    * [Meta.synthInstance.resume] size: 1


    * [Meta.synthInstance.answer] ✅️ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")




  * [Meta.synthInstance.resume] propagating [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") to subgoal [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") of [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty"))

    * [Meta.synthInstance.resume] size: 2


    * [Meta.synthInstance.answer] ✅️ [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty"))




  * [Meta.synthInstance] result @Sum.nonemptyLeft [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") (@instNonemptyOfInhabited [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") instInhabitedNat)



```

By exploring the trace, it is possible to follow the depth-first, backtracking search that Lean uses for type class instance search. This can take a little practice to get used to! In the example above, Lean follows these steps:
  * Lean considers the first goal, `[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty"))`. Lean sees four ways of possibly satisfying this goal:
    * The `Sum.nonemptyRight` instance, which would create a sub-goal `[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")`.
    * The `Sum.nonemptyLeft` instance, which would create a sub-goal `[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`.
    * The `instNonemptyOfMonad` instance, which would create two sub-goals `[Monad](Functors___-Monads-and--do--Notation/#Monad___mk "Documentation for Monad") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat"))` and `[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`.
    * The `instNonemptyOfInhabited` instance, which would create a sub-goal `[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") ([Sum](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty"))`.
  * The first sub-goal, `[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")`, is considered. Lean sees two ways of possibly satisfying this goal:
    * The `instNonemptyOfMonad` instance, which is rejected. It can't be used because the type `[Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")` is not the application of a monad to a type. Lean describes this as a failure of `trace.Meta.synthInstance.tryResolve` to solve the equation `Nonempty Empty ≟ Nonempty (?m.5 ?m.6)`.
    * The `instNonemptyOfInhabited` instance, which would create a sub-goal `[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")`.
  * The newly-generated sub-goal, `[Inhabited](Type-Classes/Basic-Classes/#Inhabited___mk "Documentation for Inhabited") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")`, is considered. Lean only sees one way of possibly satisfying this goal, `instInhabitedOfMonad`, which is rejected. As before, this is because the type `[Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")` is not the application of a monad to a type.
  * At this point, there are no remaining options for achieving the original first sub-goal. The search backtracks to the second original sub-goal, `[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`. This search eventually succeeds.


The third and fourth original sub-goals are never considered. Once the search for `[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` succeeds, the ``Lean.Parser.Command.synth : command``[`#synth`](Interacting-with-Lean/#Lean___Parser___Command___synth) command finishes and outputs the solution:

```
@Sum.nonemptyLeft [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") (@instNonemptyOfInhabited [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") instInhabitedNat)
```

##  10.3.3. Candidate Instances[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Type-Classes--Instance-Synthesis--Candidate-Instances "Permalink")
Instance synthesis uses both local and global instances in its search. _Local instances_ are those available in the local context; they may be either parameters to a function or locally defined with `let`. Local instances do not need to be indicated specially; any local variable whose type is a type class is a candidate for instance synthesis. _Global instances_ are those available in the global environment; every global instance is a defined name with the `instance` attribute applied.``Lean.Parser.Command.declaration : command```instance` declarations automatically apply the `instance` attribute.
Local Instances
In this example, `[addPairs](Type-Classes/Instance-Synthesis/#addPairs-_LPAR_in-Local-Instances_RPAR_ "Definition of example")` contains a locally-defined instance of `[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") [NatPair](Type-Classes/Instance-Synthesis/#NatPair-_LPAR_in-Local-Instances_RPAR_ "Definition of example")`:
`structure NatPair where   x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")  def addPairs (p1 p2 : [NatPair](Type-Classes/Instance-Synthesis/#NatPair-_LPAR_in-Local-Instances_RPAR_ "Definition of example")) : [NatPair](Type-Classes/Instance-Synthesis/#NatPair-_LPAR_in-Local-Instances_RPAR_ "Definition of example") :=   let _ : [Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") [NatPair](Type-Classes/Instance-Synthesis/#NatPair-_LPAR_in-Local-Instances_RPAR_ "Definition of example") :=     ⟨fun ⟨x1, y1⟩ ⟨x2, y2⟩ => ⟨x1 + x2, y1 + y2⟩⟩   p1 + p2 `
The local instance is used for the addition, having been found by instance synthesis.
[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgHIEMQAVUEsyIO4AW8CAUIogB6IBcK65iAnrfSKaQCbwBmiqnTllzBEACgAOARkQSATKzSYcYAJSL0wvDQC8jADbwQiAPqsAgoLZbaeihUAX5DwgA7RA8pSANMymBL8ndKOR8mOQCdAD5AmQBqKmDfRDjQvz9GaSTZOSA"\))
Local Instances Have Priority
Here, `[addPairs](Type-Classes/Instance-Synthesis/#addPairs-_LPAR_in-Local-Instances-Have-Priority_RPAR_ "Definition of example")` contains a locally-defined instance of `[Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") [NatPair](Type-Classes/Instance-Synthesis/#NatPair-_LPAR_in-Local-Instances-Have-Priority_RPAR_ "Definition of example")`, even though there is a global instance:
`structure NatPair where   x : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")   y : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")  instance : [Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") [NatPair](Type-Classes/Instance-Synthesis/#NatPair-_LPAR_in-Local-Instances-Have-Priority_RPAR_ "Definition of example") where   [add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add.add")     | ⟨x1, y1⟩, ⟨x2, y2⟩ => ⟨x1 + x2, y1 + y2⟩  def addPairs (p1 p2 : [NatPair](Type-Classes/Instance-Synthesis/#NatPair-_LPAR_in-Local-Instances-Have-Priority_RPAR_ "Definition of example")) : [NatPair](Type-Classes/Instance-Synthesis/#NatPair-_LPAR_in-Local-Instances-Have-Priority_RPAR_ "Definition of example") :=   let _ : [Add](Type-Classes/Basic-Classes/#Add___mk "Documentation for Add") [NatPair](Type-Classes/Instance-Synthesis/#NatPair-_LPAR_in-Local-Instances-Have-Priority_RPAR_ "Definition of example") :=     ⟨fun _ _ => ⟨0, 0⟩⟩   p1 + p2 `
The local instance is selected instead of the global one:
``{ x := 0, y := 0 }`[#eval](Interacting-with-Lean/#Lean___Parser___Command___eval "Documentation for syntax") [addPairs](Type-Classes/Instance-Synthesis/#addPairs-_LPAR_in-Local-Instances-Have-Priority_RPAR_ "Definition of example") ⟨1, 2⟩ ⟨5, 2⟩ `
```
{ x := 0, y := 0 }
```

[Live ↪](javascript:openLiveLink\("M4FwTgrgxiFgpgAgHIEMQAVUEsyIO4AW8CAUIogB6IBcK65iAnrfSKadgHaipdRI6AQQAmItllwFiZCqjGMKAH0SAL8koBGADTMNgS/Id6gEw6mRvYgC8APjWbEAaiondj5uY4j4AM0TyRkmDAiAAUAA4aiGFGrGiYOGAAlLHogbSWjAA28CCIAPqsouJxaTQZFBSq3hBc+XU2agAMOo16eowRbtEcAMTwAG6omX5igcGq2ojmagCsOuZAA"\))
##  10.3.4. Instance Parameters and Synthesis[🔗](find/?domain=Verso.Genre.Manual.section&name=instance-synth-parameters "Permalink")
The search process for instances is largely governed by class parameters. Type classes take a certain number of parameters, and instances are tried during the search when their choice of parameters is _compatible_ with those in the class type for which the instance is being synthesized.
Instances themselves may also take parameters, but the role of instances' parameters in instance synthesis is very different. Instances' parameters represent either variables that may be instantiated by instance synthesis or further synthesis work to be done before the instance can be used. In particular, parameters to instances may be explicit, implicit, or instance-implicit. If they are instance implicit, then they induce further recursive instance searching, while explicit or implicit parameters must be solved by unification.
Implicit and Explicit Parameters to Instances
While instances typically take parameters either implicitly or instance-implicitly, explicit parameters may be filled out as if they were implicit during instance synthesis. In this example, `[aNonemptySumInstance](Type-Classes/Instance-Synthesis/#aNonemptySumInstance-_LPAR_in-Implicit-and-Explicit-Parameters-to-Instances_RPAR_ "Definition of example")` is found by synthesis, applied explicitly to `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, which is needed to make it type-correct.
`instance aNonemptySumInstance     (α : Type) {β : Type} [inst : [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") α] :     [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") (α ⊕ β) :=   let ⟨x⟩ := inst   ⟨[.inl](Basic-Types/Sum-Types/#Sum___inl "Documentation for Sum.inl") x⟩ ``set_option pp.explicit true [in](Namespaces-and-Sections/#Lean___Parser___Command___in "Documentation for syntax") `@[aNonemptySumInstance](Type-Classes/Instance-Synthesis/#aNonemptySumInstance-_LPAR_in-Implicit-and-Explicit-Parameters-to-Instances_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") (@instNonemptyOfInhabited [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") instInhabitedNat)`[#synth](Interacting-with-Lean/#Lean___Parser___Command___synth "Documentation for syntax") [Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") ([Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") ⊕ [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")) `
In the output, both the explicit argument `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` and the implicit argument `[Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty")` were found by unification with the search goal, while the `[Nonempty](Type-Classes/Basic-Classes/#Nonempty___intro "Documentation for Nonempty") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` instance was found via recursive instance synthesis.

```
@[aNonemptySumInstance](Type-Classes/Instance-Synthesis/#aNonemptySumInstance-_LPAR_in-Implicit-and-Explicit-Parameters-to-Instances_RPAR_ "Definition of example") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Empty](Basic-Types/The-Empty-Type/#Empty "Documentation for Empty") (@instNonemptyOfInhabited [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") instInhabitedNat)
```

[Live ↪](javascript:openLiveLink\("JYOwzgLghiDGCmACKA5A9ieBbADhAngMoCuWAkuNHPAFCL2IAUgjcCIBciAKvjvAJSIA3oCbgdlx7wAvogDaoSGPSZcBRMwC67OgyXY8+Jq0CpRImEC2AXm0AbeBESAL8gAegS/J2FxPIjaHAOlDWiK40NGB2APpoeMAYiDg4vvBOONbAsMD2EABOxEigNADEYPggEAAWiLoqBowoUPYmAKLVfEA"\))
##  10.3.5. Output Parameters[🔗](find/?domain=Verso.Genre.Manual.section&name=class-output-parameters "Permalink")
By default, the parameters of a type class are considered to be _inputs_ to the search process. If the parameters are not known, then the search process gets stuck, because choosing an instance would require the parameters to have values that match those in the instance, which cannot be determined on the basis of incomplete information. In most cases, guessing instances would make instance synthesis unpredictable.
In some cases, however, the choice of one parameter should cause an automatic choice of another. For example, the overloaded membership predicate type class `Membership` treats the type of elements of a data structure as an output, so that the type of element can be determined by the type of data structure at a use site, instead of requiring that there be sufficient type annotations to determine _both_ types prior to starting instance synthesis. An element of a `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` can be concluded to be a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` simply on the basis of its membership in the list.
Type class parameters can be declared as outputs by wrapping their types in the `[outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam")` [gadget](Type-Classes/Class-Declarations/#--tech-term-gadgets). When a class parameter is an _output parameter_ , instance synthesis will not require that it be known; in fact, any existing value is ignored completely. The first instance that matches the input parameters is selected, and that instance's assignment of the output parameter becomes its value. If there was a pre-existing value, then it is compared with the assignment after synthesis is complete, and it is an error if they do not match.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=outParam "Permalink")def
```


outParam.{u} (α : Sort u) : Sort u


outParam.{u} (α : Sort u) : Sort u


```

Gadget for marking output parameters in type classes.
For example, the `Membership` class is defined as:

```
class Membership (α : outParam (Type u)) (γ : Type v)

```

This means that whenever a typeclass goal of the form `Membership ?α ?γ` comes up, Lean will wait to solve it until `?γ` is known, but then it will run typeclass inference, and take the first solution it finds, for any value of `?α`, which thereby determines what `?α` should be.
This expresses that in a term like `a ∈ s`, `s` might be a `Set α` or `[List](Basic-Types/Linked-Lists/#List___nil "Documentation for List") α` or some other type with a membership operation, and in each case the "member" type `α` is determined by looking at the container type.
Output Parameters and Stuck Search
This serialization framework provides a way to convert values to some underlying storage type:
`class Serialize (input output : Type) where   ser : input → output [export](Namespaces-and-Sections/#Lean___Parser___Command___export "Documentation for syntax") Serialize (ser)  instance : Serialize [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") where   ser n := toString n  instance [Serialize α γ] [Serialize β γ] [[Append](Type-Classes/Basic-Classes/#Append___mk "Documentation for Append") γ] :     Serialize (α × β) γ where   ser     | (x, y) => ser x ++ ser y `
In this example, the output type is unknown.
`example := `typeclass instance problem is stuck   Serialize [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") ?m.5  Note: Lean will not try to resolve this typeclass instance problem because the second type argument to `Serialize` is a metavariable. This argument must be fully determined before Lean will try to resolve the typeclass.  Hint: Adding type annotations and supplying implicit arguments to functions can give Lean more information for typeclass resolution. For example, if you have a variable `x` that you intend to be a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, but Lean reports it as having an unresolved type like `?m`, replacing `x` with `(x : Nat)` can get typeclass resolution un-stuck.`ser (2, 3) `
Instance synthesis can't select the `Serialize [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` instance, and thus the `[Append](Type-Classes/Basic-Classes/#Append___mk "Documentation for Append") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` instance, because that would require instantiating the output type as `[String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`, so the search gets stuck:

```
typeclass instance problem is stuck
  Serialize [(](Basic-Types/Tuples/#Prod___mk "Documentation for Prod")[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [×](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")[)](Basic-Types/Tuples/#Prod___mk "Documentation for Prod") ?m.5

Note: Lean will not try to resolve this typeclass instance problem because the second type argument to `Serialize` is a metavariable. This argument must be fully determined before Lean will try to resolve the typeclass.

Hint: Adding type annotations and supplying implicit arguments to functions can give Lean more information for typeclass resolution. For example, if you have a variable `x` that you intend to be a `[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")`, but Lean reports it as having an unresolved type like `?m`, replacing `x` with `(x : Nat)` can get typeclass resolution un-stuck.
```

As the message indicates, one way to fix the problem is to supply an expected type:
`example : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") := ser (2, 3) `
The other is to make the output type into an output parameter:
`class Serialize (input : Type) (output : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") Type) where   ser : input → output [export](Namespaces-and-Sections/#Lean___Parser___Command___export "Documentation for syntax") Serialize (ser)  instance : Serialize [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") where   ser n := toString n  instance [Serialize α γ] [Serialize β γ] [[Append](Type-Classes/Basic-Classes/#Append___mk "Documentation for Append") γ] :     Serialize (α × β) γ where   ser     | (x, y) => ser x ++ ser y `
Now, instance synthesis is free to select the `Serialize [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")` instance, which solves the unknown implicit `output` parameter of `ser`:
`example := ser (2, 3) `
Output Parameters with Pre-Existing Values
The class `[OneSmaller](Type-Classes/Instance-Synthesis/#OneSmaller-_LPAR_in-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example")` represents a way to transform non-maximal elements of a type into elements of a type that has one fewer elements. There are two separate instances that can match an input type `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`, with different outputs:
`class OneSmaller (α : Type) (β : [outParam](Type-Classes/Instance-Synthesis/#outParam "Documentation for outParam") Type) where   biggest : α   shrink : (x : α) → x ≠ biggest → β  instance : [OneSmaller](Type-Classes/Instance-Synthesis/#OneSmaller-_LPAR_in-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) α where   [biggest](Type-Classes/Instance-Synthesis/#OneSmaller___biggest-_LPAR_in-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") := [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")   [shrink](Type-Classes/Instance-Synthesis/#OneSmaller___shrink-_LPAR_in-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example")     | [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x, _ => x  instance : [OneSmaller](Type-Classes/Instance-Synthesis/#OneSmaller-_LPAR_in-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")) where   [biggest](Type-Classes/Instance-Synthesis/#OneSmaller___biggest-_LPAR_in-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") := [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")   [shrink](Type-Classes/Instance-Synthesis/#OneSmaller___shrink-_LPAR_in-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example")     | [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none"), _ => [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")     | [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false"), _ => [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ()  instance : [OneSmaller](Type-Classes/Instance-Synthesis/#OneSmaller-_LPAR_in-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") where   [biggest](Type-Classes/Instance-Synthesis/#OneSmaller___biggest-_LPAR_in-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") := [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")   [shrink](Type-Classes/Instance-Synthesis/#OneSmaller___shrink-_LPAR_in-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example")     | [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false"), _ => () `
Because instance synthesis selects the most recently defined instance, the following code is an error:
`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") `failed to synthesize instance of type class   [OneSmaller](Type-Classes/Instance-Synthesis/#OneSmaller-_LPAR_in-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")  Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.`[OneSmaller.shrink](Type-Classes/Instance-Synthesis/#OneSmaller___shrink-_LPAR_in-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") (β := [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) sorry `
```
failed to synthesize instance of type class
  [OneSmaller](Type-Classes/Instance-Synthesis/#OneSmaller-_LPAR_in-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")

Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
```

The `[OneSmaller](Type-Classes/Instance-Synthesis/#OneSmaller-_LPAR_in-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit"))` instance was selected during instance synthesis, without regard to the supplied value of `β`.
[Live ↪](javascript:openLiveLink\("MYGwhgzhAEDyB2BTAygWzCEiBO0AUgjcDQBc0AKgJ4AOiAlPoE3AJ0A9gK4AuACmNmKuWp1oAdwAWORACho0AEYBLAOZLEEDswIzoEMdgXwA1szwAPTfUBJhNHOADInnLV66NYZSpB9WHjBEzBCjomDj4sFQcCizw0AT0ROKS2ooqahrEALzQ8FHSsrr6RtqyAD46LKh+pgA00AD60OkAfDbunhzevv5IaBhYuHhhEVHQAEIsLCD0A+GR0QCq8Aoc9AnYuQ4pzhllFdAc2Gzr+QaGRdCl2Ug19U1ZOWelEOV+AGYYEIjXDc1Pu3i0rXgXh8flIAR6wVwYwm0AWS1EEjWSUcqRImX2h20x0KshK0DeIA+X1u/yAA"\))
_Semi-output parameters_ are like output parameters in that they are not required to be known prior to synthesis commencing; unlike output parameters, their values are taken into account when selecting instances.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=semiOutParam "Permalink")def
```


semiOutParam.{u} (α : Sort u) : Sort u


semiOutParam.{u} (α : Sort u) : Sort u


```

Gadget for marking semi output parameters in type classes.
Semi-output parameters influence the order in which arguments to type class instances are processed. Lean determines an order where all non-(semi-)output parameters to the instance argument have to be figured out before attempting to synthesize an argument (that is, they do not contain assignable metavariables created during TC synthesis). This rules out instances such as `[Mul β] : Add α` (because `β` could be anything). Marking a parameter as semi-output is a promise that instances of the type class will always fill in a value for that parameter.
For example, the `[Coe](Coercions/#Coe___mk "Documentation for Coe")` class is defined as:

```
class Coe (α : semiOutParam (Sort u)) (β : Sort v)

```

This means that all `[Coe](Coercions/#Coe___mk "Documentation for Coe")` instances should provide a concrete value for `α` (i.e., not an assignable metavariable). An instance like `[Coe](Coercions/#Coe___mk "Documentation for Coe") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") [Int](Basic-Types/Integers/#Int___ofNat "Documentation for Int")` or `[Coe](Coercions/#Coe___mk "Documentation for Coe") α ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α)` is fine, but `[Coe](Coercions/#Coe___mk "Documentation for Coe") α [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")` is not since it does not provide a value for `α`.
Semi-output parameters impose a requirement on instances: each instance of a class with semi-output parameters should determine the values of its semi-output parameters.
Semi-Output Parameters with Pre-Existing Values
The class `[OneSmaller](Type-Classes/Instance-Synthesis/#OneSmaller-_LPAR_in-Semi-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example")` represents a way to transform non-maximal elements of a type into elements of a type that one fewer elements. It has two separate instances that can match an input type `[Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`, with different outputs:
`class OneSmaller (α : Type) (β : [semiOutParam](Type-Classes/Instance-Synthesis/#semiOutParam "Documentation for semiOutParam") Type) where   biggest : α   shrink : (x : α) → x ≠ biggest → β  instance : [OneSmaller](Type-Classes/Instance-Synthesis/#OneSmaller-_LPAR_in-Semi-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") α) α where   [biggest](Type-Classes/Instance-Synthesis/#OneSmaller___biggest-_LPAR_in-Semi-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") := [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")   [shrink](Type-Classes/Instance-Synthesis/#OneSmaller___shrink-_LPAR_in-Semi-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example")     | [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") x, _ => x  instance : [OneSmaller](Type-Classes/Instance-Synthesis/#OneSmaller-_LPAR_in-Semi-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit")) where   [biggest](Type-Classes/Instance-Synthesis/#OneSmaller___biggest-_LPAR_in-Semi-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") := [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")   [shrink](Type-Classes/Instance-Synthesis/#OneSmaller___shrink-_LPAR_in-Semi-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example")     | [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none"), _ => [none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")     | [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false"), _ => [some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") ()  instance : [OneSmaller](Type-Classes/Instance-Synthesis/#OneSmaller-_LPAR_in-Semi-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit") where   [biggest](Type-Classes/Instance-Synthesis/#OneSmaller___biggest-_LPAR_in-Semi-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") := [true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")   [shrink](Type-Classes/Instance-Synthesis/#OneSmaller___shrink-_LPAR_in-Semi-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example")     | [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false"), _ => () `
Because instance synthesis takes semi-output parameters into account when selecting instances, the `[OneSmaller](Type-Classes/Instance-Synthesis/#OneSmaller-_LPAR_in-Semi-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) ([Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Unit](Basic-Types/The-Unit-Type/#Unit "Documentation for Unit"))` instance is passed over due to the supplied value for `β`:
``[OneSmaller.shrink](Type-Classes/Instance-Synthesis/#OneSmaller___shrink-_LPAR_in-Semi-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) ⋯ : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [OneSmaller.shrink](Type-Classes/Instance-Synthesis/#OneSmaller___shrink-_LPAR_in-Semi-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") (β := [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")) ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) sorry `
```
[OneSmaller.shrink](Type-Classes/Instance-Synthesis/#OneSmaller___shrink-_LPAR_in-Semi-Output-Parameters-with-Pre-Existing-Values_RPAR_ "Definition of example") ([some](Basic-Types/Optional-Values/#Option___none "Documentation for Option.some") [false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")) ⋯ : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

[Live ↪](javascript:openLiveLink\("MYGwhgzhAEDyB2BTAygWzCEiBO0AUgjcDQBc0AKgJ4AOiAlPoE3AJ0EiqAlrAK4AuACmGxhU5anWgB3ABY5EAKGjQARuwDmqxBB7MCCllOzt4Aa2Z4AHjvqAkwmiXABkTK1GrdFsM5co1rDxgiZgQUdEwcfFgqHnYAe3hoAnoiaVk9FXVNbWIAXmh4WPlFCAMjYz1FAB8WaNQA8wAaaAB9aCyAPjtPbx5ff0CkNAwsXDwIqNjoACFo6JB6EciYuIBVeHYeemTsAqd012yqmugebC5tosMTMuhKvKQG5rbc/KvKiGqAgDMMVnuW9rfDnhaJ14D4/AFSEEBqFcFMZtAVmtJDItqlnBkSDljqc9OcSi9oF8QD8mn98MC5ABiYAyYCmKEhIYAOjxJkYmMm01m+ABn2+4je2GwFCAA"\))
##  10.3.6. Default Instances[🔗](find/?domain=Verso.Genre.Manual.section&name=default-instance-synth "Permalink")
When instance synthesis would otherwise fail, having not selected an instance, the _default instances_ specified using the `default_instance` attribute are attempted in order of priority. When priorities are equal, more recently-defined default instances are chosen before earlier ones. The first default instance that causes the search to succeed is chosen.
Default instances may induce further recursive instance search if the default instances themselves have instance-implicit parameters. If the recursive search fails, the search process backtracks and the next default instance is tried.
##  10.3.7. “Morally Canonical” Instances[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Type-Classes--Instance-Synthesis--___Morally-Canonical___-Instances "Permalink")
During instance synthesis, if a goal is fully known (that is, contains no metavariables) and search succeeds, no further instances will be attempted for that same goal. In other words, when search succeeds for a goal in a way that can't be refuted by a subsequent increase in information, the goal will not be attempted again, even if there are other instances that could potentially have been used. This optimization can prevent a failure in a later branch of an instance synthesis search from causing spurious backtracking that replaces a fast solution from an earlier branch with a slow exploration of a large state space.
The optimization relies on the assumption that instances are _morally canonical_. Even if there is more than one potential implementation of a given type class's overloaded operations, or more than one way to synthesize an instance due to diamonds, _any discovered instance should be considered as good as any other_. In other words, there's no need to consider _all_ potential instances so long as one of them has been guaranteed to work. The optimization may be disabled with the backwards-compatibility option `[backward.synthInstance.canonInstances](Type-Classes/Instance-Synthesis/#backward___synthInstance___canonInstances "Documentation for option backward.synthInstance.canonInstances")`, which may be removed in a future version of Lean.
Code that uses instance-implicit parameters should be prepared to consider all instances as equivalent. In other words, it should be robust in the face of differences in synthesized instances. When the code relies on instances _in fact_ being equivalent, it should either explicitly manipulate instances (e.g. via local definitions, by saving them in structure fields, or having a structure inherit from the appropriate class) or it should make this dependency explicit in the type, so that different choices of instance lead to incompatible types.
##  10.3.8. Options[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Type-Classes--Instance-Synthesis--Options "Permalink")
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=backward.synthInstance.canonInstances "Permalink")option
```
backward.synthInstance.canonInstances
```

Default value: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
use optimization that relies on 'morally canonical' instances during type class resolution
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=synthInstance.maxHeartbeats "Permalink")option
```
synthInstance.maxHeartbeats
```

Default value: `20000`
maximum amount of heartbeats per typeclass resolution problem. A heartbeat is number of (small) memory allocations (in thousands), 0 means no limit
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=synthInstance.maxSize "Permalink")option
```
synthInstance.maxSize
```

Default value: `128`
maximum number of instances used to construct a solution in the type class instance synthesis procedure
[←10.2. Instance Declarations](Type-Classes/Instance-Declarations/#instance-declarations "10.2. Instance Declarations")[10.4. Deriving Instances→](Type-Classes/Deriving-Instances/#deriving-instances "10.4. Deriving Instances")

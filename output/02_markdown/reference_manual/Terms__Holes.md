[←13.8. Pattern Matching](Terms/Pattern-Matching/#pattern-matching "13.8. Pattern Matching")[13.10. Type Ascription→](Terms/Type-Ascription/#The-Lean-Language-Reference--Terms--Type-Ascription "13.10. Type Ascription")
#  13.9. Holes[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Terms--Holes "Permalink")
A _hole_ or _placeholder term_ is a term that indicates the absence of instructions to the elaborator. In terms, holes can be automatically filled when the surrounding context would only allow one type-correct term to be written where the hole is. Otherwise, a hole is an error. In patterns, holes represent universal patterns that can match anything.
syntaxHoles
Holes are written with underscores.

```
term ::= ...
    | 


A _hole_ (or _placeholder term_), which stands for an unknown term that is expected to be inferred based on context.
For example, in @id _ Nat.zero, the _ must be the type of Nat.zero, which is Nat.


The way this works is that holes create fresh metavariables.
The elaborator is allowed to assign terms to metavariables while it is checking definitional equalities.
This is often known as _unification_.


Normally, all holes must be solved for. However, there are a few contexts where this is not necessary:




  * In match patterns, holes are catch-all patterns.


  * In some tactics, such as refine' and apply, unsolved-for placeholders become new goals.




Related concept: implicit parameters are automatically filled in with holes during the elaboration process.


See also ?m syntax (synthetic holes).


_
```

Filling Holes with Unification
The function `[the](Terms/Holes/#the-_LPAR_in-Filling-Holes-with-Unification_RPAR_ "Definition of example")` can be used similarly to ``Lean.Parser.Term.show : term```show` or a [type ascription](Terms/Type-Ascription/#--tech-term-Type-ascriptions).
`def the (α : Sort u) (x : α) : α := x `
If the second parameter's type can be inferred, then the first parameter can be a hole. Both of these commands are equivalent:
``[the](Terms/Holes/#the-_LPAR_in-Filling-Holes-with-Unification_RPAR_ "Definition of example") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") "Hello!" : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [the](Terms/Holes/#the-_LPAR_in-Filling-Holes-with-Unification_RPAR_ "Definition of example") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") "Hello!" `[the](Terms/Holes/#the-_LPAR_in-Filling-Holes-with-Unification_RPAR_ "Definition of example") [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String") "Hello" : [String](Basic-Types/Strings/#String___ofByteArray "Documentation for String")`[#check](Interacting-with-Lean/#Lean___Parser___Command___check "Documentation for syntax") [the](Terms/Holes/#the-_LPAR_in-Filling-Holes-with-Unification_RPAR_ "Definition of example") _ "Hello" `
[Live ↪](javascript:openLiveLink\("CYUwZgBALgFiEApCNwBAXBAygewE5QgK4CUiAHmhEieiqgLwSkBQTAxAMZzsDW0cmUHAEsAdgHMIAIgASIADZysAQkksOXXrHgB9KbIVZJQA"\))
When writing proofs, it can be convenient to explicitly introduce unknown values. This is done via _synthetic holes_ , which are never solved by unification and may occur in multiple positions. They are primarily useful in tactic proofs, and are described in [the section on metavariables in proofs](Tactic-Proofs/Reading-Proof-States/#metavariables-in-proofs).
syntaxSynthetic Holes

```
term ::= ...
    | 


A _synthetic hole_ (or _synthetic placeholder_), which stands for an unknown term that should be synthesized using tactics.




  * 
?_ creates a fresh metavariable with an auto-generated name.


  * 
?m either refers to a pre-existing metavariable named m or creates a fresh metavariable with that name.




In particular, the synthetic hole syntax creates "synthetic opaque metavariables",
the same kind of metavariable used to represent goals in the tactic state.


Synthetic holes are similar to holes in that _ also creates metavariables,
but synthetic opaque metavariables have some different properties:




  * In tactics such as refine, only synthetic holes yield new goals.


  * During elaboration, unification will not solve for synthetic opaque metavariables, they are "opaque".
This is to prevent counterintuitive behavior such as disappearing goals.


  * When synthetic holes appear under binders, they capture local variables using a more complicated mechanism known as delayed assignment.




## Delayed assigned metavariables


This section gives an overview of some technical details of synthetic holes, which you should feel free to skip.
Understanding delayed assignments is mainly useful for those who are working on tactics and other metaprogramming.
It is included here until there is a suitable place for it in the reference manual.


When a synthetic hole appears under a binding construct, such as for example fun (x : α) (y : β) => ?s,
the system creates a _delayed assignment_. This consists of




  1. A metavariable ?m of type (x : α) → (y : β) → γ x y whose local context is the local context outside the fun,
  where γ x y is the type of ?s. Recall that x and y appear in the local context of ?s.


  2. A delayed assignment record associating ?m to ?s and the variables #[x, y] in the local context of ?s





Then, this function elaborates as fun (x : α) (y : β) => ?m x y, where one should understand x and y here
as being De Bruijn indexes, since Lean uses the locally nameless encoding of lambda calculus.


Once ?s is fully solved for, in the sense that after metavariable instantiation it is a metavariable-free term e,
then we can make the assignment ?m := fun (x' : α) (y' : β) => e[x := x', y := y'].
(Implementation note: Lean only instantiates full applications ?m x' y' of delayed assigned metavariables, to skip forming this function.)
This delayed assignment mechanism is essential to the operation of basic tactics like intro,
and a good mental model is that it is a way to "apply" the metavariable ?s by substituting values in for some of its local variables.
While it would be easier to immediately assign ?s := ?m x y,
delayed assignment preserves ?s as an unsolved-for metavariable with a local context that still contains x and y,
which is exactly what tactics like intro need.


By default, delayed assigned metavariables pretty print with what they are delayed assigned to.
The delayed assigned metavariables themselves can be pretty printed using set_option pp.mvars.delayed true.


For more information, see the "Gruesome details" module docstrings in Lean.MetavarContext.


?ident
```

```
term ::= ...
    | 


A _synthetic hole_ (or _synthetic placeholder_), which stands for an unknown term that should be synthesized using tactics.




  * 
?_ creates a fresh metavariable with an auto-generated name.


  * 
?m either refers to a pre-existing metavariable named m or creates a fresh metavariable with that name.




In particular, the synthetic hole syntax creates "synthetic opaque metavariables",
the same kind of metavariable used to represent goals in the tactic state.


Synthetic holes are similar to holes in that _ also creates metavariables,
but synthetic opaque metavariables have some different properties:




  * In tactics such as refine, only synthetic holes yield new goals.


  * During elaboration, unification will not solve for synthetic opaque metavariables, they are "opaque".
This is to prevent counterintuitive behavior such as disappearing goals.


  * When synthetic holes appear under binders, they capture local variables using a more complicated mechanism known as delayed assignment.




## Delayed assigned metavariables


This section gives an overview of some technical details of synthetic holes, which you should feel free to skip.
Understanding delayed assignments is mainly useful for those who are working on tactics and other metaprogramming.
It is included here until there is a suitable place for it in the reference manual.


When a synthetic hole appears under a binding construct, such as for example fun (x : α) (y : β) => ?s,
the system creates a _delayed assignment_. This consists of




  1. A metavariable ?m of type (x : α) → (y : β) → γ x y whose local context is the local context outside the fun,
  where γ x y is the type of ?s. Recall that x and y appear in the local context of ?s.


  2. A delayed assignment record associating ?m to ?s and the variables #[x, y] in the local context of ?s





Then, this function elaborates as fun (x : α) (y : β) => ?m x y, where one should understand x and y here
as being De Bruijn indexes, since Lean uses the locally nameless encoding of lambda calculus.


Once ?s is fully solved for, in the sense that after metavariable instantiation it is a metavariable-free term e,
then we can make the assignment ?m := fun (x' : α) (y' : β) => e[x := x', y := y'].
(Implementation note: Lean only instantiates full applications ?m x' y' of delayed assigned metavariables, to skip forming this function.)
This delayed assignment mechanism is essential to the operation of basic tactics like intro,
and a good mental model is that it is a way to "apply" the metavariable ?s by substituting values in for some of its local variables.
While it would be easier to immediately assign ?s := ?m x y,
delayed assignment preserves ?s as an unsolved-for metavariable with a local context that still contains x and y,
which is exactly what tactics like intro need.


By default, delayed assigned metavariables pretty print with what they are delayed assigned to.
The delayed assigned metavariables themselves can be pretty printed using set_option pp.mvars.delayed true.


For more information, see the "Gruesome details" module docstrings in Lean.MetavarContext.


?_
```

[←13.8. Pattern Matching](Terms/Pattern-Matching/#pattern-matching "13.8. Pattern Matching")[13.10. Type Ascription→](Terms/Type-Ascription/#The-Lean-Language-Reference--Terms--Type-Ascription "13.10. Type Ascription")

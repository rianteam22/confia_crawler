[←4.1. Functions](The-Type-System/Functions/#functions "4.1. Functions")[4.3. Universes→](The-Type-System/Universes/#The-Lean-Language-Reference--The-Type-System--Universes "4.3. Universes")
#  4.2. Propositions[🔗](find/?domain=Verso.Genre.Manual.section&name=propositions "Permalink")
Propositions are meaningful statements that admit proof.  Nonsensical statements are not propositions, but false statements are. All propositions are classified by `Prop`.
Propositions have the following properties: 

Definitional proof irrelevance
    
Any two proofs of the same proposition are completely interchangeable. 

Run-time irrelevance
    
Propositions are erased from compiled code. 

Impredicativity
    
Propositions may quantify over types from any universe whatsoever. 

Restricted Elimination
    
With the exception of [subsingletons](The-Type-System/Inductive-Types/#--tech-term-subsingleton), propositions cannot be eliminated into non-proposition types. 

Extensionality 
    
Any two logically equivalent propositions can be proven to be equal with the `[propext](The-Type-System/Propositions/#propext "Documentation for propext")` axiom.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=propext "Permalink")axiom
```


propext {a b : Prop} : [(](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff")a [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") b[)](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") → a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b


propext {a b : Prop} : [(](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff")a [↔](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") b[)](Basic-Propositions/Logical-Connectives/#Iff___intro "Documentation for Iff") → a [=](Basic-Propositions/Propositional-Equality/#Eq___refl "Documentation for Eq") b


```

The [axiom](https://lean-lang.org/doc/reference/4.29.0-rc6/find/?domain=Verso.Genre.Manual.section&name=axioms) of **propositional extensionality**. It asserts that if propositions `a` and `b` are logically equivalent (that is, if `a` can be proved from `b` and vice versa), then `a` and `b` are _equal_ , meaning `a` can be replaced with `b` in all contexts.
The standard logical connectives provably respect propositional extensionality. However, an axiom is needed for higher order expressions like `P a` where `P : Prop → Prop` is unknown, as well as for equality. Propositional extensionality is intuitionistically valid.
[←4.1. Functions](The-Type-System/Functions/#functions "4.1. Functions")[4.3. Universes→](The-Type-System/Universes/#The-Lean-Language-Reference--The-Type-System--Universes "4.3. Universes")

[←15. The Simplifier](The-Simplifier/#the-simplifier "15. The Simplifier")[15.2. Rewrite Rules→](The-Simplifier/Rewrite-Rules/#simp-rewrites "15.2. Rewrite Rules")
#  15.1. Invoking the Simplifier[🔗](find/?domain=Verso.Genre.Manual.section&name=simp-tactic-naming "Permalink")
Lean's simplifier can be invoked in a variety of ways. The most common patterns are captured in a set of tactics. The [tactic reference](Tactic-Proofs/Tactic-Reference/#simp-tactics) contains a complete list of simplification tactics.
Simplification tactics all contain `simp` in their name. Aside from that, they are named according to a system of prefixes and suffixes that describe their functionality: 

`-!` suffix
    
Sets the `[autoUnfold](The-Simplifier/Configuring-Simplification/#Lean___Meta___Simp___Config___mk "Documentation for Lean.Meta.Simp.Config.autoUnfold")` configuration option to `true`, causing the simplifier to unfold all definitions 

`-?` suffix
    
Causes the simplifier to keep track of which rules it employed during simplification and suggest a minimal [simp set](The-Simplifier/Simp-sets/#--tech-term-simp-set) as an edit to the tactic script 

`-_arith` suffix
    
Enables the use of linear arithmetic simplification rules 

`d-` prefix
    
Causes the simplifier to simplify only with rewrites that hold definitionally 

`-_all` suffix
    
Causes the simplifier to repeatedly simplify all assumptions and the conclusion of the goal, taking as many hypotheses into account as possible, until no further simplification is possible
There are two further simplification tactics, `[simpa](Tactic-Proofs/Tactic-Reference/#simpa "Documentation for tactic")` and `[simpa!](Tactic-Proofs/Tactic-Reference/#simpa___ "Documentation for tactic")`, which are used to simultaneously simplify a goal and either a proof term or an assumption before discharging the goal. This simultaneous simplification makes proofs more robust to changes in the [simp set](The-Simplifier/Simp-sets/#--tech-term-simp-set).
##  15.1.1. Parameters[🔗](find/?domain=Verso.Genre.Manual.section&name=simp-tactic-params "Permalink")
The simplification tactics have the following grammar:
syntaxSimplification Tactics

```
tactic ::= ...
    | 


The simp tactic uses lemmas and hypotheses to simplify the main goal target or
non-dependent hypotheses. It has many variants:




  * 
simp simplifies the main goal target using lemmas tagged with the attribute [simp].


  * 
simp [h₁, h₂, ..., hₙ] simplifies the main goal target using the lemmas tagged
with the attribute [simp] and the given hᵢ's, where the hᵢ's are expressions.-


  * If an hᵢ is a defined constant f, then f is unfolded. If f has equational lemmas associated
with it (and is not a projection or a reducible definition), these are used to rewrite with f.


  * 
simp [*] simplifies the main goal target using the lemmas tagged with the
attribute [simp] and all hypotheses.


  * 
simp only [h₁, h₂, ..., hₙ] is like simp [h₁, h₂, ..., hₙ] but does not use [simp] lemmas.


  * 
simp [-id₁, ..., -idₙ] simplifies the main goal target using the lemmas tagged
with the attribute [simp], but removes the ones named idᵢ.


  * 
simp at h₁ h₂ ... hₙ simplifies the hypotheses h₁ : T₁ ... hₙ : Tₙ. If
the target or another hypothesis depends on hᵢ, a new simplified hypothesis
hᵢ is introduced, but the old one remains in the local context.


  * 
simp at * simplifies all the hypotheses and the target.


  * 
simp [*] at * simplifies target and all (propositional) hypotheses using the
other hypotheses.




simp [
Configuration options for tactics. 
optConfig](Tactic-Proofs/The-Tactic-Language/#Lean___Parser___Tactic___optConfig-next) only? ([ (


The simp lemma specification * means to rewrite with all hypotheses 


simpStar | 


An erasure specification -thm says to remove thm from the simp set 


simpErase | 


A simp lemma specification is:




  * optional ↑ or ↓ to specify use before or after entering the subterm


  * optional ← to use the lemma backward


  * 
thm for the theorem to rewrite with




simpLemma),* ] )? (


Location specifications are used by many tactics that can operate on either the
hypotheses or the goal. It can have one of the forms:




  * 'empty' is not actually present in this syntax, but most tactics use
(location)? matchers. It means to target the goal only.


  * 
at h₁ ... hₙ: target the hypotheses h₁, ..., hₙ



  * 
at h₁ h₂ ⊢: target the hypotheses h₁ and h₂, and the goal


  * 
at *: target all hypotheses and the goal




at 


A sequence of one or more locations at which a tactic should operate. These can include local
hypotheses and ⊢, which denotes the goal.


(term | 


The ⊢ location refers to the current goal. 


locationType)*)?
```

In other words, an invocation of a simplification tactic takes the following modifiers, in order, all of which are optional:
  * A set of [configuration options](Tactic-Proofs/The-Tactic-Language/#tactic-config), which should include the fields of `[Lean.Meta.Simp.Config](The-Simplifier/Configuring-Simplification/#Lean___Meta___Simp___Config___mk "Documentation for Lean.Meta.Simp.Config")` or `[Lean.Meta.DSimp.Config](The-Simplifier/Configuring-Simplification/#Lean___Meta___DSimp___Config___mk "Documentation for Lean.Meta.DSimp.Config")`, depending on whether the simplifier being invoked is a version of `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` or a version of `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")`.
  * The ``Lean.Parser.Tactic.simp : tactic`
The `simp` tactic uses lemmas and hypotheses to simplify the main goal target or non-dependent hypotheses. It has many variants:
    * `simp` simplifies the main goal target using lemmas tagged with the attribute `[simp]`.
    * `simp [h₁, h₂, ..., hₙ]` simplifies the main goal target using the lemmas tagged with the attribute `[simp]` and the given `hᵢ`'s, where the `hᵢ`'s are expressions.-
    * If an `hᵢ` is a defined constant `f`, then `f` is unfolded. If `f` has equational lemmas associated with it (and is not a projection or a `reducible` definition), these are used to rewrite with `f`.
    * `simp [*]` simplifies the main goal target using the lemmas tagged with the attribute `[simp]` and all hypotheses.
    * `simp only [h₁, h₂, ..., hₙ]` is like `simp [h₁, h₂, ..., hₙ]` but does not use `[simp]` lemmas.
    * `simp [-id₁, ..., -idₙ]` simplifies the main goal target using the lemmas tagged with the attribute `[simp]`, but removes the ones named `idᵢ`.
    * `simp at h₁ h₂ ... hₙ` simplifies the hypotheses `h₁ : T₁` ... `hₙ : Tₙ`. If the target or another hypothesis depends on `hᵢ`, a new simplified hypothesis `hᵢ` is introduced, but the old one remains in the local context.
    * `simp at *` simplifies all the hypotheses and the target.
    * `simp [*] at *` simplifies target and all (propositional) hypotheses using the other hypotheses.
`[`only`](Tactic-Proofs/Tactic-Reference/#simp) modifier excludes the default simp set, instead beginning with an emptyTechnically, the simp set always includes `eq_self` and `iff_self` in order to discharge reflexive cases. simp set.
  * The lemma list adds or removes lemmas from the simp set. There are three ways to specify lemmas in the lemma list:
    * `*`, which adds all assumptions in the proof state to the simp set
    * `-` followed by a lemma, which removes the lemma from the simp set
    * A lemma specifier, consisting of the following in sequence:
      * An optional `↓` or `↑`, which respectively cause the lemma to be applied before or after entering a subterm (`↑` is the default). The simplifier typically simplifies subterms before attempting to simplify parent terms, as simplified arguments often make more rules applicable; `↓` causes the parent term to be simplified with the rule prior to the simplification of subterms.
      * An optional `←`, which causes equational lemmas to be used from right to left rather than from left to right.
      * A mandatory lemma, which can be a simp set name, a lemma name, or a term. Terms are treated as if they were named lemmas with fresh names.
  * A location specifier, preceded by ``Lean.Parser.Tactic.simp : tactic`
The `simp` tactic uses lemmas and hypotheses to simplify the main goal target or non-dependent hypotheses. It has many variants:
    * `simp` simplifies the main goal target using lemmas tagged with the attribute `[simp]`.
    * `simp [h₁, h₂, ..., hₙ]` simplifies the main goal target using the lemmas tagged with the attribute `[simp]` and the given `hᵢ`'s, where the `hᵢ`'s are expressions.-
    * If an `hᵢ` is a defined constant `f`, then `f` is unfolded. If `f` has equational lemmas associated with it (and is not a projection or a `reducible` definition), these are used to rewrite with `f`.
    * `simp [*]` simplifies the main goal target using the lemmas tagged with the attribute `[simp]` and all hypotheses.
    * `simp only [h₁, h₂, ..., hₙ]` is like `simp [h₁, h₂, ..., hₙ]` but does not use `[simp]` lemmas.
    * `simp [-id₁, ..., -idₙ]` simplifies the main goal target using the lemmas tagged with the attribute `[simp]`, but removes the ones named `idᵢ`.
    * `simp at h₁ h₂ ... hₙ` simplifies the hypotheses `h₁ : T₁` ... `hₙ : Tₙ`. If the target or another hypothesis depends on `hᵢ`, a new simplified hypothesis `hᵢ` is introduced, but the old one remains in the local context.
    * `simp at *` simplifies all the hypotheses and the target.
    * `simp [*] at *` simplifies target and all (propositional) hypotheses using the other hypotheses.
`[`at`](Tactic-Proofs/Tactic-Reference/#simp), which consists of a sequence of locations. Locations may be:
    * The name of an assumption, indicating that its type should be simplified
    * An asterisk `*`, indicating that all assumptions and the conclusion should be simplified
    * A turnstile `⊢`, indicating that the conclusion should be simplified
By default, only the conclusion is simplified.

Location specifiers for `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`
In this proof state,
p:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Propx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 5 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")h':p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")3 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 9[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")⊢ p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")6 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")
the tactic `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") +[arith](The-Simplifier/Configuring-Simplification/#Lean___Meta___Simp___Config___mk "Documentation for Lean.Meta.Simp.Config.arith")p:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Propx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 5 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")h':p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")3 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 9[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")⊢ p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 7[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")` simplifies only the goal:
p:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Propx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 5 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 2[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")h':p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")3 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 9[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")⊢ p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 7[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")
Invoking `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") +[arith](The-Simplifier/Configuring-Simplification/#Lean___Meta___Simp___Config___mk "Documentation for Lean.Meta.Simp.Config.arith") at hp:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Propx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h':p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")3 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 9[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")h:p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 7[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")⊢ p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")6 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")` yields a goal in which the hypothesis `h` has been simplified:
p:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Propx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h':p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")3 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 9[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")h:p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 7[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")⊢ p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")6 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 1[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")
The conclusion can be additionally simplified by adding `⊢`, that is, `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") +[arith](The-Simplifier/Configuring-Simplification/#Lean___Meta___Simp___Config___mk "Documentation for Lean.Meta.Simp.Config.arith") at h ⊢p:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Propx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h':p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")3 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 9[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")h:p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 7[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")⊢ p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 7[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")`:
p:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Propx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h':p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")3 [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 9[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")h:p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 7[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")⊢ p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 7[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")
Using `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") +[arith](The-Simplifier/Configuring-Simplification/#Lean___Meta___Simp___Config___mk "Documentation for Lean.Meta.Simp.Config.arith") at *p:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Propx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 7[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")h':p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 12[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")⊢ p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 7[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")` simplifies all assumptions together with the conclusion:
p:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat") → Propx:[Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")h:p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 7[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")h':p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 12[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")⊢ p [(](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")x [+](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd") 7[)](Type-Classes/Basic-Classes/#HAdd___mk "Documentation for HAdd.hAdd")
[←15. The Simplifier](The-Simplifier/#the-simplifier "15. The Simplifier")[15.2. Rewrite Rules→](The-Simplifier/Rewrite-Rules/#simp-rewrites "15.2. Rewrite Rules")

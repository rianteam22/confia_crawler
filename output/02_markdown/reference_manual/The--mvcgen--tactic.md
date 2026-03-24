[←16.12. Bigger Examples](The--grind--tactic/Bigger-Examples/#grind-bigger-examples "16.12. Bigger Examples")[17.1. Overview→](The--mvcgen--tactic/Overview/#The-Lean-Language-Reference--The--mvcgen--tactic--Overview "17.1. Overview")
#  17. The `mvcgen` tactic[🔗](find/?domain=Verso.Genre.Manual.section&name=mvcgen-tactic "Permalink")
#  Tutorials
  * [Verifying Imperative Programs Using `mvcgen`](/doc/tutorials/4.29.0-rc6/mvcgen/#mvcgen-tactic-tutorial)


The `[mvcgen](Tactic-Proofs/Tactic-Reference/#mvcgen "Documentation for tactic")` tactic implements a _monadic verification condition generator_ : It breaks down a goal involving a program written using Lean's imperative ``Lean.Parser.Term.do : term``[`do`](Functors___-Monads-and--do--Notation/Syntax/#Lean___Parser___Term___do) notation into a number of smaller [_verification conditions_](The--mvcgen--tactic/Overview/#--tech-term-verification-conditions) (VCs) that are sufficient to prove the goal. In addition to a reference that describes the use of `[mvcgen](Tactic-Proofs/Tactic-Reference/#mvcgen "Documentation for tactic")`, this chapter includes a [tutorial](/doc/tutorials/4.29.0-rc6/mvcgen/#mvcgen-tactic-tutorial) that can be read independently of the reference.
In order to use the `[mvcgen](Tactic-Proofs/Tactic-Reference/#mvcgen "Documentation for tactic")` tactic, `Std.Tactic.Do` must be imported and the namespace `Std.Do` must be opened.
  1. [17.1. Overview](The--mvcgen--tactic/Overview/#The-Lean-Language-Reference--The--mvcgen--tactic--Overview)
  2. [17.2. Predicate Transformers](The--mvcgen--tactic/Predicate-Transformers/#The-Lean-Language-Reference--The--mvcgen--tactic--Predicate-Transformers)
  3. [17.3. Verification Conditions](The--mvcgen--tactic/Verification-Conditions/#The-Lean-Language-Reference--The--mvcgen--tactic--Verification-Conditions)
  4. [17.4. Enabling `mvcgen` For Monads](The--mvcgen--tactic/Enabling--mvcgen--For-Monads/#The-Lean-Language-Reference--The--mvcgen--tactic--Enabling--mvcgen--For-Monads)
  5. [17.5. Proof Mode](The--mvcgen--tactic/Proof-Mode/#mvcgen-proof-mode)

[←16.12. Bigger Examples](The--grind--tactic/Bigger-Examples/#grind-bigger-examples "16.12. Bigger Examples")[17.1. Overview→](The--mvcgen--tactic/Overview/#The-Lean-Language-Reference--The--mvcgen--tactic--Overview "17.1. Overview")

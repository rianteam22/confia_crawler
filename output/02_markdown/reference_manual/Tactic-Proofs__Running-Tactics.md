[←14. Tactic Proofs](Tactic-Proofs/#tactics "14. Tactic Proofs")[14.2. Reading Proof States→](Tactic-Proofs/Reading-Proof-States/#proof-states "14.2. Reading Proof States")
#  14.1. Running Tactics[🔗](find/?domain=Verso.Genre.Manual.section&name=by "Permalink")
syntaxTactic Proofs with `by`
Tactics are included in terms using ``Lean.Parser.Term.byTactic : term`
`by tac` constructs a term of the expected type by running the tactic(s) `tac`. 
``by`, which is followed by a sequence of tactics in which each has the same indentation:

```
term ::= ...
    | 


by tac constructs a term of the expected type by running the tactic(s) tac. 


by
      


A sequence of tactics in brackets, or a delimiter-free indented sequence of tactics.
Delimiter-free indentation is determined by the _first_ tactic of the sequence. 


tacticSeq
```

Alternatively, explicit braces and semicolons may be used:

```
term ::= ...
    | 


by tac constructs a term of the expected type by running the tactic(s) tac. 


by 


A sequence of tactics in brackets, or a delimiter-free indented sequence of tactics.
Delimiter-free indentation is determined by the _first_ tactic of the sequence. 




The syntax { tacs } is an alternative syntax for · tacs.
It runs the tactics in sequence, and fails if the goal is not solved. 


{ tactic* }
```

Tactics are invoked using the ``Lean.Parser.Term.byTactic : term`
`by tac` constructs a term of the expected type by running the tactic(s) `tac`. 
``by` term. When the elaborator encounters ``Lean.Parser.Term.byTactic : term`
`by tac` constructs a term of the expected type by running the tactic(s) `tac`. 
``by`, it invokes the tactic interpreter to construct the resulting term. Tactic proofs may be embedded via ``Lean.Parser.Term.byTactic : term`
`by tac` constructs a term of the expected type by running the tactic(s) `tac`. 
``by` in any context in which a term can occur.
[←14. Tactic Proofs](Tactic-Proofs/#tactics "14. Tactic Proofs")[14.2. Reading Proof States→](Tactic-Proofs/Reading-Proof-States/#proof-states "14.2. Reading Proof States")

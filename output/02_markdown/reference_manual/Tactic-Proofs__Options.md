[←14.3. The Tactic Language](Tactic-Proofs/The-Tactic-Language/#tactic-language "14.3. The Tactic Language")[14.5. Tactic Reference→](Tactic-Proofs/Tactic-Reference/#tactic-ref "14.5. Tactic Reference")
#  14.4. Options[🔗](find/?domain=Verso.Genre.Manual.section&name=tactic-language-options "Permalink")
These options affect the meaning of tactics.
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=tactic.customEliminators "Permalink")option
```
tactic.customEliminators
```

Default value: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
enable using custom eliminators in the 'induction' and 'cases' tactics defined using the '@[induction_eliminator]' and '@[cases_eliminator]' attributes
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=tactic.skipAssignedInstances "Permalink")option
```
tactic.skipAssignedInstances
```

Default value: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
in the `[rw](Tactic-Proofs/Tactic-Reference/#rw "Documentation for tactic")` and `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` tactics, if an instance implicit argument is assigned, do not try to synthesize instance.
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=tactic.simp.trace "Permalink")option
```
tactic.simp.trace
```

Default value: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
When tracing is enabled, calls to `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` or `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")` will print an equivalent `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") only` call.
[←14.3. The Tactic Language](Tactic-Proofs/The-Tactic-Language/#tactic-language "14.3. The Tactic Language")[14.5. Tactic Reference→](Tactic-Proofs/Tactic-Reference/#tactic-ref "14.5. Tactic Reference")

[←15.5. Terminal vs Non-Terminal Positions](The-Simplifier/Terminal-vs-Non-Terminal-Positions/#terminal-simp "15.5. Terminal vs Non-Terminal Positions")[15.7. Simplification vs Rewriting→](The-Simplifier/Simplification-vs-Rewriting/#simp-vs-rw "15.7. Simplification vs Rewriting")
#  15.6. Configuring Simplification[🔗](find/?domain=Verso.Genre.Manual.section&name=simp-config "Permalink")
`[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` is primarily configured via a configuration parameter, passed as a named argument called `config`.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Meta.Simp.Config.dsimp "Permalink")structure
```


Lean.Meta.Simp.Config : Type


Lean.Meta.Simp.Config : Type


```

The configuration for `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`. Passed to `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` using, for example, the `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") +contextual` or `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") (maxSteps := 100000)` syntax.
See also `[Lean.Meta.Simp.neutralConfig](The-Simplifier/Configuring-Simplification/#Lean___Meta___Simp___neutralConfig "Documentation for Lean.Meta.Simp.neutralConfig")` and `[Lean.Meta.DSimp.Config](The-Simplifier/Configuring-Simplification/#Lean___Meta___DSimp___Config___mk "Documentation for Lean.Meta.DSimp.Config")`.
#  Constructor

```
[Lean.Meta.Simp.Config.mk](The-Simplifier/Configuring-Simplification/#Lean___Meta___Simp___Config___mk "Documentation for Lean.Meta.Simp.Config.mk")
```

#  Fields

```
maxSteps : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

The maximum number of subexpressions to visit when performing simplification. The default is 100000.

```
maxDischargeDepth : [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

When simp discharges side conditions for conditional lemmas, it can recursively apply simplification. The `maxDischargeDepth` (default: 2) is the maximum recursion depth when recursively applying simplification to side conditions.

```
contextual : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `contextual` is true (default: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`) and simplification encounters an implication `p → q` it includes `p` as an additional simp lemma when simplifying `q`.

```
memoize : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When true (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`) then the simplifier caches the result of simplifying each sub-expression, if possible.

```
singlePass : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `singlePass` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`), the simplifier runs through a single round of simplification, which consists of running pre-methods, recursing using congruence lemmas, and then running post-methods. Otherwise, when it is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, it iteratively applies this simplification procedure.

```
zeta : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), performs zeta reduction of `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` and `have` expressions. That is, `let x := v; e[x]` reduces to `e[v]`. If `zetaHave` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` then `have` expressions are not zeta reduced. See also `zetaDelta`.

```
beta : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), performs beta reduction of applications of `fun` expressions. That is, `(fun x => e[x]) v` reduces to `e[v]`.

```
eta : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

TODO (currently unimplemented). When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), performs eta reduction for `fun` expressions. That is, `(fun x => f x)` reduces to `f`.

```
etaStruct : Lean.Meta.EtaStructMode
```

Configures how to determine definitional equality between two structure instances. See documentation for `Lean.Meta.EtaStructMode`.

```
iota : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), reduces `[match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic")` expressions applied to constructors.

```
proj : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), reduces projections of structure constructors.

```
decide : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`), rewrites a proposition `p` to `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")` or `[False](Basic-Propositions/Truth/#False "Documentation for False")` by inferring a `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") p` instance and reducing it.

```
arith : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`), simplifies simple arithmetic expressions.

```
autoUnfold : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`), unfolds applications of functions defined by pattern matching, when one of the patterns applies. This can be enabled using the `[simp!](Tactic-Proofs/Tactic-Reference/#simp___ "Documentation for tactic")` syntax.

```
dsimp : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`) then switches to `dsimp` on dependent arguments if there is no congruence theorem that would allow `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` to visit them. When `dsimp` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, then the argument is not visited.

```
failIfUnchanged : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

If `failIfUnchanged` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), then calls to `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`, `dsimp`, or `[simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic")` will fail if they do not make progress.

```
ground : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

If `ground` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`), then ground terms are reduced. A term is ground when it does not contain free or meta variables. Reduction is interrupted at a function application `f ...` if `f` is marked to not be unfolded. Ground term reduction applies `@[seval]` lemmas.

```
unfoldPartialApp : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

If `unfoldPartialApp` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`), then calls to `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`, `dsimp`, or `[simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic")` will unfold even partial applications of `f` when we request `f` to be unfolded.

```
zetaDelta : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`), local definitions are unfolded. That is, given a local context containing `x : t := e`, then the free variable `x` reduces to `e`. Otherwise, `x` must be provided as a `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` argument.

```
index : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `index` (default : `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`) is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` will only use the root symbol to find candidate `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` theorems. It approximates Lean 3 `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` behavior.

```
implicitDefEqProofs : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

If `implicitDefEqProofs := true`, `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` does not create proof terms when the input and output terms are definitionally equal.

```
zetaUnused : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default : `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), then `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` removes unused `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` and `have` expressions: `let x := v; e` simplifies to `e` when `x` does not occur in `e`. This option takes precedence over `zeta` and `zetaHave`.

```
catchRuntime : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default : `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), then `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` catches runtime exceptions and converts them into `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` exceptions.

```
zetaHave : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), then disables zeta reduction of `have` expressions. If `zeta` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, then this option has no effect. Unused `have`s are still removed if `zeta` or `zetaUnused` are true.

```
letToHave : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default : `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), then `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` will attempt to transform `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")`s into `have`s if they are non-dependent. This only applies when `zeta := false`.

```
congrConsts : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` tries to realize constant `f.congr_simp` when constructing an auxiliary congruence proof for `f`. This option exists because the termination prover uses `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` and `withoutModifyingEnv` while constructing the termination proof. Thus, any constant realized by `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` is deleted.

```
bitVecOfNat : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), the bitvector simprocs use `[BitVec.ofNat](Basic-Types/Bitvectors/#BitVec___ofNat "Documentation for BitVec.ofNat")` for representing bitvector literals.

```
warnExponents : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), the `^` simprocs generate an warning it the exponents are too big.

```
suggestions : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

If `suggestions` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, `[simp?](Tactic-Proofs/Tactic-Reference/#simp___-next "Documentation for tactic")` will invoke the currently configured library suggestion engine on the current goal, and attempt to use the resulting suggestions as parameters to the `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` tactic.

```
maxSuggestions : [Option](Basic-Types/Optional-Values/#Option___none "Documentation for Option") [Nat](Basic-Types/Natural-Numbers/#Nat___zero "Documentation for Nat")
```

Maximum number of library suggestions to use. If `[none](Basic-Types/Optional-Values/#Option___none "Documentation for Option.none")`, uses the default limit. Only relevant when `suggestions` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`.

```
locals : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

If `locals` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` will unfold all definitions from the current file. For local theorems, use `+suggestions` instead.

```
instances : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

If `instances` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` will visit instance arguments. If option `backward.dsimp.instances` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, it overrides this field.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Meta.Simp.neutralConfig "Permalink")def
```


Lean.Meta.Simp.neutralConfig : [Lean.Meta.Simp.Config](The-Simplifier/Configuring-Simplification/#Lean___Meta___Simp___Config___mk "Documentation for Lean.Meta.Simp.Config")


Lean.Meta.Simp.neutralConfig :
  [Lean.Meta.Simp.Config](The-Simplifier/Configuring-Simplification/#Lean___Meta___Simp___Config___mk "Documentation for Lean.Meta.Simp.Config")


```

A neutral configuration for `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`, turning off all reductions and other built-in simplifications.
[🔗](find/?domain=Verso.Genre.Manual.doc&name=Lean.Meta.DSimp.Config.instances "Permalink")structure
```


Lean.Meta.DSimp.Config : Type


Lean.Meta.DSimp.Config : Type


```

The configuration for `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")`. Passed to `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")` using, for example, the `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic") (config := {zeta := false})` syntax.
Implementation note: this structure is only used for processing the `(config := ...)` syntax, and it is not used internally. It is immediately converted to `[Lean.Meta.Simp.Config](The-Simplifier/Configuring-Simplification/#Lean___Meta___Simp___Config___mk "Documentation for Lean.Meta.Simp.Config")` by `Lean.Elab.Tactic.elabSimpConfig`.
#  Constructor

```
[Lean.Meta.DSimp.Config.mk](The-Simplifier/Configuring-Simplification/#Lean___Meta___DSimp___Config___mk "Documentation for Lean.Meta.DSimp.Config.mk")
```

#  Fields

```
zeta : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), performs zeta reduction of `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` and `have` expressions. That is, `let x := v; e[x]` reduces to `e[v]`. If `zetaHave` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` then `have` expressions are not zeta reduced. See also `zetaDelta`.

```
beta : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), performs beta reduction of applications of `fun` expressions. That is, `(fun x => e[x]) v` reduces to `e[v]`.

```
eta : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

TODO (currently unimplemented). When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), performs eta reduction for `fun` expressions. That is, `(fun x => f x)` reduces to `f`.

```
etaStruct : Lean.Meta.EtaStructMode
```

Configures how to determine definitional equality between two structure instances. See documentation for `Lean.Meta.EtaStructMode`.

```
iota : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), reduces `[match](Tactic-Proofs/The-Tactic-Language/#match "Documentation for tactic")` expressions applied to constructors.

```
proj : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), reduces projections of structure constructors.

```
decide : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`), rewrites a proposition `p` to `[True](Basic-Propositions/Truth/#True___intro "Documentation for True")` or `[False](Basic-Propositions/Truth/#False "Documentation for False")` by inferring a `[Decidable](Type-Classes/Basic-Classes/#Decidable___isFalse "Documentation for Decidable") p` instance and reducing it.

```
autoUnfold : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`), unfolds applications of functions defined by pattern matching, when one of the patterns applies. This can be enabled using the `[simp!](Tactic-Proofs/Tactic-Reference/#simp___ "Documentation for tactic")` syntax.

```
failIfUnchanged : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

If `failIfUnchanged` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), then calls to `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`, `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")`, or `[simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic")` will fail if they do not make progress.

```
unfoldPartialApp : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

If `unfoldPartialApp` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`), then calls to `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`, `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")`, or `[simp_all](Tactic-Proofs/Tactic-Reference/#simp_all "Documentation for tactic")` will unfold even partial applications of `f` when we request `f` to be unfolded.

```
zetaDelta : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`), local definitions are unfolded. That is, given a local context containing `x : t := e`, then the free variable `x` reduces to `e`. Otherwise, `x` must be provided as a `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` argument.

```
index : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `index` (default : `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`) is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` will only use the root symbol to find candidate `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` theorems. It approximates Lean 3 `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` behavior.

```
zetaUnused : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")` (default : `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), then `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` will remove unused `[let](Tactic-Proofs/The-Tactic-Language/#let "Documentation for tactic")` and `have` expressions: `let x := v; e` simplifies to `e` when `x` does not occur in `e`.

```
zetaHave : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

When `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")` (default: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`), then disables zeta reduction of `have` expressions. If `zeta` is `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`, then this option has no effect. Unused `have`s are still removed if `zeta` or `zetaUnused` are true.

```
locals : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

If `locals` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")` will unfold all definitions from the current file. For local theorems, use `+suggestions` instead.

```
instances : [Bool](Basic-Types/Booleans/#Bool___false "Documentation for Bool")
```

If `instances` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")` will visit instance arguments. If option `backward.dsimp.instances` is `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`, it overrides this field.
##  15.6.1. Options[🔗](find/?domain=Verso.Genre.Manual.section&name=simp-options "Permalink")
Some global options affect `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")`:
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=simprocs "Permalink")option
```
simprocs
```

Default value: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
Enable/disable `simproc`s (simplification procedures).
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=tactic.simp.trace "Permalink")option
```
tactic.simp.trace
```

Default value: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
When tracing is enabled, calls to `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic")` or `[dsimp](Tactic-Proofs/Tactic-Reference/#dsimp "Documentation for tactic")` will print an equivalent `[simp](Tactic-Proofs/Tactic-Reference/#simp "Documentation for tactic") only` call.
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=linter.unnecessarySimpa "Permalink")option
```
linter.unnecessarySimpa
```

Default value: `[true](Basic-Types/Booleans/#Bool___false "Documentation for Bool.true")`
enable the 'unnecessary simpa' linter
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=trace.Meta.Tactic.simp.rewrite "Permalink")option
```
trace.Meta.Tactic.simp.rewrite
```

Default value: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
enable/disable tracing for the given module and submodules
[🔗](find/?domain=Verso.Genre.Manual.doc.option&name=trace.Meta.Tactic.simp.discharge "Permalink")option
```
trace.Meta.Tactic.simp.discharge
```

Default value: `[false](Basic-Types/Booleans/#Bool___false "Documentation for Bool.false")`
enable/disable tracing for the given module and submodules
[←15.5. Terminal vs Non-Terminal Positions](The-Simplifier/Terminal-vs-Non-Terminal-Positions/#terminal-simp "15.5. Terminal vs Non-Terminal Positions")[15.7. Simplification vs Rewriting→](The-Simplifier/Simplification-vs-Rewriting/#simp-vs-rw "15.7. Simplification vs Rewriting")

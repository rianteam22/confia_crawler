[←24.2. Managing Toolchains with Elan](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#elan "24.2. Managing Toolchains with Elan")[Error Explanations→](Error-Explanations/#The-Lean-Language-Reference--Error-Explanations "Error Explanations")
#  Validating a Lean Proof[🔗](find/?domain=Verso.Genre.Manual.section&name=validating-proofs "Permalink")
This section discusses how to validate a proof expressed in Lean.
Depending on the circumstances, additional steps may be recommended to rule out misleading proofs. In particular, it matters a lot whether one is dealing with an [honest](ValidatingProofs/#--tech-term-honest) proof attempt, and needs protection against only benign mistakes, or a possibly-[malicious](ValidatingProofs/#--tech-term-malicious) proof attempt that actively tries to mislead.
In particular, we use _honest_ when the goal is to create a valid proof. This allows for mistakes and bugs in proofs and meta-code (tactics, attributes, commands, etc.), but not for code that clearly only serves to circumvent the system (such as using the `debug.skipKernelTC`). Note that the `unsafe` marker on API functions is unrelated to whether this API can be used in an dishonest way.
In contrast, we use _malicious_ to describe code to go out of its way to trick or mislead the user, exploit bugs or compromise the system. This includes un-reviewed AI-generated proofs and programs.
Furthermore it is important to distinguish the question “does the theorem have a valid proof” from “what does the theorem statement mean”.
Below, an escalating sequence of checks are presented, with instructions on how to perform them, an explanation of what they entail and the mistakes or attacks they guard against.
##  The Blue Double Check Marks[🔗](find/?domain=Verso.Genre.Manual.section&name=validating-blue-check-marks "Permalink")
In regular everyday use of Lean, it suffices to check the blue double check marks next to the theorem statement for assurance that the theorem is proved.
###  Instructions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--The-Blue-Double-Check-Marks--Instructions "Permalink")
While working interactively with Lean, once the theorem is proved, blue double check marks appear in the gutter to the left of the code.
A double blue check mark
###  Significance[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--The-Blue-Double-Check-Marks--Significance "Permalink")
The blue ticks indicate that the theorem statement has been successfully elaborated, according to the syntax and type class instances defined in the current file and its imports, and that the Lean kernel has accepted a proof of that theorem statement that follows from the definitions, theorems and axioms declared in the current file and its imports.
###  Trust[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--The-Blue-Double-Check-Marks--Trust "Permalink")
This check is meaningful if one believes the formal theorem statement corresponds to its intended informal meanings and trusts the authors of the imported libraries to be [honest](ValidatingProofs/#--tech-term-honest), that they performed this check, and that no unsound axioms have been declared and used.
###  Protection[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--The-Blue-Double-Check-Marks--Protection "Permalink")
This check protects against
  * Incomplete proof (missing goals, tactic error) **of the current theorem**
  * Explicit use of `sorry` **in the current theorem**
  * [Honest](ValidatingProofs/#--tech-term-honest) bugs in meta-programs and tactics
  * Proofs still being checked in the background


###  Comments[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--The-Blue-Double-Check-Marks--Comments "Permalink")
In the Visual Studio Code extension settings, the symbol can be changed. Editors other than VS Code may have a different indication.
Running [`lake build`](Build-Tools-and-Distribution/Lake/#build)` +Module`, where `Module` refers to the file containing the theorem, and observing success without error messages or warnings provides the same guarantees.
##  Printing Axioms[🔗](find/?domain=Verso.Genre.Manual.section&name=validating-printing-axioms "Permalink")
The blue double check marks appear even when there are explicit uses of `sorry` or incomplete proofs in the dependencies of the theorem. Because both `sorry` and incomplete proofs are elaborated to axioms, their presence can be detected by listing the axioms that a proof relies on.
###  Instructions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--Printing-Axioms--Instructions "Permalink")
Write ``'thmName' does not depend on any axioms`[#print](Interacting-with-Lean/#Lean___Parser___Command___printAxioms "Documentation for syntax") [axioms](Interacting-with-Lean/#Lean___Parser___Command___printAxioms "Documentation for syntax") thmName` after the theorem declaration, with `thmName` replaced by the name of the theorem and check that it reports only the built-in axioms `[propext](The-Type-System/Propositions/#propext "Documentation for propext")`, `Classical.choice`, and `[Quot.sound](The-Type-System/Quotients/#Quot___sound "Documentation for Quot.sound")`.
###  Significance[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--Printing-Axioms--Significance "Permalink")
This command prints the set of axioms used by the theorem and the theorems it depends on. The three axioms above are standard axioms of Lean's logic, and benign.
  * If `sorryAx` is reported, then this theorem or one of its dependencies uses `sorry` or is otherwise incomplete.
  * If `Lean.trustCompiler` is reported, then native evaluation is used; see below for a discussion.
  * Any other axiom means that a custom axiom was declared and used, and the theorem is only valid relative to the soundness of these axioms.


###  Trust[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--Printing-Axioms--Trust "Permalink")
This check is meaningful if one believes the formal theorem statement corresponds to its intended informal meanings and one trusts the authors of the imported libraries to be [honest](ValidatingProofs/#--tech-term-honest).
###  Protection[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--Printing-Axioms--Protection "Permalink")
(In addition to the list above)
  * Incomplete proofs
  * Explicit use of `sorry`
  * Custom axioms


###  Comments[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--Printing-Axioms--Comments "Permalink")
At the time of writing, the ``Lean.Parser.Command.printAxioms : command``[`#print axioms`](Interacting-with-Lean/#Lean___Parser___Command___printAxioms) command does not work in a [module](Source-Files-and-Modules/#--tech-term-module). To work around this, create a non-module file, import your module, and use ``Lean.Parser.Command.printAxioms : command``[`#print axioms`](Interacting-with-Lean/#Lean___Parser___Command___printAxioms) there.
##  Re-Checking Proofs with `lean4checker`[🔗](find/?domain=Verso.Genre.Manual.section&name=validating-lean4checker "Permalink")
There is a small class of bugs and some dishonest ways of presenting proofs that can be caught by re-checking the proofs that are stored in [`.olean` files](Elaboration-and-Compilation/#--tech-term-___olean-file) when building the project.
###  Instructions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--Re-Checking-Proofs-with--lean4checker--Instructions "Permalink")
Build your project using [`lake build`](Build-Tools-and-Distribution/Lake/#build), run `lean4checker --fresh` on the module that contains the theorem of interest, and check that no error is reported.
###  Significance[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--Re-Checking-Proofs-with--lean4checker--Significance "Permalink")
The `lean4checker` tool reads the declarations and proofs as they are stored by `lean` during building (the [`.olean` files](Elaboration-and-Compilation/#--tech-term-___olean-file)), and replays them through the kernel. It trusts that the [`.olean` files](Elaboration-and-Compilation/#--tech-term-___olean-file) are structurally correct.
###  Trust[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--Re-Checking-Proofs-with--lean4checker--Trust "Permalink")
This check is meaningful if one believes the formal theorem statement corresponds to its intended informal meanings and believes the authors of the imported libraries to not be very cunningly [malicious](ValidatingProofs/#--tech-term-malicious), and to neither compromise the user’s system nor use Lean’s extensibility to change the interpretation of the theorem statement.
###  Protection[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--Re-Checking-Proofs-with--lean4checker--Protection "Permalink")
(In addition to the list above)
  * Bugs in Lean’s core handling of the kernel’s state (e.g. due to parallel proof processing, or import handling)
  * Meta-programs or tactics intentionally bypassing that state (e.g. using low-level functionality to add unchecked theorems)


###  Comments[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--Re-Checking-Proofs-with--lean4checker--Comments "Permalink")
Since `lean4checker` reads the [`.olean` files](Elaboration-and-Compilation/#--tech-term-___olean-file) without validating their format, this check is prone to an attacker crafting invalid `.olean` files (e.g. invalid pointers, invalid data in strings).
Lean tactics and other meta-code can perform arbitrary actions when run. Importing libraries created by a determined [malicious](ValidatingProofs/#--tech-term-malicious) attacker and building them without further protection can compromise the user's system, after which no further meaningful checks are possible.
We recommend running `lean4checker` as part of CI for the additional protection against bugs in Lean's handling of declaration and as a deterrent against simple attacks. The [lean-action](https://github.com/leanprover/lean-action) GitHub Action provides this functionality by setting `lean4checker: true`.
Without the `--fresh` flag the tool can be instructed to only check some modules, and assume others to be correct (e.g. trusted libraries), for faster processing.
##  Gold Standard: `comparator`[🔗](find/?domain=Verso.Genre.Manual.section&name=validating-comparator "Permalink")
To protect against a seriously [malicious](ValidatingProofs/#--tech-term-malicious) proof compromising how Lean interprets a theorem statement or the user's system, additional steps are necessary. This should only be necessary for high risk scenarios (proof marketplaces, high-reward proof competitions).
###  Instructions[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--Gold-Standard___--comparator--Instructions "Permalink")
In a trusted environment, write the theorem **statement** (the ”challenge”), and then feed the challenge as well as the proposed proof to the [`comparator`](https://github.com/leanprover/comparator) tool, as documented there.
###  Significance[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--Gold-Standard___--comparator--Significance "Permalink")
Comparator will build the proof in a sandboxed environment, to protect against [malicious](ValidatingProofs/#--tech-term-malicious) code in the build step. The proof term is exported to a serialized format. Outside the sandbox and out of the reach of possibly malicious code, it validates the exported format, loads the proofs, replays them using Lean's kernel, and checks that the proved theorem statement matches the one in the challenge file.
###  Trust[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--Gold-Standard___--comparator--Trust "Permalink")
This check is meaningful if the theorem statement in the trusted challenge file is correct and the sandbox used to build the possibly-[malicious](ValidatingProofs/#--tech-term-malicious) code is safe.
###  Protection[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--Gold-Standard___--comparator--Protection "Permalink")
(In addition to the list above)
  * Actively [malicious](ValidatingProofs/#--tech-term-malicious) proofs


###  Comments[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--Gold-Standard___--comparator--Comments "Permalink")
At the time of writing, `comparator` uses only the official Lean kernel. In the future it will be easy to use multiple, independent kernel implementations; then this will also protect against implementation bugs in the official Lean kernel.
##  Remaining Issues[🔗](find/?domain=Verso.Genre.Manual.section&name=The-Lean-Language-Reference--Validating-a-Lean-Proof--Remaining-Issues "Permalink")
When following the gold standard of checking proofs using comparator, some assumptions remain:
  * The soundness of Lean’s logic.
  * The implementation of that logic in Lean’s kernel (for now; see comment above).
  * The plumbing provided by the `comparator` tool.
  * The safety of the sandbox used by `comparator`
  * No human error or misleading presentation of the theorem statement in the trusted challenge file.


##  On `Lean.trustCompiler`[🔗](find/?domain=Verso.Genre.Manual.section&name=validating-trustCompiler "Permalink")
Lean supports proofs by native evaluation. This is used by the `[decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")```Lean.Parser.Tactic.decide : tactic`
`decide` attempts to prove the main goal (with target type `p`) by synthesizing an instance of `Decidable p` and then reducing that instance to evaluate the truth value of `p`. If it reduces to `isTrue h`, then `h` is a proof of `p` that closes the goal.
The target is not allowed to contain local variables or metavariables. If there are local variables, you can first try using the `revert` tactic with these local variables to move them into the target, or you can use the `+revert` option, described below.
Options:
  * `decide +revert` begins by reverting local variables that the target depends on, after cleaning up the local context of irrelevant variables. A variable is _relevant_ if it appears in the target, if it appears in a relevant variable, or if it is a proposition that refers to a relevant variable.
  * `decide +kernel` uses kernel for reduction instead of the elaborator. It has two key properties: (1) since it uses the kernel, it ignores transparency and can unfold everything, and (2) it reduces the `Decidable` instance only once instead of twice.
  * `decide +native` uses the native code compiler (`#eval`) to evaluate the `Decidable` instance, admitting the result via an axiom. This can be significantly more efficient than using reduction, but it is at the cost of increasing the size This can be significantly more efficient than using reduction, but it is at the cost of increasing the size of the trusted code base. Namely, it depends on the correctness of the Lean compiler and all definitions with an `@[implemented_by]` attribute. Like with `+kernel`, the `Decidable` instance is evaluated only once.


Limitation: In the default mode or `+kernel` mode, since `decide` uses reduction to evaluate the term, `Decidable` instances defined by well-founded recursion might not work because evaluating them requires reducing proofs. Reduction can also get stuck on `Decidable` instances with `Eq.rec` terms. These can appear in instances defined using tactics (such as `rw` and `simp`). To avoid this, create such instances using definitions such as `decidable_of_iff` instead.
## Examples
Proving inequalities:

```
example : 2 + 2 ≠ 5 := by decide

```

Trying to prove a false proposition:

```
example : 1 ≠ 1 := by decide
/-
tactic 'decide' proved that the proposition
  1 ≠ 1
is false
-/

```

Trying to prove a proposition whose `Decidable` instance fails to reduce

```
opaque unknownProp : Prop

open scoped Classical in
example : unknownProp := by decide
/-
tactic 'decide' failed for proposition
  unknownProp
since its 'Decidable' instance reduced to
  Classical.choice ⋯
rather than to the 'isTrue' constructor.
-/

```

## Properties and relations
For equality goals for types with decidable equality, usually `rfl` can be used in place of `decide`.

```
example : 1 + 1 = 2 := by decide
example : 1 + 1 = 2 := by rfl

```

`[` +native`](Tactic-Proofs/Tactic-Reference/#decide) tactic or internally by specific tactics (`[bv_decide](Tactic-Proofs/Tactic-Reference/#bv_decide "Documentation for tactic")` in particular) and produces proof terms that call compiled Lean code to do a calculation that is then trusted by the kernel.
Specific uses wrapped in [honest](ValidatingProofs/#--tech-term-honest) tactics (e.g. `[bv_decide](Tactic-Proofs/Tactic-Reference/#bv_decide "Documentation for tactic")`) are generally trustworthy. The trusted code base is larger (it includes Lean's compilation toolchain and library annotations in the standard library), but still fixed and vetted.
General use (`[decide](Tactic-Proofs/Tactic-Reference/#decide "Documentation for tactic")```Lean.Parser.Tactic.decide : tactic`
`decide` attempts to prove the main goal (with target type `p`) by synthesizing an instance of `Decidable p` and then reducing that instance to evaluate the truth value of `p`. If it reduces to `isTrue h`, then `h` is a proof of `p` that closes the goal.
The target is not allowed to contain local variables or metavariables. If there are local variables, you can first try using the `revert` tactic with these local variables to move them into the target, or you can use the `+revert` option, described below.
Options:
  * `decide +revert` begins by reverting local variables that the target depends on, after cleaning up the local context of irrelevant variables. A variable is _relevant_ if it appears in the target, if it appears in a relevant variable, or if it is a proposition that refers to a relevant variable.
  * `decide +kernel` uses kernel for reduction instead of the elaborator. It has two key properties: (1) since it uses the kernel, it ignores transparency and can unfold everything, and (2) it reduces the `Decidable` instance only once instead of twice.
  * `decide +native` uses the native code compiler (`#eval`) to evaluate the `Decidable` instance, admitting the result via an axiom. This can be significantly more efficient than using reduction, but it is at the cost of increasing the size This can be significantly more efficient than using reduction, but it is at the cost of increasing the size of the trusted code base. Namely, it depends on the correctness of the Lean compiler and all definitions with an `@[implemented_by]` attribute. Like with `+kernel`, the `Decidable` instance is evaluated only once.


Limitation: In the default mode or `+kernel` mode, since `decide` uses reduction to evaluate the term, `Decidable` instances defined by well-founded recursion might not work because evaluating them requires reducing proofs. Reduction can also get stuck on `Decidable` instances with `Eq.rec` terms. These can appear in instances defined using tactics (such as `rw` and `simp`). To avoid this, create such instances using definitions such as `decidable_of_iff` instead.
## Examples
Proving inequalities:

```
example : 2 + 2 ≠ 5 := by decide

```

Trying to prove a false proposition:

```
example : 1 ≠ 1 := by decide
/-
tactic 'decide' proved that the proposition
  1 ≠ 1
is false
-/

```

Trying to prove a proposition whose `Decidable` instance fails to reduce

```
opaque unknownProp : Prop

open scoped Classical in
example : unknownProp := by decide
/-
tactic 'decide' failed for proposition
  unknownProp
since its 'Decidable' instance reduced to
  Classical.choice ⋯
rather than to the 'isTrue' constructor.
-/

```

## Properties and relations
For equality goals for types with decidable equality, usually `rfl` can be used in place of `decide`.

```
example : 1 + 1 = 2 := by decide
example : 1 + 1 = 2 := by rfl

```

`[` +native`](Tactic-Proofs/Tactic-Reference/#decide) or direct use of `Lean.ofReduceBool`) can be used to create invalid proofs whenever the native evaluation of a term disagrees with the kernel's evaluation. In particular, for every `implemented_by`/`extern` attribute in libraries it becomes part of the trusted code base that the replacement is semantically equivalent.
All these uses show up as an axiom `Lean.trustCompiler` in ``Lean.Parser.Command.printAxioms : command``[`#print axioms`](Interacting-with-Lean/#Lean___Parser___Command___printAxioms). External checkers (`lean4checker`, `comparator`) cannot check such proofs, as they do not have access to the Lean compiler. When that level of checking is needed, proofs have to avoid using native evaluation. 
[←24.2. Managing Toolchains with Elan](Build-Tools-and-Distribution/Managing-Toolchains-with-Elan/#elan "24.2. Managing Toolchains with Elan")[Error Explanations→](Error-Explanations/#The-Lean-Language-Reference--Error-Explanations "Error Explanations")
